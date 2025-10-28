# Delete an Asynchronous Endpoint

Delete an asynchronous endpoint in a similar manner to how you would delete a SageMaker AI
hosted endpoint with the [`DeleteEndpoint`](../APIReference/API_DeleteEndpoint.md "../APIReference/API_DeleteEndpoint.md") API. Specify the name of the asynchronous
endpoint you want to delete. When you delete an endpoint, SageMaker AI frees up all of the
resources that were deployed when the endpoint was created. Deleting a model does not
delete model artifacts, inference code, or the IAM role that you specified when
creating the model.

Delete your SageMaker AI model with the
[`DeleteModel`](../APIReference/API_DeleteModel.md "../APIReference/API_DeleteModel.md") API or with the SageMaker AI console.

Boto3

```
import boto3

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=<aws_region>)
sagemaker_client.delete_endpoint(EndpointName='<endpoint-name>')
```

SageMaker AI console

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Expand the **Inference** dropdown list.
3. Select **Endpoints**.
4. Search for endpoint in the **Search endpoints**
   search bar.
5. Select your endpoint.
6. Choose **Delete**.

In addition to deleting the asynchronous endpoint, you might want to clear up other
resources that were used to create the endpoint, such as the Amazon ECR repository (if you
created a custom inference image), the SageMaker AI model, and the asynchronous endpoint
configuration itself.
