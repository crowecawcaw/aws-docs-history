

# Troubleshooting with Amazon ECS Action Logs

Action Logs help you diagnose issues by providing detailed records of Amazon ECS service-initiated operations. Each log entry contains a timestamp, log level, event name, and a detail payload with context about what happened and why. This topic covers common troubleshooting scenarios and provides ready-to-use CloudWatch Logs Insights queries. The scenarios in this topic are examples rather than a complete list. Action Logs supports a growing set of events and failure reasons, and each scenario shows one common cause. Use the resolutions as a starting point for your investigation.

## Understanding log levels
<a name="action-logs-troubleshooting-log-levels"></a>

Action Logs use three log levels to indicate the severity of each event:

`INFO`  
Normal operations such as deployment started, task launched, or resource provisioned. These events indicate that Amazon ECS is performing actions as expected.

`WARN`  
Non-fatal issues that might need attention, such as retry attempts or capacity constraints. Amazon ECS continues to make progress, but the operation might take longer than expected.

`ERROR`  
Failures that require action, such as deployment failed, provisioning error, or task start impaired. Review these events to identify the root cause and take corrective action.

**Tip**  
Start by filtering for `ERROR` or `WARN` log levels to identify issues quickly. You can then expand your search to `INFO` events for additional context.

## Debugging a failed service deployment
<a name="action-logs-troubleshooting-failed-deployment"></a>

**Symptoms**

Deployment stuck in progress or automatically rolled back.

**What to look for**

Filter for `ERROR` logs where `eventName` contains `DEPLOYMENT`. Check the `detail` payload for the deployment ARN, status reason, and failed task count.

The following example shows a deployment failure where no rollback candidate was available:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "service/my-cluster/my-service",
  "logLevel": "ERROR",
  "eventTimestamp": 1784573730986,
  "detail": {
    "statusReason": "No rollback candidate was found to run the rollback.",
    "serviceDeploymentArn": "arn:aws:ecs:us-east-1:111122223333:service-deployment/my-cluster/my-service/abc123def456",
    "status": "FAILED",
    "eventName": "SERVICE_DEPLOYMENT_ROLLBACK_FAILED"
  }
}
```

**Resolution**

Check the `detail.statusReason` field to identify why tasks failed. Use the following CloudWatch Logs Insights query to find all deployment errors:

```
fields @timestamp, detail.statusReason
| filter logLevel = "ERROR" and detail.deploymentArn like /{{my-cluster}}\/{{my-service}}/
| sort @timestamp desc
| limit 20
```

## Diagnosing managed daemon issues
<a name="action-logs-troubleshooting-daemon"></a>

**Symptoms**

Daemon not starting on instances or daemon deployment stuck.

**What to look for**

Filter logs by the daemon ARN to find events related to your daemon. You can also filter by `logLevel` to narrow results to warnings or errors.

The following example shows a daemon task that failed to start due to insufficient memory on the target instance:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "daemon/my-cluster/my-logging-daemon",
  "logLevel": "WARN",
  "eventTimestamp": 1719500050000,
  "detail": {
    "statusReason": "RESOURCE:MEMORY - Unable to place daemon task on container instance: insufficient memory",
    "containerInstanceArn": "arn:aws:ecs:us-east-1:111122223333:container-instance/my-cluster/a1b2c3d4",
    "eventName": "DAEMON_TASK_START_IMPAIRED"
  }
}
```

**Resolution**

Verify that target instances have sufficient resources to run the daemon task. If instances are draining, the daemon might not start until new instances become available. Use the following query to filter events for a specific daemon:

```
fields @timestamp, logLevel, detail.statusReason
| filter actionSourceId like /{{my-logging-daemon}}/
| filter logLevel in ["ERROR", "WARN"]
| sort @timestamp desc
| limit 20
```

## Understanding daemon task stop reasons
<a name="action-logs-troubleshooting-daemon-task-stops"></a>

**Symptoms**

Daemon tasks stopping unexpectedly.

**What to look for**

Filter for `WARN` and `ERROR` logs that contain daemon task failure details. The following fields in the `detail` payload provide information about why a daemon task stopped:

`detail.stopCode`  
A machine-readable code that categorizes the reason for the task stop.

`detail.statusReason`  
A human-readable description of why the task stopped. This field is not present in all log entries.

`detail.containerStoppedReason`  
Additional context about the specific container that caused the task to stop.

For a full list of task stop codes and their descriptions, see [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md).

**Note**  
Expected daemon task stops, such as `UserInitiated`, are filtered out from Action Logs. You only see unexpected or error-related daemon task stops.

## Debugging a task that fails to start
<a name="action-logs-troubleshooting-task-start"></a>

**Symptoms**

A task never reaches the running state and stops during launch.

**What to look for**

