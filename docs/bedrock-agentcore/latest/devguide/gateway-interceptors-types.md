

# Types of interceptors

There are two types of interceptors that you can configure on your gateway: REQUEST interceptors and RESPONSE interceptors. The interceptor payload structure depends on the target type configured on your gateway.

This topic covers the interceptor contracts for both MCP targets and HTTP targets (such as Amazon Bedrock AgentCore Runtime).

## Request interceptors
<a name="gateway-interceptors-types-request"></a>

The REQUEST interceptor gets invoked before gateway makes a call to the target configured on the gateway. You can use the REQUEST interceptor to perform any custom validations or authorizations.

### Request interceptor input payload example
<a name="gateway-interceptors-types-request-payload"></a>

The following example shows the input payload structure that a request interceptor Lambda function receives:

```json
{
  "interceptorInputVersion": "1.0",
  "mcp": {
    "rawGatewayRequest": {
        "body": "<raw_request_body>"
    },
    "gatewayRequest" : {
        "path": "/mcp",
        "httpMethod": "POST",
        "headers": {
            "Accept": "application/json",
            "Authorization": "<bearer_token>",
            "SomeHeader": "headerValue1",
            "Mcp-Session-Id": "<session_id>",
            "User-Agent": "<client_user_agent>"
        },
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
    }
  }
}
```

**Note**  
The `headers` field is only included if `passRequestHeaders` is set to `true` in the interceptor configuration. The `gatewayResponse` field is not present for request interceptors since the response has not been generated yet.

### Request interceptor output payload example
<a name="gateway-interceptors-types-request-output"></a>

The following example shows the output payload structure that a request interceptor Lambda function should return:

```json
{
  "interceptorOutputVersion": "1.0",
  "mcp": {
    "transformedGatewayRequest" : {
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
    },
    "transformedGatewayResponse" : {
        "statusCode": 200,
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "<result_content>": "<result_value>"
            }
        }
    }
  }
}
```

**Important**  
Important notes about request interceptor output: \* The `interceptorOutputVersion` must be set to `"1.0"` . \* If the interceptor output contains a `transformedGatewayResponse` , the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided. \* If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse` , the RESPONSE interceptor will still be invoked.

## Response interceptors
<a name="gateway-interceptors-types-response"></a>

The RESPONSE interceptor gets invoked before the gateway responds to the caller. You can use the RESPONSE interceptor to perform any custom redactions or additions to the response back to the caller.

### Response interceptor input payload example
<a name="gateway-interceptors-types-response-payload"></a>

The following example shows the input payload structure that a response interceptor Lambda function receives:

```json
{
  "interceptorInputVersion": "1.0",
  "mcp": {
    "rawGatewayRequest": {
        "body": "<raw_request_body>"
    },
    "gatewayRequest" : {
        "path": "/mcp",
        "httpMethod": "POST",
        "headers": {
            "Accept": "application/json",
            "Authorization": "<bearer_token>",
            "SomeHeader": "headerValue1",
            "Mcp-Session-Id": "<session_id>",
            "User-Agent": "<client_user_agent>"
        },
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
    },
    "gatewayResponse" : {
        "statusCode": 200,
        "headers": {
            "SomeHeader": "headerValue1",
            "Mcp-Session-Id": "<session_id>"
        },
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "tools": []
            }
        }
    }
  }
}
```

**Note**  
The `headers` field in `gatewayRequest` is only included if `passRequestHeaders` is set to `true` in the interceptor configuration. Response interceptors receive both the original request and the gateway’s response, allowing you to modify the response before it’s returned to the caller.

### Response interceptor output payload example
<a name="gateway-interceptors-types-response-output"></a>

The following example shows the output payload structure that a response interceptor Lambda function should return:

```json
{
  "interceptorOutputVersion": "1.0",
  "mcp": {
    "transformedGatewayRequest" : {
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
    },
    "transformedGatewayResponse" : {
        "statusCode": 200,
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "<result_content>": "<result_value>"
            }
        }
    }
  }
}
```

**Important**  
Important notes about response interceptor output: \* The `interceptorOutputVersion` must be set to `"1.0"` . \* If the interceptor output contains a `transformedGatewayResponse` , the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided. \* If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse` , the RESPONSE interceptor will still be invoked.

