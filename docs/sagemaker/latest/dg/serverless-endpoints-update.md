

# Update a serverless endpoint
<a name="serverless-endpoints-update"></a>

Before updating your endpoint, create a new endpoint configuration or use an existing endpoint configuration. The endpoint configuration is where you specify the changes for your update. Then, you can update your endpoint with the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/home), the [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) API, or the AWS CLI. The process for updating a serverless endpoint is the same as the process for updating a [real-time endpoint](realtime-endpoints.md). Note that when updating your endpoint, you can experience cold starts when making requests to the endpoint because SageMaker AI must re-initialize your container and model.

You may want to update an on-demand serverless endpoint to a serverless endpoint with provisioned concurrency or adjust the Provisioned Concurrency value for an existing serverless endpoint with provisioned concurrency. For both cases, you will have to create a new serverless endpoint configuration with the desired value for Provisioned Concurrency, and apply `UpdateEndpoint` to the existing serverless endpoint. For more information on creating a new serverless endpoint configuration with Provisioned Concurrency, see [Create an endpoint configuration](serverless-endpoints-create-config.md).

If you want to remove Provisioned Concurrency from a serverless endpoint, you will have to create a new endpoint configuration without specifying any value for Provisioned Concurrency, and then apply `UpdateEndpoint` to the endpoint.

**Note**  
Updating a real-time inference endpoint to either an on-demand serverless endpoint or a serverless endpoint with Provisioned Concurrency is currently not supported.

## Update the endpoint
<a name="serverless-endpoints-update-endpoint"></a>

After creating a new serverless endpoint configuration you can use the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) or the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/) to update an existing serverless endpoint. Examples of how to update your endpoint using the AWS SDK for Python (Boto3) and the SageMaker AI console are outlined in the following sections.

### To update the endpoint (using Boto3)
<a name="serverless-endpoints-update-endpoint-api"></a>

The following example uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to call the [update\_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_endpoint.html) method. Specify at least the following parameters when calling the method:
+ For `EndpointName`, use the name of the endpoint you’re updating.
+ For `EndpointConfigName`, use the name of the endpoint configuration that you want to use for the update.

```
response = client.update_endpoint(
    EndpointName="{{<your-endpoint-name>}}",
    EndpointConfigName="{{<new-endpoint-config>}}",
)
```

### To update the endpoint (using the console)
<a name="serverless-endpoints-update-endpoint-console"></a>

1. Sign in to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. In the navigation tab, choose **Inference**.

1. Next, choose **Endpoints**.

1. From the list of endpoints, select the endpoint you want to update.

1. Choose **Change** in **Endpoint configuration settings** section.

1. For **Change the Endpoint configuration**, choose **Use an existing endpoint configuration**.

1. From the list of endpoint configurations, select the one you want to use for your update.

1. Choose **Select endpoint configuration**.

1. Choose **Update endpoint**.