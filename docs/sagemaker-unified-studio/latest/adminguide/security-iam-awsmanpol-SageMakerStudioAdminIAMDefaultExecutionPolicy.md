

# AWS policy: SageMakerStudioAdminIAMDefaultExecutionPolicy
<a name="security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy"></a>

This is the administrative execution policy for using IAM roles with Amazon SageMaker Unified Studio. This policy grants administrative access to provision, manage, and access resources in your account. This does not grant access to data resources.
+ Amazon DataZone permissions are required to manage Amazon DataZone resources such as Domain and Project.
+ AWS Identity and Access Management permissions are required to list IAM roles, create service-linked roles, pass roles when provisioning resources, and update the trust policy of Amazon SageMaker Unified Studio IAM execution roles from the admin portal.
+ AWS STS permissions are required to assume other roles for accessing resources in cross-account, and to get service bearer tokens.
+ Amazon Q permissions are required to interact with Amazon Q within Amazon SageMaker Unified Studio.
+ AWS Glue permissions are required to access data in Glue and allow usage of Glue Sessions.
+ AWS Systems Manager permissions are required to manage parameters to enable Q and access SageMaker distribution.
+ Amazon SageMaker AI permissions are required to manage SageMaker Space and allow SageMaker ML workloads.
+ Amazon S3 permissions are required to create S3 buckets, access service CloudFormation templates in S3, delete S3 bucket policies, and register Amazon S3 Access Grants locations and manage the grants that share project data.
+ Amazon S3 Access Grants instance permissions are required to create and get the default Amazon S3 Access Grants instance.
+ Amazon S3 Tables permissions are required to create the `aws-sagemaker-unified-studio` table bucket and set its bucket policy.
+ CloudFormation permissions are required to manage CloudFormation stack for managing resources of other services.
+ Amazon CloudWatch Logs permissions are required to access and query logs from workloads in Amazon SageMaker Unified Studio, and to set retention for Amazon Bedrock AgentCore log groups.
+ AWS Lake Formation permissions are required to manage Lake Formation grants to access data.
+ Amazon Redshift Query Editor permissions are required to interact with Query Editor in Amazon SageMaker Unified Studio.
+ Amazon Redshift Data API API permissions are required to run SQL statements using the Data API.
+ Amazon Redshift Serverless permissions are required for discovery of Redshift Serverless.
+ Amazon Redshift permissions are required for discovery of Redshift clusters.
+ Amazon Bedrock permissions are required to interact with Bedrock APIs in Amazon SageMaker Unified Studio.
+ Amazon DynamoDB permissions are required to enable federated connections to external data.
+ AWS Secrets Manager permissions are required to manage secrets for connections.
+ Amazon Athena permissions are required to interact with Query Editor in Amazon SageMaker Unified Studio.
+ Amazon CodeWhisperer permissions are required to generate code recommendations.
+ Amazon EventBridge Scheduler permissions are required to interact with one-click scheduling in Amazon SageMaker Unified Studio.
+ Amazon ECR permissions are required to run SageMaker training jobs.
+ Amazon ECR Public permissions are required to get an authorization token to pull public container images.
+ Amazon MWAA permissions are required to manage and schedule workflows.
+ Amazon Bedrock AgentCore permissions are required to build and run agents with Agent Builder in Amazon SageMaker Unified Studio, including creating the AgentCore service-linked roles and passing roles to AgentCore and the agent registry.
+ AWS X-Ray permissions are required to send trace data and get sampling rules for agents built with Agent Builder.
+ AWS Resource Groups Tagging API permissions are required to look up resources by tag.
+ AWS KMS permissions are required to support customer managed key. Resources provisioned by Amazon SageMaker Unified Studio can be encrypted with your customer managed key.
+ AWS IAM Identity Center permissions are required to look up the users and groups that Amazon S3 Access Grants are issued to.

To view the permissions for this policy, see [SageMakerStudioAdminIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioAdminIAMDefaultExecutionPolicy.html) in the *AWS Managed Policy Reference*.