

# Quotas and limitations for agent-to-agent collaboration
<a name="a2a-quotas"></a>

This page lists the requirements, service quotas, and design constraints for agent-to-agent collaboration in Connect Customer.

## Requirements
<a name="a2a-quotas-requirements"></a>

Agent-to-agent collaboration has the following requirements:
+ **Connect Customer tier required.** Agent-to-agent collaboration requires an Connect Customer instance on the Connect Customer tier. It is not available on Customer Basic, which does not include the session state, tracing, and audio streaming capabilities that collaboration requires. For tier details, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).
+ **Amazon Lex V2 bot required.** All agent-to-agent collaboration requires an Amazon Lex V2 bot configured with the `AMAZON.QInConnectIntent`. The bot routes customer input to your Connect AI agent. When audio streaming is off, you can use any Amazon Lex speech recognition and text-to-speech settings. Audio streaming requires a bot locale that uses Amazon Nova Sonic speech-to-speech, with a single `AMAZON.QInConnectIntent`. When audio streaming is on, the bot doesn't perform speech-to-speech for the collaborator. Audio streams directly between Connect Customer and the external agent.

## Service quotas
<a name="a2a-quotas-service-quotas"></a>

The following quotas apply to agent-to-agent collaboration. All quotas are adjustable. For the limit on collaboration depth, see [Design constraints](#a2a-quotas-design-constraints).


| Quota | Value | Adjustable | Description | 
| --- | --- | --- | --- | 
| Collaborators per AI agent | 5 | Yes | The maximum number of collaborators that you can configure on a single AI agent. | 
| Handoffs per customer turn | 10 | Yes | The maximum number of handoffs between agents during a single customer turn. | 
| Concurrent outbound third-party agent connections per instance | 5 | Yes | The maximum number of concurrent outbound connections to third-party agents across a single Connect Customer instance. | 

## Design constraints
<a name="a2a-quotas-design-constraints"></a>

The following constraints are architectural properties of agent-to-agent collaboration. They reflect how the feature is designed.
+ **API-only configuration.** You configure agent-to-agent collaboration through the Connect Customer API. There is no console interface for configuring collaborators, collaboration modes, or trace settings. You use the `CreateAIAgent`, `UpdateAIAgent`, and `CreateAIAgentVersion` API operations.
+ **One level of collaboration.** Collaborators can't have their own collaborators.
+ **One collaborator talks to the customer at a time.** In talk-to-the-customer mode, one collaborator holds the conversation with the customer until it hands back control. Your Connect AI agent can hand off to different collaborators at different points in the same contact. In handle-actions-behind-the-scenes mode, your Connect AI agent stays in the conversation. It invokes collaborators as its instructions require, and each invocation returns a result to your Connect AI agent.
+ **Audio streaming is available only for external collaborators.** For AI agents in your instance, Connect Customer handles voice automatically, so you don't need to set `audioStreamingEnabled`. Audio streaming (`audioStreamingEnabled` set to `true`) is for external collaborators, with the following constraints:
  + It requires `immediateHandoff` set to `true`.
  + The audio collaborator must be the only collaborator on that AI agent. An AI agent can have at most one immediate handoff.
  + The orchestrating AI agent can't have an orchestration prompt or a guardrail. Its only tools can be the reserved Complete tool (required) and Escalate tool. For more information, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).
  + Audio streaming is supported over WebSocket (`wss://`) only. The external agent must accept a secure WebSocket connection.
  + Audio streaming applies only to voice contacts. On chat, Connect Customer doesn't negotiate audio, and the external agent must handle text.

## Pricing
<a name="a2a-quotas-pricing"></a>

Agent-to-agent collaboration pricing depends on the collaboration mode. For current pricing, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).

## Related topics
<a name="a2a-quotas-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Observability for collaborating AI agents](a2a-observability.md)