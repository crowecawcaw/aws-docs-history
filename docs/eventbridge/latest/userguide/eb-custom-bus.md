

# Amazon EventBridge event bus (Custom)
<a name="eb-custom-bus"></a>

The EventBridge Custom Event Bus is an event bus that routes events to subscribers and retains them for a period that you choose. Producers publish events to the bus. Consumers create *subscribers* on the bus. Each subscriber filters the events, optionally transforms them, and delivers each matching event to one target. Because the bus retains events, a subscriber can deliver events in order, start from a point in the past, and pause and resume without losing events.

EventBridge also provides Custom Event Bus - Classic, the event bus that uses rules and targets. The two products share the `events:` IAM namespace and the `events.amazonaws.com` service principal, and both remain available. This chapter describes the Custom Event Bus. For Custom Event Bus - Classic, see [Amazon EventBridge event bus (default and Classic)](eb-event-bus.md). To move existing rules to subscribers, see [Migrating from Custom Event Bus - Classic to the Custom Event Bus](eb-custom-bus-migrate.md).

This chapter contains the following topics:
+ [What is the EventBridge Custom Event Bus?](eb-custom-bus-what-is.md)
+ [Creating a bus](eb-custom-bus-create.md)
+ [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md)
+ [Publishing events to a Custom Event Bus](eb-custom-bus-publish.md)
+ [Subscribing to events on a Custom Event Bus](eb-custom-bus-subscribers.md)
+ [Ordering and deduplicating events on a Custom Event Bus](eb-custom-bus-ordering.md)
+ [Migrating from Custom Event Bus - Classic to the Custom Event Bus](eb-custom-bus-migrate.md)
+ [Access control for the Custom Event Bus](eb-custom-bus-access.md)
+ [Encryption at Rest for Amazon EventBridge Custom Event Bus](eb-custom-bus-encryption.md)
+ [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md)
+ [Creating Custom Event Bus resources with CloudFormation](eb-custom-bus-cloudformation.md)
+ [Names, endpoints, and IAM permissions for the Custom Event Bus](eb-custom-bus-names.md)