Filter for `ERROR` logs where `detail.eventName` is `TASK_FAILED_TO_START`. The `detail.stopCode` field is `TaskFailedToStart`, and `detail.lastStatus` shows the stage the task failed in: `PROVISIONING`, `PENDING`, or `ACTIVATING`. The `detail.statusReason` field explains the cause.

The following example shows a task that failed to start because Amazon ECS could not pull the container image:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "cluster/my-cluster",
  "logLevel": "ERROR",
  "eventTimestamp": 1784573730986,
  "detail": {
    "statusReason": "CannotPullContainerError: pull image manifest has been retried 7 time(s): failed to resolve ref public.ecr.aws/nginx/nginx:does-not-exist: public.ecr.aws/nginx/nginx:does-not-exist: not found",
    "taskArn": "arn:aws:ecs:us-east-1:111122223333:task/my-cluster/1234567890abcdef0",
    "stopCode": "TaskFailedToStart",
    "lastStatus": "PENDING",
    "eventName": "TASK_FAILED_TO_START"
  }
}
```

**Resolution**

The fix depends on the `detail.statusReason` value. For the image pull failure shown in the example, verify that the image URI and tag exist. Confirm that the task execution role can pull from the registry. Other causes include volume attachment failures, a subnet with no free IP addresses, and a capacity provider that could not supply capacity in time.

For a standalone task, `actionSourceId` is the cluster. For a service task or a managed daemon task, it is the service or the daemon. Use the following CloudWatch Logs Insights query to find tasks that failed to start:

```
fields @timestamp, detail.lastStatus, detail.statusReason
| filter detail.eventName = "TASK_FAILED_TO_START" and detail.taskArn like /{{my-cluster}}/
| sort @timestamp desc
| limit 20
```

## Investigating tasks stopped by failed health checks
<a name="action-logs-troubleshooting-health-check"></a>

**Symptoms**

A service repeatedly stops and replaces tasks that start successfully but fail load balancer health checks.

**What to look for**

Filter for `ERROR` logs where `detail.eventName` is `TASK_STOPPED_UNHEALTHY`. For a load balancer health check, `detail.failureType` is `ELB_HEALTH_CHECK` and `detail.stopCode` is always `ServiceSchedulerInitiated`. The `detail.reasonCode` and `detail.reasonDescription` fields explain the failure. The `detail.healthCheckPath`, `detail.healthCheckPort`, `detail.healthCheckProtocol`, `detail.unhealthyThresholdCount`, `detail.healthCheckIntervalSeconds`, and `detail.targetGroupArn` fields describe the health check that failed.

The following example shows a task that Amazon ECS stopped because it failed load balancer health checks:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "service/my-cluster/my-service",
  "logLevel": "ERROR",
  "eventTimestamp": 1784573730986,
  "detail": {
    "clusterArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
    "taskArn": "arn:aws:ecs:us-east-1:111122223333:task/my-cluster/1234567890abcdef0",
    "stopCode": "ServiceSchedulerInitiated",
    "statusReason": "Task failed ELB health checks in (target-group arn:aws:elasticloadbalancing:us-east-1:111122223333:targetgroup/my-target-group/1234567890abcdef)",
    "failureType": "ELB_HEALTH_CHECK",
    "lastStatus": "DEACTIVATING",
    "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:111122223333:targetgroup/my-target-group/1234567890abcdef",
    "containerName": "my-container",
    "reasonCode": "Target.ResponseCodeMismatch",
    "reasonDescription": "Health checks failed with these codes: [404]",
    "healthCheckPath": "/health",
    "healthCheckPort": "traffic-port",
    "healthCheckProtocol": "HTTP",
    "unhealthyThresholdCount": 2,
    "healthCheckIntervalSeconds": 5,
    "eventName": "TASK_STOPPED_UNHEALTHY"
  }
}
```

A container health check failure instead sets `detail.failureType` to `CONTAINER_HEALTH_CHECK` and lists the affected containers in `detail.unhealthyContainerNames`. Amazon ECS publishes one record for each task, even when the task uses several target groups. Amazon ECS does not publish these records during the health check grace period or for scale-in.

**Resolution**

Compare the health check path, port, and protocol against what the container actually serves. If the application needs longer to become ready, raise the health check grace period. Use the following CloudWatch Logs Insights query to find health check failures:

```
fields @timestamp, detail.reasonCode, detail.reasonDescription, detail.targetGroupArn
| filter detail.eventName = "TASK_STOPPED_UNHEALTHY" and detail.targetGroupArn like /{{my-target-group}}/
| sort @timestamp desc
| limit 20
```

## Resolving capacity provider failures
<a name="action-logs-troubleshooting-capacity-provider"></a>

**Symptoms**

A capacity provider create, update, or delete request fails after Amazon ECS accepts it.

**What to look for**

