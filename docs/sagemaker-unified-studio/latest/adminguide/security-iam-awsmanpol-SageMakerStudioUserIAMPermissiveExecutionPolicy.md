# AWS policy:

SageMakerStudioUserIAMPermissiveExecutionPolicy

This is an execution policy for using IAM roles with Amazon SageMaker Unified Studio. This policy grants
access to users to access resources in your account, including broad access to data
resources.

This policy provides full access to all APIs and resources for services used in
Amazon SageMaker Unified Studio, such as Amazon CloudWatch Logs AWS Glue, Amazon Redshift,
Amazon Redshift Data API, Amazon Redshift Serverless, Amazon S3,
Amazon Athena, Amazon Bedrock, Amazon CodeWhisperer, Amazon DataZone,
Amazon Q, Amazon SageMaker AI, AWS SQL Workbench, Amazon EventBridge Scheduler,
and AWS CloudFormation.

Additional access is provided for the following services:

- Amazon DataZone permissions are required to access Amazon DataZone resources such as
  Project and Asset.
- AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, and pass roles when
  provisioning resources.
- AWS Security Token Service permissions are required to assume other roles for accessing
  cross-account resources.
- AWS Systems Manager permissions are required to access parameters for Amazon Q and
  Amazon SageMaker AI distribution.
- AWS Lake Formation permissions are required to describe
  AWS Lake Formation Resources.
- Amazon DynamoDB permissions are required to enable federated
  connections to external data.
- AWS Secrets Manager permissions are required to access secrets for
  connections.
- Amazon ECR permissions are required to run Amazon SageMaker AI training
  jobs.
  To view the permissions for this policy, see [SageMakerStudioUserIAMPermissiveExecutionPolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioUserIAMPermissiveExecutionPolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioUserIAMPermissiveExecutionPolicy.md") in the _AWS Managed Policy Reference_.
