## Project Owners
<table>
  <tr>
    <td><img src="project-images/readme-images/AhmetAksoy.png" alt="Ahmet Aksoy" width="250"></td>
    <td><img src="project-images/readme-images/MehmetSever.png" alt="Mehmet Sever" width="250"></td>
  </tr>
    <tr>
    <td><a href="" align="center">---------->Ahmet Aksoy<---------</a></td>
    <td><a href="" align="center">---------->Mehmet Sever<---------</a></td>
  </tr>
  <tr>
  <td align="center" style="width: 67%;">
    <a href="https://github.com/Herr-Aksoy">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40' title='Github Profile'>
    </a>
    <a href="https://www.linkedin.com/in/aksoy-ahmet/">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40' title='Linkedin Profile'>
    </a>
    <a href="https://www.instagram.com/updated_devops?igsh=N3kxOWMwdDhsaTZl">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg' alt='instagram' height='40' title='Instagram Profile'>
    </a>
    <a href="https://www.xing.com/profile/Ahmet_Aksoy68/web_profiles?expandNeffi=true">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/xing.svg' alt='xing' height='40' title='Xing Profile'>
    </a>
  </td>                                       <!--Mehmet Sever abi burdan asagi kisim senin-->
    <td align="center" style="width: 67%;">
    <a href="https://github.com/cemalsenel">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40' title='Github Profile'>
    </a>
    <a href="https://www.linkedin.com/in/mehmet8sever/">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40' title='Linkedin Profile'>
    <!-- </a>
    <a href="https://www.instagram.com/updated_devops?igsh=N3kxOWMwdDhsaTZl">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg' alt='instagram' height='40' title='Instagram Profile'>
    </a>
    <a href="https://www.xing.com/profile/Ahmet_Aksoy68/web_profiles?expandNeffi=true">
      <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/xing.svg' alt='xing' height='40' title='Xing Profile'>
    </a> -->
  </td>
</tr>
</table>


<p align="center"><strong>AWS-EKS Infrastructure</strong></p>
<p align="center">
  <img src="https://github.com/Herr-Aksoy/CFN-GithubAction/blob/main/AWS-Eks/images/AWS-Eks-CludFormation.gif" width="700" height="900"/>  
</p>




# CloudFormation Template for Creating EKS Cluster and Node Group
This CloudFormation template creates an Elastic Kubernetes Service (EKS) cluster and associated Node Group on AWS. It also provisions the required network infrastructure and IAM roles. Below is a detailed description of each resource, its type, and purpose.

## Resources
### 1. EksVpc
- **Type:** AWS::EC2::VPC
- **Description:** Creates a Virtual Private Cloud (VPC) which provides a network environment for the EKS cluster.
- **Purpose:** To establish an isolated network environment where the EKS cluster will operate.
### 2. EksVpcIgw
- **Type:** AWS::EC2::InternetGateway
- **Description:** Creates an Internet Gateway to enable internet access for the VPC.
- **Purpose:** To allow resources within the VPC to access the internet.
### 3. VpcGatewayAttachment
- **Type:** AWS::EC2::VPCGatewayAttachment
- **Description:** Attaches the Internet Gateway to the VPC.
- **Purpose:** To link the Internet Gateway with the VPC for internet connectivity.
### 4. PublicSubnetUsEast1a
- **Type:** AWS::EC2::Subnet
- **Description:** Creates a public subnet in the 'us-east-1a' Availability Zone.
- **Purpose:** To provide a network segment for the EKS cluster and other public-facing services.
### 5. PublicSubnetUsEast1b
- **Type:** AWS::EC2::Subnet
- **Description:** Creates a public subnet in the 'us-east-1b' Availability Zone.
- **Purpose:** To provide a network segment for the EKS cluster and other public-facing services.
### 6. PublicRouteTable
- **Type:** AWS::EC2::RouteTable
- **Description:** Creates a route table for public subnets.
- **Purpose:** To define routing rules for public subnets, including internet access.
### 7. PublicRoute
- **Type:** AWS::EC2::Route
- **Description:** Defines a route for public subnets to access the internet (0.0.0.0/0).
- **Purpose:** To enable internet access for resources in public subnets.
### 8. PublicSubnetRouteTableAssociationUsEast1a
- **Type:** AWS::EC2::SubnetRouteTableAssociation
- **Description:** Associates the 'us-east-1a' public subnet with the route table.
- **Purpose:** To ensure that the 'us-east-1a' public subnet has internet access through the route table.
### 9. PublicSubnetRouteTableAssociationUsEast1b
- **Type:** AWS::EC2::SubnetRouteTableAssociation
- **Description:** Associates the 'us-east-1b' public subnet with the route table.
- **Purpose:** To ensure that the 'us-east-1b' public subnet has internet access through the route table.
### 10. EksRole
- **Type:** AWS::IAM::Role
- **Description:** Creates an IAM role for the EKS cluster with the necessary permissions.
- **Purpose:** To grant the EKS cluster the required permissions to access AWS resources.
### 11. EksCluster
- **Type:** AWS::EKS::Cluster
- **Description:** Creates an EKS cluster configured to run within the specified VPC.
- **Purpose:** To provide a managed Kubernetes cluster for running containerized applications.
### 12. EksNodeRole
- **Type:** AWS::IAM::Role
- **Description:** Creates an IAM role for the EKS Node Group's EC2 instances with necessary permissions.
- **Purpose:** To allow EC2 instances in the EKS Node Group to interact with AWS services.
### 13. EksNodeGroup
- **Type:** AWS::EKS::Nodegroup
- **Description:** Creates a Node Group within the EKS cluster, specifying the desired EC2 instance types and scaling configuration.
- **Purpose:** To provide a group of EC2 instances that will run workloads within the EKS cluster.



