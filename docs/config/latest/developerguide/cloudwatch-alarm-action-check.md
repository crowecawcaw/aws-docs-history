# cloudwatch-alarm-action-check

Checks if CloudWatch alarms have an action configured for the ALARM, INSUFFICIENT_DATA, or OK state. Optionally checks if any actions match a named ARN. The rule is NON_COMPLIANT if there is no action specified for the alarm or optional parameter.

**Identifier:** CLOUDWATCH_ALARM_ACTION_CHECK

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

okActionRequired
Type: String
Default: false

Alarms have at least one action when the alarm transitions to an OK state from any other state.

insufficientDataActionRequired
Type: String
Default: true

Alarms have at least one action when the alarm transitions to the INSUFFICIENT_DATA state from any other state.

alarmActionRequired
Type: String
Default: true

Alarms have at least one action.

action1 (Optional)
Type: String

The action to execute, specified as an ARN.

action2 (Optional)
Type: String

The action to execute, specified as an ARN.

action3 (Optional)
Type: String

The action to execute, specified as an ARN.

action4 (Optional)
Type: String

The action to execute, specified as an ARN.

action5 (Optional)
Type: String

The action to execute, specified as an ARN.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
