

# Set up an AI agent for Amazon Lightsail

AI agents can speed up your work with Amazon Lightsail by guiding you through tasks that otherwise mean moving between several documentation pages. Lightsail publishes agent skills that give your agent step-by-step guidance for the tasks they cover. These tasks range from creating a resource to troubleshooting issues while you manage it. An agent configured with your AWS credentials can also run the underlying API calls. Without credentials, a skill provides guidance only.

Setting up an agent takes two steps. You connect your agent to AWS once, and then install the skills for the tasks you do.

**Topics**
+ [How an agent works](#agent-setup-guide-how-it-works)
+ [Before you begin](#agent-setup-guide-prerequisites)
+ [Step 1: Connect your agent to AWS](#agent-setup-guide-connect)
+ [Step 2: Install the skills you need](#agent-setup-guide-install-skills)
+ [Step 3: Work with Lightsail using your agent](#agent-setup-guide-use)
+ [Lightsail AI skills](lightsail-ai-skills.md)

## How an agent works
<a name="agent-setup-guide-how-it-works"></a>

You describe what you want in your own words. Your agent loads the skill that matches your request, and the skill supplies the steps and the AWS Command Line Interface (AWS CLI) operations that do the work. Each part has the following role.

**AI agent**  
Reads your request, loads the skill that fits it, and runs the operations that the skill calls for. Your agent is the AI coding tool that you work in, such as Claude Code, Codex, Cursor, or Kiro.

**Agent skill**  
Carries the instructions for one task: the steps to follow, the operations to run, and how to check the result.

**AWS MCP Server**  
Delivers the skill to your agent and runs the operations for you, over the open Model Context Protocol (MCP). For more information, see [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in the *Agent Toolkit for AWS User Guide*.

**AWS CLI**  
Provides the operations that do the work, and runs them on your computer when the AWS MCP Server isn't available. It also carries the setup wizard in Step 1.

## Before you begin
<a name="agent-setup-guide-prerequisites"></a>

Complete these steps on the computer where you run your AI agent. The agent runs the commands on this page locally, and it calls AWS APIs with the credentials that it finds on that computer.

The following table lists what you need before you start, and what each item is used for.


| Requirement | Needed for | 
| --- | --- | 
| AWS Command Line Interface version 2.35.0 or later. For instructions, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). | The setup wizard in Step 1. Check your version with aws --version. | 
| uv, which provides the uvx command that runs the MCP Proxy for AWS. To install it, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html). | Connecting your agent in Step 1. | 
| Node.js, which provides the npx command that runs the skills CLI. | Installing a skill in Step 2. | 
| AWS credentials configured locally. For instructions, see [Authentication and access credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html). | Letting your agent call Lightsail APIs on your behalf. Searching documentation and discovering skills don't require credentials. | 

## Step 1: Connect your agent to AWS
<a name="agent-setup-guide-connect"></a>

Install the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html), which includes the AWS MCP Server. The toolkit supports Claude Code, Codex, Cursor, Kiro, and other agents that support MCP.

From the computer where you run your agent, run the setup wizard.

```bash
aws configure agent-toolkit
```

The wizard detects the supported agents that are installed on your computer, installs the default AWS skills, and configures the AWS MCP Server. Restart your agent after the wizard completes.

If you can't use the wizard, configure the AWS MCP Server for your agent manually. For instructions, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) in the *Agent Toolkit for AWS User Guide*. That guide also covers the authentication options and the supported agents.

This step is the same for every Lightsail skill, and you complete it only once.

## Step 2: Install the skills you need
<a name="agent-setup-guide-install-skills"></a>

Installing a skill takes one command, whichever agent you use. The command names the repository that holds the skill, and the skill to install.

```bash
npx skills add https://github.com/aws/agent-toolkit-for-aws \
    --skill {{skill-name}} \
    --yes \
    --global
```

For the skills that Lightsail publishes and the exact command for each one, see [Lightsail AI skills](lightsail-ai-skills.md).

Add `--global` to install a skill for your user account, so that it's available in every project that you open. Omit it to install the skill into the current project only, which keeps the skill alongside the code that needs it.

To update the skills that you installed, run `npx skills update`. To list them, run `npx skills list`.

## Step 3: Work with Lightsail using your agent
<a name="agent-setup-guide-use"></a>

Describe the outcome that you want, in your own words. Your agent matches your request against the description of each installed skill and loads the one that fits.

Some agents load a skill automatically when your request describes a task that the skill covers. To make sure your agent uses a specific skill, name it in your request, as in `Use the Lightsail container skill to...`. Each skill in [Lightsail AI skills](lightsail-ai-skills.md) lists example prompts that you can adapt.

To see which skills are available from inside your agent, ask `What Lightsail skills do I have?`