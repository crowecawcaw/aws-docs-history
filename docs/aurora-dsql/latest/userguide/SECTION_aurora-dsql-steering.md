# Aurora DSQL Steering: Skills and Powers

This section describes how to configure AI steering for Aurora DSQL using skills and powers. These
markdown-based configuration files provide context and guidance that AI assistants automatically
apply when generating code to improve the quality of agentic development.

## Overview

Skills and powers are modular capabilities that extend AI assistant functionality for Aurora DSQL.
They package instructions, metadata, and resources that AI assistants use automatically when
working with Aurora DSQL databases.

### Why Use Skills and Powers

Skills and powers provide several key benefits for Aurora DSQL development:

- **Specialize AI assistants** - Provide domain-specific
  expertise for Aurora DSQL including best practices, Postgres-compatible SQL patterns,
  and distributed database optimizations.
- **Reduce repetition** - Create once, use automatically.
  Eliminates the need to repeatedly provide the same guidance across multiple conversations.
- **Context efficiency** - Skills load on-demand rather
  than consuming context upfront. The AI loads information in stages as needed.
- **Continual learning** - As Aurora DSQL features evolve,
  AI assistants access updated patterns automatically when skills are updated.

### Recommended Setup Paths

Choose the setup path that matches your development environment:

- [Skills CLI](#skills-cli "#skills-cli") (Agent-Agnostic)
- [Kiro Power](#kiro-power "#kiro-power")
- [Claude Skill](#claude-skill "#claude-skill")
- [Gemini Skill](#gemini-skill "#gemini-skill")
- [Codex Skill](#codex-skill "#codex-skill")

The [DSQL Skill](https://github.com/awslabs/mcp/tree/main/src/aurora-dsql-mcp-server/skills/dsql-skill "https://github.com/awslabs/mcp/tree/main/src/aurora-dsql-mcp-server/skills/dsql-skill")
can also be used with other AI coding agents by copying the skill folder into the tool's
`rules` or `skills` directory.

## Skills CLI

The [DSQL skill](https://skills.sh/awslabs/mcp/dsql "https://skills.sh/awslabs/mcp/dsql") can be installed using
the [Skills CLI](https://skills.sh/docs/cli "https://skills.sh/docs/cli"). This agent-agnostic
setup method works with most AI coding assistants and allows you to install the skill to
multiple agents at once.

### Setup

Run the following command to install the Aurora DSQL skill:

```
npx skills add awslabs/mcp --skill dsql
```

The CLI will guide you through:

- **Selecting agents** - Choose which agents to install to
  (Kiro, Claude Code, Cursor, Copilot, Gemini, Codex, Roo, Cline, OpenCode, Windsurf, etc.)
- **Installation scope** - Choose between:
  - Project: Install in current directory (committed with your project)
  - Global: Install in home directory (available across all projects)

- **Installation method** - Choose between:
  - Symlink (Recommended): Single source of truth, easy updates
  - Copy to all agents: Independent copies for each agent

### Managing Skills

Check and update skills at any time using:

```
npx skills check
npx skills update
```

## Kiro Power

Kiro powers are unified packages that bundle MCP tools with framework expertise and steering
instructions. Each power includes an entry point document explaining available MCP tools and
activation triggers, the MCP server configuration, and additional workflow-specific guidance
loaded on-demand.

Powers activate dynamically based on user context. Rather than loading all tools upfront,
powers maintain near-zero baseline usage until relevant keywords trigger activation.

### Setup

To setup the Kiro power for Aurora DSQL:

1. Install directly from the [Kiro Powers Registry](https://kiro.dev/launch/powers/amazon-aurora-dsql/ "https://kiro.dev/launch/powers/amazon-aurora-dsql/")
2. Once redirected to the Power in the IDE, either:
   - Select the **Try Power** button. Suggested for users who want
     the AI to guide MCP server setup or an interactive onboarding experience with Aurora DSQL to create
     a new cluster.
   - Open a new Kiro chat and ask anything related to Aurora DSQL. Optionally update the MCP Config
     with your existing cluster details to test the MCP server connection so it can be used out
     of the box with the power. The Kiro agent will automatically activate the power if it
     identifies the power as valuable for completing the user's task.

## Claude Skill

Claude skills are modular capabilities that extend Claude's functionality. Each skill packages
instructions, metadata, and optional resources that Claude uses automatically when relevant.
Skills are filesystem-based and load on-demand to minimize context usage.

### Simple Setup with the Skills CLI

The skill can be installed to Claude Code using the [Skills CLI](#skills-cli "#skills-cli"). To specify
only Claude Code as the agent to install to, use:

```
npx skills add awslabs/mcp --skill dsql --agent claude-code
```

### Alternative: Direct Setup Using a Git Clone

The alternative setup takes a sparse clone of the dsql-skill directory and symlinks this clone
into the `~/.claude/skills/` folder. This allows changes to the skill to be pulled
whenever the skill needs to be updated.

#### Prerequisites

- Git installed

#### Setup Steps

**1. Create a base repos directory**

```
mkdir -p .dsql_skill_repos
```

**2. Sparse clone the skill from the MCP repository**

Clone only the `dsql-skill` folder (no other files):

```
cd .dsql_skill_repos
git clone --filter=blob:none --no-checkout https://github.com/awslabs/mcp.git
cd mcp
git sparse-checkout init --cone
git sparse-checkout set src/aurora-dsql-mcp-server/skills/dsql-skill
git checkout
cd ../..
```

**3. Symlink the skill into the Skills Directory**

Add the skills directory (default: global/user-scoped):

```
mkdir -p ~/.claude/skills
```

###### Note

If you want to make this a project-scoped skill, use your project root's `.claude/skills/` directory instead.

Add the symlink:

```
ln -s "$(pwd)/.dsql_skill_repos/mcp/src/aurora-dsql-mcp-server/skills/dsql-skill" ~/.claude/skills/dsql-skill
```

**4. Verify the setup**

```
# Should show SKILL.md and other skill files
ls -la ~/.claude/skills/dsql-skill/
```

**5. Verify Skill Use**

Once the skill is configured, you should have a new skill command: `/dsql`.
You may have to restart Claude Code after adding the skill for it to be detected. You can use
this command from the Claude Code CLI or panel as desired.

#### Updating the Skill

To pull the latest changes from the repository:

```
cd .dsql_skill_repos/mcp
git pull
```

#### Directory Structure

After setting up a global skill, you should see these directories:

```
.dsql_skill_repos/
└── mcp/                              # Sparse git checkout
    └── src/
        └── aurora-dsql-mcp-server/
            └── skills/
                └── dsql-skill/
                    ├── SKILL.md
                    └── ...

~/.claude/
└── skills/
    └── dsql-skill -> /path/to/.dsql_skill_repos/mcp/src/aurora-dsql-mcp-server/skills/dsql-skill
```

###### Note

Add `.dsql_skill_repos/` to your `.gitignore` if you don't want to track it.
The sparse checkout keeps only the skill folder, minimizing disk usage.

## Gemini Skill

To add the Aurora DSQL skill directly in Gemini, decide on a scope: `workspace`
(contained to project) or `user` (default, global) and use the skills installer.

### Setup

```
gemini skills install https://github.com/awslabs/mcp.git --path src/aurora-dsql-mcp-server/skills/dsql-skill --scope $SCOPE
```

Replace `$SCOPE` with either `workspace` or `user`.

You can then use the `/dsql` skill command with Gemini, and Gemini will
automatically detect when the skill should be used.

## Codex Skill

Use the skill installer from the Codex CLI or TUI using the `$skill-installer` skill.

### Setup

```
$skill-installer install dsql skill: https://github.com/awslabs/mcp/tree/main/src/aurora-dsql-mcp-server/skills/dsql-skill
```

Restart Codex to pick up the skill. The skill can then be activated using `$dsql`.
