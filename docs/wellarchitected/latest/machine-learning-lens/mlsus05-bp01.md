# MLSUS05-BP01 Align SLAs with sustainability goals

Define service level agreements (SLAs) that support your
sustainability goals while meeting your business requirements.
Define SLAs to meet your business requirements, not exceed them.
Make trade-offs that significantly reduce environmental impacts in
exchange for acceptable decreases in service levels.

**Desired outcome:** You establish
SLAs that balance business requirements with sustainability
objectives, optimizing resource utilization while maintaining
acceptable service levels. By implementing appropriate inference
methods based on latency tolerance, availability needs, and response
time requirements, you can reduce idle resources, minimize energy
consumption, and lower your machine learning workload's
environmental impact.

**Common anti-patterns:**

- Maintaining always-on inference endpoints for workloads with
  sporadic or batch processing needs.
- Setting unnecessarily stringent response time requirements when
  users can tolerate some latency.
- Configuring excessive redundancy beyond what's needed for
  business continuity.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs through optimized resource
  utilization.
- Lower carbon footprint from minimized idle computing resources.
- Alignment of technical operations with organizational
  sustainability goals.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When designing machine learning systems, your SLA choices directly
impact resource consumption and environmental sustainability. By
carefully analyzing your actual business requirements rather than
automatically opting for maximum performance, you can identify
opportunities to make sustainable trade-offs without compromising
essential functionality.

Consider your application's true latency requirements,
availability needs, and processing patterns. For example, if your
users can tolerate a response time of seconds rather than
milliseconds, asynchronous or batch processing approaches can
dramatically reduce resource usage compared to always-on real-time
endpoints. Similarly, if your application can gracefully handle
occasional unavailability during instance failures, you can avoid
overprovisioning redundant capacity.

The goal is to make conscious trade-offs that balance
sustainability with business needs, focusing on what's truly
required rather than defaulting to full time maximum performance.

### Implementation steps

1. **Queue incoming requests and process
   them asynchronously**. If your users can tolerate
   some latency, deploy your model on
   [serverless](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
   or
   [asynchronous
   endpoints](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md") to reduce resources that are idle between
   tasks and minimize the impact of load spikes. These options
   will automatically scale the instance or endpoint count to
   zero when there are no requests to process, so you only
   maintain an inference infrastructure when your endpoint is
   processing requests.
2. **Adjust availability**. If
   your users can tolerate some latency in the rare case of a
   failover, don't provision extra capacity. If an outage
   occurs or an instance fails, Amazon SageMaker AI
   [automatically
   attempts to distribute your instances across Availability
   Zones](../../../sagemaker/latest/dg/deployment-best-practices.md#deployment-best-practices-availability-zones "../../../sagemaker/latest/dg/deployment-best-practices.md#deployment-best-practices-availability-zones"). Adjusting availability is an example of a
   [conscious
   trade off](../sustainability-pillar/sustainability-as-a-non-functional-requirement.md "../sustainability-pillar/sustainability-as-a-non-functional-requirement.md") you can make to meet your sustainability
   targets.
3. **Adjust response time**.
   When you don't need real-time inference, use
   [SageMaker AI Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md"). Unlike a persistent endpoint,
   clusters are decommissioned when batch transform jobs finish
   so you don't continuously maintain an inference
   infrastructure.
4. **Conduct workload
   analysis**. Assess your machine learning workload's
   usage patterns and latency requirements to determine the
   most sustainable deployment option. Identify periods of peak
   activity versus low or no usage to determine if on-demand
   scaling is appropriate for your needs.
5. **Define sustainability
   metrics**. Establish key metrics to track your
   sustainability improvements, such as compute hours saved,
   idle time reduced, or overall carbon footprint reduction.
   Include these metrics alongside traditional performance
   indicators in your operational dashboards.
6. **Leverage enhanced serverless
   inference capabilities**. Use improved
   [SageMaker AI
   Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md") with increased memory
   configurations and better cold-start performance for
   variable workloads that don't require always-on
   infrastructure.
7. **Optimize large language model
   deployments with serverless deployment or batch
   processing**. For generative AI workloads using
   large language models (LLMs), consider serverless model
   inference through SageMaker AI or implement
   [Bedrock
   batch processing](../../../bedrock/latest/userguide/batch-inference.md "../../../bedrock/latest/userguide/batch-inference.md") for non-interactive generation tasks
   like content summarization or document analysis to reduce
   resource consumption.

## Resources

**Related documents:**

- [Asynchronous
  inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [Batch
  transform for inference with Amazon SageMaker AI](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Multi-model
  endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Best
  practices for deploying models on SageMaker AI Hosting
  Services](../../../sagemaker/latest/dg/deployment-best-practices.md "../../../sagemaker/latest/dg/deployment-best-practices.md")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Sustainability
  as a non-functional requirement](../sustainability-pillar/sustainability-as-a-non-functional-requirement.md "../sustainability-pillar/sustainability-as-a-non-functional-requirement.md")
- **Related services:**
- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
