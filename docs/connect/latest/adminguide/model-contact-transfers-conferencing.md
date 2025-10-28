# Model contact transfers and

conferencing in Amazon Connect

This topic is for developers who have integrated their external voice system with
Amazon Connect Contact Lens.

Your external voice system may support contact transfers (cold and warm) and
conferencing multiple agents in a single call. You can signal these cases to Amazon Connect by
calling the [CreateContact](../APIReference/API_CreateContact.md "../APIReference/API_CreateContact.md") and
[StopContact](../APIReference/API_StopContact.md "../APIReference/API_StopContact.md") APIs. These APIs create a contact chain similar to native Amazon Connect
voice contacts. Each leg of the call will get its own recording, contact record, and
analytics, just like native Amazon Connect voice contacts.

Each agent-customer interaction is modeled by an independent contact segment.

- To model adding an agent to an ongoing call, you create a new contact segment
  using the [CreateContact](../APIReference/API_CreateContact.md "../APIReference/API_CreateContact.md") API with initiation method `TRANSFER`.
  Transfer contacts are linked to the previous contact by their
  `previousContactId`.
- If enabled, call recordings are generated independently for each contact
  segment and delivered upon completion of that segment.
- Contact Lens real-time and post-call analytics are generated for each
  contact segment independently.
- A contact record is generated for each independent contact segment.
- To model an agent leaving a call, you can end a contact segment by calling the
  [StopContact](../APIReference/API_StopContact.md "../APIReference/API_StopContact.md")
  API.

## Workflow for warm transfer

Warm transfers involve putting the customer on hold as the agent makes an
introduction about the caller to another party.

To model a warm transfer using the contact APIs, implement the following
workflow:

1. A call in your external voice system creates an initial contact
   segment.
2. When the new agent joins the call, invoke the [CreateContact](../APIReference/API_CreateContact.md "../APIReference/API_CreateContact.md") API. Use the initial contact segment's
   `contactId` as the `PreviousContactId` parameter.
   Provide the new agent's ID in the `UserInfo` parameter.
3. Let the initial agent introduce the new agent to the call and then
   disconnect from the call.
4. When the initial agent disconnects from the call, invoke the [StopContact](../APIReference/API_StopContact.md "../APIReference/API_StopContact.md") API.
5. When the call ends in your external voice system (upon SIP BYE), the
   contact chain ends.

## Workflow for cold transfer

Cold transfers involve directly transferring the customer from one agent to
another without any introduction or context shared between them.

To model a cold transfer using the contact APIs, implement the following
workflow:

1. A call in your external voice system creates an initial contact
   segment.
2. When the initial agent disconnects from the call, invoke the [StopContact](../APIReference/API_StopContact.md "../APIReference/API_StopContact.md") API.
3. When the new agent joins the call, invoke the [CreateContact](../APIReference/API_CreateContact.md "../APIReference/API_CreateContact.md") API. Use the initial contact segment's
   `contactId` as the `PreviousContactId` parameter.
   Provide the new agent's ID in the `UserInfo` parameter.
4. When the call ends in your external voice system (upon SIP BYE), the
   contact chain ends.

## Contact segment limits

You can have up to two concurrent contact segments and 10 total contact segments
in a chain.
