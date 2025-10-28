# Default agent selection

Amazon Q Developer CLI uses the following priority order to select which agent to use:

1. **Command-line specified agent**: `q chat --agent my-agent`
2. **User-configured default agent**: Set via `q settings chat.defaultAgent agent-name`
3. **Built-in default agent**: Fallback agent with basic configuration

## Setting a default agent

You can configure a custom agent as your default for all chat sessions:

```
q settings chat.defaultAgent my-preferred-agent
```

To delete the setting:

```
q setting chat.defaultAgent --delete
```

## Built-in default agent

When no custom agent is specified or found, Amazon Q Developer CLI uses a built-in default agent with:

- Access to all available tools (`"tools": ["*"]`)
- Only `fs_read` pre-approved (`"allowedTools": ["fs_read"]`)
- Automatic inclusion of legacy MCP configuration (`"useLegacyMcpJson": true`)

## Error messages

When agent fallback occurs, you'll see informative messages:

### Agent not found

```
Error: no agent with name my-agent found. Falling back to user specified default
```

### User default not found

```
Error: user defined default my-default not found. Falling back to in-memory default
```
