

# Configure voice for collaborating AI agents
<a name="a2a-voice"></a>

When a customer calls and your Connect AI agent brings in a collaborator to talk to the customer, the collaborator needs a way to handle speech. Amazon Connect Customer gives you two options for voice contacts: text streaming and voice streaming. The option you choose determines whether Connect Customer converts speech on the collaborator's behalf or passes audio directly to the collaborator's endpoint.

This page explains how the two voice modes work, how to set the mode in the API, and what constraints apply.

**Note**  
Voice mode applies only to collaborators that talk to the customer directly (`handoffAgentConfiguration`). Collaborators that handle actions behind the scenes (`delegateAgentConfiguration`) exchange text with your Connect AI agent and never interact with the customer, so voice mode does not apply to them.

## Text streaming (Connect Customer handles speech)
<a name="a2a-voice-text-streaming"></a>

In text streaming mode, Connect Customer manages all voice processing on behalf of the collaborator:

1. Connect Customer converts the caller's speech to text using speech recognition.

1. Connect Customer sends the text to the collaborator over a WebSocket.

1. The collaborator processes the text, decides how to respond, and sends a text response back.

1. Connect Customer converts the response to speech using Connect Agentic voices and plays it to the caller.

This cycle repeats for each turn of the conversation. From the customer's perspective, they hear an AI voice powered by Connect Customer. From the collaborator's perspective, the entire conversation is text in and text out.

**When to use text streaming.** Use this mode when the collaborator does not have its own voice infrastructure, or when you want a consistent voice experience across all collaborators. Text streaming works with any collaborator that supports the A2A protocol over a WebSocket endpoint and can send and receive text messages.

**API field.** Set `audioStreamingEnabled` to `false` on `handoffAgentConfiguration`. This is the default when the field is not specified.

## Voice streaming (collaborator provides speech)
<a name="a2a-voice-voice-streaming"></a>

In voice streaming mode, Connect Customer passes the caller's audio directly to the collaborator's endpoint over the A2A WebSocket connection:

1. Connect Customer streams the caller's audio to the collaborator in real time.

1. The collaborator runs its own speech recognition on the incoming audio, processes the request, generates a response, and streams audio back to Connect Customer.

1. Connect Customer plays the collaborator's audio to the caller in real time.

The caller and the collaborator are in a live bidirectional audio exchange for the duration of the conversation. The collaborator uses its own AI voice, which might sound different from Connect Customer's default voice.

**When to use voice streaming.** Use this mode when the collaborator has its own voice capabilities and you want the lowest possible latency. Common reasons include a partner voice agent optimized for a specific domain, or custom speech models tuned for particular languages or dialects.

**API field.** Set `audioStreamingEnabled` to `true` on `handoffAgentConfiguration`.

## How to set the voice mode
<a name="a2a-voice-set-mode"></a>

Voice mode is controlled by the `audioStreamingEnabled` field on `handoffAgentConfiguration` when you add a collaborator to your Connect AI agent using `CreateAIAgent` or `UpdateAIAgent`.

1. Decide which voice mode the collaborator needs. If the collaborator works with text and you want Connect Customer to handle voice, use text streaming (`false`). If the collaborator has its own voice and you want to pass audio directly, use voice streaming (`true`).

1. Call `CreateAIAgent` or `UpdateAIAgent` with the collaborator's configuration. Set `audioStreamingEnabled` on the `handoffAgentConfiguration` object:

   ```
   {
     "assistantId": "YOUR_ASSISTANT_ID",
     "aiAgentId": "YOUR_AI_AGENT_ID",
     "configuration": {
       "orchestrationAIAgentConfiguration": {
         "multiAgentConfigurations": [
           {
             "handoffAgentConfiguration": {
               "agentTarget": {
                 "applicationId": "YOUR_APP_INTEGRATION_ID"
               },
               "audioStreamingEnabled": false
             }
           }
         ]
       }
     }
   }
   ```

   Replace `false` with `true` to enable voice streaming.

1. Publish a new version of the AI agent by calling `CreateAIAgentVersion`. The voice mode change takes effect when the published version is associated with an AI assistant.

**For agents that handle actions only.** If you are configuring a collaborator with `delegateAgentConfiguration`, you do not need to set a voice mode. Agents configured with `delegateAgentConfiguration` exchange text with your Connect AI agent behind the scenes and never interact with the customer directly.

## Latency
<a name="a2a-voice-latency"></a>

Connect Customer's audio streaming path is designed for low latency. The total latency the customer experiences depends on both the Connect Customer infrastructure and the external agent's processing time. Optimize your collaborator's response time to maintain a natural conversational pace.

## Constraints
<a name="a2a-voice-constraints"></a>

Before choosing a voice mode, review the following constraints for this release:
+ **Voice contacts only.** Voice mode settings apply to voice contacts. Chat contacts always use text, regardless of the `audioStreamingEnabled` value.
+ **PCM encoding required.** Voice streaming uses PCM audio encoding. The collaborator's endpoint must be able to receive and send PCM audio over the A2A WebSocket connection. We support multiple sample rates (8 kHz, 16 kHz, and 24 kHz) for both input and output audio, negotiated at session initialization.
+ **Audio handback is not supported.** In this release, once a collaborator takes over a voice contact in voice streaming mode, audio control cannot be returned mid-stream to your Connect AI agent while the A2A session remains active. When the collaborator signals that it has finished (COMPLETE or ESCALATE), Connect Customer ends the A2A session and returns control to your Connect AI agent, which resumes with text streaming or the default voice. There is no mechanism to switch audio modes within a single A2A session.
+ **One voice mode per collaborator.** Each collaborator configured with `handoffAgentConfiguration` has a single `audioStreamingEnabled` setting. You cannot dynamically switch between text streaming and voice streaming for the same collaborator during a contact.

## Related topics
<a name="a2a-voice-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Set up collaboration with an external AI agent](a2a-setup-external.md)
+ [Observability for collaborating AI agents](a2a-observability.md)