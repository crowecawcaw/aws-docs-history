

# Aurora DSQL steering: Plugins, skills, and powers
<a name="SECTION_aurora-dsql-steering"></a>

 Use the `databases-on-aws` plugin to give your AI coding agent guidance for Aurora DSQL development. The plugin includes the `dsql` skill, which helps with schema design, queries, migrations, and troubleshooting. Install the plugin in Claude Code, Codex, or Cursor. You can also use the Kiro Power or install the skill on its own. 

## Overview
<a name="steering-overview"></a>

 Choose the format that your AI tool supports: 
+ **Plugins** bundle skills with tools and hooks. The `databases-on-aws` plugin is available from [Agent Plugins for AWS](https://github.com/awslabs/agent-plugins/blob/main/README.md#agent-plugins-for-aws) on the GitHub website.
+ **Skills** give an agent instructions and reference files to load as needed. Use the Skills CLI to install the `dsql` skill on its own.
+ **Powers** package guidance and Model Context Protocol (MCP) server configuration for Kiro. The Aurora DSQL power helps you set up tools and develop applications in the Kiro IDE.

### Why use steering
<a name="why-use-steering"></a>

 Steering gives your agent Aurora DSQL guidance that you don't need to repeat in each prompt. After setup, start a new chat. Ask the agent to review an Aurora DSQL schema or plan a migration. The agent can load guidance for the task. You can also ask it to use the Aurora DSQL skill or power by name. 

### Recommended setup paths
<a name="recommended-paths"></a>

Choose the setup path for your AI tool:
+ [Claude Code plugin](#claude-code-plugin)
+ [Codex plugin](#codex-plugin)
+ [Cursor plugin](#cursor-plugin)
+ [Kiro Power](#kiro-power)
+ [Other AI tools: Standalone skill](#other-ai-tools)<a name="claude-skill"></a><a name="claude-skill.title"></a>

## Claude Code plugin
<a name="claude-code-plugin"></a>

Install the `databases-on-aws` plugin in Claude Code.<a name="claude-skill-direct-setup"></a><a name="claude-skill-direct-setup.title"></a><a name="claude-skill-prerequisites"></a><a name="claude-skill-prerequisites.title"></a><a name="claude-skill-setup"></a><a name="claude-skill-setup.title"></a><a name="claude-skill-updating"></a><a name="claude-skill-updating.title"></a><a name="claude-skill-directory-structure"></a><a name="claude-skill-directory-structure.title"></a><a name="claude-skill-simple-setup"></a><a name="claude-skill-simple-setup.title"></a>

### Setup
<a name="claude-code-plugin-setup"></a>

Run these commands in Claude Code to add the marketplace and install the plugin:

```
/plugin marketplace add awslabs/agent-plugins
/plugin install databases-on-aws@agent-plugins-for-aws
```

 For more information, see [Claude Code](https://github.com/awslabs/agent-plugins/blob/main/README.md#claude-code) in *Agent Plugins for AWS* on the GitHub website. <a name="codex-skill"></a><a name="codex-skill.title"></a><a name="codex-skill-setup"></a><a name="codex-skill-setup.title"></a>

## Codex plugin
<a name="codex-plugin"></a>

Install the `databases-on-aws` plugin from the repository's marketplace:

1. Use Git to clone the Agent Plugins for AWS repository:

   ```
   git clone https://github.com/awslabs/agent-plugins.git
   ```

1. Open the cloned `agent-plugins` directory in Codex. Restart Codex to discover the marketplace.

1. Open the plugin directory, choose the **Agent Plugins for AWS** marketplace, and install `databases-on-aws`.

1. Start a new chat to use the plugin's skills and tools.

 For more information, see [Codex](https://github.com/awslabs/agent-plugins/blob/main/README.md#codex) in *Agent Plugins for AWS* on the GitHub website. To install only the skill, see [Other AI tools: Standalone skill](#other-ai-tools). 

## Cursor plugin
<a name="cursor-plugin"></a>

 Install [AWS Databases](https://cursor.com/marketplace/aws/databases-on-aws) from the Cursor Marketplace. This is the `databases-on-aws` plugin, which includes the Aurora DSQL skill. 

 For more information, see [Cursor](https://github.com/awslabs/agent-plugins/blob/main/README.md#cursor) in *Agent Plugins for AWS* on the GitHub website. 

## Kiro Power
<a name="kiro-power"></a>

Use the Aurora DSQL power for guidance and MCP tools in the Kiro IDE.

### Setup
<a name="kiro-power-setup"></a>

1. Open the Aurora DSQL power from the [Kiro Powers Registry](https://kiro.dev/launch/powers/add/?name=amazon-aurora-dsql). The link opens the power in the Kiro IDE.

1. Choose **Try power** for guided MCP server setup, or open a new Kiro chat and describe an Aurora DSQL task.

1. (Optional) To connect to an existing cluster, add your cluster details to the power's MCP configuration. Test the connection. For more information, see [AWS Labs Aurora DSQL MCP Server](SECTION_aurora-dsql-mcp-server.md).<a name="gemini-skill"></a><a name="gemini-skill.title"></a><a name="other-skill"></a><a name="other-skill.title"></a>

## Other AI tools: Standalone skill
<a name="other-ai-tools"></a>

 Use the Skills CLI to install the `dsql` skill in other supported AI tools. You can also choose this path when you want only the skill. It installs instructions and reference files, without the plugin's MCP servers or hooks. To set up database tools, see [AWS Labs Aurora DSQL MCP Server](SECTION_aurora-dsql-mcp-server.md). <a name="gemini-skill-setup"></a><a name="gemini-skill-setup.title"></a><a name="other-skill-setup"></a><a name="other-skill-setup.title"></a>

### Skills CLI
<a name="skills-cli"></a>

 You can install the skill for one or more coding agents, including Codex. For more information, see [CLI Reference](https://www.skills.sh/docs/cli) on the skills.sh website. 

#### Setup
<a name="skills-cli-setup"></a>

 Install Node.js 22.20.0 or later and npm. Run this command to install the Aurora DSQL skill: 

```
npx skills add https://github.com/awslabs/agent-plugins --skill dsql
```

 Follow the prompts: 
+ Choose the coding agents that use the skill.
+ Choose project scope for the current directory, or global scope for all projects.
+ Use symlinks to share one copy of the skill, or keep a copy for each agent.

#### Managing skills
<a name="skills-cli-management"></a>

 To list skills in the current project, run this command: 

```
npx skills list
```

 To list only global skills, run this command: 

```
npx skills list --global
```

 To update the Aurora DSQL skill in both the current project and global scope, run this command. The command defaults to both scopes. 

```
npx skills update dsql
```

 To update only the current project's Aurora DSQL skill, run this command: 

```
npx skills update dsql --project
```

 To update only the global Aurora DSQL skill, run this command: 

```
npx skills update dsql --global
```