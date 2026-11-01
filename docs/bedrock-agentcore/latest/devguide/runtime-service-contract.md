

# Understand the AgentCore Runtime service contract
<a name="runtime-service-contract"></a>

The AgentCore Runtime service contract defines the standardized communication protocol that your agent application must implement to integrate with the Amazon Bedrock agent hosting infrastructure. This contract ensures seamless communication between your custom agent code and AWS's managed hosting environment.

**Topics**
+ [Supported protocols](#supported-protocols)
+ [Compare supported protocols](#protocol-comparison)
+ [Reserved platform ports](#runtime-reserved-ports)
+ [HTTP protocol contract](runtime-http-protocol-contract.md)
+ [MCP protocol contract](runtime-mcp-protocol-contract.md)
+ [A2A protocol contract](runtime-a2a-protocol-contract.md)
+ [AG-UI protocol contract](runtime-agui-protocol-contract.md)
+ [Configure your agent’s serving port and invocation path](runtime-configure-invocation.md)

## Supported protocols
<a name="supported-protocols"></a>

The AgentCore Runtime service contract supports the following communication protocols:
+  [HTTP](runtime-http-protocol-contract.md) : Direct REST API endpoints for traditional request/response patterns
+  [MCP](runtime-mcp-protocol-contract.md) : Model Context Protocol for tools and agent servers
+  [A2A](runtime-a2a-protocol-contract.md) : Agent-to-Agent protocol for multi-agent communication and discovery
+  [AG-UI](runtime-agui-protocol-contract.md) : Agent-to-User Interface protocol for interactive agent experiences with UI rendering

## Compare supported protocols
<a name="protocol-comparison"></a>

Compare the HTTP, MCP, A2A, and AG-UI protocols to understand the differences and use cases.


| Feature | HTTP Protocol | MCP Protocol | A2A Protocol | AG-UI Protocol | 
| --- | --- | --- | --- | --- | 
|  **Default serving port**  | 8080 | 8000 | 9000 | 8080 | 
|  **Default mount path**  | /invocations (HTTP), /ws (WebSocket) | /mcp | / (root) | /invocations (SSE), /ws (WebSocket) | 
|  **Message Format**  | REST JSON/SSE, WebSocket (text/binary) | JSON-RPC | JSON-RPC 2.0 | Event streams (SSE/WebSocket) | 
|  **Discovery**  | N/A | Tool listing | Agent Cards | N/A | 
|  **Authentication**  | SigV4, OAuth 2.0; WebSocket supports SigV4 by headers and query params | SigV4, OAuth 2.0 | SigV4, OAuth 2.0 | SigV4, OAuth 2.0 | 
|  **Use Case**  | Direct API calls, real-time streaming | Tool servers | Agent-to-agent communication | Interactive UI experiences | 

You can configure the serving port and the POST path used by `InvokeAgentRuntime`. For configuration details and examples, see [Configure your agent’s serving port and invocation path](runtime-configure-invocation.md).

To access application-defined HTTP methods and paths or additional servers in a session, enable session endpoints with `allowedPorts`. For more information, see [Connect to runtime sessions through a session endpoint](runtime-session-endpoints.md).

## Reserved platform ports
<a name="runtime-reserved-ports"></a>

AgentCore Runtime reserves the following ports for platform use:
+  `1144` 
+  `1514` 
+  `1571` 
+  `2049` 
+  `4317`–`4318` (inclusive)
+  `8443` 
+  `48620` 
+  `48640` 
+  `53530`–`53532` (inclusive)

Choose other ports for your application servers. An `allowedPorts` entry cannot specify a reserved port or a range that contains any reserved port. For the other port validation rules, see [Configure allowed ports](runtime-session-endpoints.md#runtime-session-endpoints-allowed-ports).