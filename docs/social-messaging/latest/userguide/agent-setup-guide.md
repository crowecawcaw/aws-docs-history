

# Agent setup guide
<a name="agent-setup-guide"></a>

AI coding agents can accelerate WhatsApp development. They guide you through workflows that historically required navigating multiple documentation pages, such as connecting a WhatsApp Business Account, adding a tester, sending your first message, and managing templates. AWS End User Messaging Social publishes an agent skill that gives your agent step-by-step, validated guidance for these tasks. An agent configured with your AWS credentials can also run the underlying API calls. Without credentials, the skill provides guidance only.

This skill is part of a set that spans both messaging services. This page covers WhatsApp. For SMS, RCS, voice, and notify (one-time passcode), see the [Agent setup guide](https://docs.aws.amazon.com/sms-voice/latest/userguide/agent-setup-guide.html) in the AWS End User Messaging SMS documentation.

## Prerequisites
<a name="agent-setup-guide-prerequisites"></a>
+ Install [`uv`](https://docs.astral.sh/uv/) on your system.
+ (Optional) An AWS account with AWS Identity and Access Management (IAM) credentials configured locally. Credentials are required only for tools that execute AWS End User Messaging Social API calls, not for searching documentation or discovering skills. If you do not have credentials configured, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html).

## Step 1 — Connect the AWS MCP Server
<a name="agent-setup-guide-connect-mcp-server"></a>

The AWS MCP Server, built on the Model Context Protocol (MCP), gives your agent AWS API access, sandboxed execution, and documentation search. Follow [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for your agent. The essentials:

### Claude Code, Codex, or Cursor
<a name="agent-setup-guide-connect-claude-codex-cursor"></a>

The `aws-core` plugin bundles the AWS MCP Server configuration and a curated set of skills in one install:

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-core@agent-toolkit-for-aws
```

### Kiro
<a name="agent-setup-guide-connect-kiro"></a>

Add the server to `.kiro/settings/mcp.json`:

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

### Any other agent
<a name="agent-setup-guide-connect-other"></a>

See [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for the configuration block for your MCP client. Only the configuration file location differs (`.cursor/mcp.json`, `.vscode/mcp.json`, and so on).

## Step 2 — Install the WhatsApp skill (aws-social-messaging)
<a name="agent-setup-guide-install-skill"></a>

For Claude Code, Codex, or Cursor, `aws-core` already includes the skill, so you can skip this step. For any other agent:

```
npx skills add aws/agent-toolkit-for-aws/skills --skill aws-social-messaging --yes --global
```

This skill covers WhatsApp through AWS End User Messaging Social. Try a hero prompt:

*I want to send myself a WhatsApp message from AWS End User Messaging. Walk me through connecting a WhatsApp Business Account, adding my number as a tester, and sending my first message.*

Other things to ask:
+ *Help me create a WhatsApp utility template for order-shipping notifications.*
+ *List my WhatsApp message templates and show which are approved versus pending.*
+ *I want delivery-status and template-status notifications for my WhatsApp Business Account. What are my options?*

For the underlying workflows, see the WhatsApp getting-started pages in the AWS End User Messaging Social documentation. For more information, see [Getting started with AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/getting-started-whatsapp.html).

## Keeping the skill current
<a name="agent-setup-guide-keeping-current"></a>

As AWS End User Messaging Social adds features, future skill releases include updated patterns and guidance, so your agent always works from current best practices.