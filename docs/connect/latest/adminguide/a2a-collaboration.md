

# Agent-to-agent collaboration
<a name="a2a-collaboration"></a>

Agent-to-agent collaboration lets a Connect Customer AI agent collaborate with other AI agents during a live contact. The collaborating agent can be one you already run in your Connect Customer instance, an agent you host on Amazon Bedrock AgentCore, or an external agent built by a third-party provider.

Collaboration uses the Agent-to-Agent (A2A) protocol, an open standard originally developed by Google and now governed by the Linux Foundation. Connect Customer adds A2A extensions for voice streaming, contact-level session continuity, and built-in observability that the base protocol does not provide.

**Topics**
+ [What collaborating agents can do](#a2a-collaboration-what-agents-can-do)
+ [How Connect Customer manages the collaboration](#a2a-collaboration-how-connect-manages)
+ [API-only feature](#a2a-collaboration-api-only)
+ [Requirements](#a2a-collaboration-requirements)
+ [Related topics](#a2a-collaboration-related)
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md)
+ [Set up collaboration with an external AI agent](a2a-setup-external.md)
+ [Configure voice for collaborating AI agents](a2a-voice.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)

## What collaborating agents can do
<a name="a2a-collaboration-what-agents-can-do"></a>

There are two things a collaborating agent can do during a contact:
+ **Handle actions.** Your Connect AI agent stays in the conversation with the customer and asks the collaborator to perform work behind the scenes. The collaborator receives a request over text, does the work (looks up an order, files a claim, runs a calculation), and returns the result. The customer never interacts with the collaborator directly.
+ **Talk to the customer.** The collaborator speaks or chats with the customer directly, then returns control to your Connect AI agent when it finishes. For voice AI agents, Connect Customer gives you two ways to do this with A2A:
  + **Text streaming.** Connect Customer converts the caller's speech to text, sends it to the collaborator, receives text responses, and converts them back to speech. The collaborator does not need any voice infrastructure.
  + **Voice streaming.** Connect Customer passes the caller's audio directly to the collaborator's endpoint. The collaborator uses its own AI voice. This is bidirectional audio streaming over A2A.

## How Connect Customer manages the collaboration
<a name="a2a-collaboration-how-connect-manages"></a>

Connect Customer handles the infrastructure so your Connect AI agent and the collaborator can focus on the conversation:
+ **Invocation.** Connect Customer establishes the A2A session with the collaborator when your Connect AI agent's instructions call for it.
+ **Context.** Connect Customer passes conversational context to the collaborator so it has the information it needs.
+ **Voice.** For voice contacts, you have two choices. Connect Customer can manage speech-to-text and text-to-speech conversion using Connect Agentic voices, or you can enable bidirectional audio streaming.
+ **Observability.** Connect Customer collects trace data from every collaboration. External collaborators are required to send trace data back to Connect Customer. If Connect Customer detects that an external agent is not sending the required trace data, that endpoint will be disabled for new contacts. For details, see [Observability for collaborating AI agents](a2a-observability.md).
+ **Fallback.** If a collaborator fails to respond or returns an error, Connect Customer routes the contact according to the fallback path you configure.

## API-only feature
<a name="a2a-collaboration-api-only"></a>

Agent-to-agent collaboration is configured through the Connect Customer API (QConnect). There is no console interface for this feature. You use the `CreateAIAgent` and `UpdateAIAgent` API operations to add collaborators to your Connect AI agent's configuration, and `CreateAIAgentVersion` to publish a version that can be deployed.

For setup instructions, see:
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md) (for agents in your instance or on AgentCore)
+ [Set up collaboration with an external AI agent](a2a-setup-external.md) (for third-party agents)

## Requirements
<a name="a2a-collaboration-requirements"></a>
+ Your instance must be on the **Connect Customer** tier. Agent-to-agent collaboration is not available on Customer Basic.
+ The collaborating agent must support the A2A protocol with Connect A2A extensions.
+ External agents must send trace data to Connect Customer. Connect Customer will disable external agent endpoints that do not send the required trace data. For details, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md).

## Related topics
<a name="a2a-collaboration-related"></a>
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Configure voice for collaborating AI agents](a2a-voice.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)

**Note**  
To bring a human agent into a contact, see [Use agentic self-service](agentic-self-service.md).