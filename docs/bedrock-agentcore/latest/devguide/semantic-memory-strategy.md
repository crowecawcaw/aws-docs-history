# Semantic memory strategy

The `SemanticMemoryStrategy` is designed to identify and extract
key pieces of factual information and contextual knowledge from conversational
data. This lets your agent to build a persistent knowledge base about the
entities, events, and key details discussed during an interaction.

Examples of facts captured by this strategy include:

- An order number (`#XYZ-123`) is associated with a specific
  support case.
- A project's deadline of October 25th.
- The user is running version 2.1 of the software.
  By referencing this stored knowledge, your agent can provide more accurate,
  context-aware responses, perform multi-step tasks that rely on previously stated
  information, and avoid asking users to repeat key details.

**Default namespace**

`/strategies/{memoryStrategyId}/actors/{actorId}`
