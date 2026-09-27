

# Agent setup guide
<a name="agent-setup-guide"></a>

Amazon SES publishes the `amazon-ses` skill to help AI coding agents set up and troubleshoot email sending. The AWS MCP Server can provide the current skill when your request needs it.

The current `amazon-ses` skill does not include Mail Manager or email receiving.

**Topics**
+ [Before you begin](#agent-setup-guide-prerequisites)
+ [Step 1: Connect your agent to AWS](#agent-setup-guide-choose-setup)
+ [Step 2: Use the Amazon SES skill](#agent-setup-guide-use-skill)
+ [Keep your setup current](#agent-setup-guide-keeping-current)

## Before you begin
<a name="agent-setup-guide-prerequisites"></a>

Prerequisites depend on the setup method that you choose.
+ For the AWS Command Line Interface wizard, an `aws-core` plugin, or the Kiro local-proxy configuration on this page, install [uv](https://docs.astral.sh/uv/), which includes `uvx`. These methods use `uvx` to run the local proxy for the AWS MCP Server. A direct OAuth connection does not require `uv`.
+ This step applies only when you install the skill locally for Kiro. Install [Node.js](https://nodejs.org/), which provides the `npx` command.
+ For a local-proxy or IAM SigV4 connection, configure AWS credentials locally before the agent calls AWS APIs. Documentation search and skill discovery do not require credentials. A direct OAuth connection uses browser sign-in and does not require local AWS credentials for the MCP connection. Local scripts that call AWS APIs still require credentials.
+ For a direct OAuth connection, the IAM identity that signs in must allow `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token`.

## Step 1: Connect your agent to AWS
<a name="agent-setup-guide-choose-setup"></a>

Follow the instructions for your agent. When connected, your agent can access the `amazon-ses` skill when needed.

### Claude Code
<a name="agent-setup-guide-connect-claude-code"></a>

Run these commands in Claude Code:

```
/plugin install aws-core@claude-plugins-official
/reload-plugins
```

**Note**  
If Claude Code reports that the plugin was not found, run `/plugin marketplace update claude-plugins-official`, and then retry the installation.

### Codex
<a name="agent-setup-guide-connect-codex"></a>

Add the Agent Toolkit marketplace from your terminal:

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Launch Codex, run `/plugins`, and install `aws-core`. Start a new conversation before you continue to Step 2.

### Cursor
<a name="agent-setup-guide-connect-cursor"></a>

In Cursor, choose *Settings*, *Plugins*, *Team Marketplaces*, *Add Marketplace*, and *Import from Repo*. Enter `aws/agent-toolkit-for-aws`. Then open the Plugins panel and install `aws-core`.

### Kiro
<a name="agent-setup-guide-connect-kiro"></a>

Kiro uses separate MCP and local skill configurations. Add the AWS MCP Server to `.kiro/settings/mcp.json`. Replace `us-west-2` with the default AWS Region for your operations.

```
{
  "mcpServers": {
    "aws": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws-cli@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

From your project root, install the local `amazon-ses` skill and its reference files:

```
npx skills add https://github.com/aws/agent-toolkit-for-aws \
    --skill amazon-ses \
    --agent kiro-cli \
    --yes
```

### Alternative: Automatic setup with the AWS Command Line Interface
<a name="agent-setup-guide-automatic-setup"></a>

If you have AWS Command Line Interface version 2.35.0 or later, run the setup wizard:

```
aws configure agent-toolkit
```

The wizard detects supported installed agents, installs the default AWS skills, and configures the AWS MCP Server. Restart your agent after the wizard completes.

### Alternative: Connect directly with OAuth 2.1
<a name="agent-setup-guide-connect-oauth"></a>

If your agent supports remote MCP servers, you can connect directly with OAuth 2.1 instead of running the local proxy. This path uses browser sign-in and does not require `uv` or local AWS credentials for the MCP connection. For commands for Claude Code, Codex, Cursor, and Kiro, see [OAuth 2.1 authentication for AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/oauth-authentication.html). A direct connection does not install the local skills included with `aws-core`.

### Another agent or custom framework
<a name="agent-setup-guide-custom-mcp-client"></a>

If your agent supports MCP, connect it directly to the AWS MCP Server. For client configuration and authentication options, including OAuth and IAM SigV4, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html).

If the agent supports Agent Skills, you can also install `amazon-ses` locally from the [Agent Toolkit for AWS on GitHub](https://github.com/aws/agent-toolkit-for-aws). Choose the target agent when prompted.

## Step 2: Use the Amazon SES skill
<a name="agent-setup-guide-use-skill"></a>

For Amazon SES access-control guidance, see [Identity and access management in Amazon SES](control-user-access.md). For connection or authentication problems, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html).

Describe the outcome that you want. You don't need to name the skill. For example, replace `example.com` with your domain and use this prompt:

```
Set up example.com as a sending domain in Amazon SES.
```

## Keep your setup current
<a name="agent-setup-guide-keeping-current"></a>

The AWS MCP Server provides the current `amazon-ses` skill. If you installed a local copy, repeat the installation process to update it.