# GENOPS02-BP03 Implement solutions to

mitigate the risk of system overload

There are two primary ways to mitigate the risk of system
overload for generative AI workloads. The first is to scale the
inference serving architecture using advanced auto-scaling
technologies. This is possible using Amazon SageMaker AI
Inference Components, which you can use to host and scale model
independent of the underlying infrastructure. For self-hosted
language models, this is the ideal approach.

The second approach is to rate limit and throttle managed
inference to maintain application stability and performance.
This approach is more applicable to managed inference on Amazon
Bedrock. This practice controls request processing rates to
avoid system overload, which provides consistent application
health and a better user experience. You can increase system
throughput by opting for cross-Region inference or in some cases
by purchasing provisioned model thoughput.

By adopting these measures, you can achieve balanced workload
distribution, reduce service disruption risks, and enhance
application reliability. This approach safeguards against
excessive demand, optimizes resource utilization, and improves
cost efficiency and performance.

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
is not established:** High

## Implementation guidance

For self-hosted models, adopt SageMaker AI Inference
Components. Inference Components are an extension of
multimodel endpoints, and are meant for hosting and scaling
large-language models dynamically. Inference components treat
models as primary elements, scaling the underlying hardware as
needed based on the availability of CPU and GPU resources, as
well as the full inference load on the provisioned
infrastructure. Inference components are meant for workloads
where you have control over the underlying infrastructure, and
therefore should not be considered for generative AI workloads
hosted on managed infrastructure such as Amazon Q for Business
or Amazon Bedrock.

Implementing rate limiting and throttling is crucial for the
stability of generative AI applications. This practice
controls incoming request rates to reduce the risk of system
overload, helping to provide consistent performance and
availability. It helps protect against traffic spikes, can act
as one of the mitigations to denial-of-service attacks, and
promotes fair usage. Benefits include reliable performance,
enhanced security, optimized resource utilization, and
improved user experience, which align with key principles of
reliability, performance efficiency, security, and cost
optimization.

When designing generative AI systems, consider the limitations
of source systems, and implement appropriate measures. The
level of parallelism achievable may be constrained by the
source system's capacity, necessitating the implementation of
throttling mechanisms and backoff techniques. Amazon Bedrock,
like other AWS services, has default quotas (formerly known as
limits) that apply to your account. These quotas are in place
to help maintain steady service performance and appropriate
usage. Given the potential for occasional disruptions and
errors in source systems, robust error handling and retry
logic should be incorporated into the application
architecture. These measures improve success rates, resiliency
in your application, and user experience.

In SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, establish comprehensive request rate controls
and resource throttling mechanisms that help protect your
cluster from overload conditions while maintaining optimal
training performance.

For EKS-based HyperPod, implement rate limiting through
managed Kubernetes orchestration with resource quotas and
limit ranges to control resource consumption at namespace and
pod levels, avoiding system overload during peak demand.
Configure HyperPod Task Governance with intelligent throttling
mechanisms that automatically manage task queues and resource
allocation rates, verifying that production workloads receive
priority processing while development tasks are throttled
appropriately to avoid cluster saturation.

Use horizontal pod autoscaling with conservative scaling
policies and priority classes to implement request throttling
based on workload criticality, while using node selectors to
distribute load across different instance types and reduce
hotspots. The usage reporting feature provides real-time
visibility into resource consumption patterns, enabling
proactive rate limiting adjustments based on GPU, CPU, and
Neuron Core utilization metrics to maintain optimal cluster
performance under varying load conditions.

For Slurm-based HyperPod, use Slurm's native job submission
throttling and fair share scheduling to avoid system overload
by controlling the rate at which jobs are admitted to the
cluster based on available resources and current system load.
Implement quality of service (QoS) policies and job priority
classes that automatically throttle lower-priority workloads
when system resources approach capacity limits, while
maintaining consistent processing rates for critical training
jobs.

Configure resource allocation policies that dynamically adjust
job submission rates based on cluster health metrics, combined
with HyperPod's auto-resume functionality to handle temporary
overload conditions gracefully without cascading failures.

Both systems benefit from implementing circuit breaker
patterns through SageMaker AI HyperPod Recipes that provide
pre-configured throttling mechanisms and rate limiting
strategies optimized for specific model architectures like
Llama and Mistral, providing sustained performance while
reducing resource exhaustion and system instability during
high-demand periods.

The embedding model has important performance considerations
in your application, regardless of whether it's deployed
locally within the pipeline or accessed as an external
service. Embedding models, as foundational models that operate
on GPUs, have finite processing capacity. For locally-run
models, workload distribution must be carefully managed based
on available GPU capacity. When using external models, avoid
overloading the service with excessive requests. In both
scenarios, the level of parallelism is determined by the
embedding model's capabilities not by the compute resources of
the batch processing system. This highlights the importance of
efficient resource allocation and optimization strategies.

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

**Related best practices:**

- [OPS10-BP02](../framework/ops_event_response_process_per_alert.md "../framework/ops_event_response_process_per_alert.md")
- [OPS08-BP04](../framework/ops_workload_observability_create_alerts.md "../framework/ops_workload_observability_create_alerts.md")

**Related documents:**

- [Quotas
  for Amazon Bedrock - Amazon Bedrock](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md")
- [Amazon
  SDK Developer Guide - Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md")
- [AWS Prescriptive Guidance - Retry behavior](../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md "../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md")

**Related examples:**

- [Supercharge
  your auto scaling for generative AI inference – Introducing
  Container Caching in SageMaker AI Inference](https://aws.amazon.com/blogs/machine-learning/supercharge-your-auto-scaling-for-generative-ai-inference-introducing-container-caching-in-sagemaker-inference/ "https://aws.amazon.com/blogs/machine-learning/supercharge-your-auto-scaling-for-generative-ai-inference-introducing-container-caching-in-sagemaker-inference/")
- [Implementing
  Rate Limiting with API Gateway](../../../apigateway/latest/developerguide/api-gateway-request-throttling.md "../../../apigateway/latest/developerguide/api-gateway-request-throttling.md")
- [Using
  Step Functions for Retry Logic](../../../step-functions/latest/dg/tutorial-handling-error-conditions.md "../../../step-functions/latest/dg/tutorial-handling-error-conditions.md")
- [Managing
  and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/ "https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/")
- [Analyze
  Amazon SageMaker AI spend and determine cost optimization
  opportunities based on usage, Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/ "https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/")
- [Maximize
  Accelerator Utilization for Model Development with New Amazon SageMaker AI HyperPod Task Governance](https://aws.amazon.com/blogs/aws/maximize-accelerator-utilization-for-model-development-with-new-amazon-sagemaker-hyperpod-task-governance/ "https://aws.amazon.com/blogs/aws/maximize-accelerator-utilization-for-model-development-with-new-amazon-sagemaker-hyperpod-task-governance/")
- [Introducing
  Amazon SageMaker AI HyperPod to train foundation models at
  scale](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-to-train-foundation-models-at-scale/ "https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-to-train-foundation-models-at-scale/")
- [Best
  practices for Amazon SageMaker AI HyperPod task governance](https://aws.amazon.com/blogs/machine-learning/best-practices-for-amazon-sagemaker-hyperpod-task-governance/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-amazon-sagemaker-hyperpod-task-governance/")
- [Get
  started with Amazon SageMaker AI HyperPod task governance](https://www.youtube.com/watch?v=_wDhBAPwhoM "https://www.youtube.com/watch?v=_wDhBAPwhoM")
- [Usage
  reporting for cost attribution in SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.md")

**Related tools:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [AWS SDK for Javascript](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
