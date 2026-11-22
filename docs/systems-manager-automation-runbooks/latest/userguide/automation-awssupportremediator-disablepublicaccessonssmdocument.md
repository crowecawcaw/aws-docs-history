

# `AWSSupportRemediator-DisablePublicAccessOnSsmDocument`

**Description**

Disables public sharing on an AWS Systems Manager document by removing the `all` entry from the document's share permissions using the `ModifyDocumentPermission` API.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [SSM documents should not be public](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-4).

If the Systems Manager document does not exist or public sharing is already disabled, the automation completes successfully without making changes.

Any AWS account that relies on the public share to run or reference this document loses access after remediation. This action does not affect accounts explicitly added to the document's share list; it removes only the `all` entry.

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
+ SsmDocumentArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Systems Manager document to remove public share access from.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:DescribeDocumentPermission`
+ `ssm:ModifyDocumentPermission`

**Document Steps**

1. **validate** - Validates whether the Systems Manager document exists and is currently publicly shared.

1. **branchOnValidate** - Branches on whether the Systems Manager document requires remediation.

1. **disablePublicAccess** - Removes the `all` share permission from the Systems Manager document, disabling public access.

**Outputs**
+ validate.ChangeRequired: Whether a change is required.
+ validate.ValidationMessage: A message describing the validation result.