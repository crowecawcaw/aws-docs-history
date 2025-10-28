# Use foundation models

with the SageMaker Python SDK

All JumpStart foundation models are available for programmatic deployment using the
SageMaker Python SDK.

To deploy publicly available foundation models, you can use their model ID. You
can find the model IDs for all publicly available foundation models in the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html"). Search for the name
of a foundation model in the **Search** bar. Use the **Show
entries** dropdown or the pagination controls to navigate the available
models.

Proprietary models must be deployed using the model package information after
subscribing to the model in AWS Marketplace.

You can find the list of JumpStart available models in [Available foundation models](jumpstart-foundation-models-latest.md "jumpstart-foundation-models-latest.md").

###### Important

Some foundation models require explicit acceptance of an end-user license
agreement (EULA). For more information, see [EULA
acceptance with the SageMaker Python SDK](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk").

The following sections show how to fine-tune publicly available foundation models
using the `JumpStartEstimator` class, deploy publicly available
foundation models using the `JumpStartModel` class, and deploy
proprietary foundation models using the`ModelPackage` class.

###### Topics

- [Fine-tune publicly available foundation models with the
  JumpStartEstimator class](jumpstart-foundation-models-use-python-sdk-estimator-class.md "jumpstart-foundation-models-use-python-sdk-estimator-class.md")
- [Deploy
  publicly available foundation models with the JumpStartModel
  class](jumpstart-foundation-models-use-python-sdk-model-class.md "jumpstart-foundation-models-use-python-sdk-model-class.md")
- [Deploy
  proprietary foundation models with the ModelPackage
  class](jumpstart-foundation-models-use-python-sdk-proprietary.md "jumpstart-foundation-models-use-python-sdk-proprietary.md")
