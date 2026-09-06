

# Create Endpoint
<a name="async-inference-create-endpoint-create-endpoint"></a>

Once you have your model and endpoint configuration, use the [`CreateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) API to create your endpoint. The endpoint name must be unique within an AWS Region in your AWS account. 

The following creates an endpoint using the endpoint configuration specified in the request. Amazon SageMaker AI uses the endpoint to provision resources and deploy models.

```
# The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
endpoint_name = {{'<endpoint-name>'}} 

# The name of the endpoint configuration associated with this endpoint.
endpoint_config_name={{'<endpoint-config-name>'}}

create_endpoint_response = sagemaker_client.create_endpoint(
                                            EndpointName=endpoint_name, 
                                            EndpointConfigName=endpoint_config_name)
```

When you call the `CreateEndpoint` API, Amazon SageMaker Asynchronous Inference sends a test notification to check that you have configured an Amazon SNS topic. Amazon SageMaker Asynchronous Inference also sends test notifications after calls to `UpdateEndpoint` and `UpdateEndpointWeightsAndCapacities`. This lets SageMaker AI check that you have the required permissions. The notification can simply be ignored. The test notification has the following form:

```
{
    "eventVersion":"1.0",
    "eventSource":"aws:sagemaker",
    "eventName":"TestNotification"
}
```