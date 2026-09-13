

# Deploy publicly available foundation models with the `ModelBuilder` class
<a name="jumpstart-foundation-models-use-python-sdk-model-class"></a>

You can deploy a built-in algorithm or pre-trained model to a SageMaker AI endpoint in just a few lines of code using the SageMaker Python SDK.

1. First, find the model ID for the model of your choice in [Available foundation models](jumpstart-foundation-models-latest.md).

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

1. You can then run inference with the deployed model using the `invoke` method. Text-generation models like this one accept a JSON request body with an `inputs` key. Serialize the payload with `json.dumps` and set the content type to `application/json`.

   ```
   import json
   
   question = {{"What is Southern California often abbreviated as?"}}
   payload = {"inputs": question, "parameters": {"max_new_tokens": 100}}
   response = endpoint.invoke(body=json.dumps(payload), content_type="application/json")
   print(response.body.read().decode('utf-8'))
   ```

**Note**  
This example uses the foundation model FLAN-T5 XL, which is suitable for a wide range of text generation use cases including question answering, summarization, chatbot creation, and more. For more information about model use cases, see [Available foundation models](jumpstart-foundation-models-latest.md).

For more information about the `ModelBuilder` class and its parameters, see [ModelBuilder](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html#sagemaker.serve.ModelBuilder) in the SageMaker Python SDK documentation on the Read the Docs website.

## Check default instance types
<a name="jumpstart-foundation-models-use-python-sdk-model-class-instance-types"></a>

When deploying a pre-trained model, you can optionally specify a model version on your `JumpStartConfig`. You can also choose an instance type on your `ModelBuilder` (for example, with the `instance_type` parameter). All JumpStart models have a default instance type. Retrieve the default deployment instance type using the following code:

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

An inference component is a SageMaker AI hosting object that you can use to deploy one or more models to an endpoint for increased flexibility and scalability. You must change the `endpoint_type` for your JumpStart model to be inference-component-based rather than the default model-based endpoint. Import `EndpointType` and deploy with the inference-component-based endpoint type:

```
from sagemaker.core.enums import EndpointType

endpoint = model_builder.deploy(
    endpoint_name = {{'jumpstart-model-id-123456789012'}}, 
    endpoint_type = EndpointType.INFERENCE_COMPONENT_BASED
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