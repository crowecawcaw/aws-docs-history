

# Troubleshooting with Amazon ECS Action Logs
<a name="action-logs-troubleshooting"></a>

Action Logs help you diagnose issues by providing detailed records of Amazon ECS service-initiated operations. Each log entry contains a timestamp, log level, event name, and a detail payload with context about what happened and why. This topic covers common troubleshooting scenarios and provides ready-to-use CloudWatch Logs Insights queries.

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

Deployment stuck in progress or automatically rolled back.

Filter for `ERROR` logs where `eventName` contains `DEPLOYMENT`. Check the `detail` payload for the deployment ARN, status reason, and failed task count.

The following example shows a deployment failure where no rollback candidate was available:

```
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

Check the `detail.statusReason` field to identify why tasks failed. Use the following CloudWatch Logs Insights query to find all deployment errors:

```
fields @timestamp, detail.statusReason
| filter logLevel = "ERROR" and detail.deploymentArn like /{{my-cluster}}\/{{my-service}}/
| sort @timestamp desc
| limit 20
```

## Diagnosing managed daemon issues
<a name="action-logs-troubleshooting-daemon"></a>

Daemon not starting on instances or daemon deployment stuck.

Filter logs by the daemon ARN to find events related to your daemon. You can also filter by `logLevel` to narrow results to warnings or errors.

The following example shows a daemon task that failed to start due to insufficient memory on the target instance:

```
{
  "timestamp": 1719500050000,
  "logLevel": "WARN",
  "account": "123456789012",
  "region": "us-east-1",
  "resourceArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
  "actionSourceId": "arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-logging-daemon",
  "eventName": "DAEMON_TASK_START_IMPAIRED",
  "detail": {
    "statusReason": "RESOURCE:MEMORY - Unable to place daemon task on container instance: insufficient memory",
    "containerInstanceArn": "arn:aws:ecs:us-east-1:123456789012:container-instance/my-cluster/a1b2c3d4"
  }
}
```

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

Daemon tasks stopping unexpectedly.

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