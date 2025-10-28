# Managing a schedule in EventBridge Scheduler

A _schedule_ is the main resource you create, configure, and manage using Amazon EventBridge Scheduler.

Every schedule has a _schedule expression_ that determines when, and with what frequency, the schedule runs. EventBridge Scheduler supports three types of schedules: rate, cron, and one-time schedules. For more
information about different schedule types, see [Schedule types in EventBridge Scheduler](schedule-types.md "schedule-types.md").

When you create a schedule, you configure a target for the schedule to invoke. A target is an API operation that EventBridge Scheduler calls on your behalf every time your schedule runs.
EventBridge Scheduler supports two types of targets: _templated_ targets call common API operations across a core groups of services, and the _universal target parameter (UTP)_ that you can use to call more than 6,000 operations
across over 270 services. For more information about configuring targets, see [Managing targets in EventBridge Scheduler](managing-targets.md "managing-targets.md").

You configure how your schedule handles failures, when EventBridge Scheduler is unable to deliver an event successfully to a target, by using two primary mechanisms: a _retry policy_, and a _dead-letter queue (DLQ)_.
A retry policy determines the number of times EventBridge Scheduler must retry a failed event, and how long to keep an unprocessed event. A DLQ is a standard Amazon SQS queue EventBridge Scheduler uses to deliver failed events to, after the retry policy has been exhausted.
You can use a DLQ to troubleshoot issues with your schedule or its downstream target. For more information about, see [Configuring a schedule's dead-letter queue in EventBridge Scheduler](configuring-schedule-dlq.md "configuring-schedule-dlq.md").

In this section, you can find examples for managing your EventBridge Scheduler schedules using the console, the AWS CLI and the EventBridge Scheduler SDKs.

###### Topics

- [Changing the schedule state in EventBridge Scheduler](managing-schedule-state.md "managing-schedule-state.md")
- [Configuring flexible time windows in EventBridge Scheduler](managing-schedule-flexible-time-windows.md "managing-schedule-flexible-time-windows.md")
- [Configuring a schedule's dead-letter queue in EventBridge Scheduler](configuring-schedule-dlq.md "configuring-schedule-dlq.md")
- [Deleting a schedule in EventBridge Scheduler](managing-schedule-delete.md "managing-schedule-delete.md")
- [What's next?](#managing-schedule-whats-next "#managing-schedule-whats-next")

## What's next?

- For more information on how you can configure templated targets for Lambda and Step Functions, and to learn about using the universal target parameter,
  see [Managing targets in EventBridge Scheduler](managing-targets.md "managing-targets.md").
- For more information about the EventBridge Scheduler data types and API operations, see the [EventBridge Scheduler API Reference](../APIReference.md "../APIReference.md").
