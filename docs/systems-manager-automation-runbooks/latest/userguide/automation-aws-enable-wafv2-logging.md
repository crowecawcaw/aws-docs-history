# `AWSConfigRemediation-EnableWAFV2Logging`

**Description**

The `AWSConfigRemediation-EnableWAFV2Logging` runbook enables logging
for an AWS WAF (AWS WAFV2) web access control list (web ACL) with the specified
Amazon Data Firehose (Firehose) delivery stream.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableWAFV2Logging "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableWAFV2Logging")

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

Description: (Required) The Firehose delivery stream ARN that you want to
associate with the web ACL.

###### Note

The Firehose delivery stream ARN must begin with the prefix
`aws-waf-logs-` . For example,
`aws-waf-logs-us-east-2-analytics` . For more
information, see [Amazon Data Firehose](../../../waf/latest/developerguide/logging-kinesis.md "../../../waf/latest/developerguide/logging-kinesis.md") .

- WebAclArn

Type: String

Description: (Required) ARN of the web ACL for which logging will be
enabled.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `firehose:DescribeDeliveryStream`
- `wafv2:PutLoggingConfiguration`

- `wafv2:GetLoggingConfiguration`

**Document Steps**

- `aws:executeScript` - Enables logging for the AWS WAFV2 web ACL and
  verifies that the logging has the specified configuration.
