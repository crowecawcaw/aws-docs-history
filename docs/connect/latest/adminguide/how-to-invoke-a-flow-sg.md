

# Invoke a guide at the start of a contact in Connect Customer
<a name="how-to-invoke-a-flow-sg"></a>

After you create your flows, you can choose which guide each user sees. To do this:

1. Add a [Set event flow](set-event-flow.md) block to your flow.

1. In the **Set event flow** block, configure a **Default flow for Agent UI** event hook.

You can branch on IVR responses, the queue name, or customer information to decide which flow ID to set. Use the [Check contact attributes](check-contact-attributes.md) block for the conditions, and the [Set event flow](set-event-flow.md) block to set the flow to run.

Guides start as soon as the contact is offered to the agent. They don't wait for the contact to be accepted.

The following image shows the **Properties** page for the **Set event flow** block. The event hook is set to **Default flow for Agent UI**.

![The Set event flow block, the Default flow for Agent UI event hook.](https://docs.aws.amazon.com/connect/latest/adminguide/images/example-flow-id-sq.png)
