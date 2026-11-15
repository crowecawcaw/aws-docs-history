

# Troubleshooting Lambda Managed Instances
<a name="lambda-managed-instances-troubleshooting"></a>

## Throttling and scaling issues
<a name="lambda-managed-instances-ts-throttling"></a>

### Occasional throttling
<a name="lambda-managed-instances-ts-occasional-throttling"></a>

**Problem:** You experience throttling errors (HTTP 429) during normal operations.

**Cause:** Lambda Managed Instances might reject new invokes to protect invokes that are already in flight. If your execution environments have consistently high utilization, new invocations might be throttled.

**Solution:**
+ **Monitor scaling metrics:** Examine the Throttle Reasons graph to understand the reason for throttles and capacity scaling issues. In the following example, high CPU is causing throttles.
+ **Review function configuration:** Ensure your function memory and vCPU settings support multi-concurrent executions. Increase function memory or vCPU allocation if needed. If `ExecutionEnvironmentVCPUUtilization` is high, try adding more vCPU per function.

  ```
  aws lambda update-function \
    --function-name my-function \
    ...
    --memory-size 8192
  ```

  If `ExecutionEnvironmentMemoryUtilization` is high, try adding more memory per vCPU:

  ```
  aws lambda update-function \
    --function-name my-function \
    --capacity-provider-config '{
      "LambdaManagedInstancesCapacityProviderConfig": {
        "ExecutionEnvironmentMemoryGiBPerVCpu": 4.0
      }
    }'
  ```

### Throttles during scale-up
<a name="lambda-managed-instances-ts-throttles-during-scale-up"></a>

**Problem:** You experience throttling errors (HTTP 429) when traffic increases rapidly.

**Cause:** Lambda Managed Instances scale asynchronously based on CPU resource utilization and multi-concurrency saturation. If your traffic more than doubles within 5 minutes, you might see throttles as Lambda scales up instances and execution environments to meet demand.

**Solutions:**
+ **Adjust target resource utilization:** If your workload has predictable traffic patterns, set a lower target resource utilization to maintain additional headroom for traffic bursts.

  ```
  aws lambda create-capacity-provider \
    --name my-capacity-provider \
    ...
    --capacity-provider-scaling-config '{
      "ScalingMode": "Manual",
      "ScalingPolicies": [
        {
          "PredefinedMetricType": "LambdaCapacityProviderAverageCPUUtilization",
          "TargetValue": 30.0
        }
      ]
    }'
  ```
+ **Pre-warm capacity:** For planned traffic increases, use the `PutFunctionScalingConfig` API to pre-warm additional capacity.

  ```
  aws lambda put-function-scaling-config \
    --function-name my-function \
    --qualifier 1 \
    --function-scaling-config '{
      "MinExecutionEnvironments": 100
    }'
  ```
