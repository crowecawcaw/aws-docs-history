

# Disaggregated Prefill and Decode (DPD) deployment issues
<a name="sagemaker-hyperpod-model-deployment-ts-dpd"></a>

**Overview:** Common issues that can occur when deploying inference endpoints with Disaggregated Prefill and Decode (DPD). These problems typically involve pod startup, KV cache transfer, routing behavior, or resource allocation.

## Pod startup issues
<a name="sagemaker-hyperpod-model-deployment-ts-dpd-pod-startup"></a>

**Problem:** DPD pods fail to start or remain in a non-ready state.

**Symptoms and resolution:**
+ **Pods stuck in `ContainerCreating` for more than 10 minutes.** Run `kubectl describe pod <pod-name>` and look for `Failed to pull image` or `MountVolume.SetUp failed`. Verify the worker image exists and the Amazon S3 bucket is accessible from the cluster.
+ **Pods stuck at 2/3 Ready.** The vLLM worker is still loading the model. Llama 3.3 70B takes 5–10 minutes from a cold Amazon S3 fetch. Check progress:

  ```
  kubectl logs <pod-name> -c <prefill|decode>-<endpoint-name> | grep -i "engine\|loading"
  ```

  Wait for the log message indicating the engine is ready.
+ **Pods restart with `EngineDeadError` or `TimeoutError`.** This indicates an operator version older than v3.2. Upgrade the inference operator before continuing.
+ **All HTTP requests return 503 immediately after deploy.** Pods are still loading the model. Wait for the `InferenceEndpointConfig` status to reach `DeploymentComplete`:

  ```
  kubectl get inferenceendpointconfig <endpoint-name> -n <namespace> -w
  ```

## KV cache transfer issues
<a name="sagemaker-hyperpod-model-deployment-ts-dpd-kv-transfer"></a>

**Problem:** KV cache transfer between prefill and decode pods fails or performs poorly.

**Symptoms and resolution:**
+ **Decoder logs show `Retrieved 0 out of N required tokens`.** KV transfer did not occur and the decoder fell back to local recomputation. Verify that the `pd_role` is correct (prefiller must be `sender`, decoder must be `receiver`), both pods use the same worker image, and `PYTHONHASHSEED` is set to `"0"` on both pods.
+ **Decoder logs show `Failed to allocate memory object, retrying...`** The decoder PD buffer is full under high concurrency. Either increase `PD_BUFFER_SIZE` (try `"17179869184"` for 16 GiB or `"34359738368"` for 32 GiB) or scale `decodingSpec.replicas`.
+ **KV transfer throughput below 1 GB/s.** EFA is not being used and transfers are falling back to CPU. Verify that both pods are scheduled on EFA-capable nodes in the same Availability Zone, that nodes have EFA resources available (`kubectl describe node <node-name> | grep efa`), and that the worker image includes the EFA libfabric provider.

## Routing issues
<a name="sagemaker-hyperpod-model-deployment-ts-dpd-routing"></a>

**Problem:** Requests are not being routed correctly between prefill and decode pods.

**Symptoms and resolution:**
+ **All requests bypass the prefiller (even long prompts).** Check the router logs for routing decisions:

  ```
  ROUTER_POD=$(kubectl get pods -n hyperpod-inference-system -o name | grep router | head -1)
  kubectl logs $ROUTER_POD -n hyperpod-inference-system -c router-container --tail=50 \
    | grep "Conditional routing"
  ```

  Verify the `estimated_tokens` value exceeds your `routingThreshold`. If the token estimate is lower than expected, the router's tokenizer may be counting differently — try lowering `routingThreshold`.
+ **Uneven load distribution across prefillers.** If you have multiple prefiller replicas and observe that one is overloaded while others are idle, switch the routing strategy to `roundrobin` for even distribution. Alternatively, use `kvaware` for cache-aware distribution that accounts for the actual state of each prefiller.