# Logging and monitoring Amazon EventBridge Pipes using Amazon CloudWatch Logs

You can log EventBridge Pipes invocations using CloudTrail and monitor the health of your pipes using CloudWatch metrics.

## CloudWatch metrics

EventBridge Pipes sends metrics to Amazon CloudWatch every minute for everything from a pipe executions being throttled to a target successfully being invoked.

| Metric                       | Description                                                                                                                               | Dimensions             | Units        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `Concurrency`                | The number of concurrent executions of a pipe.                                                                                            | AwsAccountId           | None         |
| `Duration`                   | Length of time the pipe execution took.                                                                                                   | PipeName               | Milliseconds |
| `EventCount`                 | The number of events a pipe has processed.                                                                                                | PipeName               | None         |
| `EventSize`                  | The size of the payload of the event that invoked the pipe.                                                                               | PipeName               | Bytes        |
| `ExecutionThrottled`         | How many executions of a pipe were throttled. NoteThis value will be `0` if no executions were throttled.                                 | AwsAccountId, PipeName | None         |
| `ExecutionTimeout`           | How many executions of a pipe timed out before completing execution. NoteThis value will be `0` if no executions timed out.               | PipeName               | None         |
| `ExecutionFailed`            | How many executions of a pipe failed. NoteThis value will be `0` if no executions failed.                                                 | PipeName               | None         |
| `ExecutionPartiallyFailed`   | How many executions of a pipe partially failed. NoteThis value will be `0` if no executions partially failed.                             | PipeName               | None         |
| `EnrichmentStageDuration`    | How long the enrichment stage took to complete.                                                                                           | PipeName               | Milliseconds |
| `EnrichmentStageFailed`      | How many executions of a pipe's enrichment stage failed. NoteThis value will be `0` if no executions failed.                              | PipeName               | None         |
| `Invocations`                | Total number of invocations.                                                                                                              | AwsAccountId, PipeName | None         |
| `TargetStageDuration`        | How long the target stage took to complete.                                                                                               | PipeName               | Milliseconds |
| `TargetStageFailed`          | How many executions of a pipe's target stage failed. NoteThis value will be `0` if no executions failed.                                  | PipeName               | None         |
| `TargetStagePartiallyFailed` | How many executions of a pipe's target stage partially failed. NoteThis value will be `0` if no target stage executions partially failed. | PipeName               | None         |
| `TargetStageSkipped`         | How many executions of a pipe's target stage were skipped (for example, due to the enrichment returning an empty payload).                | PipeName               | Count        | ## Dimensions for CloudWatch metrics CloudWatch metrics have _dimensions_, or sortable attributes, which are listed below. |
| Dimension                    | Description                                                                                                                               |                        | ---          | ---                                                                                                                        |
| `AwsAccountId`               | Filters the available metrics by account ID.                                                                                              |                        | `PipeName`   | Filters the available metrics by pipe name.                                                                                |
