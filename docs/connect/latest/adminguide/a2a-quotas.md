

# Quotas and limitations for agent-to-agent collaboration
<a name="a2a-quotas"></a>

This page lists the requirements, service quotas, and current limitations for agent-to-agent collaboration in Connect Customer.

## Requirements
<a name="a2a-quotas-requirements"></a>

**Connect Customer tier required.** Agent-to-agent collaboration requires an Amazon Connect instance on the Connect Customer tier. It is not available on Customer Basic, which does not include the session state, tracing, and audio streaming capabilities that collaboration requires. For tier details, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).

## Service quotas
<a name="a2a-quotas-service-quotas"></a>

The following quotas apply to agent-to-agent collaboration. For current values, see the [Connect Customer service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) page.


| Quota | Description | 
| --- | --- | 
| Maximum collaborators per AI agent | The maximum number of collaborators you can configure on a single AI agent. | 
| Maximum collaboration depth | The maximum nesting depth when a collaborator invokes another collaborator. | 
| Maximum handoffs per session | The maximum number of times control can transfer between agents in a single contact. | 

These values are subject to change. Check the Connect Customer service quotas page for current limits.

For connection timeout values and concurrent collaboration limits, see the same service quotas page.

## Design constraints
<a name="a2a-quotas-design-constraints"></a>

These are architectural properties of agent-to-agent collaboration that reflect how the feature is designed.
+ **API-only configuration.** Agent-to-agent collaboration is configured through the Connect Customer API (QConnect). There is no console interface for configuring collaborators, collaboration modes, or trace settings. You use the `CreateAIAgent`, `UpdateAIAgent`, and `CreateAIAgentVersion` API operations.
+ **One active collaborator per turn.** Your Connect AI agent can bring in one collaborator at a time during a contact. The AI agent can use different collaborators at different points in the same contact, but only one collaboration session is active at any given moment.
+ **Lex V2 bot required for voice contacts.** Agent-to-agent collaboration on voice contacts requires a Lex V2 bot configured with the AMAZON.QInConnectIntent. The bot handles the speech-to-speech inference and routes customer input to your Connect AI agent. See your Connect Customer setup documentation for bot configuration details.
+ **Bidirectional audio streaming requires an external endpoint.** The collaborator must host its own voice infrastructure and accept a WebSocket connection from Connect Customer. Connect Customer does not provide voice infrastructure to the collaborator in this mode.

## Features not yet available
<a name="a2a-quotas-not-yet-available"></a>

These are capabilities that are planned or under development but not available today.
+ **Audio handback.** When a collaborator is talking to the customer using bidirectional audio streaming, the collaborator cannot hand audio back to the original AI agent mid-contact. The collaborator must complete or escalate the conversation. Text-mode handback (where the collaborator returns control and your Connect AI agent resumes) works as expected.
+ **Selective contact data passing.** You cannot currently choose which contact attributes are shared with a collaborator. Connect Customer passes a fixed set of context automatically.

## Pricing
<a name="a2a-quotas-pricing"></a>

Agent-to-agent collaboration is priced by collaboration mode (text, unidirectional voice, bidirectional voice). For current pricing, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).

## Related topics
<a name="a2a-quotas-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Observability for collaborating AI agents](a2a-observability.md)