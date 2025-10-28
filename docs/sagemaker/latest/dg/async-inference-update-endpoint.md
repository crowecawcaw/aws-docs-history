# Update an Asynchronous Endpoint

Update an asynchronous endpoint with the [`UpdateEndpoint`](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md") API. When you update an endpoint, SageMaker AI
first provisions and switches to the new endpoint configuration you specify before it
deletes the resources that were provisioned in the previous endpoint configuration. Do
not delete an `EndpointConfig` with an endpoint that is live or while the
`UpdateEndpoint` or `CreateEndpoint` operations are being
performed on the endpoint.

```
# The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
endpoint_name=`'<endpoint-name>'`

# The name of the endpoint configuration associated with this endpoint.
endpoint_config_name=`'<endpoint-config-name>'`

sagemaker_client.update_endpoint(
                                EndpointConfigName=endpoint_config_name,
                                EndpointName=endpoint_name
                                )
```

When Amazon SageMaker AI receives the request, it sets the endpoint status to **Updating**. After updating the
asynchronous endpoint, it sets the status to **InService**. To check the status of an endpoint, use the
[`DescribeEndpoint`](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API.
For a full list of parameters you can specify when updating an endpoint, see the
[`UpdateEndpoint`](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md") API.
