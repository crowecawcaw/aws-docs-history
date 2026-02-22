# Tutorial: Schedule a AWS Lambda function

###### Note

Scheduled rules are a legacy feature of EventBridge.

EventBridge
offers a more flexible and powerful way to create, run, and manage scheduled tasks
centrally, at scale: EventBridge Scheduler. With EventBridge Scheduler, you can create schedules using cron
and rate expressions for recurring patterns, or configure one-time invocations. You can set
up flexible time windows for delivery, define retry limits, and set the maximum retention
time for failed API invocations.

Scheduler is highly customizable, and offers improved scalability over scheduled rules, with a wider set of target API operations and AWS services.
We recommend that you use Scheduler to invoke targets on a schedule.

For more information, see [Create a schedule](using-eventbridge-scheduler.md#using-eventbridge-scheduler-create "using-eventbridge-scheduler.md#using-eventbridge-scheduler-create") or the _[EventBridge Scheduler User Guide](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md")_.

This tutorial previously demonstrated how to invoke a Lambda function on a schedule
using EventBridge scheduled rules. We now recommend using Amazon EventBridge Scheduler instead. EventBridge Scheduler offers
improved scalability, a wider set of target API operations, flexible time windows,
and built-in retry and dead-letter queue support.

For a complete walkthrough of scheduling a Lambda function using EventBridge Scheduler, see
[Invoke a Lambda function on a schedule](../../../lambda/latest/dg/with-eventbridge-scheduler.md "../../../lambda/latest/dg/with-eventbridge-scheduler.md")
in the _AWS Lambda Developer Guide_.

For more information about EventBridge Scheduler, including how to create schedules using the console,
AWS CLI, or SDKs, see the
[Amazon EventBridge Scheduler User Guide](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md").

If you still need to use EventBridge scheduled rules, see
[Creating a scheduled rule (legacy) in Amazon EventBridge](eb-create-rule-schedule.md "eb-create-rule-schedule.md").
