# A2A protocol contract

The A2A protocol contract defines the requirements for implementing agent-to-agent
communication in Amazon Bedrock AgentCore Runtime. This contract specifies the technical requirements,
endpoints, and communication patterns that your A2A server must implement.

For example code, see [Deploy A2A servers in AgentCore Runtime](runtime-a2a.md "runtime-a2a.md").

###### Topics

- [Protocol implementation
  requirements](#protocol-implementation-requirements "#protocol-implementation-requirements")
- [Container requirements](#container-requirements "#container-requirements")
- [Path requirements](#path-requirements "#path-requirements")
- [Authentication requirements](#authentication-requirements "#authentication-requirements")
- [Error handling](#error-handling "#error-handling")

## Protocol implementation

requirements

Your A2A server must implement these specific protocol requirements:

- **Transport**: [JSON-RPC 2.0](https://www.jsonrpc.org/specification "https://www.jsonrpc.org/specification") over HTTP -
  Enables standardized agent-to-agent communication
- **Session Management**: Platform
  automatically adds `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id`
  header for session isolation
- **Agent Discovery**: Must provide Agent Card
  at `/.well-known/agent-card.json` endpoint

## Container requirements

Your A2A server must be deployed as a containerized application meeting these
specifications:

- **Host**: `0.0.0.0`
- **Port**: `9000` - Standard port
  for A2A server communication (different from HTTP and MCP protocols)
- **Platform**: ARM64 container - Required for
  compatibility with AWS Amazon Bedrock AgentCore runtime environment

## Path requirements

### / - POST

#### Purpose

Receives JSON-RPC 2.0 messages and processes them through your agent's
capabilities, complete pass-through of [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md") API payload with A2A protocol
messages

#### Use cases

The root endpoint serves several key purposes:

- Agent-to-agent communication and collaboration
- Multi-step agent workflows and task delegation
- Real-time conversational experiences between agents
- Tool invocation and capability sharing

#### Request format

A2A servers expect JSON-RPC 2.0 formatted requests:

```
Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [
        {
          "kind": "text",
          "text": "Your message content here"
        }
      ],
      "messageId": "unique-message-id"
    }
  }
}
```

#### Response format

A2A servers respond with JSON-RPC 2.0 formatted responses containing tasks
and artifacts:

```
Content-Type: application/json
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "result": {
    "artifacts": [
      {
        "artifactId": "unique-artifact-id",
        "name": "agent_response",
        "parts": [
          {
            "kind": "text",
            "text": "Agent response content"
          }
        ]
      }
    ]
  }
}
```

### /.well-known/agent-card.json - GET

#### Purpose

Provides Agent Card metadata for agent discovery and capability
advertisement

#### Use cases

The Agent Card endpoint serves several key purposes:

- Agent discovery in multi-agent systems
- Capability and skill advertisement
- Authentication requirement specification
- Service endpoint configuration

#### Response format

Returns JSON metadata describing the agent's identity and
capabilities:

```
Content-Type: application/json
{
  "name": "Agent Name",
  "description": "Agent description and purpose",
  "version": "1.0.0",
  "url": "https://bedrock-agentcore.region.amazonaws.com/runtimes/agent-arn/invocations/",
  "protocolVersion": "0.3.0",
  "preferredTransport": "JSONRPC",
  "capabilities": {
    "streaming": true
  },
  "defaultInputModes": ["text"],
  "defaultOutputModes": ["text"],
  "skills": [
    {
      "id": "skill-id",
      "name": "Skill Name",
      "description": "Skill description and capabilities",
      "tags": []
    }
  ]
}
```

### /ping - GET

#### Purpose

Verifies that your A2A server is operational and ready to handle
requests

#### Response format

Returns a status code indicating your agent's health:

- **Content-Type**:
  `application/json`
- **HTTP Status Code**:
  `200` for healthy, appropriate error codes for
  unhealthy states

```
{
  "status": "Healthy",
  "time_of_last_update": 1640995200
}
```

## Authentication requirements

A2A servers support multiple authentication mechanisms:

### OAuth 2.0 Bearer Tokens

For A2A client authentication, include the Bearer token in request
headers:

```
Authorization: Bearer <oauth-token>
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: <session-id>
```

### SigV4 Authentication

Standard AWS SigV4 authentication is also supported for programmatic
access.

## Error handling

A2A servers return errors as standard JSON-RPC 2.0 error responses with HTTP 200
status codes to maintain protocol compliance:

| A2A Error Codes | JSON-RPC Error Code       | Runtime Exception | HTTP Error Code                                                                     | JSON-RPC Error Message |
| --------------- | ------------------------- | ----------------- | ----------------------------------------------------------------------------------- | ---------------------- |
| -32501          | ResourceNotFoundException | 404               | Resource not found<br>• Requested resource does not exist                           |
| -32052          | ValidationException       | 400               | Validation error<br>• Invalid request data                                          |
| -32053          | ThrottlingException       | 429               | Rate limit exceeded<br>• Too many requests                                          |
| -32054          | ResourceConflictException | 409               | Resource conflict<br>• Resource already exists                                      |
| -32055          | RuntimeClientError        | 424               | Runtime client error<br>• Please check your CloudWatch logs for more<br>information |

Example error response:

```
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "error": {
    "code": -32052,
    "message": "Validation error - Invalid request data"
  }
}
```
