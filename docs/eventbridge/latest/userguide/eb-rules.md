# Rules in Amazon EventBridge

You specify what EventBridge does with the events delivered to each event bus. To do
this, you create _rules_. A rule specifies which
events to send to which [targets](eb-targets.md "eb-targets.md") for processing. A single
rule can send an event to multiple targets, which then run in parallel.

You can create two types of rules: rules that match on event data as events are delivered, and rules that run on a defined schedule.
In addition, certain AWS services may create and manage rules in your account as well.

## Rules that match on event data

You can create rules that match against incoming events based on event data
criteria (called an _event pattern_). An event
pattern defines the event structure and the fields that a rule
matches. If an event matches the criteria defined in the event pattern, EventBridge sends it to the target(s) you specify.

For more information, see [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md").

## Rules that run on a schedule

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

You can also create rules that sends events to the specified targets at specified
intervals. For example, to periodically run an Lambda function, you can
create a rule to run on a schedule.

For more information, see [Creating a scheduled rule (legacy) in Amazon EventBridge](eb-create-rule-schedule.md "eb-create-rule-schedule.md").

## Rules managed by AWS services

In addition to the rules you create, AWS services can create and manage
EventBridge rules in your AWS account that are needed for
certain functions in those services. These are called _managed
rules_.

When a service creates a managed rule, it can also create an [IAM policy](eb-iam.md "eb-iam.md") that grants permission to that service to
create the rule. IAM policies created this way are scoped narrowly with resource-level
permissions to allow the creation of only the necessary rules.

You can delete managed rules by using the **Force delete** option,
but you should only delete them if you're sure that the other service no longer needs
the rule. Otherwise, deleting a managed rule causes the features that rely on it to stop
working.