<table align="center">
  <tr>
    <td><img src="images/a1-components.png" alt="Components" width="350"></td>
    <td><img src="images/a2-resources.png" alt="Resources" width="350"></td>
  </tr>
  <tr>
    <td align="center"><a  title="Settings">Components</a></td>
    <td align="center"><a  title="Settings">Resources</a></td>
  </tr>
</table>


# GitHub Actions Workflow for Deploying EKS Cluster and Setting Up Argo CD
This GitHub Actions workflow automates the deployment of an Amazon EKS cluster using CloudFormation and sets up Argo CD on the newly created EKS cluster. Below is a detailed description of each job and step in the workflow.

## Workflow Overview
The workflow is triggered manually via the GitHub Actions interface. It consists of two main jobs:

**a. Deploy EKS Cluster:**<a href="https://github.com/Herr-Aksoy/CFN-GithubAction/tree/main/AWS-Eks#a--deploy-eks-cluster-job:~:text=a%2D%20%27deploy%2Deks%2Dcluster%27%20Job" title="More information">Deploys an EKS cluster using AWS CloudFormation.</a>


**b. Setup Argo CD:** <a href="https://github.com/Herr-Aksoy/CFN-GithubAction/tree/main/AWS-Eks#a--deploy-eks-cluster-job:~:text=b%2D%20%27setup%2Dargocd%27%20Job" title="More information">Sets up Argo CD on the deployed EKS cluster.</a> 

**c. Deploy Lambda CloudFormation Stack:** <a href="https://github.com/Herr-Aksoy/CFN-GithubAction/tree/main/AWS-Eks#a--deploy-eks-cluster-job:~:text=c%2D%20%27deploy%2Dlambda%2Dcfn%27%20Job" title="More information">Deploys a CloudFormation stack to create a Lambda function.</a>

**d. Delete Lambda CloudFormation Stack:** <a href="https://github.com/Herr-Aksoy/CFN-GithubAction/tree/main/AWS-Eks#a--deploy-eks-cluster-job:~:text=d%2D%20delete%2Dlambda%2Dcfn%20Job" title="More information">Deletes the previously created Lambda CloudFormation stack.</a>  

## Workflow Definition

## a- 'deploy-eks-cluster' Job

**Purpose:** Deploys an EKS cluster using a CloudFormation stack.

**Steps:**

### 1. Checkout Repository

- **Description:** Checks out the code from the repository so that the workflow can access the CloudFormation template.
- **Action:** actions/checkout@v2
### 2. Configure AWS Credentials

- **Description:** Configures AWS credentials required for deploying the CloudFormation stack.
- **Action:** aws-actions/configure-aws-credentials@v2
- **Inputs:**
  - **aws-access-key-id:** AWS access key ID stored in GitHub Secrets.
  - **aws-secret-access-key:** AWS secret access key stored in GitHub Secrets.
  - **aws-region:** AWS region where the resources will be deployed (us-east-1).
### 3. Deploy CloudFormation Stack

- **Description:** Deploys the CloudFormation stack to create the EKS cluster and related resources.
- **Command:**
```sh
aws cloudformation deploy \
  --stack-name eks-cluster-stack \
  --template-file ./eks-temel.yaml \
  --capabilities CAPABILITY_NAMED_IAM
```

## b- 'setup-argocd' Job
**Purpose:** Sets up Argo CD on the EKS cluster created in the previous job.

**Dependencies:** This job depends on the successful completion of the deploy-eks-cluster job.

**Steps:**

### 1. Checkout Code

- **Description:** Checks out the code from the repository to access additional files if necessary.
- **Action:** actions/checkout@v2
### 2. Configure AWS Credentials

