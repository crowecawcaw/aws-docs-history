# CloudWatch metrics for Lambda Managed Instances

You can monitor Lambda Managed Instances using CloudWatch metrics. Lambda automatically publishes metrics to CloudWatch to help you monitor resource utilization, track costs, and optimize performance.

## Available metrics

Lambda Managed Instances provides metrics at two levels: capacity provider level and execution environment level.

### Capacity provider level metrics

Capacity provider level metrics provide visibility into overall resource utilization across your instances. These metrics use the following dimensions:

- **CapacityProviderName** - The name of your capacity provider
- **InstanceType** - The EC2 instance type

**Resource utilization metrics:**

- **CPUUtilization** - The percentage of CPU utilization across instances in the capacity provider
- **MemoryUtilization** - The percentage of memory utilization across instances in the capacity provider

**Capacity metrics:**

- **vCPUAvailable** - The amount of vCPU available on instances for allocation (in count)
- **MemoryAvailable** - The amount of memory available on instances for allocation (in bytes)
- **vCPUAllocated** - The amount of vCPU allocated on instances for execution environments (in count)
- **MemoryAllocated** - The amount of memory allocated on instances for execution environments (in bytes)

### Execution environment level metrics

Execution environment level metrics provide visibility into resource utilization and concurrency for individual functions. These metrics use the following dimensions:

- **CapacityProviderName** - The name of your capacity provider
- **FunctionName** - The name of your Lambda function
- **Resource** - By resource, view metrics for a specific version of a function.

###### Note

For Lambda Managed Instances (LMI), the `Resource` dimension supports function versions only. The format is `<FunctionName>:<FunctionVersion>`.

**Available execution environment metrics:**

- **ExecutionEnvironmentConcurrency** - The maximum concurrency over a 5-minute sample period
- **ExecutionEnvironmentConcurrencyLimit** - The maximum concurrency limit per execution environment
- **ExecutionEnvironmentCPUUtilization** - The percentage of CPU utilization for the function's execution environments
- **ExecutionEnvironmentMemoryUtilization** - The percentage of memory utilization for the function's execution environments

## Throttle reason metrics

Lambda Managed Instances emits granular throttle reason metrics that identify the resource constraint that caused a throttle. For each throttle, Lambda emits exactly one of the following sub-metrics with a value of 1, while the remaining three are emitted with a value of 0:

- **ConcurrencyThrottles** – The execution environment reached its maximum concurrency limit. This can be addressed by either raising [ExecutionEnvironmentMaxConcurrency](lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency "lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency") or by [scaling execution environments more aggressively](lambda-managed-instances-scaling.md#lambda-managed-instances-target-resource-utilization "lambda-managed-instances-scaling.md#lambda-managed-instances-target-resource-utilization").
- **CPUThrottles** – The execution environment exhausted its allocated CPU resources. This can be addressed by increasing your function's [vCPU allocation](lambda-managed-instances-scaling.md#lambda-managed-instances-function-memory-vcpus "lambda-managed-instances-scaling.md#lambda-managed-instances-function-memory-vcpus") or by reducing [ExecutionEnvironmentMaxConcurrency](lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency "lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency") to lower per-environment load.
- **MemoryThrottles** – The execution environment exhausted its allocated memory. This can be addressed by increasing your function's [memory allocation](configuration-memory.md "configuration-memory.md") or by reducing [ExecutionEnvironmentMaxConcurrency](lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency "lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency") to lower per-environment load.
- **DiskThrottles** – The execution environment exhausted its allocated disk space. This can be addressed by increasing your function's [ephemeral storage](configuration-ephemeral-storage.md "configuration-ephemeral-storage.md") or by reducing [ExecutionEnvironmentMaxConcurrency](lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency "lambda-managed-instances-scaling.md#lambda-managed-instances-maximum-concurrency") to lower per-environment load.

Lambda always emits the standard `Throttles` metric alongside these sub-metrics. Use these metrics to understand why your function is scaling and whether to adjust your maximum concurrency, function memory, vCPU allocation, or disk configuration. For the full list of Lambda metrics, see [Types of metrics for Lambda functions](monitoring-metrics-types.md "monitoring-metrics-types.md").

## Metric frequency and retention

Lambda Managed Instances metrics are published at 5-minute intervals and retained for 15 months.

## Viewing metrics in CloudWatch

**To view Lambda Managed Instances metrics in the CloudWatch console**

1. Open the CloudWatch console at [console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **All metrics** tab, choose **AWS/Lambda**.
4. Choose the metric dimension you want to view:

   - For capacity provider level metrics, filter by **CapacityProviderName** and **InstanceType**
   - For execution environment level metrics, filter by **CapacityProviderName**, **FunctionName**, and **Resource**

5. Select the metrics you want to monitor.

## Using metrics to optimize performance

Monitor CPU and memory utilization to understand if your functions are properly sized. High utilization may indicate the need for larger instance types or increased function memory allocation. Track concurrency metrics to understand scaling behavior and identify potential throttling.

Monitor capacity metrics to verify sufficient resources are available for your workloads. The **vCPUAvailable** and **MemoryAvailable** metrics help you understand remaining capacity on your instances.

## Next steps

- Learn about [scaling Lambda Managed Instances](lambda-managed-instances-scaling.md "lambda-managed-instances-scaling.md")
- Review runtime-specific guides for [Java](lambda-managed-instances-java-runtime.md "lambda-managed-instances-java-runtime.md"), [Node.js](lambda-managed-instances-nodejs-runtime.md "lambda-managed-instances-nodejs-runtime.md"), and [Python](lambda-managed-instances-python-runtime.md "lambda-managed-instances-python-runtime.md")
- Configure [VPC connectivity for your capacity providers](lambda-managed-instances-networking.md "lambda-managed-instances-networking.md")
- Understand [security and permissions for Lambda Managed Instances](lambda-managed-instances-security.md "lambda-managed-instances-security.md")
