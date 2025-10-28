# Inference cost optimization best practices

The following content provides techniques and considerations for optimizing the cost of endpoints.
You can use these recommendations to optimize the cost for both new and existing endpoints.

## Best practices

To optimize your SageMaker AI Inference costs, follow these best practices.

SageMaker AI offers 4 different inference options to provide the best inference option for the job.
You may be able to save on costs by picking the inference option that best matches your workload.

- Use [real-time inference](realtime-endpoints.md "realtime-endpoints.md")
  for low latency workloads with predictable traffic patterns that need to have consistent latency
  characteristics and are always available. You pay for using the instance.
- Use [serverless inference](serverless-endpoints.md "serverless-endpoints.md")
  for synchronous workloads that have a spiky traffic pattern and can accept variations in the p99 latency.
  Serverless inference automatically scales to meet your workload traffic so you don’t pay for any idle resources.
  You only pay for the duration of the inference request. The same model and containers can be used with both real-time
  and serverless inference so you can switch between these two modes if your needs change.
- Use [asynchronous inference](async-inference.md "async-inference.md")
  for asynchronous workloads that process up to 1 GB of data (such as text corpus, image, video, and audio)
  that are latency insensitive and cost sensitive. With asynchronous inference, you can control costs by specifying
  a fixed number of instances for the optimal processing rate instead of provisioning for the peak. You can also
  scale down to zero to save additional costs.
- Use [batch inference](batch-transform.md "batch-transform.md")
  for workloads for which you need inference for a large set of data for processes that happen offline (that is,
  you don’t need a persistent endpoint). You pay for the instance for the duration of the batch inference job.

- If you have a consistent usage level across all SageMaker AI services, you can opt in to a SageMaker AI Savings Plan to
  help reduce your costs by up to 64%.
- [Amazon SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/ "https://aws.amazon.com/savingsplans/ml-pricing/") provide a flexible pricing model
  for Amazon SageMaker AI, in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a one-year
  or three-year term. These plans automatically apply to eligible SageMaker AI ML instance usages including
  SageMaker Studio Classic Notebook, SageMaker On-Demand Notebook, SageMaker Processing, SageMaker Data Wrangler,
  SageMaker Training, SageMaker Real-Time Inference, and SageMaker Batch Transform regardless of instance
  family, size, or Region. For example, you can change usage from a CPU ml.c5.xlarge instance running in
  US East (Ohio) to a ml.Inf1 instance in US West (Oregon) for inference workloads at any time and automatically
  continue to pay the Savings Plans price.

- Unoptimized models can lead to longer run times and use more resources. You may choose to use more
  or bigger instances to improve performance; however, this leads to higher costs.
- By optimizing your models to be more performant, you may be able to lower costs by using fewer or smaller
  instances while keeping the same or better performance characteristics. You can use
  [SageMaker Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/") with SageMaker AI Inference to automatically optimize models.
  For more details and samples, see [Model performance optimization with SageMaker Neo](neo.md "neo.md").

- SageMaker Inference has over 70 instance types and sizes that can be used to deploy ML models
  including AWS Inferentia and Graviton chipsets that are optimized for ML. Choosing the right instance for your
  model helps ensure you have the most performant instance at the lowest cost for your models.

- By using [Inference Recommender](inference-recommender.md "inference-recommender.md"),
  you can quickly compare different instances to understand the performance of the model and the costs.
  With these results, you can choose the instance to deploy with the best return on investment.

- Costs can quickly add up when you deploy multiple endpoints, especially if the endpoints don’t fully utilize
  the underlying instances. To understand if the instance is under-utilized, check the utilization metrics (CPU, GPU, etc) in
  Amazon CloudWatch for your instances. If you have more than one of these endpoints, you can combine the models or containers
  on these multiple endpoints into a single endpoint.
- Using [Multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md") (MME) or
  [Multi-container endpoints](multi-container-endpoints.md "multi-container-endpoints.md") (MCE), you
  can deploy multiple ML models or containers in a single endpoint to share the instance across multiple models or containers
  and improve your return on investment. To learn more, see this
  [Save on inference costs by using Amazon SageMaker AI multi-model endpoints](https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/ "https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/")
  or [Deploy multiple serving containers on a single instance using Amazon SageMaker AI multi-container endpoints](https://aws.amazon.com/blogs/machine-learning/deploy-multiple-serving-containers-on-a-single-instance-using-amazon-sagemaker-multi-container-endpoints/ "https://aws.amazon.com/blogs/machine-learning/deploy-multiple-serving-containers-on-a-single-instance-using-amazon-sagemaker-multi-container-endpoints/") on the AWS Machine Learning blog.

- Without autoscaling, you need to provision for peak traffic or risk model unavailability. Unless the traffic to your model
  is steady throughout the day, there will be excess unused capacity. This leads to low utilization and wasted resources.
- [Autoscaling](endpoint-auto-scaling.md "endpoint-auto-scaling.md") is an out-of-the-box feature
  that monitors your workloads and dynamically adjusts the capacity to maintain steady and predictable performance at the possible
  lowest cost. When the workload increases, autoscaling brings more instances online. When the workload decreases, autoscaling
  removes unnecessary instances, helping you reduce your compute cost. To learn more, see
  [Configuring autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/") on the AWS Machine Learning blog.
