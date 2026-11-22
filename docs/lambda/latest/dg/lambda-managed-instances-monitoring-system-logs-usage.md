

# Using capacity provider system logs

Capacity provider system logs record what Lambda does on your behalf. This topic explains how to find the logs, how to filter them, and how to read and correlate each type of log. For the full list of events and metadata fields, see [Capacity provider system log event reference](lambda-managed-instances-monitoring-system-log-events.md).

## Finding and querying system logs
<a name="lambda-managed-instances-system-logs-usage-query"></a>

Lambda sends system logs to the capacity provider's log group in CloudWatch Logs. To find the log group and view the logs, see [Viewing CloudWatch logs for capacity providers](lambda-managed-instances-cwl-view-logs.md).

Each log entry is a JSON object, so you can select events by any field. Use the `operation` field to choose a type of log, and the `metadata` fields to narrow down to a function, an instance, or an execution environment.

To search the logs from the AWS CLI, use `filter-log-events` with a filter pattern. The following example returns the warnings and errors from the last hour:

```bash
aws logs filter-log-events \
  --log-group-name /aws/lambda/capacity-provider/{{my-capacity-provider}} \
  --start-time $(($(date +%s) - 3600))000 \
  --filter-pattern '{ $.level = "WARN" || $.level = "ERROR" }'
```

To analyze the logs, for example to count or group events, use CloudWatch Logs Insights. The following query lists the most recent events for one function:

```
fields @timestamp, level, operation, message
| filter metadata.functionName = "{{my-function}}"
| sort @timestamp desc
| limit 100
```

Some events apply to the whole capacity provider instead of one function, for example instance launches and the capacity provider vCPU limit. These events don't include `functionName`. To include them when you filter by function, add a `NOT EXISTS` condition:

```
{ $.metadata.functionName = "{{my-function}}" || $.metadata.functionName NOT EXISTS }
```

## FunctionLifecycle logs
<a name="lambda-managed-instances-system-logs-usage-function-lifecycle"></a>

`FunctionLifecycle` logs record each function version on the capacity provider as it's activated, has its scaling configuration updated, is deactivated, and is deleted.
+ **Select the events for a function version:** Filter on `operation` and `functionVersionArn`. To follow a version from start to finish, sort the events by time.

  ```
  { $.operation = "FunctionLifecycle" && $.metadata.functionVersionArn = "{{arn:aws:lambda:us-east-1:111122223333:function:my-function:1}}" }
  ```
