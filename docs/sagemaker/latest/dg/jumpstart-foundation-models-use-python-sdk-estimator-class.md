

# Fine-tune publicly available foundation models with the `JumpStartEstimator` class
<a name="jumpstart-foundation-models-use-python-sdk-estimator-class"></a>

**Note**  
For instructions on fine-tuning foundation models in a private curated hub, see [Fine-tune curated hub models](jumpstart-curated-hubs-fine-tune.md).

You can fine-tune a built-in algorithm or pre-trained model in just a few lines of code using the SageMaker Python SDK.

1. First, find the model ID for the model of your choice in the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html). 

1. Using the model ID, define your training job with a JumpStart `ModelTrainer`.

   ```
   from sagemaker.train import ModelTrainer
   from sagemaker.core.jumpstart.configs import JumpStartConfig
   
   jumpstart_config = JumpStartConfig(model_id={{"huggingface-textgeneration1-gpt-j-6b"}})
   model_trainer = ModelTrainer.from_jumpstart_config(jumpstart_config=jumpstart_config)
   ```

1. Call the `train()` method on your `ModelTrainer`, pointing to the training data to use for fine-tuning.

   ```
   from sagemaker.train.configs import InputData
   
   model_trainer.train(
       input_data_config=[
           InputData(channel_name="train", data_source={{training_dataset_s3_path}}),
           InputData(channel_name="validation", data_source={{validation_dataset_s3_path}}),
       ]
   )
   ```

1. Then, use the `deploy` method to automatically deploy your model for inference. In this example, we use the GPT-J 6B model from Hugging Face.

   ```
   from sagemaker.serve import ModelBuilder
   
   model_builder = ModelBuilder.from_jumpstart_config(jumpstart_config=jumpstart_config)
   model = model_builder.build()
   endpoint = model_builder.deploy()
   ```

1. You can then run inference with the deployed model using the `predict` method.

   ```
   question = {{"What is Southern California often abbreviated as?"}}
   response = endpoint.invoke(body=question, content_type="text/plain")
   print(response.body.read().decode('utf-8'))
   ```

**Note**  
This example uses the foundation model GPT-J 6B, which is suitable for a wide range of text generation use cases including question answering, named entity recognition, summarization, and more. For more information about model use cases, see [Available foundation models](jumpstart-foundation-models-latest.md).

You can optionally specify model versions or instance types when creating your `JumpStartEstimator`. For more information about the `JumpStartEstimator `class and its parameters, see [JumpStartEstimator](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.estimator.JumpStartEstimator).

## Check default instance types
<a name="jumpstart-foundation-models-use-python-sdk-estimator-class-instance-types"></a>

You can optionally include specific model versions or instance types when fine-tuning a pre-trained model using the `JumpStartEstimator` class. All JumpStart models have a default instance type. Retrieve the default training instance type using the following code:

```
from sagemaker.core import instance_types

instance_type = instance_types.retrieve_default(
    model_id=model_id,
    model_version=model_version,
    scope={{"training"}})
print(instance_type)
```

You can see all supported instance types for a given JumpStart model with the `instance_types.retrieve()` method.

## Check default hyperparameters
<a name="jumpstart-foundation-models-use-python-sdk-estimator-class-hyperparameters"></a>

To check the default hyperparameters used for training, you can use the `retrieve_default()` method from the `hyperparameters` class.

```
from sagemaker.core import hyperparameters

my_hyperparameters = hyperparameters.retrieve_default(model_id=model_id, model_version=model_version)
print(my_hyperparameters)

# Optionally override default hyperparameters for fine-tuning
my_hyperparameters["epoch"] = "3"
my_hyperparameters["per_device_train_batch_size"] = "4"

# Optionally validate hyperparameters for the model
hyperparameters.validate(model_id=model_id, model_version=model_version, hyperparameters=my_hyperparameters)
```

For more information on available hyperparameters, see [Commonly supported fine-tuning hyperparameters](jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters).

## Check default metric definitions
<a name="jumpstart-foundation-models-use-python-sdk-estimator-class-metric-definitions"></a>

You can also check the default metric definitions:

```
from sagemaker.core import metric_definitions

print(metric_definitions.retrieve_default(model_id=model_id, model_version=model_version))
```