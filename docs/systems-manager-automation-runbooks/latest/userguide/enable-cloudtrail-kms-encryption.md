# `AWS-EnableCloudTrailKmsEncryption`

**Description**

This runbook updates the configuration of one or more AWS CloudTrail trails to use AWS Key Management Service (AWS KMS) encryption.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailKmsEncryption "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailKmsEncryption")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- KMSKeyId

Type: String

Description: (Required) The key ID of the of the
customer managed key you want to use to encrypt the trail you specify in the
`TrailName` parameter. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, or a fully specified ARN to a key.

- TrailNames

Type: StringList

Description: (Required) A comma separated list of the trails you want to update to
be encrypted.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudtrail:UpdateTrail`
- `kms:DescribeKey`
- `kms:ListKeys`
  **Document Steps**

- `aws:executeScript` - Enables AWS KMS encryption on the trails you specify in the
  `TrailName` parameter.
