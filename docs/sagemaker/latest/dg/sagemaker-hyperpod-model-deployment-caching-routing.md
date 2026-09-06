

# KV caching and intelligent routing
<a name="sagemaker-hyperpod-model-deployment-caching-routing"></a>

Amazon SageMaker HyperPod Inference provides managed tiered key-value (KV) caching and intelligent routing to optimize inference performance for large language model (LLM) workloads. KV caching saves precomputed key-value vectors after processing previous tokens, eliminating redundant recalculations. Through a two-tier caching architecture, you can configure an L1 cache that uses CPU memory for low-latency local reuse, and an L2 cache that leverages Redis or managed tiered storage to enable scalable, node-level cache sharing.

Intelligent routing analyzes incoming requests and directs them to the inference instance most likely to have relevant cached key-value pairs. The system examines the request and routes it based on one of the following routing strategies:
+ `prefixaware` — Subsequent requests with the same prompt prefix are routed to the same instance.
+ `kvaware` — Incoming requests are routed to the instance with the highest KV cache hit rate.
+ `session` — Requests from the same user session are routed to the same instance.
+ `roundrobin` — Distributes requests evenly without considering the state of the KV cache.

Intelligent routing works with all Amazon SageMaker HyperPod Inference deployment methods, including Amazon SageMaker JumpStart deployments (both console and kubectl), NVMe local storage deployments, and deployments from Amazon S3, Amazon FSx, or Hugging Face Hub. You can enable caching and routing regardless of which deployment method you use to serve your model.

**Note**  
KV caching and intelligent routing currently support only vLLM-based inference containers.

## Configure KV caching and intelligent routing
<a name="sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route"></a>

1. Enable KV caching by setting `enableL1Cache` and `enableL2Cache` to `true`. Then, configure `l2CacheSpec` by setting `l2CacheBackend` to either `redis` or `tieredstorage`. If you choose `redis`, update `l2CacheLocalUrl` with the Redis cluster URL.

   ```
     kvCacheSpec:
       enableL1Cache: true
       enableL2Cache: true
       l2CacheSpec:
         l2CacheBackend: <redis | tieredstorage>
         l2CacheLocalUrl: <Redis cluster URL if l2CacheBackend is redis >
   ```
**Note**  
If the Redis cluster is not within the same Amazon VPC as the HyperPod cluster, encryption for the data in transit is not guaranteed.
**Note**  
You do not need `l2CacheLocalUrl` if `tieredstorage` is selected.

1. Enable intelligent routing by setting `enabled` to `true` under `intelligentRoutingSpec`. You can specify which routing strategy to use under `routingStrategy`. If no routing strategy is specified, it defaults to `prefixaware`.

   ```
   intelligentRoutingSpec:
       enabled: true
       routingStrategy: <routing strategy to use>
   ```

1. Enable router metrics and caching metrics by setting `enabled` to `true` under `metrics`. The `port` value needs to be the same as the `containerPort` value under `modelInvocationPort`.

   ```
   metrics:
       enabled: true
       modelMetrics:
         port: <port value>
       ...
       modelInvocationPort:
         containerPort: <port value>
   ```

## KV-aware routing compatibility
<a name="sagemaker-hyperpod-model-deployment-kv-routing-compatibility"></a>

The compatibility matrix and version constraints in this section apply *only* to the `kvaware` routing strategy. The `kvaware` strategy directs incoming requests to the inference instance with the highest KV cache hit rate and currently supports only vLLM-based images with the `/completions` API as the invocation endpoint.

**Note**  
If you use `kvaware` routing, you must set `invocationEndpoint` to `/completions` in your deployment manifest. The `/v1/chat/completions` endpoint is not supported with `kvaware` routing. Other routing strategies (`prefixaware`, `session`, `roundrobin`) work with any invocation endpoint.

**Supported images:**
+ vLLM Image: [hub.docker.com/r/vllm/vllm-openai](https://hub.docker.com/r/vllm/vllm-openai)
+ LMCache Image: [hub.docker.com/r/lmcache/vllm-openai](https://hub.docker.com/r/lmcache/vllm-openai/tags)
+ AWS Deep Learning Container: [gallery.ecr.aws/deep-learning-containers/vllm](https://gallery.ecr.aws/deep-learning-containers/vllm)


| Inference Operator Version | Amazon EKS Add-on Version | LMCache Image Version | vLLM Image Version | 
| --- | --- | --- | --- | 
| >= v3.1.3 | >= v1.2.1-eksbuild.1 | >= v0.4.3 | >= v0.19.1 | 
| < v3.1.3 | < v1.2.1-eksbuild.1 | v0.3.9post2 | v0.11.1 | 

**Note**  
We recommend using inference operator version v3.1.3 or above with the corresponding LMCache and vLLM versions shown in the support matrix. Newer LMCache versions support tensor parallelism, improved failure handling, and cache worker registration, which provide better robustness for KV-aware routing.

### Validating KV cache aware routing
<a name="sagemaker-hyperpod-model-deployment-kv-routing-validation"></a>

After deploying a model with KV-aware routing enabled, use the following steps to verify that routing is working correctly.

#### Check worker registration
<a name="sagemaker-hyperpod-model-deployment-kv-routing-validation-registration"></a>

Verify that workers have registered with the router by checking the router logs:

```
kubectl logs -n hyperpod-inference-system <router-pod> | grep -i "register"
```

A healthy registration shows:

```
INFO: Worker registered: lmcacheengineconfig_<hash>
```

#### Check cache hits in router logs
<a name="sagemaker-hyperpod-model-deployment-kv-routing-validation-cache-hits"></a>

Verify that the router is using KV-aware routing to direct requests:

```
kubectl logs -n hyperpod-inference-system <router-pod> | grep -i "kvaware\|Matched instance\|Lookup"
```

When KV-aware routing is working correctly:

```
INFO: Routing request to lmcacheengineconfig_<hash> found by kvaware router
```

When KV-aware routing is not working (falls back to round-robin):

```
DEBUG: Matched instance url None
```

#### Check LMCache initialization in worker logs
<a name="sagemaker-hyperpod-model-deployment-kv-routing-validation-lmcache"></a>

Verify that LMCache initialized successfully on the worker pods:

```
kubectl logs -n <namespace> <worker-pod> | grep -i "LMCache"
```

A healthy initialization shows:

```
LMCache INFO: LMCacheManager initialized successfully
```

If LMCache failed to initialize, you will see:

```
LMCache ERROR: Failed to initialize LMCacheManager components: . System will operate in degraded mode (recompute).
```

#### Verify with Grafana metrics
<a name="sagemaker-hyperpod-model-deployment-kv-routing-validation-metrics"></a>

With metrics enabled (`metrics.enabled: true`), the following metrics from the vLLM worker `/metrics` endpoint confirm cache hits. These metrics should show high values when KV-aware routing is working correctly:


| Metric | Description | 
| --- | --- | 
| vllm:prefix\_cache\_hits\_total / vllm:prefix\_cache\_queries\_total | GPU prefix cache hit rate (computed as a ratio) | 
| lmcache:num\_vllm\_hit\_tokens\_total | Number of tokens served from LMCache | 
| lmcache:num\_lookup\_hits\_total / lmcache:num\_lookup\_tokens\_total | LMCache lookup hit rate (computed as a ratio) | 
| lmcache:request\_cache\_hit\_rate | Per-request cache hit rate (histogram) | 