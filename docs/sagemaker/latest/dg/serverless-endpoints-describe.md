# Describe a serverless endpoint

You might want to retrieve information about your endpoint, including details such as the
endpoint’s ARN, current status, deployment configuration, and failure reasons. You can find
information about your endpoint using the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home"), the [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API, or the AWS CLI.

## To describe an endpoint (using API)

The following example uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#id309 "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#id309") to call the [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API. For `EndpointName`, use the name of the endpoint you
want to check.

```
response = client.describe_endpoint(
    EndpointName="`<your-endpoint-name>`",
)
```

## To describe an endpoint (using the

console)

1. Sign in to the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home").
2. In the navigation tab, choose **Inference**.
3. Next, choose **Endpoints**.
4. From the list of endpoints, choose the endpoint you want to check.

The endpoint page contains the information about your endpoint.
