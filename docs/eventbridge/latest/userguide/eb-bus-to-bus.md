# Sending events between event buses in

the same account and Region in Amazon EventBridge

You can configure EventBridge to send and receive [events](eb-events.md "eb-events.md") between
[event buses](eb-event-bus.md "eb-event-bus.md") in the same AWS account and Region.

When you configure EventBridge to send or receive events between event buses, you use IAM roles
on the _sender_ event bus to give the _sender_ event
bus permission to send events to the _receiver_ event bus. You use [Resource-based](eb-use-resource-based.md "eb-use-resource-based.md") policies on the
_receiver_ event bus to give the _receiver_ event
bus permission to receive events from the _sender_ event bus. You can
also allow or deny events from certain event buses, specific [rules](eb-rules.md "eb-rules.md") associated with the event bus, or events from specific sources. For more
information about event bus permissions, including example policies, see [Permissions for event buses in Amazon EventBridge](eb-event-bus-perms.md "eb-event-bus-perms.md").

The steps to configure EventBridge to send events to or receive events between event buses in
your account include the following:

- To use an existing IAM role, you need to give either the sender event bus
  permissions to the receiver event bus or the receiver event bus permissions to the
  sender event bus.
- On the _sender_ event bus, set up one or more rules that have
  the receiver event bus as the target and create an IAM role. For an example of the policy that should be attached to the role, see [Example policy: Send events to an event bus in the same account in Amazon EventBridge](eb-event-bus-example-policy-same-account.md "eb-event-bus-example-policy-same-account.md").
- On the _receiver_ event bus, edit the permissions to allow
  events to be passed from the other event bus.
- On the _receiver_ event, set up one or more rules that match
  events that come from the sender event bus.

###### Note

EventBridge can't route events received from a sender event bus to a third event
bus.
Events sent from one event bus to another are charged as custom events. For more
information, see [Amazon EventBridge
Pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/").

## Creating rules that send events

to a different event bus in the same AWS account and Region

To send events to another event bus, you create a rule with an event bus as a target.
Specifying an event bus in the same AWS account and Region as a target is part of
creating the rule.

###### To create a rule that sends events to a different event bus in the same AWS account and Region using the

console

1. Follow the steps in the [Creating rules that react to events in Amazon EventBridge](eb-create-rule.md "eb-create-rule.md") procedure.
2. In the [Select targets](eb-create-rule.md#eb-create-rule-target "eb-create-rule.md#eb-create-rule-target") step, when prompted to choose a target type:
   1. Select **EventBridge event bus**.
   2. Select **Event bus in the same AWS account and Region**.
   3. For **Event bus as a target**, select an event bus from the drop-down list.

3. Complete creating the rule following the procedure steps.
