

# Setting up your coding agent for Amazon Braket
<a name="amazon-braket-agent-setup"></a>

Amazon Braket is a fully managed quantum computing service. With AI coding agents, you can accelerate quantum development. Your agent can help you build circuits, find devices, run quantum tasks and hybrid jobs, and track and control costs.

**Work with your coding agent**  
Paste the following link into your coding agent:  

```
https://docs.aws.amazon.com/braket/latest/developerguide/samples/aws-braket-agent-setup.md
```

## Prerequisites
<a name="amazon-braket-agent-setup-prerequisites"></a>


| Requirement | Description | 
| --- | --- | 
| uv | To run the AWS Model Context Protocol (MCP) Server, install uv on your system. The `aws-core` plugin uses the AWS MCP Server to give your agent access to AWS APIs and documentation. For instructions, see [Installing uv on the Astral website](https://docs.astral.sh/uv/getting-started/installation/). | 
| AWS Command Line Interface (AWS CLI) | Install AWS CLI version `2.35.0` or later. You use the AWS CLI to install the `amazon-braket` skill. | 
| (Optional) AWS credentials | Set up an AWS account with AWS Identity and Access Management (IAM) credentials on your local machine. You need credentials for tools that run AWS API calls and scripts. You do not need credentials to search documentation or discover skills. For instructions on setting up credentials, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html#choosing-auth-method). | 

## Installing the amazon-braket skill
<a name="amazon-braket-agent-setup-install"></a>

To give your agent expertise in Amazon Braket, install the `amazon-braket` skill. A skill is a package of instructions and reference material that your agent loads when a task needs it. The `amazon-braket` skill is part of the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html), which gives AI coding agents the tools, knowledge, and guardrails they need to build, deploy, and manage applications on AWS. To install the skill into each supported agent that the AWS CLI detects on your system, run the following AWS CLI command:

```
aws agent-toolkit add-skill \
    --skill-name amazon-braket \
    --region us-east-1
```

The `amazon-braket` skill is now installed for each supported agent that the AWS CLI detects. For example commands and output, see [add-skill](https://docs.aws.amazon.com/cli/latest/reference/agent-toolkit/add-skill.html) in the *AWS CLI Command Reference*.

Agent Toolkit for AWS is available only in the US East (N. Virginia) AWS Region, so the command uses `--region us-east-1`.

To see the supported agents, run `aws agent-toolkit add-skill help` and check the `--agent` option. For more information, see [AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html#aws-cli-add-skill) in the *Agent Toolkit for AWS User Guide*.

## Installing the aws-core plugin
<a name="amazon-braket-agent-setup-aws-core"></a>

The `aws-core` plugin is part of the Agent Toolkit for AWS. It bundles the AWS MCP Server configuration and a curated set of agent skills. The plugin does not include the `amazon-braket` skill. Choose the section for your agent.

### Claude Code
<a name="amazon-braket-agent-setup-claude-code"></a>

To install the `aws-core` plugin, run the following Claude Code CLI commands:

1. Add the Agent Toolkit for AWS marketplace to Claude Code.

   ```
   claude plugin marketplace add aws/agent-toolkit-for-aws
   ```

1. Install the `aws-core` plugin.

   ```
   claude plugin install aws-core@agent-toolkit-for-aws
   ```

The plugin is now available in Claude Code.

### Codex
<a name="amazon-braket-agent-setup-codex"></a>

To install the `aws-core` plugin, run the following Codex CLI commands:

1. Add the Agent Toolkit for AWS marketplace to Codex.

   ```
   codex plugin marketplace add aws/agent-toolkit-for-aws
   ```

1. Install the `aws-core` plugin.

   ```
   codex plugin add aws-core@agent-toolkit-for-aws
   ```

The plugin is now available in Codex.

### Kiro
<a name="amazon-braket-agent-setup-kiro"></a>

In Kiro, a plugin is called a power. To install the `aws-core` power, run the following Kiro CLI command. The command installs the power from the Kiro powers registry.

```
kiro-cli powers install aws-core
```

For more information about powers, see [Powers on the Kiro website](https://kiro.dev/docs/powers/). For instructions on installing powers in the Kiro IDE or Kiro Web, see [Install powers on the Kiro website](https://kiro.dev/docs/powers/installation/).

### Other agents
<a name="amazon-braket-agent-setup-other-agents"></a>

For other agents, see your agent's documentation for skill and plugin installation instructions.

## Removing the amazon-braket skill and aws-core plugin
<a name="amazon-braket-agent-setup-remove"></a>

To remove the `amazon-braket` skill from each agent where you installed it, run the following AWS CLI command:

```
aws agent-toolkit remove-skill \
    --skill-name amazon-braket \
    --region us-east-1
```

For example commands and output, see [remove-skill](https://docs.aws.amazon.com/cli/latest/reference/agent-toolkit/remove-skill.html) in the *AWS CLI Command Reference*.

To remove the `aws-core` plugin, run the command for your agent:
+ Claude Code:

  ```
  claude plugin uninstall aws-core@agent-toolkit-for-aws
  ```
+ Codex:

  ```
  codex plugin remove aws-core@agent-toolkit-for-aws
  ```
+ Kiro:

  ```
  kiro-cli powers uninstall aws-core
  ```