- **Description:** Configures AWS credentials required for interacting with the EKS cluster.
- **Action:** aws-actions/configure-aws-credentials@v2
- **Inputs:**
  - **aws-access-key-id:** AWS access key ID stored in GitHub Secrets.
  - **aws-secret-access-key:** AWS secret access key stored in GitHub Secrets.
  - **aws-region:** AWS region where the EKS cluster is located (us-east-1).
### 3. Setup kubectl

- **Description:** Installs kubectl, the command-line tool for interacting with Kubernetes clusters.
- **Command:**
```sh
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

### 4. Update kubeconfig

- **Description:** Configures kubectl to use the newly created EKS cluster.
- **Command:**
```sh
aws eks --region us-east-1 update-kubeconfig --name eks-cluster
```
### 5. Install Argo CD

- **Description:** Deploys Argo CD to the EKS cluster and exposes it via a LoadBalancer service.
- **Command:**
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```
<br><br>

# CloudFormation Template: Route 53 Record Creation for EKS Classic Load Balancer using Lambda
This CloudFormation template automates the creation of a Route 53 DNS record for an existing Elastic Kubernetes Service (EKS) Classic Load Balancer (CLB) using an AWS Lambda function. Below is a detailed description of the resources defined in this template and their purposes.

## Description
The template consists of the following key components:

1. IAM Role for Lambda Execution
2. Lambda Function to Find and Create DNS Record
3. Permission for Lambda Invocation
4. Custom Resource to Trigger Lambda

## Resources

### 1. IAM Role for Lambda Execution

**Resource:** LambdaExecutionRole

**Purpose:** Defines an IAM Role that grants the necessary permissions for the Lambda function to interact with AWS services.

**Details:**

- **Service:** lambda.amazonaws.com is allowed to assume this role.
- **Policies:**
    - Allows describing load balancers and their tags.
    - Allows changing and listing Route 53 resource record sets and hosted zones.

## 2. Lambda Function to Find and Create DNS Record

**Resource:** FindAndCreateRecordFunction

**Purpose:** A Lambda function that identifies the target CLB based on specific tags and creates a corresponding DNS record in Route 53.

**Code Functionality:**

- Uses the AWS SDK for Python (boto3) to interact with ELB and Route 53 services.
- Looks for a CLB with the tag kubernetes.io/service-name set to argocd/argocd-server.
- Upon finding the CLB, it creates an A record in Route 53 pointing to the CLB's DNS name.

## 3. Permission for Lambda Invocation

**Resource:** LambdaInvokePermission

**Purpose:** Grants permission to AWS events to invoke the Lambda function.

**Details:**

- **Action:** lambda:InvokeFunction
- **Principal:** events.amazonaws.com

## 4. Custom Resource to Trigger Lambda

**Resource:** CustomResourceTrigger

**Purpose:** A custom resource that triggers the Lambda function during the CloudFormation stack creation process.

**Details:**

- **ServiceToken:** The ARN of the Lambda function.

<br><br>

# Workflow Definition continued

## c- 'deploy-lambda-cfn' Job 

**Purpose:** Deploys a CloudFormation stack to create a Lambda function.

**Steps:**

### 1. Checkout Repository
- **Description:** Checks out the code from the repository.
- **Action:** actions/checkout@v2

### 2. Configure AWS Credentials
- **Description:** Configures AWS credentials required for deploying the CloudFormation stack.
- **Action:** aws-actions/configure-aws-credentials@v2
- **Inputs:**
  - 'aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}'
  - 'aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}'
  - 'aws-region: us-east-1'

### 3. Deploy CloudFormation Stack
- **Description:** Deploys the CloudFormation stack defined in lambda-cfn.yaml to create a Lambda function.
- **Command:**

```sh
aws cloudformation deploy \
  --stack-name lambdaFunction \
  --template-file ./lambda-cfn.yaml \
  --capabilities CAPABILITY_NAMED_IAM
```

## d- delete-lambda-cfn Job
**Purpose:** Deletes the previously created Lambda CloudFormation stack.

**Dependencies:** This job requires both setup-argocd and deploy-lambda-cfn to be completed successfully.

**Steps:**

### 1. Checkout Repository
- **Description:** Checks out the code from the repository.
- **Action:** actions/checkout@v2

### 2. Configure AWS Credentials
- **Description:** Configures AWS credentials required for deleting the CloudFormation stack.
- **Action:** aws-actions/configure-aws-credentials@v2
- **Inputs:**
  - 'aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}'
  - 'aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}'
  - 'aws-region: us-east-1'

### 3. Delete CloudFormation Stack
- **Description:** Deletes the CloudFormation stack named lambdaFunction.
- **Command:** 
```sh
aws cloudformation delete-stack \
  --stack-name lambdaFunction
```
### 4. Wait for Stack Deletion to Complete
- **Description:** Waits for the stack deletion process to complete.
- **Command:**
```sh
aws cloudformation wait stack-delete-complete \
  --stack-name lambdaFunction
```