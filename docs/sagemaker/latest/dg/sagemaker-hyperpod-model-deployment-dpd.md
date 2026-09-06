

# Disaggregated Prefill and Decode for HyperPod inference
<a name="sagemaker-hyperpod-model-deployment-dpd"></a>

Disaggregated Prefill and Decode (DPD) separates the two phases of LLM inference, prefill and decode, onto dedicated GPU pools and transfers key-value (KV) cache between them over Elastic Fabric Adapter (EFA) using GPU-Direct Remote Direct Memory Access (RDMA).

When prefill and decode run on the same GPU (colocated), a single long-context request can stall in-flight token streams for other clients, inflating per-token latency under load. DPD removes this interference by running compute-bound prefill on one set of GPUs and memory-bandwidth-bound decode on another, producing more predictable latency under mixed traffic and letting you scale each phase independently.

The inference operator handles the orchestration, which includes provisioning the router, wiring prefill and decode pods together via LMCache and NIXL, and integrating with HyperPod observability. You can enable DPD by adding a `pdSpec` section to the same `InferenceEndpointConfig` resource you already use for inference endpoints.

## When DPD helps
<a name="sagemaker-hyperpod-model-deployment-dpd-when"></a>

DPD delivers the most benefit when all of the following conditions are present:
+ **Large dense models** — 70B\+ parameters (for example, Llama 3.3 70B).
+ **Long inputs** — 4,000\+ input tokens. Inter-token latency (ITL) improvement scales with input length because longer prefills cause more decode interference when colocated.
+ **Sustained concurrency** — 2\+ requests per second. Without concurrent requests competing for the same GPU, there is nothing to disaggregate.
+ **Moderate or long outputs** — 256\+ output tokens. More output tokens means more cumulative benefit from stable per-token latency.

If your workload has short inputs, low concurrency, or uses small models, a standard colocated deployment is simpler and performs well.

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-dpd-prereqs"></a>

