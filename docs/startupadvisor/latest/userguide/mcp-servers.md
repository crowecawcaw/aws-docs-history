

# Configure live data with the MCP server (optional)
<a name="mcp-servers"></a>

 AWS Startup Advisor can use a Model Context Protocol (MCP) server for live AWS data. The MCP server is an optional enhancement, not a requirement. Skills run without it, but they cannot fetch live AWS data, such as documentation, regional service availability, and live API calls. The MCP server is independent of skills, and it does not serve the skills that you install locally.

**Topics**
+ [Available MCP server](#mcp-servers-available)
+ [Provision the MCP server](#mcp-servers-provisioning)

## Available MCP server
<a name="mcp-servers-available"></a>

 AWS Startup Advisor can use the following MCP server:
+  `aws-mcp` – The AWS MCP Server. This stdio server launches through `uvx`. It provides access to current AWS documentation (search and read), regional service availability, authenticated AWS API calls, sandboxed Python script execution, and on-demand skill retrieval and recommendations. For more information, see [Understanding AWS MCP Server tools](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/understanding-mcp-server-tools.html).

This server runs through `uvx`, which requires `uv` and `uvx` on your machine. To install `uv`, see [the uv documentation](https://docs.astral.sh/uv/). The server launches with the following command.

```
uvx mcp-proxy-for-aws-cli@latest https://aws-mcp.us-east-1.api.aws/mcp
```

## Provision the MCP server
<a name="mcp-servers-provisioning"></a>

When you install the Claude Code plugin from the Claude Code Plugin Marketplace, the `aws-mcp` server is configured automatically because it is bundled with the plugin. For more information, see [Install the Claude Code plugin](getting-started.md#getting-started-claude-code).

The `npx skills add` path installs only the skills, not the MCP server. To use the MCP server with another agent, such as Kiro, Cursor, Codex, or fx, add the AWS MCP Server to that agent’s own MCP configuration. Then, install the skills separately. For example, add the server to the Kiro `.kiro/settings/mcp.json` file or the Cursor `.cursor/mcp.json` file with the following command.

```
uvx mcp-proxy-for-aws-cli@latest https://aws-mcp.us-east-1.api.aws/mcp
```