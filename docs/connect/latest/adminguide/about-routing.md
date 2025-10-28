# How routing works in Amazon Connect

Contacts are routed through your contact center based on these factors:

- The routing profile assigned to the agent.
- The hours of operation for a given queue.
- The routing logic you define in your flows.
  For example, you use routing profiles to route specific types of contacts to agents
  with specific skill sets. If no agent with the required skill set is available, you can
  place the contact in the queue defined in the flow.

Here's the logic Amazon Connect uses to route contacts:

- Contacts in a queue are automatically prioritized and forwarded to the next
  available agent (that is, the agent who has been
  idle longest).
- Contacts are placed on hold if there are no available agents. The order in
  which they are serviced is determined by their time in queue, on a first-come,
  first-served basis.
- If multiple agents are ready for a contact, by default an inbound contact is
  routed to the agent who has been in the **Available** status
  for the longest time.

###### Tip

For information about how queue priority and delay work, see [Queues: priority and
delay examples](concepts-routing-profiles-priority.md "concepts-routing-profiles-priority.md").

Handling either inbound or outbound contacts causes agents to drop to the
bottom of the list for inbound contacts. You can set up your [routing profile](routing-profiles.md "routing-profiles.md") to ignore outbound
contacts in this calculation by choosing the **Outbound calls should not
impact routing order** option. Consider choosing this option if
your organization wants agents to take outbound calls and still get a fair share
of inbound contacts.

For example:

    + An agent named Joe is idle. He is third in line to receive an inbound
     contact. He would rather handle an inbound contact than an outbound
     contact because he knows he will speak to a customer, whereas an
     outbound contact may not pick up the phone. Talking to an inbound
     contact increases his odds of getting recognition in his role.
    + Because he is idle, Joe decides to make an outbound contact to chip
     away at the backlog. He may or may not reach someone.
    + By default, when Joe makes the outbound contact, he moves from third
     in line to the bottom of the list of agents waiting to receive an
     inbound contact. (If there are 10 agents, he is moved to 10th place). If
     instead he should remain in third place, you can override the default
     behavior.

- A routing profile may assign a priority to one queue over another, but the
  priority within the queue is always set by the order the contact was added to
  the queue.
- If the contact belongs to a queue and channel combination that is **only** listed under the manually assigned section of a
  routing profile, that contact is **not** routed
  automatically to agents assigned to that routing profile.

## How routing transfers works

As the previous section explains, the order in which contacts in queue are handled
in Amazon Connect depends on multiple factors, including the enqueue time, routing age
adjustment, and contact priority. In the case of contacts that experience a
transfer, however, Amazon Connect handles the routing age adjustment slightly differently: it
depends on whether the contact was transferred by an agent, or if it was transferred
by a queue-to-queue transfer in a flow or an API.

The following two scenarios demonstrate how Amazon Connect handles the routing age
adjustment.

- **Agent transfers the contact using a quick
  connect**: A contact is originally enqueued at time **X** and is then handled by an agent. The agent then
  transfers it back to a queue using a quick connect at time **Y**. In this scenario:
  - The original enqueue time **X** is
    used to calculate the order in which this contact is ranked in the
    subsequent queue.
  - Any routing age adjustments are applied relative to that contact
    enqueue time.

- **Queue-to-queue transfer**: A contact was in
  a queue from time **S** and is eventually
  transferred to a different queue at time **T**.
  In this scenario:
  - The new enqueue time **T** is used to
    calculate the order in which the contact is ranked.
  - Any routing age adjustments are applied relative to that contact
    enqueue time.

## How routing works with multiple

channels

When you set up a routing profile to handle multiple channels, you must specify
whether agents can handle contacts while already on another channel. This is called
cross-channel concurrency.

When using cross-channel concurrency, Amazon Connect checks which contact to offer the
agent as follows:

1. It checks what contacts/channels the agent is currently handling.
2. Based on what channels they are currently handling, and the cross-channel
   configuration in the agent's routing profile, it determines whether the
   agent can be routed the next contact.

For a detailed example of how Amazon Connect routes contacts when cross-channel concurrency
is set up, see [Example of how a contact is routed
with cross-channel concurrency](routing-profiles.md#example-routing-concurrency "routing-profiles.md#example-routing-concurrency").

## How routing works with

manual assignment

When you set up a routing profile that has queues and channels listed for manual
assignment, Amazon Connect does not automatically route these contacts.

Agents with this routing profile can view queued contacts (currently only
supported for Tasks, Emails, and Chats) in the worklist app in their agent
workspaces based on their security profile settings and determine the next important
work item to assign to themselves.

## Learn more about routing

See the following topics to learn more about routing:

- [Queues: priority and
  delay examples](concepts-routing-profiles-priority.md "concepts-routing-profiles-priority.md").
- [How Amazon Connect uses routing profiles](concepts-routing.md "concepts-routing.md")
- [Queue-based routing to route customers to
  a specific contact center agent](concepts-queue-based-routing.md "concepts-queue-based-routing.md")
- [Set up queue-based
  routing](set-up-queue-based-routing.md "set-up-queue-based-routing.md")
