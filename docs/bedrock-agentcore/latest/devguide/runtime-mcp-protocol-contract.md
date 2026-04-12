# MCP protocol contract

Understand the requirements for implementing the Model Context Protocol (MCP) so that agents can call tools and agent servers.

For example code, see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md "runtime-mcp.md").

###### Topics

- [Protocol implementation requirements](#protocol-implementation-requirements "#protocol-implementation-requirements")
- [Container requirements](#container-requirements-mcp "#container-requirements-mcp")
- [Path requirements](#path-requirements-mcp "#path-requirements-mcp")
- [OAuth Authentication Responses](#mcp-oauth-authentication-responses "#mcp-oauth-authentication-responses")

## Protocol implementation requirements

Your MCP server must implement these specific protocol requirements:

- **Transport** : Streamable-http transport is required. By default, use stateless mode ( `stateless_http=True` ) for compatibility with AWS's session management and load balancing.
- **Session Management** : Platform automatically adds `Mcp-Session-Id` header for session isolation. In stateless mode, servers must support stateless operation so as to not reject platform generated `Mcp-Session-Id` header.

###### Tip

Amazon Bedrock AgentCore also supports stateful MCP servers ( `stateless_http=False` ) that enable capabilities such as elicitation (multi-turn user interactions) and sampling (LLM-generated content). Stateful mode is required when your MCP server needs to maintain session context across multiple requests within the same tool invocation. For more information and examples, see [Stateful MCP server features](mcp-stateful-features.md "mcp-stateful-features.md").

### MCP session management and microVM stickiness

The Model Context Protocol (MCP) uses the `Mcp-Session-Id` header to manage session state and route requests. For the MCP specification, see [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http "https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http").

**MicroVM Stickiness** : Amazon Bedrock AgentCore uses the `Mcp-Session-Id` header to route requests to the same microVM instance. Clients must capture the `Mcp-Session-Id` returned in the response and include it in all subsequent requests to ensure session affinity. Without a consistent session ID, each request may be routed to a new microVM, which may result in additional latency due to cold starts.

**Stateless MCP** ( `stateless_http=True` ):

- Platform generates the `Mcp-Session-Id` and includes it in the request to your MCP server.
- Your MCP server must accept the platform-provided session ID (do not reject it).
- Platform returns the same `Mcp-Session-Id` to the client in the response.
- Client must include this session ID in all subsequent requests for microVM affinity.

**Stateful MCP** ( `stateless_http=False` ):

- Client sends the initialize request without an `Mcp-Session-Id` header.
- Platform returns `Mcp-Session-Id` in the response.
- Client must include this `Mcp-Session-Id` in all subsequent requests for both session state and microVM affinity.

For more details on stateful MCP session management, see the [MCP session management specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#session-management "https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#session-management").

###### Note

In both modes, Amazon Bedrock AgentCore always returns an `Mcp-Session-Id` header to clients. Always capture and reuse this header for optimal performance.

## Container requirements

Your MCP server must be deployed as a containerized application meeting these specifications:

- **Host** : `0.0.0.0`
- **Port** : `8000` - Standard port for MCP server communication (different from HTTP protocol)
- **Platform** : ARM64 container - Required for compatibility with AWS Amazon Bedrock AgentCore runtime environment

## Path requirements

### /mcp - POST

**Purpose**

Receives MCP RPC messages and processes them through your agent’s tool capabilities, complete pass-through of [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md") API payload with standard MCP RPC messages

**Response format**

JSON-RPC based request/response format, supporting both `application/json` and `text/event-stream` as response content-types

**Use cases**

The `/mcp` endpoint serves several key purposes:

- Tool invocation and management
- Agent capability discovery
- Resource access and manipulation
- Multi-step agent workflows

## OAuth Authentication Responses

OAuth-configured agents follow [RFC 6749 (OAuth 2.0)](https://datatracker.ietf.org/doc/html/rfc6749 "https://datatracker.ietf.org/doc/html/rfc6749") authentication standards. When authentication is missing, the service returns a 401 Unauthorized response with a WWW-Authenticate header (per [RFC 7235](https://datatracker.ietf.org/doc/html/rfc7235 "https://datatracker.ietf.org/doc/html/rfc7235") ), enabling clients to discover the authorization server endpoints through the GetRuntimeProtectedResourceMetadata API.

### 401 Unauthorized

Returned when the Authorization header is missing or empty.

Response includes WWW-Authenticate header:

```
WWW-Authenticate: Bearer resource_metadata="https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{ESCAPED_ARN}/invocations/.well-known/oauth-protected-resource?qualifier={QUALIFIER}"
```

###### Note

SigV4-configured agents return HTTP 403 with an `ACCESS_DENIED` error and do not include `WWW-Authenticate` headers.
