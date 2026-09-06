

# Developer tools
<a name="developer-tools"></a>

You can access AWS Transform agents from agentic IDEs, agent plugins, and the MCP server. Choose the surface that fits your workflow.

**Note**  
The Kiro Power and agent plugins automatically install the MCP server. You only need to install the MCP server manually if you want to use it without a Kiro Power or agent plugin.

## Kiro Power
<a name="developer-tools-kiro"></a>

The [AWS Transform Kiro Power](https://kiro.dev/launch/powers/aws-transform) provides full access to AWS Transform agents from the Kiro IDE.

**To install the AWS Transform Kiro Power**

1. Open Kiro IDE and navigate to the Powers panel.

1. Find **AWS Transform** in the list and install it.

1. Open Kiro Chat, click on the Power, and select **Try power**.

Alternatively, in the Powers panel choose **Add Custom Power** > **Import power from GitHub** and paste: `https://github.com/kirodotdev/powers/tree/main/aws-transform`

## Agent plugin
<a name="developer-tools-agent-plugin"></a>

The AWS Transform agent plugin is available at [awslabs/agent-plugins](https://github.com/awslabs/agent-plugins) on GitHub, in the `plugins/aws-transform` directory. The plugin supports Claude Code, Codex, and Cursor.

The plugin includes `.claude-plugin`, `.codex-plugin`, and `.mcp.json` configurations. It provides access to all AWS Transform agents, such as .NET, mainframe, VMware, SQL Server, and custom transformations.

**To install in Claude Code**

Run the following commands:

```
/plugin marketplace add awslabs/agent-plugins
/plugin install aws-transform@agent-plugins-for-aws
```

**To install in Codex or Cursor**

Follow the instructions in the agent-plugins repository README.

## IDE plugin
<a name="developer-tools-ide-plugin"></a>

The AWS Transform IDE plugin is available on VS Code and Open VSX compatible editors. It exposes AWS Transform custom features, including creating and running transformation definitions. It also exposes mainframe features, including traceability between modernization requirements, business rules, and source code, as well as the ability to generate technical documentation on demand. To get started, install using one of the following methods:
+ **VS Code:** Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-transform-plugin).
+ **Open VSX:** Install from the [Open VSX registry](https://open-vsx.org/extension/amazonwebservices/aws-transform-plugin).

## MCP server
<a name="developer-tools-mcp"></a>

Use the MCP server to integrate AWS Transform programmatically with any MCP-compatible client. You can install the MCP server from PyPI as `awslabs.aws-transform-mcp-server`. It provides 19 tools for workspace management, job management, human-in-the-loop (HITL) tasks, artifact handling, connector management, chat, and resource browsing.
+ Python 3.10 or later

**Claude Code**

```
claude mcp add awslabs.aws-transform-mcp-server -- uvx awslabs.aws-transform-mcp-server@latest
```

**Kiro**

Add to `~/.kiro/settings/mcp.json`:

```
{
  "mcpServers": {
    "awslabs.aws-transform-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-transform-mcp-server@latest"]
    }
  }
}
```

For configuration details for your specific MCP client, see the [aws-transform-mcp-server](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server) README on GitHub.

## Authentication
<a name="developer-tools-auth"></a>

AWS Transform supports SSO (AWS Identity and Access Management Identity Center) and IAM role-based authentication.

**SSO (IAM Identity Center)**

Ask your AI assistant to "Configure AWS Transform with SSO." The assistant provides a start URL and opens your browser for login.

**IAM role**

Your environment provides AWS credentials automatically. Set `AWS_PROFILE` in your MCP client configuration `env` block to select a specific profile.

For information about setting up authentication for AWS Transform, see [Getting started with AWS Transform](getting-started.md).

## Build custom agents for AWS Transform
<a name="developer-tools-build-agents"></a>

The [agent builder toolkit](https://kiro.dev/launch/powers/aws-transform-agent-toolkit) enables AWS Partners and customers to build agents tailored to their specific modernization needs that work within AWS Transform.

**To install the agent builder toolkit**

1. Open Kiro IDE and navigate to the Powers panel.

1. Find **AWS Transform Agent Toolkit** in the list and install it.

Alternatively, in the Powers panel choose **Add Custom Power** > **Import power from GitHub** and paste: `https://github.com/kirodotdev/powers/tree/main/aws-transform-agent-toolkit`

The agent builder toolkit enables Migration and Modernization Competency Partners, ISVs, or customers to create transformation solutions for specific use cases. You can integrate specialized agents, tools, knowledge bases, and workflows with AWS Transform agentic AI capabilities.

Build  
Use the Kiro Power to combine the base agent and SDK to write your own customized agent.

Share  
Distribute agents with teams or across partner networks.

Register  
Register agents with AWS Transform for discovery by other users.