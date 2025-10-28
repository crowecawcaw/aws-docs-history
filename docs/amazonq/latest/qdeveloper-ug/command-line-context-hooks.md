# Context hooks (deprecated)

###### Warning

Context hooks are deprecated. Use [agent hooks](command-line-custom-agents-configuration.md#command-line-agent-hooks "command-line-custom-agents-configuration.md#command-line-agent-hooks") instead for new configurations.

Existing context hook configurations are automatically migrated to agent files but require manual activation:

- Global context hooks are migrated to an agent named `migrated_agent_from_global_context`
- Profile-specific context hooks are migrated to agents named after each profile
  To use migrated configurations, select the appropriate agent:

```
q chat --agent migrated_agent_from_global_context
```

For new hook configurations, see [Agent Hooks](command-line-custom-agents-configuration.md#command-line-agent-hooks "command-line-custom-agents-configuration.md#command-line-agent-hooks").
