

# Agent-to-agent collaboration
<a name="a2a-collaboration"></a>

Agent-to-agent collaboration lets a Connect Customer AI agent collaborate with other AI agents during a live contact. The collaborating agent can be either an AI agent that you already run in your Connect Customer instance, or an external agent that you or a third party hosts outside of Connect Customer, including agents that run on Amazon Bedrock AgentCore.

Collaboration uses the Agent-to-Agent (A2A) protocol, an open standard originally developed by Google and now governed by the Linux Foundation. Connect Customer adds A2A extensions that the base protocol does not provide. For details, see the [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html) in the *Connect Customer Developer Guide*.

**Topics**
+ [What collaborating agents can do](#a2a-collaboration-what-agents-can-do)
+ [How Connect Customer manages the collaboration](#a2a-collaboration-how-connect-manages)
+ [Requirements](#a2a-collaboration-requirements)
+ [Permissions summary](#a2a-collaboration-permissions)
+ [Set up collaboration](#a2a-collaboration-setup)
+ [Related topics](#a2a-collaboration-related)
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md)
+ [Set up an external AI agent integration](a2a-setup-external.md)
+ [Build an external AI agent server](a2a-external-server.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)

## What collaborating agents can do
<a name="a2a-collaboration-what-agents-can-do"></a>

A collaborating agent works in one of two modes during a contact:
+ **Handle actions behind the scenes.** Your Connect AI agent stays in the conversation with the customer. When it decides to invoke the collaborator, it builds a text message that describes the work. The collaborator does the work (looks up an order, files a claim, runs a calculation) and returns the result. The customer never interacts with the collaborator directly. This mode is also called delegation.
+ **Talk to the customer.** The collaborator speaks or chats with the customer directly, then returns control to your Connect AI agent when it finishes. This mode is also called handoff. On voice contacts, this mode works in one of two ways:
  + **Text streaming.** Connect Customer converts the caller's speech to text, sends it to the collaborator, and converts the collaborator's text responses back to speech. The collaborator doesn't need any voice infrastructure.
  + **Audio streaming.** Available for external collaborators only. Connect Customer streams the caller's audio to the collaborator, and the collaborator streams audio back. Audio streaming uses WebSocket (`wss://`) only.

For a comparison of the modes, see [Compare collaboration modes](a2a-how-it-works.md#a2a-how-it-works-modes).

## How Connect Customer manages the collaboration
<a name="a2a-collaboration-how-connect-manages"></a>

Connect Customer handles the infrastructure so your Connect AI agent and the collaborator can focus on the conversation:
+ **Invocation.** Connect Customer establishes the A2A session with the collaborator when your Connect AI agent's instructions call for it. For details, see [How your Connect AI agent decides to use a collaborator](a2a-how-it-works.md#a2a-how-it-works-decision).
+ **Context.** In talk to the customer mode, Connect Customer passes context to the collaborator, such as the conversation so far. For details, see [What a collaborator can see](a2a-how-it-works.md#a2a-how-it-works-context). In handle actions behind the scenes mode, the collaborator receives the text message that your Connect AI agent builds.
+ **Observability.** Connect Customer publishes traces automatically for Connect AI agent collaborators. External collaborators must send trace data back to Connect Customer. If Connect Customer detects that an external agent is not sending the required trace data, Connect Customer disables that endpoint for new contacts. For details, see [Observability for collaborating AI agents](a2a-observability.md).
+ **Failures.** If a collaboration fails, the contact returns to the error branch of your contact flow, where you configure the fallback. For external collaborators, Connect Customer first retries a WebSocket connection attempt once for certain errors. In talk to the customer mode on voice contacts over WebSocket, it also reconnects once if the connection drops during the session. For details, see [Connection retries, reconnects, and close codes](a2a-external-server.md#a2a-external-server-reconnect).

## Requirements
<a name="a2a-collaboration-requirements"></a>

The following requirements apply to all agent-to-agent collaboration:
+ Your instance must be on the **Connect Customer** tier. Agent-to-agent collaboration is not available on Customer Basic.
+ You configure collaboration through the Connect Customer API. There is no console interface for this feature. You use the `CreateAIAgent` and `UpdateAIAgent` API operations to add collaborators to your Connect AI agent's configuration. You use the `CreateAIAgentVersion` API operation to publish a version that you can deploy.
+ Your contact flow reaches your Connect AI agent through an Amazon Lex V2 bot with the `AMAZON.QInConnectIntent`. Audio streaming requires a bot locale that uses Amazon Nova Sonic speech-to-speech, with a single `AMAZON.QInConnectIntent`.

The following additional requirements apply to Connect AI agent collaborators:
+ A collaborator that talks to the customer must have the reserved Complete tool, and should also have the Escalate tool, so it can give control back to the main Connect AI agent. The main Connect AI agent is invoked again with the reason that the collaborator gives. It can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow. For more information, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).

The following additional requirements apply to external collaborators:
+ The external agent must implement the A2A protocol with the Connect Customer A2A extensions. For details, see [Build an external AI agent server](a2a-external-server.md).
+ You register the external agent as an Connect Customer AppIntegrations application of type `A2A_SERVER`. The application stores the endpoint URL and a reference to the API key, which you keep in AWS Secrets Manager.
+ In either mode, a text endpoint can use `https://` (HTTP JSON-RPC) or `wss://` (WebSocket). Audio streaming, in talk to the customer mode with immediate handoff, requires `wss://`.
+ External agents must send trace data to Connect Customer. Connect Customer disables external agent endpoints that do not send the required trace data. For details, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md).

## Permissions summary
<a name="a2a-collaboration-permissions"></a>

Agent-to-agent collaboration uses two kinds of permissions: the permissions that you need when you configure collaboration, and the permissions that Connect Customer needs at runtime, when your Connect AI agent invokes a collaborator.

You need the following permissions when you configure collaboration:
+ **IAM permissions.** The principal that configures collaboration needs permissions to call the AI agent API operations. For the list, see [Required permissions](a2a-setup-1p.md#a2a-setup-1p-permissions). Setting up an external collaborator also requires permissions to create the application and the secret. For details, see [Set up an external AI agent integration](a2a-setup-external.md).
+ **API key secret for external collaborators.** You store the external agent's API key as an AWS Secrets Manager secret that is encrypted with a customer managed KMS key. For the required secret and key configuration, see [Store the external agent's API key](a2a-setup-external.md#a2a-setup-external-step1).

Connect Customer uses the following permissions at runtime:
+ **Security profile for external collaborators.** The security profile of your Connect AI agent must allow the external application (type `THIRD_PARTY`). You must also associate the security profile with your Connect AI agent (entity type `AI_AGENT`).
+ **Amazon Lex and Connect AI agent permissions.** Your Amazon Lex bot uses the `AMAZON.QInConnectIntent` to reach your Connect AI agent. The existing permissions for that setup apply. For the required permissions, see [AMAZON.QInConnectIntent](https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-qinconnect.html) in the *Amazon Lex V2 Developer Guide*. For how to create the intent from your Connect Customer instance, see [Create an agent assist intent](create-qic-intent-connect.md).
+ **Contact context for external collaborators.** To pass contact context (customer address, system address, and channel) to an external collaborator that talks to the customer, the security profile of your Connect AI agent must grant the **Access Contact Control Panel** permission.

For more information about security profiles for AI agents, see [Assign security profile permissions to AI agents](ai-agent-security-profile-permissions.md).

## Set up collaboration
<a name="a2a-collaboration-setup"></a>

For setup instructions, see the following pages:
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md) (for AI agents in your instance)
+ [Set up an external AI agent integration](a2a-setup-external.md) (for external agents, including agents on Amazon Bedrock AgentCore)
  + [Build an external AI agent server](a2a-external-server.md) (how to build and host the external agent's server)

## Related topics
<a name="a2a-collaboration-related"></a>
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Build an external AI agent server](a2a-external-server.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)

**Note**  
To bring a human agent into a contact, see [Use agentic self-service](agentic-self-service.md).