# `AWS-EnableStepFunctionsStateMachineLogging`

**Description**

The `AWS-EnableStepFunctionsStateMachineLogging` runbook enables or updates logging on the AWS Step Functions state machine you specify. The minimum logging level must be set to `ALL`, `ERROR`, or `FATAL`.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableStepFunctionsStateMachineLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableStepFunctionsStateMachineLogging")

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

- Level

Type: String

Valid values: ALL | ERROR | FATAL

Description: (Required) The URL of the Amazon SQS queue you want to enable encryption on.

- LogGroupArn

Type: String

Description: (Required) The ARN of the Amazon CloudWatch Logs log group you want to send state machine logs to.

- StateMachineArn

Type: String

Description: (Required) The ARN of the state machine you want enable logging on.

- IncludeExecutionData

Type: Boolean

Default: False

Description: (Optional) Determines whether execution data is included in the logs.

- TracingConfiguration

Type: Boolean

Default: False

Description: (Optional) Determines whether AWS X-Ray tracing is enabled.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `states:DescribeStateMachine`
- `states:UpdateStateMachine`

**Document Steps**

- `EnableStepFunctionsStateMachineLogging (aws:executeAwsApi)` - Updates the specified state machine with the logging configuration specified.
- `VerifyStepFunctionsStateMachineLoggingEnabled (aws:assertAwsResourceProperty)` - Verifies logging was enabled for the specified state machine.

**Outputs**

- EnableStepFunctionsStateMachineLogging.Response - Response from the UpdateStateMachine API call.
