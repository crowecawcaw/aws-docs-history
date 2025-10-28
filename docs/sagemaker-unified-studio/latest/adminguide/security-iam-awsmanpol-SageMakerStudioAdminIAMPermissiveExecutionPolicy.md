# AWS policy:

SageMakerStudioAdminIAMPermissiveExecutionPolicy

This is an administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio. This
policy grants administrative access to provision, manage, and access resources in your
account. This includes broad access to data resources.

This policy provides full access to all APIs and resources for services used in
Amazon SageMaker Unified Studio, such as Amazon CloudWatch Logs AWS Glue, Amazon Redshift,
Amazon Redshift Data API, Amazon Redshift Serverless, Amazon S3,
Amazon Athena, Amazon Bedrock, Amazon CodeWhisperer, Amazon DataZone,
Amazon Q, Amazon SageMaker AI, AWS SQL Workbench, Amazon EventBridge Scheduler,
and AWS CloudFormation.

Additional access is provided for the following services:

- AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, and pass roles when
  provisioning resources.
- AWS Security Token Service permissions are required to assume other roles for accessing
  resources in cross-account.
- AWS Systems Manager permissions are required to manage parameters to enable Amazon Q and
  access SageMaker distribution.
- AWS Lake Formation permissions are required to manage
  AWS Lake Formation grants to access data.
- Amazon DynamoDB permissions are required to enable federated
  connections to external data.
- AWS Secrets Manager permissions are required to manage secrets for
  connections.
- Amazon ECR permissions are required to run SageMaker training jobs.
  To view the permissions for this policy, see [SageMakerStudioAdminIAMPermissiveExecutionPolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMPermissiveExecutionPolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMPermissiveExecutionPolicy.md") in the _AWS Managed Policy Reference_.
