# Events in Amazon EventBridge

An _event_ indicates a change in an environment such as an AWS
environment, a SaaS partner service or application, or one of your applications or services.
The following are examples of events:

- Amazon EC2 generates an event when the state of an instance changes, such as from pending to
  running.
- AWS CloudFormation generates an event when it creates, updates, or deletes a stack.
- AWS CloudTrail publishes events when you make API calls.
  You can also set up scheduled events that are generated on a periodic basis.

Events are represented as JSON objects and they all have a similar structure, and the same
top-level fields. For more information, see [Event
structure](../ref/welcome.md#overiew-event-structure "../ref/welcome.md#overiew-event-structure") in the _EventBridge Events Reference_.

## Events from AWS services

Many AWS services generate events that EventBridge receives.
When an AWS service in your account sends an event to EventBridge, it goes to your account’s default
event bus.

For a list of AWS services that send events to EventBridge, and the events they send, see the [EventBridge Events Reference](../ref/welcome.md "../ref/welcome.md").

AWS services send events to EventBridge on a _durable_ or _best-effort basis_. For more information, see
[Event delivery level](../ref/welcome.md#event-delivery-level "../ref/welcome.md#event-delivery-level") in the _EventBridge Events Reference_.

The following video explains the basics of events:

The following video covers the ways events get to EventBridge:
