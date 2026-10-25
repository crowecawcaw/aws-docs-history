

# Build an external AI agent server
<a name="a2a-external-server"></a>

This page contains information on how to build and host an external AI agent, including an agent that you host on Amazon Bedrock AgentCore. It describes what your agent server must do, and what Connect Customer does, in each collaboration mode. For account setup, see [Set up an external AI agent integration](a2a-setup-external.md).

Your server must implement the Agent-to-Agent (A2A) protocol with the Connect Customer A2A extensions. The contract targets A2A protocol v1.0. This page explains how your server must behave in each collaboration mode. For event names, fields, and headers, see the [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html). For example payloads, see [A2A sample events](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html).

Your agent can collaborate in the following modes:
+ **Handle actions behind the scenes.** When the Connect AI agent decides to invoke your agent, it builds a text message for it. Your agent performs the work and returns a text result, which the Connect AI agent uses to invoke another action or to formulate a response to the customer. The Connect AI agent keeps talking to the customer.
+ **Talk to the customer.** Your agent takes over the conversation. Your agent exchanges text, or, with audio streaming, exchanges audio on voice contacts.

For how to configure a collaborator in one of these modes, see [Set up an external AI agent integration](a2a-setup-external.md).

## Transport and authentication
<a name="a2a-external-server-transport"></a>

Your server must meet the following transport and authentication requirements:
+ **Transport.** For text, your server can accept JSON-RPC over a secure WebSocket (`wss://`) or over HTTPS (`https://`). Audio streaming is supported over secure WebSocket (`wss://`) only.
+ **Authentication.** Connect Customer sends your API key as a bearer token when it connects. The Connect Customer administrator stores this key in AWS Secrets Manager during setup. Check the bearer token on each incoming connection or request, and reject the connection or request if the token doesn't match the API key that you issued.

Connect Customer also sends headers that activate the Connect Customer A2A extensions and carry trace context. For the header names and values, see [Transport and discovery](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-transport-discovery) in the A2A protocol contract.

## Session initiation
<a name="a2a-external-server-init"></a>

Each session starts when Connect Customer sends an `INIT_SESSION` event. Your server replies with `INIT_SESSION_RESPONSE`. You do not configure what Connect Customer sends. What happens next depends on the mode.

**Talk to the customer.** A session starts in the following order:

1. Connect Customer sends `INIT_SESSION`, and your server replies with `INIT_SESSION_RESPONSE`. `INIT_SESSION` carries session details, such as the conversation so far and information that identifies the contact, so the customer doesn't have to repeat their request.

1. Connect Customer sends `CHANNEL_STATE` with state `READY`. Wait for it before you send output to the customer.

