# Amazon Q CLI Command Reference

This section provides a comprehensive reference for all Amazon Q Developer CLI commands and their arguments. Use this reference to understand the available options for each command and their proper syntax.

For help with any command, you can use the `--help` flag:

```
q [COMMAND] --help
```

## Global Arguments

The following arguments are available with any Amazon Q CLI command:

| Global arguments | Argument | Short form                                                                                        | Description |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------- | ----------- |
| `--verbose`      | `-v`     | Increase logging verbosity. Can be repeated for more verbose output: `-v`, `-vv`, `-vvv`, `-vvvv` |
| `--help`         | `-h`     | Show help information for the command                                                             |
| `--version`      | `-V`     | Show version information                                                                          |
| `--help-all`     |          | Print help for all subcommands                                                                    |

## Commands

The following sections describe each Amazon Q CLI command and its available arguments.

### q chat

Start an interactive chat session with Amazon Q. When no subcommand is specified, `q` defaults to `q chat`.

**Syntax:**

```
q chat [OPTIONS] [INPUT]
```

| q chat arguments    | Argument | Short form                                                                                                                                                              | Description |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `--no-interactive`  |          | Print the first response to STDOUT without interactive mode. This will fail if the prompt requests permissions to use a tool, unless `--trust-all-tools` is also used   |
| `--resume`          | `-r`     | Resume the previous conversation from this directory                                                                                                                    |
| `--agent`           |          | Agent to use                                                                                                                                                            |
| `--trust-all-tools` |          | Allow the model to use any tool to run commands without asking for confirmation                                                                                         |
| `--trust-tools`     |          | Trust only the specified set of tools. Provide a comma-separated list of tool names. Example: `--trust-tools=fs_read,fs_write`. To trust no tools, use `--trust-tools=` |
| `INPUT`             |          | The first question to ask (positional argument)                                                                                                                         |

**Examples:**

```
q chat
q chat "How do I list files in Linux?"
q chat --no-interactive --trust-all-tools "Show me the current directory"
q chat --resume
q chat --agent my-agent "Help me with AWS CLI"
```

### q translate

Translate natural language instructions to executable shell commands using AI.

**Syntax:**

```
q translate [OPTIONS] [INPUT...]
```

| q translate arguments | Argument | Short form                                                                              | Description |
| --------------------- | -------- | --------------------------------------------------------------------------------------- | ----------- |
| `--n`                 | `-n`     | Number of completions to generate (must be ≤5)                                          |
| `INPUT`               |          | Natural language description of the command you want to generate (positional arguments) |

**Examples:**

```
q translate "list all files in the current directory"
q translate "find all Python files modified in the last week"
q translate "compress all log files older than 30 days"
```

### q doctor

Fix and diagnose common installation and configuration issues with Amazon Q.

**Syntax:**

```
q doctor [OPTIONS]
```

| q doctor arguments | Argument | Short form                          | Description |
| ------------------ | -------- | ----------------------------------- | ----------- |
| `--all`            | `-a`     | Run all doctor tests, with no fixes |
| `--strict`         | `-s`     | Error on warnings                   |

**Examples:**

```
q doctor
q doctor --all
q doctor --strict
```

### q update

Update the Amazon Q application to the latest version.

**Syntax:**

```
q update [OPTIONS]
```

| q update arguments     | Argument | Short form                                            | Description |
| ---------------------- | -------- | ----------------------------------------------------- | ----------- |
| `--non-interactive`    | `-y`     | Don't prompt for confirmation                         |
| `--relaunch-dashboard` |          | Relaunch into dashboard after update. Default is true |
| `--rollout`            |          | Uses rollout                                          |

**Examples:**

```
q update
q update --non-interactive
q update --rollout
```

### q theme

Get or set the visual theme for the autocomplete dropdown menu. This affects the appearance of the popup window that shows command completions.

**Syntax:**

```
q theme [OPTIONS] [THEME]
```

| q theme arguments | Argument                                                                                           | Description |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| `--list`          | List all available themes                                                                          |
| `--folder`        | Show the theme directory path                                                                      |
| `THEME`           | Name of the theme to set. Built-in themes include: `dark`, `light`, `system` (positional argument) |

**Examples:**

```
q theme --list
q theme --folder
q theme dark
q theme light
q theme system
```

**Note:** Theme changes affect the autocomplete popup window. You may need to trigger autocomplete suggestions to see the visual changes.

### q integrations

Manage system integrations for Amazon Q.

**Syntax:**

```
q integrations [SUBCOMMAND] [OPTIONS]
```

#### q integrations subcommands

| q integrations subcommands | Subcommand                                                                        | Description |
| -------------------------- | --------------------------------------------------------------------------------- | ----------- |
| `install`                  | Install an integration. Supports `--silent` ( `-s`) to suppress status messages   |
| `uninstall`                | Uninstall an integration. Supports `--silent` ( `-s`) to suppress status messages |
| `reinstall`                | Reinstall an integration. Supports `--silent` ( `-s`) to suppress status messages |
| `status`                   | Check the status of an integration. Supports `--format` ( `-f`) for output format |

