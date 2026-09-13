

# Model sources and license agreements
<a name="jumpstart-foundation-models-choose"></a>

Amazon SageMaker JumpStart provides access to hundreds of publicly available and proprietary foundation models from third-party sources and partners. You can explore the JumpStart foundation model selection directly in the SageMaker AI console, Studio, or Studio Classic. 

## Licenses and model sources
<a name="jumpstart-foundation-models-choose-source"></a>

Amazon SageMaker JumpStart provides access to both publicly available and proprietary foundation models. Foundation models are onboarded and maintained from third-party open source and proprietary providers. As such, they are released under different licenses as designated by the model source. Be sure to review the license for any foundation model that you use. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using the content. Some examples of common foundation model licenses include:
+ Alexa Teacher Model
+ Apache 2.0
+ BigScience Responsible AI License v1.0
+ CreativeML Open RAIL\+\+-M license

Similarly, for any proprietary foundation models, be sure to review and comply with any terms of use and usage guidelines from the model provider. If you have questions about license information for a specific proprietary model, reach out to model provider directly. You can find model provider contact information in the **Support** tab of each model page in AWS Marketplace.

## End-user license agreements
<a name="jumpstart-foundation-models-choose-eula"></a>

Some JumpStart foundation models require explicit acceptance of an end-user license agreement (EULA) before use. 

### EULA acceptance in Amazon SageMaker Studio
<a name="jumpstart-foundation-models-choose-eula-studio"></a>

You may be prompted to accept an end-user license agreement before fine-tuning, deploying, or evaluating a JumpStart foundation model in Studio. To get started with JumpStart foundation models in Studio, see [Use foundation models in Studio](jumpstart-foundation-models-use-studio-updated.md). 

**Important**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md).

Some JumpStart foundation models require acceptance of an end-user license agreement before deployment. If this applies to the foundation model that you choose to use, Studio prompts you with a window containing the EULA content. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

#### EULA acceptance in Amazon SageMaker Studio Classic
<a name="jumpstart-foundation-models-choose-eula-studio-classic"></a>

You may be prompted to accept an end-user license agreement before deploying a JumpStart foundation model or opening a JumpStart foundation model notebook in Studio Classic. To get started with JumpStart foundation models in Studio Classic, see [Use foundation models in Amazon SageMaker Studio Classic](jumpstart-foundation-models-use-studio.md).

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

Some JumpStart foundation models require acceptance of an end-user license agreement before deployment. If this applies to the foundation model that you choose to use, Studio Classic prompts you with a window titled **Review the End User License Agreement (EULA) and Acceptable Use Policy (AUP) below** after you choose either **Deploy** or **Open notebook**. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

### EULA acceptance with the SageMaker Python SDK
<a name="jumpstart-foundation-models-choose-eula-python-sdk"></a>

The following sections show you how to explicitly declare EULA acceptance when deploying or fine-tuning a JumpStart model with the SageMaker Python SDK. For more information on getting started with JumpStart foundation models using the SageMaker Python SDK, see [Use foundation models with the SageMaker Python SDK](jumpstart-foundation-models-use-python-sdk.md).

Before you begin, make sure that you do the following:
+ Upgrade to the latest version of the model that you use. 
+ Install the latest version of the SageMaker Python SDK.

**Important**  
To use the following workflow you must have version 3.0.0 or later of the SageMaker Python SDK installed. For information about upgrading, see [Use Version 3.x of the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/) on the Read the Docs website.

#### EULA acceptance when deploying a JumpStart model
<a name="jumpstart-foundation-models-choose-eula-python-sdk-deploy"></a>

For models that require the acceptance of an end-user license agreement, you must explicitly declare EULA acceptance when deploying your JumpStart model.

```
from sagemaker.serve import ModelBuilder
from sagemaker.core.jumpstart.configs import JumpStartConfig

# Declare EULA acceptance in your JumpStart configuration
jumpstart_config = JumpStartConfig(
    model_id={{"meta-textgeneration-llama-2-13b"}},
    accept_eula=True,
)
model_builder = ModelBuilder.from_jumpstart_config(jumpstart_config=jumpstart_config)
model = model_builder.build()
endpoint = model_builder.deploy()
```

The `accept_eula` value is `False` by default. To accept the end-user license agreement, explicitly set it to `True`. For more information, see [ModelBuilder](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html#sagemaker.serve.ModelBuilder) in the SageMaker Python SDK documentation on the Read the Docs website.

#### EULA acceptance when fine-tuning a JumpStart model
<a name="jumpstart-foundation-models-choose-eula-python-sdk-fine-tune"></a>

For fine-tuning models that require the acceptance of an end-user license agreement, you must explicitly declare acceptance. Set this on the `JumpStartConfig` that you use to create your `ModelTrainer`. Fine-tuning a pre-trained model changes the weights of the original model. Therefore, when you deploy the fine-tuned model later, you do not need to accept a EULA.

**Note**  
The following example sets `accept_eula=False`. To accept the EULA, you must change the value to `True`.

```
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.core.jumpstart.configs import JumpStartConfig

# Declare EULA acceptance in your JumpStart configuration
jumpstart_config = JumpStartConfig(
    model_id={{"meta-textgeneration-llama-2-13b"}},
    accept_eula=False,
)
model_trainer = ModelTrainer.from_jumpstart_config(jumpstart_config=jumpstart_config)
model_trainer.train(
    input_data_config=[
        InputData(channel_name="train", data_source={{training_dataset_s3_path}}),
        InputData(channel_name="validation", data_source={{validation_dataset_s3_path}}),
    ]
)
```

The `accept_eula` value is `False` by default. To accept the end-user license agreement, explicitly set it to `True` on the `JumpStartConfig`. For more information, see [SageMaker Train](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) in the SageMaker Python SDK documentation on the Read the Docs website.