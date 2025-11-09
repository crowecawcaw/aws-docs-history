# Train a Model with Amazon SageMaker

Amazon SageMaker Training is a fully managed machine learning (ML) service offered by SageMaker that
helps you efficiently train a wide range of ML models at scale. The core of SageMaker AI jobs is the
containerization of ML workloads and the capability of managing AWS compute resources. The
SageMaker Training platform takes care of the heavy lifting associated with setting up and
managing infrastructure for ML training workloads. With SageMaker Training, you can focus on
developing, training, and fine-tuning your model. This page introduces three recommended
ways to get started with training a model on SageMaker, followed by additional options you can
consider.

###### Tip

For information about training foundation models for Generative AI, see [Use
SageMaker JumpStart foundation models in Amazon SageMaker Studio](jumpstart-foundation-models-use-studio-updated.md "jumpstart-foundation-models-use-studio-updated.md").

## Choosing a feature within

Amazon SageMaker Training

There are three main use cases for training ML models within SageMaker AI. This section
describes those use cases, as well as the SageMaker AI features we recommend for each use case.

Whether you are training complex deep learning models or implementing smaller machine
learning algorithms, SageMaker Training provides streamlined and cost-effective solutions
that meet the requirements of your use cases.

### Use cases

The following are the main uses cases for training ML models within SageMaker AI.

- Use case 1: Develop a machine learning
  model in a low-code or no-code environment.
- Use case 2: Use code to develop machine
  learning models with more flexibility and control.
- Use case 3: Develop machine learning models
  at scale with maximum flexibility and control.

### Recommended

features

The following table describes three common scenarios of training ML models and
corresponding options to get started with SageMaker Training.

