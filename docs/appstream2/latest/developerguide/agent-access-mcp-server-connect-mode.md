

# Connection modes
<a name="agent-access-mcp-server-connect-mode"></a>

You can control how your agent waits for the desktop session to become available by setting the `x-amzn-agentaccess-connect-mode` header on your Model Context Protocol (MCP) requests.

**Note**  
Connection modes apply to both non-domain-joined and domain-joined fleets. Set the `x-amzn-agentaccess-connect-mode` header alongside whichever authentication mechanism your fleet type uses. For non-domain-joined fleets, that is either the stack and user ID headers or a streaming-URL header. For domain-joined fleets, it is the SAML assertion metadata.

The following modes are available:
+ **BLOCKING** (default): the MCP server waits until the desktop connection is fully established before responding. When `tools/list` returns, all tools are immediately available.
+ **POLLING**: the MCP server responds immediately without waiting for the desktop connection. Initially, only the `connection_status` tool is available. Your agent polls this tool until the connection is established, at which point the full tool set becomes available.

Use POLLING mode when you want your agent to perform other work while waiting for the desktop connection, or when you need more control over connection timeout behavior.

The following example shows how to use POLLING mode:

```
# Pass the header when creating the MCP connection
headers = {
    "x-amzn-agentaccess-streaming-session-url": streaming_url,  # non-domain-joined fleets
    "x-amzn-agentaccess-connect-mode": "POLLING",
}

# After initialize, tools/list returns immediately with connection_status
tools = await session.list_tools()
# tools = [connection_status]

# Poll connection_status until the desktop is ready
while True:
    result = await session.call_tool("connection_status", {})
    status = json.loads(result.content[0].text)
    if status["state"] == "CONNECTED":
        break
    time.sleep(2)

# Now tools/list returns the full set (screenshot, left_click, type_text, and so on)
tools = await session.list_tools()
```

**Clean up**: To avoid ongoing streaming charges, end the WorkSpaces Applications streaming session when your agent finishes its work. Disconnect the agent so the session closes, and do not leave idle sessions running.