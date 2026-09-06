

# Plan your deployment
<a name="plan-your-deployment"></a>

This section contains information on cost, security, supported regions, and quotas that can help you plan your deployment of Research and Engineering Studio on AWS.

## Cost
<a name="plan-your-deployment-cost"></a>

Research and Engineering Studio on AWS is available at no additional charge, and you pay only for the AWS resources needed to run your applications. For more information, see [AWS services in this product](architecture-overview.md#aws-services-in-this-product).

**Note**  
You are responsible for the cost of the AWS services used while running this product.  
As a best practice, create a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this product. 

## Security
<a name="plan-your-deployment-security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) .  To learn about the compliance programs that apply to Research and Engineering Studio on AWS, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) .  
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

To understand how to apply the shared responsibility model with the AWS services used by Research and Engineering Studio, see [Security considerations for services in this product](#plan-your-deployment-security-links). For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

### IAM roles
<a name="plan-your-deployment-iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This product creates IAM roles that grant the product’s AWS Lambda functions and Amazon EC2 instances access to create Regional resources.

RES supports identity-based policies within IAM. When deployed, RES creates policies to define the administrator permission and access. The administrator who implements the product creates and manages end users and project leaders within the existing customer Active Directory integrated with RES. For more information, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *AWS Identity and Access Management User Guide*.

Your organization's administrator can manage user access with an active directory. When end users access the RES user interface, RES authenticates with [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html).

### Security groups
<a name="plan-your-deployment-security-groups"></a>

The security groups created in this product are designed to control and isolate network traffic between the Lambda functions, Amazon EC2 instances, file systems, and remote VPN endpoints. Review the security groups and further restrict access as needed after the product is deployed. 

### Data encryption
<a name="plan-your-deployment-data-encryption"></a>

By default, Research and Engineering Studio on AWS (RES) encrypts customer data at rest and in transit using an RES-owned key. When you deploy RES, you may specify an AWS KMS key. RES uses your credentials to grant key access. If you supply a customer owned and managed AWS KMS key, customer data at rest will be encrypted using that key. 

RES encrypts customer data in transit using SSL/TLS. TLS 1.2 is required, but TLS 1.3 is recommended. 

### Security considerations for services in this product
<a name="plan-your-deployment-security-links"></a>

For more detailed information regarding security considerations for the services used by Research and Engineering Studio, follow the links in this table:


| AWS service security info | Service type | How the service is used in RES | 
| --- | --- | --- | 
| [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html) | Core | Provides the underlying compute services to create virtual desktops with their chosen operating system and software stack. | 
| [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security.html) | Core | Bastion, cluster-manager, and VDI hosts are created in Auto Scaling groups behind the load balancer. Elastic Load Balancing balances traffic from the web portal across RES hosts. | 
| [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/security.html) | Core | All core product components are created within your VPC. | 
| [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/security.html) | Core | Manages user identities and authentication. Active Directory users are mapped to Amazon Cognito users and groups to authenticate access levels. | 
| [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html) | Core | Provides the /home file system for the file browser and VDI hosts, as well as shared external file systems. | 
| [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html) | Core | Stores configuration data such as users, groups, projects, file systems, and component settings. | 
| [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/security.html) | Core | Stores documents for performing commands for VDI session management. | 
| [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html) | Core | Supports product functionalities such as updating settings within the DynamoDB table, starting Active Directory sync workflows, and updating the prefix list. | 
| [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security.html) | Supporting | Provides metrics and activity logs for all Amazon EC2 hosts and Lambda functions. | 
| [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html) | Supporting | Stores application binaries for host bootstrapping and configuration. | 
| [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-security.html) | Supporting | Used for encryption at rest with Amazon SQS queues, DynamoDB tables, and Amazon SNS topics. | 
| [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html) | Supporting | Stores service account credentials in Active Directory and self-signed certificates for VDIs. | 
| [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security.html) | Supporting | Provides a deployment mechanism for the product.  | 
| [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/security.html) | Supporting | Restricts the access level for hosts. | 
| [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/security.html) | Supporting | Creates private hosted zone for resolving the internal load balancer and the bastion host domain name.  | 
| [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security.html) | Supporting | Creates task queues to support asynchronous executions. | 
| [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/sns-security.html) | Supporting | Supports the publish-subscribe model between VDI components such as the controller and hosts. | 
| [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-fargate.html) | Supporting | Installs, updates, and deletes environments using Fargate tasks. | 
| [Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security.html) | Optional | Provides external shared file system. | 
| [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security.html) | Optional | Provides external shared file system. | 
| [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/security.html) | Optional | Generates a trusted certificate for your custom domain. | 
| [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html) | Optional | Offers backup capabilities for Amazon EC2 hosts, file systems, and DynamoDB. | 

## Quotas
<a name="plan-your-deployment-quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

### Quotas for AWS services in this product
<a name="quotas-for-aws-services-in-this-product"></a>

Make sure you have sufficient quota for each of the [ services implemented in this product](architecture-overview.md#aws-services-in-this-product). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

As a best practice, raise quotas for the following services:
+ Amazon Virtual Private Cloud
+ Amazon EC2

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

### AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](launch-the-product.md) in this product. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this product successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*. 

### Planning for resilience
<a name="planning-for-resilience"></a>

The product deploys a default infrastructure with the minimum number and size of Amazon EC2 instances to operate the system. To improve resilience in large-scale production environments, as a best practice, increase the default minimum capacity settings within the infrastructure's Auto Scaling groups (ASG). Increasing the value from one instance to two instances provides the benefit of multiple Availability Zones (AZ) and reduces the time to restore system functionality in the event of unexpected data loss. 

ASG settings can be customized within the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/). The product creates four ASGs by default with each name ending with `-asg`. You can change the minimum and desired values to an amount appropriate for your production environment. Select the group you want to modify, and then choose **Actions** and select **Edit**. For more information on ASGs, see [Scale the size of your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Supported AWS Regions
<a name="plan-your-deployment-supported-aws-regions"></a>

This product uses services which are not currently available in all AWS Regions. You must launch this product in an AWS Region where all services are available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). 

Research and Engineering Studio on AWS is supported in the following AWS Regions: 


| Region name | Region | Previous versions | Latest version (2026.06) | 
| --- | --- | --- | --- | 
| US East (N. Virginia)  | us-east-1 | yes | yes | 
| US East (Ohio)  | us-east-2 | yes | yes | 
| US West (N. California)  | us-west-1 | yes | yes | 
| US West (Oregon)  | us-west-2 | yes | yes | 
| Asia Pacific (Tokyo) | ap-northeast-1 | yes | yes | 
| Asia Pacific (Seoul) | ap-northeast-2 | yes | yes | 
| Asia Pacific (Osaka) | ap-northeast-3 | yes | yes | 
| Asia Pacific (Mumbai) | ap-south-1 | yes | yes | 
| Asia Pacific (Singapore)  | ap-southeast-1 | yes | yes | 
| Asia Pacific (Sydney)  | ap-southeast-2 | yes | yes | 
| Asia Pacific (Jakarta)  | ap-southeast-3 | yes | yes | 
| Canada (Central) | ca-central-1 | yes | yes | 
| Europe (Frankfurt) | eu-central-1 | yes | yes | 
| Europe (Milan) | eu-south-1 | yes | yes | 
| Europe (Ireland) | eu-west-1 | yes | yes | 
| Europe (London)  | eu-west-2 | yes | yes | 
| Europe (Paris)  | eu-west-3 | yes | yes | 
| Europe (Stockholm)  | eu-north-1 | yes | yes | 
| Israel (Tel Aviv) | il-central-1 | yes | yes | 
| Middle East (UAE) | me-central-1 | yes | yes | 
| South America (São Paulo) | sa-east-1 | yes | yes | 
| AWS GovCloud (US-East) | us-gov-east-1 | yes | yes | 
| AWS GovCloud (US-West) | us-gov-west-1 | yes | yes | 