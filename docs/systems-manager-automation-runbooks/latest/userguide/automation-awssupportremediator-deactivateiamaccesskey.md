

# `AWSSupportRemediator-DeactivateIamAccessKey`

**Description**

Deactivates an AWS Identity and Access Management (IAM) access key for a specified IAM user by setting its status to `Inactive`.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Exposed Access Keys](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#exposed-access-keys).

If the IAM user does not exist, the specified access key does not exist on the user, or the access key is already `Inactive`, the automation completes successfully without making changes.

Applications configured with the deactivated access key can no longer authenticate to AWS.

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
+ AccessKeyId

  Type: String

  Description: (Required) The ID of the IAM access key to deactivate.
+ UserName

  Type: String

  Description: (Required) The name of the IAM user that owns the access key.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `iam:ListAccessKeys`
+ `iam:UpdateAccessKey`

**Document Steps**

1. **validateInput** - Validates whether the IAM access key exists and is currently `Active`.

1. **branchOnChangeRequired** - Branches on whether the access key needs to be deactivated.

1. **deactivateAccessKey** - Sets the status of the specified IAM access key to `Inactive`.

**Outputs**
+ validateInput.ChangeRequired: Whether the access key needs to be deactivated.
+ validateInput.ValidationMessage: A message describing the validation result.