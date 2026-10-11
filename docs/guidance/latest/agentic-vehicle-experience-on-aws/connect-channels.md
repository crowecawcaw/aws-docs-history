

# Channels and entry points
<a name="connect-channels"></a>

AVX has two channels, voice and text, and both run in the tenant’s app or web surface. Amazon Connect is where a conversation goes when it needs a person. Both channels reach the same supervisor, and both escalate the same way: the P0 or P1 card, then `/escalate`, then a Connect chat. A phone rings only for the P0 callback.


| Channel | Stack | Typical use | 
| --- | --- | --- | 
|  **Voice**  | AVX app → WebSocket → AgentCore bidirectional runtime (`vsa_supervisor_bidi_<stage>`) with Amazon Nova 2 Sonic speech-to-speech → VSA supervisor | Drivers on the road, hands-free interactions, primary channel for fleet drivers and vehicle owners | 
|  **Text**  | AVX app or the CMS web chat → `POST /assistant/chat` → AgentCore text runtime (`vsa_supervisor_text_<stage>`) → VSA supervisor | Text interactions, including the web chat opened from a vehicle page in the CMS console | 

## Voice channel [functional]
<a name="voice-channel-functional"></a>

The voice channel is the in-app voice session:

1. The driver opens the assistant in the AVX app. The app opens a WebSocket to the AgentCore bidirectional runtime, passing the user’s token, tenant, vehicle and driver at session start.

1. Nova 2 Sonic handles audio transcription and synthesis within the streaming session. The VSA supervisor runs on Claude Sonnet 4.6.

1. When the triage classifier returns P0 or P1, the session sends the classification to the app, which shows the escalation card. On P0 the stop-driving instruction comes first, word for word.

1. The session continues until the driver ends it. A handoff opens a Connect chat alongside the voice session rather than ending it.

Nova 2 Sonic latency target for voice is sub-700 ms from customer end-of-speech to first synthesized audio — achieved through streaming delivery of the supervisor’s first tokens before the full response is complete.

## Text channel [functional]
<a name="text-channel-functional"></a>

The text channel goes through the AVX API:

1. The app or the CMS web chat sends each message to `POST /assistant/chat` behind a Cognito authorizer.

1. The Lambda function reads the tenant from the caller’s `custom:tenantId` claim and, for a driver bound to a vehicle, the vehicle from the `custom:vehicleId` claim. A vehicle named in the request that doesn’t match the claim is dropped.

1. The function invokes the AgentCore text runtime with the message and returns the reply.

## Mobile and web escalation into Connect [functional]
<a name="mobile-and-web-escalation-into-connect-functional"></a>

Sessions that start in the AVX app or the web chat escalate into Connect mid-conversation. The pattern:

1. The driver talks to the supervisor in the app over the AgentCore WebSocket, or types in the web chat (`POST /assistant/chat`).

1. The triage classifier returns P0 or P1. The app shows a card with **Talk to an agent**, plus **Request roadside** on P0. The supervisor recommends the handoff; it does not open one by itself.

1. The driver’s tap sends only an intent (`human` or `roadside`) over the WebSocket. The runtime calls `POST /escalate` with the severity the classifier surfaced, never a value from the client or the model. A driver who asks for a person at any priority gets a service escalation, which carries no severity.

1.  `/escalate` starts a Connect chat with `StartChatContact`. The response carries the participant credentials, and the app joins the chat through the Connect Participant Service in the same screen.

The tier-2 agent sees the same triage result and summary whether the conversation started in Connect or in the app.