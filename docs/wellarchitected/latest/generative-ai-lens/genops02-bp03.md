# GENOPS02-BP03 Implement rate limiting and throttling to

mitigate the risk of system overload

Implement rate limiting and throttling for AI application stability
and performance. These practices control request processing rates to
prevent system overload, which provides consistent application
health and a better user experience. By adopting these measures, you
can achieve balanced workload distribution, reduce service
disruption risks, and enhance application reliability. This approach
safeguards against excessive demand, optimizes resource utilization,
and improves cost efficiency and performance.

**Desired outcome:** After
implementing rate limiting and throttling, your organization can
maintain the stability and performance of their AI applications.

**Benefits of establishing this best
practice:**

- [Safely
  automate where possible](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Respond to system load events.
- [Anticipate
  failure](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Maximize operational success by implementing
  responses to failure scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing rate limiting and throttling is crucial for the
stability of generative AI applications. This practice controls
incoming request rates to reduce the risk of system overload,
helping to provide consistent performance and availability. It
protects against traffic spikes, can act as one of the mitigations
to denial-of-service attacks, and promotes fair usage. Benefits
include reliable performance, enhanced security, optimized
resource utilization, and improved user experience, which align
with key principles of reliability, performance efficiency,
security, and cost optimization.

When designing generative AI systems, consider the limitations of
source systems, and implement appropriate measures. The level of
parallelism achievable may be constrained by the source system's
capacity, necessitating the implementation of throttling
mechanisms and backoff techniques. Amazon Bedrock, like other AWS
services, has default quotas (formerly known as limits) that apply
to your account. These quotas are in place to help maintain steady
service performance and appropriate usage. Given the potential for
occasional disruptions and errors in source systems, robust error
handling and retry logic should be incorporated into the
application architecture. These measures improve success rates,
resiliency in your application, and user experience.

The embedding model has important performance considerations in
your application, regardless of whether it's deployed locally
within the pipeline or accessed as an external service. Embedding
models, as foundational models that operate on GPUs, have finite
processing capacity. For locally-run models, workload distribution
must be carefully managed based on available GPU capacity. When
using external models, avoid overloading the service with
excessive requests. In both scenarios, the level of parallelism is
determined by the embedding model's capabilities not by the
compute resources of the batch processing system. This highlights
the importance of efficient resource allocation and optimization
strategies.

### Implementation steps

1. Understand your Amazon Bedrock quotas.
   - Quotas may apply to various aspects of Amazon Bedrock
     usage, such as API request rates, token usage, or
     concurrent model invocations
   - You can view the current quotas for Amazon Bedrock
     through the Service Quotas dashboard in the AWS Management Console
   - Default quotas may be updated based on factors such as
     regional availability and usage patterns
   - Some quotas may be specific to particular models or
     model families within Amazon Bedrock
   - Some quotas may be adjustable, allowing you to request
     an increase through the Service Quotas console
   - For quotas that cannot be adjusted through Service Quotas, contact Support for guidance

2. Implement throttling mechanisms.
   - Use Amazon API Gateway for rate limiting to control the
     number of requests

3. Implement backoff techniques.
   - Use exponential backoff with jitter to handle transient
     errors effectively
   - Integrate with AWS SDK for Javascript's built-in retry
     mechanisms for seamless error recovery

4. Design retry logic.
   - Implement idempotent operations where possible to
     facilitate safe retries
   - Use AWS Step Functions for managing complex retry
     workflows
   - Consider circuit breaker patterns for failing fast in
     case of repeated failures

5. Implement continuous monitoring and optimization.
   - Use Amazon CloudWatch observability to monitor system
     performance
   - Conduct regular load testing and capacity planning

## Resources

**Related practices:**

- [OPS10-BP02](../framework/ops_event_response_process_per_alert.md "../framework/ops_event_response_process_per_alert.md")
- [OPS08-BP04](../framework/ops_workload_observability_create_alerts.md "../framework/ops_workload_observability_create_alerts.md")

**Related guides, videos, and documentation:**

- [Quotas
  for Amazon Bedrock - Amazon Bedrock](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md")
- [Amazon
  SDK Developer Guide - Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md")
- [AWS Prescriptive Guidance - Retry behavior](../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md "../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md")

**Related examples:**

- [Implementing
  Rate Limiting with API Gateway](../../../apigateway/latest/developerguide/api-gateway-request-throttling.md "../../../apigateway/latest/developerguide/api-gateway-request-throttling.md")
- [Using
  Step Functions for Retry Logic](../../../step-functions/latest/dg/tutorial-handling-error-conditions.md "../../../step-functions/latest/dg/tutorial-handling-error-conditions.md")
- [Managing
  and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/ "https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/")

**Related tools:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [AWS SDK for Javascript](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
