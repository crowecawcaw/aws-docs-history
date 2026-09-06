

# Model weights caching and image caching
<a name="sagemaker-hyperpod-model-deployment-model-caching"></a>

When you scale out an inference deployment, each new pod must pull the inference server container image from a registry. It must also download model weights from remote storage (Amazon S3 or Amazon FSx) before it can serve traffic. For large language models, downloading model weights and pulling container images contribute most to cold start latency.

To eliminate these bottlenecks during scale-out, configure one or both of the following host-local caching mechanisms in Amazon SageMaker HyperPod Inference:

Model weights caching (`weightsCache`)  
Pre-populates model weight files on host-local NVMe storage on each eligible node. Inference pods on the same node load weights from local storage instead of downloading them from the remote model source, eliminating redundant downloads across pods.

Image caching (`imageCache`)  
Pre-pulls the inference server container image onto target nodes so that new pods start without waiting for a cold image pull.

You configure both caching mechanisms through the `modelCacheConfig` field on your `InferenceEndpointConfig` or `JumpStartModel` deployment.

You can enable weights caching and image caching independently or together. Both features work with all Amazon SageMaker HyperPod Inference model sources, including Amazon SageMaker JumpStart deployments (both open-weights and gated models) and custom models from Amazon S3 or Amazon FSx.

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-model-caching-prereqs"></a>

Before you enable caching, verify the following:

Instance type with local NVMe storage  
Model weights caching stores weights on host-local NVMe storage (`/opt/dlami/nvme` by default). Your instance type must provide local NVMe storage at the configured `hostPath`.

Sufficient NVMe capacity  
Ensure the node has enough local storage for your model. Each deployment uses its own isolated cache directory, so multiple cached deployments on the same node each consume their own storage.

Inference operator  
Your cluster must have a version of the HyperPod Inference operator that supports model caching. If the `modelCacheConfig` field is not recognized, update the inference operator add-on to the latest version.

**Important**  
If your instance type does not have local NVMe storage at the configured `hostPath`, model weights caching does not warm the cache and inference pods fall back to downloading weights from the remote model source. Verify that your instance type provides local NVMe storage before enabling this feature.

## Configure model weights caching and image caching
<a name="sagemaker-hyperpod-model-deployment-model-caching-configure"></a>

Add a `modelCacheConfig` block to the `spec` of your `InferenceEndpointConfig` or `JumpStartModel` resource. The following example enables both model weights caching and image caching.

```
spec:
  # ... model source, worker, and TLS configuration ...
  modelCacheConfig:
    weightsCache:
      enabled: true
      hostPath: /opt/dlami/nvme
    imageCache:
      enabled: true
```

The `modelCacheConfig` field supports the following sub-fields.


| Field | Default | Description | 
| --- | --- | --- | 
| weightsCache.enabled | false | Whether host-local model weights caching is enabled. When true, the operator pre-populates model weights on host-local storage and mounts them into inference pods. | 
| weightsCache.hostPath | /opt/dlami/nvme | The host path where cached model weights are stored. Must be a non-empty absolute path of at most 255 characters. | 
| imageCache.enabled | false | Whether container image caching is enabled. When true, the operator pre-pulls the inference server container image onto target nodes. | 

## How model weights caching works
<a name="sagemaker-hyperpod-model-deployment-model-caching-weights"></a>

When `weightsCache.enabled` is `true`, the operator downloads model weights from the remote model source (Amazon S3 or Amazon FSx) to host-local NVMe storage on each eligible node before inference pods start serving traffic. Inference pods mount the cached weights read-only and load the model from local storage instead of downloading it from the remote source repeatedly.

The operator populates the cache on nodes that match the scheduling constraints of the inference deployment, and labels each node when its cache is warm. The inference deployment uses *preferred* node affinity on this label, so pods are scheduled onto warm nodes when available but can still schedule elsewhere.

Isolation  
Each deployment uses an isolated, per-deployment cache directory under the configured `hostPath`, so multiple model deployments on the same node do not interfere with each other.

Cache miss fallback  
If a pod is scheduled on a node where the cache is not yet available, the deployment falls back to loading model weights directly from the remote model source, so deployments remain functional even without a warm cache.

Node replacement  
If a node is replaced (for example, after a failure), the operator must warm the cache on the new node again before pods are preferentially scheduled to it. Existing warm nodes continue serving traffic in the meantime.

Cleanup on delete  
When you delete the deployment, the operator removes the cached weight files from the nodes it populated.

## How image caching works
<a name="sagemaker-hyperpod-model-deployment-model-caching-image"></a>

When `imageCache.enabled` is `true`, the operator pre-pulls the inference server container image onto target nodes. Because the image is already present on the node, new inference pods avoid the cold image pull that would otherwise delay pod startup. This is especially beneficial for large inference server images and for deployments that scale out frequently.

Image caching is independent of model weights caching. You can enable it on its own, or combine it with weights caching to reduce both image-pull and weight-download time during scale-out.

## Verify that caching is working
<a name="sagemaker-hyperpod-model-deployment-model-caching-verify"></a>

Use the following checks to confirm that caching is active for your deployment.

### Check node labels for a warm cache
<a name="sagemaker-hyperpod-model-deployment-model-caching-verify-labels"></a>

When a node's cache is warm, the operator applies a cache-ready label to it. Model weights caching uses a label with the prefix `inference.sagemaker.aws.amazon.com/weights-cache-ready.`, and image caching uses the prefix `inference.sagemaker.aws.amazon.com/image-cache-ready.`, each suffixed with the cache configuration's UID.

```
kubectl get nodes --show-labels | grep "cache-ready"
```

No output means no nodes have warmed the cache yet.

### Check pod events for the cache mount
<a name="sagemaker-hyperpod-model-deployment-model-caching-verify-pod"></a>

Inspect an inference pod and confirm it mounts the host-local cache path read-only. If the hostPath volume is absent, the pod is loading weights from remote storage.

```
kubectl describe pod {{inference-pod-name}} -n {{namespace}}
```

### Check operator logs
<a name="sagemaker-hyperpod-model-deployment-model-caching-verify-logs"></a>

Review the inference operator logs for cache warm-up activity or errors.

```
kubectl logs -n hyperpod-inference-system deployment/hyperpod-inference-controller-manager | grep -i "cache"
```

## Troubleshooting
<a name="sagemaker-hyperpod-model-deployment-model-caching-troubleshooting"></a>


| Symptom | Possible cause | Resolution | 
| --- | --- | --- | 
| Pods start slowly even though caching is enabled. | The NVMe path does not exist on the instance type. | Verify that your instance type has local NVMe storage and that hostPath matches the actual mount point. | 
| The cache never warms. | Insufficient disk space at the host path. | Check available capacity at hostPath. Large models can require substantial local storage. | 
| No nodes are labeled as cache-ready. | The cache download failed, or the remote source is unreachable. | Check the operator logs for download errors and verify network access to Amazon S3 or Amazon FSx. | 
| Multiple deployments cause disk pressure on a node. | Cached deployments share the same node NVMe storage. | Use separate instance groups or reduce the number of concurrent cached deployments per node. | 

## Considerations
<a name="sagemaker-hyperpod-model-deployment-model-caching-considerations"></a>
+ Model weights caching requires instance types with local NVMe storage. EBS-only instances are not supported.
+ The maximum cacheable model size is bounded by the available NVMe capacity on the instance type.
+ Cache warm-up time depends on model size and network throughput to the remote model source.