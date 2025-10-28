# Enable three-party call monitoring in

Amazon Connect

###### Important

This topic applies only if you have **NOT** enabled
**Enhanced contact monitoring capabilities** on the Amazon Connect
console as explained in [Enable enhanced multi-party contact
monitoring](monitor-conversations.md "monitor-conversations.md").

It only applies to voice calls that are limited to three parties or less.

For information about how the conferencing experience differs for agents when
enhanced monitoring capabilities are enabled, see [Comparison of
multi-party and three-party functionality](three-party-multi-party-comparison.md "three-party-multi-party-comparison.md").

We recommend choosing three-party monitoring only if you have an external system
that imposes a technical constraint that requires you to choose this option.
Otherwise, enhanced monitoring is the way to go. There is no pricing
difference.

You can add and configure a [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block to your flows to enable 3
participants on a contact, and 5 supervisors monitoring the call. Managers cannot barge
in to a call.

For example, you can have a group of 3 participants on the call at the same time. Up
to 5 supervisors can monitor the call.

The total number of participants on a call would look like this:

1. Customer - participant
2. Agent 1 - participant
3. Agent 2 - participant
4. Supervisor who can listen but not barge in the call
5. Supervisor who can listen but not barge in the call
6. Supervisor who can listen but not barge in the call
7. Supervisor who can listen but not barge in the call
8. Supervisor who can listen but not barge in the call
   To view a sample flow with the **Set recording behavior** block
   configured, see [Sample recording behavior in Amazon Connect](sample-recording-behavior.md "sample-recording-behavior.md").

###### Note

We recommend using the **Set recording behavior** block in an inbound or outbound whisper flow for
the most accurate behavior.

Using this block in a queue flow does not always guarantee that calls are
recorded. This is because the block might run after the contact is joined to the
agent.

###### To set up monitoring for three-party contacts

1. Log in to your Amazon Connect instance using an account that has permissions to edit
   flows.
2. On the navigation menu, choose **Routing**,
   **Flows**.

![Amazon Connect navigation menu, Routing, flows.](images/menu-contact-flows.png) 3. Open the flow that handles customer contacts you want to monitor. 4. In the flow, before the contact is connected to an agent, add a [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block to the flow. 5. To configure the [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block, under **Agent
and customer voice recording**, choose **On** and
then choose **Agent and Customer**. This only takes effect
after the agent joins the call. 6. Choose **Save** and then **Publish** to
publish the updated flow. 7. [Assign security
profile permissions](assign-permissions-to-review-recordings.md "assign-permissions-to-review-recordings.md") to managers monitor conversations. 8. Show managers how to monitor conversations.
