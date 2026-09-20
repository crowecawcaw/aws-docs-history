

# How agent-to-agent collaboration works
<a name="a2a-how-it-works"></a>

Agent-to-agent collaboration lets your Connect AI agent bring in another AI agent during a live contact. The collaborating agent performs work, talks to the customer, or both, and then returns control to your Connect AI agent.

Collaboration uses the Agent-to-Agent (A2A) protocol, an open standard originally developed by Google and now governed by the Linux Foundation. Amazon Connect Customer adds A2A extensions for voice streaming, contact-level session continuity, and built-in observability that the base protocol does not provide. This page explains what happens at runtime when your Connect AI agent uses a collaborator.

## What collaborating agents can do
<a name="a2a-how-it-works-what-agents-can-do"></a>

A collaborating agent can do one of two things during a contact:

**Handle actions.** The collaborator works behind the scenes while your Connect AI agent continues the conversation with the customer. Your Connect AI agent sends a request over text, the collaborator does the work (looks up an order, files a claim, scores a transaction), and returns the result. The customer never interacts with the collaborator directly.

**Talk to the customer.** The collaborator takes over the conversation and speaks or chats with the customer directly. Your orchestrator Connect AI agent steps aside until the collaborator finishes. When the collaborator is done, it signals an outcome and your Connect AI agent resumes. Connect Customer gives you two options for how this works on voice contacts:
+ **Text streaming.** Connect Customer converts the caller's speech to text, sends it to the collaborator, receives text responses, and converts them back to speech. The collaborator does not need any voice infrastructure.
+ **Voice streaming.** Connect Customer passes the caller's audio directly to the collaborator's endpoint over bidirectional audio streaming. The collaborator uses its own AI voice to speak with the customer.

For more about the voice options, see [Configure voice for collaborating AI agents](a2a-voice.md).

## Which AI agents can collaborate
<a name="a2a-how-it-works-which-agents"></a>

Your Connect AI agent can work with:
+ **Another AI agent in your instance.** An AI agent that you have already created in the same Connect Customer instance. Connect Customer routes the collaboration internally.
+ **An external agent.** An agent hosted outside of your Connect Customer instance and AgentCore. The agent must expose an A2A-compatible endpoint that Connect Customer can reach over HTTPS.

External agents must be registered as an external agent in your Connect Customer instance and must send trace data to Connect Customer. For setup instructions, see [Set up collaboration with an external AI agent](a2a-setup-external.md). You can also connect to an agent you host yourself, provided it implements the A2A protocol and meets the trace data requirements described in [Trace data and observability](#a2a-how-it-works-trace-data).

## How your Connect AI agent decides to use a collaborator
<a name="a2a-how-it-works-decision"></a>

The decision to bring in a collaborator is instruction-driven. When you configure your Connect AI agent, you write instructions that tell it when and how to use each collaborator. Your Connect AI agent reads those instructions, evaluates the conversation, and decides whether to invoke a collaborator based on what the customer needs.

For example, you might write an instruction like: "When the customer asks about the status of an insurance claim, use the claims collaborator to look up the claim and return the result." Or: "When the customer wants to speak with a specialist about an investment portfolio review, bring in the portfolio advisor collaborator and let it talk to the customer."

Connect Customer does not impose routing rules or priority logic on collaboration. Your Connect AI agent's instructions are the sole mechanism that determines when a collaborator is used, which collaborator is selected, and what information is passed to it.

## How a collaboration ends
<a name="a2a-how-it-works-ends"></a>

When a collaborator finishes its work, it signals one of two outcomes back to your Connect AI agent:


| Outcome | What it means | 
| --- | --- | 
| Completed | The collaborator finished the requested work successfully. Your Connect AI agent can continue the conversation using whatever the collaborator returned. | 
| Escalate | The collaborator determined that the contact needs a human agent. Your Connect AI agent receives this signal and can route accordingly. | 

These outcome names correspond to the A2A protocol values Completed (COMPLETE) and Escalate (ESCALATE). This guide uses the friendly names in prose and the enum values in code examples. Additional finish types might be supported in future releases.

These outcomes are deliberate signals. The collaborator chooses which outcome to send based on how its own processing concluded. Each outcome triggers its own routing path in your Connect AI agent's configuration, so you can define exactly what happens next for each case.

This is different from a failure. A failure is when the collaborator stops responding, the connection drops, or a timeout occurs before the collaborator sends any outcome signal at all. Failures are handled by the fallback path described in the next section.

## When a collaborator fails
<a name="a2a-how-it-works-failure"></a>

If a collaborator stops responding, the connection between Connect Customer and the collaborator drops, or the collaborator does not send any outcome signal before the session times out, Connect Customer invokes the fallback path you configured for that collaborator.

The fallback path is separate from the outcome routes described in the preceding section. The outcomes (Completed, Escalate) are deliberate signals that the collaborator sends intentionally. The fallback path handles situations where no signal arrives at all.

A typical fallback configuration routes the customer to a human agent queue. You can also configure the fallback to try a different collaborator, return control to your Connect AI agent with an apology message, or take any other action your contact flow supports.

If the fallback path returns control to your Connect AI agent, you can write instructions that tell it to try again or take a different approach.

## What a collaborator can see
<a name="a2a-how-it-works-context"></a>

When Connect Customer invokes a collaborator, it passes session attributes and contact data so the collaborator has context about the customer and the conversation. This includes attributes like the customer's phone number, the queue the contact came from, and any custom session attributes your Connect AI agent or contact flow has set.

The collaborator does not receive the full conversation history between your Connect AI agent and the customer. It receives only the information that Connect Customer explicitly shares at the start of the collaboration, plus whatever your Connect AI agent includes in the request.

If the collaborator is talking to the customer directly, it builds its own conversation history with the customer for the duration of its turn. When the collaborator finishes and control returns to your Connect AI agent, the collaborator's conversation history is merged into your Connect AI agent's session, so your Connect AI agent has context about what happened during the collaboration.

## Voice contacts
<a name="a2a-how-it-works-voice-contacts"></a>

For voice contacts, there are two options:

**Text streaming.** Connect Customer performs speech-to-text on the caller's audio, sends the resulting text to the collaborator, receives text responses, and converts them to speech using text-to-speech. The collaborator works entirely in text. This is the simpler option and does not require the collaborator to have any voice infrastructure.

**Voice streaming.** Connect Customer establishes a bidirectional audio stream over a WebSocket between the caller and the collaborator's endpoint. The collaborator receives raw audio from the caller and sends audio back directly, using its own AI voice. This option requires the collaborator to handle audio processing, speech recognition, and speech synthesis on its own endpoint.

You choose between text streaming and voice streaming when you configure each collaborator. You can use different options for different collaborators in the same AI agent configuration. For setup details, see [Configure voice for collaborating AI agents](a2a-voice.md).

## Trace data and observability
<a name="a2a-how-it-works-trace-data"></a>

Collaborating agents must send trace data back to Connect Customer for every collaboration session. Trace data includes the messages exchanged, tool calls made, timing information, and the outcome of the collaboration. Connect Customer uses this data for contact analytics, quality management, and compliance.

**Connect Customer will disable external agent endpoints that do not send the required trace data.** Disabling means the external endpoint will not be invoked for new contacts. In-flight contacts that are already using the collaborator will complete normally, but no new collaborations will start with that collaborator until the trace data issue is resolved.

For the full list of required and recommended trace fields, and details on how trace enforcement works, see [Observability for collaborating AI agents](a2a-observability.md).

## Related topics
<a name="a2a-how-it-works-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md) (overview)
+ [Configure voice for collaborating AI agents](a2a-voice.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)