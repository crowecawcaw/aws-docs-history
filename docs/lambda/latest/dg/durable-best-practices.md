# Best practices for Lambda durable functions

Durable functions use a replay-based execution model that requires different programming practices than traditional Lambda functions. See [Best practices](../../../durable-execution/patterns/best-practices.md "../../../durable-execution/patterns/best-practices.md") in the AWS Durable Execution SDK Developer Guide for guidance on how to write and test durable workflow code.

The following recommendations are best practices for deploying, invoking, and monitoring Lambda durable functions.

## Function versions and aliases

Invoke functions with version numbers or aliases to pin executions to specific code versions. Ensure new code versions can handle state from older versions. Don't rename steps or change their behavior in ways that break replay. If you rename a step or alter its behavior while executions are in progress, those executions can fail to resume or produce incorrect results. This happens because the runtime can no longer match saved state to the expected step definition.

## Monitoring

Enable structured logging with execution IDs and step names. Set up CloudWatch alarms for error rates and execution duration. Use tracing to identify bottlenecks. For detailed guidance, see [Monitoring and debugging](durable-monitoring.md "durable-monitoring.md").

## Error handling

In addition to configuring retry strategies for transient failures, configure a dead-letter queue (DLQ) on your durable function to capture events from permanently failed executions. When a durable execution reaches a terminal state (FAILED, STOPPED, or TIMED\_OUT) after an asynchronous invocation, Lambda sends the original triggering event to the DLQ. This way, you can inspect, debug, and optionally reprocess failed events without losing them.

To configure a DLQ, set the `DeadLetterConfig` property on your function to an Amazon SQS queue or Amazon SNS topic ARN. For more information, see [Dead-letter queues](invocation-async-retain-records.md#invocation-dlq "invocation-async-retain-records.md#invocation-dlq").

Follow these best practices for error handling with durable functions:

- **Configure a DLQ for async invocations** – Always attach a dead-letter queue when invoking durable functions asynchronously. Unlike standard Lambda functions, the service does not automatically retry durable executions on failure. A properly configured DLQ captures events that led to permanently failed executions. Make sure the DLQ has the correct permissions and sufficient capacity to receive messages.
- **Use retry strategies within steps** – Configure explicit retry strategies with appropriate backoff for transient failures. For guidance on configuring retries, see [Retries for durable functions](durable-execution-sdk-retries.md "durable-execution-sdk-retries.md").
- **Combine DLQs with EventBridge notifications** – Use EventBridge rules to alert on FAILED, STOPPED, and TIMED\_OUT status changes for real-time visibility, and use a DLQ to preserve the original event payload for later analysis or reprocessing.
- **Monitor DLQ depth** – Create a CloudWatch alarm on the `ApproximateNumberOfMessagesVisible` metric for your DLQ to detect when failures are accumulating.

## Related resources

- [AWS Durable Execution SDK Developer Guide](../../../durable-execution.md "../../../durable-execution.md")
- [Monitoring Lambda durable functions](durable-monitoring.md "durable-monitoring.md")
- [Retries for Lambda durable functions](durable-execution-sdk-retries.md "durable-execution-sdk-retries.md")
- [Testing Lambda durable functions](durable-testing.md "durable-testing.md")
