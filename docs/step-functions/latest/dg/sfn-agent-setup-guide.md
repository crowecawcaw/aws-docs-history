

# Agent setup guide
<a name="sfn-agent-setup-guide"></a>

AI coding agents can accelerate serverless development by providing intelligent assistance for application scaffolding, deployment configuration, debugging, and infrastructure-as-code generation. By configuring your agent with the right combination of plugins and skills, you equip it with expertise required to build and manage serverless applications.

**Work with your coding agent**  
For a quick-start reference, you can drop this link directly into your agent's context: `https://docs.aws.amazon.com/step-functions/latest/dg/samples/aws-sfn-agent-setup.md`

Choose the installation method that matches your development environment.

## Prerequisites
<a name="sfn-agent-setup-prerequisites"></a>

Ensure the following prerequisites are in place for installing the aws-core plugin:
+ [uv](https://docs.astral.sh/uv/) installed on your system.
+ (Optional) An AWS account with IAM credentials set up on your local machine. Credentials are required for tools that execute AWS API calls and run scripts, but not for searching documentation or discovering skills. If you do not have credentials configured, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) for detailed instructions.

## Claude Code
<a name="sfn-agent-setup-claude-code"></a>

Install the aws-core plugin, part of the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html), that bundles the AWS MCP Server configuration and a curated set of agent skills (including the AWS serverless skill).

### Install aws-core plugin from Agent Toolkit for AWS
<a name="sfn-agent-setup-claude-code-plugin"></a>

Run the following command to install the plugin:

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-core@agent-toolkit-for-aws
```

This installs agent skills including the AWS serverless skill, agent hooks, and the AWS MCP Server configuration in one step.

## Codex
<a name="sfn-agent-setup-codex"></a>

### Install AWS serverless skill
<a name="sfn-agent-setup-codex-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

## Cursor
<a name="sfn-agent-setup-cursor"></a>

### Install AWS serverless skill
<a name="sfn-agent-setup-cursor-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

## Kiro
<a name="sfn-agent-setup-kiro"></a>

### Install AWS serverless skill in Kiro CLI
<a name="sfn-agent-setup-kiro-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

### Install Kiro powers (from Kiro IDE)
<a name="sfn-agent-setup-kiro-powers"></a>

Install the following Kiro powers that provide specialized contexts and tools to the Kiro agents on-demand:
+ **Serverless Application Model (SAM)** — install via [Kiro powers link](https://kiro.dev/launch/powers/add/?name=aws-sam).

## GitHub Copilot
<a name="sfn-agent-setup-github-copilot"></a>

### Install AWS serverless skill
<a name="sfn-agent-setup-github-copilot-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

## Windsurf
<a name="sfn-agent-setup-windsurf"></a>

### Install AWS serverless skill
<a name="sfn-agent-setup-windsurf-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

## OpenCode
<a name="sfn-agent-setup-opencode"></a>

### Install AWS serverless skill
<a name="sfn-agent-setup-opencode-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```

## For all other agents compatible with agent skills
<a name="sfn-agent-setup-other-agents"></a>

For any other agent that supports the open-source [agent skills](https://agentskills.io/specification) format, follow these steps:

### Install AWS serverless skill
<a name="sfn-agent-setup-other-agents-skill"></a>

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-serverless --yes --global
```