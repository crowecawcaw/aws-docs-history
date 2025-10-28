# `AWSConfigRemediation-EnableWAFClassicRegionalLogging`

**Description**

The `AWSConfigRemediation-EnableWAFClassicRegionalLogging` runbook
enables logging to Amazon Data Firehose (Firehose) for the AWS WAF web access control list (ACL) you
specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableWAFClassicRegionalLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableWAFClassicRegionalLogging")

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

- LogDestinationConfigs

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the Firehose
delivery stream that you want to send logs to.

- WebACLId

Type: String

Description: (Required) The ID of the AWS WAF web ACL that you want to
enable logging on.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `iam:CreateServiceLinkedRole`
- `waf-regional:GetLoggingConfiguration`
- `waf-regional:GetWebAcl`
- `waf-regional:PutLoggingConfiguration`

**Document Steps**

- `aws:executeAwsApi` - Gathers the ARN of the AWS WAF web ACL
  specified in the `WebACLId` parameter.
- `aws:executeAwsApi` - Enables logging for the web ACL.
- `aws:assertAwsResourceProperty` - Verifies logging has been
  enabled on the AWS WAF web ACL.
