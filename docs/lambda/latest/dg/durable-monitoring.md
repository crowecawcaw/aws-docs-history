# Monitoring durable functions

You can monitor your durable functions using CloudWatch metrics, CloudWatch Logs, and tracing. Because durable functions can run for extended periods and span multiple function invocations, monitoring them requires understanding their unique execution patterns, including checkpoints, state transitions, and replay behavior.

## CloudWatch metrics

Lambda automatically publishes metrics to CloudWatch at no additional charge. Durable functions provide additional metrics beyond standard Lambda metrics to help you monitor long-running workflows, state management, and resource utilization.

### Durable execution metrics

Lambda emits the following metrics for durable executions:

| Metric                                           | Description                                                                                    |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `ApproximateRunningDurableExecutions`            | Number of durable executions in the RUNNING state                                              |
| `ApproximateRunningDurableExecutionsUtilization` | Percentage of your account's maximum running durable executions quota currently in use         |
| `DurableExecutionDuration`                       | Elapsed wall-clock time in milliseconds that a durable execution remained in the RUNNING state |
| `DurableExecutionStarted`                        | Number of durable executions that started                                                      |
| `DurableExecutionStopped`                        | Number of durable executions stopped using the StopDurableExecution API                        |
| `DurableExecutionSucceeded`                      | Number of durable executions that completed successfully                                       |
| `DurableExecutionFailed`                         | Number of durable executions that completed with a failure                                     |
| `DurableExecutionTimedOut`                       | Number of durable executions that exceeded their configured execution timeout                  |
| `DurableExecutionOperations`                     | Cumulative number of operations performed within a durable execution (max: 3,000)              |
| `DurableExecutionStorageWrittenBytes`            | Cumulative amount of data in bytes persisted by a durable execution (max: 100 MB)              |

### CloudWatch metrics

Lambda emits standard invocation, performance, and concurrency metrics for durable functions. Because a durable execution can span multiple function invocations as it progresses through checkpoints and replays, these metrics behave differently than for standard functions:

- **Invocations:** Counts each function invocation, including replays. A single durable execution can generate multiple invocation data points.
- **Duration:** Measures each function invocation separately. Use `DurableExecutionDuration` for total time taken by a single durable execution.
- **Errors:** Tracks function invocation failures. Use `DurableExecutionFailed` for execution-level failures.

For a complete list of standard Lambda metrics, see [Types of metrics for Lambda functions](monitoring-metrics-types.md "monitoring-metrics-types.md").

### Creating CloudWatch alarms

Create CloudWatch alarms to notify you when metrics exceed thresholds. Common alarms include:

- `ApproximateRunningDurableExecutionsUtilization` exceeds 80% of your quota
- `DurableExecutionFailed` increases above a threshold
- `DurableExecutionTimedOut` indicates executions are timing out
- `DurableExecutionStorageWrittenBytes` approaches storage limits

For more information, [see Using CloudWatch alarms.](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

.

## EventBridge events

Lambda publishes durable execution status change events to EventBridge. You can use these events to trigger workflows, send notifications, or track execution lifecycle changes across your durable functions.

### Durable execution status change events

Lambda emits an event to EventBridge whenever a durable execution changes status. These events have the following characteristics:

- **Source:** `aws.lambda`
- **Detail type:** `Durable Execution Status Change`

Status change events are published for the following execution states:

- `RUNNING` - Execution started
- `SUCCEEDED` - Execution completed successfully
- `STOPPED` - Execution stopped using the StopDurableExecution API
- `FAILED` - Execution failed with an error
- `TIMED_OUT` - Execution exceeded the configured timeout

The following example shows a durable execution status change event:

```

{
  "version": "0",
  "id": "d019b03c-a8a3-9d58-85de-241e96206538",
  "detail-type": "Durable Execution Status Change",
  "source": "aws.lambda",
  "account": "123456789012",
  "time": "2025-11-20T13:08:22Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "durableExecutionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function:$LATEST/durable-execution/090c4189-b18b-4296-9d0c-cfd01dc3a122/9f7d84c9-ea3d-3ffc-b3e5-5ec51c34ffc9",
    "durableExecutionName": "order-123",
    "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function:2",
    "status": "RUNNING",
    "startTimestamp": "2025-11-20T13:08:22.345Z"
  }
}

```

For terminal states (`SUCCEEDED`, `STOPPED`, `FAILED`, `TIMED_OUT`), the event includes an `endTimestamp` field indicating when the execution completed.

### Creating EventBridge rules

Create rules to route durable execution status change events to targets like Amazon Simple Notification Service, Amazon Simple Queue Service, or other Lambda functions.

The following example creates a rule that matches all durable execution status changes:

```

{
  "source": ["aws.lambda"],
  "detail-type": ["Durable Execution Status Change"]
}

```

The following example creates a rule that matches only failed executions:

```

{
  "source": ["aws.lambda"],
  "detail-type": ["Durable Execution Status Change"],
  "detail": {
    "status": ["FAILED"]
  }
}

```

The following example creates a rule that matches status changes for a specific function:

```

{
  "source": ["aws.lambda"],
  "detail-type": ["Durable Execution Status Change"],
  "detail": {
    "functionArn": [{
      "prefix": "arn:aws:lambda:us-east-1:123456789012:function:my-function"
    }]
  }
}

```

For more information about creating rules, see [Amazon EventBridge tutorials](../../../eventbridge/latest/userguide/eb-tutorial.md "../../../eventbridge/latest/userguide/eb-tutorial.md") in the EventBridge User Guide.

## AWS X-Ray tracing

You can enable X-Ray tracing on your durable functions. Lambda passes the X-Ray trace header to the durable execution, allowing you to trace requests across your workflow.

To enable X-Ray; tracing using the Lambda console, choose your function, then choose Configuration, Monitoring and operations tools, and turn on Active tracing under X-Ray.

To enable X-Ray tracing using the AWS CLI:

```

aws lambda update-function-configuration \
    --function-name my-durable-function \
    --tracing-config Mode=Active

```

To enable AWS X-Ray tracing using AWS SAM:

```

Resources:
  MyDurableFunction:
    Type: AWS::Serverless::Function
    Properties:
      Tracing: Active
      DurableConfig:
        ExecutionTimeout: 3600

```

For more information about X-Ray, [see the AWS X-Ray Developer Guide.](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")
