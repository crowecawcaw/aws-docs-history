# Contact initiation methods and flow types in

your Amazon Connect contact center

Every contact in your Amazon Connect contact center is initiated by one of the following methods:

- INBOUND
- OUTBOUND
- TRANSFER
- CALLBACK
- API
- QUEUE_TRANSFER
- DISCONNECT
- WEBRTC_API
- EXTERNAL_OUTBOUND
- MONITOR
- AGENT_REPLY
- FLOW
  The initiation method is stored in the `InitiationMethod` field of the contact
  record.

You can create flows appropriate for a given initiation method when you know which [types of flows](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") the initiation method uses.

For each initiation method, this topic explains which types of flows are run.

## INBOUND

The customer initiated a voice (phone) contact with your contact center.

- When the contact successfully connects with the phone number of your contact
  center, an [Inbound flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is presented
  to caller.
- During the transition in the **Inbound flow**, if the
  customer is put in a queue, a [Customer queue
  flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to customer.
- After the agent becomes available to handle the caller and accept the contact,
  a [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to the
  agent.
- After a [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")
  completes, a [Customer whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is
  played to customer.
- After the both whisper flows are played successfully to the agent and the
  customer respectively, the caller gets connected to agent for
  interaction.

To summarize, for a simple inbound call, the following flow types are played before
caller is connected to agent:

1. **Inbound flow**
2. **Customer queue flow**
3. **Agent whisper flow**
4. **Customer whisper flow**

## OUTBOUND

An agent initiated voice (phone) contact to an external number, by using their CCP to
make the call.

- As soon as the destination party picks the call, they are presented with an
  [Outbound whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types").
- After an **Outbound whisper flow** successfully completes,
  the agent and the contact are connected for interaction.

Before the call is made, all the blocks before the first **Play
prompt** are run. After the customer picks up, the first **Play
prompt** and all the blocks after it are run.

To summarize, an **Outbound flow** type is the only one involved in
an outbound call initiated from Amazon Connect.

## TRANSFER

The contact was transferred by an agent to another agent or to a queue, using quick
connects in the CCP. This results in a new contact record being created.

Before the agent transfers the contact to another agent or queue, all the flows
involved in an INBOUND contact are run.

- Agent to Agent transfer using Agent Quick Connect

      + After the agent transfers the inbound contact to another agent:




      	- A [Agent transfer
      	 flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to the source agent.
      	- After the destination agent accepts the call, a [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is
      	 played to destination agent, and then a [Customer whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is
      	 played to source agent.
      	- After all three flows are successfully run, the interaction
      	 begins between the source and destination agents.
      	- During this whole process, the inbound caller is on hold and a
      	 [Customer hold flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")
      	 is played to the inbound caller during hold time.
      After the source agent is connected with destination agent, the source
       agent can do one of the following actions:




      	- Choose **Join**. This joins all parties on
      	 the call: source agent, destination agent, and the customer are
      	 joined in a conference call.
      	- Choose **Hold all**. This puts the
      	 destination agent and the customer on hold.
      	- Put destination agent on hold, so only the source agent can
      	 talk to the customer.
      	- Choose **End call**. The source agent leaves
      	 the call but the destination agent and the customer are directly
      	 connected and continue talking.

  To summarize for an agent to agent transfer call, the following flow types are
  run:

      1. **Agent transfer flow**
      2. **Agent whisper flow** (played to the destination
       agent)
      3. **Customer whisper flow** (played to the source
       agent) during whole this process
      4. **Customer hold flow** played to the original
       caller

- Agent to Queue transfer using Queue Quick Connect

      + After the agent transfers the inbound call to another queue:




      	- A [Queue transfer
      	 flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to source agent.
      	- After the agent from the transferred queue accepts the call,
      	 an [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")
      	 is played to destination agent, and then a [Customer whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is
      	 played to source agent.
      	- After these flows run, the source and destination agent
      	 interaction begins.
      	- During this whole process, the inbound caller is on hold. A
      	 [Customer hold flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")
      	 is played to the inbound caller during the hold time.
      After the source agent is connected with destination agent, the source
       agent can do one of the following:




      	- Choose **Join**. This joins all parties on
      	 the call: source agent, destination agent, and the customer are
      	 joined in a conference call.
      	- Choose **Hold all**. This puts destination
      	 agent and the customer on hold.
      	- Put destination agent on hold, so only the source agent can
      	 talk to the customer.
      	- Choose **End call**. The source agent leaves
      	 the call but the destination agent and the customer are directly
      	 connected and continue talking.

  To summarize for agent to queue transfer call, the following flows are played:

      1. **Queue transfer flow**
      2. **Agent whisper flow** (played to the destination
       agent)
      3. **Customer whisper flow** (played to the source
       agent) during whole this process
      4. **Customer hold flow** played to the original
       caller

## CALLBACK

The customer is contacted as part of a callback flow.

- As soon as agent accepts the callback contact, an [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to the
  agent.
- After the customer accepts the callback call, an [Outbound whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to
  customer.
- After these two flows are played, the agent and customer are connected and can
  interact.

To summarize, for callback contacts, the following flow types are played:

- **Agent whisper flow**
- **Outbound whisper flow**

## API

The contact was initiated with Amazon Connect by API. This could be:

1. An outbound contact you created and queued to an agent using the [StartOutboundVoiceContact](../APIReference/API_StartOutboundVoiceContact.md "../APIReference/API_StartOutboundVoiceContact.md") API.
2. A live chat that was initiated by the customer with your contact center where
   you called the [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md") API.
3. A task that was initiated by calling the [StartTaskContact](../APIReference/API_StartTaskContact.md "../APIReference/API_StartTaskContact.md")
   API.

Following is an example of an API initiated contact method:

- After the outbound contact is successfully initiated using the [StartOutboundVoiceContact](../APIReference/API_StartOutboundVoiceContact.md "../APIReference/API_StartOutboundVoiceContact.md") API, an [Inbound flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") provided in the API request
  is played to the customer.
- Depending on the configuration of the [Inbound flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"), additional flows are played. For example, an [Inbound flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") transfers a customer to an
  agent for conversation. In this case, a [Customer queue flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to customer while they waiting in
  queue for an agent.
- When the available agent accepts the call, an [Agent whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to
  agent.
- A [Customer whisper flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types") is played to
  customer.
- After both whisper flows are played successfully to the agent and customer
  respectively, the caller is connected to agent for interaction.

To summarize API initiation methods, the following flows are played before the
customer is connected to agent:

- **Inbound flow**
- **Customer queue flow**
- **Agent whisper flow**
- **Customer whisper flow**

## QUEUE_TRANSFER

While the customer was in one queue (listening to a [Customer queue flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")), they were transferred into another queue using a flow
block.

- The customer who is waiting in the queue for an agent is presented only with a
  [Customer queue flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"). No additional
  flows are involved.

## DISCONNECT

When a [Set disconnect flow](set-disconnect-flow.md "set-disconnect-flow.md")
block runs, it specifies which flow to run after a disconnect event during a
contact.

- You can specify only an [Inbound flow](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types")
  in this block. Since it occurs after the disconnect event, no additional flow is
  presented to customer.

## WEBRTC_API

The contact used the communication widget to make an in-app voice/video call to an
agent. This initiation method is created by the same flow types as the Inbound
initiation method:

1. **Inbound flow**
2. **Customer queue flow**
3. **Agent whisper flow**
4. **Customer whisper flow**

## EXTERNAL_OUTBOUND

An agent initiated a voice (phone) contact with an external participant by using
either a quick connect in the CCP or a flow block. No flow type is associated with this
initiation method.

## MONITOR

A supervisor initiated the monitor feature on a contact connected to an agent. The
supervisor can silently monitor the agent and customer, or barge the
conversation. No flow type is associated with this
initiation method.

## AGENT_REPLY

An agent has replied to an inbound email contact to create an outbound email reply.
For this initiation method the **Outbound whisper flow** type is
played.

## FLOW

An email was initiated by the [Send message](send-message.md "send-message.md") block. For this initiation method the
**Outbound whisper flow** type is played.

## Override the default contact

flows

For all of the initiation methods discussed in this topic, if you don't specify flows
for **Agent whisper flow**, **Customer whisper flow**,
**Customer queue flow**, or **Outbound whisper
flow**, then the default flow of that type runs instead. For a list of
default flows, see [Default flows in Amazon Connect for your contact
center](contact-flow-default.md "contact-flow-default.md").

To override the defaults and use your own flows, use the following blocks:

- [Set customer queue
  flow](set-customer-queue-flow.md "set-customer-queue-flow.md")
- [Set hold flow](set-hold-flow.md "set-hold-flow.md")
- [Set whisper flow](set-whisper-flow.md "set-whisper-flow.md")

For more information, see [Default flows in Amazon Connect for your contact
center](contact-flow-default.md "contact-flow-default.md").
