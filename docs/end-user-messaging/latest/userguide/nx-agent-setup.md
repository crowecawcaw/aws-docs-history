

# Agent setup guide
<a name="nx-agent-setup"></a>

AI coding agents can accelerate messaging development by guiding you through workflows that historically required navigating multiple documentation pages. Examples include creating a Rich Communication Services (RCS) branded agent, sending a one-time passcode, registering to send SMS, connecting a WhatsApp Business Account, and moving from the sandbox to production. AWS End User Messaging publishes agent skills that give your agent step-by-step, validated guidance for these tasks. An agent configured with your AWS credentials can also run the underlying API calls. Without credentials, a skill provides guidance only.

AWS End User Messaging publishes a set of skills that spans its messaging services:
+ The `aws-sms-voice` skill covers SMS, RCS, voice, and Notify (one-time passcode).
+ The `aws-social-messaging` skill covers WhatsApp.

You connect the AWS MCP Server once, then install the skill or skills for the channels you use.

## Prerequisites
<a name="nx-agent-setup-prerequisites"></a>
+ [uv](https://docs.astral.sh/uv/) installed on your system.
+ (Optional) An AWS account with IAM credentials configured locally. Credentials are required only for tools that run AWS End User Messaging API calls, not for searching documentation or discovering skills. If you do not have credentials configured, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html).

## Step 1: Connect the AWS MCP Server
<a name="nx-agent-setup-connect-mcp-server"></a>

The AWS MCP Server, built on the Model Context Protocol (MCP), gives your agent AWS API access, sandboxed execution, and documentation search. Follow [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for your agent. The essentials follow.

**Claude Code, Codex, or Cursor**  
The `aws-core` plugin bundles the AWS MCP Server configuration and a curated set of skills in one install:

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-core@agent-toolkit-for-aws
```

**Kiro**  
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

**Any other agent**  
See [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for the configuration block for your MCP client. Only the configuration file location differs (`.cursor/mcp.json`, `.vscode/mcp.json`, and so on).

## Step 2: Install the skills
<a name="nx-agent-setup-install-skills"></a>

Install the skill or skills for the channels you use. For Claude Code, Codex, and Cursor, the `aws-core` plugin already includes these skills, so you can skip the install command.

### SMS, RCS, voice, and Notify (aws-sms-voice)
<a name="nx-agent-setup-install-sms-voice"></a>

For any agent other than Claude Code, Codex, or Cursor, install the skill:

```
npx skills add aws/agent-toolkit-for-aws/skills --skill aws-sms-voice --yes --global
```

This skill's onboarding paths that reach a real message are RCS Business Messaging and Notify (one-time passcode, or OTP). It also carries registration guidance for SMS and RCS. Things to ask:
+ Send myself a branded RCS message with media, and show me how to add rich cards and suggestion buttons.
+ My RCS agent works in test. How do I launch it for a country so it delivers to real customers, with carrier monitoring and SMS fallback?
+ How do I receive replies to my RCS messages, and check a recipient's opt-out state before I send?
+ I need to send a one-time passcode over SMS to my customers. How do I set that up?
+ I want to send SMS to customers in the US. What registration do I need, and can you walk me through it?
+ I have been testing SMS in the sandbox. How do I move to production and raise my sending limits?

For the underlying workflows, see [How to get set up](nx-sms-get-set-up.md) and [How to get set up](nx-rcs-get-set-up.md).

### WhatsApp (aws-social-messaging)
<a name="nx-agent-setup-install-social"></a>

For any agent other than Claude Code, Codex, or Cursor, install the skill:

```
npx skills add aws/agent-toolkit-for-aws/skills --skill aws-social-messaging --yes --global
```

This skill covers WhatsApp through AWS End User Messaging. Things to ask:
+ Help me create a WhatsApp utility template for order-shipping notifications.
+ List my WhatsApp message templates and show which are approved versus pending.
+ I want delivery-status and template-status notifications for my WhatsApp Business Account. What are my options?

For the underlying workflows, see [How to get set up](nx-whatsapp-get-set-up.md).

## Keeping the skills current
<a name="nx-agent-setup-keeping-current"></a>

As AWS End User Messaging adds features, future skill releases include updated patterns and guidance, so your agent always works from current best practices.