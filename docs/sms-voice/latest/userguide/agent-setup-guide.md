

# Agent setup guide
<a name="agent-setup-guide"></a>

AI coding agents can accelerate messaging development by guiding you through workflows that historically required navigating multiple documentation pages. Examples include creating a Rich Communication Services (RCS) branded agent, sending a one-time passcode, registering to send SMS, and moving from the sandbox to production. AWS End User Messaging SMS publishes an agent skill that gives your agent step-by-step, validated guidance for these tasks. An agent configured with your AWS credentials can also run the underlying API calls. Without credentials, the skill provides guidance only.

This skill is part of a set that spans both messaging services. This page covers SMS, RCS, voice, and notify (one-time passcode). For WhatsApp, see the [Agent setup guide](https://docs.aws.amazon.com/social-messaging/latest/userguide/agent-setup-guide.html) in the AWS End User Messaging Social documentation.

**Topics**
+ [Prerequisites](#agent-setup-guide-prerequisites)
+ [Step 1: Connect the AWS MCP Server](#agent-setup-guide-connect-mcp-server)
+ [Step 2: Install the RCS and notify skill (aws-sms-voice)](#agent-setup-guide-install-skill)
+ [Keeping the skill current](#agent-setup-guide-keeping-current)

## Prerequisites
<a name="agent-setup-guide-prerequisites"></a>
+ [uv](https://docs.astral.sh/uv/) installed on your system.
+ (Optional) An AWS account with IAM credentials configured locally. Credentials are required only for tools that execute AWS End User Messaging SMS API calls, not for searching documentation or discovering skills. If you do not have credentials configured, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html).

## Step 1: Connect the AWS MCP Server
<a name="agent-setup-guide-connect-mcp-server"></a>

The AWS MCP Server, built on the Model Context Protocol (MCP), gives your agent AWS API access, sandboxed execution, and documentation search. Follow [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for your agent. The essentials:

### Claude Code / Codex / Cursor
<a name="agent-setup-guide-connect-plugin"></a>

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

## Step 2: Install the RCS and notify skill (aws-sms-voice)
<a name="agent-setup-guide-install-skill"></a>

For Claude Code, Codex, and Cursor, `aws-core` already includes the skill, so you can skip this step. For any other agent:

```
npx skills add aws/agent-toolkit-for-aws/skills --skill aws-sms-voice --yes --global
```

This skill's onboarding paths that reach a real message are RCS Business Messaging and notify (one-time passcode, or OTP). It also carries registration guidance for SMS and RCS. Try a hero prompt:

*I want to try out RCS Business Messaging on AWS End User Messaging SMS. How do I create a branded test agent, add my phone as a verified tester, and send myself my first RCS message?*

Other things to ask:
+ *Send myself a branded RCS message with media, and show me how to add rich cards and suggestion buttons.*
+ *My RCS agent works in test. How do I launch it for a country so it delivers to real customers, with carrier monitoring and SMS fallback?*
+ *How do I receive replies to my RCS messages, and check a recipient's opt-out state before I send?*
+ *I need to send a one-time passcode over SMS to my customers. How do I set that up?*
+ *I want to send SMS to customers in the US. What registration do I need, and can you walk me through it?*
+ *I have been testing SMS in the sandbox. How do I move to production and raise my sending limits?*

For the underlying workflows, see the SMS and RCS getting started pages, [Getting started with AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started.html) and [Getting started with RCS](https://docs.aws.amazon.com/sms-voice/latest/userguide/rcs-getting-started.html).

## Keeping the skill current
<a name="agent-setup-guide-keeping-current"></a>

As AWS End User Messaging SMS adds features, future skill releases include updated patterns and guidance, so your agent always works from current best practices.