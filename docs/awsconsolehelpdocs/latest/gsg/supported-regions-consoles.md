

# Supported AWS Regions, service consoles, and features in Private Access
<a name="supported-regions-consoles"></a>

AWS Management Console Private Access is available in all commercial AWS Regions but supports only a subset of AWS service consoles. In addition, certain AWS Management Console features might be disabled when using AWS Management Console Private Access, for example, AWS CloudShell and the [Default Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html) setting.

**Note**  
To help users avoid errors from navigating to unsupported AWS Regions or service consoles, account administrators can configure which Regions and service consoles are visible. For more information, see [AWS User Experience Customization (UXC)](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/uxc.html).

The following service consoles are fully supported or provide graceful degradation of features. You can still navigate to other consoles, but will require internet connectivity with missing AWS PrivateLink support for AWS services or unsupported console-only APIs.

**Supported service consoles**
+ AWS Auto Scaling
+ AWS Certificate Manager
+ AWS CloudFormation
+ AWS CloudTrail
+ AWS Database Migration Service
+ AWS Directory Service
+ AWS Glue
+ AWS Glue DataBrew
+ AWS Identity and Access Management
+ AWS Key Management Service
+ AWS Lambda
+ AWS Network Firewall
+ AWS Organizations
+ AWS Private Certificate Authority
+ AWS Resource Access Manager
+ AWS Resource Groups
+ AWS Security Hub
+ AWS Service Catalog
+ AWS Step Functions
+ AWS Systems Manager
+ AWS WAF
+ Amazon API Gateway
+ Amazon Athena
+ Amazon CloudWatch
+ Amazon DynamoDB
+ Amazon EMR
+ Amazon Elastic Compute Cloud
+ Amazon Elastic Container Registry
+ Amazon Elastic Container Service
+ Amazon Elastic File System
+ Amazon Elastic Kubernetes Service
+ Amazon GuardDuty
+ Amazon Kinesis
+ Amazon Kinesis Video Streams
+ Amazon Managed Streaming for Apache Kafka
+ Amazon OpenSearch Service
+ Amazon Rekognition
+ Amazon Relational Database Service
+ Amazon Route 53 Resolver
+ Amazon Route 53
+ Amazon SageMaker
+ Amazon SageMaker AI
+ Amazon Simple Queue Service
+ Amazon Simple Storage Service
+ Amazon Virtual Private Cloud
+ Amazon WorkSpaces

**Note**  
The AWS Billing console is not available through AWS Management Console Private Access, even with internet connectivity. To access billing information, sign in to the AWS Management Console outside of AWS Management Console Private Access.