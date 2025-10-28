# MLPER-12: Choose an optimal deployment option in the cloud

If models are suitable for cloud deployment, you should
determine how to deploy them for best performance efficiency
according to frequency, latency, and runtime requirements in
your use cases.

## Implementation plan

- **Amazon SageMaker AI Real-time
  Inference** - Use if you need a persistent
  endpoint for near-instantaneous response from the ML model
  for requests that can come in any time. You can host the
  models behind an HTTPS endpoint to be integrated with your
  applications. SageMaker AI real-time endpoints are fully
  managed and support autoscaling.
- **Amazon SageMaker AI Serverless
  Inference** - Use if you receive spiky inference
  requests that vary substantially in rate and volume. This
  is a purpose-built inference option that makes it easy to
  deploy and scale ML models without managing any servers.
  Serverless Inference is ideal for workloads which have
  idle periods between traffic spurts and can tolerate cold
  starts.
- **Amazon SageMaker AI Asynchronous
  Inference** - Use if you have model requests with
  large payload sizes (up to 1GB), long processing times (up
  to 15 minutes), and near-instantaneous latency
  requirements, SageMaker AI Asynchronous Inference is ideal as
  it has larger payload limit and longer time-out limit
  compared to SageMaker AI Real-time inference. SageMaker AI
  Asynchronous Inference queues incoming requests and
  processes them asynchronously with an internal queueing
  system.
- **Amazon SageMaker AI Batch
  Transform** - Use if you do not need
  near-instantaneous response from the ML model and can
  gather data points together into a large batch for a
  schedule-based inference. When a batch transform job
  starts, SageMaker AI initializes compute instances and
  distributes the inference or preprocessing workload among
  them. SageMaker AI Batch Transform automatically splits input
  files into mini-batches (so that you won’t need to worry
  about out-of-memory (OOM) for large datasets) and shuts
  down compute instances once the entire dataset is
  processed.

## Documents

- [Amazon SageMaker AI Real-time Inference](../../../sagemaker/latest/dg/realtime-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints.md")
- [Amazon SageMaker AI Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
- [Amazon SageMaker AI Asynchronous Inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [Amazon SageMaker AI Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md")

## Blogs

- [Announcing
  managed inference for Hugging Face models in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/")
- [Performing
  batch inference with TensorFlow Serving in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/performing-batch-inference-with-tensorflow-serving-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/performing-batch-inference-with-tensorflow-serving-in-amazon-sagemaker/")
- [Deploying
  ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/ "https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/")
- [Run
  computer vision inference on large videos with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/ "https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/")

## Videos

- [AWS re:Invent 2021 - Achieve high performance and
  cost-effective model deployment](https://youtu.be/gWuO0gNKlm8 "https://youtu.be/gWuO0gNKlm8")
- [AWS re:Invent 2021 - Amazon SageMaker AI serverless
  inference](https://youtu.be/KB6vLQGixjA "https://youtu.be/KB6vLQGixjA")

## Examples

- [Deploy
  models with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html "https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html")
