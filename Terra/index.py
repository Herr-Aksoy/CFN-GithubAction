import boto3
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def handler(event, context):
    region = 'us-east-1'  # Buraya Load Balancer'ın bulunduğu bölgeyi yazın
    elb_client = boto3.client('elb', region_name=region)
    route53_client = boto3.client('route53', region_name=region)

    # Etiket adı ve değeri
    target_tag_key = 'kubernetes.io/service-name'
    target_tag_value = 'argocd/argocd-server'

    # Describe Load Balancers
    response = elb_client.describe_load_balancers()
    logger.info(f"Found {len(response['LoadBalancerDescriptions'])} Load Balancers")

    # Filter Load Balancer by tags
    load_balancer_dns_name = None
    for lb in response['LoadBalancerDescriptions']:
        lb_name = lb['LoadBalancerName']
        logger.info(f"Checking Load Balancer: {lb_name}")
        
        # Get tags for the Load Balancer
        tags = elb_client.describe_tags(LoadBalancerNames=[lb_name])
        
        # Check if the Load Balancer has the target tag
        for tag in tags['TagDescriptions'][0]['Tags']:
            logger.info(f"Found tag: {tag['Key']} = {tag['Value']}")
            if tag['Key'] == target_tag_key and tag['Value'] == target_tag_value:
                load_balancer_dns_name = lb['DNSName']
                logger.info(f"Found target Load Balancer with DNS Name: {load_balancer_dns_name}")
                break

        if load_balancer_dns_name:
            break

    if not load_balancer_dns_name:
        logger.error(f"No Load Balancer found with the tag {target_tag_key} = {target_tag_value}")
        raise Exception(f"No Load Balancer found with the tag {target_tag_key} = {target_tag_value}")

    logger.info(f"Load Balancer DNS Name: {load_balancer_dns_name}")

    # Get Route 53 hosted zone ID (use your specific hosted zone)
    hosted_zones = route53_client.list_hosted_zones_by_name(DNSName="awspublic.link.")
    hosted_zone_id = hosted_zones['HostedZones'][0]['Id']
    logger.info(f"Hosted Zone ID: {hosted_zone_id}")

    # Correct Hosted Zone ID for CLB in us-east-1
    elb_hosted_zone_id = 'Z3DZXE0Q79N41H'

    # Create Route 53 record
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': 'argocd.awspublic.link.',  # Sonundaki nokta eklendi
                        'Type': 'A',
                        'AliasTarget': {
                            'HostedZoneId': elb_hosted_zone_id,
                            'DNSName': load_balancer_dns_name,
                            'EvaluateTargetHealth': False
                        }
                    }
                }
            ]
        }
    )

    logger.info(f"Route 53 Record Created: {response}")

    return {
        'statusCode': 200,
        'body': json.dumps('Record created successfully')
    }
