# Limitations of customizing Amazon Nova models

Amazon Nova customization doesn't support the following capabilities on SageMaker.

- **SSH into the instance to find the
  metrics**

Due to security controls in place, you can't SSH into the master node in the
training algo-1 instance to find memory stats or NVIDIA stats and validate the
training steps.

- **Warm pools are not accessible to SageMaker training
  jobs**

Due to security controls in place, the SageMaker warm pools can't be used to keep
the instance in the warm pool till the time to live.

- **Custom model merging**

Merging multiple models is not currently supported. This means that creating
multiple LoRA adapters and perform a multi-merge operation with the base model
is not available.

- **Supported observability tool**

[TensorBoard](https://www.tensorflow.org/tensorboard "https://www.tensorflow.org/tensorboard") and [MLflow](https://mlflow.org/ "https://mlflow.org/") are the
only supported observability tools to view metrics for SageMaker training jobs. For
more information, see [TensorBoard in SageMaker](../../../sagemaker/latest/dg/tensorboard-on-sagemaker.md "../../../sagemaker/latest/dg/tensorboard-on-sagemaker.md") and [MLflow in SageMaker](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md").
