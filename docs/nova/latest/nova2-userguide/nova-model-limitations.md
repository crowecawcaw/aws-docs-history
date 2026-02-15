# Limitations of customizing Amazon Nova models

Amazon Nova customization doesn't support the following capabilities on SageMaker AI.

- **SSH into the instance to find the
  metrics**

Due to security controls in place, you can't SSH into the master node in the
training algo-1 instance to find memory stats or NVIDIA stats and validate the
training steps.

- **Support for SageMaker AI trainer SDK**

SageMaker AI trainer is currently not available to start training jobs. You can start
training jobs only via **estimator API** today.

- **Warm pools are not accessible to SageMaker AI training
  jobs**

Due to security controls in place, the SageMaker AI warm pools can't be used to keep
the instance in the warm pool till the time to live.

- **Custom model merging**

Merging multiple models is not currently supported. This means that creating
multiple LoRA adapters and perform a multi-merge operation with the base model
is not available.

- **Supported observability tool**

[TensorBoard](https://www.tensorflow.org/tensorboard "https://www.tensorflow.org/tensorboard") is the
only supported observability tool to view metrics for SageMaker AI training jobs.
[MLFlow](https://mlflow.org/ "https://mlflow.org/") or [WandB](https://wandb.ai/site/ "https://wandb.ai/site/") are not currently supported. For
more information about using TensorBoard in SageMaker AI, see [TensorBoard in SageMaker AI](../../../sagemaker/latest/dg/tensorboard-on-sagemaker.md "../../../sagemaker/latest/dg/tensorboard-on-sagemaker.md").