Before deploying inference endpoints that use Disaggregated Prefill and Decode, you need the following components set up in your local development environment:
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
+ Access to your HyperPod Amazon EKS cluster via [kubectl](https://kubernetes.io/docs/tasks/tools/)
+ [Hugging Face](https://huggingface.co/) token that allows read access to the respective model checkpoint. This is not required if the model checkpoint is already located in an Amazon S3 bucket.
+ A worker image that includes vLLM, LMCache, NVIDIA NIXL, and the EFA libfabric provider. The following image options are supported:
  + DLC: `public.ecr.aws/deep-learning-containers/vllm:server-hyperpod-cuda-v1.1`
  + LMCache: `lmcache/vllm-openai:v0.4.3`

  Both images include LMCache 0.4.3, vLLM 0.19.0, and NIXL 1.0.0.
+ HyperPod Inference Operator **version 3.2 or later** installed. DPD is not supported on earlier versions. The operator is installed by default in newly created HyperPod Amazon EKS clusters. If you intend to use an existing cluster, follow the installation instructions in [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md). Verify your version:

  ```
  kubectl get deployment hyperpod-inference-operator-controller-manager \
    -n hyperpod-inference-system \
    -o jsonpath='{.spec.template.spec.containers[?(@.name=="manager")].image}{"\n"}'
  ```

**Important**  
Disaggregated Prefill and Decode requires EFA-capable instances with GPU-Direct RDMA support. The following instance types are supported: `ml.p5.48xlarge`, `ml.p5e.48xlarge`, `ml.p5en.48xlarge`, `ml.p6-b200.48xlarge`, `ml.p6-b300.48xlarge`. Other instance types are not supported for DPD.

## Deploy a DPD endpoint
<a name="sagemaker-hyperpod-model-deployment-dpd-deploy"></a>

Most `InferenceEndpointConfig` fields are shared with non-DPD endpoints and documented in [Deploy foundation models and custom fine-tuned models](sagemaker-hyperpod-model-deployment-deploy.md). To enable DPD, add the following sections to your manifest.

### Prefill-Decode Spec: `pdSpec`
<a name="sagemaker-hyperpod-model-deployment-dpd-fields-pdspec"></a>

Declares the prefill/decode topology and specifies arguments. Presence of this field is what makes the endpoint disaggregated: the operator creates separate Deployments for prefill and decode and wires them together via the router and LMCache PD backend.

```
pdSpec:
  prefillSpec:
    replicas: 1
    resources:
      limits:
        nvidia.com/gpu: ${GPUS_PER_NODE}
      requests:
        nvidia.com/gpu: ${GPUS_PER_NODE}
    args:
      - "--gpu-memory-utilization"
      - "0.75"
  decodingSpec:
    replicas: 1
    resources:
      limits:
        nvidia.com/gpu: ${GPUS_PER_NODE}
      requests:
        nvidia.com/gpu: ${GPUS_PER_NODE}
  routingThreshold: 4096
```

`replicas`  
Scale prefill and decode independently.

`resources`  
Applied to the role's pod spec. Top-level `worker.resources` is ignored for DPD pods; per-role values override.

`routingThreshold`  
Token length threshold that routes requests to the disaggregated path. Requests that do not meet this threshold bypass the prefiller and go directly to the decoder.

`args`  
vLLM flags specific to that role. Merged into `worker.args` at startup: flags already in `worker.args` are replaced with the per-role value; flags not present are appended.

### DPD Environment Variables: `environmentVariables`
<a name="sagemaker-hyperpod-model-deployment-dpd-fields-env"></a>

These environment variables are applied identically to both the prefiller and decoder containers; there is no per-role env-var field. For per-role behavior, use `pdSpec.{prefillSpec,decodingSpec}.args` instead.

```
environmentVariables:
  - name: PD_BUFFER_SIZE
    value: "8589934592"
  - name: LMCACHE_SAVE_DECODE_CACHE
    value: "False"
  - name: PYTHONHASHSEED
    value: "0"
```

`PD_BUFFER_SIZE` (8 GiB)  
GPU buffer reserved on the decoder for incoming KV cache transfers, sized per rank. For Llama 70B at TP=8, each token's KV cache is approximately 40 KB per rank, so a 6000-token prompt occupies approximately 0.23 GB per rank and 8 GiB holds approximately 35 such in-flight transfers. When the buffer exceeds capacity, the decoder logs `Failed to allocate memory object, retrying...` and clients see latency spikes. Increase to 16/32 GiB or scale `decodingSpec.replicas` if needed.

`LMCACHE_SAVE_DECODE_CACHE`: `"False"`  
Disables redundant L1 caching on the decoder. The prefiller is the source of truth for cache hits.

`PYTHONHASHSEED`: `"0"`  
LMCache uses Python's built-in `hash()` to compute prompt-token cache keys. Python randomizes that hash seed per process by default, so identical prompts produce different keys on prefiller and decoder and lookups miss. Pinning the seed makes the keys agree across pods.

### Configure the routing strategy
<a name="sagemaker-hyperpod-model-deployment-dpd-fields-routing"></a>

The `intelligentRoutingSpec` section sets the routing strategy the DPD router uses to select a prefiller for each request. The router is created automatically when `pdSpec` is present; this section is optional and defaults to `prefixaware`.

```
intelligentRoutingSpec:
  enabled: true
  routingStrategy: prefixaware
```

DPD can also be integrated with intelligent routing and KV caching. For more information, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route).

With a single prefill replica, all strategies route to that replica. The choice only affects behavior when `prefillSpec.replicas > 1`:
+ For a single prefill replica, use `prefixaware` (the default) to maximize KV cache hits when prompts share common prefixes such as system prompts or chat history.
+ For multiple prefill replicas, use `roundrobin` to distribute load evenly across replicas and avoid hot-spotting a single prefiller.

### Complete example
<a name="sagemaker-hyperpod-model-deployment-dpd-deploy-example"></a>

The following manifest deploys Llama 3.3 70B on two ml.p5.48xlarge instances (one prefiller, one decoder):

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: dpd-test
  namespace: default
spec:
  endpointName: dpd-test
  instanceType: ml.p5.48xlarge
  invocationEndpoint: v1/chat/completions
  modelName: Llama-3.3-70B-Instruct
  modelSourceConfig:
    modelSourceType: s3
    modelLocation: Llama-3.3-70B-Instruct
    s3Storage:
      bucketName: <YOUR_BUCKET>
      region: <YOUR_REGION>
  loadBalancer:
    healthCheckPath: /health
  metrics:
    enabled: true
  kvCacheSpec:
    enableL1Cache: true
  intelligentRoutingSpec:
    enabled: true
    routingStrategy: prefixaware
  pdSpec:
    prefillSpec:
      replicas: 1
      resources:
        requests:
          nvidia.com/gpu: "8"
        limits:
          nvidia.com/gpu: "8"
    decodingSpec:
      replicas: 1
      resources:
        requests:
          nvidia.com/gpu: "8"
        limits:
          nvidia.com/gpu: "8"
    routingThreshold: 4096
  worker:
    image: public.ecr.aws/deep-learning-containers/vllm:server-hyperpod-cuda-v1.1
    args:
      - "--model"
      - "/opt/ml/model"
      - "--host"
      - "0.0.0.0"
      - "--port"
      - "8000"
      - "--tensor-parallel-size"
      - "8"
      - "--max-model-len"
      - "16384"
      - "--gpu-memory-utilization"
      - "0.75"
    modelInvocationPort:
      name: http
      containerPort: 8000
    modelVolumeMount:
      name: model-weights
      mountPath: /opt/ml/model
    resources:
      requests:
        cpu: "96"
        memory: 1024Gi
        nvidia.com/gpu: "8"
      limits:
        cpu: "96"
        memory: 1024Gi
        nvidia.com/gpu: "8"
    environmentVariables:
      - name: HF_HOME
        value: /tmp/hf_home
      - name: PD_BUFFER_SIZE
        value: "8589934592"
      - name: LMCACHE_SAVE_DECODE_CACHE
        value: "False"
      - name: PYTHONHASHSEED
        value: "0"
```

Apply the manifest:

```
kubectl apply -f inference_endpoint_dpd_config.yaml
```

## Verify the deployment
<a name="sagemaker-hyperpod-model-deployment-dpd-verify"></a>

Image pull and model loading take several minutes. Monitor pod status:

```
kubectl get pods -A \
  | grep -E "prefill-|decode-|router"
```

A healthy deployment shows:

```
NAMESPACE                   NAME                                   READY   STATUS    RESTARTS   AGE
default                     prefill-dpd-test-XXXX                  3/3     Running   0          7m
default                     decode-dpd-test-XXXX                   3/3     Running   0          7m
hyperpod-inference-system   dpd-test-router-XXXX                   2/2     Running   0          7m
```

Each model pod has 3 containers (vLLM worker, Nginx reverse proxy, OpenTelemetry collector). The router pod has 2 containers (router, OpenTelemetry collector). Check the `InferenceEndpointConfig` status:

```
kubectl get inferenceendpointconfig dpd-test -n default \
  -o jsonpath='{.status.conditions[0].message}{"\n"}'
```

Expected output: `DPD prefill and decode deployments are ready`

### Verify DPD roles
<a name="sagemaker-hyperpod-model-deployment-dpd-verify-roles"></a>

Confirm the prefiller reports `sender` and the decoder reports `receiver`. This is the single most discriminating startup signal — if both pods report the same role or neither prints the line, the operator did not wire DPD correctly.

```
PREFILL_POD=$(kubectl get pod -n ${NAMESPACE} \
  -l 'inference.sagemaker.aws.amazon.com/dpd-role=prefill' \
  -o jsonpath='{.items[0].metadata.name}')

DECODE_POD=$(kubectl get pod -n ${NAMESPACE} \
  -l 'inference.sagemaker.aws.amazon.com/dpd-role=decode' \
  -o jsonpath='{.items[0].metadata.name}')

kubectl logs $PREFILL_POD -n ${NAMESPACE} -c prefill-${DEPLOYMENT_NAME} \
  | grep -oE "'pd_role': '[a-z]+'" | sort -u

kubectl logs $DECODE_POD -n ${NAMESPACE} -c decode-${DEPLOYMENT_NAME} \
  | grep -oE "'pd_role': '[a-z]+'" | sort -u
```

Expected output:

```
'pd_role': 'sender'
'pd_role': 'receiver'
```

## Invoke the endpoint
<a name="sagemaker-hyperpod-model-deployment-dpd-invoke"></a>

Once the endpoint is ready, send a short and a long prompt to exercise both routing paths, then check the logs to confirm KV transfer over EFA.

```
PREFILL_POD=$(kubectl get pod -n ${NAMESPACE} \
  -l 'inference.sagemaker.aws.amazon.com/dpd-role=prefill' \
  -o jsonpath='{.items[0].metadata.name}')

DECODE_POD=$(kubectl get pod -n ${NAMESPACE} \
  -l 'inference.sagemaker.aws.amazon.com/dpd-role=decode' \
  -o jsonpath='{.items[0].metadata.name}')

ROUTER_POD=$(kubectl get pods -n hyperpod-inference-system -o name \
  | grep -- "${DEPLOYMENT_NAME}-${NAMESPACE}-router" | head -1)

ROUTER_URL=http://${DEPLOYMENT_NAME}-${NAMESPACE}-routing-service.hyperpod-inference-system.svc.cluster.local:443/v1/chat/completions
```

### Short prompt (under threshold, direct to decoder)
<a name="sagemaker-hyperpod-model-deployment-dpd-invoke-short"></a>

Requests with fewer tokens than `routingThreshold` bypass the prefiller and go directly to the decoder:

```
kubectl run curl-short --rm -it --image=curlimages/curl --restart=Never -- \
  curl -s -k -X POST "$ROUTER_URL" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "/opt/ml/model",
      "messages": [{"role": "user", "content": "What is disaggregated prefill-decode in one sentence?"}],
      "max_tokens": 80,
      "temperature": 0.0
    }'