+ **Check the `Autoscaling` system logs:** If throttles continue after the scale-up period, check whether Lambda started to scale out, or whether a limit stopped it. For more information, see [Function doesn't scale beyond a limit](#lambda-managed-instances-ts-scaling-limits).

### Slow scale-down
<a name="lambda-managed-instances-ts-slow-scale-down"></a>

**Problem:** Instances take a long time to scale down after traffic decreases.

**Cause:** Lambda Managed Instances scale down gradually to maintain availability and avoid rapid capacity changes that could impact performance.

**Solution:**

This is expected behavior. Lambda scales down instances conservatively to ensure stability. Monitor your CloudWatch metrics to track the number of running instances.

To see when scale-down started and how long it took, check the capacity provider system logs:
+ `Scale-in triggered` events show when Lambda started to scale in.
+ `Terminating` and `Terminated` events show when each instance started and finished terminating.

For how to query these events, see [Autoscaling logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-autoscaling) and [InstanceLifecycle logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-instance-lifecycle).

### Function doesn't scale beyond a limit
<a name="lambda-managed-instances-ts-scaling-limits"></a>

**Problem:** The number of execution environments for a function version stops growing under load, or doesn't shrink when traffic drops, or never reaches the configured minimum.

**Cause:** A configured limit is preventing Lambda from scaling. The limit can be on the function version (minimum or maximum execution environments) or on the capacity provider (maximum vCPUs or allowed instance types).

**Solution:**

Check the `Autoscaling` warnings in the capacity provider system logs. Each warning names the limit that blocked scaling. For how to find these events, see [Autoscaling logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-autoscaling). Then follow the guidance for the warning that you see:
+ `Scale-out blocked: function's maximum execution environments reached.` Increase the function version's maximum execution environments. In the following example, replace {{my-function}} and the qualifier with your function name and version, and set the minimum and maximum that you need:

  ```
  aws lambda put-function-scaling-config \
    --function-name my-function \
    --qualifier 1 \
    --function-scaling-config '{
      "MinExecutionEnvironments": 3,
      "MaxExecutionEnvironments": 50
    }'
  ```
+ `Scale-in blocked: function's minimum execution environments reached.` This is expected when traffic is low. To run fewer execution environments, lower the minimum.
+ `Scale-out blocked: capacity provider's maximum vCPU reached.` Increase `MaxVCpuCount` on the capacity provider, or move some functions to another capacity provider. In the following example, replace {{my-capacity-provider}} with the name of your capacity provider and {{800}} with the maximum number of vCPUs that you need:

  ```
  aws lambda update-capacity-provider \
    --capacity-provider-name my-capacity-provider \
    --capacity-provider-scaling-config ScalingMode=Auto,MaxVCpuCount=800
  ```
+ `No configured instance type can satisfy function resource requirements.` Add a larger instance type to the capacity provider's allowed instance types, remove the instance type restriction, or reduce the function's memory or vCPU configuration.

For more information about scaling controls, see [Scaling Lambda Managed Instances](lambda-managed-instances-scaling.md).

## Concurrency issues
<a name="lambda-managed-instances-ts-concurrency"></a>

### Execution environments with low concurrency experience throttles
<a name="lambda-managed-instances-ts-low-concurrency-throttles"></a>

**Problem:** Your functions experience throttling despite having available capacity.

**Cause:** Execution environments with very low maximum concurrency might have difficulty scaling effectively. Lambda Managed Instances are designed for multi-concurrent applications.

**Solutions:**
+ **Increase maximum concurrency:** If your function invocations use very little CPU, increase the maximum concurrency setting up to 64 per vCPU.

  ```
  aws lambda update-function \
    --function-name ordering-api-backend \
    --capacity-provider-config '{
      "LambdaManagedInstancesCapacityProviderConfig": {
        "PerExecutionEnvironmentMaxConcurrency": 32
      }
    }'
  ```
+ **Optimize function code:** Review your function code to reduce CPU consumption per invocation, allowing higher concurrency.
+ **Adjust function memory and vCPU:** Ensure your function has sufficient resources to handle multiple concurrent invocations.

### Thread safety issues (Java runtime)
<a name="lambda-managed-instances-ts-thread-safety-java"></a>

**Problem:** Your Java function produces incorrect results or experiences race conditions under load.

**Cause:** Multiple threads execute the handler method simultaneously, and shared state is not thread-safe.

**Solution:**
+ Use `AtomicInteger` or `AtomicLong` for counters instead of primitive types
+ Replace `HashMap` with `ConcurrentHashMap`
+ Use `Collections.synchronizedList()` to wrap `ArrayList`
+ Use `ThreadLocal` for request-specific state
+ Access trace IDs from the Lambda Context object, not environment variables

For detailed guidance, see the [Java runtime for Lambda Managed Instances](lambda-managed-instances-java-runtime.md) documentation.

### State isolation issues (Node.js runtime)
<a name="lambda-managed-instances-ts-state-isolation-nodejs"></a>

**Problem:** Your Node.js function returns data from different requests or experiences data corruption.

**Cause:** Global variables are shared across concurrent invocations on the same worker thread. When async operations yield control, other invocations can modify shared state.

**Solution:**
+ Install and use `@aws/lambda-invoke-store` for all request-specific state
+ Replace global variables with `InvokeStore.set()` and `InvokeStore.get()`
+ Use unique file names in `/tmp` with request IDs
+ Access trace IDs using `InvokeStore.getXRayTraceId()` instead of environment variables

For detailed guidance, see the [Node.js runtime for Lambda Managed Instances](lambda-managed-instances-nodejs-runtime.md) documentation.

### File conflicts (Python runtime)
<a name="lambda-managed-instances-ts-file-conflicts-python"></a>

**Problem:** Your Python function reads incorrect data from files in `/tmp`.

**Cause:** Multiple processes share the `/tmp` directory. Concurrent writes to the same file can cause data corruption.

**Solution:**
+ Use unique file names with request IDs: `/tmp/request_{context.request_id}.txt`
+ Use file locking with `fcntl.flock()` for shared files
+ Clean up temporary files with `os.remove()` after use

For detailed guidance, see the [Python runtime for Lambda Managed Instances](lambda-managed-instances-python-runtime.md) documentation.

## Performance issues
<a name="lambda-managed-instances-ts-performance"></a>

### High memory utilization
<a name="lambda-managed-instances-ts-high-memory"></a>

**Problem:** Your functions experience high memory utilization or out-of-memory errors.

**Cause:** Each concurrent request in Python runs in a separate process with its own memory space. Total memory usage equals per-process memory multiplied by concurrent processes.

**Solution:**
+ Monitor the `MemoryUtilization` metric in CloudWatch
+ Reduce the `MaxConcurrency` setting if memory usage approaches the function's memory limit
+ Increase function memory allocation to support higher concurrency
+ Optimize memory usage by loading data on-demand instead of during initialization

### Inconsistent performance
<a name="lambda-managed-instances-ts-inconsistent-performance"></a>

**Problem:** Function performance varies significantly between invocations.

**Cause:** Lambda might select different instance types based on availability, or functions might be running on instances with varying resource availability.

**Solution:**
+ **Specify allowed instance types:** If you have specific performance requirements, configure allowed instance types in your capacity provider to limit the instance types Lambda can select.
+ **Monitor instance-level metrics:** Track `CPUUtilization` and `MemoryUtilization` at the capacity provider level to identify resource constraints.
+ **Review capacity metrics:** Check `vCPUAvailable` and `MemoryAvailable` to ensure sufficient resources are available on your instances.

## Capacity provider issues
<a name="lambda-managed-instances-ts-capacity-provider"></a>

### Function version fails to become ACTIVE
<a name="lambda-managed-instances-ts-function-not-active"></a>

**Problem:** Your function version remains in a pending state after publishing, or its state becomes Failed.

**Cause:** Lambda is launching Managed Instances and starting execution environments. This process takes time, especially for the first function version on a new capacity provider. If Lambda can't create the execution environments, activation fails.

**Solution:**

Wait for Lambda to complete the initialization process. Lambda launches three instances by default for AZ resiliency and starts three execution environments before marking your function version ACTIVE. This typically takes several minutes.

If the function version stays pending or fails, check the `FunctionLifecycle` events in the capacity provider system logs. The `Function version activation failed.` event includes the reason in `stateReasonCode`. For how to find these events, see [FunctionLifecycle logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-function-lifecycle). Then use the reason code to find the cause:
+ If the reason code starts with `FunctionError.`, the execution environments failed to initialize. See [Execution environments fail to initialize](#lambda-managed-instances-ts-ee-failures).
+ If the reason code points to a capacity provider setting, such as an AWS KMS key, subnet, or security group, the event also includes that setting. Fix the setting, and then update the capacity provider. For details, see [Capacity provider settings in failure events](lambda-managed-instances-monitoring-system-log-events.md#lambda-managed-instances-system-log-events-cp-config-fields).
+ If the reason code points to capacity, check whether Lambda could launch instances. See [Instances fail to launch or are replaced](#lambda-managed-instances-ts-instance-launch-failures) and [Function doesn't scale beyond a limit](#lambda-managed-instances-ts-scaling-limits).

### Function scaling configuration update fails
<a name="lambda-managed-instances-ts-scaling-config-update-fails"></a>

**Problem:** An update to a function version's scaling configuration, such as a new minimum number of execution environments, fails.

**Cause:** Lambda couldn't reach the new configuration. For example, the capacity provider doesn't allow enough vCPUs for the new minimum.

**Solution:**

Check the `FunctionLifecycle` events in the capacity provider system logs. The `Function scaling configuration update failed.` event includes the reason in `lastUpdateStatusReasonCode`. For how to find these events, see [FunctionLifecycle logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-function-lifecycle). Use the reason code the same way as for activation failures. See [Function version fails to become ACTIVE](#lambda-managed-instances-ts-function-not-active).

If the reason code is `CapacityProviderScalingLimitExceeded`, the new minimum needs more vCPUs than the capacity provider's `MaxVCpuCount` allows. Increase `MaxVCpuCount`, or lower the minimum. For more information, see [Function doesn't scale beyond a limit](#lambda-managed-instances-ts-scaling-limits).

### Execution environments fail to initialize
<a name="lambda-managed-instances-ts-ee-failures"></a>

**Problem:** Execution environments fail or are replaced repeatedly, and the function version doesn't reach its minimum number of execution environments.

**Cause:** The function code, a Lambda extension, the container image, or the execution role prevents the execution environment from initializing, or initialization takes longer than the function's initialization timeout.

**Solution:**

1. Check the `ExecutionEnvironmentLifecycle` errors in the capacity provider system logs. `Execution environment failed.` events include the reason in `reasonCode`. For how to find these events, see [ExecutionEnvironmentLifecycle logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-ee-lifecycle). For what each reason code means, see [Execution environment failure reason codes](lambda-managed-instances-monitoring-system-log-events.md#lambda-managed-instances-system-log-events-reason-codes).

1. Open the function's own log stream for a failed execution environment. The log stream name is in the event's `cloudWatchLogStreamName` field. The function logs usually contain the error or stack trace from initialization.

1. Fix the cause, and then publish a new function version.

### Instances fail to launch or are replaced
<a name="lambda-managed-instances-ts-instance-launch-failures"></a>

**Problem:** Lambda can't launch enough Amazon EC2 instances for your capacity provider, or Lambda terminates and replaces instances unexpectedly.

**Cause:** Amazon EC2 rejected the launch request, for example because of an account quota, a lack of capacity in an Availability Zone, a subnet without free IP addresses, or a network configuration error. Instances that fail health checks are replaced.

**Solution:**

Check the `InstanceLifecycle` errors in the capacity provider system logs. Each `Failed to launch` event includes the Amazon EC2 error message and the Amazon EC2 error code in `errorCode`. For how to find these events and follow one launch attempt, see [InstanceLifecycle logs](lambda-managed-instances-monitoring-system-logs-usage.md#lambda-managed-instances-system-logs-usage-instance-lifecycle). Then fix the cause, based on `errorCode`. For example:
+ `InsufficientInstanceCapacity`: Amazon EC2 doesn't have enough capacity for the instance type in that Availability Zone. Lambda retries in other Availability Zones and with other instance types. To give Lambda more options, use subnets in more Availability Zones. Avoid restricting the allowed instance types.
+ `VcpuLimitExceeded`: Your account has reached its Amazon EC2 vCPU quota for the instance family. Request a quota increase. For more information, see [Lambda Managed Instances quotas](lambda-managed-instances-quotas.md).
+ `InsufficientFreeAddressesInSubnet`: The subnet has no free IP addresses. Add subnets with more free addresses to the capacity provider.
+ `InvalidSubnetID.NotFound` or `InvalidGroup.NotFound`: A subnet or security group in the capacity provider configuration doesn't exist. Update the capacity provider with valid IDs.
+ `RequestLimitExceeded`: Amazon EC2 throttled the request. Lambda retries automatically. If the error persists, check for other workloads that call the Amazon EC2 API at a high rate in the same account and Region.

If you see `Health check failed for {{instance-id}}: Instance will be replaced.`, Lambda replaces the instance automatically. If this happens repeatedly, contact Support.

### Cannot delete capacity provider
<a name="lambda-managed-instances-ts-cannot-delete"></a>

**Problem:** You receive an error when attempting to delete a capacity provider.

**Cause:** You cannot delete a capacity provider that has function versions attached to it.

**Solution:**

1. Identify all function versions using the capacity provider with the `ListFunctionVersionsByCapacityProvider` API.

1. Delete or update those function versions to remove the capacity provider association.

1. Retry deleting the capacity provider.

### Generic error messages during function publishing
<a name="lambda-managed-instances-ts-generic-errors"></a>

**Problem:** You encounter generic error messages such as "Internal error occurred during publishing" when publishing functions.

**Solution:**
+ **Check IAM permissions:** Ensure you have the `lambda:PassCapacityProvider` permission for the capacity provider you're trying to use.
+ **Verify capacity provider configuration:** Confirm that your capacity provider is in the ACTIVE state using the `GetCapacityProvider` API.
+ **Review VPC configuration:** Ensure the subnets and security groups specified in your capacity provider are correctly configured and accessible.
+ **Check AWS CloudTrail logs:** Review CloudTrail logs for detailed error information about the failed operation.
+ **Check capacity provider system logs:** If the function version fails to become ACTIVE after you publish it, the system logs show the reason. For more information, see [Function version fails to become ACTIVE](#lambda-managed-instances-ts-function-not-active).

## Monitoring and observability issues
<a name="lambda-managed-instances-ts-monitoring"></a>

### Missing CloudWatch metrics
<a name="lambda-managed-instances-ts-missing-metrics"></a>

**Problem:** You don't see expected metrics in CloudWatch for your capacity provider or functions.

**Cause:** Metrics are published at 1-minute intervals. New capacity providers or functions might not have metrics available immediately.

**Solution:**

Wait at least 5-10 minutes after publishing a function version before expecting metrics to appear in CloudWatch. Verify you're looking at the correct namespace (`AWS/Lambda`) and dimensions (`CapacityProviderName`, `FunctionName`, or `InstanceType`).

### Cannot find CloudWatch logs
<a name="lambda-managed-instances-ts-no-logs"></a>

**Problem:** Your function executes successfully, but you cannot find logs in CloudWatch Logs.

**Cause:** Lambda Managed Instances run in your VPC and require network connectivity to send logs to CloudWatch Logs. Without proper VPC connectivity configuration, your functions cannot reach the CloudWatch Logs service endpoint.

**Solution:**

Configure VPC connectivity to enable your functions to send logs to CloudWatch Logs. You have three options:

**Option 1: VPC endpoint for CloudWatch Logs (recommended for production)**

1. Open the Amazon VPC console at [console.aws.amazon.com/vpc/](http://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, choose **AWS services**.

1. For **Service name**, select `com.amazonaws.region.logs` (replace `region` with your AWS Region).

1. For **VPC**, select the VPC used by your capacity provider.

1. For **Subnets**, select the subnets where you want to create endpoint network interfaces. For high availability, select subnets in multiple Availability Zones.

1. For **Security groups**, select security groups that allow inbound HTTPS traffic (port 443) from your function's security group.

1. Enable **Private DNS** for the endpoint.

1. Choose **Create endpoint**.

**Option 2: Public subnet with internet gateway**

If your capacity provider uses public subnets, ensure:

1. An internet gateway is attached to your VPC

1. The route table routes `0.0.0.0/0` traffic to the internet gateway

1. Security groups allow outbound HTTPS traffic on port 443

**Option 3: Private subnet with NAT gateway**

If your capacity provider uses private subnets, ensure:

1. A NAT gateway exists in a public subnet

1. The private subnet route table routes `0.0.0.0/0` traffic to the NAT gateway

1. The public subnet route table routes `0.0.0.0/0` traffic to an internet gateway

1. Security groups allow outbound HTTPS traffic on port 443

For detailed guidance on VPC connectivity options, see [VPC connectivity for Lambda Managed Instances](lambda-managed-instances-networking.md).

### Difficulty correlating logs from concurrent requests
<a name="lambda-managed-instances-ts-log-correlation"></a>

**Problem:** Logs from different requests are interleaved, making it difficult to trace individual requests.

**Cause:** Log interleaving is expected and standard behavior in multi-concurrent systems.

**Solution:**
+ **Use structured logging with JSON format:** Include request ID in all log statements
+ **Java:** Use Log4j with `ThreadContext` to automatically include request ID
+ **Node.js:** Use `console.log()` with JSON formatting and include `InvokeStore.getRequestId()`
+ **Python:** Use the standard logging module with JSON formatting and include `context.request_id`

For detailed guidance, see the runtime-specific documentation pages.

## Getting additional help
<a name="lambda-managed-instances-ts-getting-help"></a>

If you continue to experience issues after trying these solutions:

1. **Review CloudWatch metrics:** Check capacity provider and execution environment metrics to identify resource constraints or scaling issues.

1. **Check AWS CloudTrail logs:** Review CloudTrail logs for detailed information about API calls and errors.

1. **Contact AWS Support:** If you cannot resolve the issue, contact AWS Support with details about your capacity provider configuration, function configuration, and the specific error messages you're encountering.

## Next steps
<a name="lambda-managed-instances-ts-next-steps"></a>
+ Learn about [capacity providers for Lambda Managed Instances](lambda-managed-instances-capacity-providers.md)
+ Understand [scaling for Lambda Managed Instances](lambda-managed-instances-scaling.md)
+ Review runtime-specific guides for [Java](lambda-managed-instances-java-runtime.md), [Node.js](lambda-managed-instances-nodejs-runtime.md), and [Python](lambda-managed-instances-python-runtime.md)
+ Monitor Lambda Managed Instances with [CloudWatch metrics](lambda-managed-instances-monitoring.md)
+ Review [best practices for Lambda Managed Instances](lambda-managed-instances-best-practices.md)