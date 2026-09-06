

# Integrating Connector for AD into event-driven applications using Amazon EventBridge
<a name="eventbridge-integration"></a>

You can incorporate Connector for AD into event-driven applications (EDAs) that use events that occur in Connector for AD to communicate between application components and initiate downstream processes. 

For example, you could invoke other AWS services or custom components when the following Connector for AD events occur in your account:
+ A certificate is created or when creation fails.
+ A certificate is enrolled, or enrollment fails.

You do this by using Amazon EventBridge to route events from Connector for AD to other software components. Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to integrate AWS services like Connector for AD into event-driven architectures without additional code and operations.

## How EventBridge routes Connector for AD events
<a name="eventbridge-routes-service-events"></a>

Here's how EventBridge works with Connector for AD events:

As with many AWS services, Connector for AD generates and sends events to the EventBridge default *event bus*. An event bus is a router that receives events and routes them to the destinations, or *targets*, that you specify. Targets can include other AWS services, custom applications, and SaaS partner applications. 

EventBridge routes events according to *rules* you create on the event bus. For each rule, you specify a filter, or *event pattern*, to select only the events you want. Whenever an event is sent to the event bus, EventBridge compares it against each rule. If the event matches the rule, EventBridge routes the event to the specified target(s).

![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge routes the event to the targets specified for that rule.](http://docs.aws.amazon.com/privateca/latest/userguide/images/eventbridge-integration-how-it-works.png)


## Connector for AD events
<a name="eventbridge-service-events"></a>

For a list of Connector for AD events sent to EventBridge, refer to the Connector for AD topic in the [*EventBridge Events Reference*](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-pca-connector-ad.html).

### Event structure
<a name="eventbridge-event-structure"></a>

All events from AWS services contain two types of data:
+ A common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others. For definitions of these general fields, see [Event structure ](https://docs.aws.amazon.com/eventbridge/latest/ref/overiew-event-structure.html) in the *Amazon EventBridge Events Reference*. 
+ A `detail` field that contains data specific to that particular service event. 

## Creating event patterns that match Connector for AD events
<a name="eventbridge-event-delivery-filter"></a>

Event patterns are filters where specify what data the events you want to select should contain.

Each event pattern is a JSON object that contains:
+ A `source` attribute that identifies the service sending the event. For Connector for AD events, the source is `aws.pca-connector-ad`.
+ (Optional): A `detail-type` attribute that contains an array of the event names to match.
+ (Optional): A `detail` attribute containing any other event data on which to match.

For example, the following event pattern would select all Certificate Policy Enrollment Succeeded events from Connector for AD:

```
{
  "source": ["aws.pca-connector-ad"],
  "detail-type": ["Certificate Policy Enrollment Succeeded"]
}
```

For more information on writing event patterns, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *EventBridge User Guide*.

## Receiving events from EventBridge
<a name="eventbridge-service-as-target"></a>

You can specify Connector for AD certificates as the target for a rule. This enables Connector for AD to receive events from a wide variety of sources, including other AWS services, custom applications, and SaaS partners. For more information, see [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *EventBridge User Guide*. 

For a full list of the AWS services that you can specify as targets, see [Target types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets) in the *EventBridge Events Reference*. 