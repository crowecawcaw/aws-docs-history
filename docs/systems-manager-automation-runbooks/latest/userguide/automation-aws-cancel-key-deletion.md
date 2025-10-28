# `AWSConfigRemediation-CancelKeyDeletion`

**Description**

The `AWSConfigRemediation-CancelKeyDeletion` runbook cancels deletion
of the AWS Key Management Service (AWS KMS) customer managed key that you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-CancelKeyDeletion "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-CancelKeyDeletion")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- KeyId

Type: String

Description: (Required) The ID of the customer managed key that you want to cancel
deletion for.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `kms:CancelKeyDeletion`
- `kms:DescribeKey`

**Document Steps**

- `aws:executeAwsApi` - Cancels deletion for the customer managed key you
  specify in the `KeyId` parameter.
- `aws:assertAwsResourceProperty` - Confirms key deletion is
  disabled on your customer managed key.
