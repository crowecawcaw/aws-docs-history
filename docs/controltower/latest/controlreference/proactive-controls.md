# Proactive controls

These controls are referred to as _proactive_ because
they check your resources – before the resources are deployed – to determine
whether the new resources will comply with the controls that are activated in your
environment.

Proactive controls are _optional controls_ implemented
with [AWS CloudFormation
hooks](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md") and [hooks managed by AWS Control Tower](update-hooks.md "update-hooks.md").

Proactive controls fall into four main
**Categories**. In the AWS Control Tower console, you can view the controls in groups according to their assigned
categories, which are:

- **Control objectives**: Specific purposes for implementing
  controls in your environment.
- **Frameworks**: Industry-standard compliance frameworks.
- **Services**: The AWS services that the control may
  govern.
- **Groups**: Groups of controls designed to help you meet a specific policy standard.
  In this reference guide, the proactive controls are categorized according to their
  associated AWS services.

**Behavior of proactive controls**

Proactive controls check resources whenever those resources are created or updated by
means of AWS CloudFormation stack operations. Specifically, these proactive controls are implemented as
`preCreate` and `preUpdate` hook handlers. As a consequence,
these controls may not affect requests that are made directly to services through the AWS
console, through AWS APIs, or through other means such as AWS SDKs, or other
Infrastructure-as-Code (IaC) tools. For more information about when `preCreate`
and `preUpdate` hooks operate, see [AWS CloudFormation
hooks](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md").

###### Limitation of hooks managed by AWS CloudFormation

Proactive controls evaluate strings passed into the AWS CloudFormation hook within the
`targetNames` property. Secure strings and secrets are not resolved
before they are sent to the hook, which prevents the proactive control from evaluating
the string. For more information about how the `targetNames` are passed to
hooks, see [AWS CloudFormation Hooks
structure overview](../../../cloudformation-cli/latest/hooks-userguide/hooks-structure.md "../../../cloudformation-cli/latest/hooks-userguide/hooks-structure.md").

When you follow an example template to set up a test for a proactive control in your
environment, be aware that the template is created to test one specific control only. Other
controls may not receive a PASS rating for that template. This behavior is expected. We
recommend that you test proactive controls individually before you enable them in your
environment.

###### Topics

- [Amazon API Gateway controls](api-gateway-rules.md "api-gateway-rules.md")
- [AWS Certificate Manager controls](acm-rules.md "acm-rules.md")
- [AWS AppSync controls](appsync-rules.md "appsync-rules.md")
- [Amazon Athena controls](athena-rules.md "athena-rules.md")
- [Amazon CloudFront controls](cloudfront-rules.md "cloudfront-rules.md")
- [AWS CloudTrail controls](cloudtrail-rules.md "cloudtrail-rules.md")
- [Amazon CloudWatch controls](cloudwatch-rules.md "cloudwatch-rules.md")
- [AWS CodeBuild controls](codebuild-rules.md "codebuild-rules.md")
- [AWS Database Migration Service (AWS DMS) controls](dms-rules.md "dms-rules.md")
- [Amazon DocumentDB controls](documentdb-rules.md "documentdb-rules.md")
- [Amazon DynamoDB controls](dynamodb-rules.md "dynamodb-rules.md")
- [DynamoDB Accelerator controls](dax-rules.md "dax-rules.md")
- [AWS Elastic Beanstalk controls](ebs-rules.md "ebs-rules.md")
- [Amazon Elastic Compute Cloud (Amazon EC2) controls](ec2-rules.md "ec2-rules.md")
- [Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling controls](ec2-auto-scaling-rules.md "ec2-auto-scaling-rules.md")
- [Amazon ElastiCache controls](elasticache-rules.md "elasticache-rules.md")
- [Amazon Elastic Container Registry controls](ecr-rules.md "ecr-rules.md")
- [Amazon Elastic Container Service controls](ecs-rules.md "ecs-rules.md")
- [Amazon Elastic File System controls](efs-rules.md "efs-rules.md")
- [Amazon Elastic Kubernetes Service (EKS) controls](eks-rules.md "eks-rules.md")
- [Elastic Load Balancing controls](elb-rules.md "elb-rules.md")
- [Amazon Elastic Map Reduce (Amazon EMR) controls](emr-rules.md "emr-rules.md")
- [AWS Glue controls](glue-rules.md "glue-rules.md")
- [Amazon GuardDuty controls](guard-duty-rules.md "guard-duty-rules.md")
- [AWS Identity and Access Management (IAM) controls](iam-rules.md "iam-rules.md")
- [AWS Key Management Service (AWS KMS) controls](kms-rules.md "kms-rules.md")
- [Amazon Kinesis controls](kinesis-rules.md "kinesis-rules.md")
- [AWS Lambda controls](lambda-rules.md "lambda-rules.md")
- [Amazon MQ controls](mq-rules.md "mq-rules.md")
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK) controls](msk-rules.md "msk-rules.md")
- [Amazon Neptune controls](neptune-rules.md "neptune-rules.md")
- [AWS Network Firewall controls](network-firewall-rules.md "network-firewall-rules.md")
- [Amazon OpenSearch controls](opensearch-rules.md "opensearch-rules.md")
- [Amazon Relational Database Service (Amazon RDS) controls](rds-rules.md "rds-rules.md")
- [Amazon Redshift controls](redshift-rules.md "redshift-rules.md")
- [Amazon Simple Storage Service (Amazon S3) controls](s3-rules.md "s3-rules.md")
- [Amazon SageMaker AI controls](sagemaker-rules.md "sagemaker-rules.md")
- [Amazon Simple Queue Service (Amazon SQS) controls](sqs-rules.md "sqs-rules.md")
- [AWS Step Functions controls](stepfunctions-rules.md "stepfunctions-rules.md")
- [AWS WAF regional controls](waf-regional-rules.md "waf-regional-rules.md")
- [AWS WAF controls](waf-rules.md "waf-rules.md")
- [AWS WAFV2 controls](wafv2-rules.md "wafv2-rules.md")
