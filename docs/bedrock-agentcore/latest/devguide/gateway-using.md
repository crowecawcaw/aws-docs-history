# Use an AgentCore gateway

After [setting up your gateway with targets](gateway-building.md "gateway-building.md"), you can configure your application or agent to use the gateway through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro"). The MCP provides a standardized way for agents to discover and invoke tools.

###### Note

AgentCore Gateway supports the following MCP versions:

- 2025-06-18
- 2025-03-26
  You can use the following MCP operations with an AgentCore gateway:

| Operation  | Description                                         |
| ---------- | --------------------------------------------------- |
| tools/call | Invokes a specific tool with the provided arguments |
| tools/list | Lists all available tools provided by the gateway   |

The following topics describe how to invoke your AgentCore gateway:

###### Topics

- [Authorize and authenticate to a AgentCore gateway and gateway target](gateway-using-auth.md "gateway-using-auth.md")
- [List available tools in an AgentCore gateway](gateway-using-mcp-list.md "gateway-using-mcp-list.md")
- [Call a tool in a AgentCore gateway](gateway-using-mcp-call.md "gateway-using-mcp-call.md")
- [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md")
- [Create an agent that uses your AgentCore gateway](gateway-agent-integration.md "gateway-agent-integration.md")
