

# Model contact transfers and conferencing in Connect Customer
<a name="model-contact-transfers-conferencing"></a>

This topic is for developers who have integrated their external voice system with Connect Customer conversational analytics. 

Your external voice system might support contact transfers (cold and warm) and conferencing multiple agents in a single call. You can signal these cases to Connect Customer by calling the [CreateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContact.html) and [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html) APIs. These APIs create a contact chain similar to native Connect Customer voice contacts. Each leg of the call will get its own recording, contact record, and analytics, just like native Connect Customer voice contacts. 

Each agent-customer interaction is modeled by an independent contact segment.
+ To model adding an agent to an ongoing call, you create a new contact segment using the [CreateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContact.html) API with initiation method `TRANSFER`. Transfer contacts are linked to the previous contact by their `previousContactId`. 
+ If enabled, call recordings are generated independently for each contact segment and delivered upon completion of that segment.
+ Conversational analytics real-time and post-call analytics are generated for each contact segment independently. 
+ A contact record is generated for each independent contact segment.
+ To model an agent leaving a call, you can end a contact segment by calling the [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html) API.

## Workflow for warm transfer
<a name="workflow-warm-transfer"></a>

Warm transfers involve putting the customer on hold as the agent makes an introduction about the caller to another party.

To model a warm transfer using the contact APIs, implement the following workflow:

1. A call in your external voice system creates an initial contact segment.

1. When the new agent joins the call, invoke the [CreateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContact.html) API. Use the initial contact segment's `contactId` as the `PreviousContactId` parameter. Provide the new agent's ID in the `UserInfo` parameter.

1. Let the initial agent introduce the new agent to the call and then disconnect from the call.

1. When the initial agent disconnects from the call, invoke the [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html) API.

1. When the call ends in your external voice system (upon SIP BYE), the contact chain ends.

## Workflow for cold transfer
<a name="workflow-cold-transfer"></a>

Cold transfers involve directly transferring the customer from one agent to another without any introduction or context shared between them.

To model a cold transfer using the contact APIs, implement the following workflow:

1. A call in your external voice system creates an initial contact segment.

1. When the initial agent disconnects from the call, invoke the [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html) API.

1. When the new agent joins the call, invoke the [CreateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContact.html) API. Use the initial contact segment's `contactId` as the `PreviousContactId` parameter. Provide the new agent's ID in the `UserInfo` parameter.

1. When the call ends in your external voice system (upon SIP BYE), the contact chain ends.

## Contact segment limits
<a name="contact-segment-limits"></a>

You can have up to two concurrent contact segments and 10 total contact segments in a chain.