# Changing the schedule state in EventBridge Scheduler

An EventBridge Scheduler schedule has two states: _enabled_ and _disabled_.
The following example uses `UpdateSchedule` to disable a schedule
that fires every five minutes and invokes a Lambda target.

When you use `UpdateSchedule`, you must provide all required parameters. EventBridge Scheduler replaces your schedule with the information you provide.
If you do not specify a parameter that you've previously set, it defaults to `null`.

###### Example AWS CLI

```
`$` `aws scheduler update-schedule --name lambda-universal --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "`ROLE_ARN`", "Arn":"arn:aws:scheduler:::aws-sdk:lambda:invoke" "Input": "{\"FunctionName\":\"arn:aws:lambda:`REGION`:123456789012:function:HelloWorld\",\"InvocationType\":\"Event\",\"Payload\":\"{\\\"message\\\":\\\"testing function\\\"}\"}" }' \
--flexible-time-window '{ "Mode": "OFF"}' \
**--state DISABLED**`
```

```
{
    "ScheduleArn": "arn:aws:scheduler:us-west-2:123456789012:schedule/default/lambda-universal"
}
```

The following example uses the Python SDK and the `UpdateSchedule` operation to disable a schedule that targets Amazon SQS using a templated target.

###### Example Python SDK

```
import boto3
scheduler = boto3.client('scheduler')

sqs_templated = {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<QUEUE_ARN>",
    "Input": "{}"}

flex_window = { "Mode": "OFF" }

scheduler.update_schedule(Name="your-schedule",
    ScheduleExpression="rate(5 minutes)",
    Target=sqs_templated,
    FlexibleTimeWindow=flex_window,
    State='DISABLED')
```