### q inline

Manage inline suggestions (ghost text) that appear directly on your command line as you type. For more information, see [Command line assistance features](command-line-assistance.md "command-line-assistance.md")

**Syntax:**

```
q inline [SUBCOMMAND] [OPTIONS]
```

#### q inline subcommands

| q inline subcommands  | Subcommand                                                                           | Description |
| --------------------- | ------------------------------------------------------------------------------------ | ----------- |
| `enable`              | Enable inline suggestions that appear as you type                                    |
| `disable`             | Disable inline suggestions                                                           |
| `status`              | Show whether inline suggestions are enabled or disabled                              |
| `set-customization`   | Select a customization model to use. Optionally specify the ARN of the customization |
| `show-customizations` | Show available customization models. Supports `--format` ( `-f`) for output format   |

**Examples:**

```
q inline enable
q inline disable
q inline status
q inline set-customization
q inline set-customization arn:aws:codewhisperer:us-east-1:123456789012:customization/example
q inline show-customizations
q inline show-customizations --format json
```

### q login

Authenticate with Amazon Q using either AWS Builder ID (free) or IAM Identity Center (Pro).

**Syntax:**

```
q login [OPTIONS]
```

| q login arguments     | Argument                                                                                             | Description |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| `--license`           | License type. Options: `free` (for Builder ID), `pro` (for Identity Center)                          |
| `--identity-provider` | Identity provider URL (for Identity Center)                                                          |
| `--region`            | AWS region (for Identity Center)                                                                     |
| `--use-device-flow`   | Always use the OAuth device flow for authentication. Useful when browser redirects cannot be handled |

**Examples:**

```
q login
q login --license free
q login --license pro --identity-provider https://my-company.awsapps.com/start --region us-east-1
q login --use-device-flow
```

### q logout

Sign out of your Amazon Q session.

**Syntax:**

```
q logout
```

This command takes no additional arguments.

### q whoami

Display information about the current user and authentication status.

**Syntax:**

```
q whoami [OPTIONS]
```

| q whoami arguments | Argument | Short form                                                       | Description |
| ------------------ | -------- | ---------------------------------------------------------------- | ----------- |
| `--format`         | `-f`     | Output format. Options: `plain` (default), `json`, `json-pretty` |

### q profile

Show the profile associated with the current IAM Identity Center user. This command is only available for Pro users.

**Syntax:**

```
q profile
```

This command takes no additional arguments.

### q settings

Manage Amazon Q configuration settings. For detailed information about settings management, see [Configure Amazon Q settings](command-line-settings.md "command-line-settings.md")
.

**Syntax:**

```
q settings [SUBCOMMAND] [OPTIONS] [KEY] [VALUE]
```

| q settings arguments | Argument | Short form                                                       | Description |
| -------------------- | -------- | ---------------------------------------------------------------- | ----------- |
| `--delete`           | `-d`     | Delete a setting                                                 |
| `--format`           | `-f`     | Output format. Options: `plain` (default), `json`, `json-pretty` |
| `KEY`                |          | Setting key (positional argument)                                |
| `VALUE`              |          | Setting value (positional argument)                              |

#### q settings subcommands

| q settings subcommands | Subcommand                                                                                                         | Description |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| `open`                 | Open the settings file in your default editor                                                                      |
| `list`                 | List configured settings. Use `--all` to show all available settings with descriptions. Supports `--format` option |
| `all`                  | (Deprecated) List all current settings. Use `list` instead. Supports `--format` option                             |

### /prompts

Manage reusable prompt templates for chat interactions. For comprehensive information about prompt management and arguments, see [Manage prompts](command-line-prompts.md "command-line-prompts.md").

**Syntax:**

```
/prompts [SUBCOMMAND] [OPTIONS] [NAME] [ARGUMENTS...]
```

| /prompts arguments | Argument                                                 | Description |
| ------------------ | -------------------------------------------------------- | ----------- |
| `NAME`             | Prompt name (for details, create, edit, remove commands) |
| `ARGUMENTS...`     | Arguments to pass to the prompt when using `get` command |

#### /prompts subcommands

| /prompts subcommands                               | Subcommand                                                                        | Description |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | ----------- |
| `list [search-word]`                               | List available prompts, optionally filtered by search word                        |
| `details <name>`                                   | Show detailed information about a prompt including arguments, usage, and examples |
| `get <name> [args...]`                             | Retrieve and execute a prompt with optional arguments                             |
| `create --name <name> [--content text] [--global]` | Create a new prompt. Opens editor if no content provided                          |
| `edit <name> [--global]`                           | Edit an existing prompt in your default editor                                    |
| `remove <name> [--global]`                         | Remove an existing prompt (requires confirmation)                                 |

#### Using prompts in chat

Prompts can be invoked directly in chat using the @ prefix:

```
@<prompt-name> [arguments...]
```

Examples:

```
# Simple prompt without arguments
@code-review

# Prompt with single argument
@debug-help "connection timeout error"

# Prompt with multiple arguments
@aws-deploy "my-service" "production" "us-west-2"

# Server-specific prompt (when ambiguous)
@dev-tools/analyze "performance issue"
```

