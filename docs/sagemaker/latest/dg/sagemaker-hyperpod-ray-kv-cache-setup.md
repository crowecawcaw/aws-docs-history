

# Setting up tiered KV cache
<a name="sagemaker-hyperpod-ray-kv-cache-setup"></a>

The managed tiered KV cache adds a cluster-wide cache tier to Ray Serve deployments, so one replica reads a token prefix that another replica already computed. This reduces time to first token for long documents, multi-turn conversations, and shared system prompts. The cluster-wide tier runs on HyperPod Tiered Storage using [LMCache with the HyperPod storage backend](https://docs.lmcache.ai/kv_cache/storage_backends/sagemaker_hyperpod.html) in the LMCache documentation, which integrates with Ray Serve and vLLM to provide distributed KV caching backed by HyperPod Tiered Storage.

The cache has two tiers:
+ A **local tier** in the memory of the node serving the request, for the fastest reuse.
+ A **cluster-wide tier** on HyperPod Tiered Storage, a pooled memory tier that spans cluster nodes. A replica reads a prefix computed by another replica instead of recomputing it.

When a request shares a token prefix with earlier work, the deployment reads the cached KV state from the local tier, then the cluster-wide tier, before recomputing anything.

## Prerequisites
<a name="sagemaker-hyperpod-ray-kv-cache-setup-prereq"></a>
+ A HyperPod cluster orchestrated by Amazon EKS, with the KubeRay operator installed.
+ HyperPod Tiered Storage enabled on the cluster. For setup instructions, see [Setting up managed tiered checkpointing](https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing-setup.html).

## Configure your RayCluster
<a name="sagemaker-hyperpod-ray-kv-cache-setup-raycluster"></a>

Add the following to your worker group spec to expose the Tiered Storage endpoint and shared memory to the Ray Serve replicas.

```
workerGroupSpecs:
- template:
    spec:
      volumes:
        - name: host-shm
          hostPath:
            path: /dev/shm
      containers:
      - name: ray-worker
        env:
          - name: NODE_IP
            valueFrom:
              fieldRef:
                fieldPath: status.hostIP
        volumeMounts:
          - name: host-shm
            mountPath: /dev/shm/ai_toolkit_cache
            subPath: ai_toolkit_cache
```

The `NODE_IP` environment variable provides the host IP address so the LMCache client can connect to the Tiered Storage service on port 9200. The shared memory volume mount enables the CPU offloading path for local KV cache.

## Configure your Ray Serve application
<a name="sagemaker-hyperpod-ray-kv-cache-setup-serve-config"></a>

Use the `LLMConfig` API with the LMCache connector to enable KV caching in your Ray Serve deployment. The following example serves a model with tiered KV caching enabled:

```
from ray.serve.llm import LLMConfig, build_openai_app

llm_config = LLMConfig(
    model_loading_config={
        "model_id": "my-llm",
        "model_source": "Qwen/Qwen-7B-Chat",
    },
    engine_kwargs={
        "trust_remote_code": True,
        "kv_transfer_config": {
            "kv_connector": "LMCacheConnectorV1",
            "kv_role": "kv_both",
        },
    },
    runtime_env={
        "env_vars": {
            "LMCACHE_REMOTE_URL": "sagemaker-hyperpod://$(NODE_IP):9200",
            "LMCACHE_EXTRA_CONFIG": '{"sagemaker_hyperpod_bucket": "lmcache", "sagemaker_hyperpod_shared_memory_name": "ai_toolkit_cache"}',
            "LMCACHE_CHUNK_SIZE": "256",
        },
    },
    accelerator_type="A10G",
)

app = build_openai_app({"llm_configs": [llm_config]})
```

The key configuration values are:
+ `kv_connector`: Set to `LMCacheConnectorV1` to enable the LMCache integration with vLLM.
+ `kv_role`: Set to `kv_both` so each replica both reads from and writes to the shared cache.
+ `LMCACHE_REMOTE_URL`: The Tiered Storage endpoint on the local node. Uses the `NODE_IP` environment variable configured in the RayCluster manifest.
+ `LMCACHE_CHUNK_SIZE`: The number of tokens per cache chunk. Smaller values increase cache hit rate for shared prefixes at the cost of more cache entries.

## Enable CPU offloading (optional)
<a name="sagemaker-hyperpod-ray-kv-cache-setup-cpu-offloading"></a>

To add a local CPU memory tier that caches KV entries before they are written to Tiered Storage, add the following environment variables to `runtime_env`:

```
"env_vars": {
    "LMCACHE_REMOTE_URL": "sagemaker-hyperpod://$(NODE_IP):9200",
    "LMCACHE_EXTRA_CONFIG": '{"sagemaker_hyperpod_bucket": "lmcache", "sagemaker_hyperpod_shared_memory_name": "ai_toolkit_cache"}',
    "LMCACHE_CHUNK_SIZE": "256",
    "LMCACHE_LOCAL_CPU": "True",
    "LMCACHE_MAX_LOCAL_CPU_SIZE": "100",
}
```

When CPU offloading is enabled, KV cache entries are stored in CPU memory on the local node before being written to the cluster-wide Tiered Storage. This provides faster cache reads for replicas on the same node.