```

### Long prompt (exceeds threshold, DPD path)
<a name="sagemaker-hyperpod-model-deployment-dpd-invoke-long"></a>

Requests that exceed the threshold route through the prefiller for KV cache computation, then to the decoder for token generation:

```
kubectl run curl-long --rm -it --image=curlimages/curl --restart=Never -- sh -c '
LONG=""
i=0; while [ $i -lt 600 ]; do LONG="${LONG}The quick brown fox jumps over the lazy dog. "; i=$((i+1)); done
curl -s -k -X POST "'"$ROUTER_URL"'" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"/opt/ml/model\",\"messages\":[{\"role\":\"user\",\"content\":\"${LONG}\"}],\"max_tokens\":30,\"temperature\":0.0}"
'
```

### Verify KV transfer
<a name="sagemaker-hyperpod-model-deployment-dpd-invoke-verify-kv"></a>

After sending a long prompt, confirm the KV cache was transferred by checking decoder logs:

```
kubectl logs $DECODE_POD -n ${NAMESPACE} -c decode-${DEPLOYMENT_NAME} \
  | grep -E "Retrieved.*tokens.*throughput" | tail -2
```

Expected output (one line per TP rank):

```
[Worker_TP5] [LMCache INFO] [req_id=cmpl-...] Retrieved 6035 out of 6035 required tokens (from 6035 total tokens).
   size: 0.2344 gb, cost 1.3304 ms, throughput: 176.1686 GB/s
