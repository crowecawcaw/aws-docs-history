# Tutorial: Schedule automated Amazon EBS snapshots

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

This tutorial previously demonstrated how to create automated Amazon EBS snapshots
using EventBridge scheduled rules. We now recommend using one of the following
alternatives, depending on your use case.

## Recommended: Amazon Data Lifecycle Manager

For automated Amazon EBS snapshot lifecycle management, including creation, retention,
and deletion on a schedule, we recommend
[Amazon Data Lifecycle Manager](../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md "../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md") (Amazon Data Lifecycle Manager).
Amazon Data Lifecycle Manager is purpose-built for Amazon EBS snapshot automation and provides policy-based
lifecycle management without requiring you to build and maintain scheduling
infrastructure.

## Alternative: Amazon EventBridge Scheduler

If you need more flexible scheduling options or want to combine snapshot creation
with other AWS API actions, you can use Amazon EventBridge Scheduler. EventBridge Scheduler offers improved
scalability over EventBridge scheduled rules, with a wider set of target API operations,
flexible time windows, and built-in retry support.

To get started with EventBridge Scheduler, see
[Getting started with Amazon EventBridge Scheduler](../../../scheduler/latest/UserGuide/getting-started.md "../../../scheduler/latest/UserGuide/getting-started.md")
in the _Amazon EventBridge Scheduler User Guide_.

## Legacy: EventBridge scheduled rules

If you still need to use EventBridge scheduled rules, see
[Creating a scheduled rule (legacy) in Amazon EventBridge](eb-create-rule-schedule.md "eb-create-rule-schedule.md").
