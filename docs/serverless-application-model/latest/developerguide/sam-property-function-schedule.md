# Schedule

The object describing a `Schedule` event source type, which sets your serverless
function as the target of an Amazon EventBridge rule that triggers on a schedule. For more information, see
[What
Is Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md") in the _Amazon EventBridge User Guide_.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Events::Rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md") resource when this event type is set.

###### Note

EventBridge now offers a new scheduling capability, [Amazon EventBridge Scheduler](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md"). Amazon EventBridge
Scheduler is a serverless scheduler that allows you to create, run, and manage tasks from one central,
managed service. EventBridge Scheduler is highly customizable, and offers improved scalability over EventBridge
scheduled rules, with a wider set of target API operations and AWS services.

We recommend that you use EventBridge Scheduler to invoke targets on a schedule. To define this event
source type in your AWS SAM templates, see [ScheduleV2](sam-property-function-schedulev2.md "sam-property-function-schedulev2.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  DeadLetterConfig: `DeadLetterConfig`
  Description: `String`
  Enabled: `Boolean`
  Input: `String`
  Name: `String`
  RetryPolicy: `RetryPolicy`
  Schedule: `String`
  State: `String`

```

## Properties

`DeadLetterConfig`

Configure the Amazon Simple Queue Service (Amazon SQS) queue where EventBridge sends events after a failed target
invocation. Invocation can fail, for example, when sending an event to a Lambda function
that doesn't exist, or when EventBridge has insufficient permissions to invoke the Lambda
function. For more information, see [Event retry policy
and using dead-letter queues](../../../eventbridge/latest/userguide/rule-dlq.md "../../../eventbridge/latest/userguide/rule-dlq.md") in the _Amazon EventBridge User Guide_.

###### Note

The [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md")
resource type has a similar data type, `DeadLetterQueue`, which handles
failures that occur after successful invocation of the target Lambda function. Examples
of these types of failures include Lambda throttling, or errors returned by the Lambda
target function. For more information about the function `DeadLetterQueue`
property, see [Dead-letter queues](../../../lambda/latest/dg/invocation-async.md#invocation-dlq "../../../lambda/latest/dg/invocation-async.md#invocation-dlq") in the _AWS Lambda Developer Guide_.

_Type_: [DeadLetterConfig](sam-property-function-scheduledeadletterconfig.md "sam-property-function-scheduledeadletterconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DeadLetterConfig` property of the `AWS::Events::Rule`
`Target` data type. The AWS SAM version of this property includes additional
subproperties, in case you want AWS SAM to create the dead-letter queue for you.

`Description`

A description of the rule.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::Events::Rule`
resource.

`Enabled`

Indicates whether the rule is enabled.

To disable the rule, set this property to `false`.

###### Note

Specify either the `Enabled` or `State` property, but not
both.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`State` property of an `AWS::Events::Rule` resource. If
this property is set to `true` then AWS SAM passes `ENABLED`,
otherwise it passes `DISABLED`.

`Input`

Valid JSON text passed to the target. If you use this property, nothing from the
event text itself is passed to the target.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Input` property of an `AWS::Events::Rule Target`
resource.

`Name`

The name of the rule. If you don't specify a name, AWS CloudFormation generates a unique physical
ID and uses that ID for the rule name.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::Events::Rule` resource.

`RetryPolicy`

A `RetryPolicy` object that includes information about the retry policy
settings. For more information, see [Event retry policy
and using dead-letter queues](../../../eventbridge/latest/userguide/rule-dlq.md "../../../eventbridge/latest/userguide/rule-dlq.md") in the _Amazon EventBridge User Guide_.

_Type_: [RetryPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-retrypolicy "../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-retrypolicy")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RetryPolicy` property of the `AWS::Events::Rule`
`Target` data type.

`Schedule`

The scheduling expression that determines when and how often the rule runs. For more
information, see [Schedule Expressions for Rules](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md").

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`ScheduleExpression` property of an `AWS::Events::Rule`
resource.

`State`

The state of the rule.

_Accepted values:_
`DISABLED | ENABLED`

###### Note

Specify either the `Enabled` or `State` property, but not
both.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`State` property of an `AWS::Events::Rule` resource.

## Examples

### CloudWatch Schedule Event

CloudWatch Schedule Event Example

#### YAML

```
CWSchedule:
  Type: Schedule
  Properties:
    Schedule: 'rate(1 minute)'
    Name: TestSchedule
    Description: test schedule
    Enabled: false

```
