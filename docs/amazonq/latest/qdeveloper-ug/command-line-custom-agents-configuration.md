# Configuration reference

Custom agent configuration files are JSON documents that define how an custom agent behaves. This section provides an overview of configuration concepts and common patterns.

## Configuration reference

For complete details about custom agent configuration file format, available fields, and syntax, see the supplementary Amazon Q Developer CLI documentation:

- [Agent configuration format](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md") - Complete reference for all configuration options
- [Built-in tools reference](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/built-in-tools.md") - Documentation for all built-in tools and their configuration options

You can also view the JSON schema for custom agent configuration files by running:

```
/agent schema
```

## Configuration concepts

Custom agent configuration files contain several key sections that control different aspects of custom agent behavior:

### Basic metadata

Every custom agent can include basic metadata for identification and documentation:

- **Name** - The custom agent's identifier (derived from filename if not specified)
- **Description** - Human-readable explanation of the custom agent's purpose
- **Prompt** - High-level context for the agent, similar to a system prompt
- **Model** - Specify which model the agent should use (e.g., `"model": "claude-sonnet-4"`). If not specified, the agent uses the default model. The model ID must match an available model from the Amazon Q CLI model service.

### Tools configuration

The tools configuration controls which tools are available to the custom agent and how they behave:

tools

Lists all tools the custom agent can potentially use, including built-in tools and MCP server tools

allowedTools

Specifies which tools can run without user confirmation, improving workflow efficiency

toolAliases

Provides alternative names for tools, useful for resolving naming conflicts or creating shortcuts

toolsSettings

Configures specific behavior for individual tools, such as allowed file paths or service permissions

### Built-in tool settings

Built-in tools can be configured through the `toolsSettings` section to control their behavior and permissions. Each tool supports specific configuration options that allow you to pre-approve certain operations or restrict access to specific resources.

#### execute_bash tool

Controls which bash commands can be executed without user confirmation:

```
{
  "toolsSettings": {
    "execute_bash": {
      "allowedCommands": ["git status", "git fetch"],
      "deniedCommands": ["git commit .*", "git push .*"],
      "allowReadOnly": true
    }
  }
}
```

allowedCommands

Array of specific commands allowed without prompting. Supports regex formatting with anchors `\A` and `\z`.

deniedCommands

Array of commands to deny. Supports regex formatting. Deny rules are evaluated before allow rules.

allowReadOnly

Boolean (default: `true`) - Whether to allow read-only commands without prompting.

#### fs_read tool

Controls which files and directories can be read without user confirmation:

```
{
  "toolsSettings": {
    "fs_read": {
      "allowedPaths": ["~/projects", "./src/**"],
      "deniedPaths": ["/some/denied/path/", "/another/denied/path/**/file.txt"]
    }
  }
}
```

allowedPaths

Array of paths that can be read without prompting. Supports glob patterns with gitignore-style behavior.

deniedPaths

Array of paths to deny access. Supports glob patterns. Deny rules are evaluated before allow rules.

#### fs_write tool

Controls which files and directories can be written to without user confirmation:

```
{
  "toolsSettings": {
    "fs_write": {
      "allowedPaths": ["~/projects/output.txt", "./src/**"],
      "deniedPaths": ["/some/denied/path/", "/another/denied/path/**/file.txt"]
    }
  }
}
```

allowedPaths

Array of paths that can be written to without prompting. Supports glob patterns with gitignore-style behavior.

deniedPaths

Array of paths to deny write access. Supports glob patterns. Deny rules are evaluated before allow rules.

#### use_aws tool

Controls which AWS services can be accessed without user confirmation:

```
{
  "toolsSettings": {
    "use_aws": {
      "allowedServices": ["s3", "lambda", "ec2"],
      "deniedServices": ["eks", "rds"]
    }
  }
}
```

allowedServices

Array of AWS services that can be accessed without prompting.

deniedServices

Array of AWS services to deny access. Deny rules are evaluated before allow rules.

#### Tool permissions and defaults

Built-in tools have different default permission behaviors:

- **Trusted by default:** `fs_read`, `report_issue`
- **Require permission by default:** `execute_bash`, `fs_write`, `use_aws`
- **No configuration options:** `introspect`, `knowledge`, `thinking`, `todo_list`

Tools can be explicitly allowed in the `allowedTools` section, or configured with specific permissions through `toolsSettings`. If a tool is not in the `allowedTools` list, users will be prompted for permission unless an appropriate `toolsSettings` configuration is set.

### MCP servers configuration

The `mcpServers` section defines which Model Context Protocol servers the custom agent can access. Each server configuration includes:

- **Command** - The executable command to start the MCP server
- **Arguments** - Command-line arguments for the server
- **Environment variables** - Environment settings for the server process
- **Timeout settings** - Request timeout configuration

For more information about MCP integration, see [Using MCP with Amazon Q Developer](qdev-mcp.md "qdev-mcp.md").

### Resources and context

Custom agents can automatically include relevant context through two mechanisms:

resources

Files and directories to include in the custom agent's context, supporting glob patterns for flexible file selection

hooks

Commands to run at specific trigger points (like custom agent startup or user input), with output included in context

## Common configuration patterns

### Minimal custom agent configuration

A simple custom agent that provides basic file operations with pre-approved read access:

```
{
"name": "basic-ops",
  "description": "Basic file operations custom agent",
  "prompt": "You are a helpful assistant specialized in basic file operations",
  "tools": [
    "fs_read",
    "fs_write",
    "execute_bash"
  ],
  "allowedTools": [
    "fs_read"
  ]
}
```

### Specialized workflow custom agent

An custom agent configured for AWS infrastructure management with specific tool permissions:

```
{
"name": "infra-manage",
  "description": "AWS infrastructure management custom agent",
  "prompt": "You are an expert AWS infrastructure specialist",
  "tools": [
    "fs_read",
    "fs_write",
    "execute_bash",
    "use_aws"
  ],
  "allowedTools": [
    "fs_read",
    "use_aws"
  ],
  "toolsSettings": {
    "use_aws": {
      "allowedServices": ["s3", "lambda", "cloudformation"]
    }
  },
  "resources": [
    "file://README.md",
    "file://infrastructure/**/*.yaml",
    "file://docs/deployment.md"
  ]
}
```

### Project-specific custom agent with hooks

An custom agent that includes project context through both static files and dynamic commands:

```
{
  "name": "project-dev",
  "description": "Project development custom agent with git context",
  "prompt": "You are a project development assistant with access to git information",
  "tools": [
    "fs_read",
    "fs_write",
    "execute_bash",
    "@git"
  ],
  "allowedTools": [
    "fs_read",
    "@git/git_status"
  ],
  "resources": [
    "file://README.md",
    "file://CONTRIBUTING.md",
    "file://src/**/*.md"
  ],
  "hooks": {
    "agentSpawn": [
      {
        "command": "git status --porcelain",
        "timeout_ms": 10000
      }
    ]
  }
}
```

### Custom agent with MCP server integration

An custom agent that integrates external tools through MCP servers:

```
{
"name": "custom-dev",
  "description": "Development custom agent with external tool integration",
  "prompt": "You are a development assistant with access to git and web fetching capabilities",
  "mcpServers": {
    "git": {
      "command": "git-mcp-server",
      "args": [],
      "timeout": 30000
    },
    "fetch": {
      "command": "fetch-mcp-server",
      "args": ["--timeout", "10"]
    }
  },
  "tools": [
    "fs_read",
    "fs_write",
    "@git",
    "@fetch/fetch_url"
  ],
  "allowedTools": [
    "fs_read",
    "@git/git_status",
    "@fetch/fetch_url"
  ],
  "toolAliases": {
    "@git/git_status": "status",
    "@fetch/fetch_url": "get"
  }
}
```

## Agent hooks

Agent hooks automatically execute shell commands at specific trigger points and include their output as context. This enables agents to gather dynamic information about your environment.

### Hook triggers

Q Developer supports two hook triggers:

agentSpawn

Runs once when the agent is initialized. Output is added to the conversation context and persists throughout the session.

userPromptSubmit

Runs with each user message. Output is added only to the current prompt, providing fresh context for each interaction.

### Hook configuration

Configure hooks in your agent's JSON file:

```
{
  "hooks": {
    "agentSpawn": [
      {
        "command": "git branch --show-current"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "git status --porcelain",
        "timeout_ms": 5000,
        "cache_ttl_seconds": 30
      }
    ]
  }
}
```

Each hook supports these properties:

command

The shell command to execute (required)

timeout_ms

Maximum execution time in milliseconds (default: 30000)

max_output_size

Maximum output size in bytes before truncation (default: 10240)

cache_ttl_seconds

How long to cache output before re-executing (default: 0 - no caching)

### Hook examples

#### Git development assistant

Automatically include git repository status with each prompt:

```
{
  "name": "Git Assistant",
  "hooks": {
    "agentSpawn": [
      {
        "command": "git branch --show-current"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "git status --porcelain"
      }
    ]
  }
}
```

#### Project context agent

Gather project information at startup and current directory contents per prompt:

```
{
  "name": "Project Assistant",
  "hooks": {
    "agentSpawn": [
      {
        "command": "echo \"Project: $(basename $(pwd))\""
      },
      {
        "command": "find . -name '*.json' -maxdepth 1"
      }
    ],
    "userPromptSubmit": [
      {
        "command": "ls -la",
        "cache_ttl_seconds": 60
      }
    ]
  }
}
```
