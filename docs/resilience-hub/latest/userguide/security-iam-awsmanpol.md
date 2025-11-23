# AWS managed policies for AWS Resilience Hub

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWSResilienceHubAsssessmentExecutionPolicy

You can attach the `AWSResilienceHubAsssessmentExecutionPolicy` to your
IAM identities. While running an assessment, this policy grants access permissions to
other AWS services for executing assessments.

### Permission

details

This policy provides adequate permissions to publish alarms, AWS FIS and SOP
templates to your Amazon Simple Storage Service (Amazon S3) bucket. The Amazon S3 bucket name must start with
`aws-resilience-hub-artifacts-`. If you wish to publish to another
Amazon S3 bucket, you can do that while calling `CreateRecommendationTemplate`
API. For more information, see [CreateRecommendationTemplate](../APIReference/API_CreateRecommendationTemplate.md "../APIReference/API_CreateRecommendationTemplate.md").

This policy includes the following permissions:

- Amazon CloudWatch (CloudWatch) – Gets all the implemented alarms that you set up
  in Amazon CloudWatch to monitor the application. In addition, we use
  `cloudwatch:PutMetricData` to publish CloudWatch metrics for the
  resiliency score of the application in the `ResilienceHub`
  namespace.
- Amazon Data Lifecycle Manager – Gets and provides `Describe` permissions for
  Amazon Data Lifecycle Manager resources that are associated with your AWS account.
- Amazon DevOps Guru – Lists and provides `Describe` permissions
  for Amazon DevOps Guru resources that are associated with your AWS account.
- Amazon DocumentDB – Lists and provides `Describe`
  permissions for Amazon DocumentDB resources that are associated with your AWS
  account.
- Amazon DynamoDB (DynamoDB) – Lists and provides `Describe`
  permissions for Amazon DynamoDB resources that are associated with your AWS
  account.
- Amazon ElastiCache (ElastiCache) – Provides `Describe` permissions for
  ElastiCache resources that are associated with your AWS account.
- Amazon ElastiCache (Redis OSS) Serverless (ElastiCache (Redis OSS) Serverless) – Provides `Describe`
  permissions for ElastiCache (Redis OSS) Serverless configurations that are associated with your AWS
  account.
- Amazon Elastic Compute Cloud (Amazon EC2) – Lists and provides `Describe`
  permissions for Amazon EC2 resources that are associated with your AWS
  account.
- Amazon Elastic Container Registry (Amazon ECR) – Provides `Describe` permissions for
  Amazon ECR resources that are associated with your AWS account.
- Amazon Elastic Container Service (Amazon ECS) – Provides `Describe` permissions for
  Amazon ECS resources that are associated with your AWS account.
- Amazon Elastic File System (Amazon EFS) – Provides `Describe` permissions for
  Amazon EFS resources that are associated with your AWS account.
- Amazon Elastic Kubernetes Service (Amazon EKS) – Lists and provides `Describe`
  permissions for Amazon EKS resources that are associated with your AWS
  account.
- Amazon EC2 Auto Scaling – Lists and provides `Describe` permissions for
  Amazon EC2 Auto Scaling resources that are associated with your AWS account.
- Amazon EC2 Systems Manager (SSM) – Provides `Describe` permissions for
  SSM resources that are associated with your AWS account.
- AWS Fault Injection Service (AWS FIS) – Lists and provides `Describe`
  permissions for AWS FIS experiments and experiment templates that are
  associated with your AWS account.
- Amazon FSx for Windows File Server (Amazon FSx) – Lists and provides `Describe`
  permissions for Amazon FSx resources that are associated with your AWS
  account.
- Amazon RDS – Lists and provides `Describe` permissions for
  Amazon RDS resources that are associated with your AWS account.
- Amazon Route 53 (Route 53) – Lists and provides `Describe`
  permissions for Route 53 resources that are associated with your AWS
  account.
- Amazon Route 53 Resolver – Lists and provides `Describe` permissions
  for Amazon Route 53 Resolver resources that are associated with your AWS account.
