# Defining a custom agent

This section covers how to create and use custom agents in your Amazon Q Developer CLI workflow.

## Creating your first custom agent

Here's a step-by-step walkthrough to create your first custom agent:

1. Start a Amazon Q Developer CLI chat session:

```
$ q chat
```

2. List existing agents to see what's available:

```
/agent list
```

3. Create a new agent (replace `my-agent` with your preferred name):

```
/agent create --name my-agent
```

This creates a new agent configuration file in `~/.aws/amazonq/cli-agents` by default, and opens it in your default editor (set via the `EDITOR` environment variable). 4. Customize the custom agent configuration as needed. For a simple start, you might want to:

    * Add a description explaining the custom agent's purpose
    * Specify which tools should be available
    * Pre-approve tools you use frequently

5. Save the configuration file and exit your editor to return to the chat session.
6. Start a new chat session with your custom agent:

```
$ q chat --agent my-agent
```

**Note:** You cannot switch custom agents within an existing chat session. Custom agent changes require starting a new session. 7. Test your custom agent by asking it to perform tasks using the tools you've configured.

For detailed information about custom agent configuration options, see [Configuration reference](command-line-custom-agents-configuration.md "command-line-custom-agents-configuration.md").

## Custom agent commands

Amazon Q Developer CLI provides several commands for managing custom agents. These commands are available during a chat session and start with `/agent`.

| Custom agent commands         | Command                                                                           | Description  | Availability |
| ----------------------------- | --------------------------------------------------------------------------------- | ------------ | ------------ |
| `/agent list`                 | Shows all available custom agents in your environment                             | Chat session |
| `/agent schema`               | Displays the JSON schema for creating custom agent configuration files            | Chat session |
| `/agent create --name [name]` | Creates a new custom agent configuration file and opens it in your default editor | Chat session |

**Note:** Some custom agent management operations require manual file editing rather than interactive commands. Custom agent changes take effect when you start a new chat session.

## Migration from legacy profiles

When you update to a version of Amazon Q Developer CLI that supports agents and sign in, you may be prompted to migrate your legacy profiles to agents if:

- You have existing legacy profile configurations
- You're running in interactive mode (migration is skipped with `--no-interactive`)
- You haven't previously completed the migration process

The migration process:

- Converts existing profile configurations to the new agent format
- Preserves your existing tool permissions and context settings
- Creates agent configuration files in your home directory
- Maintains backward compatibility with your existing workflows

The migration is optional and can be declined. If you choose not to migrate, you can continue using the default agent or create new agents manually. To control migration behavior, use the `--no-interactive` flag to skip migration prompts entirely.

## Using the default agent vs custom agents

Amazon Q Developer CLI includes a built-in default agent that provides access to all tools with minimal pre-approved permissions. This default agent:

- Includes all available tools (built-in and MCP)
- Pre-approves only the `fs_read` tool for security
- Automatically includes common project files like `README.md` and `AmazonQ.md`
- Uses legacy MCP configuration if available

Custom agents allow you to:

- Limit tool access to only what you need
- Pre-approve additional tools to reduce interruptions
- Include specific project documentation and context files
- Configure tool behavior for your specific use case
