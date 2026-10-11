

# Voice sessions
<a name="ca-voice"></a>

Voice is the most intricate subsystem in the app, and the one where platform constraints are most visible. The agent architecture behind it is documented in [Amazon Nova 2 Sonic speech-to-speech voice](nova-sonic-voice.md); what follows is the client half.

## Transport and authentication
<a name="ca-voice-transport"></a>

The app opens a SigV4-signed WebSocket to the Amazon Bedrock AgentCore bidirectional runtime. Signing requires AWS credentials rather than a bearer token, so the app exchanges its Cognito identity for temporary credentials through an Amazon Cognito identity pool federated with the user pool it signed into, and signs the request with those. The credentials are short-lived by construction.

This is the app’s only AWS-signed request path; every other call is a bearer-token REST request. It is also the path that fails most legibly when the identity pool is not configured to trust the user pool the app signs into — see [the identity-pool troubleshooting entry](ts-voice-identity-pool.md).

## Wire protocol
<a name="ca-voice-protocol"></a>

A small JSON message protocol runs over the socket in both directions.


| Direction | Message | Meaning | 
| --- | --- | --- | 
| App to runtime |  `session.start`  | Opens the session and supplies session context. | 
| App to runtime |  `audio.chunk`  | One captured audio frame, base64-encoded, with its sample rate. | 
| App to runtime |  `text.input`  | A typed message, used when the user types instead of speaking and when a screen primes the conversation. | 
| App to runtime |  `escalation.request`  | Requests handoff to a contact-center agent. | 
| App to runtime |  `session.end`  | Closes the session. | 
| Runtime to app |  `transcript`  | Incremental or final transcript text, for either speaker. | 
| Runtime to app |  `audio.chunk`  | Synthesized speech for playback. | 
| Runtime to app |  `tool.call` / `tool.result`  | A tool invocation and its result, surfaced in the reasoning drawer. | 
| Runtime to app |  `classification`  | A triage classification. | 
| Runtime to app |  `escalation`  | Escalation status, driving the handoff banner. | 
| Runtime to app |  `interruption`  | The user spoke over the agent; playback is cut. | 
| Runtime to app |  `info.message`  | A screen-side card emitted by a tool — for example a tire-pressure table — rendered as Markdown rather than spoken. | 
| Runtime to app |  `session.ended`, `error`, `debug`  | Termination, failure, and diagnostic detail. | 

The `info.message` type exists because some answers are better read than heard. A tool that produces tabular content sends it to the screen while the agent narrates a summary, instead of reading a table aloud.

## Audio formats, and why they differ by direction
<a name="ca-voice-audio"></a>

Capture and playback use deliberately different formats.

 **Capture** is 16 kHz mono 16-bit PCM. Device input rarely matches, so each buffer is converted to the target format, then base64-encoded into an `audio.chunk`. The app also tracks per-chunk peak amplitude so a silent microphone is distinguishable from silence in the room when reading logs.

 **Playback** is 24 kHz, and the player node is connected to the mixer using the standard deinterleaved **Float32** format, with each incoming 16-bit chunk converted per buffer. The conversion is not a stylistic preference. Connecting a player node to the main mixer with a 16-bit format is accepted by the simulator and **fails on real devices**, raising an Objective-C exception that Swift cannot catch — the app terminates rather than degrading. The Float32 connection is pinned by a unit test so the crash cannot be reintroduced by a plausible-looking simplification.

A related device condition is handled explicitly rather than allowed to crash: when the audio hardware reports a zero sample rate or no channels, capture and playback are unavailable, the app says so, and the session continues as a text conversation. Installing an audio tap against a zero-rate format raises the same uncatchable class of exception, so the check happens before the tap, not after.

## Session state machine
<a name="ca-voice-state"></a>

The voice session moves through seven states — disconnected, connecting, ready, talking, thinking, speaking, and an error state carrying its reason. The UI derives from this state rather than maintaining a parallel copy: the thinking indicator, for instance, is a function of the session state rather than a row inserted and removed by individual call sites, which is what keeps it from appearing at the wrong moments.

![Assistant in the ready state](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-assistant-ready.png)


The assistant in the `ready` state, before any utterance. The header names the persona and the vehicle in session, so the user can see what context the agent is working from. The state line is rendered from the session state rather than assembled per call site.

Messages typed while the session is still connecting are queued locally and marked pending, then sent when the session becomes ready, so the user is never told to wait for a connection.

Escalation state is tracked **orthogonally** to session state. When a handoff to a contact-center agent is initiated the voice session keeps running, so the agent can continue narrating to the driver while the contact-center channel opens; the handoff drives its own banner and chat surface. See [Handoff sequence](connect-warm-transfer.md).

## Keep-alives and timeouts
<a name="ca-voice-timing"></a>


| Interval | Behavior | 
| --- | --- | 
| \~1 second | The budget a tool call must return within. This is a platform constraint the app cannot influence, and the reason no reasoning step runs inside a tool. | 
| 55 seconds | Nova Sonic closes an idle session. The app sends periodic silence audio to keep a live session open while the user is reading or on another tab. | 
| 40 seconds | The keep-alive interval, chosen to stay comfortably inside the 55-second window. | 
| 90 seconds | The client-side allowance for a booking commit, which can legitimately take far longer than a conversational turn. | 
| 2–4 seconds | Typical setup cost of the WebSocket, agent and audio session — the reason a session is kept alive rather than reopened per utterance. | 

## Showing the reasoning
<a name="ca-voice-reasoning"></a>

Tool calls and their results are surfaced to the user in a reasoning drawer, alongside classifications and session boundaries. Each interaction records its name, input, output and timings, so the drawer shows not just that a tool ran but what it was asked and what it returned.

This is a deliberate transparency property rather than a debugging leftover. A conversational agent that says "I have booked Tuesday at one" is more trustworthy when the user can see the booking tool’s actual result, and a Finding narrated from Tier 2 evidence is more trustworthy when the evidence is inspectable. Booking confirmations and tool-emitted cards are rendered as structured cards in the transcript rather than as prose the agent composed.