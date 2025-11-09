# Configure Amazon Q settings

Amazon Q provides various ways to customize its behavior through settings. You can access these settings through both a graphical interface and command-line options.

## Access settings

You can access Amazon Q settings in two ways:

- Settings GUI: Run `q settings` to open the graphical settings interface
- Command line: Use various commands to view and modify settings directly

## Manage settings from the command line

You can manage Amazon Q settings directly from the command line using the following commands:

| Basic settings commands                | Command                                        | Description |
| -------------------------------------- | ---------------------------------------------- | ----------- |
| `q settings open`                      | Opens the settings file in your default editor |
| `q settings list`                      | Lists all configured settings                  |
| `q settings list --all`                | Lists all available settings with descriptions |
| `q settings list --format json-pretty` | Lists settings in formatted JSON               |
| `q settings [KEY]`                     | Views the value of a specific setting          |
| `q settings [KEY] [VALUE]`             | Sets a specific setting to the given value     |
| `q settings --delete [KEY]`            | Deletes a specific setting                     |

When using `q settings` commands, you can specify the output format:

```
q settings --format [FORMAT]
```

Available formats:

- `plain`: Outputs results as plain text (default)
- `json`: Outputs results as JSON
- `json-pretty`: Outputs results as formatted JSON

## Available settings reference

The following sections describe all available Amazon Q CLI settings, organized by category. Each setting includes its key name, description, expected value type, and examples.

### Telemetry and privacy settings

| Telemetry and privacy settings                   | Setting Key                              | Description | Type                                                              | Example |
| ------------------------------------------------ | ---------------------------------------- | ----------- | ----------------------------------------------------------------- | ------- |
| `telemetry.enabled`                              | Enable/disable telemetry collection      | boolean     | `q settings telemetry.enabled true`                               |
| `telemetryClientId`                              | Legacy client identifier for telemetry   | string      | `q settings telemetryClientId "client-123"`                       |
| `codeWhisperer.shareCodeWhispererContentWithAWS` | Share content with CodeWhisperer service | boolean     | `q settings codeWhisperer.shareCodeWhispererContentWithAWS false` |

### Chat interface settings

| Chat interface settings            | Setting Key                                  | Description | Type                                               | Example |
| ---------------------------------- | -------------------------------------------- | ----------- | -------------------------------------------------- | ------- |
| `chat.enableThinking`              | Enable thinking tool for complex reasoning   | boolean     | `q settings chat.enableThinking true`              |
| `chat.greeting.enabled`            | Show greeting message on chat start          | boolean     | `q settings chat.greeting.enabled false`           |
| `chat.editMode`                    | Enable edit mode for chat interface          | boolean     | `q settings chat.editMode true`                    |
| `chat.enableNotifications`         | Enable desktop notifications                 | boolean     | `q settings chat.enableNotifications true`         |
| `chat.defaultModel`                | Default AI model for conversations           | string      | `q settings chat.defaultModel "claude-3-sonnet"`   |
| `chat.disableMarkdownRendering`    | Disable markdown formatting in chat          | boolean     | `q settings chat.disableMarkdownRendering false`   |
| `chat.defaultAgent`                | Default agent configuration                  | string      | `q settings chat.defaultAgent "my-agent"`          |
| `chat.disableAutoCompaction`       | Disable automatic conversation summarization | boolean     | `q settings chat.disableAutoCompaction true`       |
| `chat.enableHistoryHints`          | Show conversation history hints              | boolean     | `q settings chat.enableHistoryHints true`          |
| `chat.uiMode`                      | Specify UI variant to use                    | string      | `q settings chat.uiMode "compact"`                 |
| `chat.enableContextUsageIndicator` | Show context usage percentage in prompt      | boolean     | `q settings chat.enableContextUsageIndicator true` |

### Knowledge base settings

| Knowledge base settings            | Setting Key                                          | Description | Type                                                                      | Example |
| ---------------------------------- | ---------------------------------------------------- | ----------- | ------------------------------------------------------------------------- | ------- |
| `chat.enableKnowledge`             | Enable knowledge base functionality                  | boolean     | `q settings chat.enableKnowledge true`                                    |
| `knowledge.defaultIncludePatterns` | Default file patterns to include in knowledge base   | array       | `q settings knowledge.defaultIncludePatterns '["*.py", "*.js"]'`          |
| `knowledge.defaultExcludePatterns` | Default file patterns to exclude from knowledge base | array       | `q settings knowledge.defaultExcludePatterns '["*.log", "node_modules"]'` |
| `knowledge.maxFiles`               | Maximum number of files for knowledge indexing       | number      | `q settings knowledge.maxFiles 1000`                                      |
| `knowledge.chunkSize`              | Text chunk size for knowledge processing             | number      | `q settings knowledge.chunkSize 512`                                      |
| `knowledge.chunkOverlap`           | Overlap between text chunks                          | number      | `q settings knowledge.chunkOverlap 50`                                    |
| `knowledge.indexType`              | Type of knowledge index to use                       | string      | `q settings knowledge.indexType "fast"`                                   |

### Key bindings

