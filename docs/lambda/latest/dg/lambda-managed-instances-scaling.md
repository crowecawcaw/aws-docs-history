

# Scaling Lambda Managed Instances

With Lambda Managed Instances, your function doesn't scale when invocations arrive. Instead, it scales asynchronously based on resource consumption signals. Managed Instances currently scales based on CPU resource utilization and multi-concurrency saturation.

**Key differences:**
+ **Lambda (default)** – Scales when there is no free execution environment to handle an incoming invocation (cold start)
+ **Lambda Managed Instances** – Scales asynchronously based on CPU resource utilization and multi-concurrency saturation of execution environments

If your traffic more than doubles within 5 minutes, you might see throttles while Lambda scales up instances and execution environments to meet demand.

## The scaling lifecycle
<a name="lambda-managed-instances-scaling-lifecycle"></a>

Lambda Managed Instances uses a distributed architecture to manage scaling.

**Components:**
+ **Managed Instances** – Run in your account in the subnets you provide
+ **Router and Scaler** – Shared Lambda components that route invocations and manage scaling
+ **Lambda Agent** – Runs on each Managed Instance to manage the execution environment lifecycle and monitor resource consumption

**How it works:**

1. When you publish a function version with a capacity provider, Lambda launches Managed Instances in your account. By default, it launches three instances for Availability Zone resiliency. It starts three execution environments before your function version becomes `Active`.

1. Each Managed Instance can run execution environments for multiple functions that use the same capacity provider.

1. As traffic flows into your application, execution environments consume resources. The Lambda Agent notifies the Scaler, which decides whether to scale new execution environments or Managed Instances.

1. The Router might send an invocation to an execution environment with high resource consumption. In that case, the Lambda Agent on that instance tells the Router to retry on another execution environment.

1. As traffic decreases, the Lambda Agent notifies the Scaler. The Scaler then scales down execution environments and scales in Managed Instances.

## Adjusting scaling behavior
<a name="lambda-managed-instances-adjusting-scaling"></a>

You can customize the scaling behavior of Managed Instances through five controls.

### Function level controls
<a name="lambda-managed-instances-function-level-controls"></a>

#### 1. Function memory and vCPUs
<a name="lambda-managed-instances-function-memory-vcpus"></a>

Choose the memory size and vCPU allocation for your function. The smallest supported function size is 2 GB and 1 vCPU.

**Considerations:**
+ Pick a memory and vCPU setting that supports multi-concurrent executions of your function.
+ You can't configure a function with less than 1 vCPU, because functions that run on Managed Instances should support multi-concurrent workloads.
+ You can't choose less than 2 GB. This minimum matches the 2 to 1 memory to vCPU ratio of c instances, which have the lowest ratio.
+ For Python applications, you might need a higher ratio of memory to vCPUs, such as 4 to 1 or 8 to 1. This is because of the way Python handles multi-concurrency.
+ If you run CPU-intensive operations or perform little input/output (I/O), choose more than one vCPU.

#### 2. Maximum concurrency
<a name="lambda-managed-instances-maximum-concurrency"></a>

Set the maximum concurrency for each execution environment.

**Default behavior:** Lambda chooses defaults that balance resource consumption and throughput for a wide variety of applications.

**Adjustment guidelines:**
+ **Increase concurrency** – If your function invocations use very little CPU, you can increase maximum concurrency up to 64 for each vCPU.
+ **Decrease concurrency** – If your application consumes a large amount of memory and very little CPU, you can reduce your maximum concurrency.

**Important:** Lambda Managed Instances targets multi-concurrent applications, so execution environments with very low concurrency might experience throttles when scaling. When an invocation arrives at an execution environment that has reached its concurrency limit, Lambda routes the invocation elsewhere. Lambda also scales out new execution environments to handle the load. To identify which resource constraint causes throttles, monitor the throttle reason metrics: `ConcurrencyThrottles`, `CPUThrottles`, `MemoryThrottles`, and `DiskThrottles`. For more information about these metrics, see [Types of metrics for Lambda Event Functions](monitoring-metrics-types.md).

#### 3. Execution environments for each function
<a name="lambda-managed-instances-execution-environments-per-function"></a>

Set the minimum and maximum number of execution environments for your function.

**Default behavior:** The default minimum is 3 execution environments across Availability Zones, with no default maximum. You can change both values after you create the function.

