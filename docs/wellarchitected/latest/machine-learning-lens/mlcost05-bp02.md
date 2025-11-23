# MLCOST05-BP02 Explore cost effective hardware options

Machine learning models that power AI applications are becoming
increasingly complex resulting in rising underlying compute
infrastructure costs. Up to 90% of the infrastructure spend for
developing and running ML applications is often on inference. Look
for cost-effective infrastructure solutions for deploying their ML
applications in production.

**Desired outcome:** You achieve
significant cost savings while maintaining or improving the
performance of your machine learning inference workloads. By
implementing cost-effective hardware options, you optimize your
infrastructure spend, reduce operational costs, and can allocate
resources more efficiently across your ML applications. Your ML
models run on purpose-built hardware that provides the right balance
of performance and cost for your specific use case.

**Common anti-patterns:**

- Using general-purpose compute instances for ML workloads without
  considering specialized hardware options.
- Over-provisioning inference resources to handle peak loads
  without implementing scaling strategies.
- Ignoring model optimization opportunities before deploying to
  production.
- Selecting hardware based solely on performance metrics without
  considering cost-efficiency.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for ML model inference.
- Improved inference throughput and latency.
- More efficient use of computational resources.
- Lower total cost of ownership for AI applications.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning inference costs represent a significant portion
of the total expenses associated with running ML workloads in
production. As models become more complex, their computational
requirements increase, which can lead to higher infrastructure
costs. Selecting the right hardware for your ML workloads is
crucial for maintaining cost efficiency without sacrificing
performance.

AWS offers multiple options to optimize the cost and performance
of your ML inference workloads. These include services that
optimize models for specific hardware targets, instances that
provide cost-effective acceleration for inference workloads, and
deployment options that match your specific latency and throughput
requirements.

Evaluating your specific workload requirements is essential before
selecting hardware options. Consider factors such as latency
requirements, throughput needs, model complexity, batch size
capabilities, and budget constraints. This evaluation will assist
you to determine the most appropriate hardware solution for your
use case.

### Implementation steps

1. **Use Amazon SageMaker AI Neo for model
   optimization**. Amazon SageMaker AI Neo automatically
   optimizes machine learning models for inference on cloud
   instances and edge devices. For inference in the cloud,
   SageMaker AI Neo speeds up inference and saves cost by creating
   an inference optimized container in SageMaker AI hosting. For
   inference at the edge, SageMaker AI Neo saves developers months
   of manual tuning by automatically tuning the model for the
   selected operating system and processor hardware. Neo
   optimizes models trained in TensorFlow, PyTorch, MXNet, and
   other frameworks for deployment on ARM, Intel, and NVIDIA
   processors.
2. **Deploy on Amazon EC2 Inf2
   Instances**. Amazon EC2 Inf1 instances deliver
   high-performance ML inference at the lowest cost in the
   cloud. They deliver up to 2.3-times higher throughput and up
   to 70% lower cost per inference than comparable current
   generation GPU-based Amazon EC2 instances. Inf1 instances
   are built from the ground up to support machine learning
   inference applications. They feature up to 16 AWS Inferentia
   chips, high-performance machine learning inference chips
   designed and built by AWS. Additionally, Inf1 instances
   include second generation Intel Xeon Scalable processors and
   up to 100 Gbps networking to deliver high throughput
   inference.
3. **Explore Amazon EC2 Inf2
   Instances**. The second generation of AWS
   Inferentia-based instances, EC2 Inf2 instances, offer even
   greater performance improvements over previous generations.
   These instances are powered by AWS Inferentia2 chips and
   provide up to 4x higher throughput and up to 10x lower
   latency than Inf1 instances. They're ideal for more complex
   generative AI models and large language models (LLMs) that
   require high performance and cost-effective inference
   solutions.
4. **Consider Amazon SageMaker AI serverless
   inference**. SageMaker AI serverless inference is a
   purpose-built inference option that automatically
   provisions, scales, and shuts down compute capacity based on
   your workload needs. This pay-per-use model can reduce costs
   by avoiding the need to continuously run instances when
   there are no inference requests, making it ideal for
   workloads with intermittent traffic patterns.
5. **Evaluate batch and asynchronous
   inference options**. For non-real-time inference
   requirements, consider using SageMaker AI batch transform for
   offline inference processing or SageMaker AI asynchronous
   inference for workloads that can tolerate higher latency.
   These options often allow for more efficient resource
   utilization and lower costs compared to real-time inference
   endpoints.
6. **Implement automated scaling
   policies**. Configure auto-scaling for your
   SageMaker AI endpoints to dynamically adjust the number of
   instances based on workload demands. This way, you can pay
   for the resources you need while maintaining performance
   requirements during peak usage periods.
7. **Use enhanced SageMaker AI Inference
   Recommender**. Use
   [SageMaker AI
   Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") with enhanced algorithms and
   support for multi-model endpoints to get sophisticated cost
   optimization recommendations for your specific workloads.
8. **Regularly monitor and analyze
   inference costs**. Use AWS Cost Explorer and Amazon CloudWatch metrics to track your inference costs and
   performance metrics. Regularly review this data to identify
   optimization opportunities and adjust your hardware strategy
   accordingly.

## Resources

**Related documents:**

- [Model
  performance optimization with SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")
- [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/ "https://aws.amazon.com/ec2/instance-types/inf2/")
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")
- [Deploy
  models for inference](../../../sagemaker/latest/dg/deploy-model.md "../../../sagemaker/latest/dg/deploy-model.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Asynchronous
  inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")

**Related examples:**

- [AWS Neuron SDK Examples for Inferentia and Trainium
  instances](https://github.com/aws-neuron/aws-neuron-sdk "https://github.com/aws-neuron/aws-neuron-sdk")
