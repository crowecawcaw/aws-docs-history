

# Types of agentic memory
<a name="agentic-memory-types"></a>

## Short-term memory
<a name="agentic-memory-short-term"></a>

Short-term memory maintains context within a single session. It tracks the current conversation flow, recent interactions, and intermediate reasoning steps. Short-term memory is essential for multi-turn conversations where the agent needs to reference earlier parts of the dialogue.

ElastiCache for Valkey supports short-term memory through data structures such as lists (for ordered chat history), hashes (for session metadata), and strings (for tool result caching with TTL-based expiration).

## Long-term memory
<a name="agentic-memory-long-term"></a>

Long-term memory stores information across multiple sessions. This enables agents to remember user preferences, past decisions, and historical context for future conversations. Long-term memory requires a persistent, searchable store that supports semantic retrieval — finding relevant memories based on meaning rather than exact keyword matches.

ElastiCache for Valkey supports long-term memory through its vector similarity search capabilities (available in Valkey 8.2 and later). Vector search enables semantic memory retrieval, allowing agents to find relevant memories based on meaning by comparing vector embeddings of stored memories against new queries.

## Additional memory types
<a name="agentic-memory-additional-types"></a>


| Memory type | Description | ElastiCache support | 
| --- | --- | --- | 
| Episodic memory | Records of specific past interactions and events | Vector search over stored conversation embeddings | 
| Semantic memory | General knowledge and facts extracted from interactions | Vector similarity search with HNSW or FLAT indexes | 
| Procedural memory | Knowledge about how to perform tasks and use tools | Hash-based storage of tool configurations and workflows | 