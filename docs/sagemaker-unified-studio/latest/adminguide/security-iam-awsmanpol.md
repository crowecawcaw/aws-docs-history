# AWS managed policies for Amazon SageMaker Unified Studio

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS policy:
  SageMakerStudioFullAccess](security-iam-awsmanpol-SageMakerStudioFullAccess.md "security-iam-awsmanpol-SageMakerStudioFullAccess.md")
- [AWS policy:
  SageMakerStudioProjectUserRolePermissionsBoundary](security-iam-awsmanpol-SageMakerStudioProjectUserRolePermissionsBoundary.md "security-iam-awsmanpol-SageMakerStudioProjectUserRolePermissionsBoundary.md")
- [AWS
  policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md")
- [AWS
  policy: SageMakerStudioProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md")
- [AWS policy:
  SageMakerStudioProjectRoleMachineLearningPolicy](security-iam-awsmanpol-SageMakerStudioProjectRoleMachineLearningPolicy.md "security-iam-awsmanpol-SageMakerStudioProjectRoleMachineLearningPolicy.md")
- [AWS
  policy: SageMakerStudioDomainServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainServiceRolePolicy.md")
- [AWS policy: SageMakerStudioProjectProvisioningRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.md "security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.md")
- [AWS policy: AmazonDataZoneBedrockModelManagementPolicy](security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.md "security-iam-awsmanpol-AmazonDataZoneBedrockModelManagementPolicy.md")
- [AWS
  policy: SageMakerStudioQueryExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioQueryExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioQueryExecutionRolePolicy.md")
- [AWS
  policy: SageMakerStudioEMRServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioEMRServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioEMRServiceRolePolicy.md")
- [AWS policy: AmazonDataZoneBedrockModelConsumptionPolicy](security-iam-awsmanpol-AmazonDataZoneBedrockModelConsumptionPolicy.md "security-iam-awsmanpol-AmazonDataZoneBedrockModelConsumptionPolicy.md")
- [AWS
  policy: SageMakerStudioEMRInstanceRolePolicy](security-iam-awsmanpol-SageMakerStudioEMRInstanceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioEMRInstanceRolePolicy.md")
- [AWS policy: SageMakerStudioBedrockAgentServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockAgentServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockAgentServiceRolePolicy.md")
- [AWS policy: SageMakerStudioBedrockChatAgentUserRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockChatAgentUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockChatAgentUserRolePolicy.md")
- [AWS policy: SageMakerStudioBedrockPromptUserRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockPromptUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockPromptUserRolePolicy.md")
- [AWS policy: SageMakerStudioBedrockFlowServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockFlowServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockFlowServiceRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockEvaluationJobServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockEvaluationJobServiceRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy](security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseCustomResourcePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockKnowledgeBaseServiceRolePolicy.md")
- [AWS policy:
  SageMakerStudioBedrockFunctionExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioBedrockFunctionExecutionRolePolicy.md")
- [AWS
  policy: SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md")
- [AWS policy: SageMakerStudioUserIAMDefaultExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md")
- [AWS policy:
  SageMakerStudioUserIAMPermissiveExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMPermissiveExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMPermissiveExecutionPolicy.md")
- [AWS
  policy: SageMakerStudioAdminIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.md")
- [AWS policy: SageMakerStudioAdminIAMDefaultExecutionPolicy](security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioAdminIAMDefaultExecutionPolicy.md")
- [AWS policy:
  SageMakerStudioAdminIAMPermissiveExecutionPolicy](security-iam-awsmanpol-SageMakerStudioAdminIAMPermissiveExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioAdminIAMPermissiveExecutionPolicy.md")
- [AWS
  policy: SageMakerStudioAdminProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioAdminProjectUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioAdminProjectUserRolePolicy.md")
- [Amazon SageMaker Unified Studio updates to AWS managed
  policies](security-iam-awsmanpol-updates.md "security-iam-awsmanpol-updates.md")
