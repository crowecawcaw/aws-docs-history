

# Why ElastiCache for Valkey for semantic caching
<a name="semantic-caching-why-elasticache"></a>

Semantic caching workloads continuously write, search, and evict cache entries to serve the stream of incoming user queries while keeping responses fresh. The cache store must meet the following requirements:
+ **Real-time vector updates** – New queries and responses must be immediately available in the cache to maintain hit rates.
+ **Low-latency lookups** – The cache sits in the online request path of every query, so lookups must not add perceptible delay to end-user response time.
+ **Efficient ephemeral management** – Entries are frequently written, read, and evicted, requiring efficient management of a hot set.

ElastiCache for Valkey meets these requirements:
+ **Lowest latency vector search** – At the time of writing, ElastiCache for Valkey delivers the lowest latency vector search with the highest throughput and best price-performance at 95%\+ recall rate among popular vector databases on AWS. Latency is as low as microseconds with up to 99% recall.
+ **Multithreaded architecture** – Vector search on ElastiCache uses a multithreaded architecture that supports real-time vector updates and high write throughput while maintaining low latency for search requests.
+ **Built-in cache features** – TTL (time to live), eviction policies (`allkeys-lru`), and atomic operations help manage the ephemeral hot set of entries that semantic caching creates.
+ **Vector index support** – ElastiCache supports both HNSW (Hierarchical Navigable Small World) and FLAT index algorithms with COSINE, Euclidean, and inner product distance metrics.
+ **Zero-downtime scalability** – ElastiCache supports scaling without downtime, allowing you to adjust capacity as your cache grows.
+ **Framework integration** – ElastiCache for Valkey integrates with Amazon Bedrock AgentCore through the LangGraph framework, enabling you to implement a Valkey-backed semantic cache for agents built on Amazon Bedrock.