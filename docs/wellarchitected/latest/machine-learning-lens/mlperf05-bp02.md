# MLPERF05-BP02 Choose an optimal deployment option in the

cloud

When deploying machine learning models in the cloud, selecting the
right deployment option is crucial for performance efficiency. By
matching your deployment method to your use case requirements for
request frequency, latency, and runtime, you can optimize both
performance and cost.

**Desired outcome:** You can deploy
your machine learning models in a way that meets your application's
needs for throughput, response time, and cost efficiency. The
selected deployment option provides the optimal balance between
performance and resource utilization while accommodating your
workload patterns.

**Common anti-patterns:**

- Deploying models on persistent endpoints regardless of traffic
  patterns or workload spikes.
- Overlooking payload size and processing time requirements when
  selecting deployment options.
- Using real-time inference for batch processing use cases that
  don't require immediate responses.
- Failing to consider cost implications of different deployment
  options.
- Not monitoring and optimizing deployment configurations after
  initial setup.

**Benefits of establishing this best
practice:**

- Improved cost efficiency by matching resources to actual usage
  patterns.
- Enhanced performance through selection of appropriate deployment
  methods.
- Better scalability to handle varying workloads.
- Reduced operational overhead with managed deployment options.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting the optimal deployment option for your machine learning
models involves understanding your use case requirements and
matching them to the capabilities of different AWS SageMaker AI
deployment services. Consider factors such as request frequency,
payload size, processing time, and response latency needs.

Avoid deploying models on persistent endpoints regardless of
traffic patterns or workload spikes. Many organizations overlook
payload size and processing time requirements when selecting a
deployment option, use real-time inference for batch processing
use cases that don't require immediate responses, and fail to
consider cost implications of different deployment options.

For time-sensitive applications requiring immediate responses,
real-time inference provides persistent endpoints, while workloads
with inconsistent traffic patterns might benefit from serverless
options that scale automatically. For larger payloads or longer
processing times, asynchronous inference is appropriate, and for
non-time-sensitive bulk processing, batch transformation offers an
efficient option.

Your deployment choice should align with your application's
operational patterns to balance performance and cost efficiency. A
chatbot requiring immediate responses would benefit from real-time
inference, while overnight batch processing of transactions might
use batch transform.

### Implementation steps

1. **Evaluate your model deployment
   requirements**. Begin by clearly defining your
   application's requirements for inference frequency, latency
   needs, payload sizes, and budget constraints. Consider how
   often model predictions will be requested, how quickly
   responses must be delivered, and what resource constraints
   you may have.
2. **Implement Amazon SageMaker AI Real-time
   Inference for continuous, low-latency needs**.
   Deploy models that require near-instantaneous responses and
   consistent availability using
   [SageMaker AI
   real-time endpoints](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md"). These fully managed endpoints
   support auto-scaling and are ideal for applications like
   real-time recommendation engines, chatbots, or fraud
   detection systems where immediate response is critical.
3. **Implement Amazon SageMaker AI
   Serverless Inference for variable traffic
   patterns**. For workloads with inconsistent request
   patterns or idle periods between traffic spikes, use
   [SageMaker AI
   Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md"). This option automatically
   provisions and scales compute resources based on traffic,
   avoiding the need to manage server infrastructure while
   optimizing costs during periods of low utilization.
4. **Implement Amazon SageMaker AI
   Asynchronous Inference for large payloads or long
   processing**. For use cases involving large input
   files (up to 1GB) or models requiring extended processing
   time (up to 15 minutes), deploy using
   [SageMaker AI
   Asynchronous Inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md"). This option queues incoming
   requests and processes them when resources are available,
   making it ideal for tasks like video processing, large
   document analysis, or complex NLP tasks.
5. **Implement Amazon SageMaker AI Batch
   Transform for scheduled bulk processing**. For
   non-time-sensitive workloads where predictions can be
   processed in batches, such as overnight processing of
   transactions or weekly sentiment analysis of customer
   feedback, use
   [SageMaker AI
   Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md"). This option automatically
   distributes workloads across compute instances and shuts
   down resources when processing is complete.
6. **Monitor and optimize your
   deployment**. Once deployed, continuously monitor
   your model's performance, resource utilization, and costs.
   Use Amazon CloudWatch metrics to track invocation metrics,
   errors, latency, and resource utilization. Adjust
   auto-scaling configurations or switch deployment options if
   your usage patterns change over time.
7. **Implement security and
   governance**. Incorporate proper security controls
   in your model deployments, including IAM roles with least
   privilege access, network isolation where appropriate, and
   encryption of data in transit and at rest. Use
   [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md") to create persona-based IAM
   roles for different ML user types (data scientists, MLOps
   engineers, business analysts) with preconfigured templates
   that follow least-privilege principles. For regulated
   industries, implement model governance practices to track
   model versions, approvals, and changes.

## Resources

**Related documents:**

- [Real-time
  inference](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md")
- [Deploy
  models with Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Asynchronous
  inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [Batch
  transform for inference with Amazon SageMaker AI](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md")
- [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md")
- [Deploy
  models with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html "https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html")
- [Deploying
  ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/ "https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/")
- [Optimize
  deployment cost of Amazon SageMaker AI JumpStart foundation
  models with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/")
- [Announcing
  managed inference for Hugging Face models in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/")
- [Run
  computer vision inference on large videos with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/")

**Related videos:**

- [Achieve high
  performance and cost-effective model deployment](https://youtu.be/gWuO0gNKlm8 "https://youtu.be/gWuO0gNKlm8")
- [Amazon SageMaker AI serverless inference](https://youtu.be/KB6vLQGixjA "https://youtu.be/KB6vLQGixjA")
