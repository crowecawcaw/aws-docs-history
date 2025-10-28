# Integrating with CodeGuru Profiler

This section provides an overview of how Amazon DevOps Guru integrates with Amazon CodeGuru Profiler. You can
view recommendations from CodeGuru Profiler as insights in the DevOps Guru console.

Amazon DevOps Guru integrates with Amazon CodeGuru Profiler with an EventBridge managed rule. CodeGuru Profiler sends events
to EventBridge. The managed rule routes events that are sent with the default event bus.
Each inbound event from CodeGuru Profiler is a proactive anomaly report. For more information, see
[Working with EventBridge
with CodeGuru Profiler](../../../codeguru/latest/profiler-ug/working-with-eventbridge.md "../../../codeguru/latest/profiler-ug/working-with-eventbridge.md").

DevOps Guru supports inbound events with EventBridge. An event indicates a change in a
recommendation that DevOps Guru identified. CodeGuru Profiler sends a heartbeat event every 24 hours to show
the continuity of the event. Events carry CodeGuru Profiler recommendation information as well as
metadata for your compute resources. For information on an event lifecycle, see [Amazon
EventBridge Events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

When you set up DevOps Guru, DevOps Guru creates the EventBridge Managed Rule in your account that
routes events from another service. This rule routes to DevOps Guru. Notifications are sent when
there is an inbound event.

An event bus receives events from a source such as DevOps Guru and routes them to rules
associated with that event bus. For more information on event buses, see [Event
buses](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md").

For information on some of the parameters, see [Amazon EventBridge
events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

To receive CodeGuru Profiler insights in DevOps Guru, you must have the following.

- CodeGuru Profiler must be enabled. For information on enabling CodeGuru Profiler, see [Setting
  up CodeGuru Profiler](../../../codeguru/latest/profiler-ug/setting-up.md "../../../codeguru/latest/profiler-ug/setting-up.md").
- DevOps Guru must be enabled. For information on enabling DevOps Guru, see [Enable
  DevOps Guru](getting-started-enable-service.md "getting-started-enable-service.md").
- The same resources must be monitored in the same Region in both CodeGuru Profiler and DevOps Guru.
