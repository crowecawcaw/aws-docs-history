# Configure built-in

strategies

AgentCore Memory provides pre-configured, [built-in memory strategies](built-in-strategies.md "built-in-strategies.md") for common use cases.

###### Topics

- [User preferences](#long-term-user-preferences-strategy "#long-term-user-preferences-strategy")
- [Semantic](#long-term-semantic-facts-strategy "#long-term-semantic-facts-strategy")
- [Session summaries](#long-term-session-summaries-strategy "#long-term-session-summaries-strategy")
- [Episodic](#long-term-session-episodic-strategy "#long-term-session-episodic-strategy")

## User preferences

The [user preferences](user-preference-memory-strategy.md "user-preference-memory-strategy.md")
(`UserPreferenceMemoryStrategy`) strategy is designed to
automatically identify and extract user preferences, choices, and styles from
conversations. This lets your agent build a persistent profile of each user, leading
to more personalized and relevant interactions.

- **Example use case:** An e-commerce agent
  remembers a user's favorite brands and preferred size, letting it offer
  tailored product recommendations in future sessions.

###### Configuration example:

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import UserPreferenceStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Create memory resource with user preference strategy
memory = memory_manager.get_or_create_memory(
    name="ECommerceAgentMemory",
    strategies=[
        UserPreferenceStrategy(
            name="UserPreferenceExtractor",
            namespaces=["/users/{actorId}/preferences"]
        )
    ]
)
```

## Semantic

The [Semantic](semantic-memory-strategy.md "semantic-memory-strategy.md")
(`SemanticMemoryStrategy`) memory strategy is engineered to identify
and extract key pieces of factual information and contextual knowledge from
conversational data. This lets your agent build a persistent knowledge base about
important entities, events, and details discussed during an interaction.

- **Example use case:** A customer support
  agent remembers that order `#ABC-123` is related to a specific
  support ticket, so the user doesn't have to provide the order number again
  when following up.

###### Configuration example:

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SemanticStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Create memory resource with semantic strategy
memory = memory_manager.get_or_create_memory(
    name="SupportAgentFactMemory",
    strategies=[
        SemanticStrategy(
            name="FactExtractor",
            namespaces=["/support_cases/{sessionId}/facts"]
        )
    ]
)
```

## Session summaries

The [session summaries](summary-strategy.md "summary-strategy.md")
(`SummaryMemoryStrategy`) memory strategy creates condensed, running
summaries of conversations as they happen within a single session. This captures the
key topics and decisions, letting an agent quickly recall the context of a long
conversation without needing to re-process the entire history.

- **Example use case:** After a 30-minute
  troubleshooting session, the agent can access a summary like, "User reported
  issue with software v2.1, attempted a restart, and was provided a link to
  the knowledge base article."

###### Configuration example:

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SummaryStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Create memory resource with summary strategy
memory = memory_manager.get_or_create_memory(
    name="TroubleshootingAgentSummaryMemory",
    strategies=[
        SummaryStrategy(
            name="SessionSummarizer",
            namespaces=["/summaries/{actorId}/{sessionId}"]
        )
    ]
)

```

## Episodic

The [episodic](episodic-memory-strategy.md "episodic-memory-strategy.md")
(`EpisodicStrategy`) memory strategy captures interactions as structured episodes consisting of scenarios, intents, thoughts, actions taken, outcomes, and artifacts. With this strategy, reflections are also made across episodes to extract broader insights, letting an agent learn and apply successful patterns from prior interactions to new interactions.

- **Example use case:** A customer support agent logs interactions as episodes. The system captures which phrases and actions lead to successful interactions

###### Configuration example:

```
from bedrock_agentcore_starter_toolkit.operations.memory.manager import MemoryManager
from bedrock_agentcore_starter_toolkit.operations.memory.models.strategies import SummaryStrategy

# Create memory manager
memory_manager = MemoryManager(region_name="us-west-2")

# Create memory resource with summary strategy
memory_manager.get_or_create_memory(
    name="MyMemory",
    strategies=[
        EpisodicStrategy(
            name="EpisodicStrategy",
            namespaces=["strategy/{memoryStrategyId}/actors/{actorId}/sessions/{sessionId}"],
            reflection={
                "namespaces": ["strategy/{memoryStrategyId}/actors/{actorId}/"]
            }
        )
    ]
)
```
