# Developer tools

You can access AWS Transform agents from agentic IDEs, agent plugins, and the MCP server.
Choose the surface that fits your workflow.

###### Note

The Kiro Power and agent plugins automatically install the MCP server. You only need to
install the MCP server manually if you want to use it without a Kiro Power or agent
plugin.

## Kiro Power

The AWS Transform Kiro Power provides full access to AWS Transform agents from the
Kiro IDE.

###### To install the AWS Transform Kiro Power

1. Open the Kiro marketplace.
2. Search for "AWS Transform" in the marketplace.
3. Choose **Install** to add the power to your Kiro environment.

The Kiro Power follows the standard Kiro power installation process and provides access
to all AWS Transform agents.

## Agent plugin

The AWS Transform agent plugin is available at
[https://github.com/awslabs/agent-plugins](https://github.com/awslabs/agent-plugins "https://github.com/awslabs/agent-plugins")
in the `plugins/aws-transform` directory. The plugin supports Claude Code, Codex,
and Cursor.

The plugin includes `.claude-plugin`, `.codex-plugin`, and
`.mcp.json` configurations. It provides access to all AWS Transform agents, such as
.NET, mainframe, VMware, SQL Server, and custom transformations.

**To install in Claude Code**

Run the following commands:

```
/plugin marketplace add awslabs/agent-plugins
/plugin install aws-transform@agent-plugins-for-aws
```

**To install in Codex or Cursor**

Follow the instructions in the agent-plugins repository README.

## MCP server

Use the MCP server to integrate AWS Transform programmatically with any MCP-compatible
client. You can install the MCP server from PyPI as
`awslabs.aws-transform-mcp-server`. It provides 19 tools for workspace management,
job management, human-in-the-loop (HITL) tasks, artifact handling, connector management, chat,
and resource browsing.

###### Prerequisites

- Python 3.10 or later

###### Installation

```
uvx awslabs.aws-transform-mcp-server@latest
```

For configuration details for your specific MCP client, see
[https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server "https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server").

## Authentication

AWS Transform supports SSO (AWS Identity and Access Management Identity Center) and IAM role-based
authentication.

**SSO (IAM Identity Center)**

Ask your AI assistant to "Configure AWS Transform with SSO." The assistant provides a
start URL and opens your browser for login.

**IAM role**

Your environment provides AWS credentials automatically. Set
`AWS_PROFILE` in your MCP client configuration `env` block to select a
specific profile.

For information about setting up authentication for AWS Transform, see
[Getting started with AWS Transform](getting-started.md "getting-started.md").

## Build custom agents for AWS Transform

The agent builder toolkit enables AWS Partners and customers to build agents tailored to
their specific modernization needs that work within AWS Transform.

###### To install the agent builder toolkit

1. Open the Kiro marketplace.
2. Search for "Build an agent for AWS Transform" in the marketplace.
3. Choose **Install** to add the power to your Kiro environment.

The agent builder toolkit enables Migration and Modernization Competency Partners, ISVs,
or customers to create transformation solutions for specific use cases. You can integrate specialized
agents, tools, knowledge bases, and workflows with AWS Transform agentic AI capabilities.

###### Agent lifecycle

Build

Use the Kiro Power to combine the base agent and SDK to write your own customized
agent.

Share

Distribute agents with teams or across partner networks.

Register

Register agents with AWS Transform for discovery by other users.
