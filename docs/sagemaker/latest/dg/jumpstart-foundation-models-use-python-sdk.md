

# Use foundation models with the SageMaker Python SDK
<a name="jumpstart-foundation-models-use-python-sdk"></a>

All JumpStart foundation models are available for programmatic deployment using the SageMaker Python SDK.

To deploy publicly available foundation models, you can use their model ID. To find a model ID, search for the foundation model by name in [Available foundation models](jumpstart-foundation-models-latest.md).

Proprietary models must be deployed using the model package information after subscribing to the model in AWS Marketplace. 

You can find the list of JumpStart available models in [Available foundation models](jumpstart-foundation-models-latest.md).

**Important**  
Some foundation models require explicit acceptance of an end-user license agreement (EULA). For more information, see [EULA acceptance with the SageMaker Python SDK](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk).

The following sections show how to fine-tune and deploy foundation models with the updated SageMaker Python SDK classes (`ModelTrainer`, `ModelBuilder`, and `JumpStartConfig`), depending on whether you're fine-tuning a public model, deploying a public model, or deploying a subscribed AWS Marketplace model:
+ Fine-tune publicly available foundation models with the `ModelTrainer` class.
+ Deploy publicly available foundation models with the `ModelBuilder` class.
+ Deploy proprietary foundation models with the `ModelBuilder` class, referencing the subscribed `ModelPackage`.

**Topics**
+ [Fine-tune publicly available foundation models with the `ModelTrainer` class](jumpstart-foundation-models-use-python-sdk-estimator-class.md)
+ [Deploy publicly available foundation models with the `ModelBuilder` class](jumpstart-foundation-models-use-python-sdk-model-class.md)
+ [Deploy proprietary foundation models with the `ModelBuilder` class](jumpstart-foundation-models-use-python-sdk-proprietary.md)