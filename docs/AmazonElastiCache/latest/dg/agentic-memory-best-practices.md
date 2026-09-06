

# Best practices
<a name="agentic-memory-best-practices"></a>

## Memory lifecycle management
<a name="agentic-memory-bp-lifecycle"></a>
+ **Use TTL for short-term memory** – Set appropriate TTL values on memory entries to automatically expire transient information. For session context, use TTLs of 30 minutes to 24 hours. For long-term user preferences, use longer TTLs or persist indefinitely.
+ **Implement memory decay** – Mem0 provides built-in decay mechanisms that remove irrelevant information over time. Configure these to prevent memory bloat as the agent accumulates more interactions.
+ **Deduplicate memories** – Before storing a new memory, check if a similar memory already exists using vector similarity search. Update existing memories rather than creating duplicates.

## Vector index configuration
<a name="agentic-memory-bp-index"></a>
+ **Choose the right index type** – Use `FLAT` for smaller memory stores (under 100,000 entries) where exact search is feasible. Use `HNSW` for larger stores where approximate nearest neighbor search provides better performance at scale.
+ **Select appropriate dimensions** – Match the embedding dimensions to your model. Amazon Titan Text Embeddings V2 produces 1024-dimensional vectors. OpenAI's text-embedding-3-small produces 1536-dimensional vectors.
+ **Use COSINE distance metric** – For text embeddings from models like Amazon Titan and OpenAI, COSINE distance is typically the most appropriate metric for measuring semantic similarity.

## Multi-user isolation
<a name="agentic-memory-bp-isolation"></a>
+ **Scope memories by user ID** – Always include a `user_id` parameter when storing and searching memories to prevent information leaking between users.
+ **Use TAG filters for efficient isolation** – When querying the vector index, use TAG filters (for example, `@user_id:{user_123}`) to pre-filter results by user before performing KNN search. This runs as a single atomic operation, providing both isolation and performance.

  ```
  # Example: TAG-filtered vector search for user isolation
  results = client.execute_command(
      "FT.SEARCH", "agent_memory",
      f"@user_id:{{{user_id}}}=>[KNN 5 @embedding $query_vec]",
      "PARAMS", "2", "query_vec", query_vec,
      "DIALECT", "2",
  )
  ```

## Memory management at scale
<a name="agentic-memory-bp-scale"></a>
+ **Set maxmemory policy** – Configure `maxmemory-policy allkeys-lru` on your ElastiCache cluster to automatically evict least-recently-used memory entries when the cluster reaches its memory limit.
+ **Monitor memory usage** – Use Amazon CloudWatch metrics to track memory utilization, cache hit rates, and vector search latency. Set alarms for high memory usage to proactively manage capacity.
+ **Plan for capacity** – Each memory entry typically requires approximately 4–6 KB (embedding dimensions × 4 bytes \+ metadata). A 1 GB ElastiCache instance can store approximately 170,000–250,000 memory entries depending on embedding size and metadata.