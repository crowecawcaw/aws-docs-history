

# Configure request limits for your HyperPod inference model deployment
<a name="sagemaker-hyperpod-model-deployment-request-limits"></a>

You can configure request limiting on your Amazon SageMaker HyperPod inference model deployments to control the number of concurrent requests each pod accepts. When the limit is reached, excess requests receive a configurable HTTP error response, enabling fail-fast behavior and allowing the load balancer to redirect traffic to other pods.

Request limiting is enforced by the nginx sidecar proxy that runs alongside your model container. This requires metrics to be enabled on your deployment.

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-request-limits-prereqs"></a>

Before configuring request limits, verify that:
+ Metrics are enabled on your deployment (`metrics.enabled: true`). The nginx sidecar proxy that enforces request limits is only created when metrics is enabled.

## Configure request limits in your deployment YAML
<a name="sagemaker-hyperpod-model-deployment-request-limits-configure"></a>

Add the `requestLimits` section under `worker` in your `InferenceEndpointConfig` YAML. The following example limits each pod to 10 concurrent requests with a queue of 5, returning HTTP 503 when limits are exceeded.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: my-model
  namespace: ns-team-a
spec:
  modelName: my-model-name
  instanceType: ml.g5.8xlarge
  invocationEndpoint: invocations
  modelSourceConfig:
    modelSourceType: s3
    s3Storage:
      bucketName: my-model-bucket
      region: us-east-2
      modelLocation: models/my-model
  worker:
    image: my-model-image:latest
    modelInvocationPort:
      containerPort: 8080
      name: http
    modelVolumeMount:
      mountPath: /opt/ml/model
      name: model-weights
    resources:
      limits:
        nvidia.com/gpu: "1"
      requests:
        cpu: "4"
        memory: "32Gi"
        nvidia.com/gpu: "1"
    requestLimits:
      maxConcurrentRequests: 10
      maxQueueSize: 5
      overflowStatusCode: 503
  metrics:
    enabled: true
  tlsConfig:
    tlsCertificateOutputS3Uri: "s3://my-tls-bucket/certs"
```

## Explanation of fields
<a name="sagemaker-hyperpod-model-deployment-request-limits-fields"></a>

`maxConcurrentRequests` (Optional, Integer)  
Maximum number of concurrent requests the nginx sidecar proxy accepts per pod. When the limit is reached, new requests are either queued (if `maxQueueSize` is configured) or immediately rejected with the overflow status code. Minimum: 1. If not set or set to 0, no concurrency limit is enforced.

`maxQueueSize` (Optional, Integer)  
Maximum number of requests to queue when the concurrent request limit is reached. Queued requests wait until an in-flight request completes. When the queue is full, new requests receive the overflow status code response. Minimum: 0. If not set or set to 0, no queuing is applied — requests are rejected immediately when the concurrent request limit is reached.

`overflowStatusCode` (Optional, Integer)  
HTTP status code returned when request limits are exceeded. Must be between 400 and 599. Default: 429 (Too Many Requests). Common values:  
+ `429` — Too Many Requests (default). Standard HTTP status for rate limiting.
+ `503` — Service Unavailable. Useful when you want the load balancer to retry on a different pod.

## How request limiting works
<a name="sagemaker-hyperpod-model-deployment-request-limits-how-it-works"></a>

When an inference request arrives at the nginx sidecar proxy:

1. If the number of active requests is below `maxConcurrentRequests`, the request is forwarded to the model container.

1. If the limit is reached and `maxQueueSize` is greater than 0, the request is queued and waits (up to 60 seconds) for an active slot to become available.

1. If the queue is full (or no queue is configured), the request is immediately rejected with the configured `overflowStatusCode` and a JSON error response:

   ```
   {
     "error": "Too many concurrent requests",
     "max_concurrent": 10,
     "max_queue_size": 5,
     "current": 10
   }
   ```

## Examples
<a name="sagemaker-hyperpod-model-deployment-request-limits-examples"></a>

**Strict concurrency limit without queuing**

To reject excess requests immediately without queuing:

```
requestLimits:
  maxConcurrentRequests: 5
  overflowStatusCode: 429
```

**Concurrency limit with queuing**

To allow a small queue before rejecting:

```
requestLimits:
  maxConcurrentRequests: 10
  maxQueueSize: 5
  overflowStatusCode: 503
```

In this configuration, up to 10 requests are processed concurrently. When the 11th through 15th requests arrive, they are queued and wait for an active slot. The 16th request and beyond receive HTTP 503.