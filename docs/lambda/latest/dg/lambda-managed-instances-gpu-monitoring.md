

# Monitoring GPU-accelerated Event Functions

This page explains how to monitor the GPU metrics of your GPU-accelerated Event Functions and use them to optimize performance. Lambda publishes GPU metrics for your GPU-accelerated Event Functions to Amazon CloudWatch in the `AWS/Lambda` namespace, alongside the [standard Lambda Managed Instances metrics](lambda-managed-instances-monitoring-metrics.md), to help you monitor GPU utilization, size accelerator memory, and track available GPU capacity.

## Available GPU metrics
<a name="lambda-managed-instances-gpu-available-metrics"></a>

Lambda provides GPU metrics at the capacity provider level and the execution environment level. Lambda collects GPU metrics from NVIDIA Data Center GPU Manager (DCGM). For more information, see the [NVIDIA Data Center GPU Manager documentation](https://docs.nvidia.com/datacenter/dcgm/latest/) on the NVIDIA website.

### Capacity provider level GPU metrics
<a name="lambda-managed-instances-gpu-capacity-provider-metrics"></a>

Capacity provider level GPU metrics provide visibility into utilization and GPU capacity across all instances in the capacity provider. These metrics use the following dimensions:
+ **CapacityProviderName** – The name of your capacity provider
+ **InstanceType** – The EC2 instance type

The capacity provider level includes the following GPU utilization metrics:
+ **GPUUtilization** – The percentage of time during the sampling period when one or more kernels were executing on the GPU, aggregated across all instances in the capacity provider. This metric measures how long the GPU was busy, not how much of the GPU was in use. A workload that runs on a small fraction of the GPU cores for the whole sampling period reports 100 percent.
+ **GPUMemoryUtilization** – The percentage of time during the sampling period when GPU device memory was being read or written, aggregated across all instances in the capacity provider. It does not measure how much memory is allocated or occupied.
+ **GPUMemoryUsed** – The amount of GPU device memory in use across all instances in the capacity provider (in bytes).
+ **GPUPowerUtilization** – The GPU power draw as a percentage of the GPU power limit across all instances in the capacity provider

Lambda also emits the following metrics for GPU capacity at the capacity provider level:
+ **GPUAvailable** – The number of GPUs on instances in the capacity provider that are not assigned to an execution environment (in count)
+ **GPUAllocated** – The number of GPUs on instances in the capacity provider that are assigned to an execution environment (in count)

### Execution environment level GPU metrics
<a name="lambda-managed-instances-gpu-execution-environment-metrics"></a>

Execution environment level GPU metrics provide visibility into GPU utilization for each execution environment of a function. They use the following dimensions:
+ **CapacityProviderName** – The name of your capacity provider
+ **FunctionName** – The name of your Lambda event function
+ **Resource** – For Lambda Managed Instances, the `Resource` dimension supports function versions only. The format is `FunctionName:Version`

Lambda reports the following metrics at the execution environment level:
+ **ExecutionEnvironmentGPUUtilization** – The percentage of time during the sampling period when one or more kernels were executing on the GPU, aggregated across the function's execution environments. This metric measures how long the GPU was busy, not how much of the GPU was in use. A workload that runs on a small fraction of the GPU cores for the whole sampling period reports 100 percent.
+ **ExecutionEnvironmentGPUMemoryUtilization** – The percentage of time during the sampling period when GPU device memory was being read or written, aggregated across the function's execution environments. It does not measure how much memory is allocated or occupied.
+ **ExecutionEnvironmentGPUMemoryUsed** – The amount of GPU device memory in use by the function's execution environments (in bytes).
+ **ExecutionEnvironmentGPUPowerUtilization** – The GPU power draw as a percentage of the GPU power limit for the function's execution environments

GPU metrics are published at 1-minute intervals and retained for 15 months, the same as other Lambda Managed Instances metrics. To view them in the CloudWatch console, filter the `AWS/Lambda` namespace by `CapacityProviderName` and `InstanceType` for capacity provider level metrics, or by `CapacityProviderName`, `FunctionName`, and `Resource` for execution environment level metrics. For more information, see [CloudWatch metrics for Lambda Managed Instances](lambda-managed-instances-monitoring-metrics.md).

## GPU metrics in the Lambda console
<a name="lambda-managed-instances-gpu-console"></a>

The Lambda console shows the GPU metrics as graphs. On the function's Monitor tab, the console shows GPU utilization, GPU memory utilization, GPU memory used, and GPU power utilization for the function's execution environments. On the capacity provider's Monitoring tab, the console shows the same four metrics across the capacity provider's instances. To view the GPU capacity metrics, use the [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/) console or API.

## Using GPU metrics to optimize performance
<a name="lambda-managed-instances-gpu-using-metrics"></a>

Start with the default configuration. Leave `PerExecutionEnvironmentMaxConcurrency` at its default of 4, set `AcceleratorMemorySize` to the smallest value that fits one copy of your model or working set, publish the version, and send it representative traffic. Then monitor `ExecutionEnvironmentGPUMemoryUsed` and the function's `Errors` metric.

Adjust the configuration based on what you observe:
+ **Memory used is consistently below the available accelerator memory and `ExecutionEnvironmentGPUUtilization` is low under load** – This indicates that your workload uses only part of the GPU it has been allocated. Increase `PerExecutionEnvironmentMaxConcurrency` so that more invocations share the GPU. Each increment adds one worker process with its own CUDA context and its own copy of whatever that worker allocates on the GPU.
+ **GPU memory use approaches the accelerator memory, invocations fail with out-of-memory errors, or CUDA processes crash** – Decrease `PerExecutionEnvironmentMaxConcurrency`, or increase `AcceleratorMemorySize` so that the function runs on a GPU with more memory. If a single copy of your model occupies most of the accelerator memory, set `PerExecutionEnvironmentMaxConcurrency` to 1, or serve the model from one server process. For more details, see [Run one model server for all worker processes](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-model-server).

Monitor GPU utilization to understand scaling behavior. The `GPUUtilization` metric at the capacity provider level is one of the metrics that scaling acts on. Compare it with your target utilization to understand when the capacity provider scales.

Monitor GPU capacity metrics to determine if provisioned capacity is sufficient. `GPUAllocated` shows how many GPUs in the capacity provider are serving execution environments, and `GPUAvailable` shows how many are idle and can take a new execution environment without launching an instance. When `GPUAvailable` stays at zero under load, new execution environments wait for instance launches.