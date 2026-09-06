

# Events in Amazon EventBridge
<a name="eb-events"></a>

An *event* indicates a change in an environment such as an AWS environment, a SaaS partner service or application, or one of your applications or services. The following are examples of events:
+ Amazon EC2 generates an event when the state of an instance changes, such as from pending to running.
+ AWS CloudFormation generates an event when it creates, updates, or deletes a stack.
+ AWS CloudTrail publishes events when you make API calls.

You can also set up scheduled events that are generated on a periodic basis. 

Events are represented as JSON objects and they all have a similar structure, and the same top-level fields. For more information, see [Event structure](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html#overiew-event-structure) in the *EventBridge Events Reference*.

## Events from AWS services
<a name="eb-service-event"></a>

Many AWS services generate events that EventBridge receives. When an AWS service in your account sends an event to EventBridge, it goes to your account’s default event bus.

For a list of AWS services that send events to EventBridge, and the events they send, see the [EventBridge Events Reference](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html).

AWS services send events to EventBridge on a *durable* or *best-effort basis*. For more information, see [Event delivery level](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html#event-delivery-level) in the *EventBridge Events Reference*.

 The following video explains the basics of events:




 The following video covers the ways events get to EventBridge:


