# Enable long-term memory

You can enable long-term memory in two ways: by adding strategies when you first [create an AgentCore Memory](memory-create-a-memory-store.md "memory-create-a-memory-store.md"), or by
updating an existing resource to include them.

## Creating a new

memory with long-term strategies

The most direct method is to include strategies when you create a new
AgentCore Memory. After calling `get_or_create_memory`, you must wait for
the AgentCore Memory status to become `ACTIVE` before you can use
it.

###### Example Create a new AgentCore Memory

Starter toolkit CLI

```
agentcore memory create PersonalizedShoppingAgentMemory \
  --region us-west-2 \
  --strategies '[{"userPreferenceMemoryStrategy": {"name": "UserShoppingPreferences", "namespaces": ["/users/{actorId}/preferences/"]}}]' \
  --wait
```

Starter toolkit

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import UserPreferenceStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Create memory resource with user preference strategy
memory = memory_manager.get_or_create_memory(
    name="PersonalizedShoppingAgentMemory",
    strategies=[
        UserPreferenceStrategy(
            name="UserShoppingPreferences",
            namespaces=["/users/{actorId}/preferences/"]
        )
    ]
)

memory_id = memory.get('id')
print(f"Memory resource is now ACTIVE with ID: {memory_id}")



```

## Adding long-term

strategies to an existing AgentCore Memory

To add long-term capabilities to an existing AgentCore Memory, you use the
`update_memory_strategies` operation. You can add, modify or delete
strategies for an existing memory.

###### Note

The starter toolkit CLI currently supports creating and managing memory resources. To update memory strategies on an existing memory, use the starter toolkit Python API or AWS SDK.

###### Example Add a Session Summary strategy to an existing AgentCore Memory

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SummaryStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Assume 'memory_id' is the ID of an existing AgentCore Memory that has no strategies attached to it
memory_id = "your-existing-memory-id"

summaryStrategy = SummaryStrategy(
    name="SessionSummarizer",
    description="Summarizes conversation sessions for context",
    namespaces=["/summaries/{actorId}/{sessionId}/"]
)

memory = memory_manager.update_memory_strategies(
    memory_id=memory_id,
    add_strategies=[summaryStrategy]
)

print(f"Successfully submitted update for memory ID: {memory_id}")

# Validate startegy was added to the memory
memory_strategies = memory_manager.get_memory_strategies(memoryId=memory_id)
print(f"Memory strategies for memoryID: {memory_id} are: {memory_strategies}")

```

###### Note

Long-term memory records will only be extracted from conversational events
that are stored **after** a new strategy becomes
`ACTIVE`. Conversations stored before a strategy is added will
not be processed for long-term memory.
