

# How agent-to-agent collaboration works
<a name="a2a-how-it-works"></a>

Agent-to-agent collaboration lets your Connect AI agent bring in another AI agent during a live contact. The collaborating agent performs work or talks to the customer, and then returns control to your Connect AI agent.

Collaboration uses the Agent-to-Agent (A2A) protocol, an open standard originally developed by Google and now governed by the Linux Foundation. Amazon Connect Customer adds A2A extensions that the base protocol does not provide. For details, see the [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html). This page explains what happens at runtime when your Connect AI agent uses a collaborator.

## What collaborating agents can do
<a name="a2a-how-it-works-what-agents-can-do"></a>

A collaborating agent works in one of two modes during a contact:

**Handle actions behind the scenes.** The collaborator works behind the scenes while your Connect AI agent continues the conversation with the customer. When your Connect AI agent decides to invoke the collaborator, it builds a text message that describes the work. The collaborator does the work (looks up an order, files a claim, scores a transaction) and returns the result. The customer never interacts with the collaborator directly. This mode is also called delegation.

**Talk to the customer.** The collaborator takes over the conversation and speaks or chats with the customer directly. This mode is also called handoff. The main Connect AI agent steps aside until the collaborator finishes. When the collaborator is done, it signals an outcome and your Connect AI agent resumes. On voice contacts, this mode uses text streaming or audio streaming. For details, see [Voice contacts in talk-to-the-customer mode](#a2a-how-it-works-voice-contacts).

## Compare collaboration modes
<a name="a2a-how-it-works-modes"></a>

The following table compares the collaboration modes.


**Collaboration modes**  

| Mode | Who talks to the customer | Connection behavior (external agents) | Audio support | Returning control to the main Connect AI agent | Collaborator types | 
| --- | --- | --- | --- | --- | --- | 
| Handle actions behind the scenes | Your Connect AI agent | A new connection and session initialization for each invocation, reusing the same session (contextId). | Not applicable. The collaborator exchanges text with your Connect AI agent. | The collaborator returns its result to your Connect AI agent. The collaborator doesn't need hand-back tools. | Connect AI agent and external collaborators | 
| Talk to the customer (text) | The collaborator. On voice, Connect Customer converts speech to text and text to speech. | Voice over WebSocket (wss://): one persistent connection for the session. HTTP JSON-RPC (https://): a request and response for each exchange, with no persistent connection. Chat: a new connection for each customer message. | No. Connect Customer provides the voice. | **Connect AI agent collaborator:** uses its Complete or Escalate tool.<br />**External collaborator:** sends a FINISH event with COMPLETE or ESCALATE.<br />Control returns to the main Connect AI agent. | Connect AI agent and external collaborators | 
| Talk to the customer (audio) | The collaborator, using its own AI voice | One persistent wss:// connection for the session. | Yes, bidirectional audio on voice contacts, over WebSocket (wss://) only | The collaborator sends a FINISH event with COMPLETE or ESCALATE. Control returns to the main Connect AI agent. | External only | 

When a collaborator that talks to the customer completes or escalates, control returns to the main Connect AI agent, which is invoked again with the collaborator's reason. The main Connect AI agent can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow. For more information about these tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).

For Connect AI agent collaborators, Connect Customer manages the connection for you.

## Which AI agents can collaborate
<a name="a2a-how-it-works-which-agents"></a>

Your Connect AI agent can work with the following types of AI agents:
+ **Another AI agent in your instance (Connect AI agent collaborator).** An AI agent that you have already created in the same Connect Customer instance. Connect Customer routes the collaboration internally and manages the A2A protocol for you.
+ **An external agent (third-party).** An agent hosted outside of your Connect Customer instance, including an agent that runs on Amazon Bedrock AgentCore. The agent must implement the A2A protocol with the Connect Customer A2A extensions. It must expose a public endpoint that Connect Customer can reach over WebSocket (`wss://`) or HTTP JSON-RPC (`https://`, text only). Audio streaming is supported over WebSocket (`wss://`) only.

You register an external agent as an AppIntegrations application in your account. The external agent authenticates Connect Customer with an API key. You store the key in AWS Secrets Manager, and Connect Customer sends it to the external agent as a bearer token when it connects. External agents must also send trace data to Connect Customer.

For setup instructions, see [Set up an external AI agent integration](a2a-setup-external.md). For what the external agent must implement, see [Build an external AI agent server](a2a-external-server.md).

## How your Connect AI agent decides to use a collaborator
<a name="a2a-how-it-works-decision"></a>

The decision to bring in a collaborator is instruction-driven. When you configure your Connect AI agent, you write instructions that tell it when and how to use each collaborator. Your Connect AI agent reads those instructions, evaluates the conversation, and decides whether to invoke a collaborator based on what the customer needs.

For example, you might write an instruction such as the following: "When the customer asks about the status of an insurance claim, use the claims collaborator to look up the claim and return the result." Or: "When the customer wants to speak with a specialist about an investment portfolio review, bring in the portfolio advisor collaborator and let it talk to the customer."

For a collaborator that talks to the customer, you can instead set `immediateHandoff` to `true`. With immediate handoff, the collaborator takes over the conversation on the first turn, and your Connect AI agent does not evaluate instructions first.

## How a talk-to-the-customer collaboration ends
<a name="a2a-how-it-works-ends"></a>

A collaborator that handles actions behind the scenes returns its result to your Connect AI agent for each request, so it doesn't signal an outcome. In talk to the customer mode, when the collaborator finishes, it signals one of two outcomes back to your Connect AI agent:


| Outcome | What it means | 
| --- | --- | 
| Complete | The collaborator finished its part of the conversation. Control returns to your Connect AI agent. | 
| Escalate | The collaborator determined that the contact needs a human agent. Control returns to your Connect AI agent. If your Connect AI agent has the Escalate tool, it can call Escalate to return the contact to the Escalate path of your contact flow, which typically transfers the contact to a human agent. | 

In either case, control returns to the main Connect AI agent, which is invoked again with the collaborator's reason. The main Connect AI agent can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow. For more information, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).

How the collaborator signals the outcome depends on the collaborator type:
+ **Connect AI agent collaborators.** In talk to the customer mode, a Connect AI agent collaborator must have the reserved Complete tool, and should also have the Escalate tool, so it can give control back to the main Connect AI agent. For more information about these tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).
+ **External collaborators.** The external agent sends a FINISH event with the type COMPLETE or ESCALATE.

With either outcome, the collaborator can include a reason. Connect Customer passes the reason back and invokes your Connect AI agent again so it can handle the outcome gracefully. For example, a collaborator can complete with a reason that explains why it couldn't finish the task, and your Connect AI agent can offer another option.

This is different from a failure. A failure occurs when the connection to the collaborator fails or drops before the collaborator signals an outcome. A failure also occurs when an external agent ends a task as failed, canceled, or rejected. That ends the collaboration, not just the turn, and the contact returns to the Error branch of your flow. For more information, see the following section.

## When a collaborator fails
<a name="a2a-how-it-works-failure"></a>

For some WebSocket connection errors, Connect Customer retries before it treats the collaboration as failed:
+ If a connection attempt fails, Connect Customer retries a WebSocket connection attempt once for certain errors.
+ In talk to the customer mode on voice contacts over WebSocket, if the connection drops unexpectedly during the session, Connect Customer reconnects one time. For which connection closes trigger a reconnect, see [Connection retries, reconnects, and close codes](a2a-external-server.md#a2a-external-server-reconnect).

If the retry or reconnect also fails, the collaboration fails. The contact returns to the error branch of your contact flow. Configure your fallback on that error branch. For example, you can route the customer to a human agent queue or play a message.

The error branch handles failures, where no outcome arrives. To handle a problem gracefully within the conversation, the collaborator can instead finish with a reason, as described in the preceding section. Your Connect AI agent then decides how to continue.

## What a collaborator can see
<a name="a2a-how-it-works-context"></a>

In talk to the customer mode, Connect Customer passes the conversation history automatically, so the collaborator knows what the customer already said. For external collaborators in talk to the customer mode, Connect Customer passes the following at the start of the session:
+ The conversation history of the Connect AI agent session, up to the handoff
+ The contact ARN and instance ARN
+ Contact context: the customer address, the system address, and the channel. Connect Customer includes contact context only when the security profile of your Connect AI agent grants the **Access Contact Control Panel** permission.

Connect Customer doesn't pass custom contact attributes to external collaborators. You can't choose which context is shared. For details about what the external agent receives, see [Build an external AI agent server](a2a-external-server.md).

In talk to the customer mode, the collaborator also builds its own conversation history with the customer for the duration of its turn. When the collaborator finishes and control returns to your Connect AI agent, Connect Customer merges the collaborator's conversation history into your Connect AI agent's session. Your Connect AI agent then has context about what happened during the collaboration.

## Voice contacts in talk-to-the-customer mode
<a name="a2a-how-it-works-voice-contacts"></a>

Collaborators that handle actions behind the scenes exchange text with your Connect AI agent and never interact with the customer, so voice options don't apply to them.

For Connect AI agent collaborators, Connect Customer manages voice for you with text streaming. For external collaborators, you choose text streaming or audio streaming with the `audioStreamingEnabled` field.


| Aspect | Text streaming | Audio streaming | 
| --- | --- | --- | 
| Setting | audioStreamingEnabled set to false or omitted | audioStreamingEnabled and immediateHandoff set to true | 
| Collaborator types | Connect AI agent and external collaborators | External only | 
| Speech recognition and speech synthesis | Connect Customer converts the caller's speech to text and converts the collaborator's text responses to speech using Connect Agentic voices. | The external agent receives the caller's audio, runs its own speech recognition, and streams audio back in its own AI voice. The Amazon Lex bot doesn't perform speech-to-speech for the collaborator. | 
| Transport (external agents) | Text over WebSocket (wss://) or HTTP JSON-RPC (https://) | PCM audio over WebSocket (wss://) only | 
| Connection (external agents) | WebSocket: one persistent connection for the session. HTTP JSON-RPC: a request and response for each exchange, with no persistent connection. | One persistent WebSocket connection for the session | 
| Amazon Lex bot locale | Any Amazon Lex speech recognition and text-to-speech settings | Amazon Nova Sonic speech-to-speech, with a single AMAZON.QInConnectIntent | 

Audio streaming has the following additional constraints:
+ The audio collaborator must be the only collaborator on that AI agent. An AI agent can have at most one immediate handoff.
+ The orchestrating AI agent can't have an orchestration prompt or a guardrail. Its only tools can be the reserved Complete tool (required) and Escalate tool. For more information, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).
+ Each collaborator has a single `audioStreamingEnabled` setting. You can't switch between text streaming and audio streaming for the same collaborator during a contact.

For setup details, see [Set up an external AI agent integration](a2a-setup-external.md). For audio requirements on the external agent, see [Build an external AI agent server](a2a-external-server.md).

## Chat contacts
<a name="a2a-how-it-works-chat-contacts"></a>

On chat contacts, collaboration is always text. For Connect AI agent collaborators, Connect Customer manages the exchange for you.

For external collaborators that talk to the customer, Connect Customer opens a new connection for each customer message. Each connection uses the same session (`contextId`), and Connect Customer sends the conversation history again when it initializes the session. If you set `audioStreamingEnabled` to `true`, Connect Customer doesn't negotiate audio on chat. The external agent must handle text.

## Trace data and observability
<a name="a2a-how-it-works-trace-data"></a>

Connect Customer uses trace data for contact analytics, quality management, and compliance. Trace data includes the messages exchanged, tool calls made, and timing information.
+ **Connect AI agent collaborators.** Connect Customer publishes traces automatically for each collaborating AI agent.
+ **External collaborators.** The external agent must publish trace data from its server as `TRACING_SPAN` events. For details, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract.

**Connect Customer disables external agent endpoints that do not send the required trace data.** After Connect Customer disables an external endpoint, it doesn't invoke that endpoint for new contacts. In-flight contacts that are already using the collaborator complete normally, but no new collaborations start with that collaborator until the trace data issue is resolved.

For the full list of required and encouraged trace fields, and details about how trace enforcement works, see [Observability for collaborating AI agents](a2a-observability.md).

## Related topics
<a name="a2a-how-it-works-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md) (overview)
+ [Set up collaboration with another Connect Customer AI agent](a2a-setup-1p.md)
+ [Set up an external AI agent integration](a2a-setup-external.md)
+ [Build an external AI agent server](a2a-external-server.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)