Filter for `ERROR` logs where `detail.eventName` is `CAPACITY_PROVIDER_CREATE_FAILED`. The `CAPACITY_PROVIDER_UPDATE_FAILED` and `CAPACITY_PROVIDER_DELETE_FAILED` events behave the same way. These events cover asynchronous failures only. Amazon ECS does not log a request that synchronous validation rejects. The `detail.statusReason` field matches the `updateStatusReason` field that `DescribeCapacityProviders` returns, and `actionSourceId` is the capacity provider.

The following example shows a capacity provider that failed to create because its IAM instance profile does not exist:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "capacity-provider/my-capacity-provider",
  "logLevel": "ERROR",
  "eventTimestamp": 1784573730986,
  "detail": {
    "status": "FAILED",
    "statusReason": "The IamInstanceProfile.Arn 'arn:aws:iam::111122223333:instance-profile/my-instance-profile' does not exist.",
    "eventName": "CAPACITY_PROVIDER_CREATE_FAILED"
  }
}
```

**Resolution**

Confirm that the referenced IAM instance profile, subnets, and security groups exist, and that Amazon ECS has permission to use them. Then retry the request. Use the following CloudWatch Logs Insights query to find capacity provider failures:

```
fields @timestamp, detail.eventName, detail.statusReason
| filter detail.eventName like /CAPACITY_PROVIDER_.*_FAILED/ and actionSourceId like /{{my-capacity-provider}}/
| sort @timestamp desc
| limit 20
```

## Finding instances that never join the cluster
<a name="action-logs-troubleshooting-instance-registration"></a>

**Symptoms**

An Auto Scaling group launches instances, but they never appear as container instances in the cluster.

**What to look for**

Filter for `ERROR` logs where `detail.eventName` is `EC2_INSTANCE_NEVER_REGISTERED`. Amazon ECS publishes this event when an Auto Scaling group instance has been in service for 15 minutes without registering with the cluster. Amazon ECS publishes one record for each instance. It does not publish this event for warm pool instances or for instances terminated before 15 minutes. The `actionSourceId` field is the capacity provider.

The following example shows an instance that launched but never registered with the cluster:

```json
{
  "resourceArn": "arn:aws:ecs:us-east-1:111122223333:cluster/my-cluster",
  "actionSourceId": "capacity-provider/my-capacity-provider",
  "logLevel": "ERROR",
  "eventTimestamp": 1784573730986,
  "detail": {
    "status": "FAILED",
    "statusReason": "EC2 instance i-1234567890abcdef0 (t3.medium) launched but did not register with the ECS cluster within 15 minutes.",
    "eventName": "EC2_INSTANCE_NEVER_REGISTERED"
  }
}
```

**Resolution**

The usual cause is instance user data that writes the wrong `ECS_CLUSTER` value. The instance might also lack network access to the Amazon ECS endpoint or the required IAM instance profile permissions. Amazon ECS publishes a related event, `CONTAINER_INSTANCE_REGISTRATION_FAILED`, when an instance attempts registration and fails outright, for example when the subnet has no free IP addresses. Use the following CloudWatch Logs Insights query to find instances that never registered:

```
fields @timestamp, detail.statusReason
| filter detail.eventName = "EC2_INSTANCE_NEVER_REGISTERED" and actionSourceId like /{{my-capacity-provider}}/
| sort @timestamp desc
| limit 20
```

## Useful CloudWatch Logs Insights queries
<a name="action-logs-troubleshooting-queries"></a>

Use the following CloudWatch Logs Insights queries to investigate common issues with your Amazon ECS services.

**All errors in the last hour**

```
fields @timestamp, logLevel, eventName, detail.statusReason
| filter logLevel = "ERROR"
| sort @timestamp desc
| limit 50
```

**Note**  
The `detail.statusReason` field is not present in all log entries. If the field is empty in your results, use the `eventName` and other fields in the `detail` payload for context.

**Events for a specific service**

```
fields @timestamp, logLevel, detail.statusReason
| filter @message like /{{my-service}}/
| sort @timestamp desc
| limit 50
```

**Deployment timeline for a specific deployment**

```
fields @timestamp, logLevel, detail.statusReason
| filter detail.deploymentArn like /{{my-cluster}}\/{{my-service}}\/{{abc123}}/
| sort @timestamp asc
```

**Daemon task failures grouped by reason**

```
filter logLevel = "ERROR" and detail.stopCode != ""
| stats count(*) as failureCount by detail.stopCode, detail.statusReason
| sort failureCount desc
| limit 20
```

**Tasks that failed to start, grouped by reason**

```
filter detail.eventName = "TASK_FAILED_TO_START"
| stats count(*) as failureCount by detail.statusReason
| sort failureCount desc
| limit 20
```

**Health check failures by target group**

```
filter detail.eventName = "TASK_STOPPED_UNHEALTHY"
| stats count(*) as failureCount by detail.targetGroupArn, detail.reasonCode
| sort failureCount desc
| limit 20
```