## Response interceptors with streaming enabled
<a name="gateway-interceptors-types-streaming"></a>

**Note**  
If response streaming is enabled on your gateway, your response interceptor Lambda function must check the `isStreamingResponse` field in `gatewayResponse` to distinguish between streaming and non-streaming responses. For streaming responses, handle multiple invocations per request — one per eligible event — and note that only the first invocation can override `headers` and `statusCode`.

When [response streaming](gateway-mcp-streaming.md) is enabled on your gateway, the response interceptor behavior changes. The interceptor is invoked multiple times during a streaming response — once per eligible event — instead of once with the complete response.

**Note**  
This section applies to MCP targets only. You turn on MCP response streaming with `protocolConfiguration.mcp.streamingConfiguration.enableResponseStreaming`, which decides whether the gateway streams MCP responses to the client. For more information, see [Enable response streaming](gateway-mcp-streaming.md#gateway-mcp-streaming-enable).  
For HTTP and inference targets, this setting has no effect. To have the response interceptor process a streamed response in batches of events, set `responseInterceptionMode` to `STREAM` in the interceptor configuration. For more information, see [Stream responses through the response interceptor](#gateway-interceptors-types-http-stream).

### When the response interceptor is invoked
<a name="gateway-interceptors-types-streaming-when"></a>

The response interceptor is invoked for events that contain a JSON-RPC `id` field:
+  **First event** — The first JSON-RPC response or server-initiated request on the stream (e.g., the tool result, or an `elicitation/create` / `sampling/createMessage` request).
+  **Subsequent events** — Any additional JSON-RPC responses or server-initiated requests (e.g., the final tool result after an elicitation is fulfilled).

The response interceptor is **not** invoked for:
+  `notifications/progress` — Progress updates are forwarded directly to the client.
+  `notifications/message` — Log messages are forwarded directly to the client.
+ Pings — Keep-alive signals are forwarded directly to the client.

### Streaming response interceptor input payload
<a name="gateway-interceptors-types-streaming-input"></a>

The input payload includes a new `isStreamingResponse` field set to `true`. The `gatewayResponse.body` field contains the current event body.

 **First event** — The interceptor receives `headers`, `statusCode`, and `body`:

```json
{
  "interceptorInputVersion": "1.0",
  "mcp": {
    "rawGatewayRequest": {
        "body": "<raw_request_body>"
    },
    "gatewayRequest" : {
        "path": "/mcp",
        "httpMethod": "POST",
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "myTool",
                "arguments": {}
            }
        }
    },
    "gatewayResponse" : {
        "statusCode": 200,
        "headers": {
            "Mcp-Session-Id": "<session_id>"
        },
        "isStreamingResponse": true,
        "body": {
            "jsonrpc": "2.0",
            "id": "elicit-1",
            "method": "elicitation/create",
            "params": {
                "message": "Confirm this action?",
                "requestedSchema": {}
            }
        }
    }
  }
}
```

 **Subsequent events** — The interceptor receives only `body` (headers and status code have already been sent to the client):

```json
{
  "interceptorInputVersion": "1.0",
  "mcp": {
    "rawGatewayRequest": {
        "body": "<raw_request_body>"
    },
    "gatewayRequest" : {
        "path": "/mcp",
        "httpMethod": "POST",
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "myTool",
                "arguments": {}
            }
        }
    },
    "gatewayResponse" : {
        "isStreamingResponse": true,
        "body": {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "content": [{"type": "text", "text": "Tool result"}]
            }
        }
    }
  }
}
```

### Streaming response interceptor output payload
<a name="gateway-interceptors-types-streaming-output"></a>

What the interceptor can override depends on whether it is the first or a subsequent event:


| Event | Can override | Ignored if returned | 
| --- | --- | --- | 
| First event |  `headers`, `statusCode`, `body`  | N/A | 
| Subsequent events |  `body` only |  `headers`, `statusCode` (already sent to client) | 
| Non-streaming (unchanged) |  `headers`, `statusCode`, `body`  | N/A | 

## Interceptors for HTTP targets
<a name="gateway-interceptors-types-http"></a>

HTTP targets use a different interceptor payload structure than MCP targets. HTTP targets (AgentCore Runtime and passthrough) and inference targets all use this `http` payload structure. Inference is a separate target type that happens to share the HTTP interceptor payload shape. The payload uses an `http` key instead of an `mcp` key. Request and response bodies are base64-encoded strings rather than parsed JSON objects.

HTTP targets support both REQUEST and RESPONSE interceptors. A RESPONSE interceptor runs in one of two modes, which you choose with `responseInterceptionMode` in the interceptor configuration:
+  `BUFFERED` (default) – The gateway buffers the full response before invoking the response interceptor once.
+  `STREAM` – For streaming responses (Server-Sent Events or AWS event stream), the gateway invokes the response interceptor for each batch of events and sends each batch to the client after your Lambda function returns. Other responses are buffered. For more information, see [Stream responses through the response interceptor](#gateway-interceptors-types-http-stream).

The following list summarizes the key behaviors for HTTP target interceptors:
+ The `httpMethod` field is read-only.
+ The request and response `body` fields are base64-encoded strings.
+ The `headers` field is included in the request payload only when `passRequestHeaders` is set to `true` in the interceptor configuration.
+ If a REQUEST interceptor’s output contains `transformedGatewayResponse`, the gateway short-circuits the request. It skips policy engine evaluation and the target call. It uses that response instead. If you configure both REQUEST and RESPONSE interceptors, the gateway still invokes the RESPONSE interceptor and passes it the short-circuit response.

### Request interceptor input payload example
<a name="gateway-interceptors-types-http-request-input"></a>

The following JSON example shows the structure of the input payload that your request interceptor Lambda function receives when processing an HTTP target request:

```json
{
  "interceptorInputVersion": "1.0",
  "http": {
    "gatewayRequest": {
      "path": "/my-target-name/invocations",
      "httpMethod": "POST",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "<bearer_token>"
      },
      "body": "<base64_encoded_body>"
    }
  }
}
```

**Note**  
Note the following about the input payload:
+ The `headers` field is included only if `passRequestHeaders` is set to `true` in the interceptor configuration.
+ The `body` field is a base64-encoded string that represents the raw HTTP request body.
+ The `httpMethod` field is included for informational purposes but is read-only. The interceptor cannot change it.

### Request interceptor output payload example
<a name="gateway-interceptors-types-http-request-output"></a>

The following JSON example shows the structure of the output payload that your request interceptor Lambda function must return when transforming an HTTP target request:

```json
{
  "interceptorOutputVersion": "1.0",
  "http": {
    "transformedGatewayRequest": {
      "headers": {
        "Content-Type": "application/json",
        "X-Custom-Header": "custom-value"
      },
      "body": "<base64_encoded_body>"
    },
    "transformedGatewayResponse": {
      "contentType": "application/json",
      "statusCode": 200,
      "headers": {
        "X-Custom-Header": "custom-value"
      },
      "body": "<base64_encoded_body>"
    }
  }
}
```

**Important**  
Important notes about HTTP request interceptor output:  
The `interceptorOutputVersion` must be set to `"1.0"`.
If the output contains a `transformedGatewayResponse`, the gateway skips policy engine evaluation and the target call, and uses that response instead. If you also configure a RESPONSE interceptor, the gateway still invokes it.
The `body` field must be a base64-encoded string.
The `httpMethod` is not included in the output because it cannot be modified.

### Response interceptor input payload example
<a name="gateway-interceptors-types-http-response-input"></a>

When you configure a RESPONSE interceptor for an HTTP target, the gateway buffers the target response and passes it to your Lambda function. The following JSON example shows the structure of the input payload:

```json
{
  "interceptorInputVersion": "1.0",
  "http": {
    "gatewayRequest": {
      "path": "/my-target-name/invocations",
      "httpMethod": "POST",
      "body": "<base64_encoded_body>"
    },
    "gatewayResponse": {
      "statusCode": 200,
      "headers": {
        "Content-Type": "application/json"
      },
      "isStreamingResponse": false,
      "body": "<base64_encoded_body>",
      "contentType": "application/json"
    }
  }
}
```

**Note**  
Note the following about the response input payload:
+ The `body` field is a base64-encoded string that represents the raw HTTP response body.
+ The `body` field is `null` if you exclude the response body with a payload filter, which you can do only in `BUFFERED` mode. For more information, see [Handle large response payloads](#gateway-interceptors-types-http-large).
+ The `headers` field contains the target’s response headers.
+ The `gatewayRequest` field contains the request that the gateway sent to the target, for HTTP and inference targets.
+ The `isStreamingResponse` field is `false` for a buffered response. In `STREAM` mode, a streamed batch has `isStreamingResponse` set to `true`. For more information, see [Stream responses through the response interceptor](#gateway-interceptors-types-http-stream).

### Response interceptor output payload example
<a name="gateway-interceptors-types-http-response-output"></a>

The following JSON example shows the structure of the output payload that your response interceptor Lambda function returns when transforming an HTTP target response:

```json
{
  "interceptorOutputVersion": "1.0",
  "http": {
    "transformedGatewayResponse": {
      "statusCode": 200,
      "headers": {
        "X-Custom-Header": "custom-value"
      },
      "body": "<base64_encoded_body>",
      "contentType": "application/json"
    }
  }
}
```

**Important**  
Important notes about HTTP response interceptor output:  
The `interceptorOutputVersion` must be set to `"1.0"`.
The `statusCode`, `body`, and `contentType` fields each override the original response value. If you omit a field (or set it to `null`), the gateway uses the original value.
The `body` field must be a base64-encoded string.
To pass the response through unchanged, return an empty `http` object: `{"interceptorOutputVersion": "1.0", "http": {}}`.

### Stream responses through the response interceptor
<a name="gateway-interceptors-types-http-stream"></a>

By default, a RESPONSE interceptor on an HTTP or inference target receives the whole response after the target finishes. For a streaming response, the client then gets no text until the model finishes. In `STREAM` mode, the gateway invokes your Lambda function for each batch of events, and the client gets each batch as soon as your function returns it.

**Important**  
 `STREAM` mode applies only to streaming responses (Server-Sent Events and AWS event streams). For any other response, your function gets the whole response at once, the same as in `BUFFERED` mode. Check `isStreamingResponse` and handle both cases. For an example, see [Interceptor examples](gateway-interceptors-examples.md).

#### Configure STREAM mode
<a name="gateway-interceptors-types-http-stream-config"></a>

Set `responseInterceptionMode` to `STREAM` and `maxEventsPerInvocation` in the interceptor configuration:

```json
{
  "interceptor": {
    "lambda": {
      "arn": "arn:aws:lambda:us-west-2:123456789012:function:my-response-interceptor"
    }
  },
  "interceptionPoints": ["RESPONSE"],
  "responseInterceptionMode": "STREAM",
  "responseStreamingConfiguration": {
    "maxEventsPerInvocation": 10
  }
}
```
+  `responseInterceptionMode` – `BUFFERED` (default) or `STREAM`. Allowed only when `interceptionPoints` includes `RESPONSE`. With `STREAM`, only Server-Sent Events (`text/event-stream`) and AWS event stream (`application/vnd.amazon.eventstream`) responses are streamed. All other responses, such as a JSON response to a non-streaming request, are buffered and passed to your function once, as in `BUFFERED` mode.
+  `responseStreamingConfiguration.maxEventsPerInvocation` – The maximum number of events in one Lambda invocation. Required with `STREAM`, and at least 1. A smaller value sends text to the client sooner and invokes your function more often. For example, with a value of 10, a 1,000-word answer takes about 50 to 170 invocations, depending on the model.

**Note**  
 `responseInterceptionMode` and `protocolConfiguration.mcp.streamingConfiguration.enableResponseStreaming` are separate settings:  
 `enableResponseStreaming` applies only to MCP targets. It decides whether the gateway streams MCP responses to the client at all, because an MCP server responds with or without streaming depending on this setting. For MCP targets, see [Enable response streaming](gateway-mcp-streaming.md#gateway-mcp-streaming-enable) and [Response interceptors with streaming enabled](#gateway-interceptors-types-streaming).
 `responseInterceptionMode` applies only to HTTP and inference targets. These targets already stream to the client when the client asks for it, for example with `"stream": true`. `STREAM` mode only controls how your response interceptor receives that streamed response: in batches of events instead of once after the response finishes.

#### Streamed input payload
<a name="gateway-interceptors-types-http-stream-input"></a>

Each invocation carries one batch of events. The following example is a batch from an Anthropic Messages API stream (Server-Sent Events):

```json
{
  "interceptorInputVersion": "1.0",
  "http": {
    "gatewayRequest": {
      "path": "/v1/messages",
      "httpMethod": "POST",
      "body": "<base64_encoded_body>"
    },
    "gatewayResponse": {
      "statusCode": 200,
      "headers": {
        "Content-Type": "text/event-stream"
      },
      "contentType": "text/event-stream",
      "isStreamingResponse": true,
      "events": [
        {
          "event": "content_block_delta",
          "data": {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "my SSN is 123-"}}
        },
        {
          "event": "content_block_delta",
          "data": {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "45-6789"}}
        }
      ]
    }
  }
}
```

For an AWS event stream, such as Amazon Bedrock `InvokeModelWithResponseStream`, the same batch looks like this. The gateway decodes the binary message and its base64 `bytes` field, so your function reads JSON:

```json
"gatewayResponse": {
  "statusCode": 200,
  "contentType": "application/vnd.amazon.eventstream",
  "isStreamingResponse": true,
  "events": [
    {
      "event": "chunk",
      "data": {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "my SSN is 123-"}}
    }
  ]
}
```

**Note**  
 `isStreamingResponse` is `true` on every streamed invocation, and `body` isn’t set.
 `events` lists the events of the batch, in order, as the target sent them. For Server-Sent Events, `event` is the event name and is absent when the event has no name. For an AWS event stream, `event` is the `:event-type` header, for example `chunk`.
 `data` is the event’s JSON. It is usually an object, but a target can send any JSON value, such as a string or a number. Check its type before you read fields from it.
The gateway doesn’t change the provider’s JSON. For example, the text is in `choices[0].delta.content` for an OpenAI Chat Completions stream and in `delta.text` for an Anthropic Messages stream.
 `statusCode`, `contentType`, and `headers` are the target’s values, the same in every invocation of one response. Read `contentType` to tell Server-Sent Events from an AWS event stream.
 `gatewayRequest` is included in every invocation. There is no ID that links the invocations of one response.

#### Streamed output payload
<a name="gateway-interceptors-types-http-stream-output"></a>

Return one event for each input event, in the same order. Entry *i* replaces the `data` of input event *i*:

```json
{
  "interceptorOutputVersion": "1.0",
  "http": {
    "transformedGatewayResponse": {
      "events": [
        {"data": {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "my SSN is "}}},
        {"data": {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "***"}}}
      ]
    }
  }
}
```

Note the following about streamed output:
+ You can change only `data`. You can’t change the event name (`event`): if you return one, the client still receives the original.
+ To keep an event unchanged, return its original `data`. An entry without `data` replaces the event’s content with `{}`.
+ To leave all the events in this invocation unchanged, return an empty `http` object, or omit `events`.

**Important**  
 `events` must have exactly one entry for each input event. You can’t add or remove single events, but you can drop the whole batch by returning `"events": []`.
If `isStreamingResponse` is `true`, return your changes in `events`, not `body`.
Text can be split across events and across batches of events. If you redact or filter content, check the joined text of neighboring events, and redact a partial match at the end of a batch.

#### How events are batched
<a name="gateway-interceptors-types-http-stream-batches"></a>

The gateway sends a batch of events to your function when any of the following happens:
+ The batch has `maxEventsPerInvocation` events.
+ The next event would make the input to your function more than 6 MB, the Lambda payload limit. The input also contains the original request, so a large request leaves less room for events.
+ The gateway adds an event named `error` (Server-Sent Events) to the batch. The gateway doesn’t wait for more events, so your function gets the error event as soon as it arrives.
+ The target ends the stream.

The following events go to the client without invoking your function, in their original order:
+ Server-Sent Events comments and keep-alives, events with no `data`, and events whose `data` isn’t a JSON value, such as `data: [DONE]`.
+  AWS event stream messages whose `:message-type` is `exception` or `error`.

#### Status code and headers
<a name="gateway-interceptors-types-http-stream-first-batch"></a>

The client receives the status code and headers once, with the first batch of events. So only your function’s first invocation can change them:
+ From the first invocation, the gateway applies the `statusCode`, `contentType`, and `headers` that your function returns. Only headers in the target’s `allowedResponseHeaders` are applied. For more information, see [Target-level header configuration](gateway-headers.md#gateway-headers-target-level).
+ If the first invocation returns a 4xx or 5xx `statusCode`:
  + For an inference target, the client receives only that error. The gateway doesn’t send the stream.
  + For an HTTP target, the client receives that status code, followed by the stream.
+ From later invocations, the gateway applies only `events`. It ignores `statusCode`, `contentType`, and `headers`, because the client already has them. When a later value differs from the one sent, the gateway writes a log entry for you. To block content in a later batch, change or drop its events.

#### Errors and timeouts
<a name="gateway-interceptors-types-http-stream-errors"></a>

An invocation fails if any of the following happens:
+ Your function returns an error or times out. Each invocation times out after 30 seconds.
+ Your function’s input or output is more than 6 MB, for example because a single event doesn’t fit.
+ Your function returns a malformed result: `events` doesn’t have one entry for each input event, an event has a field other than `data` and `event`, or the response has `body` for a batch of events.

What the client gets depends on when the failure happens:
+  **Before the first batch** – The client gets an HTTP error response, as in `BUFFERED` mode.
+  **After the first batch** – The client already has a `200` status. The gateway stops the target and ends the stream. For an inference target, the stream ends with an error event in the request’s API format, for example a `modelStreamErrorException` on an AWS event stream. For an HTTP target, the response ends early.

After the first batch, the client’s status code doesn’t show the failure, so the gateway writes a log entry for you that names the error type, without its message. For example:

```
Streamed response failed after the status was sent: the response interceptor failed (InvalidLambdaResponseException). The stream was ended with an error.
```

To receive these log entries, configure a log destination for the gateway. For more information, see [Provided log data](observability-gateway-metrics.md#observability-gateway-logs-provided).

#### Other considerations
<a name="gateway-interceptors-types-http-stream-notes"></a>
+  **Metering** – Gateway charges count the bytes that the client receives, after your function’s changes.

### Handle large response payloads
<a name="gateway-interceptors-types-http-large"></a>

Lambda synchronous invocation has a 6 MB payload limit for the request and response combined. If a target returns a large body — which is common with inference models — the base64-encoded payload can exceed this limit and cause an error.

To avoid this, exclude the response body from the interceptor input by configuring a payload filter that excludes the `RESPONSE_BODY` field. Your interceptor can still inspect the `statusCode`, `contentType`, and `headers`, and can inject headers or override the status code. When the response body is excluded, the `body` field in the input payload is `null`, and if your function returns `body: null`, the gateway uses the original (unmodified) response body.

For a streaming response (Server-Sent Events or AWS event stream), use `STREAM` mode instead. The 6 MB limit then applies to each batch of events, not to the whole response, so your function can read and change the response content. In `STREAM` mode, you can’t exclude the response body with a payload filter. For more information, see [Stream responses through the response interceptor](#gateway-interceptors-types-http-stream).

### Client context
<a name="gateway-interceptors-types-http-context"></a>

For HTTP targets, the gateway passes request metadata to your Lambda function through the invocation’s client context. Your function can read the following custom values: `GATEWAY_ARN`, `GATEWAY_ACCOUNT_ID`, `REQUEST_ID`, and `SOURCE_IP`. The `GATEWAY_ARN`, `GATEWAY_ACCOUNT_ID`, and `REQUEST_ID` values are always present. The `SOURCE_IP` value is included only when a source IP is available, so your function should treat it as optional.

### Key differences between MCP and HTTP interceptor payloads
<a name="gateway-interceptors-types-http-differences"></a>

The following table summarizes the differences between MCP and HTTP target interceptor payloads.


| Field | MCP target | HTTP target | 
| --- | --- | --- | 
| Body format | Map<String, Object> (parsed JSON) | String (base64-encoded) | 
| Path | Always "/mcp" | Actual HTTP path (for example, "/my-target-name/invocations") | 
| httpMethod | Immutable | Immutable | 
| rawGatewayRequest | Included | Not included | 
| Response interceptor | Supported (per event when MCP response streaming is turned on) | Supported, `BUFFERED` or `STREAM` mode | 