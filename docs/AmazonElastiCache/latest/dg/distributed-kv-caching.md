

# Distributed KV caching

Distributed key-value (KV) caching with Amazon ElastiCache for Valkey is fully managed and can reduce self-hosted large language model (LLM) inference costs by up to 40% and time to first token (TTFT) by up to 80%. A fleet of graphics processing unit (GPU) inference hosts running LLM inference can share and reuse KV state through the cache instead of recomputing it for each request. This reduces inference costs and TTFT, and lets you serve more traffic from your existing fleet, with open-weight, fine-tuned, or self-trained models that your inference engine supports. You can use models from families such as Qwen, Kimi, Hy4, GPT-OSS, DeepSeek, Inkling, Gemma, Nemotron, and GLM, if your inference engine and LMCache support them.

Distributed KV caching runs on node-based clusters of the `cache.i8ge.48xlarge` node type with ElastiCache for Valkey 9.1 or later, and is based on the [valkey-large-object](https://github.com/valkey-io/valkey-large-object) module. The large object module adds a data type and `BLOB.*` commands for large objects, which each node stores in dynamic random-access memory (DRAM) and on local Non-Volatile Memory Express (NVMe) storage. Clients transfer data with remote direct memory access (RDMA) over Elastic Fabric Adapter (EFA), or over TCP. To get started, see [Getting started with distributed KV caching](distributed-kv-caching-getting-started.md).

Distributed KV caching is best suited to long-running or multi-turn sessions, workloads with shared or repeated context, and spiky traffic spread across many GPU servers. Examples include coding agents, multi-turn chat, shared system prompts, and long-context or retrieval-augmented generation (RAG) workloads. It gives little benefit for short or never-repeated prompts, such as classification, translation, or moderation, for workloads where output generation takes most of the time, and for diffusion models.

Before you create the cluster, you can estimate the benefit of distributed KV caching with KVTrace. KVTrace records the KV cache events of your running vLLM or SGLang fleet, simulates a shared cache at different numbers of cache nodes, and reports the estimated hit rate, the savings, and the break-even price of the cache. To get started, see [KVTrace](https://github.com/aws-samples/amazon-elasticache-samples/tree/main/kvtrace) on the GitHub website.

You can also use the large object commands directly from any Valkey client for other large values, such as model artifacts. For more information, see [Large object module reference for distributed KV caching](large-objects.md).

Distributed KV caching is available in the following AWS Regions:
+ In North America, it is available in US East (N. Virginia), US East (Ohio), and US West (Oregon).
+ In Europe, it is available in Europe (Ireland), Europe (Frankfurt), and Europe (Stockholm).
+ In Asia Pacific, it is available in Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Hong Kong), Asia Pacific (Malaysia), and Asia Pacific (Thailand).

You pay for each `cache.i8ge.48xlarge` node per hour, with standard ElastiCache node pricing, until you delete the cluster. There is no charge for data transfer between your GPU hosts and the cluster in the same Availability Zone. Reserved nodes are available for the `cache.i8ge.48xlarge` node type. For more information, see [Reserved nodes](CacheNodes.Reserved.md). For current prices, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/).

**Topics**
+ [How distributed KV caching works](distributed-kv-caching-how-it-works.md)
+ [Getting started with distributed KV caching](distributed-kv-caching-getting-started.md)
+ [Configuring distributed KV caching](distributed-kv-caching-configuration.md)
+ [Monitoring distributed KV caching](distributed-kv-caching-monitoring.md)
+ [Requirements and limits for distributed KV caching](distributed-kv-caching-limits.md)
+ [Security in distributed KV caching](distributed-kv-caching-security.md)
+ [Troubleshooting distributed KV caching](distributed-kv-caching-troubleshooting.md)
+ [Large object module reference for distributed KV caching](large-objects.md)