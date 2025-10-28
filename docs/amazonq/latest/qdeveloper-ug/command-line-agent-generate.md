# Creating agents with AI assistance (/agent generate)

The `/agent generate` command uses AI to intelligently create custom agent configurations. This is the recommended approach for creating new agents, as it leverages Amazon Q Developer's understanding of your requirements to generate appropriate configurations.

## Prerequisites

- Amazon Q Developer CLI installed and configured
- Default text editor configured (set `EDITOR` environment variable or ensure `vi` is available)
- Write permissions to workspace directory (for local agents) or home directory (for global agents)

## Usage

```
/agent generate
```

## How it works

1. **Interactive prompts**: After running the command, Q Developer prompts for agent name, description, scope (local/global), and MCP server selection
2. **AI generation**: Q Developer analyzes your requirements and generates an appropriate JSON configuration
3. **Editor opens**: The generated configuration opens in your default editor for review and refinement
4. **Validation**: Q Developer validates the JSON schema when you save and close the editor
5. **Agent creation**: The validated agent is saved and ready for use

## Storage locations

Local agents (default)

`.amazonq/cli-agents/`agent-name`.json`

Global agents (selected via prompt)

`~/.aws/amazonq/cli-agents/`agent-name`.json`

## Example workflow

```
# Start agent generation
/agent generate

# Q Developer prompts for agent name
Enter agent name: my-dev-agent

# Q Developer prompts for description
Enter agent description: I need an agent that helps with Python development, includes linting tools, and can access my project documentation

# Q Developer prompts for scope selection
Agent scope
> Local (current workspace)
  Global (all workspaces)

# Q Developer generates configuration and opens editor
Generating agent configuration...
Opening editor for review...

# After saving and closing editor
Agent 'my-dev-agent' created successfully at .amazonq/cli-agents/my-dev-agent.json
```

## Editor configuration

The command uses your system's default editor:

- Uses `EDITOR` environment variable if set
- Falls back to `vi` if no editor is configured

## Error handling

Invalid JSON

Configuration is rejected with clear error messages

Editor failures

Graceful handling with informative error messages

File system errors

Clear reporting of permission or path issues

## Related commands

- `/agent create` - Manual agent creation approach
- `/agent list` - View available agents
- `/agent schema` - View agent configuration schema

## Best practices

- Provide detailed, specific requirements when describing your agent needs
- Review and customize the generated configuration before saving
- Test your new agent with simple tasks before complex workflows
- Use descriptive agent names that reflect their purpose
