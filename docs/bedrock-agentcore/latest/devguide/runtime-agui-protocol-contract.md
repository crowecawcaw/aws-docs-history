# AG-UI protocol contract

The AG-UI protocol contract defines the requirements for implementing agent-to-user interface communication in Amazon Bedrock AgentCore Runtime. This contract specifies the technical requirements, endpoints, and communication patterns that your AG-UI agent must implement.

For example code, see [Deploy AG-UI servers in AgentCore Runtime](runtime-agui.md "runtime-agui.md").

###### Topics

- [Protocol implementation requirements](#agui-protocol-implementation-requirements "#agui-protocol-implementation-requirements")
- [Container requirements](#agui-container-requirements "#agui-container-requirements")
- [Path requirements](#agui-path-requirements "#agui-path-requirements")
- [Authentication requirements](#agui-authentication-requirements "#agui-authentication-requirements")
- [Error handling](#agui-error-handling "#agui-error-handling")
- [OAuth authentication responses](#agui-oauth-authentication-responses "#agui-oauth-authentication-responses")

## Protocol implementation requirements

Your AG-UI agent must implement these specific protocol requirements:

- **Transport** : Server-Sent Events (SSE) or WebSocket - SSE provides unidirectional streaming from server to client, while WebSocket enables bidirectional real-time communication
- **Session Management** : Platform automatically adds `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` header for session isolation

## Container requirements

Your AG-UI agent must be deployed as a containerized application meeting these specifications:

- **Host** : `0.0.0.0`
- **Port** : `8080` - Standard port for AG-UI agent communication (same as HTTP protocol)
- **Platform** : ARM64 container - Required for compatibility with AWS Amazon Bedrock AgentCore runtime environment

## Path requirements

### /invocations - POST

#### Purpose

Receives user requests and streams responses as Server-Sent Events (SSE)

#### Use cases

The invocations endpoint serves several key purposes:

- Streaming chat responses
- Agent status and thinking steps
- Tool calls and results

#### Request format

Amazon Bedrock AgentCore passes request payloads directly to your container without validation. To be AG-UI-compliant, your requests should follow the `RunAgentInput` format. Your container implementation determines which fields are required and how validation errors are handled.

AG-UI-compliant agents expect a `RunAgentInput` JSON payload. Example:

```
{
  "threadId": "thread-123",
  "runId": "run-456",
  "messages": [{"id": "msg-1", "role": "user", "content": "Hello, agent!"}],
  "tools": [],
  "context": [],
  "state": {},
  "forwardedProps": {}
}
```

For the complete `RunAgentInput` schema and message format details, see [AG-UI Types](https://docs.ag-ui.com/sdk/js/core/types "https://docs.ag-ui.com/sdk/js/core/types").

#### Response format

AG-UI agents respond with SSE-formatted event streams:

```
Content-Type: text/event-stream

data: {"type":"RUN_STARTED","threadId":"thread-123","runId":"run-456"}

data: {"type":"TEXT_MESSAGE_START","messageId":"msg-789","role":"assistant"}

data: {"type":"TEXT_MESSAGE_CONTENT","messageId":"msg-789","delta":"Processing your request"}

data: {"type":"TOOL_CALL_START","toolCallId":"tool-001","toolCallName":"search","parentMessageId":"msg-789"}

data: {"type":"TOOL_CALL_RESULT","messageId":"msg-789","toolCallId":"tool-001","content":"Search completed"}

data: {"type":"TEXT_MESSAGE_END","messageId":"msg-789"}

data: {"type":"RUN_FINISHED","threadId":"thread-123","runId":"run-456"}
```

### /ws - WebSocket

#### Purpose

Provides bidirectional real-time communication between clients and agents

#### Use cases

The WebSocket endpoint serves several key purposes:

- Real-time conversational interfaces
- Interactive agent sessions with user interrupts
- Multi-turn conversations with persistent connections

### /ping - GET

#### Purpose

Verifies that your AG-UI agent is operational and ready to handle requests

#### Response format

Returns a status code indicating your agent’s health:

- **Content-Type** : `application/json`
- **HTTP Status Code** : `200` for healthy, appropriate error codes for unhealthy states

```
{
  "status": "Healthy",
  "time_of_last_update": 1640995200
}
```

## Authentication requirements

AG-UI agents support multiple authentication mechanisms:

### OAuth 2.0 Bearer Tokens

For AG-UI client authentication, include the Bearer token in request headers:

```
Authorization: Bearer <oauth-token>
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: <session-id>
```

### SigV4 Authentication

Standard AWS SigV4 authentication is also supported for programmatic access.

## Error handling

Errors are classified into two categories based on when they occur:

- **Connection-level errors** : Occur before the request reaches your container (authentication, validation, throttling). These return standard HTTP status codes.
- **Runtime errors** : Occur during agent execution after the stream has started. These surface as `RUN_ERROR` events in the SSE stream rather than HTTP status codes.

| AG-UI Error Code      | HTTP Status | Description                                                     |
| --------------------- | ----------- | --------------------------------------------------------------- |
| `UNAUTHORIZED`        | 401         | Authentication required or invalid credentials                  |
| `ACCESS_DENIED`       | 403         | Insufficient permissions for requested operation                |
| `VALIDATION_ERROR`    | 400         | Invalid request data or parameters                              |
| `RATE_LIMIT_EXCEEDED` | 429         | Too many requests from client                                   |
| `AGENT_ERROR`         | 200         | Agent code failed during execution – check your CloudWatch logs |

Example runtime error (agent failure):

```
HTTP/1.1 200 OK
Content-Type: text/event-stream
x-amzn-requestid: 8bg30e9c-7e26-6bge-dc4b-75h368cc10cf

data: {"type":"RUN_ERROR","code":"AGENT_ERROR","message":"Agent execution failed"}
```

## OAuth authentication responses

OAuth-configured agents return authentication errors with standard HTTP status codes. The response includes a `WWW-Authenticate` header (per [RFC 7235](https://datatracker.ietf.org/doc/html/rfc7235 "https://datatracker.ietf.org/doc/html/rfc7235") ) for OAuth discovery through the GetRuntimeProtectedResourceMetadata API.

Example OAuth authentication error:

```
HTTP/1.1 401 Unauthorized
Content-Type: text/event-stream
WWW-Authenticate: Bearer resource_metadata="https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{ESCAPED_ARN}/invocations/.well-known/oauth-protected-resource?qualifier={QUALIFIER}"
x-amzn-requestid: 8bg30e9c-7e26-6bge-dc4b-75h368cc10cf

data: {"type":"RUN_ERROR","code":"UNAUTHORIZED","message":"Authentication required"}
```

SigV4-configured agents return HTTP 403 with an `ACCESS_DENIED` error and do not include `WWW-Authenticate` headers.
