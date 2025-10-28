# Built-in tools

Amazon Q Developer CLI includes several built-in tools that agents can use to perform various tasks. This section describes the most commonly used tools and their configuration options.

## Available tools

The following built-in tools are available:

- `fs_read` - Read files, directories, and images
- `fs_write` - Create and edit files
- `execute_bash` - Execute shell commands
- `use_aws` - Make AWS CLI API calls
- `knowledge` - Store and retrieve information across sessions
- `introspect` - Provide information about Q CLI capabilities

## File reading (fs_read)

The `fs_read` tool allows Amazon Q to read files, directories, and images. This tool is trusted by default.

### Configuration

You can configure which paths are allowed or denied:

```
{
  "toolsSettings": {
    "fs_read": {
      "allowedPaths": ["~/projects", "./src/**"],
      "deniedPaths": ["/etc/**", "~/.ssh/**"]
    }
  }
}
```

- `allowedPaths` - Paths that can be read without prompting. Supports glob patterns.
- `deniedPaths` - Paths that are denied. Deny rules are evaluated before allow rules.

## File writing (fs_write)

The `fs_write` tool allows Amazon Q to create and edit files. This tool prompts for permission by default.

### Configuration

You can configure which paths are allowed for writing:

```
{
  "toolsSettings": {
    "fs_write": {
      "allowedPaths": ["~/projects/output.txt", "./src/**"],
      "deniedPaths": ["/system/**", "~/.config/**"]
    }
  }
}
```

- `allowedPaths` - Paths that can be written to without prompting. Supports glob patterns.
- `deniedPaths` - Paths that are denied for writing.

## Command execution (execute_bash)

The `execute_bash` tool allows Amazon Q to execute shell commands. This tool prompts for permission by default.

### Configuration

You can configure which commands are allowed or denied:

```
{
  "toolsSettings": {
    "execute_bash": {
      "allowedCommands": ["git status", "git fetch"],
      "deniedCommands": ["git commit .*", "git push .*"],
      "autoAllowReadonly": true
    }
  }
}
```

- `allowedCommands` - Commands that are allowed without prompting. Supports regex patterns.
- `deniedCommands` - Commands that are denied. Evaluated before allow rules.
- `autoAllowReadonly` - Whether to allow read-only commands without prompting.

## AWS API calls (use_aws)

The `use_aws` tool allows Amazon Q to make AWS CLI API calls. This tool prompts for permission by default.

### Configuration

You can configure which AWS services are allowed:

```
{
  "toolsSettings": {
    "use_aws": {
      "allowedServices": ["s3", "lambda", "ec2"],
      "deniedServices": ["eks", "rds"],
      "autoAllowReadonly": true
    }
  }
}
```

- `allowedServices` - AWS services that can be accessed without prompting.
- `deniedServices` - AWS services to deny access to.
- `autoAllowReadonly` - Whether to allow read-only operations (get, describe, list) without prompting.

## Tool permissions

Tools can be explicitly allowed in the `allowedTools` section of your agent configuration:

```
{
  "allowedTools": [
    "fs_read",
    "knowledge",
    "use_aws"
  ]
}
```

Default permission behaviors:

- `fs_read` and `report_issue` are trusted by default
- `execute_bash`, `fs_write`, and `use_aws` prompt for permission by default
- Tools not in `allowedTools` will prompt for permission unless configured with appropriate `toolsSettings`

## Complete example

Here's an example agent configuration with tool settings:

```
{
  "name": "development-assistant",
  "description": "Agent for development tasks with restricted tool access",
  "allowedTools": ["fs_read", "fs_write", "execute_bash"],
  "toolsSettings": {
    "fs_read": {
      "allowedPaths": ["~/projects/**"],
      "deniedPaths": ["~/.ssh/**", "/etc/**"]
    },
    "fs_write": {
      "allowedPaths": ["~/projects/**"],
      "deniedPaths": ["~/projects/production/**"]
    },
    "execute_bash": {
      "allowedCommands": ["git status", "git diff", "npm test"],
      "deniedCommands": ["git push .*", "rm -rf .*"],
      "autoAllowReadonly": true
    }
  }
}
```

## Security improvements

Recent security improvements include:

- **fs_read**: Default trust permission now limited to current working directory only
- **execute_bash**: `autoAllowReadonly` now defaults to `false` for enhanced security
- **use_aws**: New `autoAllowReadonly` setting available for configuration

Configure these settings in your agent's `toolsSettings` section as needed.
