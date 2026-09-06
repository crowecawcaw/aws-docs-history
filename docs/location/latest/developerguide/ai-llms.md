

# Build with AI agents
<a name="ai-llms"></a>

 AI and LLMs can significantly accelerate development with Amazon Location Service by providing intelligent assistance for API usage, code generation, and troubleshooting. By configuring your LLM client with the right MCP servers and context, you can create a powerful development assistant that understands AWS services and Amazon Location Service specifics. Using a minimal context and MCP configuration as recommended on this page can ensure your LLM model of choice has enough context to lead to correct results without overwhelming the context window. This can reduce hallucinations and increase result accuracy. This configuration also ensures that model knowledge cutoff does not impact the quality of the results. The Amazon Location Service agent context package provides ready-to-use integrations for popular AI coding assistants, guiding AI agents through adding maps, places search, geocoding, routing, and other geospatial features, including authentication setup, SDK integration, and best practices. 

**Work with your coding agent**  
To get started quickly, paste this link into your AI assistant's context window:  

```
https://docs.aws.amazon.com/location/latest/developerguide/ai-llms.md
```

 Choose the installation method that matches your development environment. 

## For Kiro users
<a name="ai-llms-install-kiro"></a>

 [Kiro](https://kiro.dev) supports Amazon Location Service through both the Kiro IDE (as a power) and the Kiro CLI (as an Agent Skill). 

------
#### [ Kiro IDE ]

 Install Amazon Location Service as a power using the one-click install link: 

 [Install Amazon Location Service power in Kiro](https://kiro.dev/launch/powers/amazon-location-service) 

**Tip**  
 Alternatively, open Kiro IDE, navigate to the **Powers** panel, select the **Available** tab, and search for "Build geospatial applications with Amazon Location Service". 

**Note**  
 When using [Spec](https://kiro.dev/docs/specs/) mode, include "use the Amazon Location Service power" in your spec prompt for Kiro to activate it. 

------
#### [ Kiro CLI ]

 Install Amazon Location Service as an [Agent Skill](https://agentskills.io) using the skills CLI: 

```
npx skills add aws-geospatial/amazon-location-agent-context -a kiro-cli
```

 After installing, add the skill to your custom agent's resources in `.kiro/agents/<agent>.json`: 

```
{
    "resources": [
        "skill://.kiro/skills/**/SKILL.md"
    ]
}
```

**Note**  
 Kiro CLI skill installations don't include MCP configuration automatically. See [MCP Servers](#ai-llms-mcp-servers) for manual setup. 

------

 Once installed, Amazon Location Service activates automatically when you mention keywords like "location", "maps", "geocoding", "routing", "places", "geofencing", or "tracking" in your prompts. 

## For Claude Code and Cursor users
<a name="ai-llms-install-plugin"></a>

 For Claude Code and Cursor users, install the **amazon-location-service** plugin from the respective official marketplaces. The plugin includes MCP configuration automatically. 

------
#### [ Claude Code ]

 You can install the **amazon-location-service** plugin from the official [Claude Plugins Marketplace](https://github.com/anthropics/claude-plugins-official). 

Run the following command to install the plugin:

```
/plugin install amazon-location-service@claude-plugins-official
```

**Note**  
 If you install the plugin during an active session, run `/reload-plugins` to activate it without restarting. 

------
#### [ Cursor ]

 You can install the **amazon-location-service** plugin from the official [Cursor Marketplace](https://cursor.com/marketplace/aws). For additional information, see the [Cursor plugin documentation](https://docs.cursor.com/plugins). You can also install within the Cursor application: 

1. Open Cursor Settings.

1. Navigate to **Plugins**.

1. Search for **AWS**.

1.  Select the **amazon-location-service** plugin and choose **Add to Cursor**. 

1. Select the scope for the installed plugin.

 The plugin should appear under **Plugins** > **Installed**. 

------

## For Codex users
<a name="ai-llms-install-codex"></a>

 Our plugin hasn't been added to the official Codex marketplace yet, so you'll need to install it from the [agent-plugins](https://github.com/awslabs/agent-plugins) marketplace: 

1.  Clone the [agent-plugins](https://github.com/awslabs/agent-plugins) repository locally. 

1.  Open the repository in Codex so it can discover `.agents/plugins/marketplace.json`. 

1. Open the plugins with `/plugins`.

1. Navigate to **Amazon Location Service**.

1.  Press Enter and choose **Install plugin**. 

## For other AI coding agents
<a name="ai-llms-install-agent-skill"></a>

 For AI coding agents that support the [Agent Skills](https://agentskills.io) open standard (including GitHub Copilot, OpenCode, Codex, Antigravity, and [more](https://github.com/vercel-labs/skills?tab=readme-ov-file#supported-agents)), install the skill using the skills CLI: 

```
npx skills add aws-geospatial/amazon-location-agent-context
```

 The CLI guides you through selecting which agent to install the skill for and at what scope (project or user level): 

```
$ npx skills add aws-geospatial/amazon-location-agent-context

? Select an agent: (Use arrow keys)
› Claude Code
  Cursor
  GitHub Copilot
  OpenCode
  Codex
  Antigravity

? Select a scope: (Use arrow keys)
› Project — install in current directory (committed with your project)
  Global — install globally for all projects
```

 You can also install for a specific agent directly: 

GitHub Copilot:

```
npx skills add aws-geospatial/amazon-location-agent-context -a github-copilot
```

OpenCode:

```
npx skills add aws-geospatial/amazon-location-agent-context -a opencode
```

Codex:

```
npx skills add aws-geospatial/amazon-location-agent-context -a codex
```

 Once installed, the skill activates automatically when your task involves location, maps, geocoding, routing, or other Amazon Location Service topics. 

**Note**  
 For Claude Code and Cursor users, we recommend the [For Claude Code and Cursor users](#ai-llms-install-plugin) for the best experience, as it includes MCP configuration automatically. 

## For direct context usage
<a name="ai-llms-install-direct-context"></a>

 If you are not using Kiro, Claude Code/Cursor plugins, or one of the agents supported by Agent Skills, you can load the context files directly into your LLM: 

1.  Start with `context/amazon-location.md` from the [amazon-location-agent-context](https://github.com/aws-geospatial/amazon-location-agent-context) repository for the service overview. 

1.  Add specific files from `context/additional/` as needed for your task, or allow the LLM client to read them on demand. 

## MCP Servers
<a name="ai-llms-mcp-servers"></a>

 The Kiro IDE (Power) and [For Claude Code and Cursor users](#ai-llms-install-plugin) installations include MCP configuration automatically. If you are using the Kiro CLI, [For other AI coding agents](#ai-llms-install-agent-skill), or [For direct context usage](#ai-llms-install-direct-context), configure the following server manually for full functionality: 
+  **[AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-aws-mcp-server.html)** – AWS API exploration, execution, and documentation access. For setup instructions, see [Getting started with the AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/getting-started-aws-mcp-server.html). 