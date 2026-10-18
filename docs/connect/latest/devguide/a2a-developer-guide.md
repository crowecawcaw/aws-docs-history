

# A2A protocol contract for external AI agents
<a name="a2a-developer-guide"></a>

This page describes the A2A protocol contract that your external AI agent server must implement to collaborate with Connect Customer. It covers what is on the wire: event names, fields, headers, error codes, and payloads. The contract targets A2A protocol v1.0.

For server behavior, such as collaboration modes, connections, the turn lifecycle, retries, and reconnects, start with [Build an external AI agent server](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html). For sample payloads of each event, see [A2A sample events](a2a-sample-events.md).

To register your agent and configure your Connect Customer instance to use it, see [Set up an external AI agent integration](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-setup-external.html).

**Topics**
+ [Transport and discovery](#a2a-dg-transport-discovery)
+ [Session initiation](#a2a-dg-session-initiation)
+ [Channel readiness](#a2a-dg-channel-readiness)
+ [Finishing: hand-back and terminal outcomes](#a2a-dg-finishing)
+ [Errors](#a2a-dg-errors)
+ [Interruptions](#a2a-dg-interruptions)
+ [DTMF input](#a2a-dg-dtmf-input)
+ [Silence input](#a2a-dg-silence-input)
+ [Transport fragmentation](#a2a-dg-transport-fragmentation)
+ [Tracing](#a2a-dg-tracing)
+ [Note on A2A spec compliance](#a2a-dg-spec-compliance)
+ [Related topics](#a2a-dg-related-topics)
+ [A2A sample events](a2a-sample-events.md)

## Transport and discovery
<a name="a2a-dg-transport-discovery"></a>

Your agent server communicates with Connect Customer under the following transport rules:
+ Your agent exchanges JSON-RPC frames with Connect Customer over WebSocket (`wss://`) or HTTPS (`https://`). Audio streaming requires WebSocket. For which collaboration mode uses which transport, see [Transport and authentication](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-transport).
+ On WebSocket, each event is the same JSON-RPC result frame pushed over the socket.
+ **Authentication.** Connect Customer sends your API key as `Authorization: Bearer <apiKey>` on each HTTPS request and on the WebSocket upgrade.
+ **Extension activation.** Connect Customer sends the header `A2A-Extensions: https://docs.aws.amazon.com/connect/a2a/ext/v1` on requests and upgrades. Echo it back to confirm activation.

### Event conventions
<a name="a2a-dg-event-conventions"></a>

The following conventions apply to every A2A event:
+ Extension semantics ride on standard A2A objects. The event type is in metadata under the key `https://docs.aws.amazon.com/connect/a2a/ext/v1/eventType`.
+ **Trace context.** Connect Customer sends W3C `traceparent` and `tracestate` (`connect=parentSpanId:{full-uuid}`) as headers on each request (WebSocket: on the connection upgrade). Adopt the propagated traceId and parent span in the spans you emit (see [A.10 TRACING\_SPAN (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-tracing-span)).
+ **Response artifacts.** Each response artifact carries one partial but complete message, streamed in chunks. Set `lastChunk: true` on the final chunk of that message. Send the next partial message in a new artifact. To close the turn, send a terminal task status. For a sample, see [A.4 Text response chunk (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-text-response-chunk).

## Session initiation
<a name="a2a-dg-session-initiation"></a>

In talk to the customer mode, before your agent receives turns, Connect Customer sends `INIT_SESSION` (see [A.1 INIT\_SESSION (Connect to your agent)](a2a-sample-events.md#a2a-dg-sample-init-session)) and expects an `INIT_SESSION_RESPONSE`. You can receive the following fields:
+ **instanceArn, contactArn.** The Connect Customer instance and contact this session belongs to.
+ **history.** Prior conversation turns as A2A-native Message objects, oldest first. On chat, Connect Customer re-sends the history on each `INIT_SESSION`. Empty for the first handoff when `immediateHandoff` is set to `true`.
+ **contactContext.** System attributes for the contact: the customer address, the system address, and the channel (voice or chat). Custom contact attributes aren't included. Connect Customer includes this field only when the AI agent's security profile has the required permission. For the permission, see [Session initiation](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-init).
+ **supportedFinishTypes.** The FINISH types the caller can route on. Emit only FINISH events whose type appears in this list.
+ **subscribeToTracingEvents.** Indicates whether Connect Customer is subscribed to trace events for the session. For the tracing requirements, see [Tracing](#a2a-dg-tracing).
+ **audioInputConfiguration / audioOutputConfiguration.** Voice only. Connect Customer proposes a config (LINEAR\_PCM, 16-bit, mono, 8000, 16000, or 24000 Hz). Your `INIT_SESSION_RESPONSE` can counter-propose a different rate from the supported set (a counter-proposal is a full re-declaration). Connect Customer resamples between the negotiated config and the caller side. The config is fixed for the session.

Respond with `INIT_SESSION_RESPONSE` (see [A.2 INIT\_SESSION\_RESPONSE (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-init-session-response)).

For when Connect Customer starts a session in each collaboration mode and on each channel, see [Session initiation](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-init) and [Connections by mode and channel](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-connections).

## Channel readiness
<a name="a2a-dg-channel-readiness"></a>

In talk to the customer mode, your agent gates its output on the channel being live. It must not start producing turn output until it has seen a `CHANNEL_STATE` event with state `READY` for the session. `READY` signals that the customer channel is connected and can receive your output.

Connect Customer publishes `CHANNEL_STATE` only in talk to the customer mode. Handle actions behind the scenes mode doesn't transfer the channel, so Connect Customer doesn't send `READY` in that mode.

## Finishing: hand-back and terminal outcomes
<a name="a2a-dg-finishing"></a>

Hand-back is when your agent sends FINISH to return control of the conversation to the orchestrating Connect AI agent. That agent can then continue, invoke another collaborator, or use its Complete or Escalate tool to return the contact to the flow. For when to finish and what Connect Customer does after hand-back, see [Finishing a collaboration](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-finishing).

To conclude your agent's participation, emit a FINISH event. You can carry a finish data part on the terminal status update (see [A.5 Terminal status update with FINISH (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-terminal-finish)) or as a message on WebSockets. The types are:
+ **COMPLETE.** Your agent fulfilled the request.
+ **ESCALATE.** The conversation needs a human agent.

Emit only finish types that appear in the `supportedFinishTypes` sent on init. After emitting FINISH, your agent must not send further messages on the session. Connect Customer can close the connection immediately.

## Errors
<a name="a2a-dg-errors"></a>

For what fails and how Connect Customer responds, see [Errors and retries](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-errors).

Errors fall into these levels, based on where the failure occurs:
+ **Connection level.** Failures on the request or WebSocket upgrade surface as native HTTP status codes (for example, authentication failures, or 429 when your server throttles Connect Customer requests). No A2A event is involved.
+ **Request level.** A request your agent cannot dispatch (malformed frame, unknown method, unknown task) receives a standard JSON-RPC error object. According to A2A v1.0, the error's `data` carries a `google.rpc.ErrorInfo` object (`{"@type":"type.googleapis.com/google.rpc.ErrorInfo","reason":"...","domain":"a2a-protocol.org"}`). Connect Customer treats a JSON-RPC error from your agent as a failure.
+ **Task level.** The primary structured-error path. When a turn starts but cannot complete, emit a terminal statusUpdate with `status.state: TASK_STATE_FAILED`, carrying the structured error as an error data part on `status.message` (see [A.6 Task failure with structured error (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-task-failed)). Connect Customer consumes structured errors from this terminal task status update event. Fields: `errorCode` (HTTP-style: 408 timeout, 424 dependency failure, 400 bad request, 500 internal), `errorReason` (human-readable), `errorCategory` (`DEPENDENCY_FAILURE`, `INTERNAL_ERROR`, `TIMEOUT`, `BAD_REQUEST`, extensible; treat unknown values as generic failures).
+ **Standalone ERROR messages are informational, not terminal.** An ERROR event sent as its own message (see [A.6b Informational ERROR message (Connect to your agent)](a2a-sample-events.md#a2a-dg-sample-informational-error)) is a diagnostic signal. It does not change task state or end the turn. Connect Customer sends your agent one to explain a problem it detected. For fatal problems (an idle timeout 408, TIMEOUT, or a protocol violation such as conflicting artifacts 400, BAD\_REQUEST), the ERROR precedes Connect Customer closing the connection. For non-fatal problems (such as a malformed trace frame 400, BAD\_REQUEST), the connection stays open and the conversation continues. Treat the ERROR as context. The authoritative signals remain the terminal statusUpdate and the connection close.
+ **Terminal failure states end the collaboration.** A terminal `TASK_STATE_FAILED`, `TASK_STATE_CANCELED`, or `TASK_STATE_REJECTED` from your agent ends the collaboration, not just the turn. The collaboration ends with an error, and Connect Customer closes the connection. For what happens to the contact, see [Errors and retries](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-errors).

### Connection attempt retries
<a name="a2a-dg-errors-connection-retries"></a>

The following rules apply to every WebSocket connection that Connect Customer opens, in either collaboration mode:
+ If the WebSocket upgrade fails with HTTP `502`, `503`, or `504`, Connect Customer retries the upgrade once. It also retries once when there is no HTTP response, for example after a DNS failure, a connection reset, a TLS error, or a connect timeout.
+ Connect Customer doesn't retry any other status, including `400`, `401`, `403`, `408`, `429`, and `500`. The attempt fails immediately. For example, an invalid API key returns `401` or `403`.
+ Over HTTPS (JSON-RPC), Connect Customer doesn't retry failed requests.
+ The retry covers only opening the WebSocket connection. After the connection opens, your server might respond to `INIT_SESSION` with an error, or not send `INIT_SESSION_RESPONSE` in time. In that case, Connect Customer doesn't send `INIT_SESSION` again on that connection, and the connection attempt fails. A reconnect on a voice contact is different: it opens a new connection and sends a new `INIT_SESSION`.

For how Connect Customer reconnects after a dropped connection, and which close codes trigger a reconnect, see [Connection retries, reconnects, and close codes](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html#a2a-external-server-reconnect).

## Interruptions
<a name="a2a-dg-interruptions"></a>

When your agent is receiving text over the voice channel and the customer speaks over your agent's audio, Connect Customer sends an `INTERRUPTION` event with `type: USER_AUDIO_INPUT` (see [A.7 INTERRUPTION (either direction)](a2a-sample-events.md#a2a-dg-sample-interruption)). On receipt, stop generating, discard buffered output, and do not send a `lastChunk` for the interrupted artifact. Open a fresh `artifactId` for your next response.

When your agent is receiving customer audio directly, Connect Customer expects you to publish this event so that Connect Customer can flush any buffered audio. Interruption events also arrive if the customer gives a DTMF input with `type: DTMF_INPUT`. You can consume that or ignore it based on whether your agent consumes DTMF.

## DTMF input
<a name="a2a-dg-dtmf-input"></a>

Connect Customer accumulates telephone keypad input (end character `#`, deletion `*`, inter-digit timeout). It delivers the input to your agent as a single `DTMF_INPUT_COMPLETE` event that carries the accumulated `inputString` and a `terminationReason` (`END_CHARACTER`, `TIMEOUT`, or `MAX_LENGTH`). See [A.8 DTMF\_INPUT\_COMPLETE (Connect to your agent)](a2a-sample-events.md#a2a-dg-sample-dtmf). A companion `INTERRUPTION` (`type: DTMF_INPUT`) precedes it if output is in flight. Treat the digit string as the turn's input. The accumulation policy is fixed. You can't change it for individual sessions.

## Silence input
<a name="a2a-dg-silence-input"></a>

Connect Customer detects extended silence and sends input so that an agent can re-prompt the customer. Your agent receives a payload with the text value `<EMPTY_USER_INPUT>`.

## Transport fragmentation
<a name="a2a-dg-transport-fragmentation"></a>

Transport fragmentation applies to WebSocket connections only. Payloads that exceed the WebSocket frame budget split into `FRAGMENT` events (see [A.9 FRAGMENT (WebSocket only, either direction)](a2a-sample-events.md#a2a-dg-sample-fragment)). Buffer by `fragmentId`, reassemble in `partNumber` order after `totalParts` fragments arrive, then base64-decode into the original JSON payload. Your agent must reassemble inbound fragments and can fragment its own oversized frames. Use FRAGMENT only for complete payloads that exceed frame size. Never use it for progressive output streaming (use `artifactUpdate` chunks), never for audio (emit smaller independent audio chunks), and never on HTTPS.

## Tracing
<a name="a2a-dg-tracing"></a>

Your agent must publish `TRACING_SPAN` events for every turn (a `tracingSpan` data part on an `artifactUpdate`). Traces ride as artifacts on the turn's task: emit each trace as an `artifactUpdate` carrying the turn's `taskId`. This is how Connect Customer attributes the trace to the turn. Connect Customer consumes and persists traces for analytics and multi-agent observability. They never reach the end customer. Emit each turn's traces after the response and before the terminal status update. Keep individual span payloads under the frame budget (split oversized trace messages with FRAGMENT).

For the trace data that Connect Customer requires from external AI agents, see [Trace data requirements for external AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-trace-enforcement.html).
+ **Wire format.** The `tracingSpan` payload wraps a standard OpenTelemetry OTLP/JSON TracesData document under an `otlp` key: `{"otlp": {"resourceSpans": [...]}}`. Generate spans with any OpenTelemetry SDK and serialize the finished spans with the OTLP/JSON encoding. See [A.10 TRACING\_SPAN (your agent to Connect)](a2a-sample-events.md#a2a-dg-sample-tracing-span).
+ **Session subscription.** `INIT_SESSION` carries `subscribeToTracingEvents`, which indicates whether Connect Customer is subscribed to trace events for the session.
+ **Span naming (OpenTelemetry GenAI semantic conventions).** `invoke_agent <agentName>` as the root span for the turn (SpanKind SERVER), `chat <model>` around each LLM call (CLIENT), `execute_tool <toolName>` around each tool call (CLIENT).
+ **Required on every span.** `traceId`, `spanId`, `name`, `startTimeUnixNano`, `endTimeUnixNano`. Use the trace context that Connect Customer propagates in `traceparent`. Use the same `taskId` as the turn response.
+ **What to include for each turn.** The customer input, the agent's output, and any tool-call requests and results, carried as `aws.connect.span.message` span events with `role` (input, output, or instruction), `type` (for example, TEXT\_MESSAGE), `participant`, and `content` attributes. Set `status.code = ERROR` with a message on failure.
+ **Recognized attributes.** OTEL GenAI keys (`gen_ai.agent.name`, `gen_ai.operation.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, and others) plus Connect Customer-defined keys (`aws.connect.span.message.tool_id`, `aws.connect.span.message.tool_type`, `aws.connect.usage.total_tokens`, `aws.connect.error.type`, and others). You can emit additional keys; unrecognized keys have no effect.

## Note on A2A spec compliance
<a name="a2a-dg-spec-compliance"></a>

Connect Customer doesn't support the following A2A task states:
+ `TASK_STATE_UNSPECIFIED`
+ `TASK_STATE_SUBMITTED`
+ `TASK_STATE_INPUT_REQUIRED`
+ `TASK_STATE_AUTH_REQUIRED`

For how Connect Customer handles `TASK_STATE_FAILED`, `TASK_STATE_CANCELED`, and `TASK_STATE_REJECTED`, see [Errors](#a2a-dg-errors).

## Related topics
<a name="a2a-dg-related-topics"></a>
+ [Observability for collaborating AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-observability.html)
+ [Trace data requirements for external AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-trace-enforcement.html)
+ [Build an external AI agent server](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-external-server.html)
+ [A2A sample events](a2a-sample-events.md)