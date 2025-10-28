# Configuring flexible time windows in EventBridge Scheduler

When you configure your schedule with a flexible time window, EventBridge Scheduler invokes the target within the time window you set.
This is useful in cases that do not require precise scheduled invocation of targets. Setting a flexible time window improves the
reliability of your schedule by dispersing your target invocations.

For example, if you configure a 15 minute flexible time window for a schedule that runs every hour, it invokes the target
within 15 minutes after the scheduled time. The following AWS CLI, and EventBridge Scheduler SDK examples use `UpdateSchedule`
to set a 15 minute flexible time window for a schedule that runs once every hour.

###### Note

You must specify whether you want to set a flexible time window or not. If you do not want to set this option, specify `OFF`. If you do set the value to `FLEXIBLE`, you must then specify a maximum window of time during which
you schedule will run.

###### Example AWS CLI

```
`$` `aws scheduler update-schedule --name lambda-universal --schedule-expression 'rate(1 hour)' \
--target '{"RoleArn": "`ROLE_ARN`", "Arn":"arn:aws:scheduler:::aws-sdk:lambda:invoke" "Input": "{\"FunctionName\":\"arn:aws:lambda:`REGION`:123456789012:function:HelloWorld\",\"InvocationType\":\"Event\",\"Payload\":\"{\\\"message\\\":\\\"testing function\\\"}\"}" }' \
--flexible-time-window '{ "Mode": "FLEXIBLE", "MaximumWindowInMinutes": 15} \`
```

```
{
    "ScheduleArn": "arn:aws:scheduler:us-west-2:123456789012:schedule/lambda-universal"
}
```

###### Example Python SDK

```
import boto3
scheduler = boto3.client('scheduler')

sqs_templated = {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<QUEUE_ARN>",
    "Input": "{}"}

flex_window = { "Mode": "FLEXIBLE", "MaximumWindowInMinutes": 15}

scheduler.update_schedule(Name="your-schedule",
    ScheduleExpression="rate(1 hour)",
    Target=sqs_templated,
    FlexibleTimeWindow=flex_window)

```
