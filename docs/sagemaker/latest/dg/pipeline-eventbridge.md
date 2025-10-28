# Schedule Pipeline Runs

You can schedule your Amazon SageMaker Pipelines executions using [Amazon EventBridge](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md"). Amazon SageMaker Pipelines is supported as a target in [Amazon EventBridge](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md"). This allows you to initiate the execution of your model building pipeline
based on any event in your event bus. With EventBridge, you can automate your pipeline executions and
respond automatically to events such as training job or endpoint status changes. Events include
a new file being uploaded to your Amazon S3 bucket, a change in status of your Amazon SageMaker AI endpoint due
to drift, and _Amazon Simple Notification Service_ (SNS) topics.

The following Pipelines actions can be automatically initiated: 

- `StartPipelineExecution`
  For more information on scheduling SageMaker AI jobs, see [Automating SageMaker AI with Amazon EventBridge.](automating-sagemaker-with-eventbridge.md "automating-sagemaker-with-eventbridge.md")

###### Topics

- [Schedule a Pipeline with Amazon EventBridge](#pipeline-eventbridge-schedule "#pipeline-eventbridge-schedule")
- [Schedule a pipeline with the SageMaker Python SDK](#build-and-manage-scheduling "#build-and-manage-scheduling")

## Schedule a Pipeline with Amazon EventBridge

To start a pipeline execution with Amazon CloudWatch Events, you must create an EventBridge [rule](../../../eventbridge/latest/APIReference/API_Rule.md "../../../eventbridge/latest/APIReference/API_Rule.md"). When you create a rule for events, you specify a target action to take when
EventBridge receives an event that matches the rule. When an event matches the rule, EventBridge sends the
event to the specified target and initiates the action defined in the rule.

The following tutorials show how to schedule a pipeline execution with EventBridge using the EventBridge
console or the AWS CLI. 

### Prerequisites

- A role that EventBridge can assume with the `SageMaker::StartPipelineExecution`
  permission. This role can be created automatically if you create a rule from the EventBridge
  console; otherwise, you need to create this role yourself. For information on creating a
  SageMaker AI role, see [SageMaker Roles](sagemaker-roles.md "sagemaker-roles.md").
- An Amazon SageMaker AI Pipeline to schedule. To create an Amazon SageMaker AI Pipeline, see [Define a
  Pipeline](define-pipeline.md "define-pipeline.md").

### Create an EventBridge rule using the EventBridge

console

The following procedure shows how to create an EventBridge rule using the EventBridge console. 

1. Navigate to the [EventBridge console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. Select **Rules** on the left hand side.
3. Select `Create Rule`.
4. Enter a name and
   description for your rule.
5. Select how you want to initiate this rule. You have the following choices for your
   rule:
   - **Event pattern**: Your rule is initiated when an
     event matching the pattern occurs. You can choose a predefined pattern that matches
     a certain type of event, or you can create a custom pattern. If you select a
     predefined pattern, you can edit the pattern to customize it. For more information
     on Event patterns, see [Event Patterns in CloudWatch Events](../../../AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.md "../../../AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.md").
   - **Schedule**: Your rule is initiated regularly on
     a specified schedule. You can use a fixed-rate schedule that initiates regularly for
     a specified number of minutes, hour, or weeks. You can also use a [cron expression](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions") to create a more fine-grained schedule, such as “the
     first Monday of each month at 8am.” Schedule is not supported on a custom or partner
     event bus.

6. Select your desired Event bus.
7. Select the target(s) to invoke when an event matches your event pattern or when the
   schedule is initiated. You can add up to 5 targets per rule. Select `SageMaker
Pipeline` in the target dropdown list.
8. Select the pipeline you want to initiate from the pipeline dropdown list.
9. Add parameters to pass to your pipeline execution using a name and value pair.
   Parameter values can be static or dynamic. For more information on Amazon SageMaker AI Pipeline
   parameters, see [AWS::Events::Rule SagemakerPipelineParameters](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.md#aws-resource-sagemaker-pipeline-properties "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.md#aws-resource-sagemaker-pipeline-properties").
   - Static values are passed to the pipeline execution every time the pipeline is
     initiated. For example, if `{"Name": "Instance_type",
"Value": "ml.4xlarge"}` is specified in the parameter
     list, then it is passed as a parameter in `StartPipelineExecutionRequest`
     every time EventBridge initiates the pipeline.
   - Dynamic values are specified using a JSON path. EventBridge parses the value from an
     event payload, then passes it to the pipeline execution. For example:
     _`$.detail.param.value`_

10. Select the role to use for this rule. You can either use an existing role or create
    a new one.
11. (Optional) Add tags.
12. Select `Create` to finalize your rule.

Your rule is now in effect and ready to initiate your pipeline executions.

### Create an EventBridge rule using the [AWS CLI](../../../cli/latest/reference/events/index.md "../../../cli/latest/reference/events/index.md")

The following procedure shows how to create an EventBridge rule using the AWS CLI.

1. Create a rule to be initiated. When creating an EventBridge rule using the AWS CLI, you have two
   options for how your rule is initiated, event pattern and schedule.
   - **Event pattern**: Your rule is initiated when an
     event matching the pattern occurs. You can choose a predefined pattern that matches
     a certain type of event, or you can create a custom pattern. If you select a
     predefined pattern, you can edit the pattern to customize it.  You can create a rule
     with event pattern using the following command:

   ```
   aws events put-rule --name `<RULE_NAME>` ----event-pattern `<YOUR_EVENT_PATTERN>` --description `<RULE_DESCRIPTION>` --role-arn `<ROLE_TO_EXECUTE_PIPELINE>` --tags `<TAGS>`
   ```

   - **Schedule**: Your rule is initiated regularly on a
     specified schedule. You can use a fixed-rate schedule that initiates regularly for a
     specified number of minutes, hour, or weeks. You can also use a cron expression to
     create a more fine-grained schedule, such as “the first Monday of each month at
     8am.” Schedule is not supported on a custom or partner event bus. You can create a
     rule with schedule using the following command:

   ```
   aws events put-rule --name `<RULE_NAME>` --schedule-expression `<YOUR_CRON_EXPRESSION>` --description `<RULE_DESCRIPTION>` --role-arn `<ROLE_TO_EXECUTE_PIPELINE>` --tags `<TAGS>`
   ```

2. Add target(s) to invoke when an event matches your event pattern or when the schedule
   is initiated. You can add up to 5 targets per rule.  For each target, you must specify: 
   - ARN: The resource ARN of your pipeline.
   - Role ARN: The ARN of the role EventBridge should assume to execute the pipeline.
   - Parameters:  Amazon SageMaker AI pipeline parameters to pass.

3. Run the following command to pass a Amazon SageMaker AI pipeline as a target to your rule using
   [put-targets](../../../cli/latest/reference/events/put-targets.md "../../../cli/latest/reference/events/put-targets.md") :

```
aws events put-targets --rule `<RULE_NAME>` --event-bus-name `<EVENT_BUS_NAME>` --targets "[{\"Id\": `<ID>`, \"Arn\": `<RESOURCE_ARN>`, \"RoleArn\": `<ROLE_ARN>`, \"SageMakerPipelineParameter\": { \"SageMakerParameterList\": [{\"Name\": `<NAME>`, \"Value\": `<VALUE>`}]} }]"] 
```

## Schedule a pipeline with the SageMaker Python SDK

The following sections show you how to set up permissions to access EventBridge resources and
create your pipeline schedule using the SageMaker Python SDK.

### Required permissions

You need to have necessary permissions to use the pipeline scheduler.
Complete the following steps to set up your permissions:

1. Attach the following minimum privilege policy to the IAM role used to
   create the pipeline triggers, or use the AWS managed policy
   `AmazonEventBridgeSchedulerFullAccess`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:ListSchedules",
 "scheduler:GetSchedule",
 "scheduler:CreateSchedule",
 "scheduler:UpdateSchedule",
 "scheduler:DeleteSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

2. Establish a trust relationship with EventBridge by adding
   the service principal `scheduler.amazonaws.com` to this role’s
   trust policy. Make sure you attach the following
   trust policy to the execution role if you launch the notebook
   in SageMaker Studio.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "scheduler.amazonaws.com",
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### Create a pipeline schedule

Using the `PipelineSchedule`
constructor, you can schedule
a pipeline to run once or at a predetermined interval. A pipeline schedule
must be of the type `at`, `rate`, or `cron`.
This set of scheduling types is an extension of the [EventBridge scheduling options](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md").
For more information about how to use the `PipelineSchedule` class, see [sagemaker.workflow.triggers.PipelineSchedule](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#pipeline-schedule "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#pipeline-schedule").
The following example demonstrates how to create each scheduling type with `PipelineSchedule`.

```
from sagemaker.workflow.triggers import PipelineSchedule

# schedules a pipeline run for 12/13/2023 at time 10:15:20 UTC
my_datetime_schedule = PipelineSchedule(
    name="`<schedule-name>`",
    at=datetime(2023, 12, 13, 10, 15, 20)
)

# schedules a pipeline run every 5 minutes
my_rate_schedule = PipelineSchedule(
    name="`<schedule-name>`",
    rate=(5, "minutes")
)

# schedules a pipeline run at 10:15am UTC on the last Friday of each month during the years 2022 to 2023
my_cron_schedule = PipelineSchedule(
    name="`<schedule-name>`",
    cron="15 10 ? * 6L 2022-2023"
)
```

###### Note

If you create a one-time schedule and need to access the current time, use
`datetime.utcnow()` instead of `datetime.now()`. The latter
does not store the current zone context and results in an incorrect time passed to EventBridge.

### Attach the trigger to your pipeline

To attach your `PipelineSchedule` to your pipeline, invoke the `put_triggers` call
on your created pipeline object with a list of triggers. If you get a response ARN,
you successfully created the schedule in your account and EventBridge begins to invoke
the target pipeline at the time or rate specified. You must specify a role with
correct permissions to attach triggers to a parent pipeline. If you don't provide one,
Pipelines fetches the default role used to create the pipeline from the [configuration file](train-remote-decorator-config.md "train-remote-decorator-config.md").

The following example demonstrates how to attach a schedule to a pipeline.

```
scheduled_pipeline = Pipeline(
    name="`<pipeline-name>`",
    steps=[...],
    sagemaker_session=`<sagemaker-session>`,
)
custom_schedule = PipelineSchedule(
    name="`<schedule-name>`",
    at=datetime(year=2023, month=12, date=25, hour=10, minute=30, second=30)
)
scheduled_pipeline.put_triggers(triggers=[custom_schedule], role_arn=`<role>`)
```

### Describe current triggers

To retrieve information about your created pipeline triggers, you can
invoke the `describe_trigger()` API with the trigger name. This command
returns details about the created schedule expression such as its start time,
enabled state, and other useful information. The following snippet shows a sample
invocation:

```
scheduled_pipeline.describe_trigger(name="`<schedule-name>`")
```

### Cleanup trigger resources

Before you delete your pipeline, clean up existing triggers to avoid a resource leak
in your account. You should delete the triggers before destroying the parent pipeline.
You can delete your triggers by passing a list of trigger names to the `delete_triggers`
API. The following snippet demonstrates how to delete triggers.

```
pipeline.delete_triggers(trigger_names=["`<schedule-name>`"])
```

###### Note

Be aware of the following limitations when you delete your triggers:

- The option to delete the triggers by specifying trigger names is only available
  in the SageMaker Python SDK. Deleting the pipeline in the CLI or a `DeletePipeline`
  API call does not delete your triggers. As a result, the triggers become orphaned
  and SageMaker AI attempts to start a run for a non-existent pipeline.
- Also, if you are using another notebook session or already deleted the
  pipeline target, clean up orphaned schedules through the scheduler [CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/delete-schedule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/delete-schedule.html")
  or EventBridge console.
