# `AWS-BulkResolveOpsItems`

**Description**

The `AWS-BulkResolveOpsItems` runbook resolves AWS Systems Manager OpsItems that
match the filter you specify. You can also specify an OpsItemId to add to the
resolved OpsItems using the `OpsInsightsId` parameter. If you specify a
value for the `S3BucketName` parameter, a result summary is sent to the
Amazon Simple Storage Service (Amazon S3) bucket. To receive a notification once the result summary has been
sent to the Amazon S3 bucket, specify a value for the `SnsTopicArn` parameter.
This automation will resolve a maximum of 1,000 OpsItems at a time.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-BulkResolveOpsItems "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-BulkResolveOpsItems")

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

- Filters

Type: String

Description: (Required) The key-value pairs of filters to return the
OpsItems you want to resolve. For example, `[{"Key": "Status", "Values":
 ["Open"], "Operator": "Equal"}]` . To learn more about the options
available for filtering OpsItems responses, see [OpsItemFilters](../../../systems-manager/latest/APIReference/API_DescribeOpsItems.md#systemsmanager-DescribeOpsItems-request-OpsItemFilters "../../../systems-manager/latest/APIReference/API_DescribeOpsItems.md#systemsmanager-DescribeOpsItems-request-OpsItemFilters") in the _AWS Systems Manager API Reference_ .

- OpsInsightId

Type: String

Description: (Optional) The related resource identifier you want to add to
resolved OpsItems.

- S3BucketName

Type: String

Description: (Optional) The name of the Amazon S3 bucket you want to send the
result summary to.

- SnsMessage

Type: String

Description: (Optional) The notification you want Amazon Simple Notification Service (Amazon SNS) to
send when the automation completes.

- SnsTopicArn

Type: String

Description: (Optional) The ARN of the Amazon SNS topic you want to notify when
the result summary has been sent to Amazon S3.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `s3:GetBucketAcl`
- `s3:PutObject`
- `sns:Publish`
- `ssm:DescribeOpsItems`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `ssm:UpdateOpsItem`

**Document Steps**

- `aws:executeScript` - Gathers and resolves the OpsItems based on the
  filters you specify. If you specified a value for the
  `OpsInsightId` parameter, the value is added as a related
  resource.
- `aws:executeScript` - If you specified a value for the
  `S3BucketName` parameter, a result summary is then sent to
  the Amazon S3 bucket.
- `aws:executeScript` - If you specified a value for the
  `SnsTopicArn` parameter, a notification is sent to the Amazon SNS
  topic after the result summary has been sent to Amazon S3 including the
  `SnsMessage` parameter value if specified.
