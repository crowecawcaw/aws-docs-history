# `AWS-EnableAthenaWorkGroupEncryptionAtRest`

**Description**

The `AWS-EnableAthenaWorkGroupEncryptionAtRest` runbook enables encryption at rest for the Amazon Athena workgroup you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableAthenaWorkGroupEncryptionAtRest "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableAthenaWorkGroupEncryptionAtRest")

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

- WorkGroup

Type: String

Description: (Required) The workgroup that you want to enable encryption at rest for.

- EncryptionOption

Type: String

Valid Values: SSE_S3 | SSE_KMS | CSE_KMS

Description: (Required) Specifies which encryption option is used. You can choose server-side encryption with Amazon S3 managed keys (SSE_S3), server-side encryption with AWS KMS managed keys (SSE_KMS), or client-side encryption with AWS KMS managed keys (CSE_KMS).

- KmsKeyId

Type: String

Description: (Optional) If you're using a AWS KMS encryption option, specify the key ARN, key ID, or the key alias of the key you want to use.

- EnableMinimumEncryptionConfiguration

Type: Boolean

Default: True

Description: (Optional) Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries. This setting does not apply to Spark-enabled workgroups.

- EnforceWorkGroupConfiguration

Type: Boolean

Default: True

Description: (Optional) If set to `True`, the settings for the workgroup override client-side settings. If set to `False`, client-side settings are used.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `athena:GetWorkGroup`
- `athena:UpdateWorkGroup`

**Document Steps**

- aws:branch - Branches based on the encryption option specified in the `EncryptionOption` parameter.
- aws:executeAwsApi - This step updates the Athena Work Group with the specified encryption setting.
- aws:executeAwsApi - Updates the Athena Work Group with the specified encryption setting.
- aws:assertAwsResourceProperty - Verifies that encryption for the workgroup has been enabled.
