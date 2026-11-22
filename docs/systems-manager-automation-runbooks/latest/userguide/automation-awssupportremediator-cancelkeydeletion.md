

# `AWSSupportRemediator-CancelKeyDeletion`

**Description**

Cancels the scheduled deletion of an AWS Key Management Service (AWS KMS) key.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [AWS KMS keys should not be deleted unintentionally](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-3).

If the AWS KMS key does not exist or is not scheduled for deletion, the automation completes successfully without making changes.

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
+ KeyId

  Type: String

  Description: (Required) The ID of the AWS KMS key for which to cancel deletion.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `kms:CancelKeyDeletion`

**Document Steps**

1. **cancelKeyDeletion** - Cancels the scheduled deletion of the specified AWS KMS key.

**Outputs**
+ cancelKeyDeletion.ValidationMessage: A message describing the result of the automation.