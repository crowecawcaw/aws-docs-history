

# `AWSSupportRemediator-PutEcrRepositoryLifecyclePolicy`

**Description**

Configures a lifecycle policy on an Amazon Elastic Container Registry (Amazon ECR) repository that has no lifecycle policy.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon ECR Repository Without Lifecycle Policy Configured](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-ecr-repository-without-lifecycle-policy) and AWS Security Hub CSPM control [ECR repositories should have at least one lifecycle policy configured](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-3).

If the Amazon ECR repository does not exist or already has a lifecycle policy, the automation completes successfully without making changes.

The runbook applies the lifecycle policy JSON that you provide through the `LifecyclePolicyText` parameter. If you omit `LifecyclePolicyText`, the runbook applies a default policy that expires images older than 365 days based on image push time.

Applying a lifecycle policy evaluates existing images against the policy rules.

**Irreversible action**  
Amazon ECR deletes any image that matches an expiration rule, and you cannot recover deleted images.

The `validateRepository.InitialLifecyclePolicy` output captures the existing lifecycle policy before the change. You can use this output to re-apply the original policy manually, but it does not restore any deleted images.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ RepositoryName

  Type: String

  Description: (Required) The name of the Amazon ECR repository on which to configure the lifecycle policy.
+ LifecyclePolicyText

  Type: String

  Description: (Optional) The JSON lifecycle policy text to apply to the Amazon ECR repository. If you omit this parameter, the runbook applies a default policy that expires images older than 365 days.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ecr:GetLifecyclePolicy`
+ `ecr:PutLifecyclePolicy`

**Document Steps**

1. **validateRepository** - Verifies that the Amazon ECR repository exists and checks whether it already has a lifecycle policy. Validates `LifecyclePolicyText` when you provide a value, or selects the default policy.

1. **branchOnChangeRequired** - Branches on whether the runbook needs to apply a lifecycle policy.

1. **putLifecyclePolicy** - Applies the selected lifecycle policy to the Amazon ECR repository by calling the Amazon ECR `PutLifecyclePolicy` API.

**Outputs**
+ `validateRepository.ChangeRequired`: Boolean indicating whether the runbook needs to apply a lifecycle policy to the Amazon ECR repository.
+ `validateRepository.InitialLifecyclePolicy`: The existing lifecycle policy on the Amazon ECR repository before the runbook runs. Empty when the repository has no existing policy or does not exist.
+ `validateRepository.AppliedLifecyclePolicy`: The lifecycle policy that this runbook applies to the Amazon ECR repository. Empty when the runbook makes no change.
+ `validateRepository.ValidationMessage`: A message describing the validation result.