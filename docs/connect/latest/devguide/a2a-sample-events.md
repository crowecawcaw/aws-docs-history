

# A2A sample events
<a name="a2a-sample-events"></a>

This page shows sample payloads for the events that your external AI agent exchanges with Connect Customer. Each sample shows one event. For the rules that govern each event and its fields, see [A2A protocol contract for external AI agents](a2a-developer-guide.md).

`<EXT>` = `https://docs.aws.amazon.com/connect/a2a/ext/v1`. The contract targets A2A protocol v1.0 (JSON-RPC binding). All samples show the full JSON-RPC framing. Requests from Connect Customer are JSON-RPC requests (method and params). Your agent's direct RPC response must echo the request's `id`. Events your agent streams back ride in a JSON-RPC result envelope whose value is exactly one of `message`, `task`, `statusUpdate`, or `artifactUpdate`. Connect Customer identifies each event by which of those keys is present (plus the `eventType` metadata) and correlates it by `contextId` and `taskId`.

**Topics**
+ [A.1 INIT\_SESSION (Connect to your agent)](#a2a-dg-sample-init-session)
+ [A.2 INIT\_SESSION\_RESPONSE (your agent to Connect)](#a2a-dg-sample-init-session-response)
+ [A.2b CHANNEL\_STATE READY (Connect to your agent, talk to the customer mode)](#a2a-dg-sample-channel-state)
+ [A.3 Text turn input (Connect to your agent)](#a2a-dg-sample-text-turn-input)
+ [A.3b Audio input chunk (Connect to your agent, voice, external AI agent with audio streaming)](#a2a-dg-sample-audio-input-chunk)
+ [A.4 Text response chunk (your agent to Connect)](#a2a-dg-sample-text-response-chunk)
+ [A.4b Audio response chunk (your agent to Connect, voice, external AI agent with audio streaming)](#a2a-dg-sample-audio-response-chunk)
+ [A.5 Terminal status update with FINISH (your agent to Connect)](#a2a-dg-sample-terminal-finish)
+ [A.6 Task failure with structured error (your agent to Connect)](#a2a-dg-sample-task-failed)
+ [A.6b Informational ERROR message (Connect to your agent)](#a2a-dg-sample-informational-error)
+ [A.7 INTERRUPTION (either direction)](#a2a-dg-sample-interruption)
+ [A.8 DTMF\_INPUT\_COMPLETE (Connect to your agent)](#a2a-dg-sample-dtmf)
+ [A.9 FRAGMENT (WebSocket only, either direction)](#a2a-dg-sample-fragment)
+ [A.10 TRACING\_SPAN (your agent to Connect)](#a2a-dg-sample-tracing-span)
+ [A.10b TRACING\_SPAN with per-segment latency (multiple spans in one trace)](#a2a-dg-sample-tracing-multi-segment)

## A.1 INIT\_SESSION (Connect to your agent)
<a name="a2a-dg-sample-init-session"></a>

The audio config is negotiated only when `audioStreamingEnabled` is `true` and the contact is a voice contact.

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
                        "supportedFinishTypes": ["COMPLETE", "ESCALATE"],
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

Text-only sessions omit the audio configurations. The `history` is re-sent in the `INIT_SESSION` on each new chat connection (one for each customer message).

## A.2 INIT\_SESSION\_RESPONSE (your agent to Connect)
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

## A.2b CHANNEL\_STATE READY (Connect to your agent, talk to the customer mode)
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

## A.3 Text turn input (Connect to your agent)
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

Audio streaming sessions on voice contacts instead stream audio parts (see [A.3b Audio input chunk (Connect to your agent, voice, external AI agent with audio streaming)](#a2a-dg-sample-audio-input-chunk)).

## A.3b Audio input chunk (Connect to your agent, voice, external AI agent with audio streaming)
<a name="a2a-dg-sample-audio-input-chunk"></a>

Customer audio streams continuously as SendMessage requests, roughly one small PCM slice for each frame, each with its own JSON-RPC request id, at the negotiated `audioInputConfiguration`. There is no per-turn boundary marker on input audio. Your agent detects turn-taking from the audio itself (voice activity detection). Your spoken response does not correlate to any audio frame's request id: it streams back as `artifactUpdate` events on the turn's task (see [A.4b Audio response chunk (your agent to Connect, voice, external AI agent with audio streaming)](#a2a-dg-sample-audio-response-chunk)).

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

## A.4 Text response chunk (your agent to Connect)
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

Continuations set `append: true`; the final chunk sets `lastChunk: true`. For audio output, see [A.4b Audio response chunk (your agent to Connect, voice, external AI agent with audio streaming)](#a2a-dg-sample-audio-response-chunk).

## A.4b Audio response chunk (your agent to Connect, voice, external AI agent with audio streaming)
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

## A.5 Terminal status update with FINISH (your agent to Connect)
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

## A.6 Task failure with structured error (your agent to Connect)
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

## A.6b Informational ERROR message (Connect to your agent)
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

## A.7 INTERRUPTION (either direction)
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

## A.8 DTMF\_INPUT\_COMPLETE (Connect to your agent)
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

## A.9 FRAGMENT (WebSocket only, either direction)
<a name="a2a-dg-sample-fragment"></a>

Connect Customer to external AI agent:

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

External AI agent to Connect Customer:

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

## A.10 TRACING\_SPAN (your agent to Connect)
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
                                    "scope": { "name": "example.billing-agent", "version": "1.0.0" },
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

## A.10b TRACING\_SPAN with per-segment latency (multiple spans in one trace)
<a name="a2a-dg-sample-tracing-multi-segment"></a>

A turn can emit multiple output segments (for example, one sentence at a time). To record the latency of each segment, put one span for each segment inside the same `otlp` envelope, not multiple `TRACING_SPAN` frames. Send exactly one `TRACING_SPAN` artifact per turn, and put every span for the turn in its `otlp.resourceSpans` batch. Each segment span carries its own `startTimeUnixNano`/`endTimeUnixNano` (segment latency = end minus start) and parents to the turn's `invoke_agent` root; give every span the turn's single `traceId`.

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
                                    "scope": { "name": "example.billing-agent", "version": "1.0.0" },
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

Three chat segment spans nest under the one `invoke_agent` root; their start and end deltas give per-segment latencies of 420 ms, 485 ms, and 405 ms. All spans share one `traceId` and ride in a single `TRACING_SPAN` artifact. Send exactly one `TRACING_SPAN` artifact per turn, and put every span for the turn in its `otlp.resourceSpans` batch.