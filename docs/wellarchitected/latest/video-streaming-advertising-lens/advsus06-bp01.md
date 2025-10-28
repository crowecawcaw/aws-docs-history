# ADVSUS06-BP01 Shut down resources when not in use, and implement energy-efficient machine learning models

Resources for machine learning may have real-time demands that
fluctuate or not be needed at certain times, such as when data can
be processed as a batch. Set machine learning workloads to respond
to demand in real-time, including turning off or shutting down
resources when not needed. Use available tools to optimize the
compute resources and models used for machine learning workloads.

## Implementation guidance

- Organizations can use machine learning to draw insights on
  correlation and causation from data sets in order to
  optimize advertising activities. However, resources for data
  preparation, identity resolution, data collaboration, and
  creation of machine learning models do not need to run 24/7.
  Optimize and shut down these resources when not in use to
  reduce carbon emissions.
- When using
  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"), customers can take multiple steps to
  optimize their compute usage:
  - Use Graviton-based instances when possible.
  - [Amazon SageMaker AI Inference Recommender](../../../sagemaker/latest/dg/inference-recommender.md "../../../sagemaker/latest/dg/inference-recommender.md") can specify the
    most performant instance type.
  - [Inference
    optimization techniques](../../../sagemaker/latest/dg/model-optimize.md "../../../sagemaker/latest/dg/model-optimize.md") can be applied to
    SageMaker AI models.
  - SageMaker AI can dynamically adjust the number of instances
    provisioned for a model in response to changes in your
    workload by
    using [scaling
    policies](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md").

- Use AI chips that provide the highest performance for
  training and inference, such as
  [AWS Tranium](https://aws.amazon.com/ai/machine-learning/trainium/ "https://aws.amazon.com/ai/machine-learning/trainium/") and
  [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/ "https://aws.amazon.com/ai/machine-learning/inferentia/").
