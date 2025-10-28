# Create a multi-container endpoint (Boto 3)

Create a Multi-container endpoint by calling [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md"),
[CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md"), and
[CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md")
APIs as you would to create any other endpoints. You can
run these containers sequentially as an inference pipeline, or run each individual
container by using direct invocation. Multi-container endpoints have the following
requirements when you call `create_model`:

- Use the `Containers` parameter instead of
  `PrimaryContainer`, and include more than one container in the
  `Containers` parameter.
- The `ContainerHostname` parameter is required for each
  container in a multi-container endpoint with direct invocation.
- Set the `Mode` parameter of the
  `InferenceExecutionConfig` field to `Direct` for
  direct invocation of each container, or `Serial` to use containers as
  an inference pipeline. The default mode is `Serial`.

###### Note

Currently there is a limit of up to 15 containers supported on a multi-container
endpoint.

The following example creates a multi-container model for direct
invocation.

1. Create container elements and `InferenceExecutionConfig` with
   direct invocation.

```
container1 = {
                 'Image': '123456789012.dkr.ecr.us-east-1.amazonaws.com/myimage1:mytag',
                 'ContainerHostname': 'firstContainer'
             }

container2 = {
                 'Image': '123456789012.dkr.ecr.us-east-1.amazonaws.com/myimage2:mytag',
                 'ContainerHostname': 'secondContainer'
             }
inferenceExecutionConfig = {'Mode': 'Direct'}

```

2. Create the model with the container elements and set the
   `InferenceExecutionConfig` field.

```
import boto3
sm_client = boto3.Session().client('sagemaker')

response = sm_client.create_model(
               ModelName = 'my-direct-mode-model-name',
               InferenceExecutionConfig = inferenceExecutionConfig,
               ExecutionRoleArn = role,
               Containers = [container1, container2]
           )

```

To create an endoint, you would then call [create_endpoint_config](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config") and [create_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint") as you would to create any other endpoint.
