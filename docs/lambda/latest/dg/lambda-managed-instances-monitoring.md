# Monitoring Lambda Managed Instances

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
- **NetworkOut** - Network traffic sent through the customer ENI (in bytes)
- **NetworkIn** - Network traffic received through the customer ENI (in bytes)
- **DiskReadBytes** - Read traffic from local storage across instances (in bytes)
- **DiskWriteBytes** - Write traffic to local storage across instances (in bytes)

**Capacity metrics:**

- **vCPUAvailable** - The amount of vCPU available on instances for allocation (in count)
- **MemoryAvailable** - The amount of memory available on instances for allocation (in bytes)
- **vCPUAllocated** - The amount of vCPU allocated on instances for execution environments (in count)
- **MemoryAllocated** - The amount of memory allocated on instances for execution environments (in bytes)

### Execution environment level metrics

Execution environment level metrics provide visibility into resource utilization and concurrency for individual functions. These metrics use the following dimensions:

- **CapacityProviderName** - The name of your capacity provider
- **FunctionName** - The name of your Lambda function

**Available execution environment metrics:**

- **ExecutionEnvironmentConcurrency** - The maximum concurrency over a 5-minute sample period
- **ExecutionEnvironmentConcurrencyLimit** - The maximum concurrency limit per execution environment
- **ExecutionEnvironmentCPUUtilization** - The percentage of CPU utilization for the function's execution environments
- **ExecutionEnvironmentMemoryUtilization** - The percentage of memory utilization for the function's execution environments

## Metric frequency and retention

Lambda Managed Instances metrics are published at 5-minute intervals and retained for 15 months.

## Viewing metrics in CloudWatch

**To view Lambda Managed Instances metrics in the CloudWatch console**

1. Open the CloudWatch console at [console.aws.amazon.com/cloudwatch/](http://console.aws.amazon.com/cloudwatch/ "http://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **All metrics** tab, choose **AWS/Lambda**.
4. Choose the metric dimension you want to view:
   - For capacity provider level metrics, filter by **CapacityProviderName** and **InstanceType**
   - For execution environment level metrics, filter by **CapacityProviderName** and **FunctionName**

5. Select the metrics you want to monitor.

## Using metrics to optimize performance

Monitor CPU and memory utilization to understand if your functions are properly sized. High utilization may indicate the need for larger instance types or increased function memory allocation. Track concurrency metrics to understand scaling behavior and identify potential throttling.

Monitor capacity metrics to verify sufficient resources are available for your workloads. The **vCPUAvailable** and **MemoryAvailable** metrics help you understand remaining capacity on your instances.

## Next steps

- Learn about [scaling Lambda Managed Instances](lambda-managed-instances-scaling.md "lambda-managed-instances-scaling.md")
- Review runtime-specific guides for [Java](lambda-managed-instances-java-runtime.md "lambda-managed-instances-java-runtime.md"), [Node.js](lambda-managed-instances-nodejs-runtime.md "lambda-managed-instances-nodejs-runtime.md"), and [Python](lambda-managed-instances-python-runtime.md "lambda-managed-instances-python-runtime.md")
- Configure [VPC connectivity for your capacity providers](lambda-managed-instances-networking.md "lambda-managed-instances-networking.md")
- Understand [security and permissions for Lambda Managed Instances](lambda-managed-instances-security.md "lambda-managed-instances-security.md")