**Adjustment guidelines:**
+ **Set the minimum** – Provision capacity for baseline traffic and reduce throttles during sudden bursts. Values below 3 reduce Availability Zone redundancy.
+ **Set the maximum** – Cap the number of execution environments to control scale-out. A cap also prevents noisy neighbor issues when multiple functions share a capacity provider.
+ **Scale to zero** – Set the minimum to 0 and the maximum to a value greater than 0. When the function version is idle, Lambda stops all of its execution environments. Lambda starts one again when you invoke the function version. For more information about scaling to zero, see [Scaling to zero](#lambda-managed-instances-scale-to-zero).
+ **Deactivate the function** – Set both the minimum and maximum to 0 to deactivate a function without deleting it. A deactivated function version doesn't scale up when you invoke it.

To set these values, use the `PutFunctionScalingConfig` API operation. For instructions, see [Configuring execution environments with the AWS CLI](#lambda-managed-instances-configure-scaling).

Keep the following in mind when you configure execution environments.

**Qualifier scope**  
The scaling configuration applies to one qualified Amazon Resource Name (ARN) of the function. If you set it on `$LATEST.PUBLISHED`, future `$LATEST.PUBLISHED` versions inherit it. If you set it on a specific version, newly published versions use the default values.

**Paired configuration**  
You must set the minimum and maximum values together. Lambda resets any value that you don't specify to its default. Valid values for both `MinExecutionEnvironments` and `MaxExecutionEnvironments` range from 0 to 15000. A minimum of 0 with a maximum greater than 0 allows the function version to scale to zero. A minimum and maximum of 0 deactivates the function version.

**Cost implication**  
Scaling to zero and deactivation apply to one function version. Lambda terminates an underlying Amazon EC2 instance when it has no active execution environments. Instance charges continue until termination completes, which typically takes a few minutes.

### Capacity provider level controls
<a name="lambda-managed-instances-capacity-provider-level-controls"></a>

#### 4. Target resource utilization
<a name="lambda-managed-instances-target-resource-utilization"></a>

Choose your own target for CPU utilization.

**Default behavior:** Lambda maintains enough headroom for your traffic to double within 5 minutes without throttles.

**Optimization options:**
+ If your workload is very steady or your application isn't sensitive to throttles, you can set a high target. A high target achieves higher utilization and lower costs.
+ If you want to maintain headroom for bursts of traffic, you can set a low target. A low target requires more capacity.

#### 5. Instance type selection
<a name="lambda-managed-instances-instance-type-selection"></a>

Set allowed or excluded instance types.

**Default behavior:** Lambda chooses the best instance types for your workload. We recommend that you let Lambda Managed Instances choose instance types. If you restrict the number of possible instance types, availability might be lower.

**Custom configuration:**
+ **Specific hardware requirements** – Set allowed instance types to a list of compatible instances. For example, if your application requires high network bandwidth, you can select several n instance types.
+ **Cost optimization** – For testing or development environments, you can choose smaller instance types, such as m7a.large.

## Configuring execution environments with the AWS CLI
<a name="lambda-managed-instances-configure-scaling"></a>

Use the `put-function-scaling-config` command to set the minimum and maximum number of execution environments for a function version.

**To configure execution environments for a function version**
+ Run the following command. This example sets a minimum of 5 and a maximum of 20 execution environments for the `$LATEST.PUBLISHED` version.

  ```bash
  aws lambda put-function-scaling-config \
    --function-name {{my-lmi-function}} \
    --qualifier '$LATEST.PUBLISHED' \
    --function-scaling-config MinExecutionEnvironments={{5}},MaxExecutionEnvironments={{20}} \
    --region {{us-east-1}}
  ```

  Replace the following values:
  + `{{my-lmi-function}}` – The name of your function.
  + `{{5}}` – The minimum number of execution environments. To turn on scale to zero, use 0.
  + `{{20}}` – The maximum number of execution environments. To turn on scale to zero, use a value greater than 0. To deactivate the function version, use 0.
  + `{{us-east-1}}` – The AWS Region of your function.

  To configure a numbered version instead, replace `$LATEST.PUBLISHED` with the version number.

## Scheduled scaling
<a name="lambda-managed-instances-scheduled-scaling"></a>

Use [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html) to adjust your function's minimum and maximum execution environments on a recurring or one-time schedule. Scheduled scaling helps with predictable traffic patterns, such as scaling up before peak hours and scaling down during off-peak hours.

Scheduled scaling adjusts the floor and ceiling of execution environments. Between the minimum and maximum, Lambda still scales based on CPU utilization and concurrency saturation. If your traffic more than doubles within 5 minutes of a scheduled scale-up, you might still see throttles while Lambda provisions capacity.

**To set up scheduled scaling**

1. Create an EventBridge Scheduler execution role, or use an existing role. The role must grant permission to call `lambda:PutFunctionScalingConfig` on your function.

1. Create a schedule with a cron or rate expression. Set the `PutFunctionScalingConfig` API operation as a universal target. In the `Input` payload, specify the new `MinExecutionEnvironments` and `MaxExecutionEnvironments` values.

1. To change the values again later, create another schedule with the new values. For example, create one schedule that scales up before peak hours and another that scales down afterward.

The following examples show common schedules. In each example, replace the following values:
+ `{{111122223333}}` – Your AWS account ID.
+ `{{eventbridge-scheduler-role}}` – The name of your EventBridge Scheduler execution role.
+ `{{my-lmi-function}}` – The name of your function.

### Example 1: Scale to handle planned peak traffic
<a name="lambda-managed-instances-scheduled-scaling-peak"></a>

Create two schedules to scale up before peak hours and scale down afterward.

The following command creates a schedule that sets the minimum to 100 and the maximum to 1000 execution environments at 8:00 AM UTC.

```bash
aws scheduler create-schedule \
  --name "ScaleUpLambdaManagedInstances" \
  --schedule-expression "cron(0 8 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 100, \"MaxExecutionEnvironments\": 1000}}"
  }'
```

The following command creates a schedule that sets the minimum to 5 and the maximum to 20 execution environments at 6:00 PM UTC.

```bash
aws scheduler create-schedule \
  --name "ScaleDownLambdaManagedInstances" \
  --schedule-expression "cron(0 18 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 5, \"MaxExecutionEnvironments\": 20}}"
  }'
```

### Example 2: Deactivate during off-peak hours and reactivate
<a name="lambda-managed-instances-scheduled-scaling-deactivate"></a>

If you set both `MinExecutionEnvironments` and `MaxExecutionEnvironments` to 0, Lambda deactivates the function version without deleting it. A deactivated function doesn't scale back up with traffic. To reactivate it, you must call `PutFunctionScalingConfig` with non-zero values, for example from another schedule.

The following command creates a schedule that deactivates the function version at 10:00 PM UTC by setting the minimum and maximum to 0.

```bash
aws scheduler create-schedule \
  --name "DeactivateLambdaManagedInstances" \
  --schedule-expression "cron(0 22 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 0, \"MaxExecutionEnvironments\": 0}}"
  }'
```

The following command creates a schedule that reactivates the function version at 7:00 AM UTC with a minimum of 10 and a maximum of 20.

```bash
aws scheduler create-schedule \
  --name "ReactivateLambdaManagedInstances" \
  --schedule-expression "cron(0 7 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 10, \"MaxExecutionEnvironments\": 20}}"
  }'
```

### Example 3: Scale to zero during off-peak hours
<a name="lambda-managed-instances-scheduled-scaling-zero"></a>

Create two schedules to keep execution environments running during business hours and allow the function version to scale to zero overnight. Unlike a deactivated function, a function version that can scale to zero still serves invocations during off-peak hours. Lambda throttles the first invocations after an idle period while it starts an execution environment.

The following command creates a schedule that allows the function version to scale to zero at 10:00 PM UTC. It sets the minimum to 0 and the maximum to 20.

```bash
aws scheduler create-schedule \
  --name "AllowScaleToZeroLambdaManagedInstances" \
  --schedule-expression "cron(0 22 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 0, \"MaxExecutionEnvironments\": 20}}"
  }'
```

The following command creates a schedule that raises the minimum to 10 at 7:00 AM UTC, with a maximum of 20.

```bash
aws scheduler create-schedule \
  --name "RaiseMinimumLambdaManagedInstances" \
  --schedule-expression "cron(0 7 * * ? *)" \
  --flexible-time-window '{"Mode": "OFF"}' \
  --target '{
    "Arn": "arn:aws:scheduler:::aws-sdk:lambda:putFunctionScalingConfig",
    "RoleArn": "arn:aws:iam::{{111122223333}}:role/{{eventbridge-scheduler-role}}",
    "Input": "{\"FunctionName\": \"{{my-lmi-function}}\", \"Qualifier\": \"$LATEST.PUBLISHED\", \"FunctionScalingConfig\": {\"MinExecutionEnvironments\": 10, \"MaxExecutionEnvironments\": 20}}"
  }'
```

## Scaling to zero
<a name="lambda-managed-instances-scale-to-zero"></a>

When your function version has no traffic, it can scale to zero execution environments to reduce instance costs during idle periods. When you invoke a function version that has scaled to zero, Lambda starts an execution environment for it. The function version stays in the `Active` state while it has zero execution environments.

### Turning on scale to zero
<a name="lambda-managed-instances-scale-to-zero-configure"></a>

To turn on scale to zero, set `MinExecutionEnvironments` to 0 and `MaxExecutionEnvironments` to a value greater than 0. To turn it off, set `MinExecutionEnvironments` to a value greater than 0. For instructions, see [Configuring execution environments with the AWS CLI](#lambda-managed-instances-configure-scaling).

### How a function version scales to zero
<a name="lambda-managed-instances-scale-to-zero-how"></a>

A function version with a minimum of 0 goes through the following stages.

1. When the function version becomes active, Lambda starts one execution environment.

1. As traffic decreases, Lambda scales in execution environments as usual, down to one.

1. After the function version goes without invocations for a period of time, Lambda stops its last execution environment.

1. Lambda terminates a Managed Instance when the instance runs no execution environments for any function in the capacity provider. Instance charges continue until termination completes, usually within minutes. Instances that run execution environments for other functions keep running.

A function version doesn't scale to zero in the following cases:
+ **The last execution environment is still using CPU** – Lambda scales in execution environments only when resource utilization is low. Your function might run background work between invocations, such as background threads or polling loops. In that case, the last execution environment might never scale in.
+ **A deployment is in progress** – During a [rolling update or a weighted alias traffic shift](lambda-managed-instances-deployments.md#lambda-managed-instances-deployments-strategies), Lambda keeps at least one execution environment running for each version. This lets traffic shift back without delay. The function version can scale to zero after the deployment completes.

### Scaling up from zero
<a name="lambda-managed-instances-scale-from-zero"></a>

When you invoke a function version that has scaled to zero, Lambda throttles the invocation with an HTTP 429 error. Lambda then starts an execution environment. If no Managed Instance has room for the execution environment, Lambda launches a new instance. Lambda throttles invocations to the function version until the first execution environment is ready. This typically takes a few minutes. Functions with long initialization times can take longer. After the first execution environment is ready, the function version scales as usual.

**Recommendations:**
+ **Retry throttled synchronous invocations** – Use exponential backoff with enough retries to cover the time it takes to start an execution environment. AWS SDKs retry throttling errors by default. However, the default retry settings might stop retrying before the execution environment is ready.
+ **Use scale to zero for workloads that can tolerate delay after idle periods** – Examples include development and test environments, batch jobs, and internal tools. For latency-sensitive workloads, keep a minimum of at least 1 execution environment. For Availability Zone redundancy, keep a minimum of 3.
+ **Scale up ahead of predictable traffic** – If you know when traffic will arrive, use [scheduled scaling](#lambda-managed-instances-scheduled-scaling) to raise the minimum before that time. Set the minimum back to 0 afterward.

### Scale to zero compared with deactivation
<a name="lambda-managed-instances-scale-to-zero-vs-deactivation"></a>

Unlike deactivated function versions, function versions that scale to zero still count toward the function version quota for each capacity provider. If you reach this quota, we recommend that you deactivate or delete older function versions that you no longer use. For more information about this quota, see [Lambda Managed Instances quotas](lambda-managed-instances-quotas.md).

The following table compares scale to zero with deactivation.


| Option | Configuration | When execution environments stop | When you invoke the function version | To serve traffic again | 
| --- | --- | --- | --- | --- | 
| Scale to zero | MinExecutionEnvironments = 0, MaxExecutionEnvironments greater than 0 | After a period without invocations | Lambda throttles the invocation and starts an execution environment | No action needed | 
| Deactivation | MinExecutionEnvironments = 0, MaxExecutionEnvironments = 0 | When you apply the configuration | Lambda doesn't start an execution environment | Call PutFunctionScalingConfig with a maximum greater than 0 | 

## Next steps
<a name="lambda-managed-instances-scaling-next-steps"></a>
+ Learn about [capacity providers for Lambda Managed Instances](lambda-managed-instances-capacity-providers.md)
+ Review runtime-specific guides for handling multi-concurrency
+ Configure [VPC connectivity for your capacity providers](lambda-managed-instances-networking.md)
+ Monitor scaling metrics to optimize scaling behavior