- Amazon Simple Notification Service (Amazon SNS) – Lists and provides `Describe`
  permissions for Amazon SNS resources that are associated with your AWS
  account.
- Amazon Simple Queue Service (Amazon SQS) – Lists and provides `Describe`
  permissions for Amazon SQS resources that are associated with your AWS
  account.
- Amazon Simple Storage Service (Amazon S3) – Lists and provides `Describe`
  permissions for Amazon S3 resources that are associated with your AWS
  account.

###### Note

While running an assessment, if there are any missing permissions that needs to be updated from Managed policies, AWS Resilience Hub will successfully complete the assessment using s3:GetBucketLogging permission. However, AWS Resilience Hub will display a warning message that lists the missing permissions and will provide a grace period to add the same. If you do not add the missing permissions within the specified grace period, the assessment will fail.

- AWS Backup – Lists and gets `Describe` permissions for
  Amazon EC2 Auto Scaling resources that are associated with your AWS account.
- AWS CloudFormation – Lists and gets `Describe` permissions for
  resources on AWS CloudFormation stacks that are associated with your AWS
  account.
- AWS DataSync – Lists and provides `Describe` permissions for AWS DataSync resources that are associated with your AWS account.
- Directory Service – Lists and provides `Describe` permissions for Directory Service resources that are associated with your AWS account.
- AWS Elastic Disaster Recovery (Elastic Disaster Recovery) – Provides `Describe` permissions for
  Elastic Disaster Recovery resources that are associated with your AWS account.
- AWS Lambda (Lambda) – Lists and provides `Describe`
  permissions for Lambda resources that are associated with your AWS
  account.
- AWS Resource Groups (Resource Groups) – Lists and provides `Describe`
  permissions for Resource Groups resources that are associated with your AWS
  account.
- AWS Service Catalog (Service Catalog) – Lists and provides `Describe`
  permissions for Service Catalog resources that are associated with your AWS
  account.
- AWS Step Functions – Lists and provides `Describe` permissions
  for AWS Step Functions resources that are associated with your AWS account.
- ELB – Lists and provides `Describe` permissions for
  ELB resources that are associated with your AWS account.
- `ssm:GetParametersByPath` – We use this permission to
  manage CloudWatch alarms, tests, or SOPs that are configured for your
  application.

The following IAM policy is required for an AWS account to add permissions for
users, user-groups, and roles that provide required permissions for your team to
access AWS services while running assessments.

## AWS Resilience Hub updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Resilience Hub since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Resilience Hub Document history page.

| Change                                                                                                                              | Description                                                                                                                                                                                                                                         | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`List` and `Get` permissions to allow you to<br>access experiments from AWS FIS while running assessments.                                               | December 17, 2024  |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`Describe` permissions to allow you to access resources<br>and configurations on Amazon ElastiCache (Redis OSS) Serverless while running<br>assessments. | September 25, 2024 |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`Describe` permissions to allow you to access resources<br>and configurations on Amazon DocumentDB, ELB, and AWS Lambda while running<br>assessments.    | August 01, 2024    |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`Describe` permissions to allow you to read the<br>Amazon FSx for Windows File Server configuration while running assessments.                           | March 26, 2024     |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`Describe` permissions to allow you to read the AWS Step Functions<br>configuration while running assessments.                                           | October 30, 2023   |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>Change | AWS Resilience Hub updated the<br>`AWSResilienceHubAsssessmentExecutionPolicy` to grant<br>`Describe` permissions to allow you to access resources<br>on Amazon RDS while running assessments.                                                      | October 5, 2023    |
| [AWSResilienceHubAsssessmentExecutionPolicy](#security_iam_aws-assessment-policy "#security_iam_aws-assessment-policy") –<br>New    | This AWS Resilience Hub policy provides access to other AWS services for<br>running assessments.                                                                                                                                                    | June 26, 2023      |
| AWS Resilience Hub started tracking changes                                                                                         | AWS Resilience Hub started tracking changes for its AWS managed policies.                                                                                                                                                                           | June 15, 2023      |