1. Connect Customer sends customer turns, and your agent responds. For more information, see [Turn lifecycle](#a2a-external-server-turns).

In this mode, Connect Customer shares contact context, such as the channel, only when the Connect AI agent's security profile grants the **Access Contact Control Panel** permission. Connect Customer does not send custom contact attributes. For details on all of the context that Connect Customer shares, see [Session initiation](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-session-initiation) in the A2A protocol contract.

**Handle actions behind the scenes.** For each invocation, Connect Customer sends `INIT_SESSION`, and then the message that the Connect AI agent builds for your agent. There is no `CHANNEL_STATE` in this mode.

For example payloads, see [INIT\_SESSION](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-init-session) and [INIT\_SESSION\_RESPONSE](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-init-session-response) in A2A sample events.

## Connections by mode and channel
<a name="a2a-external-server-connections"></a>

How often Connect Customer opens a connection depends on the mode and the channel. Your server must handle a new `INIT_SESSION` on each new connection. The following table summarizes the behavior.

<a name="a2a-external-server-connections-table"></a>
<table>
<thead>
  <tr><th>Mode</th><th>Voice contacts</th><th>Chat contacts</th></tr>
</thead>
<tbody>
  <tr><td>Handle actions behind the scenes</td><td colspan="2">A new connection and <code>INIT_SESSION</code> each time the Connect AI agent invokes your agent. Each connection uses the same session (<code>contextId</code>).</td></tr>
  <tr><td>Talk to the customer (text)</td><td>WebSocket: one persistent connection for the whole session. HTTPS: separate requests, with no persistent connection. For the request flow, see the HTTPS table that follows.</td><td>A new connection for each customer message, with the same <code>contextId</code>. Connect Customer sends the conversation history again in each <code>INIT_SESSION</code>.</td></tr>
  <tr><td>Talk to the customer (audio)</td><td>One persistent secure WebSocket connection for the whole session, carrying audio.</td><td>Same as text. Connect Customer doesn't negotiate audio, so your agent must handle text.</td></tr>
</tbody>
</table>


Persistent connections apply only to talk to the customer sessions over WebSocket on voice contacts. Audio always uses a persistent secure WebSocket connection.

Over HTTPS, no socket stays open between messages. Connect Customer sends each step as a separate `SendMessage` request. The following table shows the request flow for each mode.


| Mode | What Connect Customer sends | What your server returns | 
| --- | --- | --- | 
| Talk to the customer | SendMessage requests in this order: INIT\_SESSION, then CHANNEL\_STATE with state READY, then the customer message. | For the customer message, the response or a task (taskId). If your server returns a task, Connect Customer polls for the response with GetTask. | 
| Handle actions behind the scenes | SendMessage requests with INIT\_SESSION, then the message that the Connect AI agent builds for your agent. There is no CHANNEL\_STATE in this mode. | The result, or a task (taskId) that Connect Customer polls with GetTask. | 

## Turn lifecycle
<a name="a2a-external-server-turns"></a>

In talk to the customer mode, text and audio, your agent handles each customer turn in the following order:

1. Stream a response message as an artifact. Each artifact carries one partial but complete message, streamed in chunks. End the message when it's complete. For how to mark the end of a message, see [Event conventions](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-event-conventions) in the A2A protocol contract.

1. Optionally, send another partial message as a new artifact.

1. Send the turn's `TRACING_SPAN` events. For more information, see [Tracing](#a2a-external-server-tracing).

1. Close the turn with a terminal task status update.

If your agent leaves an artifact or a task open, the customer's playback runs dry (an underrun). Connect Customer then closes the connection, and the collaboration ends with an error.

In talk to the customer mode, a normal turn doesn't end the collaboration. To end it, send `FINISH`. For more information, see [Finishing a collaboration](#a2a-external-server-finishing). For example payloads, see [Text response chunk](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-text-response-chunk) and [Terminal status update with FINISH](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-terminal-finish) in A2A sample events.

## Audio streaming
<a name="a2a-external-server-audio"></a>

In talk to the customer mode with audio streaming on voice contacts, your agent receives and sends audio. Audio streaming always uses immediate handoff, and it is supported only over secure WebSocket (`wss://`). In this mode, your agent handles speech itself. Connect Customer does not convert speech to text or text to speech for your agent.

Audio streaming is available only for external agents. An external agent that uses audio streaming must be the only collaborator on its Connect AI agent.

Your server must handle audio as follows:
+ **Agree on the audio format.** At session start, Connect Customer proposes a format for the caller's audio and a format for your agent's audio, so both sample rates are negotiated. Your server can accept them or counter-propose a different supported sample rate for either one. Every proposal and counter-proposal must be linear PCM, 16-bit, mono, at 8 kHz, 16 kHz, or 24 kHz. The format is fixed for the session, and Connect Customer resamples for the caller.
+ **Detect turns from the audio.** Caller audio streams continuously, with no turn boundary markers. Your agent detects turn-taking itself, for example with voice activity detection.
+ **Stream one response at a time.** Send each spoken response as a single audio artifact, as part of a distinct task. Do not open a second audio artifact while one is still open. Connect Customer treats conflicting artifacts as a protocol violation and closes the connection.
+ **Keep audio chunks small.** Don't split audio across fragments. Fragmented audio can't be played until all the parts arrive. Instead, keep each audio chunk small enough to fit in one WebSocket frame, so that each chunk can be played on its own.
+ **Finish every audio response.** End each audio artifact when the response is complete, and close each turn's task. An unfinished audio artifact causes an underrun, and Connect Customer closes the connection. For more information, see [Turn lifecycle](#a2a-external-server-turns).
+ **Handle interruptions.** When the caller speaks over your agent, send an `INTERRUPTION` event so that Connect Customer can flush buffered audio. Then close the current artifact and task, including the turn's trace, before you send a new response.
+ **Handle chat as text.** If the same collaborator serves chat contacts, Connect Customer does not negotiate audio. Your agent must accept and return text. To identify the channel, read it from contact context.

**Latency.** The latency that the caller experiences depends on both Connect Customer and your agent's processing time. Optimize your agent's response time to keep a natural conversational pace. We recommend that you work with your AWS account team or Solutions Architect to validate latency and audio quality before you go to production.

For the audio format fields and frame rules, see [Session initiation](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-session-initiation), [Transport fragmentation](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-transport-fragmentation), and [Interruptions](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-interruptions) in the A2A protocol contract. For example payloads, see [Audio input chunk](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-audio-input-chunk) and [Audio response chunk](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-audio-response-chunk) in A2A sample events.

## Finishing a collaboration
<a name="a2a-external-server-finishing"></a>

Finishing applies to talk to the customer mode only. Handle actions behind the scenes mode doesn't support `FINISH`. In that mode, each invocation is a request and response with the Connect AI agent, whenever it decides to invoke your agent, so there is no collaboration to finish.

In talk to the customer mode, your agent ends its participation by sending a `FINISH` event. Send `FINISH` only when your agent is done with the conversation, not at the end of every turn. After you send `FINISH`, do not send more messages on the session.

When your agent sends `FINISH`, control returns to the main Connect AI agent, which is invoked again with your reason. The main Connect AI agent can continue the conversation, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow.

Your agent can send the following finish types:
+ **`COMPLETE`**. The request is fulfilled. To return the contact to the flow, the main Connect AI agent can use its Complete tool, which follows the flow's Complete path.
+ **`ESCALATE`**. The conversation needs a human agent. To return the contact to the flow, the main Connect AI agent can use its Escalate tool, which follows the flow's Escalate path. There, the administrator can transfer the contact to a human agent.

For more information about the Complete and Escalate tools, see [Tools for orchestrator AI agents](agentic-self-service.md#agentic-self-service-default-tools).

When you finish, explain why. The main Connect AI agent may process your reason before the contact continues, and a specific reason helps it handle the outcome gracefully.

For the `FINISH` payload, see [Finishing: hand-back and terminal outcomes](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-finishing) in the A2A protocol contract. For an example, see [Terminal status update with FINISH](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-terminal-finish) in A2A sample events.

## Errors and retries
<a name="a2a-external-server-errors"></a>

When a turn starts but cannot complete, send a terminal status update that marks the task as failed and includes a structured error. Connect Customer also treats a JSON-RPC error from your agent as a failure. A terminal failed, canceled, or rejected task ends the collaboration, not just the turn, and the contact returns to the flow's Error branch.

Connect Customer retries as follows:
+ If a WebSocket connection attempt fails with certain errors, Connect Customer retries it once.
+ In talk to the customer mode on voice contacts over WebSocket, if an established connection drops unexpectedly, Connect Customer reconnects once. On chat contacts, Connect Customer doesn't reconnect. For details, see [Connection retries, reconnects, and close codes](#a2a-external-server-reconnect).

If the retry or reconnect fails, the collaboration fails. The contact returns to the error branch of the contact flow, where the administrator configures a fallback.

For the error levels, codes, and fields, see [Errors](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-errors) in the A2A protocol contract. For an example, see [Task failure with structured error](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-task-failed) in A2A sample events.

### Connection retries, reconnects, and close codes
<a name="a2a-external-server-reconnect"></a>

**Connection attempts.** Connect Customer retries a failed connection attempt once for certain errors. This applies to every WebSocket connection, including each chat message's connection. For which errors, see [Connection attempt retries](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-errors-connection-retries) in the A2A protocol contract.

**Reconnects.** In talk to the customer mode on voice contacts over WebSocket, with text or audio streaming, Connect Customer handles a dropped connection as follows. The reconnect attempt gets the same upgrade retry as any other connection attempt.

If the WebSocket connection drops during the session, Connect Customer tries to reconnect once before the collaboration fails. Connect Customer also reconnects when the socket fails with no close frame, or when the connection closes with one of the following codes:
+ `1005` – No Status Received
+ `1006` – Abnormal Closure
+ `1012` – Service Restart
+ `1013` – Try Again Later
+ `1014` – Bad Gateway

Any other close code, including `1000` (Normal Closure), ends the collaboration without a reconnect. Don't close the connection mid-session to end a conversation. Send `FINISH` instead. For more information, see [Finishing a collaboration](#a2a-external-server-finishing). If you must restart your server during a deployment, close the persistent voice connection with `1012` so that Connect Customer reconnects.

The following rules apply to reconnects:
+ **One reconnect per session.** Connect Customer reconnects at most once per collaboration session. A successful reconnect doesn't reset this limit, so a second drop ends the collaboration.
+ **New session initialization.** A reconnect re-initializes the session. Connect Customer opens a new connection, sends a new `INIT_SESSION` with the same `contextId`, and then sends `CHANNEL_STATE` with state `READY`. Your server must handle a repeated `INIT_SESSION` for the same `contextId`.
+ **Failure.** If the reconnect fails, or a second drop occurs, Connect Customer ends the collaboration and closes your connection with code `1011`. The contact returns to the contact flow's Error branch. For more information, see [Errors and retries](#a2a-external-server-errors).

**Chat contacts.** Each customer message uses its own WebSocket connection, which closes after the turn. If the connection drops during a turn, Connect Customer doesn't reconnect, whatever the close code, and the collaboration fails. The next customer message opens a new connection, unless the collaboration has already ended.

In handle actions behind the scenes mode, each invocation uses its own connection. Connect Customer doesn't reconnect a dropped invocation.

## Tracing
<a name="a2a-external-server-tracing"></a>

Your server must publish `TRACING_SPAN` events for every turn, covering the turn's input, output, and tool activity. Connect Customer disables external agent endpoints that do not send the required trace data. For the requirements and how enforcement works, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md). For the field names and wire format, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract and [TRACING\_SPAN](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-tracing-span) in A2A sample events.

## Related topics
<a name="a2a-external-server-related"></a>
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)
+ [A2A sample events](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html)
+ [Set up an external AI agent integration](a2a-setup-external.md)
+ [How agent-to-agent collaboration works](a2a-how-it-works.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Quotas and limitations for agent-to-agent collaboration](a2a-quotas.md)