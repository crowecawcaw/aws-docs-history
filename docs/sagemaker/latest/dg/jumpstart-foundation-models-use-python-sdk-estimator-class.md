# Fine-tune publicly available foundation models with the

`JumpStartEstimator` class

###### Note

For instructions on fine-tuning foundation models in a private curated
hub, see [Fine-tune curated hub models](jumpstart-curated-hubs-fine-tune.md "jumpstart-curated-hubs-fine-tune.md").

You can fine-tune a built-in algorithm or pre-trained model in just a few
lines of code using the SageMaker Python SDK.

1. First, find the model ID for the model of your choice in the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html").
2. Using the model ID, define your training job as a JumpStart
   estimator.

```
from sagemaker.jumpstart.estimator import JumpStartEstimator

model_id = `"huggingface-textgeneration1-gpt-j-6b"`
estimator = JumpStartEstimator(model_id=model_id)
```

3. Run `estimator.fit()` on your model, pointing to the
   training data to use for fine-tuning.

```
estimator.fit(
    {"train": `training_dataset_s3_path`, "validation": `validation_dataset_s3_path`}
)
```

4. Then, use the `deploy` method to automatically deploy your
   model for inference. In this example, we use the GPT-J 6B model from
   Hugging Face.

```
predictor = estimator.deploy()
```

5. You can then run inference with the deployed model using the
   `predict` method.

```
question = `"What is Southern California often abbreviated as?"`
response = predictor.predict(question)
print(response)
```

###### Note

This example uses the foundation model GPT-J 6B, which is suitable for a
wide range of text generation use cases including question answering, named
entity recognition, summarization, and more. For more information about
model use cases, see [Available foundation models](jumpstart-foundation-models-latest.md "jumpstart-foundation-models-latest.md").

You can optionally specify model versions or instance types when creating your
`JumpStartEstimator`. For more information about the
`JumpStartEstimator` class and its parameters, see [JumpStartEstimator](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.estimator.JumpStartEstimator "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.estimator.JumpStartEstimator").

## Check default instance types

You can optionally include specific model versions or instance types when
fine-tuning a pre-trained model using the `JumpStartEstimator`
class. All JumpStart models have a default instance type. Retrieve the default
training instance type using the following code:

```
from sagemaker import instance_types

instance_type = instance_types.retrieve_default(
    model_id=model_id,
    model_version=model_version,
    scope=`"training"`)
print(instance_type)
```

You can see all supported instance types for a given JumpStart model with the
`instance_types.retrieve()` method.

## Check default hyperparameters

To check the default hyperparameters used for training, you can use the
`retrieve_default()` method from the
`hyperparameters` class.

```
from sagemaker import hyperparameters

my_hyperparameters = hyperparameters.retrieve_default(model_id=model_id, model_version=model_version)
print(my_hyperparameters)

# Optionally override default hyperparameters for fine-tuning
my_hyperparameters["epoch"] = "3"
my_hyperparameters["per_device_train_batch_size"] = "4"

# Optionally validate hyperparameters for the model
hyperparameters.validate(model_id=model_id, model_version=model_version, hyperparameters=my_hyperparameters)
```

For more information on available hyperparameters, see [Commonly supported fine-tuning hyperparameters](jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters "jumpstart-foundation-models-fine-tuning.md#jumpstart-foundation-models-fine-tuning-hyperparameters").

## Check default metric definitions

You can also check the default metric definitions:

```
print(metric_definitions.retrieve_default(model_id=model_id, model_version=model_version))
```
