

# Deploy publicly available foundation models with the `JumpStartModel` class
<a name="jumpstart-foundation-models-use-python-sdk-model-class"></a>

You can deploy a built-in algorithm or pre-trained model to a SageMaker AI endpoint in just a few lines of code using the SageMaker Python SDK.

1. First, find the model ID for the model of your choice in the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html).

1. Using the model ID, define your model as a JumpStart model.

   ```
   from sagemaker.serve import ModelBuilder
   from sagemaker.core.jumpstart.configs import JumpStartConfig
   
   jumpstart_config = JumpStartConfig(model_id={{"huggingface-text2text-flan-t5-xl"}})
   model_builder = ModelBuilder.from_jumpstart_config(jumpstart_config=jumpstart_config)
   ```

1. Use the `deploy` method to automatically deploy your model for inference. In this example, we use the FLAN-T5 XL model from Hugging Face.

   ```
   model = model_builder.build()
   endpoint = model_builder.deploy()
   ```

1. You can then run inference with the deployed model using the `predict` method.

   ```
   question = {{"What is Southern California often abbreviated as?"}}
   response = predictor.predict(question)
   print(response)
   ```

**Note**  
This example uses the foundation model FLAN-T5 XL, which is suitable for a wide range of text generation use cases including question answering, summarization, chatbot creation, and more. For more information about model use cases, see [Available foundation models](jumpstart-foundation-models-latest.md).

For more information about the `JumpStartModel `class and its parameters, see [JumpStartModel](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.jumpstart.model.JumpStartModel).

## Check default instance types
<a name="jumpstart-foundation-models-use-python-sdk-model-class-instance-types"></a>

You can optionally include specific model versions or instance types when deploying a pre-trained model using the `JumpStartModel` class. All JumpStart models have a default instance type. Retrieve the default deployment instance type using the following code:

```
from sagemaker.core import instance_types

instance_type = instance_types.retrieve_default(
    model_id=model_id,
    model_version=model_version,
    scope={{"inference"}})
print(instance_type)
```

See all supported instance types for a given JumpStart model with the `instance_types.retrieve()` method.

## Use inference components to deploy multiple models to a shared endpoint
<a name="jumpstart-foundation-models-use-python-sdk-model-class-endpoint-types"></a>

An inference component is a SageMaker AI hosting object that you can use to deploy one or more models to an endpoint for increased flexibility and scalability. You must change the `endpoint_type` for your JumpStart model to be inference-component-based rather than the default model-based endpoint. 

```
predictor = my_model.deploy(
    endpoint_name = {{'jumpstart-model-id-123456789012'}}, 
    endpoint_type = {{EndpointType.INFERENCE_COMPONENT_BASED}}
)
```

For more information on creating endpoints with inference components and deploying SageMaker AI models, see [Shared resource utilization with multiple models](realtime-endpoints-deploy-models.md#deployed-shared-utilization).

## Check valid input and output inference formats
<a name="jumpstart-foundation-models-use-python-sdk-model-class-input-output"></a>

To check valid data input and output formats for inference, you can use the `retrieve_options()` method from the `Serializers` and `Deserializers` classes.

```
from sagemaker.core.serializers.implementations import retrieve_options as retrieve_serializer_options
from sagemaker.core.deserializers.implementations import retrieve_options as retrieve_deserializer_options

print(retrieve_serializer_options(model_id=model_id, model_version=model_version))
print(retrieve_deserializer_options(model_id=model_id, model_version=model_version))
```

## Check supported content and accept types
<a name="jumpstart-foundation-models-use-python-sdk-model-class-content-types"></a>

Similarly, you can use the `retrieve_options()` method to check the supported content and accept types for a model.

```
from sagemaker.core import content_types, accept_types

print(content_types.retrieve_options(model_id=model_id, model_version=model_version))
print(accept_types.retrieve_options(model_id=model_id, model_version=model_version))
```

For more information about utilities, see [Utility APIs](https://sagemaker.readthedocs.io/en/stable/api/utility/index.html).