| Descriptor              | Use case 1                                                                                                                                                                                                                                                                                                                                                                                                                  | Use case 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Use case 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SageMaker AI feature    | [Build a model<br>using Amazon SageMaker Canvas](canvas-build-model.md "canvas-build-model.md").                                                                                                                                                                                                                                                                                                                            | Train a model using one of the [SageMaker AI built-in ML algorithms](algos.md "algos.md") such as [XGBoost](xgboost.md#xgboost-modes "xgboost.md#xgboost-modes") or [Task-Specific Models by SageMaker JumpStart](jumpstart-models.md "jumpstart-models.md") with the<br>SageMaker Python SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                            | Train a model at scale with maximum flexibility leveraging [script mode](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/sagemaker-script-mode.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/sagemaker-script-mode.html") or [custom containers](docker-containers-adapt-your-own.md "docker-containers-adapt-your-own.md") in SageMaker AI.                                                                                                                                                                                                    |
| Description             | Bring your data. SageMaker AI helps manage building ML models and setting<br>up the training infrastructure and resources.                                                                                                                                                                                                                                                                                                  | Bring your data and choose one of the built-in ML algorithms<br>provided by SageMaker AI. Set up the model hyperparameters, output<br>metrics, and basic infrastructure settings using the SageMaker Python<br>SDK. The SageMaker Training platform helps provision the training<br>infrastructure and resources.                                                                                                                                                                                                                                                                                                                                                                                                                         | Develop your own ML code and bring it as a script or a set of<br>scripts to SageMaker AI. To learn more, see [Distributed computing with SageMaker best<br>practices](distributed-training-options.md#distributed-training-options-2 "distributed-training-options.md#distributed-training-options-2"). Additionally, you can [bring your own Docker container](adapt-training-container.md#byoc-training-step2 "adapt-training-container.md#byoc-training-step2"). The SageMaker Training<br>platform helps provision the training infrastructure and<br>resources at scale based on your custom settings. |
| Optimized for           | Low/no-code and UI-driven model development with quick<br>experimentation with a training dataset. When you [build a custom model](canvas-build-model.md "canvas-build-model.md") an<br>algorithm automatically selected based on your data. For<br>advanced customization options like algorithm selection, see<br>[advanced model<br>building configurations](canvas-advanced-settings.md "canvas-advanced-settings.md"). | Training ML models with high-level customization for<br>hyperparameters, infrastructure settings, and the ability to<br>directly use ML frameworks and entrypoint scripts for more<br>flexibility. Use built-in algorithms, pre-trained models, and<br>JumpStart models through the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") to develop<br>ML models. For more information, see [Low-code deployment with the JumpStart<br>class](https://sagemaker.readthedocs.io/en/stable/overview.html#low-code-deployment-with-the-jumpstartmodel-class "https://sagemaker.readthedocs.io/en/stable/overview.html#low-code-deployment-with-the-jumpstartmodel-class"). | ML training workloads at scale, requiring multiple instances<br>and maximum flexibility. See [distributed computing<br>with SageMaker best practices](distributed-training-options.md "distributed-training-options.md"). SageMaker AI uses Docker<br>images to host the training and serving of all models. You can<br>use any SageMaker AI or external algorithms and [use Docker containers to build<br>models](docker-containers.md "docker-containers.md").                                                                                                                                            |
| Considerations          | Minimal flexibility to customize the model provided by<br>Amazon SageMaker Canvas.                                                                                                                                                                                                                                                                                                                                          | The SageMaker Python SDK provides a simplified interface and fewer<br>configuration options compared to the low-level SageMaker Training<br>API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Requires knowledge of AWS infrastructure and distributed<br>training options. See also [Create your own training container](your-algorithms-training-algo.md "your-algorithms-training-algo.md") using the [SageMaker Training toolkit](amazon-sagemaker-toolkits.md "amazon-sagemaker-toolkits.md").                                                                                                                                                                                                                                                                                                       |
| Recommended environment | Use [Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"). To learn how to set it up, see [Getting started with using SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md").                                                                                                                                                        | Use [SageMaker AI<br>JupyterLab](studio-updated-jl.md "studio-updated-jl.md") within [Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md"). To learn how to set it up, see [Launch<br>Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use [SageMaker<br>JupyterLab](studio-updated-jl.md "studio-updated-jl.md") within [Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md"). To learn how to set it up, see [Launch<br>Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").                                                                                                                                                                                                                                                                                                                  |

## Additional

options

SageMaker AI offers the following additional options for training ML models.

**SageMaker AI features offering training capabilities**

- **[SageMaker
  JumpStart](studio-jumpstart.md "studio-jumpstart.md")**: SageMaker JumpStart provides access to
  the SageMaker AI public model hub that contains the latest publicly available and
  proprietary foundation models (FMs). You can fine-tune, evaluate, and deploy
  these models within Amazon SageMaker Studio. SageMaker JumpStart streamlines the process of
  leveraging foundation models for your generative AI use-cases and allows you to
  create private model hubs to use foundation models while enforcing governance
  guardrails and ensuring that your organization can only access approved models.
  To get started with SageMaker JumpStart, see [SageMaker JumpStart Foundation Models](jumpstart-foundation-models.md "jumpstart-foundation-models.md").
- **[SageMaker HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md")**: SageMaker HyperPod is a persistent cluster
  service for use cases that need resilient clusters for massive machine learning
  (ML) workloads and developing state-of-the-art foundation models (FMs). It
  accelerates development of such models by removing undifferentiated
  heavy-lifting involved in building and maintaining large-scale compute clusters
  powered by thousands of accelerators such as AWS Trainium or NVIDIA A100 and
  H100 Graphical Processing Units (GPUs). You can use workload manager software
  such as Slurm on HyperPod.

**More features of SageMaker Training**

- **[Hyperparameter
  Tuning](automatic-model-tuning.md "automatic-model-tuning.md")**: This SageMaker AI feature helps define a set of
  hyperparameters for a model and launch many training jobs on a dataset.
  Depending on the hyperparameter values, the model training performance might
  vary. This feature provides the best performing set of hyperparameters within
  the given range of hyperparameters you set to search through.
- **[Distributed
  training](distributed-training.md "distributed-training.md")**: Pre-train or fine-tune FMs built with
  PyTorch, NVIDIA CUDA, and other PyTorch-based frameworks. To efficiently utilize
  GPU instances, use the SageMaker AI distributed training libraries that offer collective
  communication operations and various model parallelism techniques such as expert
  parallelism and shared data parallelism that are optimized for AWS
  infrastructure.
- **Observability features**: Use the profiling and
  debugging functionalities of SageMaker Training to gain insights into model training
  workloads, model performance, and resource utilization. To learn more, see
  [Debug and improve model performance](train-debug-and-improve-model-performance.md "train-debug-and-improve-model-performance.md") and [Profile and optimize computational performance](train-profile-computational-performance.md "train-profile-computational-performance.md").
- **Cost-saving and efficient instance options**:
  To optimize compute cost and efficiency for training instance provisioning, use
  [Heterogeneous
  Cluster](train-heterogeneous-cluster.md "train-heterogeneous-cluster.md"), [Managed Spot
  instances](model-managed-spot-training.md "model-managed-spot-training.md"), or [Managed Warm
  Pools](train-warm-pools.md "train-warm-pools.md").
