

# Connecting to the DevOps Agent MCP server
<a name="connecting-to-devops-agent-remote-servers-connecting-to-the-devops-agent-mcp-server"></a>

## Connect with Kiro
<a name="connect-with-kiro"></a>

For [Kiro](https://kiro.dev/) users, a dedicated **AWS DevOps Agent** power is available from the IDE or from the [Kiro Powers marketplace](https://kiro.dev/powers/#aws-devops-agent).

**Step 1: Install the power**

Install the **aws-devops-agent** power from the Powers marketplace.

**Step 2: Set environment variables**

Set the following environment variables to configure the connection:

```
DEVOPS_AGENT_TOKEN=<your-access-token>
DEVOPS_AGENT_REGION=<your-agent-space-region>
```

**Step 3: Approve the variables in Kiro**

Go to **Settings** > **MCP Approved Env Vars** and approve `DEVOPS_AGENT_TOKEN` and `DEVOPS_AGENT_REGION`. Kiro does not pass environment variables to MCP servers until they are approved.

**Step 4: Restart Kiro**

Restart Kiro to apply the changes.

The Kiro power includes `aws-mcp` as a fallback, which provides direct AWS API access when the remote server endpoint is unavailable.

## Connect with Claude Code
<a name="connect-with-claude-code"></a>

For [Claude Code](https://code.claude.com/docs/en/overview) users, AWS DevOps Agent is available from the **aws-agents-for-devsecops** Claude plugin, which brings both AWS DevOps Agent and AWS Security Agent capabilities into Claude. Install it from [Claude plugins](https://claude.com/plugins/aws-agents-for-devsecops) or the [source repository](https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-agents-for-devsecops).

1. Install the **aws-agents-for-devsecops** plugin.

1. Run the `/aws-agents-for-devsecops:setup-devops-agent` command to configure your connection.

## Connect with other MCP clients
<a name="connect-with-other-mcp-clients"></a>

For any MCP-compatible client, configure the server with:
+ **URL** – `https://connect.aidevops.{region}.api.aws/mcp`
+ **Authorization header** – `Bearer <your-token>`
+ **Timeout** – 120 seconds minimum (initial responses can take 5–30 seconds; ongoing chat sessions may take longer)

This configuration also works with Kiro and Claude Code if you prefer to configure the connection manually instead of using the dedicated power or plugin.

Example MCP configuration:

```
{
  "mcpServers": {
    "aws-devops-agent": {
      "url": "https://connect.aidevops.{region}.api.aws/mcp",
      "headers": {
        "Authorization": "Bearer <your-access-token>"
      }
    }
  }
}
```

Replace `{region}` with your Agent Space's Region (for example, `us-east-1`) and `<your-access-token>` with the token value.

For token creation and SigV4 setup, see [Authentication and security](connecting-to-devops-agent-remote-servers-authentication-and-security.md).