| Key binding settings     | Setting Key                                    | Description | Type                                      | Example |
| ------------------------ | ---------------------------------------------- | ----------- | ----------------------------------------- | ------- |
| `chat.skimCommandKey`    | Key binding for fuzzy search command           | char        | `q settings chat.skimCommandKey "f"`      |
| `chat.autocompletionKey` | Key binding for autocompletion hint acceptance | char        | `q settings chat.autocompletionKey "Tab"` |
| `chat.tangentModeKey`    | Key binding for tangent mode toggle            | char        | `q settings chat.tangentModeKey "t"`      |
| `chat.delegateModeKey`   | Key binding for delegate command               | char        | `q settings chat.delegateModeKey "d"`     |

### Feature toggles

| Feature toggle settings  | Setting Key                                      | Description | Type                                     | Example |
| ------------------------ | ------------------------------------------------ | ----------- | ---------------------------------------- | ------- |
| `chat.enableTangentMode` | Enable tangent mode feature                      | boolean     | `q settings chat.enableTangentMode true` |
| `introspect.tangentMode` | Auto-enter tangent mode for introspect questions | boolean     | `q settings introspect.tangentMode true` |
| `chat.enableTodoList`    | Enable the todo list feature                     | boolean     | `q settings chat.enableTodoList true`    |
| `chat.enableCheckpoint`  | Enable the checkpoint feature                    | boolean     | `q settings chat.enableCheckpoint true`  |
| `chat.enableDelegate`    | Enable the delegate tool for subagent management | boolean     | `q settings chat.enableDelegate true`    |

### API and service settings

| API and service settings    | Setting Key                        | Description | Type                                                                                   | Example |
| --------------------------- | ---------------------------------- | ----------- | -------------------------------------------------------------------------------------- | ------- |
| `api.timeout`               | API request timeout in seconds     | number      | `q settings api.timeout 30`                                                            |
| `api.codewhisperer.service` | CodeWhisperer service endpoint URL | string      | `q settings api.codewhisperer.service "https://codewhisperer.us-east-1.amazonaws.com"` |
| `api.q.service`             | Q service endpoint URL             | string      | `q settings api.q.service "https://q.us-east-1.amazonaws.com"`                         |

### Model Context Protocol settings

| MCP settings               | Setting Key                         | Description | Type                                    | Example |
| -------------------------- | ----------------------------------- | ----------- | --------------------------------------- | ------- |
| `mcp.initTimeout`          | MCP server initialization timeout   | number      | `q settings mcp.initTimeout 10`         |
| `mcp.noInteractiveTimeout` | Non-interactive MCP timeout         | number      | `q settings mcp.noInteractiveTimeout 5` |
| `mcp.loadedBefore`         | Track previously loaded MCP servers | boolean     | `q settings mcp.loadedBefore true`      |

## Common settings examples

Here are some common configuration scenarios:

### Basic configuration

```
# Enable telemetry
q settings telemetry.enabled true

# Set default chat model
q settings chat.defaultModel "claude-3-sonnet"

# Disable greeting message
q settings chat.greeting.enabled false
```

### Knowledge base configuration

```
# Enable knowledge base
q settings chat.enableKnowledge true

# Set file patterns to include
q settings knowledge.defaultIncludePatterns '["*.py", "*.js", "*.md", "*.txt"]'

# Set file patterns to exclude
q settings knowledge.defaultExcludePatterns '["*.log", "node_modules", ".git", "*.pyc"]'

# Set maximum files to index
q settings knowledge.maxFiles 2000
```

### Feature configuration

```
# Enable experimental features
q settings chat.enableThinking true
q settings chat.enableTangentMode true
q settings chat.enableTodoList true
q settings chat.enableCheckpoint true

# Configure key bindings
q settings chat.tangentModeKey "t"
q settings chat.delegateModeKey "d"
```

### Viewing and managing settings

```
# View all configured settings
q settings list

# View all available settings with descriptions
q settings list --all

# View specific setting
q settings chat.defaultModel

# Export settings as JSON
q settings list --format json-pretty > my-settings.json

# Delete a setting
q settings --delete chat.defaultModel
```

## Troubleshooting settings

Common issues and solutions when working with settings:

### Invalid setting values

If you encounter errors when setting values:

- **Boolean values**: Use `true` or `false` (lowercase)
- **Array values**: Use JSON format with single quotes: `'["item1", "item2"]'`
- **String values**: Use quotes for strings with spaces: `"my value"`

### Resetting settings

To reset settings to defaults:

```
# Delete individual settings
q settings --delete setting.name

# Open settings file for manual editing
q settings open

# View current settings to identify issues
q settings list --all
```

### Settings file issues

If the settings file becomes corrupted:

1. Back up current settings: `q settings list --format json > backup.json`
2. Open the settings file: `q settings open`
3. Verify JSON syntax or restore from backup

## Other Amazon Q CLI commands

Amazon Q offers many other command-line features beyond settings management. For a comprehensive reference of all available commands and their arguments, see [Amazon Q CLI Command Reference](command-line-reference.md "command-line-reference.md").

For help with any command, use the `--help` flag:

```
q [COMMAND] --help
```
