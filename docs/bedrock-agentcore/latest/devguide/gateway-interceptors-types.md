# Types of interceptors

There are two types of interceptors that can be configured on your gateway:

## Request interceptors

The REQUEST interceptor gets invoked before gateway makes a call to the target configured on the gateway. You can use the REQUEST interceptor to perform any custom validations or authorizations.

### Request interceptor input payload example

The following example shows the input payload structure that a request interceptor Lambda function receives:

```
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

###### Note

The `headers` field is only included if `passRequestHeaders` is set to `true` in the interceptor configuration. The `gatewayResponse` field is not present for request interceptors since the response has not been generated yet.

### Request interceptor output payload example

The following example shows the output payload structure that a request interceptor Lambda function should return:

```
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

###### Important

Important notes about request interceptor output: \* The `interceptorOutputVersion` must be set to `"1.0"` . \* If the interceptor output contains a `transformedGatewayResponse` , the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided. \* If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse` , the RESPONSE interceptor will still be invoked.

## Response interceptors

The RESPONSE interceptor gets invoked before the gateway responds to the caller. You can use the RESPONSE interceptor to perform any custom redactions or additions to the response back to the caller.

### Response interceptor input payload example

The following example shows the input payload structure that a response interceptor Lambda function receives:

```
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

###### Note

The `headers` field in `gatewayRequest` is only included if `passRequestHeaders` is set to `true` in the interceptor configuration. Response interceptors receive both the original request and the gateway’s response, allowing you to modify the response before it’s returned to the caller.

### Response interceptor output payload example

The following example shows the output payload structure that a response interceptor Lambda function should return:

```
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

###### Important

Important notes about response interceptor output: \* The `interceptorOutputVersion` must be set to `"1.0"` . \* If the interceptor output contains a `transformedGatewayResponse` , the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided. \* If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse` , the RESPONSE interceptor will still be invoked.

## Response interceptors with streaming enabled

###### Note

If response streaming is enabled on your gateway, your response interceptor Lambda function must check the `isStreamingResponse` field in `gatewayResponse` to distinguish between streaming and non-streaming responses. For streaming responses, handle multiple invocations per request — one per eligible event — and note that only the first invocation can override `headers` and `statusCode`.

When [response streaming](gateway-mcp-streaming.md "gateway-mcp-streaming.md") is enabled on your gateway, the response interceptor behavior changes. The interceptor is invoked multiple times during a streaming response — once per eligible event — instead of once with the complete response.

### When the response interceptor is invoked

The response interceptor is invoked for events that contain a JSON-RPC `id` field:

- **First event** — The first JSON-RPC response or server-initiated request on the stream (e.g., the tool result, or an `elicitation/create` / `sampling/createMessage` request).
- **Subsequent events** — Any additional JSON-RPC responses or server-initiated requests (e.g., the final tool result after an elicitation is fulfilled).

The response interceptor is **not** invoked for:

- `notifications/progress` — Progress updates are forwarded directly to the client.
- `notifications/message` — Log messages are forwarded directly to the client.
- Pings — Keep-alive signals are forwarded directly to the client.

### Streaming response interceptor input payload

The input payload includes a new `isStreamingResponse` field set to `true`. The `gatewayResponse.body` field contains the current event body.

**First event** — The interceptor receives `headers`, `statusCode`, and `body`:

```
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

```
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

What the interceptor can override depends on whether it is the first or a subsequent event:

| Event                     | Can override                    | Ignored if returned                              |
| ------------------------- | ------------------------------- | ------------------------------------------------ |
| First event               | `headers`, `statusCode`, `body` | N/A                                              |
| Subsequent events         | `body` only                     | `headers`, `statusCode` (already sent to client) |
| Non-streaming (unchanged) | `headers`, `statusCode`, `body` | N/A                                              |
