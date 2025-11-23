# MLCOST06-BP03 Monitor endpoint usage and right-size the

instance fleet

Use efficient compute resources to run models in production. Monitor
your endpoint usage and right-size the instance fleet. Use automatic
scaling (auto scaling) for your hosted models. _Auto
scaling_ dynamically adjusts the number of instances
provisioned for a model in response to changes in your workload.

**Desired outcome:** You have
optimized SageMaker AI endpoints that automatically adjust to workload
demands while maintaining performance and minimizing costs. Your
model deployment uses appropriately sized instances that are neither
over-provisioned nor under-provisioned, and you have continuous
monitoring in place to inform scaling decisions.

**Common anti-patterns:**

- Provisioning static endpoint configurations that remain
  unchanged regardless of workload fluctuations.
- Over-provisioning instances "just to be safe"
  without analyzing actual resource utilization.
- Ignoring endpoint metrics and failing to adjust resource
  allocation based on usage patterns.
- Deploying resources across different Availability Zones without
  consideration for data transfer costs.
- Using default instance types without evaluating performance
  requirements.

**Benefits of establishing this best
practice:**

- Reduced compute costs by reducing over-provisioned resources.
- Improved performance during peak usage periods through automatic
  scaling.
- Higher resource utilization through right-sizing.
- Increased availability by distributing instances across
  Availability Zones.
- Better understanding of model usage patterns to inform future
  optimizations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitoring and optimizing your SageMaker AI endpoints is essential
for maintaining cost-efficiency while providing high availability
and performance. By implementing CloudWatch monitoring and auto
scaling, your deployments use only the resources they needs when
they need them. Start by establishing baseline metrics for your
endpoints to understand typical usage patterns and resource
requirements. Then implement auto scaling policies based on these
metrics to automatically adjust capacity in response to changing
workloads.

For production environments, distribute your endpoint deployment
across multiple Availability Zones to maintain high availability.
Consider the placement of related resources, such as data storage
solutions like FSx for Lustre, to minimize cross-AZ data transfer
costs and optimize performance. Regular review of your metrics and
scaling configurations assists you to continuously refine your
deployment for optimal cost and performance.

### Implementation steps

1. **Monitor Amazon SageMaker AI endpoints
   with Amazon CloudWatch**. You can monitor Amazon SageMaker AI using
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), which collects raw data and processes it
   into readable, near real-time metrics. Use metrics such as
   CPUUtilization, GPUUtilization, MemoryUtilization, and
   DiskUtilization to view your endpoint's resource utilization
   and make informed decisions about right-sizing your endpoint
   instances. Set up CloudWatch dashboards to visualize these
   metrics over time and identify patterns in resource usage.
2. **Implement CloudWatch alarms for
   proactive monitoring**. Configure alarms for key
   metrics that can indicate when an endpoint is
   under-provisioned or over-provisioned. For example, set up
   alarms that go off when CPU utilization consistently exceeds
   80% (indicating potential under-provisioning) or remains
   below 20% (indicating over-provisioning). These alarms can
   notify your team to take action or run automated responses
   through AWS Lambda functions.
3. **Configure auto scaling for SageMaker AI
   endpoints**.
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") supports auto scaling that monitors your
   workloads and dynamically adjusts capacity to maintain
   steady performance at the lowest possible cost. When
   workload increases, auto scaling brings more instances
   online. When workload decreases, auto scaling removes
   unnecessary instances, which can reduce compute costs.
   Define appropriate scaling policies based on your
   application's requirements, including minimum and maximum
   instance counts, target metrics, and scale-in and scale-out
   cooldown periods.
4. **Distribute instances across
   Availability Zones**. SageMaker AI automatically
   attempts to distribute your instances across Availability
   Zones, so deploy multiple instances for each production
   endpoint to provide high availability. If you're using a
   VPC, configure at least two subnets in different
   Availability Zones to allow SageMaker AI to distribute your
   instances across those zones, providing resilience against
   zone failures.
5. **Optimize resource placement for data
   access**. When using
   [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/ "https://aws.amazon.com/fsx/lustre/") as an input data source for SageMaker AI,
   deploy FSx for Lustre and SageMaker AI in the same Availability
   Zone to avoid cross-AZ data transfer costs. This
   configuration removes the initial Amazon S3 download step,
   accelerating ML training jobs while minimizing costs.
   Consider similar placement strategies for other related
   resources to optimize performance and cost.
6. **Regularly review and adjust instance
   types**. Periodically evaluate whether your
   selected instance types are appropriate for your workload.
   SageMaker AI offers a variety of
   [instance
   types](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") optimized for different workload
   characteristics. Analyze your CloudWatch metrics to
   determine if you could achieve better price-performance by
   switching to a different instance family, such as
   compute-optimized, memory-optimized, or GPU instances.
7. **Use inference optimization
   techniques**. Implement model optimization
   techniques such as
   [Amazon SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md") to automatically optimize models for
   your target hardware, improving performance and potentially
   allowing you to use smaller instance types. Consider
   techniques like model compression, quantization, and
   batching to improve inference efficiency and throughput.
8. **Use enhanced SageMaker AI Inference
   Recommender**. Use
   [SageMaker AI
   Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") with enhanced algorithms and
   support for multi-model endpoints to get sophisticated
   instance selection and cost optimization recommendations.
9. **Implement specialized instance types
   for generative AI models**. For large language
   models and other generative AI workloads, use specialized
   instances like
   [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/") or
   [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/"), which are designed specifically for machine
   learning inference and training. These instances can provide
   significant cost savings compared to general-purpose GPU
   instances when running transformer-based models. Consider
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") for fully managed generative AI capabilities
   with built-in scaling.

## Resources

**Related documents:**

- [Amazon SageMaker AI metrics in Amazon CloudWatch](../../../sagemaker/latest/dg/monitoring-cloudwatch.md "../../../sagemaker/latest/dg/monitoring-cloudwatch.md")
- [Automatic
  scaling of Amazon SageMaker AI models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/")
- [Best
  practices for deploying models on SageMaker AI Hosting
  Services](../../../sagemaker/latest/dg/deployment-best-practices.md "../../../sagemaker/latest/dg/deployment-best-practices.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
