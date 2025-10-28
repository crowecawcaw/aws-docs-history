# AWS policy: SageMakerStudioAdminIAMDefaultExecutionPolicy

This is the administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio. This
policy grants administrative access to provision, manage, and access resources in your
account. This does not grant access to data resources.

- Amazon DataZone permissions are required to manage Amazon DataZone resources such as
  Domain and Project.
- AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, and pass roles when
  provisioning resources.
- AWS STS permissions are required to assume other roles for accessing resources
  in cross-account.
- Amazon Q permissions are required to interact with Amazon Q within
  Amazon SageMaker Unified Studio.
- AWS Glue permissions are required to access data in Glue and allow usage of Glue
  Sessions.
- AWS Systems Manager permissions are required to manage parameters to enable Q and access
  SageMaker distribution.
- Amazon SageMaker AI permissions are required to manage SageMaker Space
  and allow SageMaker ML workloads.
- Amazon S3 permissions are required to create S3 buckets, access service
  CloudFormation templates in S3, and delete S3 bucket policies.
- AWS CloudFormation permissions are required to manage CloudFormation stack for managing
  resources of other services.
- Amazon CloudWatch Logs permissions are required to access logs from
  workloads in Amazon SageMaker Unified Studio.
- AWS Lake Formation permissions are required to manage Lake Formation
  grants to access data.
- Amazon Redshift Query Editor permissions are required to interact with
  Query Editor in Amazon SageMaker Unified Studio.
- Amazon Redshift Data API API permissions are required to run SQL
  statements using the Data API.
- Amazon Redshift Serverless permissions are required for discovery of
  Redshift Serverless.
- Amazon Redshift permissions are required for discovery of Redshift
  clusters.
- Amazon Bedrock permissions are required to interact with Bedrock APIs
  in Amazon SageMaker Unified Studio.
- Amazon DynamoDB permissions are required to enable federated
  connections to external data.
- AWS Secrets Manager permissions are required to manage secrets for
  connections.
- Amazon Athena permissions are required to interact with Query Editor
  in Amazon SageMaker Unified Studio.
- Amazon CodeWhisperer permissions are required to generate code
  recommendations.
- Amazon EventBridge Scheduler permissions are required to interact with one-click
  scheduling in Amazon SageMaker Unified Studio.
- Amazon ECR permissions are required to run SageMaker training jobs.
  To view the permissions for this policy, see [SageMakerStudioAdminIAMDefaultExecutionPolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMDefaultExecutionPolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMDefaultExecutionPolicy.md") in the _AWS Managed Policy Reference_.
