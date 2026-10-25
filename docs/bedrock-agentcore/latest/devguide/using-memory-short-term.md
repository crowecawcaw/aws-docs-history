

# Use short-term memory
<a name="using-memory-short-term"></a>

In your AI agent, you write code to add events to [short-term memory](memory-types.md#short-term-memory) in an AgentCore Memory. These events are stored as short-term memory. They form the foundation for structured information extraction into long-term memory.

The following section discusses short-term memory with the AWS SDK. For examples that use the [Amazon Bedrock AgentCore samples repository](https://github.com/awslabs/amazon-bedrock-agentcore-samples) and the AWS SDK, see [Scenario: A customer support AI agent using AgentCore Memory](memory-customer-scenario.md) . For other SDKs see [Amazon Bedrock AgentCore Memory examples](memory-examples.md).

## Inspect memory with the AgentCore CLI
<a name="_inspect_memory_with_the_agentcore_cli"></a>

The AgentCore CLI provides commands for inspecting deployed memories and their data. Use event commands for short-term memory and record commands for long-term memory.

```
# List memories and inspect one memory
agentcore memory list

agentcore memory get --id <memory-id>

# Discover actors and sessions
agentcore memory actor list --id <memory-id>

agentcore memory session list \
  --id <memory-id> \
  --actor-id <actor-id>

# List or get short-term memory events
agentcore memory event list \
  --id <memory-id> \
  --actor-id <actor-id> \
  --session-id <session-id>

agentcore memory event get \
  --id <memory-id> \
  --actor-id <actor-id> \
  --session-id <session-id> \
  --event-id <event-id>

# List or get long-term memory records
agentcore memory record list \
  --id <memory-id> \
  --namespace-path /

agentcore memory record get \
  --id <memory-id> \
  --record-id <record-id>
```

**Topics**