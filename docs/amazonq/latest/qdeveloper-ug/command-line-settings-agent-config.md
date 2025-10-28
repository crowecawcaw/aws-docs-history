# Agent-related settings

The `chat.defaultAgent` setting determines which agent Amazon Q Developer CLI uses when no specific agent is provided via the `--agent` flag.

## Examples

```
# Set a custom agent as default
q settings chat.defaultAgent my-dev-agent

# View current default agent
q settings chat.defaultAgent

# Reset to built-in default
q settings chat.defaultAgent ""
```

## Agent selection priority

1. **Command-line**: `q chat --agent specific-agent`
2. **User setting**: Value of `chat.defaultAgent`
3. **Built-in default**: Fallback agent with basic configuration
