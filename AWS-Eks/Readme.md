# CloudFormation Template for EKS VPC Setup

This repository contains an AWS CloudFormation template for setting up a VPC and its associated resources for an Amazon EKS cluster. The template creates a VPC, subnets, Internet Gateway, NAT Gateway, Route Tables, and Route Table Associations.

## Resources

### VPC
- **EksVpc**: An Amazon Virtual Private Cloud (VPC) with a CIDR block of `192.168.0.0/16`.

### Internet Gateway
- **EksVpcIgw**: An Internet Gateway to allow internet access to the VPC.
- **VpcGatewayAttachment**: Attaches the Internet Gateway to the VPC.

### Subnets
- **PrivateSubnetUsEast1a**: A private subnet in availability zone `us-east-1a` with a CIDR block of `192.168.0.0/19`.
- **PrivateSubnetUsEast1b**: A private subnet in availability zone `us-east-1b` with a CIDR block of `192.168.32.0/19`.
- **PublicSubnetUsEast1a**: A public subnet in availability zone `us-east-1a` with a CIDR block of `192.168.64.0/19`. Instances in this subnet can have public IP addresses.
- **PublicSubnetUsEast1b**: A public subnet in availability zone `us-east-1b` with a CIDR block of `192.168.96.0/19`. Instances in this subnet can have public IP addresses.

### Elastic IP
- **NatEip**: An Elastic IP for the NAT Gateway.

### NAT Gateway
- **NatGateway**: A NAT Gateway in the public subnet `PublicSubnetUsEast1a` to allow instances in the private subnets to access the internet.

### Route Tables
- **PrivateRouteTable**: A route table for the private subnets.
  - **PrivateRoute**: A route in the private route table that directs internet-bound traffic (`0.0.0.0/0`) to the NAT Gateway.
- **PublicRouteTable**: A route table for the public subnets.
  - **PublicRoute**: A route in the public route table that directs internet-bound traffic (`0.0.0.0/0`) to the Internet Gateway.

### Route Table Associations
- **PrivateSubnetRouteTableAssociationUsEast1a**: Associates the private subnet `PrivateSubnetUsEast1a` with the private route table.
- **PrivateSubnetRouteTableAssociationUsEast1b**: Associates the private subnet `PrivateSubnetUsEast1b` with the private route table.
- **PublicSubnetRouteTableAssociationUsEast1a**: Associates the public subnet `PublicSubnetUsEast1a` with the public route table.
- **PublicSubnetRouteTableAssociationUsEast1b**: Associates the public subnet `PublicSubnetUsEast1b` with the public route table.

## Usage

To use this CloudFormation template, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the AWS Management Console.
3. Go to the CloudFormation service.
4. Create a new stack by uploading the `template.yaml` file.
5. Follow the prompts to complete the stack creation.

## Notes

- Ensure that your AWS CLI is configured with the necessary permissions to create the resources defined in this template.
- Modify the availability zones and CIDR blocks as needed to fit your network design.

## License

This project is licensed under the MIT License.


<table align="center">
  <tr>
    <td><img src="images/a1-components.png" alt="Components" width="250"></td>
    <td><img src="images/a2-resources.png" alt="Resources" width="250"></td>
  </tr>
  <tr>
    <td align="center"><a  title="Settings">Components</a></td>
    <td align="center"><a  title="Settings">Resources</a></td>
  </tr>
</table>