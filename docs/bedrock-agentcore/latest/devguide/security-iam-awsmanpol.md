# AWS managed policies for Amazon Bedrock AgentCore

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

###### Topics

- [AWS managed policy: BedrockAgentCoreFullAccess](#security-iam-awsmanpol-BedrockAgentCoreFullAccess "#security-iam-awsmanpol-BedrockAgentCoreFullAccess")
- [AWS managed policy: BedrockAgentCoreNetworkServiceRolePolicy](#security-iam-awsmanpol-BedrockAgentCoreNetworkServiceRolePolicy "#security-iam-awsmanpol-BedrockAgentCoreNetworkServiceRolePolicy")
- [AWS managed policy: AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy](#security-iam-awsmanpol-AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy "#security-iam-awsmanpol-AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy")
- [AWS managed policy: BedrockAgentCoreRuntimeIdentityServiceRolePolicy](#security-iam-awsmanpol-BedrockAgentCoreRuntimeIdentityServiceRolePolicy "#security-iam-awsmanpol-BedrockAgentCoreRuntimeIdentityServiceRolePolicy")
- [AgentCore updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: BedrockAgentCoreFullAccess

You can attach [BedrockAgentCoreFullAccess](../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md") to your users, groups, and roles.

This policy grants permissions that allow full access to the Amazon Bedrock AgentCore.

**Permissions details**

This policy includes the following permissions:

- `bedrock-agentcore` (Amazon Bedrock Agent Core) – Allows
  principals full access to all Amazon Bedrock Agent Core resources.
- `iam` (AWS Identity and Access Management) –
  Allows principals to list and get information about roles and policies, and to pass roles
  with "BedrockAgentCore" in the name to the bedrock-agentcore service. Also allows
  creating service-linked roles for CloudWatch Application Signals, Amazon Bedrock AgentCore network, and Amazon Bedrock AgentCore runtime identity.
- `secretsmanager` (AWS Secrets Manager) –
  Allows principals to create, update, retrieve, and delete secrets with names
  that begin with "bedrock-agentcore".
- `kms` (AWS Key Management Service) –
  Allows principals to list and describe keys, and to decrypt data within the same AWS account
  when called via the Amazon Bedrock AgentCore service.
- `s3` (Amazon Simple Storage Service) –
  Allows principals to get objects from S3 buckets with names that begin with
  "bedrock-agentcore-gateway-" when called via the Amazon Bedrock AgentCore service.
- `lambda` (AWS Lambda) –
  Allows principals to list Lambda functions.
- `logs` (Amazon CloudWatch Logs) – Allows principals
  to access, query, and manage log data in log groups related to Amazon Bedrock AgentCore and Application Signals, including creating log groups and streams.
- `application-autoscaling` (Application Auto Scaling) –
  Allows principals to describe scaling policies.
- `application-signals` (Amazon CloudWatch Application Signals) –
  Allows principals to retrieve information about application signals and start discovery.
- `autoscaling` (Amazon EC2 Auto Scaling) –
  Allows principals to describe Auto Scaling resources.
- `cloudwatch` (Amazon CloudWatch) –
  Allows principals to retrieve and list metrics, generate queries, and access other
  CloudWatch resources.
- `oam` (Amazon CloudWatch Observability Access Manager) –
  Allows principals to list sinks.
- `rum` (Amazon CloudWatch RUM) –
  Allows principals to retrieve and list RUM resources.
- `synthetics` (Amazon CloudWatch Synthetics) –
  Allows principals to describe and get information about Synthetics resources.
- `xray` (AWS X-Ray) –
  Allows principals to retrieve trace information, manage trace segment destinations,
  and work with indexing rules.

## AWS managed policy: BedrockAgentCoreNetworkServiceRolePolicy

This policy is attached to a service-linked role that allows the service to
perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

This policy grants permissions that allow AgentCore to create and manage network interfaces in your VPC when running in VPC mode.

**Permissions details**

This policy includes the following permissions:

- `ec2` (Amazon Elastic Compute Cloud) – Allows
  the service to create, manage, and delete network interfaces in your VPC,
  assign and unassign private IP addresses, and describe VPC resources.
  Network interfaces are tagged with "AmazonBedrockAgentCoreManaged" to ensure
  the service only manages resources it creates.

You can view this policy at [BedrockAgentCoreNetworkServiceRolePolicy](../../../aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.md").

For more information about the service-linked role that uses this policy, see [Using service-linked roles for Amazon Bedrock AgentCore](service-linked-roles.md "service-linked-roles.md").

## AWS managed policy: AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy

You can attach [AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonBedrockAgentCoreMemoryBedrockModelInferenceExecutionRolePolicy.md") to
your users, groups, and roles.

This policy grants permissions that allow full access to the Amazon Bedrock Agent Core Memory.

**Permissions details**

This policy includes the following permissions.

- `bedrock` – Allows principals to call the Amazon Bedrock `Invokemodel`
  and `InvokeModelWithResponseStream` actions. This is
  required so that an agent can store memories.

## AWS managed policy: BedrockAgentCoreRuntimeIdentityServiceRolePolicy

This policy is attached to a service-linked role that allows the service to
perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

This policy grants permissions that allow access to identity and token management resources that are required for AgentCore Runtime authentication and authorization.

**Permissions details**

This policy includes the following permissions:

- `bedrock-agentcore` (Amazon Bedrock Agent Core) – Allows
  the service to get workload access tokens for JWT authentication and user ID-based
  authentication. Specifically allows `GetWorkloadAccessToken`,
  `GetWorkloadAccessTokenForJWT`, and `GetWorkloadAccessTokenForUserId`
  actions on the default workload identity directory and its associated workload identities.

**Policy contents**

You can view the complete policy at [BedrockAgentCoreRuntimeIdentityServiceRolePolicy](../../../aws-managed-policy/latest/reference/BedrockAgentCoreRuntimeIdentityServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreRuntimeIdentityServiceRolePolicy.md").

For more information about the service-linked role that uses this policy, see [Using service-linked roles for Amazon Bedrock AgentCore](service-linked-roles.md "service-linked-roles.md").

## AgentCore updates to AWS managed

policies

View details about updates to AWS managed policies for AgentCore since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AgentCore Document history page.

| Change                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [BedrockAgentCoreFullAccess](#security-iam-awsmanpol-BedrockAgentCoreFullAccess "#security-iam-awsmanpol-BedrockAgentCoreFullAccess") –<br>Updated policy                                                               | • Added the `cloudtrail:CreateServiceLinkedChannel` permission to allow Amazon Bedrock AgentCore to create a CloudTrail service-linked channel for the Application Signals feature.<br>• Added `kms:CreateGrant` permission to allow the Amazon Bedrock AgentCore Gateway service to create grants on customer managed keys for the S3 vectors service used for semantic search.<br>• Added `kms:ListGrants` permission to check if previously created grants exist.<br>• Added S3 permissions to create bucket, put bucket policy, versioning, put object for buckets with prefix bedrock-agentcore-runtime-.<br>• Added list buckets, list objects in the bucket, and get object permissions.<br>• Added ECR permissions to describe repositories, list images, and describe images.<br>• Added logs `PutResourcePolicy` permissions to enable transaction search. | November 3, 2025   |
| [BedrockAgentCoreRuntimeIdentityServiceRolePolicy](#security-iam-awsmanpol-BedrockAgentCoreRuntimeIdentityServiceRolePolicy "#security-iam-awsmanpol-BedrockAgentCoreRuntimeIdentityServiceRolePolicy") –<br>New policy | Added a new AWS managed policy that allows AgentCore to manage workload identity access tokens and OAuth credentials for agent runtimes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | October 10, 2025   |
| [BedrockAgentCoreFullAccess](#security-iam-awsmanpol-BedrockAgentCoreFullAccess "#security-iam-awsmanpol-BedrockAgentCoreFullAccess") –<br>Updated policy                                                               | Added permission to create the Amazon Bedrock AgentCore runtime identity service-linked role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | October 9, 2025    |
| [BedrockAgentCoreFullAccess](#security-iam-awsmanpol-BedrockAgentCoreFullAccess "#security-iam-awsmanpol-BedrockAgentCoreFullAccess") –<br>Updated policy                                                               | Added permission to create the Amazon Bedrock AgentCore runtime identity service-linked role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | October 8, 2025    |
| [BedrockAgentCoreFullAccess](#security-iam-awsmanpol-BedrockAgentCoreFullAccess "#security-iam-awsmanpol-BedrockAgentCoreFullAccess") –<br>Updated policy                                                               | Added permission to create the Amazon Bedrock AgentCore network service-linked role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | September 19, 2025 |
| [BedrockAgentCoreNetworkServiceRolePolicy](#security-iam-awsmanpol-BedrockAgentCoreNetworkServiceRolePolicy "#security-iam-awsmanpol-BedrockAgentCoreNetworkServiceRolePolicy") –<br>New policy                         | Added a new AWS managed policy that allows AgentCore to create and manage network interfaces in your VPC when running in VPC mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | September 19, 2025 |
| AgentCore started tracking changes                                                                                                                                                                                      | AgentCore started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 16, 2025      |
