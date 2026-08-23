# Managed tiered KV cache and routing

Large language model serving spends compute rebuilding the key-value (KV) cache for tokens
it has already processed. HyperPod adds a managed two-tier KV cache and prefix-aware
routing to Ray Serve, which cut redundant recomputation and lower time to first token for
long-context and multi-turn workloads.

## How the tiered cache works

The cache has two tiers:

- A **local tier** in the memory of the node
  serving the request, for the fastest reuse.
- A **cluster-wide tier** on HyperPod
  Tiered Storage, a pooled memory tier that spans cluster nodes. A replica reads a
  prefix computed by another replica instead of recomputing it.

When a request shares a token prefix with earlier work, the deployment reads the
cached KV state from the local tier, then the cluster-wide tier, before recomputing
anything.

## Prefix-aware routing

Prefix-aware routing sends a request to a replica that already holds the KV cache for
its prefix. Multi-turn conversations and shared system prompts route to the same
replica, so the cache hit rate stays high and time to first token drops.

## Prerequisite

The cluster-wide tier runs on HyperPod Tiered Storage, so set up Tiered
Storage on the cluster before you turn on the cluster-wide cache. For more information,
see [Setting up tiered KV cache](sagemaker-hyperpod-ray-kv-cache-setup.md "sagemaker-hyperpod-ray-kv-cache-setup.md").
