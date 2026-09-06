

# Proactive controls
<a name="proactive-controls"></a>

These controls are referred to as *proactive* because they check your resources – before the resources are deployed – to determine whether the new resources will comply with the controls that are activated in your environment.

Proactive controls are *optional controls* implemented with [CloudFormation hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) and [hooks managed by AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/update-hooks.html). 

Proactive controls fall into four main **Categories**. In the AWS Control Tower console, you can view the controls in groups according to their assigned categories, which are: 
+ **Control objectives**: Specific purposes for implementing controls in your environment. 
+ **Frameworks**: Industry-standard compliance frameworks.
+ **Services**: The AWS services that the control may govern.
+ **Groups**: Groups of controls designed to help you meet a specific policy standard.

In this reference guide, the proactive controls are categorized according to their associated AWS services.

 **Behavior of proactive controls**

Proactive controls check resources whenever those resources are created or updated by means of CloudFormation stack operations. Specifically, these proactive controls are implemented as `preCreate` and `preUpdate` hook handlers. As a consequence, these controls may not affect requests that are made directly to services through the AWS console, through AWS APIs, or through other means such as AWS SDKs, or other Infrastructure-as-Code (IaC) tools. For more information about when `preCreate` and `preUpdate` hooks operate, see [CloudFormation hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html).

**Limitation of hooks managed by CloudFormation**  
Proactive controls evaluate strings passed into the CloudFormation hook within the `targetNames` property. Secure strings and secrets are not resolved before they are sent to the hook, which prevents the proactive control from evaluating the string. For more information about how the `targetNames` are passed to hooks, see [CloudFormation Hooks structure overview](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-structure.html).

When you follow an example template to set up a test for a proactive control in your environment, be aware that the template is created to test one specific control only. Other controls may not receive a PASS rating for that template. This behavior is expected. We recommend that you test proactive controls individually before you enable them in your environment.

**Topics**
+ [Update your proactive control hooks](get-new-hooks.md)
+ [Amazon API Gateway controls](api-gateway-rules.md)
+ [AWS Certificate Manager controls](acm-rules.md)
+ [AWS AppSync controls](appsync-rules.md)
+ [Amazon Athena controls](athena-rules.md)
+ [Amazon CloudFront controls](cloudfront-rules.md)
+ [AWS CloudTrail controls](cloudtrail-rules.md)
+ [Amazon CloudWatch controls](cloudwatch-rules.md)
+ [AWS CodeBuild controls](codebuild-rules.md)
+ [AWS Database Migration Service (AWS DMS) controls](dms-rules.md)
+ [Amazon DocumentDB controls](documentdb-rules.md)
+ [Amazon DynamoDB controls](dynamodb-rules.md)
+ [DynamoDB Accelerator controls](dax-rules.md)
+ [AWS Elastic Beanstalk controls](ebs-rules.md)
+ [Amazon Elastic Compute Cloud (Amazon EC2) controls](ec2-rules.md)
+ [Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling controls](ec2-auto-scaling-rules.md)
+ [Amazon ElastiCache controls](elasticache-rules.md)
+ [Amazon Elastic Container Registry controls](ecr-rules.md)
+ [Amazon Elastic Container Service controls](ecs-rules.md)
+ [Amazon Elastic File System controls](efs-rules.md)
+ [Amazon Elastic Kubernetes Service (EKS) controls](eks-rules.md)
+ [Elastic Load Balancing controls](elb-rules.md)
+ [Amazon Elastic Map Reduce (Amazon EMR) controls](emr-rules.md)
+ [AWS Glue controls](glue-rules.md)
+ [Amazon GuardDuty controls](guard-duty-rules.md)
+ [AWS Identity and Access Management (IAM) controls](iam-rules.md)
+ [AWS Key Management Service (AWS KMS) controls](kms-rules.md)
+ [Amazon Kinesis controls](kinesis-rules.md)
+ [AWS Lambda controls](lambda-rules.md)
+ [Amazon MQ controls](mq-rules.md)
+ [Amazon Managed Streaming for Apache Kafka (Amazon MSK) controls](msk-rules.md)
+ [Amazon Neptune controls](neptune-rules.md)
+ [AWS Network Firewall controls](network-firewall-rules.md)
+ [Amazon OpenSearch controls](opensearch-rules.md)
+ [Amazon Relational Database Service (Amazon RDS) controls](rds-rules.md)
+ [Amazon Redshift controls](redshift-rules.md)
+ [Amazon Simple Storage Service (Amazon S3) controls](s3-rules.md)
+ [Amazon SageMaker AI controls](sagemaker-rules.md)
+ [Amazon Simple Queue Service (Amazon SQS) controls](sqs-rules.md)
+ [AWS Step Functions controls](stepfunctions-rules.md)
+ [AWS WAF regional controls](waf-regional-rules.md)
+ [AWS WAF controls](waf-rules.md)
+ [AWS WAFV2 controls](wafv2-rules.md)