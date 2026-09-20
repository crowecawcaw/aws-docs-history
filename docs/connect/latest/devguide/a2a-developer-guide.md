

# A2A protocol contract for external AI agents
<a name="a2a-developer-guide"></a>

This page walks you through building an external AI agent that collaborates with Connect Customer over the A2A protocol. It covers the wire protocol, session lifecycle, voice and chat channels, error handling, and tracing requirements in the order you encounter them when implementing your agent server.

To collaborate with Connect Customer, you must build and set up an AI agent that is compatible with the Connect Customer A2A extension. This developer documentation describes the protocol contract your agent server must implement. The Connect Customer admin setup page links here so that the team building the agent can find these implementation details.

If you are configuring an agent that someone else built rather than implementing one yourself, see [Set up collaboration with an external AI agent](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-setup-external.html) for registration and API setup. This page explains the contract at the level of behavior and sequencing, not individual fields.

**Topics**
+ [Prerequisites](#a2a-dg-prerequisites)
+ [Transport and discovery](#a2a-dg-transport-discovery)
+ [Channels](#a2a-dg-channels)
+ [Session initiation (handoff and immediate handoff)](#a2a-dg-session-initiation)
+ [Channel readiness (CHANNEL\_STATE)](#a2a-dg-channel-readiness)
+ [Finishing: hand-back and terminal outcomes](#a2a-dg-finishing)
+ [Errors](#a2a-dg-errors)
+ [Interruptions (barge-in)](#a2a-dg-interruptions)
+ [DTMF input](#a2a-dg-dtmf-input)
+ [Silence input](#a2a-dg-silence-input)
+ [Transport fragmentation (WebSocket only)](#a2a-dg-transport-fragmentation)
+ [Tracing](#a2a-dg-tracing)
+ [Note on A2A spec compliance](#a2a-dg-spec-compliance)
+ [Sample events](#a2a-dg-sample-events)
+ [Related topics](#a2a-dg-related-topics)

## Prerequisites
<a name="a2a-dg-prerequisites"></a>

Before your agent server can receive A2A traffic, the Connect Customer instance must have a Lex V2 bot and contact flow configured. These are setup steps described in [Set up collaboration with an external AI agent](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-setup-external.html), Step 6. Your agent server does not receive traffic until both are in place.

## Transport and discovery
<a name="a2a-dg-transport-discovery"></a>

Your agent server communicates with Connect Customer under the following transport rules:
+ Every agent must support JSON-RPC frames over WebSockets. The contract targets A2A protocol v1.0.
+ On WebSocket, each event is the same JSON-RPC result frame pushed over the socket.
+ **Authentication.** Connect Customer sends your API key as `Authorization: Bearer <apiKey>` on the WebSocket upgrade.
+ **Extension activation.** Connect Customer sends the header `A2A-Extensions: https://docs.aws.amazon.com/connect/a2a/ext/v1` on requests and upgrades. Echo it back to confirm activation.

### Event conventions
<a name="a2a-dg-event-conventions"></a>

The following conventions apply to every A2A event:
+ Extension semantics ride on standard A2A objects. The event type is in metadata under the key `https://docs.aws.amazon.com/connect/a2a/ext/v1/eventType`.
+ **Trace context.** Connect Customer sends W3C `traceparent` and `tracestate` (`connect=parentSpanId:{full-uuid}`) as headers on each request (WebSocket: on the connection upgrade). Adopt the propagated traceId and parent span in the spans you emit (see [A.10 TRACING\_SPAN (your agent to Connect)](#a2a-dg-sample-tracing-span)).

## Channels
<a name="a2a-dg-channels"></a>

Connect Customer supports communication through two channels, voice and chat, on the same contact flow.

For the voice channel, a persistent connection to the third-party server stays open over WebSockets.

For the chat channel, a new WebSocket connection opens for each new customer chat message. The connection uses the same `contextId` every time.

## Session initiation (handoff and immediate handoff)
<a name="a2a-dg-session-initiation"></a>

Before your agent receives turns in a handoff, Connect Customer sends `INIT_SESSION` (see [A.1 INIT\_SESSION (Connect to your agent)](#a2a-dg-sample-init-session)) and expects an `INIT_SESSION_RESPONSE`. You can receive the following fields:
+ **instanceArn, contactArn.** The Connect Customer instance and contact this session belongs to.
+ **history.** Prior conversation turns as A2A-native Message objects, oldest first, so the customer never re-states their request. On chat, expect a new connection for each turn, with history re-sent on each `INIT_SESSION`. On voice, one persistent connection serves the whole session. Empty for the first handoff when `immediateHandoff` is set to `true`.
+ **supportedFinishTypes.** The FINISH types the caller can route on. Emit only FINISH events whose type appears in this list.
+ **subscribeToTracingEvents.** When `true`, emit `TRACING_SPAN` events for each turn (see [Tracing](#a2a-dg-tracing)).
+ **audioInputConfiguration / audioOutputConfiguration.** Voice only. Connect Customer proposes a config (LINEAR\_PCM, 16-bit, mono, 8000, 16000, or 24000 Hz). Your `INIT_SESSION_RESPONSE` can counter-propose a different rate from the supported set (a counter-proposal is a full re-declaration). Connect Customer resamples between the negotiated config and the caller side. The config is fixed for the session.

Respond with `INIT_SESSION_RESPONSE` (see [A.2 INIT\_SESSION\_RESPONSE (your agent to Connect)](#a2a-dg-sample-init-session-response)).

## Channel readiness (CHANNEL\_STATE)
<a name="a2a-dg-channel-readiness"></a>

On a handoff, your agent gates its output on the channel being live. It must not start producing turn output until it has seen a `CHANNEL_STATE` event with state `READY` for the session. `READY` signals that the customer channel is connected and can receive your output.

`CHANNEL_STATE` is published only on handoff. Delegate does not transfer the channel, so no `READY` is sent for delegate interactions.

## Finishing: hand-back and terminal outcomes
<a name="a2a-dg-finishing"></a>

To conclude your agent's participation, emit a FINISH event. You can carry a finish data part on the terminal status update (see [A.5 Terminal status update with FINISH (your agent to Connect)](#a2a-dg-sample-terminal-finish)) or as a message on WebSockets. The types are:
+ **COMPLETE.** Request fulfilled. Control returns to the parent agent.
+ **ESCALATE.** The conversation needs a human. Connect Customer routes the contact to a human queue (surfaced to the contact flow through the Tool session attribute).

Emit only finish types that appear in the `supportedFinishTypes` sent on init. After emitting FINISH, your agent must not send further messages on the session. Connect Customer can close the connection immediately.

## Errors
<a name="a2a-dg-errors"></a>

Errors fall into these levels, based on where the failure occurs:
+ **Connection level.** Failures on the request or WebSocket upgrade surface as native HTTP status codes (for example, authentication failures, or 429 when Connect Customer throttles). No A2A event is involved.
+ **Request level.** A request your agent cannot dispatch (malformed frame, unknown method, unknown task) receives a standard JSON-RPC error object. According to A2A v1.0, the error's `data` carries a `google.rpc.ErrorInfo` object (`{"@type":"type.googleapis.com/google.rpc.ErrorInfo","reason":"...","domain":"a2a-protocol.org"}`). Connect Customer treats a JSON-RPC error from your agent as a failure.
+ **Task level.** The primary structured-error path. When a turn starts but cannot complete, emit a terminal statusUpdate with `status.state: TASK_STATE_FAILED`, carrying the structured error as an error data part on `status.message` (see [A.6 Task failure with structured error (your agent to Connect)](#a2a-dg-sample-task-failed)). Connect Customer consumes structured errors from this terminal task status update event. Fields: `errorCode` (HTTP-style: 408 timeout, 424 dependency failure, 400 bad request, 500 internal), `errorReason` (human-readable), `errorCategory` (`DEPENDENCY_FAILURE`, `INTERNAL_ERROR`, `TIMEOUT`, `BAD_REQUEST`, extensible; treat unknown values as generic failures).
+ **Standalone ERROR messages are informational, not terminal.** An ERROR event sent as its own message (see [A.6b Informational ERROR message (Connect to your agent)](#a2a-dg-sample-informational-error)) is a diagnostic signal. It does not change task state or end the turn. Connect Customer sends your agent one to explain a problem it detected. For fatal problems (an idle timeout 408, TIMEOUT, or a protocol violation such as conflicting artifacts 400, BAD\_REQUEST), the ERROR precedes Connect Customer closing the connection. For non-fatal problems (such as a malformed trace frame 400, BAD\_REQUEST), the connection stays open and the conversation continues. Treat the ERROR as context. The authoritative signals remain the terminal statusUpdate and the connection close.
+ **Failure compared to error disposition.** If your agent completes its participation but with an error outcome, that is a completion, not a task failure. Emit FINISH with `type: COMPLETE_WITH_ERROR` on a `TASK_STATE_COMPLETED` terminal (see [Finishing: hand-back and terminal outcomes](#a2a-dg-finishing)).
+ Connect Customer treats `TASK_STATE_FAILED`, `TASK_STATE_CANCELED`, and `TASK_STATE_REJECTED` from your agent as turn failures.

## Interruptions (barge-in)
<a name="a2a-dg-interruptions"></a>

When your agent is receiving text over the voice channel and the customer speaks over your agent's audio, Connect Customer sends an `INTERRUPTION` event with `type: USER_AUDIO_INPUT` (see [A.7 INTERRUPTION (either direction)](#a2a-dg-sample-interruption)). On receipt, stop generating, discard buffered output, and do not send a `lastChunk` for the interrupted artifact. Open a fresh `artifactId` for your next response.

When your agent is receiving customer audio directly, Connect Customer expects you to publish this event so that Connect Customer can flush any buffered audio. Interruption events also arrive if the customer gives a DTMF input with `type: DTMF_INPUT`. You can consume that or ignore it based on whether your agent consumes DTMF.

## DTMF input
<a name="a2a-dg-dtmf-input"></a>

Connect Customer accumulates telephone keypad input (end character `#`, deletion `*`, inter-digit timeout). It delivers the input to your agent as a single `DTMF_INPUT_COMPLETE` event that carries the accumulated `inputString` and a `terminationReason` (`END_CHARACTER`, `TIMEOUT`, or `MAX_LENGTH`). See [A.8 DTMF\_INPUT\_COMPLETE (Connect to your agent)](#a2a-dg-sample-dtmf). A companion `INTERRUPTION` (`type: DTMF_INPUT`) precedes it if output is in flight. Treat the digit string as the turn's input. Connect Customer fixes the accumulation policy at launch, and you cannot change it for individual sessions.

## Silence input
<a name="a2a-dg-silence-input"></a>

Connect Customer detects extended silence and sends input so that an agent can re-prompt the customer. Your agent receives a payload with the text value `<EMPTY_USER_INPUT>`.

## Transport fragmentation (WebSocket only)
<a name="a2a-dg-transport-fragmentation"></a>

Payloads that exceed the WebSocket frame budget split into `FRAGMENT` events (see [A.9 FRAGMENT (WebSocket only, either direction)](#a2a-dg-sample-fragment)). Buffer by `fragmentId`, reassemble in `partNumber` order after `totalParts` fragments arrive, then base64-decode into the original JSON payload. Your agent must reassemble inbound fragments and can fragment its own oversized frames. Use FRAGMENT only for complete payloads that exceed frame size. Never use it for progressive output streaming (use `artifactUpdate` chunks), never for audio (emit smaller independent audio chunks), and never on HTTPS.

## Tracing
<a name="a2a-dg-tracing"></a>

We recommend that your agent publish trace spans for observability through `TRACING_SPAN` events (a `tracingSpan` data part on an `artifactUpdate`). Traces ride as artifacts on the turn's task: emit each trace as an `artifactUpdate` carrying the turn's `taskId`. This is how Connect Customer attributes the trace to the turn. Connect Customer consumes and persists traces for analytics and multi-agent observability. They never reach the end customer. Emit each turn's traces after the response and before the terminal status update. Keep individual span payloads under the frame budget (split oversized trace messages with FRAGMENT).
+ **Wire format.** The `tracingSpan` payload wraps a standard OpenTelemetry OTLP/JSON TracesData document under an `otlp` key: `{"otlp": {"resourceSpans": [...]}}`. Generate spans with any OpenTelemetry SDK and serialize the finished spans with the OTLP/JSON encoding. See [A.10 TRACING\_SPAN (your agent to Connect)](#a2a-dg-sample-tracing-span).
+ **Session opt-in.** Connect Customer sets `subscribeToTracingEvents: true` on `INIT_SESSION` when it wants traces.
+ **Span naming (OpenTelemetry GenAI semantic conventions).** `invoke_agent <agentName>` as the root span for the turn (SpanKind SERVER), `chat <model>` around each LLM call (CLIENT), `execute_tool <toolName>` around each tool call (CLIENT).
+ **Required on every span.** `traceId`, `spanId`, `name`, `startTimeUnixNano`, `endTimeUnixNano`. Use a distinct `traceId` for each turn so that you can distinguish turns on persistent (voice) connections. Use the same `taskId` as the turn response.
+ **What to include for each turn.** The customer input, the agent's output, and any tool-call requests and results, carried as `aws.connect.span.message` span events with `role` (input, output, or instruction), `type` (for example, TEXT\_MESSAGE), `participant`, and `content` attributes. Set `status.code = ERROR` with a message on failure.
+ **Recognized attributes.** OTEL GenAI keys (`gen_ai.agent.name`, `gen_ai.operation.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, and others) plus Connect Customer public keys (`aws.connect.tool.id`, `aws.connect.tool.type`, `aws.connect.usage.total_tokens`, `aws.connect.error.type`, and others). You can emit additional keys; unrecognized keys have no effect.

## Note on A2A spec compliance
<a name="a2a-dg-spec-compliance"></a>

Certain types of A2A task states are currently unsupported. These include the following:
+ `TASK_STATE_UNSPECIFIED`
+ `TASK_STATE_SUBMITTED`
+ `TASK_STATE_CANCELED`
+ `TASK_STATE_INPUT_REQUIRED`
+ `TASK_STATE_REJECTED`
+ `TASK_STATE_AUTH_REQUIRED`

## Sample events
<a name="a2a-dg-sample-events"></a>

`<EXT>` = `https://docs.aws.amazon.com/connect/a2a/ext/v1`. The contract targets A2A protocol v1.0 (JSON-RPC binding). All samples show the full JSON-RPC framing. Requests from Connect Customer are JSON-RPC requests (method and params). Your agent's direct RPC response must echo the request's `id`. Events your agent streams back ride in a JSON-RPC result envelope whose value is exactly one of `message`, `task`, `statusUpdate`, or `artifactUpdate`. Connect Customer identifies each event by which of those keys is present (plus the `eventType` metadata) and correlates it by `contextId` and `taskId`.

### A.1 INIT\_SESSION (Connect to your agent)
<a name="a2a-dg-sample-init-session"></a>

The audio config is negotiated only when the third-party agent is voice enabled.

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "1",
    "params": {
        "message": {
            "messageId": "m-1",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "data": {
                    "initSession": {
                        "instanceArn": "<CONNECT_INSTANCE_ARN>",
                        "contactArn": "<CONNECT_CONTACT_ARN>",
                        "supportedFinishTypes": ["COMPLETE", "COMPLETE_WITH_ERROR", "ESCALATE"],
                        "subscribeToTracingEvents": true,
                        "audioInputConfiguration": {
                            "encoding": "LINEAR_PCM",
                            "sampleRateHertz": 8000,
                            "sampleSizeBits": 16,
                            "channelCount": 1
                        },
                        "audioOutputConfiguration": {
                            "encoding": "LINEAR_PCM",
                            "sampleRateHertz": 16000,
                            "sampleSizeBits": 16,
                            "channelCount": 1
                        },
                        "history": [{
                            "messageId": "h-1",
                            "role": "ROLE_USER",
                            "parts": [{
                                "text": "I need help with my bill",
                                "mediaType": "text/plain"
                            }]
                        }, {
                            "messageId": "h-2",
                            "role": "ROLE_AGENT",
                            "parts": [{
                                "text": "I can help with that.",
                                "mediaType": "text/plain"
                            }]
                        }]
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "INIT_SESSION"
            }
        }
    }
}
```

Text-only sessions omit the audio configurations. The `history` is re-sent on every chat reconnection.

### A.2 INIT\_SESSION\_RESPONSE (your agent to Connect)
<a name="a2a-dg-sample-init-session-response"></a>

Your agent sends this in reply to `INIT_SESSION`.

```
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "message": {
        "messageId": "m-2",
        "contextId": "<SESSION_ID>",
        "role": "ROLE_AGENT",
        "parts": [{
            "data": {
                "initSessionResponse": {
                    "statusCode": "200",
                    "audioOutputConfiguration": {
                        "encoding": "LINEAR_PCM",
                        "sampleRateHertz": 24000,
                        "sampleSizeBits": 16,
                        "channelCount": 1
                    }
                }
            },
            "mediaType": "application/json"
        }],
        "extensions": ["<EXT>"],
        "metadata": {
            "<EXT>/eventType": "INIT_SESSION_RESPONSE"
        }
    }
  }
}
```

The audio override is present only when counter-proposing. Omit it to accept the config that Connect Customer proposed.

### A.2b CHANNEL\_STATE READY (Connect to your agent, orchestrated/tool handoff)
<a name="a2a-dg-sample-channel-state"></a>

On a handoff, your agent treats receipt of READY as the signal that the channel is live and it can begin emitting output.

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "cs-1",
    "params": {
        "message": {
            "messageId": "m-cs-1",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "data": {
                    "channelState": {
                        "state": "READY"
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "CHANNEL_STATE"
            }
        }
    }
}
```

### A.3 Text turn input (Connect to your agent)
<a name="a2a-dg-sample-text-turn-input"></a>

After initialization, Connect Customer sends each customer message as a text turn.

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "req-1",
    "params": {
        "message": {
            "messageId": "m-3",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "text": "Why is my bill higher this month?",
                "mediaType": "text/plain"
            }],
            "metadata": {}
        }
    }
}
```

Voice sessions instead stream audio parts (see [A.3b Audio input chunk (Connect to your agent, voice, audio enabled 3P agent)](#a2a-dg-sample-audio-input-chunk)).

### A.3b Audio input chunk (Connect to your agent, voice, audio enabled 3P agent)
<a name="a2a-dg-sample-audio-input-chunk"></a>

Customer audio streams continuously as SendMessage requests, roughly one small PCM slice for each frame, each with its own JSON-RPC request id, at the negotiated `audioInputConfiguration`. There is no per-turn boundary marker on input audio. Your agent detects turn-taking from the audio itself (voice activity detection). Your spoken response does not correlate to any audio frame's request id: it streams back as `artifactUpdate` events on the turn's task (see [A.4b Audio response chunk (your agent to Connect, voice, audio enabled 3P agent)](#a2a-dg-sample-audio-response-chunk)).

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "req-audio-1",
    "params": {
        "message": {
            "messageId": "m-4",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "raw": "<BASE64_PCM_CHUNK>",
                "mediaType": "audio/lpcm"
            }],
            "metadata": {}
        }
    }
}
```

### A.4 Text response chunk (your agent to Connect)
<a name="a2a-dg-sample-text-response-chunk"></a>

Your agent streams text back as `artifactUpdate` events.

```
{
  "jsonrpc": "2.0",
  "id": "c7d03f92",
  "result": {
    "artifactUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "artifact": {
            "artifactId": "resp-1",
            "parts": [{
                "text": "Your bill increased because ",
                "mediaType": "text/plain"
            }],
            "metadata": {
                "<EXT>/eventType": "TEXT_RESPONSE_CHUNK"
            }
        },
        "append": false,
        "lastChunk": false
    }
  }
}
```

Continuations set `append: true`; the final chunk sets `lastChunk: true`. For audio output, see [A.4b Audio response chunk (your agent to Connect, voice, audio enabled 3P agent)](#a2a-dg-sample-audio-response-chunk).

### A.4b Audio response chunk (your agent to Connect, voice, audio enabled 3P agent)
<a name="a2a-dg-sample-audio-response-chunk"></a>

Spoken output streams as `artifactUpdate` events tagged `AUDIO_RESPONSE_CHUNK`, carrying base64-encoded PCM at the negotiated `audioOutputConfiguration`. All chunks of one spoken response share an `artifactId`; the first frame sets `append: false`, continuations set `append: true`, and the final frame sets `lastChunk: true`:

```
{
  "jsonrpc": "2.0",
  "id": "e15a8d43",
  "result": {
    "artifactUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "artifact": {
            "artifactId": "resp-1-audio",
            "parts": [{
                "raw": "<BASE64_PCM_CHUNK>",
                "mediaType": "audio/lpcm"
            }],
            "metadata": {
                "<EXT>/eventType": "AUDIO_RESPONSE_CHUNK"
            }
        },
        "append": false,
        "lastChunk": false
    }
  }
}
```

Each audio chunk must be independently playable: keep every frame under the transport frame budget rather than relying on FRAGMENT. You cannot play fragmented audio progressively. Emit audio at the negotiated output config; Connect Customer resamples toward the caller. If the customer barges in, stop the stream without sending `lastChunk` and open a fresh `artifactId` for the next response (see [A.7 INTERRUPTION (either direction)](#a2a-dg-sample-interruption)).

### A.5 Terminal status update with FINISH (your agent to Connect)
<a name="a2a-dg-sample-terminal-finish"></a>

Your agent sends this as the last frame of the turn.

```
{
  "jsonrpc": "2.0",
  "id": "2f6b9c18",
  "result": {
    "statusUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "status": {
            "state": "TASK_STATE_COMPLETED",
            "timestamp": "2026-08-08T16:40:00.000Z",
            "message": {
                "messageId": "m-9",
                "role": "ROLE_AGENT",
                "parts": [{
                    "data": {
                        "finish": {
                            "type": "ESCALATE",
                            "reason": "Customer requested a human agent"
                        }
                    },
                    "mediaType": "application/json"
                }],
                "metadata": {
                    "<EXT>/eventType": "FINISH"
                }
            }
        }
    }
  }
}
```

A normal mid-conversation turn ends with the same statusUpdate without the finish part.

### A.6 Task failure with structured error (your agent to Connect)
<a name="a2a-dg-sample-task-failed"></a>

The terminal statusUpdate for a failed turn. The structured error rides as an error data part on `status.message`, tagged with the ERROR eventType:

```
{
  "jsonrpc": "2.0",
  "id": "a3c47e05",
  "result": {
    "statusUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "status": {
            "state": "TASK_STATE_FAILED",
            "message": {
                "messageId": "m-10",
                "role": "ROLE_AGENT",
                "parts": [{
                    "data": {
                        "error": {
                            "errorCode": 424,
                            "errorReason": "Order lookup service timed out",
                            "errorCategory": "DEPENDENCY_FAILURE"
                        }
                    },
                    "mediaType": "application/json"
                }],
                "metadata": {
                    "<EXT>/eventType": "ERROR"
                }
            }
        }
    }
  }
}
```

### A.6b Informational ERROR message (Connect to your agent)
<a name="a2a-dg-sample-informational-error"></a>

Sent as a standalone message to explain a detected problem. Not a turn boundary. For fatal problems (idle timeout, artifact conflict) it precedes a connection close; for non-fatal problems (for example, a malformed trace) the conversation continues:

```
{
  "jsonrpc": "2.0",
  "method": "SendMessage",
  "id": "d90e5b72",
  "params": {
    "message": {
        "messageId": "m-11",
        "contextId": "<SESSION_ID>",
        "role": "ROLE_USER",
        "parts": [{
            "data": {
                "error": {
                    "errorCode": 408,
                    "errorReason": "No frames received within the idle window; closing the connection",
                    "errorCategory": "TIMEOUT"
                }
            },
            "mediaType": "application/json"
        }],
        "extensions": ["<EXT>"],
        "metadata": {
            "<EXT>/eventType": "ERROR"
        }
    }
  }
}
```

### A.7 INTERRUPTION (either direction)
<a name="a2a-dg-sample-interruption"></a>

When Connect Customer detects the interruption (for example, the customer speaks or presses a key while your agent's output is playing), it arrives as a SendMessage request:

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "req-3",
    "params": {
        "message": {
            "messageId": "m-11",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "data": {
                    "interruption": {
                        "type": "USER_AUDIO_INPUT",
                        "reason": "user_speech"
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "INTERRUPTION"
            }
        }
    }
}
```

When your agent detects the interruption (audio mode, your agent's own barge-in detection), emit the same event as a streamed frame so Connect Customer flushes buffered playback:

```
{
  "jsonrpc": "2.0",
  "id": "8f2d1c07",
  "result": {
    "message": {
        "messageId": "m-11a",
        "contextId": "<SESSION_ID>",
        "role": "ROLE_AGENT",
        "parts": [{
            "data": {
                "interruption": {
                    "type": "USER_AUDIO_INPUT",
                    "reason": "user_speech"
                }
            },
            "mediaType": "application/json"
        }],
        "extensions": ["<EXT>"],
        "metadata": {
            "<EXT>/eventType": "INTERRUPTION"
        }
    }
  }
}
```

The `type` is `USER_AUDIO_INPUT` for voice barge-in, `DTMF_INPUT` for keypad, `SYSTEM` otherwise.

### A.8 DTMF\_INPUT\_COMPLETE (Connect to your agent)
<a name="a2a-dg-sample-dtmf"></a>

Connect Customer delivers the accumulated keypad digits as a single event:

```
{
    "jsonrpc": "2.0",
    "method": "SendMessage",
    "id": "req-2",
    "params": {
        "message": {
            "messageId": "m-12",
            "contextId": "<SESSION_ID>",
            "role": "ROLE_USER",
            "parts": [{
                "data": {
                    "dtmfInputComplete": {
                        "inputString": "1234",
                        "terminationReason": "END_CHARACTER"
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "DTMF_INPUT_COMPLETE"
            }
        }
    }
}
```

### A.9 FRAGMENT (WebSocket only, either direction)
<a name="a2a-dg-sample-fragment"></a>

Connect Customer to third-party agent:

```
{
  "jsonrpc": "2.0",
  "method": "SendMessage",
  "id": "6a1f3d84",
  "params": {
    "message": {
        "messageId": "m-13",
        "role": "ROLE_AGENT",
        "parts": [{
            "data": {
                "fragment": {
                    "fragmentId": "f-1",
                    "partNumber": 0,
                    "totalParts": 3,
                    "payload": "<BASE64_CHUNK>",
                    "encoding": "base64"
                }
            },
            "mediaType": "application/json"
        }],
        "metadata": {
            "<EXT>/eventType": "FRAGMENT"
        }
    }
  }
}
```

Third-party agent to Connect Customer:

```
{
  "jsonrpc": "2.0",
  "id": "6a1f3d84",
  "result": {
    "message": {
        "messageId": "m-13",
        "role": "ROLE_AGENT",
        "parts": [{
            "data": {
                "fragment": {
                    "fragmentId": "f-1",
                    "partNumber": 0,
                    "totalParts": 3,
                    "payload": "<BASE64_CHUNK>",
                    "encoding": "base64"
                }
            },
            "mediaType": "application/json"
        }],
        "metadata": {
            "<EXT>/eventType": "FRAGMENT"
        }
    }
  }
}
```

Concatenate payload values in `partNumber` order and base64-decode to recover the original JSON payload. A FRAGMENT message contains exactly one data part and no other content parts.

### A.10 TRACING\_SPAN (your agent to Connect)
<a name="a2a-dg-sample-tracing-span"></a>

The following example shows a trace with a single root span:

```
{
  "jsonrpc": "2.0",
  "id": "b8c2e690",
  "result": {
    "artifactUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "artifact": {
            "artifactId": "trace-1",
            "parts": [{
                "data": {
                    "tracingSpan": {
                        "otlp": {
                            "resourceSpans": [{
                                "resource": {
                                    "attributes": [
                                        { "key": "service.name", "value": { "stringValue": "billing-agent" } }
                                    ]
                                },
                                "scopeSpans": [{
                                    "scope": { "name": "amazon.connect.ai-agent", "version": "1.0.0" },
                                    "spans": [{
                                        "traceId": "550e8400e29b41d4a716446655440000",
                                        "spanId": "eee19b7ec3c1b173",
                                        "parentSpanId": "6ba7b8109dad11d1",
                                        "name": "invoke_agent billing-agent",
                                        "kind": 2,
                                        "startTimeUnixNano": "1715000000000000000",
                                        "endTimeUnixNano": "1715000002500000000",
                                        "attributes": [
                                            { "key": "gen_ai.agent.name", "value": { "stringValue": "billing-agent" } },
                                            { "key": "gen_ai.operation.name", "value": { "stringValue": "invoke_agent" } },
                                            { "key": "gen_ai.usage.input_tokens", "value": { "intValue": "1200" } },
                                            { "key": "gen_ai.usage.output_tokens", "value": { "intValue": "340" } }
                                        ],
                                        "events": [
                                            {
                                                "name": "aws.connect.span.message",
                                                "timeUnixNano": "1715000000000000000",
                                                "attributes": [
                                                    { "key": "aws.connect.span.message.role", "value": { "stringValue": "input" } },
                                                    { "key": "aws.connect.span.message.type", "value": { "stringValue": "TEXT_MESSAGE" } },
                                                    { "key": "aws.connect.span.message.participant", "value": { "stringValue": "user" } },
                                                    { "key": "aws.connect.span.message.content", "value": { "stringValue": "What is my balance?" } }
                                                ]
                                            },
                                            {
                                                "name": "aws.connect.span.message",
                                                "timeUnixNano": "1715000002500000000",
                                                "attributes": [
                                                    { "key": "aws.connect.span.message.role", "value": { "stringValue": "output" } },
                                                    { "key": "aws.connect.span.message.type", "value": { "stringValue": "TEXT_MESSAGE" } },
                                                    { "key": "aws.connect.span.message.participant", "value": { "stringValue": "assistant" } },
                                                    { "key": "aws.connect.span.message.content", "value": { "stringValue": "Your current balance is $2,847.53." } }
                                                ]
                                            }
                                        ],
                                        "status": { "code": 1 }
                                    }]
                                }]
                            }]
                        }
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "TRACING_SPAN"
            }
        },
        "append": false,
        "lastChunk": true
    }
  }
}
```

The payload under `otlp` is a standard OpenTelemetry OTLP/JSON TracesData document. Generate spans with any OpenTelemetry SDK and serialize finished spans with the OTLP/JSON encoding. The trace rides as an artifact on the turn's task: the `artifactUpdate` carries the turn's `taskId`, which is how Connect Customer attributes the trace to the turn. The trace adopts the propagated context from Connect Customer: `traceId` comes from the request's `traceparent` header, and the root span's `parentSpanId` is the propagated parent span. The root `invoke_agent` span carries the turn's input and output as `aws.connect.span.message` events; add child `chat` and `execute_tool` spans for LLM and tool calls. Emit traces after the turn's response and before the terminal status update.

### A.10b TRACING\_SPAN with per-segment latency (multiple spans in one trace)
<a name="a2a-dg-sample-tracing-multi-segment"></a>

A turn can emit multiple output segments (for example, one sentence at a time). To record the latency of each segment, put one span for each segment inside the same `otlp` envelope, not multiple `TRACING_SPAN` frames. Connect Customer consumes the first `TRACING_SPAN` artifact on the turn and reads every span inside its `otlp.resourceSpans` batch, so all segment spans must ride in that single envelope. Each segment span carries its own `startTimeUnixNano`/`endTimeUnixNano` (segment latency = end minus start) and parents to the turn's `invoke_agent` root; give every span the turn's single `traceId`.

```
{
  "jsonrpc": "2.0",
  "id": "b8c2e691",
  "result": {
    "artifactUpdate": {
        "taskId": "task-1",
        "contextId": "<SESSION_ID>",
        "artifact": {
            "artifactId": "trace-1",
            "parts": [{
                "data": {
                    "tracingSpan": {
                        "otlp": {
                            "resourceSpans": [{
                                "resource": {
                                    "attributes": [
                                        { "key": "service.name", "value": { "stringValue": "billing-agent" } }
                                    ]
                                },
                                "scopeSpans": [{
                                    "scope": { "name": "amazon.connect.ai-agent", "version": "1.0.0" },
                                    "spans": [
                                        {
                                            "traceId": "550e8400e29b41d4a716446655440000",
                                            "spanId": "aaaa000000000001",
                                            "parentSpanId": "6ba7b8109dad11d1",
                                            "name": "invoke_agent billing-agent",
                                            "kind": 2,
                                            "startTimeUnixNano": "1715000000000000000",
                                            "endTimeUnixNano": "1715000001310000000",
                                            "attributes": [
                                                { "key": "gen_ai.agent.name", "value": { "stringValue": "billing-agent" } },
                                                { "key": "gen_ai.operation.name", "value": { "stringValue": "invoke_agent" } }
                                            ],
                                            "status": { "code": 1 }
                                        },
                                        {
                                            "traceId": "550e8400e29b41d4a716446655440000",
                                            "spanId": "bbbb000000000001",
                                            "parentSpanId": "aaaa000000000001",
                                            "name": "chat sentence-1",
                                            "kind": 3,
                                            "startTimeUnixNano": "1715000000000000000",
                                            "endTimeUnixNano": "1715000000420000000",
                                            "attributes": [
                                                { "key": "gen_ai.operation.name", "value": { "stringValue": "chat" } }
                                            ],
                                            "events": [{
                                                "name": "aws.connect.span.message",
                                                "timeUnixNano": "1715000000420000000",
                                                "attributes": [
                                                    { "key": "aws.connect.span.message.role", "value": { "stringValue": "output" } },
                                                    { "key": "aws.connect.span.message.type", "value": { "stringValue": "TEXT_MESSAGE" } },
                                                    { "key": "aws.connect.span.message.participant", "value": { "stringValue": "assistant" } },
                                                    { "key": "aws.connect.span.message.content", "value": { "stringValue": "Your bill increased by $40 this month." } }
                                                ]
                                            }],
                                            "status": { "code": 1 }
                                        },
                                        {
                                            "traceId": "550e8400e29b41d4a716446655440000",
                                            "spanId": "bbbb000000000002",
                                            "parentSpanId": "aaaa000000000001",
                                            "name": "chat sentence-2",
                                            "kind": 3,
                                            "startTimeUnixNano": "1715000000420000000",
                                            "endTimeUnixNano": "1715000000905000000",
                                            "attributes": [
                                                { "key": "gen_ai.operation.name", "value": { "stringValue": "chat" } }
                                            ],
                                            "events": [{
                                                "name": "aws.connect.span.message",
                                                "timeUnixNano": "1715000000905000000",
                                                "attributes": [
                                                    { "key": "aws.connect.span.message.role", "value": { "stringValue": "output" } },
                                                    { "key": "aws.connect.span.message.type", "value": { "stringValue": "TEXT_MESSAGE" } },
                                                    { "key": "aws.connect.span.message.participant", "value": { "stringValue": "assistant" } },
                                                    { "key": "aws.connect.span.message.content", "value": { "stringValue": "The increase is from your streaming add-on." } }
                                                ]
                                            }],
                                            "status": { "code": 1 }
                                        },
                                        {
                                            "traceId": "550e8400e29b41d4a716446655440000",
                                            "spanId": "bbbb000000000003",
                                            "parentSpanId": "aaaa000000000001",
                                            "name": "chat sentence-3",
                                            "kind": 3,
                                            "startTimeUnixNano": "1715000000905000000",
                                            "endTimeUnixNano": "1715000001310000000",
                                            "attributes": [
                                                { "key": "gen_ai.operation.name", "value": { "stringValue": "chat" } }
                                            ],
                                            "events": [{
                                                "name": "aws.connect.span.message",
                                                "timeUnixNano": "1715000001310000000",
                                                "attributes": [
                                                    { "key": "aws.connect.span.message.role", "value": { "stringValue": "output" } },
                                                    { "key": "aws.connect.span.message.type", "value": { "stringValue": "TEXT_MESSAGE" } },
                                                    { "key": "aws.connect.span.message.participant", "value": { "stringValue": "assistant" } },
                                                    { "key": "aws.connect.span.message.content", "value": { "stringValue": "You can remove it anytime in settings." } }
                                                ]
                                            }],
                                            "status": { "code": 1 }
                                        }
                                    ]
                                }]
                            }]
                        }
                    }
                },
                "mediaType": "application/json"
            }],
            "metadata": {
                "<EXT>/eventType": "TRACING_SPAN"
            }
        },
        "append": false,
        "lastChunk": true
    }
  }
}
```

Three chat segment spans nest under the one `invoke_agent` root; their start and end deltas give per-segment latencies of 420 ms, 485 ms, and 405 ms. All spans share one `traceId` and ride in a single `TRACING_SPAN` artifact. A second `TRACING_SPAN` frame on the same turn is not read, so batch every segment span into this one envelope.

## Related topics
<a name="a2a-dg-related-topics"></a>
+ [Observability for collaborating AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-observability.html)
+ [Trace data requirements for external AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-trace-enforcement.html)
+ [Configure voice for collaborating AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-voice.html)