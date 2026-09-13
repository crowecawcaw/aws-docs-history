

# Memories
<a name="memories-desktop"></a>

Memories are the facts, preferences, procedures, and patterns Amazon Quick learns from your conversations to personalize future responses. Each memory shows a confidence score, how many times it has been referenced, and its source.

Memories are kept per agent. The default assistant and each custom agent you create have their own memories, so a rule you set for one agent does not silently change how another agent behaves. Entities in your knowledge graph remain shared across agents.

## Reviewing and organizing memories
<a name="memories-reviewing"></a>

Search memories, filter and sort them, and switch between list and grid views. A single Filters panel covers the following.
+ **Agent**: use the Agent dropdown at the top of the tab to view memories for All agents, Default (chat), or a specific custom agent.
+ **Type**: filter by memory category. The available categories are supplied at runtime, so they vary. Examples include procedures, preferences, and profile facts.
+ **Provenance**: show only Told memories (you stated it explicitly to Quick), only Learned memories (Quick inferred it from your activity or conversations), or both.
+ **Sort**: Date created, Accuracy confidence, or Times referenced.

Each memory card shows the agent it applies to. Knowledge graph entities in the memory panel are marked shared to indicate that they are visible to every agent.

A memory's detail view shows its text, an information section (created, updated, times referenced, confidence, type, and Applicable to), an attributes section (the Told or Learned badge, any tags, and a global-behavior badge), and a step-by-step provenance timeline that traces what Quick used to form it. Each memory card provides the following actions.
+ **Boost**: raise the confidence in the memory to the highest level so it is prioritized in future responses.
+ **Forget**: remove the memory. When you forget a memory, you can optionally choose a reason (for example, Too specific, Never said this, or Outdated) or add free-form feedback. Quick uses the reason to avoid re-learning the same thing.
+ **Edit**: update the memory's text. Use edit to correct a fact rather than delete and re-teach it.

## Memory settings
<a name="memories-settings"></a>

The Memory section in Configuration includes a master switch and a Forget all memories action.
+ **Enable memory**: a master toggle that controls whether Quick learns from your conversations and personalizes future responses. When memory is off, existing memories are not used and no new memories are recorded.
+ **Forget all memories**: permanently deletes every memory Quick has saved. Type "forget" to confirm.

Forgetting all memories cannot be undone. It does not affect your knowledge graph. To clear entities and relationships, use Reset knowledge graph (see [Knowledge graph](knowledge-graph-desktop.md)).