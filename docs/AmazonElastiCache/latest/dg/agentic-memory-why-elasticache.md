

# Why ElastiCache for Valkey for agentic memory
<a name="agentic-memory-why-elasticache"></a>

ElastiCache for Valkey provides several capabilities that make it well suited as the storage layer for agentic memory:
+ **Sub-millisecond latency** – ElastiCache for Valkey delivers microsecond-level latency for memory operations, making it suitable for real-time agent interactions where memory lookups must not add perceptible delay to the user experience.
+ **Vector similarity search** – Starting with Valkey version 8.2, ElastiCache supports vector similarity search through the valkey-search module. This enables semantic memory retrieval, where agents can find relevant memories based on meaning rather than exact keyword matches.
+ **Real-time index updates** – New memories become immediately searchable after being written. This is critical for agentic applications where the agent may need to recall information it stored moments ago within the same session.
+ **Built-in cache management** – Features such as TTL (time to live), eviction policies (`allkeys-lru`), and atomic operations help manage the memory lifecycle.
+ **Multiple data structures** – Valkey provides hashes, lists, strings, streams, JSON, and vectors — each optimized for different memory patterns. A single ElastiCache instance can support session state (hashes), conversation history (lists), tool result caching (strings with TTL), event logs (streams), and semantic memory (vectors).
+ **Scalability** – ElastiCache scales to handle millions of requests with consistent low latency, supporting applications with large numbers of concurrent users and agents.