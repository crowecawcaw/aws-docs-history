# Best practices for Lambda durable functions

Durable functions use a replay-based execution model that requires different programming practices than traditional Lambda functions. See [Best practices](../../../durable-execution/patterns/best-practices.md "../../../durable-execution/patterns/best-practices.md") in the AWS Durable Execution SDK Developer Guide for guidance on how to write and test durable workflow code.

The following recommendations are best practices for deploying, invoking, and monitoring Lambda durable functions.

## Function versions and aliases

Invoke functions with version numbers or aliases to pin executions to specific code versions. Ensure new code versions can handle state from older versions. Don't rename steps or change their behavior in ways that break replay.

## Monitoring

Enable structured logging with execution IDs and step names. Set up CloudWatch alarms for error rates and execution duration. Use tracing to identify bottlenecks. For detailed guidance, see [Monitoring and debugging](durable-monitoring.md "durable-monitoring.md").

## Related resources

- [AWS Durable Execution SDK Developer Guide](../../../durable-execution.md "../../../durable-execution.md")
- [Monitoring Lambda durable functions](durable-monitoring.md "durable-monitoring.md")
- [Retries for Lambda durable functions](durable-execution-sdk-retries.md "durable-execution-sdk-retries.md")
- [Testing Lambda durable functions](durable-testing.md "durable-testing.md")
