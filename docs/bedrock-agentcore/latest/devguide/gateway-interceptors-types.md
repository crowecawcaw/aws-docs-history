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

Important notes about request interceptor output:

- The `interceptorOutputVersion` must be set to `"1.0"`.
- If the interceptor output contains a `transformedGatewayResponse`, the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided.
- If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse`, the RESPONSE interceptor will still be invoked.

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

The `headers` field in `gatewayRequest` is only included if `passRequestHeaders` is set to `true` in the interceptor configuration. Response interceptors receive both the original request and the gateway's response, allowing you to modify the response before it's returned to the caller.

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

Important notes about response interceptor output:

- The `interceptorOutputVersion` must be set to `"1.0"`.
- If the interceptor output contains a `transformedGatewayResponse`, the gateway will respond with that content immediately, even if `transformedGatewayRequest` is also provided.
- If both REQUEST and RESPONSE interceptors are configured and the REQUEST interceptor output contains a `transformedGatewayResponse`, the RESPONSE interceptor will still be invoked.
