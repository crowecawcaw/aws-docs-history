# AWS Batch event stream for Amazon EventBridge

You can use the AWS Batch event stream for Amazon EventBridge to receive near real-time notifications regarding the current
state of jobs in your job queues.

You can use EventBridge to gain further insights about your AWS Batch service. More specifically, you can use it to check
the progress of jobs, build AWS Batch custom workflows, generate usage reports or metrics, or build your own dashboards.
With AWS Batch and EventBridge, you don't need scheduling and monitoring code that continuously polls AWS Batch for job status
changes. Instead, you can handle AWS Batch job state changes asynchronously using a variety of Amazon EventBridge targets. These
include AWS Lambda, Amazon Simple Queue Service, Amazon Simple Notification Service, or Amazon Kinesis Data Streams.

Events from the AWS Batch event stream are ensured to be delivered at least one time. In the event that duplicate
events are sent, the event provides enough information to identify duplicates. That way, you can compare the time
stamp of the event and the job
status.

AWS Batch jobs are available as EventBridge targets. Using simple rules, you can match events and submit AWS Batch jobs in
response to them. For more information, see [What is EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _Amazon EventBridge User
Guide_. You can also use EventBridge to schedule automated actions that self-trigger at certain times using
**cron** or rate expressions. For more information, see [Creating an Amazon EventBridge rule that runs on a
schedule](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md") in the _Amazon EventBridge User Guide_. For an example walkthrough, see [AWS Batch jobs as EventBridge targets](batch-cwe-target.md "batch-cwe-target.md"). For information about using the EventBridge Scheduler, see [Setting up Amazon EventBridge Scheduler](../../../scheduler/latest/UserGuide/setting-up.md "../../../scheduler/latest/UserGuide/setting-up.md")
in the Amazon EventBridge User Guide.

###### Topics

- [AWS Batch events](batch_cwe_events.md "batch_cwe_events.md")
- [Tutorial: Use AWS user notifications with
  AWS Batch](using-user-notifications.md "using-user-notifications.md")
- [AWS Batch jobs as EventBridge targets](batch-cwe-target.md "batch-cwe-target.md")
- [Tutorial: Listen for AWS Batch job events using EventBridge](batch_cwet.md "batch_cwet.md")
- [Tutorial: Sending Amazon Simple Notification Service alerts for failed job events](batch_sns_tutorial.md "batch_sns_tutorial.md")
