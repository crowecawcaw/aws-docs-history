# Delete a serverless endpoint

You can delete your serverless endpoint using the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home"), the [DeleteEndpoint](../APIReference/API_DeleteEndpoint.md "../APIReference/API_DeleteEndpoint.md") API, or the AWS CLI. The following examples show you how to delete your
endpoint through the API and the SageMaker AI console.

## To delete an endpoint (using API)

The following example uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html") to call the [DeleteEndpoint](../APIReference/API_DeleteEndpoint.md "../APIReference/API_DeleteEndpoint.md") API. For `EndpointName`, use the name of the serverless
endpoint you want to delete.

```
response = client.delete_endpoint(
    EndpointName="`<your-endpoint-name>`",
)
```

## To delete an endpoint (using the

console)

1. Sign in to the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home").
2. In the navigation tab, choose **Inference**.
3. Next, choose **Endpoints**.
4. From the list of endpoints, select the endpoint you want to delete.
5. Choose the **Actions** drop-down list, and then choose
   **Delete**.
6. When prompted again, choose **Delete**.

Your endpoint should now begin the deletion process.
