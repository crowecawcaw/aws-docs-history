# MLREL05-BP01 Allow automatic scaling of the model

endpoint

Implement capabilities that allow the automatic scaling of model
endpoints. This improves the reliable processing of predictions to
meet changing workload demands. Include monitoring on endpoints to
identify a threshold that initiates the addition or removal of
resources to support current demand.

**Desired outcome:** You can
efficiently handle varying workload demands by implementing
automatic scaling for your model endpoints. Your endpoints
dynamically adjust resources based on real-time needs, providing
consistent performance and availability without manual intervention.
This results in reliable prediction processing, optimal resource
utilization, and cost-effective operations.

**Common anti-patterns:**

- Manually scaling endpoints in response to traffic changes.
- Over-provisioning resources to handle peak loads at non-peak
  times.
- Neglecting to set up monitoring for endpoint performance.
- Ignoring traffic patterns when configuring scaling policies.
- Using fixed infrastructure that can't adapt to changing
  workloads.

**Benefits of establishing this best
practice:**

- Improves reliability and availability of prediction services.
- Optimizes costs through dynamic resource allocation.
- Enhances user experience with consistent response times.
- Reduces operational overhead through automation.
- Strengthens ability to handle unexpected traffic spikes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Automatic scaling of model endpoints is critical for maintaining
reliable machine learning services in production. By implementing
auto scaling, your endpoints can handle varying loads efficiently
without manual intervention. This capability is especially
important for applications with fluctuating traffic patterns or
those that experience periodic spikes in demand.

When setting up automatic scaling, you need to consider
appropriate metrics that trigger scaling actions, such as CPU
utilization, memory usage, or request latency. Define appropriate
thresholds for these metrics so that your system scale at the
right time - not too early (which wastes resources) or too late
(which impacts performance).

Monitoring is an essential component of an auto scaling solution.
By implementing comprehensive monitoring, you gain visibility into
endpoint performance and scaling operations, allowing you to
optimize your configuration over time based on real usage
patterns.

### Implementation steps

1. **Configure automatic scaling for
   Amazon SageMaker AI endpoints**. Amazon SageMaker AI
   supports
   [automatic
   scaling (auto scaling)](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md") for your hosted models.
   SageMaker AI endpoints can be configured with auto scaling to
   maintain service availability as traffic increases.
   Automatic scaling automatically provisions new resources
   horizontally to handle increased user demand or system load.
2. **Set up appropriate scaling
   policies**. Define target metrics for scaling such
   as CPU utilization, memory usage, or request count.
   Configure appropriate minimum and maximum instance counts
   based on your expected traffic patterns and performance
   requirements. Consider implementing both scale-out policies
   (adding capacity when load increases) and scale-in policies
   (removing capacity when load decreases) to optimize resource
   utilization.
3. **Implement comprehensive
   monitoring**. Use
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to monitor the performance of your
   endpoint and collect metrics that can inform scaling
   decisions. Create dashboards to visualize endpoint
   performance and scaling activities. Set up alerts to notify
   you of issues or anomalies with your endpoints.
4. **Leverage SageMaker AI Serverless
   Inference**. For workloads with intermittent or
   unpredictable traffic patterns, consider using
   [Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md"), which automatically
   scales compute capacity up and down based on traffic,
   avoiding the need to choose instance types or manage scaling
   policies.
5. **Utilize SageMaker AI Inference
   Recommender**. Before deploying models to
   production, use
   [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") to get
   recommendations on instance types and configurations that
   will best meet your performance and cost requirements,
   assisting you in optimizing your scaling policies.
6. **Implement load testing**.
   Perform load testing on your endpoints to understand how
   they behave under different traffic conditions. This
   information can fine-tune your scaling policies so that
   they're effective when real traffic increases occur.

## Resources

**Related documents:**

- [Automatic
  scaling of Amazon SageMaker AI models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Configuring
  autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/")
