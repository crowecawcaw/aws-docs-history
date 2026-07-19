# EventBridge notifications

With Amazon EventBridge, you can monitor resources in the next generation of Resilience Hub using event-driven rules.
These rules can trigger actions in other AWS services. For example, you can create a rule
that signals an Amazon SNS topic whenever a failure mode assessment completes.

You can create rules in EventBridge to act on the following events from the next generation of Resilience Hub:

- **Failure Mode Assessment Completed** – Emitted
  when a failure mode assessment completes successfully.
- **Failure Mode Assessment Failed** – Emitted when
  a failure mode assessment workflow fails.
- **Failure Mode Assessment Queued** – Emitted when
  an assessment is queued for delayed processing. The assessment is retried within 24
  hours.
- **Failure Mode Finding Resolved** – Emitted when a
  failure mode finding is marked as Resolved or Irrelevant.
  To capture specific events from the next generation of Resilience Hub that you're interested in, define
  event-specific patterns that EventBridge can use to detect the events. Event patterns have the same
  structure as the events that they match. The pattern quotes the fields that you want to match
  and provides the values that you're looking for.

Next generation Resilience Hub emits events on a best-effort basis and delivers them to EventBridge
in near real-time when the service is operating normally. However, some situations might
delay or prevent event delivery.

For more information about EventBridge rules and event patterns, see
[Events
and event patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md").
