# Chat commands

Amazon Q supports several commands that you can use during a chat session. These
commands start with a forward slash (`/`).

| Chat commands          | Command                                                                                            | Description |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| `/load`                | Import conversation state from a JSON file                                                         |
| `/save`                | Export conversation state to a JSON file                                                           |
| `/prompts`             | Lists all available prompts                                                                        |
| `/usage`               | Displays an estimate of the context window usage                                                   |
| `!`                    | Executes a shell command from inside an Amazon Q CLI session                                       |
| `ctrl-j`               | Allows multi-line input                                                                            |
| `ctrl-k`               | Fuzzy search                                                                                       |
| `/editor`              | Uses the configured editor to compose prompts                                                      |
| `/help`                | Displays a list of available commands                                                              |
| `/issue`               | Reports an issue or make a feature request                                                         |
| `/model`               | Displays available models and allows you to select one for your current chat session               |
| `/quit`                | Exits the chat session                                                                             |
| `/clear`               | Clears the chat history from the current session                                                   |
| `/tools`               | Manages tools and permissions for tools that Amazon Q can use                                      |
| `/mcp`                 | Manages authentication and connection to remote MCP servers                                        |
| `/acceptall`           | Deprecated. Disables confirmation prompts when Amazon Q performs<br>actions on your system         |
| `/profile`             | Deprecated. Manages Q profiles for Q Developer commands. Use `/agent` instead                      |
| `/context`             | Manages the context information available to Amazon Q                                              |
| `/compact`             | Compacts the conversation history and shows the output of the<br>compacted conversation history    |
| `/agent list`          | Shows all available agents in your environment                                                     |
| `/agent schema`        | Displays the JSON schema for creating agent configuration files                                    |
| `/agent create [name]` | Creates a new agent with the specified name                                                        |
| `/agent use [name]`    | Switches to using a specific agent for the current session                                         |
| `/agent edit [name]`   | Opens the agent configuration file for editing                                                     |
| `/experiment`          | Manages experimental features (requires enabling)                                                  |
| `/knowledge`           | Manages persistent knowledge base (experimental feature)                                           |
| `/tangent`             | Creates conversation checkpoints for exploring side topics (experimental feature)                  |
| `/tangent tail`        | Preserves the last tangent conversation, maintaining context from your previous tangent discussion |
| `/changelog`           | Displays information about the latest Amazon Q Developer CLI updates                               |
