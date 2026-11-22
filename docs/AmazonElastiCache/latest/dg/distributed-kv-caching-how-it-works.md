

# How distributed KV caching works

This topic describes the key-value (KV) state that distributed KV caching stores for your graphics processing unit (GPU) inference fleet, how a request uses the cache, and how the cache behaves during traffic changes and failures.

**Topics**
+ [KV state and the cache hierarchy](#distributed-kv-caching-how-it-works.hierarchy)
+ [Cache placement and sharing](#distributed-kv-caching-how-it-works.placement)
+ [Memory and NVMe storage](#distributed-kv-caching-how-it-works.tiering)
+ [Data transport](#distributed-kv-caching-how-it-works.transport)
+ [Inference engine connectors](#distributed-kv-caching-how-it-works.connectors)
+ [Resilience and data persistence](#distributed-kv-caching-how-it-works.resilience)

## KV state and the cache hierarchy
<a name="distributed-kv-caching-how-it-works.hierarchy"></a>

KV state is the working memory that a large language model (LLM) keeps for the conversation so far. Without a shared cache, inference recomputes the KV state for the entire conversation history at the start of every turn. GPU-local caches reduce this work, but they are limited in size, and they are lost when a server restarts or fails. They also can't share KV state across servers, so traffic spikes, server failures, and scaling events cause KV cache misses and expensive recomputation.

Inference engines use the following convention to describe a cache hierarchy:
+ **L0** – GPU memory.
+ **L1** – The inference server's own host memory and local Non-Volatile Memory Express (NVMe) storage.
+ **L2** – A distributed KV cache.

For each request, the inference engine checks L0, then L1, and then the distributed cache in that order. On a cache hit, the GPU skips recomputing the cached portion of the prompt and processes only the new tokens. Newly computed KV state is written to the shared cache so that other servers can reuse it.

## Cache placement and sharing
<a name="distributed-kv-caching-how-it-works.placement"></a>

The cluster and every client that uses it must be in the same VPC. Clients that use remote direct memory access (RDMA) over Elastic Fabric Adapter (EFA) must be in the Availability Zone of the cluster. TCP clients in other Availability Zones can connect. For lower latency, and because there is no data transfer charge in the same Availability Zone, we recommend that you put clients in the Availability Zone of the cluster and use RDMA. Create the cluster in the Availability Zone of your GPU fleet.

Because the cache is shared, cached context stays available to the fleet through routing shifts, traffic spikes, and host failovers.

## Memory and NVMe storage
<a name="distributed-kv-caching-how-it-works.tiering"></a>

Each node keeps large objects, the values that clients write with the large object (`BLOB.*`) commands, on its local NVMe storage. When a client reads a large object, the node copies it from NVMe storage into its dynamic random-access memory (DRAM) cache, as long as the object isn't larger than the DRAM cache limit. When the DRAM cache is full, the node drops cached copies, and the objects stay on NVMe storage. Each `cache.i8ge.48xlarge` node provides large NVMe storage and high bandwidth, so one cluster can serve many GPU or accelerator servers, which is the recommended pattern.

Values that clients write with the Valkey `SET` command, outside the large object module, don't use NVMe storage. They are stored in node memory, so their capacity is the memory of the node. For the size limits, see [Size limits](distributed-kv-caching-limits.md#distributed-kv-caching-limits.sizes).

When the storage is full, a write evicts other keys. We recommend setting `maxmemory-policy` to `allkeys-lru` for caching. For eviction behavior, see [Eviction and memory management](distributed-kv-caching-configuration.md#distributed-kv-caching-configuration.tiering).

## Data transport
<a name="distributed-kv-caching-how-it-works.transport"></a>

Clients can transfer data in two ways:
+ **RDMA over EFA** – The `BLOB.RDMA_*` commands move the data directly between client memory and the node. Only the command and a short reply use the TLS connection. Use RDMA for production workloads that need high bandwidth.
+ **TCP** – The `BLOB.TCP_*` commands send the data inline on the Transport Layer Security (TLS) connection. This works from any client that can connect to the cluster. Use TCP for development and testing, or for clients that can't use EFA.

For the client requirements and setup, see [Step 6: Set up the client hosts](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.clients).

## Inference engine connectors
<a name="distributed-kv-caching-how-it-works.connectors"></a>

Inference engines connect to the distributed cache through the open-source LMCache server, which runs on each GPU host. vLLM and SGLang connect to the LMCache server. NVIDIA TensorRT-LLM support is in the LMCache development branch. It isn't in a stable LMCache release yet. The LMCache server keeps KV state in host memory (L1) and in the cluster (L2). The `transport` setting of the LMCache Valkey L2 adapter selects how LMCache moves data:
+ `rdma` – The `BLOB.RDMA_*` commands over EFA, for production. Use this transport to store KV state on NVMe storage at high bandwidth.
+ `blob-tcp` – The `BLOB.TCP_*` commands over TLS, for tests of the large object path on hosts without EFA.
+ `tcp` (default) – The Valkey `SET` and `GET` commands over TLS, for functional tests. These values are stored in node memory, not on NVMe storage.

**Note**  
The `rdma` and `blob-tcp` transports need LMCache 0.5.8rc1 or later, which is not yet a stable LMCache release. The current stable release supports only the `tcp` transport. For the setup, see [Step 8: Connect your inference engine](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.configure).

## Resilience and data persistence
<a name="distributed-kv-caching-how-it-works.resilience"></a>

ElastiCache doesn't persist or replicate the data in a distributed KV cache, and you can't back it up or restore it. A node reboot, replacement, patch, or failure removes all objects on that node. Applications must treat the cluster as a cache, and recompute or reload data on a miss. LMCache treats a failed read from the cluster as a cache miss, and the engine recomputes the KV state.