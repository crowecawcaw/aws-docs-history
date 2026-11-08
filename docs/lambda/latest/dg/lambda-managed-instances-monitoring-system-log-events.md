

# Capacity provider system log event reference
<a name="lambda-managed-instances-monitoring-system-log-events"></a>

Lambda publishes system log events for your capacity provider and for the function versions, Amazon EC2 instances, and execution environments that it manages. This topic describes the format of each log entry, the metadata fields that log entries can contain, and the events that Lambda publishes.

For more information about configuring the system log level, see [Log-level filtering for capacity provider system logs](lambda-managed-instances-monitoring-log-levels.md).

## Log entry format
<a name="lambda-managed-instances-log-format-json-structure"></a>

Capacity provider system logs use structured JSON format. Each system log entry is a JSON object that contains the following top-level fields:


| Field | Type | Description | 
| --- | --- | --- | 
| timestamp | String | The time the log event was generated, in ISO 8601 format. | 
| level | String | The log level of the event: DEBUG, INFO, WARN, or ERROR. | 
| operation | String | The category of the event: FunctionLifecycle, Autoscaling, InstanceLifecycle, or ExecutionEnvironmentLifecycle. | 
| message | String | A human-readable description of the event. | 
| metadata | Object | Structured details about the event. The fields in this object vary by event. For a description of each field, see [Metadata fields](#lambda-managed-instances-log-format-metadata). | 

The following example shows a system log entry for a function version that has become active:

```
{
  "timestamp": "2026-07-22T18:09:30.000Z",
  "level": "INFO",
  "operation": "FunctionLifecycle",
  "message": "Function version is active.",
  "metadata": {
    "capacityProviderArn": "arn:aws:lambda:us-west-2:111122223333:capacity-provider:my-capacity-provider",
    "functionName": "my-function",
    "functionVersionArn": "arn:aws:lambda:us-west-2:111122223333:function:my-function:1",
    "functionVersion": "1",
    "lastUpdateStatus": "Successful",
    "executionEnvironmentCount": 3
  }
}
```

Because each log entry is structured JSON, you can use CloudWatch Logs filter patterns to find related events. For example:
+ All events for a category: `{ $.operation = "FunctionLifecycle" }`
+ All events for a function: `{ $.metadata.functionName = "my-function" }`
+ All events for a function, plus capacity provider events that aren't tied to a specific function: `{ $.metadata.functionName = "my-function" || $.metadata.functionName NOT EXISTS }`
+ All warnings and errors: `{ $.level = "WARN" || $.level = "ERROR" }`

## System log event level mapping
<a name="lambda-managed-instances-system-log-event-mapping"></a>

Each event has a fixed log level, shown in the event tables in this topic. The system log level that you configure for your capacity provider determines which events Lambda sends:


| Event level | System log level `DEBUG` | System log level `INFO` | System log level `WARN` | 
| --- | --- | --- | --- | 
| DEBUG | Logged | Not logged | Not logged | 
| INFO | Logged | Logged | Not logged | 
| WARN | Logged | Logged | Logged | 
| ERROR | Logged | Logged | Logged | 

## FunctionLifecycle events
<a name="lambda-managed-instances-system-log-events-function-lifecycle"></a>

`FunctionLifecycle` events track each function version that runs on the capacity provider, from activation through deletion. Messages are the same for numbered versions and `$LATEST.PUBLISHED`. To tell them apart, use the `functionVersion` field.

All `FunctionLifecycle` events include the following metadata fields: `capacityProviderArn`, `functionName`, `functionVersionArn`, `functionVersion`, and `lastUpdateStatus`.


| Message | Level | When emitted | Additional metadata | 
| --- | --- | --- | --- | 
| Function version is being activated. | INFO | A function version is added to the capacity provider and activation begins. |  + `minExecutionEnvironments`<br />+ `maxExecutionEnvironments` (only when configured)  | 
| Function version is active. | INFO | The function version is active and ready to serve invocations. |  + `executionEnvironmentCount`  | 
| Function version activation failed. | ERROR | The function version failed to activate. | + `stateReasonCode`Depending on the reason code, also `kmsKeyArn`, `subnetIds`, or `securityGroupIds`. For details, see [Capacity provider settings in failure events](#lambda-managed-instances-system-log-events-cp-config-fields). | 
| Function scaling configuration is being updated. | INFO | Lambda accepts an update to the function's scaling configuration and the update is in progress. |  + `previousMinExecutionEnvironments`<br />+ `previousMaxExecutionEnvironments` (only when configured)<br />+ `newMinExecutionEnvironments`<br />+ `newMaxExecutionEnvironments` (only when configured)  | 
| Function scaling configuration updated. | INFO | The scaling configuration update completed. |  + `previousMinExecutionEnvironments`<br />+ `previousMaxExecutionEnvironments` (only when configured)<br />+ `newMinExecutionEnvironments`<br />+ `newMaxExecutionEnvironments` (only when configured)  | 
| Function scaling configuration update failed. | ERROR | The scaling configuration update failed. | + `lastUpdateStatusReasonCode`Depending on the reason code, also `kmsKeyArn`, `subnetIds`, or `securityGroupIds`. For details, see [Capacity provider settings in failure events](#lambda-managed-instances-system-log-events-cp-config-fields). | 
| Function version is being deactivated. | INFO | Lambda begins deactivating the function version. | None | 
| Function version is deactivated. | INFO | The function version is fully deactivated. | None | 
| Function version is being deleted. | INFO | Lambda begins removing the function version from the capacity provider. | None | 
| Function version is deleted. | INFO | The function version is fully removed from the capacity provider. | None | 
| No available capacity: requesting new instance launch. | INFO | The existing instances in the capacity provider can't host the execution environments that the function version needs, so Lambda requests new instances. |  + `executionEnvironmentDeficit`  | 

### Capacity provider settings in failure events
<a name="lambda-managed-instances-system-log-events-cp-config-fields"></a>

When the reason code of a `Function version activation failed.` or `Function scaling configuration update failed.` event points to a capacity provider setting, the event also includes that setting as configured on the capacity provider. This helps you identify which resource to fix.


| Reason codes | Field added | Value | 
| --- | --- | --- | 
| KMSKeyAccessDenied, KMSKeyNotFound, InvalidStateKMSKey, DisabledKMSKey | kmsKeyArn | The AWS KMS key ARN configured on the capacity provider. | 
| InvalidSubnet, SubnetOutOfIPAddresses | subnetIds | All subnet IDs configured on the capacity provider. | 
| InvalidSecurityGroup | securityGroupIds | All security group IDs configured on the capacity provider. | 

These fields contain the values configured on the capacity provider. For details about the failed launch, such as the instance type, Availability Zone, and Amazon EC2 error code, look for the corresponding `InstanceLifecycle` launch failure event.

The following example shows a function version activation failure caused by an AWS KMS key issue:

```
{
  "timestamp": "2026-07-22T18:25:00.000Z",
  "level": "ERROR",
  "operation": "FunctionLifecycle",
  "message": "Function version activation failed.",
  "metadata": {
    "capacityProviderArn": "arn:aws:lambda:us-west-2:111122223333:capacity-provider:my-capacity-provider",
    "functionName": "my-function",
    "functionVersionArn": "arn:aws:lambda:us-west-2:111122223333:function:my-function:1",
    "functionVersion": "1",
    "lastUpdateStatus": "Failed",
    "stateReasonCode": "KMSKeyAccessDenied",
    "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }
}
```

## Autoscaling events
<a name="lambda-managed-instances-system-log-events-autoscaling"></a>

`Autoscaling` events record scaling decisions that Lambda makes based on resource utilization, and the limits that prevent scaling.

All `Autoscaling` events include the `capacityProviderArn` metadata field. Events that apply to a specific function version also include `functionName`, `functionVersionArn`, and `functionVersion`. Events that apply to the whole capacity provider don't include function fields.


| Message | Level | When emitted | Additional metadata | 
| --- | --- | --- | --- | 
| Scale-out triggered: Resource utilization exceeded threshold. | INFO | The utilization of at least one resource exceeded its scale-out threshold. |  + `action` (`scaleOut`)<br />+ `resources` (the resources that exceeded their threshold)<br />+ `currentCpuUtilization` (if `cpu` is in `resources`)<br />+ `currentConcurrencyUtilization` (if `concurrency` is in `resources`)  | 
| Scale-in triggered: Resource utilization fell below threshold. | INFO | The utilization of all measured resources fell below their scale-in thresholds. |  + `action` (`scaleIn`)<br />+ `resources` (all measured resources)<br />+ `currentCpuUtilization` (if `cpu` is in `resources`)<br />+ `currentConcurrencyUtilization` (if `concurrency` is in `resources`)  | 
| Scale-out blocked: function's maximum execution environments reached. | WARN | Lambda attempted to scale out, but the function version already has its maximum number of execution environments. |  + `action` (`scaleOut`)<br />+ `maxExecutionEnvironments`<br />+ `executionEnvironmentCount`  | 
| Scale-in blocked: function's minimum execution environments reached. | WARN | Demand fell below the function version's minimum number of execution environments, so Lambda didn't scale in further. |  + `action` (`scaleIn`)<br />+ `minExecutionEnvironments`<br />+ `executionEnvironmentCount`  | 
| Scale-out blocked: capacity provider's maximum vCPU reached. | WARN | Lambda attempted to scale out, but the capacity provider has reached its maximum vCPU limit. This event applies to the whole capacity provider and doesn't include function fields. |  + `action` (`scaleOut`)<br />+ `currentVCPU`<br />+ `vCPULimit`  | 
| No configured instance type can satisfy function resource requirements. Please add an instance type that satisfies the required resources to the allowed instance type list. | WARN | Lambda attempted to scale out, but the function version requires more resources than the capacity provider's instance type provides. |  + `action` (`scaleOut`)<br />+ `instanceTypes`<br />+ `incompatibleResources`<br />+ `requiredVCPU`<br />+ `requiredMemoryMiB`  | 
| Workers scaling to zero: no active functions remain. | INFO | All function versions were removed from the capacity provider, so Lambda is scaling its instances to zero. This event applies to the whole capacity provider and doesn't include function fields or action. | None | 

The following example shows a scale-out event triggered by CPU utilization:

```
{
  "timestamp": "2026-07-22T18:15:30.000Z",
  "level": "INFO",
  "operation": "Autoscaling",
  "message": "Scale-out triggered: Resource utilization exceeded threshold.",
  "metadata": {
    "capacityProviderArn": "arn:aws:lambda:us-west-2:111122223333:capacity-provider:my-capacity-provider",
    "functionName": "my-function",
    "functionVersionArn": "arn:aws:lambda:us-west-2:111122223333:function:my-function:1",
    "functionVersion": "1",
    "action": "scaleOut",
    "resources": ["cpu"],
    "currentCpuUtilization": 78
  }
}
```

## InstanceLifecycle events
<a name="lambda-managed-instances-system-log-events-instance-lifecycle"></a>

`InstanceLifecycle` events record how Lambda manages the Amazon EC2 instances in your capacity provider, including launches, terminations, and health checks.

All `InstanceLifecycle` events include the `capacityProviderArn` metadata field. These events apply to the whole capacity provider and don't include function fields.


| Message | Level | When emitted | Additional metadata | 
| --- | --- | --- | --- | 
| Launching instance | INFO | Lambda initiates an instance launch for the capacity provider. |  + `launchRequestId`<br />+ `instanceTypes`<br />+ `availabilityZones`  | 
| Launched {{instance-type}} instance {{instance-id}} in {{availability-zone}} | INFO | An instance is running. |  + `instanceId`<br />+ `launchRequestId`<br />+ `instanceTypes`<br />+ `availabilityZones`  | 
| Failed to launch {{instance-type}} instance in {{availability-zone}}: {{error-message}} | ERROR | An instance launch attempt failed. | + `launchRequestId`<br />+ `instanceTypes`<br />+ `availabilityZones`<br />+ `errorCode`For subnet errors, also `subnetIds`. For security group errors, also `securityGroupIds`. | 
| Terminating {{instance-id}} | INFO | Lambda begins terminating an instance. |  + `instanceId`<br />+ `instanceTypes`<br />+ `availabilityZones`  | 
| Terminated {{instance-id}} | INFO | An instance is terminated. |  + `instanceId`<br />+ `instanceTypes`<br />+ `availabilityZones`  | 
| Failed to terminate {{instance-id}}: {{error}} | ERROR | Lambda failed to terminate an instance. |  + `instanceId`<br />+ `errorCode`  | 
| Health check failed for {{instance-id}}: Instance will be replaced. | ERROR | An instance failed its health check. Lambda replaces the instance. |  + `instanceId`<br />+ `instanceTypes`<br />+ `availabilityZones`  | 

The following example shows an instance launch failure caused by insufficient Amazon EC2 capacity. The message includes the error message that Amazon EC2 returned, and `errorCode` contains the Amazon EC2 error code:

```
{
  "timestamp": "2026-07-22T19:36:29.000Z",
  "level": "ERROR",
  "operation": "InstanceLifecycle",
  "message": "Failed to launch m7i.xlarge instance in us-west-2b: We currently do not have sufficient m7i.xlarge capacity in the Availability Zone you requested (us-west-2b). Our system will be working on provisioning additional capacity. You can currently get m7i.xlarge capacity by not specifying an Availability Zone in your request or choosing us-west-2a, us-west-2c, us-west-2d.",
  "metadata": {
    "capacityProviderArn": "arn:aws:lambda:us-west-2:111122223333:capacity-provider:my-capacity-provider",
    "launchRequestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "instanceTypes": ["m7i.xlarge"],
    "availabilityZones": ["us-west-2b"],
    "errorCode": "InsufficientInstanceCapacity"
  }
}
```

## ExecutionEnvironmentLifecycle events
<a name="lambda-managed-instances-system-log-events-ee-lifecycle"></a>

`ExecutionEnvironmentLifecycle` events record the creation, termination, and failure of individual execution environments on your capacity provider's instances.

All `ExecutionEnvironmentLifecycle` events include the following metadata fields: `capacityProviderArn`, `functionName`, `functionVersionArn`, `functionVersion`, `instanceId`, and `cloudWatchLogStreamName`.


| Message | Level | When emitted | Additional metadata | 
| --- | --- | --- | --- | 
| Execution environment is being created. | INFO | Lambda begins creating an execution environment on an instance. | None | 
| Execution environment created. | INFO | The execution environment is created. | None | 
| Execution environment is being terminated. | INFO | Lambda begins terminating an execution environment. | None | 
| Execution environment terminated. | INFO | The execution environment terminated normally. | None | 
| Execution environment failed. | ERROR | The execution environment failed or terminated abnormally. | + `reasonCode`For possible values, see [Execution environment failure reason codes](#lambda-managed-instances-system-log-events-reason-codes). | 
| Execution environment exceeded function's initialization timeout while initializing; replacement scheduled. | ERROR | The execution environment didn't finish initializing within the function's initialization timeout. Lambda replaces the execution environment. |  + `initElapsedTimeMs`<br />+ `initConfiguredTimeoutMs`  | 

### Execution environment failure reason codes
<a name="lambda-managed-instances-system-log-events-reason-codes"></a>

The `reasonCode` field of an `Execution environment failed.` event contains one of the following values:


| `reasonCode` | Description | 
| --- | --- | 
| RuntimeInitError | The runtime failed to initialize because of an error in the function code. | 
| ExtensionInitError | A Lambda extension failed during initialization. | 
| InvalidEntryPoint | The function handler or entry point is invalid. | 
| InvalidWorkingDirectory | The function's working directory is invalid. | 
| PermissionDenied | Permission was denied during function initialization. | 
| TooManyExtensions | The function has too many extensions configured. | 
| InitResourceExhausted | The execution environment ran out of resources, such as memory, during initialization. | 
| InitTimeout | Initialization timed out. | 
| ImageAccessDenied | Lambda can't access the container image. Check the Amazon ECR permissions. | 
| ImageDeleted | The container image was deleted from Amazon ECR. | 
| InvalidImage | The container image has an invalid manifest or layer digest. | 
| KMSKeyAccessDenied | Lambda was denied access to the AWS KMS key. | 
| InsufficientRolePermissions | Lambda couldn't assume the function's execution role. | 
| InternalError | An internal error occurred. If the error persists, contact Support. | 

## Metadata fields
<a name="lambda-managed-instances-log-format-metadata"></a>

The following table describes every field that can appear in the `metadata` object. Each event includes only the fields listed for that event in the preceding tables.


| Field | Type | Description | 
| --- | --- | --- | 
| action | String | The scaling direction of an Autoscaling event: scaleOut or scaleIn. | 
| availabilityZones | Array of strings | The Availability Zones associated with the event. | 
| capacityProviderArn | String | The ARN of the capacity provider. | 
| cloudWatchLogStreamName | String | The name of the CloudWatch Logs log stream that contains the function logs from the execution environment. | 
| currentConcurrencyUtilization | Number | The current concurrency utilization, as a percentage, that Lambda used to make the scaling decision. | 
| currentCpuUtilization | Number | The current CPU utilization, as a percentage, that Lambda used to make the scaling decision. | 
| currentVCPU | Number | The number of vCPUs currently in use by the capacity provider. | 
| errorCode | String | The error code returned by the Amazon EC2 API call that failed, for example InsufficientInstanceCapacity. | 
| executionEnvironmentCount | Number | The current number of execution environments for the function version. | 
| executionEnvironmentDeficit | Number | The number of execution environments that need capacity that the existing instances can't provide. | 
| functionName | String | The name of the function. | 
| functionVersion | String | The function version, for example 1 for a numbered version or $LATEST.PUBLISHED. | 
| functionVersionArn | String | The ARN of the function version. | 
| incompatibleResources | Array of strings | The function resource requirements that the capacity provider's instance type can't satisfy: vcpu, memory, or both. | 
| initConfiguredTimeoutMs | Number | The function's configured initialization timeout, in milliseconds. | 
| initElapsedTimeMs | Number | The time that the execution environment spent initializing before it exceeded the timeout, in milliseconds. | 
| instanceId | String | The Amazon EC2 instance ID associated with the event. For ExecutionEnvironmentLifecycle events, this is the instance that hosts the execution environment. | 
| instanceTypes | Array of strings | The Amazon EC2 instance types associated with the event. | 
| kmsKeyArn | String | The ARN of the AWS KMS key configured on the capacity provider. | 
| lastUpdateStatus | String | The status of the last update to the function version: InProgress, Successful, or Failed. This matches the LastUpdateStatus field in the Lambda API. | 
| lastUpdateStatusReasonCode | String | The reason that the last update to the function version failed. This matches the LastUpdateStatusReasonCode field in the Lambda API. | 
| launchRequestId | String | The ID of an instance launch attempt. The Launching instance event and the Launched or Failed to launch event for the same attempt share this ID. | 
| maxExecutionEnvironments | Number | The maximum number of execution environments configured for the function version. | 
| minExecutionEnvironments | Number | The minimum number of execution environments configured for the function version. | 
| newMaxExecutionEnvironments | Number | The maximum number of execution environments after the scaling configuration update. | 
| newMinExecutionEnvironments | Number | The minimum number of execution environments after the scaling configuration update. | 
| previousMaxExecutionEnvironments | Number | The maximum number of execution environments before the scaling configuration update. | 
| previousMinExecutionEnvironments | Number | The minimum number of execution environments before the scaling configuration update. | 
| reasonCode | String | The reason that an execution environment failed. For possible values, see [Execution environment failure reason codes](#lambda-managed-instances-system-log-events-reason-codes). | 
| requiredMemoryMiB | Number | The memory, in MiB, that the function version requires for each execution environment. | 
| requiredVCPU | Number | The number of vCPUs that the function version requires for each execution environment. This value can be fractional, for example 0.5. | 
| resources | Array of strings | The resources that drove a scaling decision: cpu, concurrency, or both. | 
| securityGroupIds | Array of strings | All security group IDs configured on the capacity provider. | 
| stateReasonCode | String | The reason that the function version failed to activate. Reason codes for errors in the function code start with FunctionError., for example FunctionError.RuntimeInitError. Other reason codes, such as KMSKeyAccessDenied or CapacityProviderScalingLimitExceeded, have no prefix. | 
| subnetIds | Array of strings | All subnet IDs configured on the capacity provider. | 
| vCPULimit | Number | The maximum number of vCPUs configured for the capacity provider. | 

**Note**  
This list expands as Lambda adds new capacity provider capabilities.