```

`Retrieved N out of N required tokens` with N > 0 confirms KV cache crossed the NIXL channel successfully. If you see `Retrieved 0 out of N`, the decoder fell back to local recomputation — see [Disaggregated Prefill and Decode (DPD) deployment issues](sagemaker-hyperpod-model-deployment-ts-dpd.md).

You can also verify the routing decision in the router logs:

```
kubectl logs $ROUTER_POD -n hyperpod-inference-system -c router-container --tail=20 \
  | grep -E "Conditional routing"
```

For the long prompt, you should see:

```
[INFO] Conditional routing: estimated_tokens=6750, threshold=4096, disaggregate=True
```

For the short prompt:

```
[INFO] Conditional routing: estimated_tokens=12, threshold=4096, disaggregate=False
```

**Note**  
To invoke through a SageMaker AI AI endpoint, set `endpointName` in your `InferenceEndpointConfig`. If `endpointName` is not set, no SageMaker AI AI endpoint is created and only direct ALB invocation is available.

## Observability
<a name="sagemaker-hyperpod-model-deployment-dpd-observability"></a>

Enable metrics by setting `metrics.enabled: true` in your `InferenceEndpointConfig`. DPD metrics are available in the HyperPod inference dashboard. For more information, see [Implementing inference observability on HyperPod clusters](sagemaker-hyperpod-model-deployment-observability.md).

The following DPD-specific metrics are available:


**DPD-specific metrics**  

| Metric | Description | 
| --- | --- | 
| E2E TTFT | Overall time to first token (prefill \+ KV transfer \+ routing) | 
| Prefill TTFT | Prefiller-only latency | 
| Prefill Queue | Number of requests waiting for prefill | 
| Decode Queue | Number of requests waiting on the decoder | 
| Prefill Time | Time spent on prefill computation | 
| Decode Latency | Per-token output latency (TPOT) | 
| KV Transfer Time | Time to transfer KV cache from prefiller to decoder | 
| DPD Routing Counts | Disaggregated vs. fallback (under-threshold) requests | 

## Tune your DPD deployment
<a name="sagemaker-hyperpod-model-deployment-dpd-tuning"></a>

The following table provides a quick reference for tuning DPD based on the symptoms you observe in your metrics dashboard.


**DPD tuning reference**  

| Config | What it does | Default | When to tune | 
| --- | --- | --- | --- | 
| pdSpec.routingThreshold | Minimum input tokens to route through the prefiller. Requests under this threshold go directly to the decoder. | 4096 | The default works well for most workloads. Setting it too low increases TTFT due to unnecessary KV transfers on short prompts, while setting it too high limits TPOT improvement because fewer requests take the DPD path. | 
| pdSpec.prefillSpec.replicas | Number of prefill pods. | 1 | Scale up if prefill queue depth is high in order to improve prefill TTFT. | 
| PD\_BUFFER\_SIZE | Decoder GPU buffer for incoming KV transfers (per rank). 8 GiB holds approximately 35 in-flight 6K-token transfers for 70B at TP=8. | "8589934592" (8 GiB) | Increase to handle more concurrent KV transfers. Decrease if you see memory issues. When increasing, you may need to lower --gpu-memory-utilization on the decoder to free GPU memory for the larger buffer. | 
| --gpu-memory-utilization | Fraction of GPU memory vLLM uses for weights, activations, and KV cache. | 0.75 | Increase for more KV cache headroom on long inputs. Risk: prefiller OOM because prefill also needs memory for activations. Test with your actual input length distribution. | 
| --max-num-seqs | Max concurrent sequences per worker batch. | 16 (prefiller), 32 (decoder) | Raise for better batching under load. Lower if hitting OOM on the prefiller. Set per-role via pdSpec.{prefillSpec,decodingSpec}.args. | 
| intelligentRoutingSpec.routingStrategy | How the router selects a prefiller when multiple replicas exist. | prefixaware | Use roundrobin to evenly distribute load across multiple prefiller replicas. Use prefixaware or kvaware with a single prefiller or when prompts share common prefixes (system prompts, chat history) to maximize cache hits. | 

Test with your actual workload and input length distribution.

To apply configuration changes, edit your deployment YAML and re-apply:

```
kubectl apply -f inference_endpoint_dpd_config.yaml
```

## Known limitations
<a name="sagemaker-hyperpod-model-deployment-dpd-limitations"></a>
+ DPD is recommended for dense models with 70B or more parameters. Smaller models and Mixture-of-Experts models typically do not benefit from disaggregation.
+ The current release supports a single decode deployment per endpoint. Support for multiple decode deployments is planned for a future release.
+ Performance is validated up to 64 concurrent requests on ml.p5.48xlarge with Llama 3.3 70B.
+ To revert from a DPD deployment to a standard colocated deployment, apply a new `InferenceEndpointConfig` without `pdSpec`.

For troubleshooting DPD deployments, see [Disaggregated Prefill and Decode (DPD) deployment issues](sagemaker-hyperpod-model-deployment-ts-dpd.md).