# MSFTPERF01-BP03 Run serverless Microsoft applications on AWS Lambda

Use cases such as event-driven, like message processing and API
routes, application-based function, like packaging and entire
cross-platform ASP.NET runtime, file processing, mobile backend,
cloud automation, and similar are usually suitable for running on
AWS Lambda.

**Desired outcome:** Achieve optimal
performance efficiency and cost optimization for suitable Microsoft
workloads by leveraging AWS Lambda's serverless architecture,
eliminating infrastructure management overhead while providing
automatic scaling, high availability, and pay-per-execution pricing
for event-driven and function-based applications.

**Common anti-patterns:**

- Running long-running or stateful Microsoft applications on
  Lambda without considering execution time limits and stateless
  requirements, leading to performance issues or architectural
  mismatches.
- Implementing serverless solutions for workloads that require
  persistent connections or complex state management, missing the
  benefits of serverless while introducing unnecessary complexity.
- Choosing Lambda without evaluating cold start impacts on
  performance-sensitive applications, potentially affecting user
  experience for latency-critical workloads.

**Benefits of establishing this best
practice:**

- Eliminated infrastructure management overhead through fully
  managed serverless execution environment that automatically
  handles scaling, patching, and availability.
- Optimized cost efficiency through pay-per-execution pricing
  model that eliminates costs for idle resources and automatically
  scales to zero when not in use.
- Enhanced performance for event-driven workloads through
  automatic scaling and optimized execution environment designed
  for short-lived, stateless functions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing serverless Microsoft applications on AWS Lambda
requires careful evaluation of application architecture and
suitability for serverless patterns. Focus on event-driven,
stateless workloads and optimize for Lambda's execution model to
achieve maximum performance efficiency.

### Implementation steps

1. Identify Microsoft workload components suitable for
   serverless architecture including event-driven functions,
   API endpoints, and batch processing tasks.
2. Refactor applications to follow serverless patterns with
   stateless, event-driven design principles.
3. Configure Lambda functions with appropriate runtime, memory
   allocation, and timeout settings for optimal performance.
4. Implement efficient cold start optimization techniques
   including provisioned concurrency for latency-sensitive
   functions.
5. Set up event sources and triggers using services like API Gateway, S3, SQS, or EventBridge.
6. Configure monitoring and observability using CloudWatch,
   X-Ray, and Lambda Insights for performance tracking.

## Resources

**Related documents:**

- [Building
  .NET applications on AWS Lambda](../../../lambda/latest/dg/lambda-csharp.md "../../../lambda/latest/dg/lambda-csharp.md")

**Related tools:**

- [AWS Lambda](../../../lambda.md "../../../lambda.md")
- [AWS .NET Development Blog](https://aws.amazon.com/blogs/compute/category/devops/aws-net-development/ "https://aws.amazon.com/blogs/compute/category/devops/aws-net-development/")
