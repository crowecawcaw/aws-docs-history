# Model sources and license

agreements

Amazon SageMaker JumpStart provides access to hundreds of publicly available and proprietary foundation
models from third-party sources and partners. You can explore the JumpStart foundation model
selection directly in the SageMaker AI console, Studio, or Studio Classic.

## Licenses and model

sources

Amazon SageMaker JumpStart provides access to both publicly available and proprietary foundation
models. Foundation models are onboarded and maintained from third-party open source
and proprietary providers. As such, they are released under different licenses as
designated by the model source. Be sure to review the license for any foundation
model that you use. You are responsible for reviewing and complying with any
applicable license terms and making sure they are acceptable for your use case
before downloading or using the content. Some examples of common foundation model
licenses include:

- Alexa Teacher Model
- Apache 2.0
- BigScience Responsible AI License v1.0
- CreativeML Open RAIL++-M license

Similarly, for any proprietary foundation models, be sure to review and comply
with any terms of use and usage guidelines from the model provider. If you have
questions about license information for a specific proprietary model, reach out to
model provider directly. You can find model provider contact information in the
**Support** tab of each model page in AWS Marketplace.

## End-user license

agreements

Some JumpStart foundation models require explicit acceptance of an end-user license
agreement (EULA) before use.

### EULA acceptance

in Amazon SageMaker Studio

You may be prompted to accept an end-user license agreement before
fine-tuning, deploying, or evaluating a JumpStart foundation model in Studio. To
get started with JumpStart foundation models in Studio, see [Use foundation
models in Studio](jumpstart-foundation-models-use-studio-updated.md "jumpstart-foundation-models-use-studio-updated.md").

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

Some JumpStart foundation models require acceptance of an end-user license
agreement before deployment. If this applies to the foundation model that you
choose to use, Studio prompts you with a window containing the EULA
content. You are responsible for reviewing and complying with any applicable
license terms and making sure they are acceptable for your use case before
downloading or using a model.

#### EULA acceptance in Amazon SageMaker Studio Classic

You may be prompted to accept an end-user license agreement before
deploying a JumpStart foundation model or opening a JumpStart foundation model
notebook in Studio Classic. To get started with JumpStart foundation models in
Studio Classic, see [Use foundation models in
Amazon SageMaker Studio Classic](jumpstart-foundation-models-use-studio.md "jumpstart-foundation-models-use-studio.md").

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Some JumpStart foundation models require acceptance of an end-user license
agreement before deployment. If this applies to the foundation model that
you choose to use, Studio Classic prompts you with a window titled
**Review the End User License Agreement (EULA) and Acceptable
Use Policy (AUP) below** after you choose either
**Deploy** or **Open notebook**. You
are responsible for reviewing and complying with any applicable license
terms and making sure they are acceptable for your use case before
downloading or using a model.

### EULA

acceptance with the SageMaker Python SDK

The following sections show you how to explicitly declare EULA acceptance when
deploying or fine-tuning a JumpStart model with the SageMaker Python SDK.
For more information on getting started with JumpStart foundation models using the
SageMaker Python SDK, see [Use foundation models
with the SageMaker Python SDK](jumpstart-foundation-models-use-python-sdk.md "jumpstart-foundation-models-use-python-sdk.md").

Before you begin, make sure that you do the following:

- Upgrade to the latest version of the model that you use.
- Install the latest version of the SageMaker Python
  SDK.

###### Important

To use the following workflow you must have [v2.198.0](https://github.com/aws/sagemaker-python-sdk/releases/tag/v2.198.0 "https://github.com/aws/sagemaker-python-sdk/releases/tag/v2.198.0") or later of the SageMaker Python SDK
installed.

#### EULA acceptance when deploying a JumpStart model

For models that require the acceptance of an end-user license agreement,
you must explicitly declare EULA acceptance when deploying your JumpStart
model.

```
from sagemaker.jumpstart.model import JumpStartModel
model_id = `"meta-textgeneration-llama-2-13b"`
my_model = JumpStartModel(model_id=model_id)

# Declare EULA acceptance when deploying your JumpStart model
predictor = my_model.deploy(accept_eula=`True`)
```

The `accept_eula` value is `None` by default and
must be explicitly redefined as `True` in order to accept the
end-user license agreement. For more information, see [JumpStartModel](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.model.JumpStartModel "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.model.JumpStartModel").

#### EULA acceptance when fine-tuning a JumpStart model

For fine-tuning models that require the acceptance of an end-user license
agreement, you must explicitly declare EULA acceptance when running the
`fit()` method for your JumpStart estimator. After fine-tuning a pre-trained model, the weights of
the original model are changed. Therefore, when you deploy the fine-tuned
model later, you do not need to accept a EULA.

###### Note

The following example sets `accept_eula=False`.
You should manually change the value to `True` in order to accept the EULA.

```
from sagemaker.jumpstart.estimator import JumpStartEstimator
model_id = `"meta-textgeneration-llama-2-13b"`

# Declare EULA acceptance when defining your JumpStart estimator
estimator = JumpStartEstimator(model_id=model_id)
estimator.fit(accept_eula=False,
{"train": training_dataset_s3_path, "validation": validation_dataset_s3_path}
)
```

The `accept_eula` value is `None` by default and
must be explicitly redefined as `"true"` within the `fit()` method in order to
accept the end-user license agreement. For more information, see [JumpStartEstimator](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.jumpstart.estimator.JumpStartEstimator "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.jumpstart.estimator.JumpStartEstimator").

#### EULA acceptance SageMaker Python SDK versions earlier than

2.198.0

###### Important

When using versions earlier than [2.198.0](https://github.com/aws/sagemaker-python-sdk/releases/tag/v2.198.0 "https://github.com/aws/sagemaker-python-sdk/releases/tag/v2.198.0") of the SageMaker Python SDK, you must use
the SageMaker `Predictor` class to accept a model EULA.

After deploying a JumpStart foundation model programmatically using the SageMaker
Python SDK, you can run inference against your deployed
endpoint with the SageMaker `Predictor` class. For models that require the
acceptance of an end-user license agreement, you must explicitly declare
EULA acceptance in your call to the `Predictor` class:

```
predictor.predict(payload, custom_attributes="accept_eula=true")
```

The `accept_eula` value is `false` by default and
must be explicitly redefined as `true` in order to accept the
end-user license agreement. The predictor returns an error if you try to run
inference while `accept_eula` is set to `false`. For
more information on getting started with JumpStart foundation models using the
SageMaker Python SDK, see [Use foundation models
with the SageMaker Python SDK](jumpstart-foundation-models-use-python-sdk.md "jumpstart-foundation-models-use-python-sdk.md").

###### Important

The `custom_attributes` parameter accepts key-value pairs
in the format `"key1=value1;key2=value2"`. If you use the
same key multiple times, the inference server uses the last value
associated with the key. For example, if you pass
`"accept_eula=false;accept_eula=true"` to the
`custom_attributes` parameter, then the inference server
associates the value `true` with the `accept_eula`
key.
