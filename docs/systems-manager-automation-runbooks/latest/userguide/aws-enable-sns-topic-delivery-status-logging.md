# `AWS-EnableSNSTopicDeliveryStatusLogging`

**Description**

The `AWS-EnableSNSTopicDeliveryStatusLogging` runbook configures
delivery status logging for a `HTTP`, Amazon Data Firehose, Lambda, `Platform
 application`, or Amazon Simple Queue Service (Amazon SQS) endpoint. This allow Amazon SNS to log
failed alerts and a sample percentage of successful alert notifications to Amazon CloudWatch.
If delivery status logging is already configured for the topic, the runbook replaces
the existing configuration with the new values you specify for the input
parameters.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableSNSTopicDeliveryStatusLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableSNSTopicDeliveryStatusLogging")

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

- EndpointType

Type: String

Valid values:

    + HTTP
    + Firehose
    + Lambda
    + Application
    + SQS

Description: (Required) The type of Amazon SNS topic endpoint you want to log
delivery status notification messages for.

- TopicArn

Type: String

Description: (Required) The ARN of the Amazon SNS topic you want to configure
delivery status logging for.

- SuccessFeedbackRoleArn

Type: String

Description: (Required) The ARN of the IAM role which Amazon SNS uses to send
logs for successful notification messages to CloudWatch.

- SuccessFeedbackSampleRate

Type: String

Valid values: 0-100

Description: (Required) The percentage of successful messages to sample
for the specified Amazon SNS topic.

- FailureFeedbackRoleArn

Type: String

Description: (Required) The ARN of the IAM role which Amazon SNS uses to send
logs for failure notification messages to CloudWatch.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `iam:PassRole`
- `sns:GetTopicAttributes`
- `sns:SetTopicAttributes`

**Document Steps**

- `aws:executeAwsApi` - Applies the value for the
  `SuccessFeedbackRoleArn` parameter to the Amazon SNS topic.
- `aws:executeAwsApi` - Applies the value for the
  `SuccessFeedbackSampleRate` parameter to the Amazon SNS
  topic.
- `aws:executeAwsApi` - Applies the value for the
  `FailureFeedbackRoleArn` parameter to the Amazon SNS topic.
- `aws:executeScript` - Confirms delivery status logging is enabled
  on the Amazon SNS topic.

**Outputs**

VerifyDeliveryStatusLoggingEnabled.GetTopicAttributesResponse - Response from the
`GetTopicAttributes` API operations.

VerifyDeliveryStatusLoggingEnabled.VerifyDeliveryStatusLoggingEnabled - Message
indicating successful verification of delivery status logging.
