# GENREL01-BP01 Scale and balance foundation model throughput as a

function of utilization

Collect information on the generative AI workload's utilization. Use this information to
determine the required throughput for your foundation model.

**Desired outcome:** When implemented, this best practice improves
the reliability of your generative AI workload by matching the configured or provisioned
throughput to your foundation models to the workload's demand.

**Benefits of establishing this best practice:**
[Stop guessing
capacity](../framework/rel-dp.md "../framework/rel-dp.md") - By understanding the throughput needs of your generative AI workload, you
remove the need to guess at throughput capacity.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Foundation models have throughput quotas. Inference requests require significant
computation and memory to serve, and latency may increase during periods of high inference
demand, especially when model endpoints serve inference from multiple requests simultaneously.

For model endpoints hosted on Amazon Bedrock, consider provisioned throughput endpoints or
cross-region inference profiles. Provisioned throughput provides dedicated infrastructure that
can achieve higher, more stable throughput than allowed through default quotas for on demand
models hosted on Amazon Bedrock. Provisioned throughput capacity can be monitored in Amazon CloudWatch, which helps you proactively scale when capacity nears critical thresholds.
Cross-region inference profiles distribute inference demand over a region of availability. For
model endpoints hosted on Amazon SageMaker AI Inference Endpoints, consider leveraging traditional
throughput scaling techniques like EC2 Auto-Scaling groups behind a load balancer. If your
increased throughput needs are periodic and predictable, consider deploying larger instance
types in advance of the increased need. Ultimately, it is encouraged to proactively engage
with AWS support to increase service quotas based on known workload demands.

Queuing is a powerful technique for consuming requests. Consider placing queues between
generative AI applications and models so that models do not deny or drop requests due to
throughput constraints. This architecture lends itself to event-driven messaging patterns,
making it a particularly robust option for architectures with high demand.

### Implementation steps

1. Determine the foundation model that handles inference requests for your generative
   AI workload.
2. Perform load testing on the workload to get a baseline of performance, identifying
   if an upper-limit on throughput is feasible for this application.
3. Determine if cross-region inference profiles (if available for this model)
   increases the throughput.
4. Consider purchasing provisioned throughput if necessary.

## Resources

**Related best practices:**

- [REL01-BP01](../reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.md "../reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.md")
- [REL01-BP02](../reliability-pillar/rel_manage_service_limits_limits_considered.md "../reliability-pillar/rel_manage_service_limits_limits_considered.md")
- [REL01-BP03](../reliability-pillar/rel_manage_service_limits_aware_fixed_limits.md "../reliability-pillar/rel_manage_service_limits_aware_fixed_limits.md")

**Related documents:**

- [Increase throughput with cross-Region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md")
- [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](../../../bedrock/latest/userguide/prov-throughput.md "../../../bedrock/latest/userguide/prov-throughput.md")

**Related examples:**

- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/")
