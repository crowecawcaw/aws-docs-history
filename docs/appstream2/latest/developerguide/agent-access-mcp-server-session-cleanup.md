

# Session cleanup
<a name="agent-access-mcp-server-session-cleanup"></a>

When your agent finishes its work, it ends its session with the Model Context Protocol (MCP) server. Ending the session, and optionally expiring the streaming session, releases the underlying streaming instance so the fleet's autoscaling policy can reclaim idle capacity and avoid unnecessary cost. How the agent ends the session, and what happens to the underlying WorkSpaces Applications streaming session, depends on the MCP protocol version. For the supported versions, see [Supported MCP protocol versions](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-protocol-versions).

## Stateless MCP protocol
<a name="agent-access-mcp-cleanup-stateless"></a>

With the stateless MCP protocol (version 2026-07-28), the agent ends the session by calling the `close_session` tool. This closes the MCP session. By default, `close_session` does not expire the WorkSpaces Applications streaming session; the streaming instance is preserved for reuse until the session's disconnect timeout is reached. To also expire the streaming session, the agent sets `expire_streaming_session` to `true` when it calls `close_session`. Expiring the streaming session terminates the streaming instance and triggers the fleet's configured autoscaling policy. For more information about the tool, see [Available tools](agent-access-mcp-server-tools.md). For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md). For more information about autoscaling, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).

## Earlier MCP protocol versions
<a name="agent-access-mcp-cleanup-stateful"></a>

With the earlier MCP protocol versions, you end the session by closing the MCP client in your agent code. When the MCP client lifecycle ends, the client sends an HTTP `DELETE` request to the MCP server. Some agent frameworks, such as Strands, close the client for you when the session ends. You control whether ending the session also expires the streaming session by setting the `x-amzn-agentaccess-expire-streaming-session-on-delete` header on your MCP requests. The following values are available:
+ `true` – When the MCP client sends the HTTP `DELETE` request, the MCP server expires the WorkSpaces Applications streaming session as part of cleanup. This terminates the streaming instance and triggers the fleet's configured autoscaling policy. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).
+ `false` (default) – The streaming session continues running until the disconnect timeout is reached. For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).

**Note**  
By default, an `mcp-proxy-for-aws` MCP client handles the `DELETE` request for you when you properly end the client lifecycle.