+ **Read the state:** Each event includes `lastUpdateStatus` (`InProgress`, `Successful`, or `Failed`).
+ **Read failures:** Failures are logged as errors. `Function version activation failed.` includes the reason code in `stateReasonCode`, and `Function scaling configuration update failed.` includes it in `lastUpdateStatusReasonCode`. The reason code tells you which logs to check next:

  ```
  { $.operation = "FunctionLifecycle" && $.level = "ERROR" && $.metadata.functionVersionArn = "{{arn:aws:lambda:us-east-1:111122223333:function:my-function:1}}" }
  ```
  + A reason code that starts with `FunctionError.` means that the execution environments failed to initialize. The `ExecutionEnvironmentLifecycle` logs for the function version show each failure and its `reasonCode`.
  + A reason code for an AWS KMS key, subnet, or security group means that a capacity provider setting caused the failure. The event also includes that setting in `kmsKeyArn`, `subnetIds`, or `securityGroupIds`. For details, see [Capacity provider settings in failure events](lambda-managed-instances-monitoring-system-log-events.md#lambda-managed-instances-system-log-events-cp-config-fields).
  + A reason code about capacity, such as `CapacityProviderScalingLimitExceeded`, means that Lambda couldn't get enough capacity. The `Autoscaling` and `InstanceLifecycle` logs show the limit that was reached or the instance launches that failed.
+ **See capacity that's still needed:** While a function version waits for capacity, `No available capacity: requesting new instance launch.` events include `executionEnvironmentDeficit`, the number of execution environments that still need an instance.
+ **Correlate with other logs:** A `FunctionLifecycle` failure is often the result of earlier events. Look at the `InstanceLifecycle`, `Autoscaling`, and `ExecutionEnvironmentLifecycle` events for the same capacity provider and function in the minutes before the failure.

## ExecutionEnvironmentLifecycle logs
<a name="lambda-managed-instances-system-logs-usage-ee-lifecycle"></a>

`ExecutionEnvironmentLifecycle` logs record each execution environment that Lambda creates and terminates for a function version on the capacity provider's instances.
+ **Select the events for a function version:** Filter on `operation` and `functionVersionArn` to see every execution environment that Lambda created, terminated, or failed for that version.

  ```
  { $.operation = "ExecutionEnvironmentLifecycle" && $.metadata.functionVersionArn = "{{arn:aws:lambda:us-east-1:111122223333:function:my-function:1}}" }
  ```
+ **Follow one execution environment:** All events for one execution environment share its `cloudWatchLogStreamName`. To narrow the results to one execution environment, add a condition on that field.

  ```
  { $.operation = "ExecutionEnvironmentLifecycle" && $.metadata.cloudWatchLogStreamName = "{{log-stream-name}}" }
  ```
+ **Open the function's logs:** `cloudWatchLogStreamName` is also the name of the log stream that contains the function's own logs from that execution environment. Open it in the function's log group to see output and errors from your code, such as initialization errors.
+ **Read failures:** Failures are logged as errors. `Execution environment failed.` events include `reasonCode`. For the possible values, see [Execution environment failure reason codes](lambda-managed-instances-monitoring-system-log-events.md#lambda-managed-instances-system-log-events-reason-codes). The initialization timeout event includes `initElapsedTimeMs` and `initConfiguredTimeoutMs`.

  ```
  { $.operation = "ExecutionEnvironmentLifecycle" && $.level = "ERROR" && $.metadata.functionVersionArn = "{{arn:aws:lambda:us-east-1:111122223333:function:my-function:1}}" }
  ```
+ **Find the hosting instance:** `instanceId` is the Amazon EC2 instance that hosts the execution environment. Use it to find the related `InstanceLifecycle` events for that instance.

## Autoscaling logs
<a name="lambda-managed-instances-system-logs-usage-autoscaling"></a>

`Autoscaling` logs record the scaling decisions that Lambda makes for each function version, and the limits that stop it from scaling.
+ **See scaling decisions:** `Scale-out triggered` and `Scale-in triggered` events include `action`, the `resources` that drove the decision, and the current utilization of each resource.

  ```
  { $.operation = "Autoscaling" && $.level = "INFO" && ($.metadata.action = "scaleOut" || $.metadata.action = "scaleIn") }
  ```
+ **Find what blocked scaling:** Scaling limits are logged as warnings. Each warning names the limit and includes its current value, for example `maxExecutionEnvironments` and `executionEnvironmentCount`, or `currentVCPU` and `vCPULimit`.

  ```
  { $.operation = "Autoscaling" && $.level = "WARN" }
  ```
+ **Include capacity provider events:** The vCPU limit and scale-to-zero events apply to the whole capacity provider and don't include function fields. Include them with the `NOT EXISTS` condition described in [Finding and querying system logs](#lambda-managed-instances-system-logs-usage-query).
+ **See scaling over time:** The following CloudWatch Logs Insights query counts each type of scaling event in 5-minute intervals:

  ```
  filter operation = "Autoscaling"
  | stats count(*) by bin(5m), message
  ```

## InstanceLifecycle logs
<a name="lambda-managed-instances-system-logs-usage-instance-lifecycle"></a>

`InstanceLifecycle` logs record the Amazon EC2 instances that Lambda launches, terminates, and replaces for the capacity provider. These events apply to the whole capacity provider and don't include function fields.
+ **Follow one launch attempt:** The `Launching instance` event and the `Launched` or `Failed to launch` event for the same attempt share a `launchRequestId`. The following CloudWatch Logs Insights query shows the first and last event of each launch attempt:

  ```
  filter operation = "InstanceLifecycle" and ispresent(metadata.launchRequestId)
  | stats earliest(message) as firstEvent, latest(message) as lastEvent,
          min(@timestamp) as startTime, max(@timestamp) as endTime
    by metadata.launchRequestId
  ```
+ **Read launch failures:** A `Failed to launch` event includes the error message from Amazon EC2 and the Amazon EC2 error code in `errorCode`. For subnet and security group errors, it also includes `subnetIds` or `securityGroupIds`.
+ **Follow one instance:** After launch, events for an instance include its `instanceId`. Filter on `instanceId` to see when the instance launched, failed a health check, and terminated.

  ```
  { $.operation = "InstanceLifecycle" && $.metadata.instanceId = "{{i-0123456789abcdef0}}" }
  ```