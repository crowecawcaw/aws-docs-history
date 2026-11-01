

# AWS policy: SageMakerStudioAdminIAMPermissiveExecutionPolicy
<a name="security-iam-awsmanpol-SageMakerStudioAdminIAMPermissiveExecutionPolicy"></a>

This is an administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio. This policy grants administrative access to provision, manage, and access resources in your account. This includes broad access to data resources.

This policy provides full access to all APIs and resources for services used in Amazon SageMaker Unified Studio, such as Amazon CloudWatch Logs AWS Glue, Amazon Redshift, Amazon Redshift Data API, Amazon Redshift Serverless, Amazon S3, Amazon Athena, Amazon Bedrock, Amazon Bedrock AgentCore, AWS X-Ray, Amazon CodeWhisperer, Amazon DataZone, Amazon Q, Amazon SageMaker AI, AWS SQL Workbench, Amazon EventBridge Scheduler, and CloudFormation.

Additional access is provided for the following services:
+ AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, pass roles when provisioning resources, and update the trust policy of Amazon SageMaker Unified Studio IAM execution roles from the admin portal.
+ AWS Security Token Service permissions are required to assume other roles for accessing resources in cross-account, and to get service bearer tokens.
+ AWS Systems Manager permissions are required to manage parameters to enable Amazon Q and access SageMaker distribution.
+ AWS Lake Formation permissions are required to manage AWS Lake Formation grants to access data.
+ Amazon DynamoDB permissions are required to enable federated connections to external data.
+ AWS Secrets Manager permissions are required to manage secrets for connections.
+ Amazon ECR permissions are required to run SageMaker training jobs.
+ Amazon ECR Public permissions are required to get an authorization token to pull public container images.
+ Amazon MWAA permissions are required to manage and schedule workflows.
+ IAM permissions are required to create the Amazon Bedrock AgentCore service-linked roles and pass roles to AgentCore and the agent registry for Agent Builder in Amazon SageMaker Unified Studio.
+ AWS Resource Groups Tagging API permissions are required to look up resources by tag.
+ AWS KMS permissions are required to support customer managed key. Resources provisioned by Amazon SageMaker Unified Studio can be encrypted with your customer managed key.
+ AWS IAM Identity Center permissions are required to look up the users and groups that Amazon S3 Access Grants are issued to.

To view the permissions for this policy, see [SageMakerStudioAdminIAMPermissiveExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioAdminIAMPermissiveExecutionPolicy.html) in the *AWS Managed Policy Reference*.