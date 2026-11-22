

# Troubleshooting GPU-accelerated functions on Lambda Managed Instances

This page describes issues that are specific to GPU-accelerated functions. For issues not listed here, see [Troubleshooting Lambda Managed Instances](lambda-managed-instances-troubleshooting.md).

Issues caused by an invalid configuration of a GPU-accelerated function are reported when you publish a function version. The state reason of that version identifies the cause. To view the state and state reason of a version, use the following command:

```bash
aws lambda get-function-configuration \
  --function-name my-gpu-function:1 \
  --query '[State,StateReasonCode,StateReason]'
```

## Function configuration issues
<a name="lambda-managed-instances-gpu-troubleshooting-config"></a>

### Creating a function fails with `InvalidParameterValueException`
<a name="lambda-managed-instances-gpu-troubleshooting-config-invalidparam"></a>

**Problem:** You receive an `InvalidParameterValueException` when you create or update a function, and the error asks you to use a capacity provider with larger GPU instances or to reduce the accelerator memory.

**Cause:** No instance type in the capacity provider has a GPU with at least the `AcceleratorMemorySize` you requested. For example, a capacity provider with only G4dn instance types, which have 16 GB per GPU, cannot satisfy a request for 24 GB.

**Solutions:**
+ **Lower the accelerator memory:** Set `AcceleratorMemorySize` to a value that an instance type in the capacity provider provides. The supported values are 3, 6, 12, 16, 24, and 48 GB, and the GPU memory of each instance family is listed in [Supported GPU instances](lambda-managed-instances-gpu.md#lambda-managed-instances-gpu-supported-instances).
+ **Add an instance type with a larger GPU:** Add it to the capacity provider's `AllowedInstanceTypes` list.

### Version publish fails with `IncompatibleAcceleratorInstanceTypes`
<a name="lambda-managed-instances-gpu-troubleshooting-config-incompatible"></a>

**Problem:** Publishing a version fails with the state reason code `IncompatibleAcceleratorInstanceTypes`, and the message says that the accelerator memory requirements exceed the allowed instance types even though the capacity provider lists an instance type with enough GPU memory.

**Cause:** The accelerator memory is sufficient, but the vCPU count is not. An execution environment has to fit both on one instance type in the capacity provider. The vCPU count is `MemorySize` divided by `ExecutionEnvironmentMemoryGiBPerVCpu`, which defaults to 2 GiB per vCPU, so a 16,384 MB function needs 8 vCPUs, every vCPU on a `g6.2xlarge`, and no listed instance type qualifies.

**Solutions:**
+ **Raise the memory to vCPU ratio:** Increase `ExecutionEnvironmentMemoryGiBPerVCpu` so that the same `MemorySize` needs fewer vCPUs. At 4 GiB per vCPU, 16,384 MB needs 4 vCPUs and fits on a `g6.2xlarge`.

  ```bash
  aws lambda update-function-configuration \
    --function-name my-gpu-function \
    --capacity-provider-config '{
      "LambdaManagedInstancesCapacityProviderConfig": {
        "CapacityProviderArn": "arn:aws:lambda:us-east-2:111122223333:capacity-provider:my-gpu-capacity-provider",
        "ExecutionEnvironmentMemoryGiBPerVCpu": 4.0
      }
    }'
  ```
+ **Lower MemorySize:** Reduce the function's memory so that it needs fewer vCPUs.
+ **Specify larger instance sizes:** Add instances with larger sizes from the same families to the capacity provider's `AllowedInstanceTypes` list.

## Capacity provider issues
<a name="lambda-managed-instances-gpu-troubleshooting-capacity"></a>

### Insufficient GPU capacity
<a name="lambda-managed-instances-gpu-troubleshooting-capacity-insufficient"></a>

**Problem:** The version fails with a state reason that reports `InsufficientCapacityException`, or the capacity provider stops scaling out under load.

**Cause:** None of the GPU instance types in `AllowedInstanceTypes` are available in the capacity provider's Availability Zones at that moment. Lambda attempts the latest generation first and falls back to older generations in the list, and when every instance type is unavailable the launch fails. GPU instance types are in shorter supply than CPU instance types, so this can happen more often for GPU-accelerated functions. For more information about instance type selection, see [Instance Type Selection](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-instance-selection).

**Solutions:**
+ **Specify more instance types and Availability Zones:** Add instance types from more generations, such as G6, G5, and G4dn sizes together, and specify subnets across more Availability Zones.
+ **Reserve capacity:** For production workloads, purchase an Amazon EC2 On-Demand Capacity Reservation (ODCR) for an instance type and Availability Zone that match the capacity provider, and Lambda uses it automatically. Create the reservation with open instance eligibility. Lambda launches instances without targeting a reservation, so a targeted reservation is not used. For more information, see [Reserve compute capacity with Amazon EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html).
+ **Choose a Region with more GPU capacity available:** Deploy in a Region that has sufficient capacity for the instance families you need.

## Initialization issues
<a name="lambda-managed-instances-gpu-troubleshooting-init"></a>

### Activation fails with `InitResourceExhausted`
<a name="lambda-managed-instances-gpu-troubleshooting-init-exhausted"></a>

**Problem:** The version fails with `FunctionError.InitResourceExhausted` and a message about high resource consumption during initialization, even though the initialization log of every worker process reports success.

**Cause:** `MemorySize` is shared by all worker processes in the execution environment, and `PerExecutionEnvironmentMaxConcurrency` sets how many worker processes there are. Each worker process runs your initialization code, so the memory used during initialization is roughly the memory one worker needs multiplied by the concurrency. A function that activates at a low concurrency can therefore exceed its `MemorySize` at a higher one, even though each worker's initialization log reports success.

**Solutions:**
+ **Raise MemorySize:** Give the execution environment enough memory for every worker process to initialize at once.

  ```bash
  aws lambda update-function-configuration \
    --function-name my-gpu-function \
    --memory-size 16384
  ```
+ **Lower the concurrency:** Reduce `PerExecutionEnvironmentMaxConcurrency` if you cannot raise `MemorySize`. Fewer worker processes initialize, so the total memory used during initialization drops.

### Initialization exceeds 15 minutes
<a name="lambda-managed-instances-gpu-troubleshooting-init-timeout"></a>

**Problem:** The version fails to become `Active`, or scale-out stalls, and the initialization log shows the function still downloading or loading artifacts, such as model weights, when initialization stops.

**Cause:** Initialization is limited to 15 minutes, and a longer function timeout does not extend it. Downloading large artifacts from the internet, for example a model from a third-party repository such as the Hugging Face Hub, or pulling a very large image, can exceed the 15-minute limit.

**Solutions:**
+ **Load large artifacts from Amazon S3:** Store model weights, rendering assets, and other large artifacts in an S3 bucket in the same Region as the function. With the Lambda vLLM image, stream the weights into memory by setting the `VLLM_LOAD_FORMAT` environment variable to `runai_streamer`. With the Lambda PyTorch image, read them with the Amazon S3 Connector for PyTorch in your initialization code. For more information, see [Optimizing startup time for GPU-accelerated functions](lambda-managed-instances-gpu-startup.md).
+ **Shrink the image and use SOCI:** Keep large artifacts out of the image and use SOCI so that the execution environment starts before the whole image is downloaded. For more information about optimizing startup time, see [Optimizing startup time for GPU-accelerated functions](lambda-managed-instances-gpu-startup.md).
+ **Load artifacts on the first invocation:** If the load cannot finish within the 15-minute initialization limit, load the artifacts in the handler on the first invocation instead. Invocations are bounded by the function timeout, not by the initialization limit, so set the function timeout to cover the load.

### Model loading fails
<a name="lambda-managed-instances-gpu-troubleshooting-init-model"></a>

**Problem:** Initialization fails or stalls while loading the model, with `MODEL_ID` set to a model ID on a third-party repository, such as the Hugging Face Hub, or to an S3 prefix.

**Cause:** The network path to the model source is blocked, or the ephemeral storage is too small. A download from a third-party repository needs outbound internet access from the capacity provider's subnets and enough ephemeral storage to hold the model in `/tmp`. An S3 load needs a route from the capacity provider's VPC to Amazon S3 and an execution role with `s3:GetObject` on the objects and `s3:ListBucket` on the bucket, because the Run:ai Model Streamer and the Amazon S3 Connector for PyTorch read every object under the prefix with the function's credentials.

**Solutions:**
+ **Load the model from Amazon S3:** For production functions, copy the model to an S3 bucket in the function's Region once and set `MODEL_ID` to the S3 prefix. For more information about running inference workloads, see [Run inference workloads on GPU-accelerated functions](lambda-managed-instances-gpu-inference.md).
+ **Check the execution role:** For a model in Amazon S3, grant the role `s3:GetObject` and `s3:ListBucket` on the prefix. A download from a third-party repository does not use the execution role.
+ **Review the VPC configuration:** Give the capacity provider's subnets a route to Amazon S3 or to the internet, depending on the source you load the model from. For more information, see [Networking for Lambda Managed Instances](lambda-managed-instances-networking.md).

## Concurrency issues
<a name="lambda-managed-instances-gpu-troubleshooting-concurrency"></a>

### Out-of-memory errors on the GPU
<a name="lambda-managed-instances-gpu-troubleshooting-concurrency-oom"></a>

**Problem:** Your application framework reports an out-of-memory error, or the function processes fewer concurrent invocations than `PerExecutionEnvironmentMaxConcurrency` allows, and `ExecutionEnvironmentGPUMemoryUsed` is close to the accelerator memory you requested. Lambda does not report GPU out-of-memory errors; your framework does, so the error text depends on the framework. For example, PyTorch raises `torch.OutOfMemoryError: CUDA out of memory`, CuPy raises `cupy.cuda.memory.OutOfMemoryError`, and the underlying CUDA status is `CUDA_ERROR_OUT_OF_MEMORY`. To find them, search the function's logs for `out of memory` and `OutOfMemoryError`.

**Cause:** Each worker process holds its own CUDA context and its own copy of the data it allocates on the GPU, such as a model. GPU memory use therefore grows in proportion to `PerExecutionEnvironmentMaxConcurrency`. A model that fits in the accelerator memory once does not fit when every worker process loads its own copy.

**Solutions:**
+ **Lower the concurrency:** Reduce `PerExecutionEnvironmentMaxConcurrency`, or set it to 1 if two copies of what one invocation allocates do not fit in the accelerator memory.
+ **Raise the accelerator memory:** Increase `AcceleratorMemorySize` so that the function runs on a GPU with more memory.
+ **Share one copy of the model:** Serve the model from one inference server process so that all worker processes use the same copy. The vLLM and SGLang images work this way to avoid loading one copy per worker: the server holds the model and the worker processes forward requests to it. For more information, see [Scaling and concurrency](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-concurrency).

## Performance issues
<a name="lambda-managed-instances-gpu-troubleshooting-performance"></a>

### Throughput does not increase with concurrency for media workloads
<a name="lambda-managed-instances-gpu-troubleshooting-performance-throughput"></a>

**Problem:** Raising `PerExecutionEnvironmentMaxConcurrency` on a transcoding or rendering function increases the duration of each invocation roughly in proportion to the number of files processed at once, so a batch of files finishes no sooner.

**Cause:** The encoder, decoder, and graphics engines process one session at a time from a hardware queue, so concurrent invocations contend for the same engine. Concurrency still helps by overlapping the download, upload, and CPU work of one invocation with the GPU work of another, but it does not multiply the engine's throughput.

**Solutions:**
+ **Set concurrency to optimize batch processing duration:** Measure the total time for a batch of files rather than the duration of one invocation, and choose the concurrency at which the batch time stops improving.
+ **Scale horizontally to more execution environments:** To process more files in parallel, let the capacity provider scale out to more execution environments rather than raising the concurrency further.

### Inconsistent performance across execution environments
<a name="lambda-managed-instances-gpu-troubleshooting-performance-inconsistent"></a>

**Problem:** The same invocation runs noticeably faster in some execution environments than in others.

**Cause:** When the latest generation in `AllowedInstanceTypes` is unavailable, Lambda falls back to older generations, so execution environments of one function version can run on different GPUs, for example an L4 on G6 and a T4 on G4dn. On G6f and Gr6f instances, the encoder, decoder, and graphics engines of the physical GPU are shared with other EC2 instances, so throughput varies with their load as well.

**Solutions:**
+ **Restrict the instance types:** If consistent performance matters more than availability, limit `AllowedInstanceTypes` to one generation and reserve capacity for it with an Amazon EC2 On-Demand Capacity Reservation.
+ **Do not use fractional GPU instance types:** For encoder, decoder, and graphics workloads, leave G6f and Gr6f instance types out of `AllowedInstanceTypes` so that the execution environment runs on a whole GPU.
+ **Monitor by instance type:** Use the `InstanceType` dimension of the capacity provider GPU metrics to see which instance types are in use.

### Slow scale-out
<a name="lambda-managed-instances-gpu-troubleshooting-performance-scaleout"></a>

**Problem:** When traffic surges, new execution environments take several minutes to start serving invocations, and invocations are throttled in the meantime.

**Cause:** A new execution environment on a new instance waits for the instance to launch, for the image to be pulled, and for your initialization code to run. GPU images are large, and initialization often loads large artifacts such as a model. GPU-accelerated functions therefore scale out more slowly than other Event Functions on Lambda Managed Instances.

**Solutions:**
+ **Shorten initialization:** Keep large artifacts out of the image, stream model weights from Amazon S3 in the same Region, and use SOCI. For more information about optimizing startup time, see [Optimizing startup time for GPU-accelerated functions](lambda-managed-instances-gpu-startup.md).
+ **Lower the GPU utilization target:** A lower target makes Lambda scale out earlier. For more information, see [How GPU scaling works](lambda-managed-instances-gpu-scaling.md).
+ **Pre-warm capacity:** For planned traffic increases, raise `MinExecutionEnvironments` for the version with the `PutFunctionScalingConfig` API ahead of time, so that Lambda starts the execution environments before the traffic arrives. For more information, see [Troubleshooting Lambda Managed Instances](lambda-managed-instances-troubleshooting.md).

## Monitoring and observability issues
<a name="lambda-managed-instances-gpu-troubleshooting-monitoring"></a>

### GPU utilization reads zero while the function is busy
<a name="lambda-managed-instances-gpu-troubleshooting-monitoring-gpuzero"></a>

**Problem:** `GPUUtilization` and `ExecutionEnvironmentGPUUtilization` stay near zero while a transcoding or rendering function processes invocations.

**Cause:** These metrics measure the time the GPU's compute cores are busy. The video encoder and decoder and the graphics pipeline are separate engines on the GPU, and their activity does not count toward compute utilization, so these metrics stay low while those engines are fully in use.

**Solution:** This is expected behavior. Use the function's `Duration` metric to understand throughput for encoder, decoder, and graphics workloads.