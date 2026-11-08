

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

This server runs through `uvx`, which requires `uv` and `uvx` on your machine. To install `uv`, see [the uv documentation](https://docs.astral.sh/uv/). The plugin pins the proxy version and launches the server with the following command.

```
uvx mcp-proxy-for-aws-cli==1.7.0 https://aws-mcp.us-east-1.api.aws/mcp
```

In a manual configuration, you can use `@latest` in place of `==1.7.0` to launch the most recent version.

## Provision the MCP server
<a name="mcp-servers-provisioning"></a>

When you install the plugin for Claude Code or Codex, the `aws-mcp` server is configured automatically because it is bundled with the plugin. For more information, see [Install the plugin for Claude Code and Codex](getting-started.md#getting-started-claude-code).

The `npx skills add` path installs only the skills, not the MCP server. To use the MCP server with another agent, such as Kiro, fx, or another coding agent, add the AWS MCP Server to that agent’s own MCP configuration. Then, install the skills separately. For example, add the server to the Kiro `.kiro/settings/mcp.json` file or the Cursor `.cursor/mcp.json` file with the following command.

```
uvx mcp-proxy-for-aws-cli@latest https://aws-mcp.us-east-1.api.aws/mcp
```

The `operate-on-aws` skill registers a separate AWS DevOps Agent MCP server when you set up AWS DevOps Agent. The plugin does not register this server.