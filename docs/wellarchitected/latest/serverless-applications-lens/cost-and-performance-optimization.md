# Lambda cost and performance

optimization

With Lambda, there are no servers to manage, it scales automatically, and you only pay
for what you use. However, choosing the right memory size settings for a Lambda function is
still an important task. [AWS Compute Optimizer](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md") supports Lambda functions and
uses machine-learning to provide memory size recommendations for Lambda functions.

This allows you to reduce costs and increase performance for your Lambda-based
serverless workloads.

These recommendations are available through the Compute Optimizer console, [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), [AWS SDK](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"), and the Lambda
console. Compute Optimizer continuously monitors Lambda functions, using historical performance metrics to
improve recommendations over time.

In addition, consider configuring new and existing functions to run on ARM or Graviton
processors. If your functions or dependencies do not require a given processor architecture
(x86, ARM), you might benefit in cost and performance by switching your functions
architecture. We always recommend load testing as results might vary for each use case,
dependency, and runtime. For example, you could create two [versions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") of your function: one
for x86 and one for ARM. With the [Alias](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md") feature, you could
distribute a percentage of your traffic to a different processor architecture, and use CloudWatch
Metrics to measure duration and latency efficiency.