#### Prompt arguments

Prompts can accept arguments to customize their behavior:

- **Required arguments**: Must be provided, shown as `<arg>`
- **Optional arguments**: Can be omitted, shown as `[arg]`
- **Quoted arguments**: Use quotes for arguments containing spaces

Use `/prompts details <name>` to discover what arguments a prompt accepts.

### q diagnostic

Run diagnostic tests to troubleshoot Amazon Q installation and configuration issues.

**Syntax:**

```
q diagnostic [OPTIONS]
```

| q diagnostic arguments | Argument | Short form                                                       | Description |
| ---------------------- | -------- | ---------------------------------------------------------------- | ----------- |
| `--format`             | `-f`     | Output format. Options: `plain` (default), `json`, `json-pretty` |
| `--force`              |          | Force limited diagnostic output                                  |

### q issue

Create a new GitHub issue for Amazon Q feedback or bug reports.

**Syntax:**

```
q issue [OPTIONS] [DESCRIPTION...]
```

| q issue arguments | Argument | Short form                               | Description |
| ----------------- | -------- | ---------------------------------------- | ----------- |
| `--force`         | `-f`     | Force issue creation                     |
| `DESCRIPTION`     |          | Issue description (positional arguments) |

### q version

Display version information and optionally show the changelog.

**Syntax:**

```
q version [OPTIONS]
```

| q version arguments     | Argument                                                                                                                                        | Description |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `--changelog[=VERSION]` | Show the changelog.<br>Use `--changelog` for current version, `--changelog=all` for all versions, or `--changelog=x.x.x` for a specific version |

### q mcp

Manage Model Context Protocol (MCP) servers. For detailed information about MCP, see [Using MCP with Amazon Q Developer](qdev-mcp.md "qdev-mcp.md")
.

**Syntax:**

```
q mcp [SUBCOMMAND] [OPTIONS]
```

#### q mcp add

Add or replace a configured MCP server.

**Syntax:**

```
q mcp add [OPTIONS]
```

| q mcp add arguments | Argument                                                                                  | Description |
| ------------------- | ----------------------------------------------------------------------------------------- | ----------- |
| `--name`            | Name for the server (required)                                                            |
| `--command`         | The command used to launch the server (required)                                          |
| `--scope`           | Where to add the server. Options: `workspace`, `global`                                   |
| `--env`             | Environment variables to use when launching the server. Format: `key1=value1,key2=value2` |
| `--timeout`         | Server launch timeout in milliseconds                                                     |
| `--force`           | Overwrite an existing server with the same name                                           |

#### q mcp remove

Remove a server from the MCP configuration.

**Syntax:**

```
q mcp remove [OPTIONS]
```

| q mcp remove arguments | Argument                                             | Description |
| ---------------------- | ---------------------------------------------------- | ----------- |
| `--name`               | Name of the server to remove (required)              |
| `--scope`              | Scope to remove from. Options: `workspace`, `global` |

#### q mcp list

List configured MCP servers.

**Syntax:**

```
q mcp list [SCOPE]
```

| q mcp list arguments | Argument                                                            | Description |
| -------------------- | ------------------------------------------------------------------- | ----------- |
| `SCOPE`              | Scope to list. Options: `workspace`, `global` (positional argument) |

#### q mcp import

Import a server configuration from another file.

**Syntax:**

```
q mcp import [OPTIONS] [SCOPE]
```

| q mcp import arguments | Argument                                                                 | Description |
| ---------------------- | ------------------------------------------------------------------------ | ----------- |
| `--file`               | File to import server configuration from (required)                      |
| `--force`              | Overwrite an existing server with the same name                          |
| `SCOPE`                | Scope to import to. Options: `workspace`, `global` (positional argument) |

#### q mcp status

Get the status of a configured MCP server.

**Syntax:**

```
q mcp status [OPTIONS]
```

| q mcp status arguments | Argument                                        | Description |
| ---------------------- | ----------------------------------------------- | ----------- |
| `--name`               | Name of the server to get status for (required) |

## Log files

Amazon Q Developer CLI maintains log files that can be useful for troubleshooting. These logs are stored locally on your machine and are not sent to AWS.

**Log file locations:**

- **macOS**: `$TMPDIR/qlog/`
- **Linux**: `$XDG_RUNTIME_DIR` or `TMPDIR` or `/tmp`

The log level can be controlled by setting the `Q_LOG_LEVEL` environment variable. Valid values are:

- `error`: Only error messages (default)
- `warn`: Warning and error messages
- `info`: Informational, warning, and error messages
- `debug`: Debug, informational, warning, and error messages
- `trace`: All messages including detailed trace information

###### Warning

Log files may contain sensitive information from your conversations and interactions with Amazon Q, including file paths, code snippets, and command outputs. While these logs are stored only on your local machine and are not sent to AWS, you should be cautious when sharing log files with others.

**Example of setting the log level (for debugging purposes):**

```
# For bash/zsh
export Q_LOG_LEVEL=debug
q chat

# For fish
set -x Q_LOG_LEVEL debug
q chat
```
