

# How to create an Asynchronous Inference Endpoint
<a name="async-inference-create-endpoint"></a>

Create an asynchronous endpoint the same way you would create an endpoint using SageMaker AI hosting services:
+ Create a model in SageMaker AI with `CreateModel`.
+ Create an endpoint configuration with `CreateEndpointConfig`.
+ Create an HTTPS endpoint with `CreateEndpoint`.

To create an endpoint, you first create a model with [`CreateModel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html), where you point to the model artifact and a Docker registry path (Image). You then create a configuration using [`CreateEndpointConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) where you specify one or more models that were created using the `CreateModel` API to deploy and the resources that you want SageMaker AI to provision. Create your endpoint with [`CreateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) using the endpoint configuration specified in the request. You can update an asynchronous endpoint with the [`UpdateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) API. Send and receive inference requests from the model hosted at the endpoint with `InvokeEndpointAsync`. You can delete your endpoints with the [`DeleteEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html) API.

For a full list of the available SageMaker Images, see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md). See [Containers with custom inference code](your-algorithms-inference-main.md) for information on how to create your Docker image.

**Topics**
+ [Create a Model](async-inference-create-endpoint-create-model.md)
+ [Create an Endpoint Configuration](async-inference-create-endpoint-create-endpoint-config.md)
+ [Create Endpoint](async-inference-create-endpoint-create-endpoint.md)