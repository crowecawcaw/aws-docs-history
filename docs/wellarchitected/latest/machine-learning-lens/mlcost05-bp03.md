# MLCOST05-BP03 Right-size the model hosting instance

fleet

Use efficient compute resources to run models in production. In many
cases, up to 90% of the infrastructure spend for developing and
running an ML application is on inference, making it critical to use
high-performance, cost-effective ML inference infrastructure.
Selecting the right way to host and the right type of instance can
have a large impact on the total cost of ML projects. Use automatic
scaling for your hosted models. Auto scaling dynamically adjusts the
number of instances provisioned for a model in response to changes
in your workload.

**Desired outcome:** You optimize
your ML infrastructure costs while maintaining performance by using
the right instance types and quantities for your model deployments.
You use automated tools to recommend the most cost-effective
configurations and implement dynamic scaling that adjusts capacity
based on actual demand patterns, resulting in significant cost
savings and consistent performance.

**Common anti-patterns:**

- Using the same instance types for each model regardless of their
  specific requirements.
- Maintaining static instance counts rather than scaling with
  workload demands.
- Selecting instance types based solely on performance without
  considering cost implications.
- Not distributing model instances across multiple availability
  zones for resilience.

**Benefits of establishing this best
practice:**

- Reduced ML infrastructure costs by up to 90% through optimal
  instance selection.
- Improved model performance through use of appropriately sized
  resources.
- Enhanced reliability through automatic scaling and multi-AZ
  deployment.
- Better handling of variable workloads without performance
  degradation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Optimizing ML inference costs requires a careful balance between
performance and cost. When selecting compute resources for model
hosting, consider both the model's specific requirements and the
expected workload patterns. CPU instances may be sufficient for
many traditional ML models, while GPU instances deliver better
performance for deep learning models but at a higher cost. The key
is using the right resource for the specific workload.

Amazon SageMaker AI provides tools that can automatically select
the optimal instance type and size for your models. By testing
different configurations, you can find the sweet spot that
delivers the required performance at the lowest possible cost.
Additionally, implementing auto scaling assists in verifying that
your deployment can handle varying loads efficiently, scaling up
during peak demand and down during quiet periods to avoid
unnecessary costs.

### Implementation steps

1. **Use Amazon SageMaker AI Inference
   Recommender for instance selection**. Amazon SageMaker AI Inference Recommender automatically selects the
   right compute instance type, instance count, container
   parameters, and model optimizations for inference to
   maximize performance and minimize cost. You can use
   SageMaker AI Inference Recommender from SageMaker AI Studio,
   the AWS Command Line Interface (AWS CLI), or the AWS SDK,
   and within minutes, get recommendations to deploy your ML
   model. You can then deploy your model to one of the
   recommended instances or run a fully managed load test on a
   set of instance types you choose without worrying about
   testing infrastructure. You can review the results of the
   load test in SageMaker AI Studio and evaluate the tradeoffs
   between latency, throughput, and cost to select the most
   optimal deployment configuration.
2. **Configure auto scaling for SageMaker AI
   endpoints**. Amazon SageMaker AI supports an auto
   scaling feature that monitors your workloads and dynamically
   adjusts the capacity to maintain steady and predictable
   performance at the lowest possible cost. When the workload
   increases, auto scaling brings more instances online. When
   the workload decreases, auto scaling removes unnecessary
   instances, which can reduce your compute cost. SageMaker AI
   automatically attempts to distribute your instances across
   Availability Zones. So, we strongly recommend that you
   deploy multiple instances for each production endpoint for
   high availability. If you're using a VPC, configure at least
   two subnets in different Availability Zones so Amazon SageMaker AI can distribute your instances across those
   Availability Zones.
3. **Implement proper scaling
   policies**. Define appropriate scaling policies
   based on your model's performance characteristics and usage
   patterns. Set scaling metrics such as CPU utilization, GPU
   utilization, model latency, or custom metrics that reflect
   your workload's needs. Define appropriate target values and
   cooldown periods to avoid rapid scaling oscillations.
4. **Consider serverless inference
   options**. For workloads with unpredictable or
   intermittent traffic patterns, evaluate
   [Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md"), which automatically
   provisions and scales compute capacity based on traffic.
   This option reduces the need to select instance types or
   manage scaling policies while providing pay-per-use pricing.
5. **Regularly review and optimize
   deployments**. Set up a process to periodically
   review your model deployments' performance and cost metrics.
   As your models evolve and usage patterns change, rerun
   Inference Recommender tests to keep your infrastructure
   optimized. Look for opportunities to consolidate models or
   use multi-model endpoints where appropriate.
6. **Use SageMaker AI Training Plans for
   predictable access**. Use
   [SageMaker AI
   Training Plans](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") as a compute reservation system for
   predictable access to high-demand GPU resources, managing
   large-scale AI training workloads more efficiently with
   better resource planning and scheduling capabilities.
7. **Use model optimization
   techniques**. For large language models and other
   generative AI workloads, consider techniques like
   quantization, distillation, or pruning to reduce model size
   and computational requirements. Amazon SageMaker AI supports
   optimization techniques through
   [SageMaker AI
   Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md") and integration with
   [AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/ "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/") for optimized inference on AWS Inferentia and
   Trainium chips.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Automatic
  scaling of Amazon SageMaker AI models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Multi-model
  endpoints](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Model
  performance optimization with SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")

**Related examples:**

- [SageMaker AI Inference Recommender](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb")
- [Right-sizing
  your Amazon SageMaker AI Endpoints](https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker AI%20Endpoints.ipynb "https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker AI%20Endpoints.ipynb")
- [SageMaker AI
  Serverless Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/serverless-inference "https://github.com/aws/amazon-sagemaker-examples/tree/main/serverless-inference")
- [Automatically
  Scale Amazon SageMaker AI Models](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md")
