

# Memories
<a name="memories-desktop"></a>

Amazon Quick learns facts, preferences, procedures, and patterns from your conversations and saves them as memories. Quick uses these memories to tailor future responses. Each memory shows a confidence score, how often it has been used, and its source.

Memories are kept per agent. The default assistant and each custom agent have their own memories. A rule you set for one agent does not change how another agent behaves. Entities in your knowledge graph remain shared across agents.

## Reviewing and organizing memories
<a name="memories-reviewing"></a>

Search memories, filter and sort them, and switch between list and grid views. A single **Filters** panel covers the following.
+ **Agent**: use the **Agent** dropdown at the top of the tab to view memories for All agents, Default (chat), or a specific custom agent.
+ **Type**: filter by memory category. The available categories are supplied at runtime, so they vary. Examples include procedures, preferences, and profile facts.
+ **Provenance**: show only Told memories (you stated it explicitly to Quick), only Learned memories (Quick inferred it from your activity or conversations), or both.
+ **Sort**: Date created, Accuracy confidence, or Times referenced.

Each memory card shows the agent it applies to. Knowledge graph entities in the memory panel are marked shared to show they are visible to every agent.

A memory's detail view has four parts:
+ The memory text.
+ An information section with when the memory was created and updated, how often it was used, its confidence, its type, and what it applies to.
+ An attributes section with the Told or Learned badge, any tags, and a global-behavior badge.
+ A provenance timeline that traces, step by step, what Quick used to form the memory.

Each memory card provides the following actions.
+ **Boost**: raise the confidence in the memory to the highest level so it is used first in future responses.
+ **Forget**: remove the memory. When you forget a memory, you can choose a reason (for example, Too specific, Never said this, or Outdated) or add free-form feedback. Quick uses the reason to avoid re-learning the same thing.
+ **Edit**: update the memory's text. Use edit to fix a fact rather than delete and re-teach it.

## Memory settings
<a name="memories-settings"></a>

The Memory section in **Configuration** has a master switch and a **Forget all memories** action.
+ **Enable memory**: a master toggle that controls whether Quick learns from your conversations and tailors future responses. When memory is off, existing memories are not used and no new memories are recorded.
+ **Forget all memories**: deletes every memory Quick has saved. Type "forget" to confirm.

Forgetting all memories cannot be undone. It does not affect your knowledge graph. To clear entities and relationships, use **Reset knowledge graph** (see [Knowledge graph](knowledge-graph-desktop.md)).