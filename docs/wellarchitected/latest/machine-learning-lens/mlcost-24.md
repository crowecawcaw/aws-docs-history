# MLCOST-24: Use appropriate deployment option

Use real-time inference for low latency and ultra-high
throughput for use cases with steady traffic patterns. Use batch
transform for offline inference on data batches for use cases
with large datasets. Deploy models at edge to optimize, secure,
monitor, and maintain machine learning models on fleets of edge
devices such as smart cameras, robots, personal computers, and
mobile devices.

## Implementation plan

- **Use Amazon SageMake**r -
  Amazon SageMaker AI has a broad selection of ML
  infrastructure and model deployment options to make it
  easy to deploy ML models at the best price-performance for
  any use case. It is a fully managed service and integrates
  with MLOps tools, so you can scale your model deployment,
  reduce inference costs, manage models more effectively in
  production, and reduce operational burden. 
  - **Use Amazon SageMaker AI Real-time
    Inference, Amazon SageMaker AI Serverless Inference,
    Amazon SageMaker AI Asynchronous Inference, and Amazon SageMaker AI Batch Transform** - See “MLPER-11:
    Evaluate cloud versus edge options for machine
    learning deployment“.
  - **Use Amazon SageMaker AI
    Multi-Model endpoints** - Multi-model
    endpoints provide a scalable and cost-effective
    solution to deploying large numbers of models. They
    use a shared serving container that is enabled to host
    multiple models. This approach reduces hosting costs
    by improving endpoint utilization compared with using
    single-model endpoints. It also reduces deployment
    overhead because Amazon SageMaker AI manages loading
    models in memory and scaling them based on the traffic
    patterns to them.
  - **Use Amazon SageMaker AI
    multi-container endpoints** - SageMaker AI
    multi-container endpoints enable you to deploy
    multiple containers that use different models or
    frameworks on a single SageMaker AI endpoint. The
    containers can be run in a sequence as an inference
    pipeline, or each container can be accessed
    individually by using direct invocation to improve
    endpoint utilization and optimize costs.
  - **Use Amazon SageMaker AI
    Pipelines** - See
    **“MLREL-10: Automate endpoint
    changes through a pipeline“.**
  - **Use Amazon SageMaker AI
    Edge** - See “Optimize model deployment on
    the edge” under “MLPER-10: Evaluate machine learning
    deployment option (cloud versus edge)”.

## Documents

- [Deploy
  models for inference](../../../sagemaker/latest/dg/deploy-model.md "../../../sagemaker/latest/dg/deploy-model.md")
- [SageMaker AI
  hosting options](../../../sagemaker/latest/dg/realtime-endpoints-options.md "../../../sagemaker/latest/dg/realtime-endpoints-options.md")
- [SageMaker AI
  Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [SageMaker AI
  Asynchronous Inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [SageMaker AI
  Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md")
- [Deploy
  models at the edge with SageMaker AI Edge Manager](../../../sagemaker/latest/dg/edge.md "../../../sagemaker/latest/dg/edge.md")

## Blogs

- [Using
  Amazon SageMaker AI inference pipelines with multi-model
  endpoints](https://aws.amazon.com/blogs/machine-learning/using-amazon-sagemaker-inference-pipelines-with-multi-model-endpoints/ "https://aws.amazon.com/blogs/machine-learning/using-amazon-sagemaker-inference-pipelines-with-multi-model-endpoints/")
- [Save
  on inference costs by using Amazon SageMaker AI multi-model
  endpoints](https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/ "https://aws.amazon.com/blogs/machine-learning/save-on-inference-costs-by-using-amazon-sagemaker-multi-model-endpoints/")
- [Deploy
  multiple serving containers on a single instance using
  Amazon SageMaker AI multi-container endpoints](https://aws.amazon.com/blogs/machine-learning/deploy-multiple-serving-containers-on-a-single-instance-using-amazon-sagemaker-multi-container-endpoints/ "https://aws.amazon.com/blogs/machine-learning/deploy-multiple-serving-containers-on-a-single-instance-using-amazon-sagemaker-multi-container-endpoints/")
- [Run
  computer vision inference on large videos with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/")
- [Batch
  Inference at Scale with Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/batch-inference-at-scale-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/architecture/batch-inference-at-scale-with-amazon-sagemaker/")
- [Amazon SageMaker AI Edge Manager Simplifies Operating Machine
  Learning Models on Edge Devices](https://aws.amazon.com/blogs/aws/amazon-sagemaker-edge-manager-simplifies-operating-machine-learning-models-on-edge-devices/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-edge-manager-simplifies-operating-machine-learning-models-on-edge-devices/")

## Examples

- [SageMaker AI
  Serverless Inference Walkthrough](https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/Serverless-Inference-Walkthrough.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/Serverless-Inference-Walkthrough.ipynb")
- [SageMaker AI
  Edge Manager Workshop](https://github.com/aws-samples/amazon-sagemaker-edge-manager-workshop "https://github.com/aws-samples/amazon-sagemaker-edge-manager-workshop")
