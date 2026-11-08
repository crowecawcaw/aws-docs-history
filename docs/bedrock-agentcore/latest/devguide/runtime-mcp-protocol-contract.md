

# MCP protocol contract
<a name="runtime-mcp-protocol-contract"></a>

Understand the requirements for implementing the Model Context Protocol (MCP) in Amazon Bedrock AgentCore Runtime so that agents can call tools and agent servers. These requirements apply to MCP servers on both compute types, microVMs and [Instances](runtime-instances-how-it-works.md).

For example code, see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md).

**Topics**
+ [Protocol implementation requirements](#protocol-implementation-requirements)
+ [Server requirements](#container-requirements-mcp)
+ [Path requirements](#path-requirements-mcp)
+ [Health probes](#mcp-health-probes)
+ [Error handling](#mcp-error-handling)
+ [OAuth authentication responses](#mcp-oauth-authentication-responses)

## Protocol implementation requirements
<a name="protocol-implementation-requirements"></a>

Your MCP server must implement these specific protocol requirements:
+  **Transport** : Use the Streamable HTTP transport. For version `2025-11-25` and earlier, use stateless mode ( `stateless_http=True` ) by default for compatibility with AWS's session management and load balancing. Version `2026-07-28` and later is stateless by the MCP specification.
+  **Session Management** : The platform forwards session headers, including `Mcp-Session-Id` and `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id`, to your MCP server. Your MCP server must accept these headers and not reject requests that include them.

**Tip**  
AgentCore Runtime also supports stateful MCP servers ( `stateless_http=False` ). With a stateful MCP server, you can use capabilities such as elicitation (multi-turn user interactions) and sampling (LLM-generated content). For MCP protocol version `2025-11-25` and earlier, stateful mode is required for elicitation and sampling, because the server delivers these requests over an open session. For version `2026-07-28` and later, elicitation and sampling use the multi round-trip requests (MRTR) pattern, which does not require stateful mode. For more information about MRTR, see [Multi round-trip requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr) in the Model Context Protocol documentation.  
Stateful mode carries state within an MCP session across multiple requests. A stateless MCP server keeps state in a backing store that your application manages, such as a database. It uses explicit state handles to reference that state. The server returns a state identifier in a tool result, and the client passes it back on later tool calls to key into the store. For more information about explicit state handles, see [explicit state handles](https://modelcontextprotocol.io/seps/2567-sessionless-mcp#explicit-state-handles) in the Model Context Protocol documentation. For more information about stateful MCP servers, see [Stateful MCP server features](mcp-stateful-features.md).

### MCP session management and microVM stickiness
<a name="mcp-session-management"></a>

AgentCore Runtime routes each request to a microVM based on a session ID. It takes the session ID from a client request header, or generates one if the request doesn’t include it. Requests with the same session ID go to the same microVM while the session is active. On Instances, requests with the same session ID go to the same instance session. For more information, see [Use isolated sessions for agents](runtime-sessions.md) and, for Instances, [Session](runtime-instances-how-it-works.md#runtime-instances-session). Sending the same session ID on related requests helps you:
+ Avoid the latency of starting a new session for each request.
+ Reduce cost, because related requests share one session instead of each starting a new one.
+ Stay within the quota for active sessions, because each new session counts toward it. For more information, see [Resource allocation limits](bedrock-agentcore-limits.md#resource-allocation-limits).
+ Keep state that your server holds in memory across requests, such as the status of a long-running task that the client polls.

The header that AgentCore Runtime uses for the session ID depends on the MCP protocol version, because version `2026-07-28` removes the `Mcp-Session-Id` header. For more information, see [Key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog#major-changes) in the MCP 2026-07-28 specification.

#### Version 2026-07-28 and later
<a name="mcp-microvm-stickiness-2026-07-28"></a>

AgentCore Runtime uses `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` as the session ID. For backward compatibility, it still accepts `Mcp-Session-Id`. If the client sends both headers, AgentCore Runtime uses `Mcp-Session-Id`. Each response header returns the value that the client sent in the same request header, even if the two values differ. If the client sends only one of the headers, both response headers use its value. If the client sends neither, both use a session ID that the service generates.

**Tip**  
To keep requests on the same microVM, send the same `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` value on each request.

#### Version 2025-11-25 and earlier
<a name="mcp-microvm-stickiness-legacy"></a>

AgentCore Runtime uses `Mcp-Session-Id` as the session ID (for the MCP specification, see [MCP Streamable HTTP Transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#streamable-http)). Clients must capture the `Mcp-Session-Id` returned in the response and include it in all subsequent requests. The service doesn’t use `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` to route requests in this version.

 **Stateless MCP** ( `stateless_http=True` ):
+ The client can send its own `Mcp-Session-Id`, or omit it on the first request so that AgentCore Runtime returns one in the response.
+ The client must include the same `Mcp-Session-Id` in all subsequent requests for microVM affinity.

 **Stateful MCP** ( `stateless_http=False` ):
+ Client sends the initialize request without an `Mcp-Session-Id` header.
+ Platform returns `Mcp-Session-Id` in the response.
+ Client must include this `Mcp-Session-Id` in all subsequent requests for both session state and microVM affinity.

For more information about stateful MCP session management, see the [MCP session management specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#session-management).

## Server requirements
<a name="container-requirements-mcp"></a>

Whether you use direct code deployment or a container image, your MCP server must meet these requirements:
+  **Host**: `0.0.0.0` 
+  **Serving port**: `8000` by default, or the serving port in `protocolConfiguration.port` 
+  **Architecture**: ARM64. If you deploy a container image, build it for ARM64. If you use direct code deployment, build any native binaries in your package for ARM64.

You can change the serving port and the `InvokeAgentRuntime` POST path with `protocolConfiguration`. See [Path requirements](#path-requirements-mcp) for the default paths. For configuration examples, see [Configure your agent’s serving port and invocation path](runtime-configure-invocation.md).

## Path requirements
<a name="path-requirements-mcp"></a>

### /mcp - POST
<a name="mcp-endpoint"></a>

 **Purpose** 

Receives MCP RPC messages and processes them through your agent’s tool capabilities, complete pass-through of [InvokeAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html) API payload with standard MCP RPC messages

 **Response format** 

JSON-RPC based request/response format, supporting both `application/json` and `text/event-stream` as response content-types

 **Use cases** 

The `/mcp` endpoint serves several key purposes:
+ Tool invocation and management
+ Agent capability discovery
+ Resource access and manipulation
+ Multi-step agent workflows

### /ping - GET (Recommended)
<a name="mcp-ping-endpoint"></a>

 **Purpose** 

Reports whether your MCP server is healthy, independent of the MCP protocol version that your server implements. AgentCore Runtime doesn’t require `/ping`, but we recommend that every MCP server implement it. With `GET /ping`, your server can also report `HealthyBusy` while it runs background work, so that AgentCore Runtime doesn’t end the session for being idle. For more information, see [Runtime session lifecycle management](runtime-long-run.md#runtime-long-run-session-lifecycle).

 **Response format** 

To be detected, `/ping` must:
+ Be served at the root path (`/ping`) on your server’s serving port (`8000` by default), regardless of your MCP path.
+ Return a `2xx` status with a JSON body in the format described in [/ping - GET in the HTTP protocol contract](runtime-http-protocol-contract.md#http-ping-endpoint). Other responses, such as an HTML page or a catch-all `200` with a different body, are not treated as `/ping` support.

## Health probes
<a name="mcp-health-probes"></a>

AgentCore Runtime probes your server to decide when it is ready to serve traffic and whether it is still healthy. To implement the recommended health endpoint, see [/ping - GET (Recommended)](#mcp-ping-endpoint).

### Readiness check when a session starts
<a name="mcp-readiness-probe"></a>

When a new session starts, AgentCore Runtime sends `GET /ping` to your server’s serving port. Any response other than `502` or `429` shows that your server accepted the connection. This includes `404` and `405`. AgentCore Runtime then treats your server as ready. If your server doesn’t implement `/ping`, a `404 Not Found` for `GET /ping` in your access log is expected and harmless.

### Health checks during the session
<a name="mcp-liveness-probe"></a>

After your server is serving, AgentCore Runtime continues to check health. It first checks whether your server implements `GET /ping`. If it does, AgentCore Runtime uses `GET /ping` for the rest of the session. Otherwise, it sends an MCP `ping` request: a `POST` to your MCP path with a JSON-RPC `ping` method and the `Accept: application/json, text/event-stream` header. This fallback supports servers on MCP protocol version `2025-11-25` and earlier, in both stateful and stateless mode, and servers on version `2026-07-28`.

A server on version `2026-07-28` might reject the `ping` request, because that version removed the `ping` method and the `initialize` handshake. If your server returns HTTP `400` to `ping`, AgentCore Runtime sends an `initialize` request. If that request also returns `400`, AgentCore Runtime treats your server as healthy unless it stops responding or returns server errors. It also writes a one-time message to your agent’s logs that recommends implementing `/ping`. Other error responses to `ping` or `initialize` can fail the health check.

**Note**  
Your MCP SDK, its version, and its configuration determine whether your server answers `ping`. Some SDKs that support both the current and earlier versions still answer `ping` from clients that don’t specify a protocol version. SDKs that support only `2026-07-28` or later reject it. Without `GET /ping`, AgentCore Runtime can detect only that such a server has stopped responding or is returning errors other than the `ping` rejection, such as server errors. To give AgentCore Runtime a reliable health signal, implement `GET /ping`.

## Error handling
<a name="mcp-error-handling"></a>

AgentCore Runtime returns errors as JSON-RPC 2.0 error responses. Error codes and HTTP status codes depend on the `MCP-Protocol-Version` request header:
+  **Version `2026-07-28` and later** : The HTTP status code reflects the error, to align with the [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28).
+  **Version `2025-11-25` and earlier, or header missing or invalid** : Most errors return HTTP 200. Only authentication, authorization, and Accept header errors use other status codes.

The following table lists the error for each runtime exception.


| Runtime Exception | HTTP Error Code (2026-07-28 and later) | JSON-RPC Error Code (2026-07-28 and later) | HTTP Error Code (2025-11-25 and earlier) | JSON-RPC Error Code (2025-11-25 and earlier) | Error Message | 
| --- | --- | --- | --- | --- | --- | 
| UnauthorizedException | 401 | -32001 | 401 | -32001 | Authentication error - Invalid credentials | 
| AccessDeniedException | 403 | -20001 | 403 | -32002 | Authorization error - Insufficient permissions | 
| ThrottlingException | 429 | -32003 | 200 | -32003 | Rate limit exceeded - Too many requests | 
| ServiceQuotaExceededException | 429 | -32003 | 200 | -32003 | Rate limit exceeded - Too many requests | 
| ResourceNotFoundException | 404 | -32602 | 200 | -32004 | Resource not found - Requested resource does not exist | 
| ConflictException | 409 | -32005 | 200 | -32005 | Resource conflict - Resource already exists | 
| RetryableConflictException | 409 | -32005 | 200 | -32005 | Session operation in progress, please retry | 
| ValidationException | 400 | -32006 | 200 | -32006 | Validation error - Invalid request data | 
| RuntimeClientError | 424 | -32010 | 200 | -32010 | Tool execution error - Please check your CloudWatch logs for more information | 
| McpRequestUnacceptableException | 406 | -32011 | 406 | -32011 | Accept Header Error - MCP protocol requires Accept header: application/json, text/event-stream | 
| Any other exception | 500 | -32603 | 200 | -32603 | Internal error - Server error | 

**Note**  
For version `2026-07-28` and later, `AccessDeniedException` returns JSON-RPC error code `-20001` instead of `-32002`. The MCP 2026-07-28 specification doesn’t allow servers to send `-32002`, and it recommends that new error codes use values outside the JSON-RPC reserved range (`-32768` to `-32000`). The HTTP status code (403) stays the same.
For version `2026-07-28` and later, `ResourceNotFoundException` returns JSON-RPC error code `-32602` (Invalid params) instead of `-32004`. This matches the code that the MCP 2026-07-28 specification uses for a resource that doesn’t exist.

Example error response:

```
{
  "jsonrpc": "2.0",
  "id": "req-001",
  "error": {
    "code": -32005,
    "message": "Session operation in progress, please retry"
  }
}
```

### Responses from your MCP server
<a name="mcp-error-handling-server-status"></a>

When your MCP server returns one of the following status codes, the service returns that status code and the response body to the client. For any other status code, the service returns `RuntimeClientError`.
+  **Version `2026-07-28` and later** : 200, 202, 400, 401, 403, and 404. Other status codes return HTTP 424.
+  **Version `2025-11-25` and earlier** : 200 and 202. Other status codes return HTTP 200.

### Retrying RetryableConflictException
<a name="mcp-error-handling-retryable-conflict"></a>

 `ConflictException` and `RetryableConflictException` share error code `-32005` and differ by message. The service returns `RetryableConflictException` when an operation targets a session that is being provisioned or torn down. Retry with short exponential backoff — MCP clients do not auto-retry it. For version `2025-11-25` and earlier, the response is HTTP 200, so inspect the response body to detect it.

## OAuth authentication responses
<a name="mcp-oauth-authentication-responses"></a>

OAuth-configured agents follow [RFC 6749 (OAuth 2.0)](https://datatracker.ietf.org/doc/html/rfc6749) authentication standards. When authentication is missing, the service returns a 401 Unauthorized response with a WWW-Authenticate header (per [RFC 7235](https://datatracker.ietf.org/doc/html/rfc7235) ), enabling clients to discover the authorization server endpoints through the GetRuntimeProtectedResourceMetadata API.

### 401 Unauthorized
<a name="mcp-401-unauthorized"></a>

Returned when the Authorization header is missing or empty.

Response includes WWW-Authenticate header:

```
WWW-Authenticate: Bearer resource_metadata="https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{ESCAPED_ARN}/invocations/.well-known/oauth-protected-resource?qualifier={QUALIFIER}"
```

**Note**  
SigV4-configured agents return HTTP 403 and do not include `WWW-Authenticate` headers.