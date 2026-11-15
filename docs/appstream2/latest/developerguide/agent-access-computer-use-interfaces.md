

# Computer use interfaces
<a name="agent-access-computer-use-interfaces"></a>

By default, an agent uses the native WorkSpaces Applications tools, such as `left_click` and `type_text`. With a model-specific computer use interface, you present those tools in the model's own schema instead. The Model Context Protocol (MCP) server converts each call into the underlying desktop actions. You select the interface for each request by sending an HTTP header to the MCP server.

Different providers train their computer use models to call tools by different names and shapes. For example, to click at a point, the native tools use a `left_click` tool. One provider's model calls a single `computer` tool with an action of `left_click`. Another provider's model calls a `computer` tool with an action of `click`.

When you select the computer use interface that matches your model, the model uses the tool names and schema it was trained on. This increases accuracy and lowers the cost for your agent to perform actions.

## Select an interface
<a name="agent-access-computer-use-interfaces-select"></a>

You select a computer use interface by sending the `x-amzn-agentaccess-computer-use-interface-id` HTTP header on the `tools/list` request and on every `tools/call` request. The header name is case-insensitive, and the value is case-sensitive.

```
x-amzn-agentaccess-computer-use-interface-id: ANTHROPIC_COMPUTER_20251124
```

You send the value only as this HTTP header. The interface is selected per request and isn't stored. A change to the header takes effect on the next `tools/list` or `tools/call` request.

If you omit the header or send it empty, the agent uses the native WorkSpaces Applications tools described in [Available tools](agent-access-mcp-server-tools.md). If you send a value that isn't one of the supported values, the MCP server returns the JSON-RPC error `-32602`.

Selecting an interface replaces only the standard desktop tools. Session tools, forwarded tools, and application catalog tools are unchanged.

## Supported interfaces
<a name="agent-access-computer-use-interfaces-supported"></a>

The following table lists the computer use interfaces that WorkSpaces Applications supports.


| Computer use interface | Header value | 
| --- | --- | 
| Default (standard desktop tools) | Omit the header | 
| Anthropic computer use (2025-01-24) | ANTHROPIC\_COMPUTER\_20250124 | 
| Anthropic computer use (2025-11-24) | ANTHROPIC\_COMPUTER\_20251124 | 
| Anthropic computer toolset (2026-08-01) | ANTHROPIC\_COMPUTER\_TOOLSET\_20260801 | 
| OpenAI computer use v1 | OPENAI\_COMPUTER\_V1 | 
| Gemini computer use 3.x desktop v1 | GOOGLE\_COMPUTER\_USE\_3X\_DESKTOP\_V1 | 