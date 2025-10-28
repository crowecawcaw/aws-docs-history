# Integrating Connector for AD into

event-driven applications using Amazon EventBridge

You can incorporate Connector for AD into event-driven applications (EDAs) that
use events that occur in Connector for AD to communicate between application
components and initiate downstream processes.

For example, you could invoke other AWS services or custom components when the following
Connector for AD events occur in your account:

- A certificate is created or when creation fails.
- A certificate is enrolled, or enrollment fails.
  You do this by using Amazon EventBridge to route events from Connector for AD to other
  software components. Amazon EventBridge is a serverless service that uses events to connect
  application components together, making it easier for you to integrate AWS services like
  Connector for AD into event-driven architectures without additional code and
  operations.

## How EventBridge routes

Connector for AD events

Here's how EventBridge works with Connector for AD events:

As with many AWS services, Connector for AD generates and sends events to
the EventBridge default _event bus_. An event bus is a router that receives
events and routes them to the destinations, or _targets_, that you
specify. Targets can include other AWS services, custom applications, and SaaS partner
applications.

EventBridge routes events according to _rules_ you create on the event
bus. For each rule, you specify a filter, or _event pattern_, to
select only the events you want. Whenever an event is sent to the event bus, EventBridge
compares it against each rule. If the event matches the rule, EventBridge routes the event to
the specified target(s).

![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge routes the event to the targets specified for that rule.](images/eventbridge-integration-how-it-works.png)

## Connector for AD events

For a list of Connector for AD events sent to EventBridge, refer to the
Connector for AD topic in the [_EventBridge Events
Reference_](../../../eventbridge/latest/ref/events-ref-pca-connector-ad.md "../../../eventbridge/latest/ref/events-ref-pca-connector-ad.md").

### Event structure

All events from AWS services contain two types of data:

- A common set of fields containing metadata about the event, such as the
  AWS service that is the source of the event, the time the event was
  generated, the account and region in which the event took place, and others.
  For definitions of these general fields, see [Event
  structure](../../../eventbridge/latest/ref/overiew-event-structure.md "../../../eventbridge/latest/ref/overiew-event-structure.md") in the _Amazon EventBridge Events
  Reference_.
- A `detail` field that contains data specific to that particular
  service event.

## Creating event patterns that match

Connector for AD events

Event patterns are filters where specify what data the events you want to select
should contain.

Each event pattern is a JSON object that contains:

- A `source` attribute that identifies the service sending the event.
  For Connector for AD events, the source is
  `aws.pca-connector-ad`.
- (Optional): A `detail-type` attribute that contains an array of the
  event names to match.
- (Optional): A `detail` attribute containing any other event data on
  which to match.

For example, the following event pattern would select all Certificate Policy Enrollment Succeeded events from
Connector for AD:

```
{
  "source": ["aws.pca-connector-ad"],
  "detail-type": ["Certificate Policy Enrollment Succeeded"]
}
```

For more information on writing event patterns, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
the _EventBridge User Guide_.

## Receiving events from EventBridge

You can specify Connector for AD certificates as the target for
a rule. This enables Connector for AD to receive events from a wide variety
of sources, including other AWS services, custom applications, and SaaS partners. For
more information, see [Creating rules that react to
events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _EventBridge User Guide_.

For a full list of the AWS services that you can specify as targets, see [Target
types](../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets "../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets") in the _EventBridge Events Reference_.
