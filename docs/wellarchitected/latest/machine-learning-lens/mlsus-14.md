# MLSUS-14: Deploy multiple models behind a single endpoint

Host multiple models behind a single endpoint to improve
endpoint utilization. Sharing endpoint resources is more
sustainable and less expensive than deploying a single model
behind one endpoint.

## Implementation plan

Amazon SageMaker AI provides three methods to deploy multiple
models to a single endpoint:

- **Host multiple models in one
  container behind one endpoint** (MLCOST-24) -
  SageMaker AI multi-model endpoints (MME) are served using a
  single container. This feature is ideal when you have a
  large number of similar models that you can serve through
  a shared serving container and don’t need to access all
  the models at the same time. This can help cut inference
  costs and reduce
  [carbon
  emissions by up to 90%](https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/ "https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/") .
- **Host multiple models which use
  different containers behind one endpoint**
  (MLCOST-24) – SageMaker AI multi-container endpoint
  ([MCE)](../../../sagemaker/latest/dg/multi-container-endpoints.md "../../../sagemaker/latest/dg/multi-container-endpoints.md")
  support deploying up to 15 containers that use different
  models or framework on a single endpoint, and invoking
  them independently or in sequence for low-latency
  inference and cost savings. The models can be completely
  heterogenous, with their own independent serving stack.
- **Use SageMaker AI inference
  pipelines** - An _inference
  pipeline_ is an Amazon SageMaker AI model that is
  composed of a linear sequence of containers deployed
  behind a single endpoint. You can use an inference
  pipeline to combine preprocessing, predictions, and
  post-processing data science tasks. The output from the
  one container is passed as input to the next. When
  defining the containers for a pipeline model, you also
  specify the order in which the containers are run.

## Documents

- [Host
  multiple models in one container behind one
  endpoint](../../../sagemaker/latest/dg/multi-model-endpoints.md "../../../sagemaker/latest/dg/multi-model-endpoints.md")
- [Host
  multiple models which use different containers behind one
  endpoint](../../../sagemaker/latest/dg/multi-container-endpoints.md "../../../sagemaker/latest/dg/multi-container-endpoints.md")
- [Host
  models along with pre-processing logic as serial inference
  pipeline behind one endpoint](../../../sagemaker/latest/dg/inference-pipelines.md "../../../sagemaker/latest/dg/inference-pipelines.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 3, deployment and
  monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/")
- [Save
  on inference costs by using Amazon SageMaker AI multi-model
  endpoints](https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/ "https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/")
