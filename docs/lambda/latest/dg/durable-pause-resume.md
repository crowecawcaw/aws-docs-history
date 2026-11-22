

# Pausing and resuming durable executions

You can pause a running durable execution and resume it later without losing its progress. While an execution is paused, none of its code runs until you resume it. When you resume the execution, it continues from its last checkpoint on the same function version.

Each pause request applies to one execution. To pause several executions, for example every running execution of a function, list them with [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) and call [PauseDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_PauseDurableExecution.html) for each one. Pausing doesn't prevent new executions from starting. To also stop new executions, disable the function's event source mappings or stop invoking the function.

For example, you might pause executions when:
+ A downstream dependency is degraded, and further invocations can exhaust retries or write inconsistent data.
+ A deployment is in progress, and you don't want executions to call the systems that are changing.
+ An execution behaves unexpectedly, and you want to prevent it from continuing while you investigate.

If you invoke your function with the execution name of a paused execution, Lambda returns the existing execution. The execution stays paused, and Lambda doesn't start a new execution.

## Prerequisites
<a name="durable-pause-resume-prerequisites"></a>

Pausing and resuming require the `lambda:PauseDurableExecution` and `lambda:ResumeDurableExecution` actions on the durable execution ARN. For more information, see [Permissions for managing durable executions](durable-security.md#durable-manage-permissions).

If your durable function uses an AWS Key Management Service (AWS KMS) customer managed key, pause and resume requests require `kms:Decrypt` on the key. Lambda also encrypts the pause and resume reasons with that key. For more information, see [Encrypting AWS Lambda durable execution data](durable-encryption.md).

To pause an execution while an invocation is in progress, use one of the following AWS Durable Execution SDK versions or later:
+ JavaScript and TypeScript (`@aws/durable-execution-sdk-js`) – 2.5.0
+ Python (`aws-durable-execution-sdk-python`) – 2.1.0
+ Java (`aws-durable-execution-sdk-java`) – 2.3.0
+ Go (`github.com/aws/aws-durable-execution-sdk-go`) – 1.0.0
+ Rust (`aws-durable-execution-sdk`) – 1.0.0
+ C\# (.NET) (`Amazon.Lambda.DurableExecution`) – 2.2.0

## Pause an execution
<a name="durable-pause-resume-pause"></a>

To pause an execution, call [PauseDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_PauseDurableExecution.html) with the execution ARN. You can include a reason, which Lambda records in the execution history. In the following example, replace the execution ARN and reason with your own values:

```bash
aws lambda pause-durable-execution \
  --durable-execution-arn {{arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:my-function-version/durable-execution/my-execution-name/my-execution-id}} \
  --reason "{{Payment service outage}}"
```

This command uses the following options:
+ `--durable-execution-arn` – The ARN of the durable execution to pause.
+ `--reason` – (Optional) A description of why you're pausing the execution.

By default, the execution timeout also pauses. To keep it running, add `--no-execution-timeout-paused`. For more information, see [Execution timeout while paused](#durable-pause-resume-timeout).

To check the status, call [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html). While the execution is `PAUSING` or `PAUSED`, the response includes `PauseDetails`:

```json
{
    "Status": "PAUSED",
    "PauseDetails": {
        "PauseRequestTimestamp": "2026-06-14T10:20:00Z",
        "Reason": "Payment service outage",
        "ExecutionTimeoutPaused": true
    },
    ...
}
```

The response includes the reason only if you set `IncludeExecutionData` to `true`, which is the default.

## Resume an execution
<a name="durable-pause-resume-resume"></a>

To resume an execution, call [ResumeDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_ResumeDurableExecution.html). You can resume an execution that is `PAUSED` or `PAUSING`. In the following example, replace the execution ARN and reason with your own values:

```bash
aws lambda resume-durable-execution \
  --durable-execution-arn {{arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:my-function-version/durable-execution/my-execution-name/my-execution-id}} \
  --reason "{{Payment service recovered}}"
```

This command uses the following options:
+ `--durable-execution-arn` – The ARN of the durable execution to resume.
+ `--reason` – (Optional) A description of why you're resuming the execution.

After the status changes to `RUNNING`, what happens next depends on the state of the execution:
+ If the pause interrupted an invocation, or an operation completed while the execution was paused, Lambda invokes your function when the execution resumes.
+ If the execution is still waiting on its pending operations, Lambda invokes your function when they complete.

If you call [ResumeDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_ResumeDurableExecution.html) after pausing but before the status changes to `PAUSING` or `PAUSED`, Lambda returns a `ResourceConflictException`. Check the status with [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) and try again.

## Stop a paused execution
<a name="durable-pause-resume-stop"></a>

To end a `PAUSED` or `PAUSING` execution without resuming it, call [StopDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_StopDurableExecution.html). For more information, see [Stopping an execution](durable-managing-executions.md#durable-managing-executions-stop).

## Execution status during a pause
<a name="durable-pause-resume-how-it-works"></a>

When you pause an execution, the execution's new status depends on whether your function is running when Lambda processes the pause:
+ **Your function isn't running** – The execution is waiting, for example on a wait, a callback, a step retry delay, or a child execution. The status changes from `RUNNING` to `PAUSED`.
+ **Your function is running** – The status changes to `PAUSING`. Your code keeps running until it saves its next checkpoint, such as when a step completes. Lambda saves that checkpoint and ends the invocation, and the status changes to `PAUSED`.

The status doesn't change during the [PauseDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_PauseDurableExecution.html) call, so [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) can still report `RUNNING` after the call succeeds. To confirm the new status, call [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) again.

While the execution is `PAUSING`:
+ A step that was running when you paused the execution completes and saves its result.
+ If the invocation returns a result or an error before it reaches another checkpoint, the execution succeeds or fails as usual and isn't paused.
+ The execution can stay `PAUSING` for as long as the invocation takes to reach its next checkpoint, up to the function timeout.
+ Calling [PauseDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_PauseDurableExecution.html) again has no effect. The reason and options from the first pause request stay in effect.
+ Calling [ResumeDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_ResumeDurableExecution.html) cancels the pause, and the running invocation continues past its next checkpoint.

## What keeps running while an execution is paused
<a name="durable-pause-resume-while-paused"></a>

Pausing stops Lambda from invoking your function. It doesn't stop operations that are already pending:
+ Wait durations elapse.
+ External systems can complete callbacks and send heartbeats, and callbacks can time out.
+ Chained invocations and child executions continue to run. Pausing a parent execution doesn't pause its child executions.
+ Step retry delays elapse.

Lambda records these completions in the execution history. When you resume the execution, your function processes all of them in its next invocation.

A paused execution remains open. It counts against the quota for running durable executions, and you continue to pay for the execution data that Lambda stores. Because Lambda doesn't invoke your function, a paused execution incurs no invocation charges.

## Execution timeout while paused
<a name="durable-pause-resume-timeout"></a>

The `ExecutionTimeoutPaused` parameter of [PauseDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_PauseDurableExecution.html) controls whether the [execution timeout](durable-basic-concepts.md#durable-execution-timeout) keeps running while the execution is paused:
+ `true` (default) – The execution timeout stops when the status changes to `PAUSED`. When you resume the execution, Lambda extends the timeout by the time the execution spent paused. Even with the timeout paused, an execution times out 366 days after it started.
+ `false` – The execution timeout keeps running, and the execution can time out while paused.

In both cases, the execution timeout keeps running while the status is `PAUSING`, because your function code is still running.

To see when an execution will time out, call [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) and check `ExpectedExecutionTimeoutTimestamp`. If `ExecutionTimeoutPaused` is `true` (the default), the execution's deadline depends on when you resume it. While the execution is paused, `ExpectedExecutionTimeoutTimestamp` shows the latest possible time, 366 days after the execution started. When you resume the execution, the value changes to the original deadline plus the time that the execution spent paused, up to 366 days after the execution started. If `ExecutionTimeoutPaused` is `false`, the value doesn't change.

## Monitoring paused executions
<a name="durable-pause-resume-history"></a>

To find paused executions, call [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) with a status filter of `PAUSED` or `PAUSING`. The list is eventually consistent, so a status change can appear in [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) before it appears in the list.

Lambda records `ExecutionPaused` and `ExecutionResumed` events in the execution history. You can view them with [GetDurableExecutionHistory](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecutionHistory.html):

```json
{
    "EventType": "ExecutionPaused",
    "EventId": 12,
    "EventTimestamp": "2026-06-14T10:30:00Z",
    "ExecutionPausedDetails": {
        "PauseRequestTimestamp": "2026-06-14T10:20:00Z",
        "Reason": {
            "Payload": "Payment service outage",
            "Truncated": false
        },
        "ExecutionTimeoutPaused": true
    }
}
```

The `EventTimestamp` is when the execution paused or resumed, and `PauseRequestTimestamp` or `ResumeRequestTimestamp` is when you made the request.

To monitor pause and resume across your executions, use the [CloudWatch metrics](durable-monitoring.md#durable-monitoring-execution-metrics) and [EventBridge status change events](durable-monitoring.md#durable-eventbridge-status-changes) for durable executions.