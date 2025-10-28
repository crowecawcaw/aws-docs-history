# Fine-tune models with adapter inference

components

With Amazon SageMaker AI, you can host pre-trained foundation models without needing to create your
own models from scratch. However, to tailor a general-purpose foundation model for the
unique needs of your business, you must create a fine-tuned version of it. One
cost-effective fine-tuning technique is Low-Rank Adaptation (LoRA). The principle behind
LoRA is that only a small part of a large foundation model needs updating to adapt it to new
tasks or domains. A LoRA adapter augments the inference from a base foundation model with
just a few extra adapter layers.

If you host your base foundation model by using a SageMaker AI inference component, you can
fine-tune that base model with LoRA adapters by creating _adapter
inference components_. When you create an adapter inference component, you
specify the following:

- The _base inference component_ that is to contain
  the adapter inference component. The base inference component contains the
  foundation model that you want to adapt. The adapter inference component uses the
  compute resources that you assigned to the base inference component.
- The location where you've stored the LoRA adapter in Amazon S3.
  After you create the adapter inference component, you can invoke it directly. When you do,
  SageMaker AI combines the adapter with the base model to augment the generated response.

###### Before you begin

Before you can create an adapter inference component, you must meet the following
requirements:

- You have a base inference component that contains the foundation model to adapt.
  You've deployed this inference component to a SageMaker AI endpoint.

For more information about deploying inference components to endpoints, see [Deploy
models for real-time inference](realtime-endpoints-deploy-models.md "realtime-endpoints-deploy-models.md").

- You have a LoRA adapter model, and you've stored the model artifacts as a
  `tar.gz` file in Amazon S3. You specify the S3 URI of the
  artifacts when you create the adapter inference component.
  The following examples use the SDK for Python (Boto3) to create and invoke an adapter inference
  component.

###### Example `create_inference_component` call to create an adapter inference

component

The following example creates an adapter inference component and assigns it to a base
inference component:

```
sm_client.create_inference_component(
    InferenceComponentName = `adapter_ic_name`,
    EndpointName = `endpoint_name`,
    Specification={
        "BaseInferenceComponentName": `base_inference_component_name`,
        "Container": {
            "ArtifactUrl": `adapter_s3_uri`
        },
    },
)
```

When you use this example in your own code, replace the placeholder values as
follows:

- `adapter_ic_name` – A unique name for your
  adapter inference component.
- `endpoint_name` – The name of the endpoint
  that hosts the base inference component.
- `base_inference_component_name` – The name of
  the base inference component that contains the foundation model to adapt.
- `adapter_s3_uri` – The S3 URI that locates the
  `tar.gz` file with your LoRA adapter artifacts.
  You create an adapter inference component with code that is similar to the code for a
  normal inference component. One difference is that, for the `Specification`
  parameter, you omit the `ComputeResourceRequirements` key. When you invoke an
  adapter inference component, it is loaded by the base inference component. The adapter
  inference component uses the compute resources of the base inference component.

For more information about creating and deploying inference components with the
SDK for Python (Boto3), see [Deploy models with the Python SDKs](realtime-endpoints-deploy-models.md#deploy-models-python "realtime-endpoints-deploy-models.md#deploy-models-python").

After you create an adapter inference component, you invoke it by specifying its name in
an `invoke_endpoint` request.

###### Example `invoke_endpoint` call to invoke an adapter inference component

The following example invokes an adapter inference component:

```
response = sm_rt_client.invoke_endpoint(
    EndpointName = `endpoint_name`,
    InferenceComponentName = `adapter_ic_name`,
    Body = json.dumps(
        {
            "inputs": `prompt`,
            "parameters": {"max_new_tokens": 100, "temperature":0.9}
        }
    ),
    ContentType = "application/json",
)

adapter_reponse = response["Body"].read().decode("utf8")["generated_text"]
```

When you use this example in your own code, replace the placeholder values as
follows:

- `endpoint_name` – The name of the endpoint
  that hosts the base and adapter inference components.
- `adapter_ic_name` – The name of the adapter
  inference component.
- `prompt` – The prompt for the inference
  request.
  For more information about invoking inference components with the SDK for Python (Boto3), see [Invoke models for real-time
  inference](realtime-endpoints-test-endpoints.md "realtime-endpoints-test-endpoints.md").
