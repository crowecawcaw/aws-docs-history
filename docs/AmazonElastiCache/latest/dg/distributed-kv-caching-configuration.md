

# Configuring distributed KV caching

Distributed key-value (KV) caching has two configuration surfaces: the parameter group of the cluster, and the LMCache connector settings that you set in your inference engine. For the cluster settings, see [Cluster requirements](distributed-kv-caching-limits.md#distributed-kv-caching-limits.requirements). For general information about managing node-based clusters, see [Managing your node-based cluster in ElastiCache](manage-self-designed-cluster.md).

**Topics**
+ [Parameters](#distributed-kv-caching-configuration.parameters)
+ [Eviction and memory management](#distributed-kv-caching-configuration.tiering)
+ [LMCache connector settings](#distributed-kv-caching-configuration.connector)
+ [Request routing](#distributed-kv-caching-configuration.routing)

## Parameters
<a name="distributed-kv-caching-configuration.parameters"></a>

ElastiCache runs the large object module in tiered mode with Elastic Fabric Adapter (EFA), and manages its settings for you. You can't change them, and the `CONFIG` and `MODULE LIST` commands aren't available. To view the module state, use `INFO largeobj`.

You can change the following parameter with a custom parameter group in the `valkey9` family. The parameter group must also set `cluster-enabled` to `yes`.


**Distributed KV caching parameters**  

| Parameter | Recommended value | Description | 
| --- | --- | --- | 
| maxmemory-policy | allkeys-lru | Controls which keys can be evicted. For more information, see [Eviction and memory management](#distributed-kv-caching-configuration.tiering). | 

For the parameters of the `valkey9` family, see [Valkey 9.1 and Valkey 9.0 parameter changes](ParameterGroups.Engine.md#ParameterGroups.Valkey.9.0).

## Eviction and memory management
<a name="distributed-kv-caching-configuration.tiering"></a>

When a node is full, a write can evict other keys to make space. For large objects, the node is full when its Non-Volatile Memory Express (NVMe) storage is full. For values that you write with `SET`, the node is full when its memory is full. The `maxmemory-policy` parameter controls which keys can be evicted.


**Eviction by maxmemory-policy**  

| maxmemory-policy | Keys that can be evicted | 
| --- | --- | 
| allkeys-\* | Any key | 
| volatile-\* | Only keys with a time to live (TTL). Keys with no TTL are never evicted, so writes fail when the node is full. | 
| noeviction | None. The write fails with an OOM error. | 

If you don't choose a parameter group, the cluster uses the default parameter group of the `valkey9` family. As for other node types, this group uses `volatile-lru`. We recommend a custom parameter group with `allkeys-lru`, or the `ttl_seconds` field of LMCache. Choose one of the following options before you create the cluster:
+ **Use the default parameter group** – Set the `ttl_seconds` field of the LMCache Valkey L2 adapter, so that every LMCache key has a TTL and can be evicted. Set the TTL to more than the longest session.
+ **Use a custom parameter group with `allkeys-lru`** – LMCache keys don't need a TTL. Use a dedicated cluster, because `allkeys-lru` can evict the keys of other applications.

Objects are always evicted in least recently used (LRU) order, whatever the policy. After the cluster fills, make sure that the `Evictions` metric increases. For more information about eviction, see [Memory and eviction](https://valkey.io/topics/large-object-configuration/#memory-and-eviction) on the valkey.io website. For how this memory shows in CloudWatch, see [How existing metrics apply to distributed KV caching](distributed-kv-caching-monitoring.md#distributed-kv-caching-monitoring.existing-metrics).

## LMCache connector settings
<a name="distributed-kv-caching-configuration.connector"></a>

LMCache in multiprocess mode has two parts on each GPU host: the LMCache server, which you configure with `lmcache server` options and a `--l2-adapter` JSON object with `"type": "valkey"`, and the engine connector. For vLLM, you configure the connector with the `--kv-transfer-config` JSON object. The following table describes the settings that connect them to the cluster. For a complete example, see [Step 8: Connect your inference engine](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.configure).


**LMCache connector settings**  

| Setting | Value | Description | 
| --- | --- | --- | 
| `--host`, `--port` | `127.0.0.1`, `5555` | `lmcache server` options. The address where the engine sends requests. Use `127.0.0.1` when the engine is on the same host. Don't use `0.0.0.0`. To use the private IP address of the host, also use `--api-key-file`. | 
| `--api-key-file` | `/etc/lmcache/api.key` | `lmcache server` option. A key that protects the request channel and the HTTP API of the LMCache server. The engine reads the same key from the `LMCACHE_API_KEY_FILE` environment variable. | 
| `--l1-size-gb` | Suggested for LMCache 0.5.8rc1 or later: about half of the memory of the non-uniform memory access (NUMA) node where LMCache runs | `lmcache server` option. The size of the L1 tier in host memory, in GB. Keep it below the pinned-memory limit of the host. | 
| `--no-l1-use-lazy` | (flag) | `lmcache server` option. Required for the `rdma` transport, because EFA can't register memory that the lazy allocator hasn't filled. | 
| `--chunk-size` | `256` | `lmcache server` option. The minimum number of tokens in each cache chunk. Don't use 1,024. A prompt shorter than one chunk writes nothing to the cluster. Each chunk must be 512 MiB or smaller. | 
| `--hash-algorithm` | `sha256_cbor` | `lmcache server` option. Must be the same on every LMCache server that shares the cluster. Don't use `builtin`. | 
| `--eviction-policy` | `LRU` | `lmcache server` option. The eviction policy of the L1 tier. It isn't the `maxmemory-policy` of the cluster. | 
| `--eviction-trigger-watermark` | `0.6` | `lmcache server` option. The share of L1 memory in use that starts eviction. The default is 0.8. At 0.6, the L1 tier keeps room for the KV state that LMCache loads from the cluster, and it holds about 60% of `--l1-size-gb`. | 
| `--eviction-ratio` | `0.2` | `lmcache server` option. The share of L1 memory that LMCache frees each time eviction starts. The default is 0.2. | 
| `--supported-transfer-mode` | `auto` | `lmcache server` option. Required when SGLang uses the LMCache server. | 
| `transport` | `rdma` | `--l2-adapter` field. `rdma`, `blob-tcp`, or `tcp` (the default). Always set it. For more information, see [Inference engine connectors](distributed-kv-caching-how-it-works.md#distributed-kv-caching-how-it-works.connectors). | 
| `cluster_mode` | `true` | `--l2-adapter` field. Must be `true`, because the cluster uses cluster mode. The default is `false`. | 
| `startup_nodes` | `<endpoint>:6379` | `--l2-adapter` field. The configuration endpoint of the cluster. | 
| `tls_enable` | `true` | `--l2-adapter` field. Must be `true`, because the cluster requires Transport Layer Security (TLS). The default is `false`. | 
| `username`, `password` | From AWS Secrets Manager | `--l2-adapter` fields. The user name and password of a Valkey user in the user group of the cluster. Don't put the password in a configuration file or on the command line. | 
| `num_workers` | `16` | `--l2-adapter` field. The number of worker threads. Each worker has its own client connection. We recommend 16 workers. | 
| `key_prefix` | `<model_version_tp_keytype>` | `--l2-adapter` field. Must not be empty or contain `@`. Use a separate prefix for each model, model version, tensor parallel (TP) layout, KV cache data type, and key type. To keep tenants apart on a shared cluster, send a different `cache_salt` value for each tenant. `cache_salt` is a vLLM request field that LMCache puts in the key. Use separate clusters for tenants that must not learn about each other's prompts. The `rdma` and `blob-tcp` transports write the same key type and can share a prefix. The `tcp` transport can't share a prefix with `rdma` or `blob-tcp`. | 
| `ttl_seconds` | More than the longest session | `--l2-adapter` field. Required with the default parameter group (`volatile-lru`). With `rdma` and `blob-tcp`, LMCache sets the TTL with a separate `EXPIRE` command, so the Valkey user must be allowed to run `EXPIRE`. For more information, see [Eviction and memory management](#distributed-kv-caching-configuration.tiering). | 
| `max_capacity_gb` | `0` | `--l2-adapter` field. Keep `0`, so that the cluster, not LMCache, evicts keys. | 
| `rdma_provider`, `rdma_interface` | `efa-direct`, a list of EFA devices | `--l2-adapter` fields, for `rdma` only. The libfabric provider and the EFA devices to use. List the devices on the NUMA node of the LMCache server. | 
| `kv_connector`, `kv_connector_module_path` | `LMCacheMPConnector`, `lmcache.integration.vllm.lmcache_mp_connector` | `--kv-transfer-config` fields. The vLLM connector that sends KV state to the LMCache server, loaded from the installed LMCache version. | 
| `kv_role` | `kv_both` | `--kv-transfer-config` field. Configures the instance to both read from and write to the cache. | 
| `kv_load_failure_policy` | `recompute` or `fail` | `--kv-transfer-config` field. Always set it, because the default changes between vLLM versions. | 
| `lmcache.mp.host`, `lmcache.mp.port` | `tcp://127.0.0.1`, `5555` | `kv_connector_extra_config` fields. The address of the LMCache server. Use the `--host` value of `lmcache server` with the `tcp://` scheme (`grpc://` with `--transport grpc`), and the same `--port` value. | 
| `PYTHONHASHSEED` | `0` | Environment variable. Required for every engine and LMCache process, so that all hosts compute the same cache keys. | 

Every GPU host that shares the cluster must use the same model and revision, TP layout, KV cache data type, LMCache version, `--hash-algorithm`, and `PYTHONHASHSEED=0`. A difference causes cache misses or wrong KV state, with no error.

For all LMCache server options and Valkey L2 adapter fields, see [Valkey L2 adapter](https://docs.lmcache.ai/mp/l2_storage/valkey.html) on the LMCache website.

## Request routing
<a name="distributed-kv-caching-configuration.routing"></a>

You can keep your existing request router. Request routers don't count the KV state in the cluster, and you don't need to change your routing to use it. Route requests to GPU hosts in the Availability Zone of the cluster. For more information, see [Cache placement and sharing](distributed-kv-caching-how-it-works.md#distributed-kv-caching-how-it-works.placement).