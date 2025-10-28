# MLCOST-26: Right-size the model hosting instance fleet

Use efficient compute resources to run models in production. In
many cases, up to 90% of the infrastructure spend for developing
and running an ML application is on inference, making it
critical to use high-performance, cost-effective ML inference
infrastructure. Selecting the right way to host and the right
type of instance can have a large impact on the total cost of ML
projects. Use automatic scaling (autoscaling) for your hosted
models. _Auto scaling_ dynamically adjusts
the number of instances provisioned for a model in response to
changes in your workload. 

## Implementation plan

- **Use Amazon SageMaker AI Inference
  Recommender** - Amazon SageMaker AI Inference
  Recommender automatically selects the right compute
  instance type, instance count, container parameters, and
  model optimizations for inference to maximize performance
  and minimize cost. You can use SageMaker AI Inference
  Recommender from SageMaker AI Studio, the AWS Command Line Interface (AWS CLI), or the AWS SDK, and within minutes,
  get recommendations to deploy your ML model. You can then
  deploy your model to one of the recommended instances or
  run a fully managed load test on a set of instance types
  you choose without worrying about testing infrastructure.
  You can review the results of the load test in SageMaker AI
  Studio and evaluate the tradeoffs between latency,
  throughput, and cost to select the most optimal deployment
  configuration.
- **Use AutoScaling with Amazon SageMaker AI** - Amazon SageMaker AI supports an
  Autoscaling feature that monitors your workloads and
  dynamically adjusts the capacity to maintain steady and
  predictable performance at the lowest possible cost. When
  the workload increases, autoscaling brings more instances
  online. When the workload decreases, autoscaling removes
  unnecessary instances, helping you reduce your compute
  cost. SageMaker AI automatically attempts to distribute your
  instances across Availability Zones. So, we strongly
  recommend that you deploy multiple instances for each
  production endpoint for high availability. If you’re using
  a VPC, configure at least two subnets in different
  Availability Zones so Amazon SageMaker AI can distribute your
  instances across those Availability Zones.

## Documents

- [Automatically
  Scale Amazon SageMaker AI Models](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md")

## Blogs

- [Ensure
  efficient compute resources on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/ensure-efficient-compute-resources-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/ensure-efficient-compute-resources-on-amazon-sagemaker/")
- [Configuring
  autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/")
- [Announcing
  Amazon SageMaker AI Inference Recommender](https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-inference-recommender/ "https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-inference-recommender/")

## Examples

- [Right-sizing
  your Amazon SageMaker AI Endpoints](https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker%20Endpoints.ipynb "https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker%20Endpoints.ipynb")
- [Automatically
  Scale Amazon SageMaker AI Models](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md")
- [SageMaker AI
  Inference Recommender](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb")
