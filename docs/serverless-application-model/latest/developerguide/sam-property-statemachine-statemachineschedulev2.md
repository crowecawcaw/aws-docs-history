# ScheduleV2

The object describing a `ScheduleV2` event source type, which sets your state
machine as the target of an Amazon EventBridge Scheduler event that triggers on a schedule. For more
information, see [What is Amazon EventBridge Scheduler?](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md") in
the _EventBridge Scheduler User Guide_.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Scheduler::Schedule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md") resource when this event type is
set.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
DeadLetterConfig: `DeadLetterConfig`
Description: `String`
EndDate: `String`
FlexibleTimeWindow: `FlexibleTimeWindow`
GroupName: `String`
Input: `String`
KmsKeyArn: `String`
Name: `String`
OmitName: `Boolean`
PermissionsBoundary: `String`
RetryPolicy: `RetryPolicy`
RoleArn: `String`
ScheduleExpression: `String`
ScheduleExpressionTimezone: `String`
StartDate: `String`
State: `String`
```

## Properties

`DeadLetterConfig`

Configure the Amazon Simple Queue Service (Amazon SQS) queue where EventBridge sends events after a failed target
invocation. Invocation can fail, for example, when sending an event to a Lambda function
that doesn't exist, or when EventBridge has insufficient permissions to invoke the Lambda
function. For more information, see [Configuring a
dead-letter queue for EventBridge Scheduler](../../../scheduler/latest/UserGuide/configuring-schedule-dlq.md "../../../scheduler/latest/UserGuide/configuring-schedule-dlq.md") in the _EventBridge Scheduler User
Guide_.

_Type_: [DeadLetterConfig](sam-property-statemachine-statemachinescheduledeadletterconfig.md "sam-property-statemachine-statemachinescheduledeadletterconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DeadLetterConfig` property of the
`AWS::Scheduler::Schedule`
`Target` data type. The AWS SAM version of this property includes additional
subproperties, in case you want AWS SAM to create the dead-letter queue for you.

`Description`

A description of the schedule.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::Scheduler::Schedule`
resource.

`EndDate`

The date, in UTC, before which the schedule can invoke its target. Depending on the
schedule's recurrence expression, invocations might stop on, or before, the
**EndDate** you specify.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`EndDate` property of an `AWS::Scheduler::Schedule`
resource.

`FlexibleTimeWindow`

Allows configuration of a window within which a schedule can be invoked.

_Type_: [FlexibleTimeWindow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md#cfn-scheduler-schedule-flexibletimewindow "../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md#cfn-scheduler-schedule-flexibletimewindow")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FlexibleTimeWindow` property of an
`AWS::Scheduler::Schedule` resource.

`GroupName`

The name of the schedule group to associate with this schedule. If not defined, the
default group is used.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`GroupName` property of an `AWS::Scheduler::Schedule`
resource.

`Input`

Valid JSON text passed to the target. If you use this property, nothing from the
event text itself is passed to the target.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Input` property of an `AWS::Scheduler::Schedule Target`
resource.

`KmsKeyArn`

The ARN for a KMS Key that will be used to encrypt customer data.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn` property of an `AWS::Scheduler::Schedule`
resource.

`Name`

The name of the schedule. If you don't specify a name, AWS SAM generates a name in the
format
`StateMachine-Logical-ID`Event-Source-Name``
and uses that ID for the schedule name.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::Scheduler::Schedule`
resource.

`OmitName`

By default, AWS SAM generates and uses a schedule name in the format of
`<State-machine-logical-ID><event-source-name>`. Set this property to
`true` to have AWS CloudFormation generate a unique physical ID and use that for the schedule name instead.

_Type_: Boolean

_Required_: No

_Default_: `false`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation
equivalent.

`PermissionsBoundary`

The ARN of the policy used to set the permissions boundary for the role.

###### Note

If `PermissionsBoundary` is defined, AWS SAM will apply the same
boundaries to the scheduler schedule's target IAM role.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`PermissionsBoundary` property of an `AWS::IAM::Role`
resource.

`RetryPolicy`

A `RetryPolicy` object that includes information about the retry policy
settings.

_Type_: [RetryPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.md#cfn-scheduler-schedule-target-retrypolicy "../../../AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.md#cfn-scheduler-schedule-target-retrypolicy")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RetryPolicy` property of the `AWS::Scheduler::Schedule`
`Target` data type.

`RoleArn`

The ARN of the IAM role that EventBridge Scheduler will use for the target when the
schedule is invoked.

_Type_: [RoleArn](../../../AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.md#cfn-scheduler-schedule-target-rolearn "../../../AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.md#cfn-scheduler-schedule-target-rolearn")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RoleArn` property of the `AWS::Scheduler::Schedule`
`Target` data type.

`ScheduleExpression`

The scheduling expression that determines when and how often the schedule
runs.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`ScheduleExpression` property of an
`AWS::Scheduler::Schedule` resource.

`ScheduleExpressionTimezone`

The timezone in which the scheduling expression is evaluated.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ScheduleExpressionTimezone` property of an
`AWS::Scheduler::Schedule` resource.

`StartDate`

The date, in UTC, after which the schedule can begin invoking a target. Depending on
the schedule's recurrence expression, invocations might occur on, or after, the
**StartDate** you specify.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartDate` property of an `AWS::Scheduler::Schedule`
resource.

`State`

The state of the schedule.

_Accepted values:_
`DISABLED | ENABLED`

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`State` property of an `AWS::Scheduler::Schedule`
resource.

## Examples

### Basic example of

defining a ScheduleV2 resource

```
StateMachine:
  Type: AWS::Serverless::StateMachine
  Properties:
    Name: MyStateMachine
    Events:
      ScheduleEvent:
        Type: ScheduleV2
        Properties:
          ScheduleExpression: "rate(1 minute)"
      ComplexScheduleEvent:
        Type: ScheduleV2
        Properties:
          ScheduleExpression: rate(1 minute)
          FlexibleTimeWindow:
            Mode: FLEXIBLE
            MaximumWindowInMinutes: 5
          StartDate: '2022-12-28T12:00:00.000Z'
          EndDate: '2023-01-28T12:00:00.000Z'
          ScheduleExpressionTimezone: UTC
          RetryPolicy:
            MaximumRetryAttempts: 5
            MaximumEventAgeInSeconds: 300
          DeadLetterConfig:
            Type: SQS
    DefinitionUri:
      Bucket: sam-sam-s3-demo-bucket
      Key: my-state-machine.asl.json
      Version: 3
    Policies:
      - LambdaInvokePolicy:
          FunctionName: !Ref MyFunction
```
