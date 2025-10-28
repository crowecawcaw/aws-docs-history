# Create a model

To create your model, you must provide the location of your model artifacts and container
image. You can also use a model version from [SageMaker Model Registry](model-registry.md "model-registry.md"). The examples in
the following sections show you how to create a model using the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API, Model
Registry, and the [Amazon SageMaker AI
console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home").

## To create a model (using Model

Registry)

[Model Registry](model-registry.md "model-registry.md") is a feature of SageMaker AI that helps you
catalog and manage versions of your model for use in ML pipelines. To use Model Registry with
Serverless Inference, you must first register a model version in a Model Registry model group. To learn how to
register a model in Model Registry, follow the procedures in [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md") and [Register a Model Version](model-registry-version.md "model-registry-version.md").

The following example requires you to have the ARN of a registered model version and uses
the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html") to call the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API. For Serverless Inference,
Model Registry is currently only supported by the AWS SDK for Python (Boto3). For the example, specify the
following values:

- For `model_name`, enter a name for the model.
- For `sagemaker_role`, you can use the default SageMaker AI-created role or a customized
  SageMaker AI IAM role from Step 4 of the [Complete the prerequisites](serverless-endpoints-prerequisites.md "serverless-endpoints-prerequisites.md") section.
- For `ModelPackageName`, specify the ARN for your model version, which must be registered to a model group in Model Registry.

```
#Setup
import boto3
import sagemaker
region = boto3.Session().region_name
client = boto3.client("sagemaker", region_name=region)

#Role to give SageMaker AI permission to access AWS services.
sagemaker_role = sagemaker.get_execution_role()

#Specify a name for the model
model_name = "`<name-for-model>`"

#Specify a Model Registry model version
container_list = [
    {
        "ModelPackageName": `<model-version-arn>`
     }
 ]

#Create the model
response = client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    container_list
)
```

## To create a model (using API)

The following example uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html") to call the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API. Specify the
following values:

- For `sagemaker_role,` you can use the default SageMaker AI-created role or a customized
  SageMaker AI IAM role from Step 4 of the [Complete the prerequisites](serverless-endpoints-prerequisites.md "serverless-endpoints-prerequisites.md") section.
- For `model_url`, specify the Amazon S3 URI to your model.
- For `container`, retrieve the container you want to use by its Amazon ECR path.
  This example uses a SageMaker AI-provided XGBoost container. If you have not selected a SageMaker AI
  container or brought your own, see Step 6 of the [Complete the prerequisites](serverless-endpoints-prerequisites.md "serverless-endpoints-prerequisites.md") section for more information.
- For `model_name`, enter a name for the model.

```
#Setup
import boto3
import sagemaker
region = boto3.Session().region_name
client = boto3.client("sagemaker", region_name=region)

#Role to give SageMaker AI permission to access AWS services.
sagemaker_role = sagemaker.get_execution_role()

#Get model from S3
model_url = "`s3://amzn-s3-demo-bucket/models/model.tar.gz`"

#Get container image (prebuilt example)
from sagemaker import image_uris
container = image_uris.retrieve("xgboost", region, "0.90-1")

#Create model
model_name = "`<name-for-model>`"

response = client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    Containers = [{
        "Image": container,
        "Mode": "SingleModel",
        "ModelDataUrl": model_url,
    }]
)
```

## To create a model (using the

console)

1. Sign in to the [Amazon SageMaker AI
   console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home").
2. In the navigation tab, choose **Inference**.
3. Next, choose **Models**.
4. Choose **Create model**.
5. For **Model name**, enter a name for the model that is unique to your
   account and AWS Region.
6. For **IAM role**, either select an IAM role you have already
   created (see [Complete the prerequisites](serverless-endpoints-prerequisites.md "serverless-endpoints-prerequisites.md")) or allow SageMaker AI to create one for
   you.
7. In **Container definition 1**, for **Container input
   options**, select **Provide model artifacts and input
   location**.
8. For **Provide model artifacts and inference image options**, select
   **Use a single model**.
9. For **Location of inference code image**, enter an Amazon ECR path to a
   container. The image must either be a SageMaker AI-provided first party image (e.g. TensorFlow, XGBoost)
   or an image that resides in an Amazon ECR repository within the same account in which you are
   creating the endpoint. If you do not have a container, go back to Step 6 of the [Complete the prerequisites](serverless-endpoints-prerequisites.md "serverless-endpoints-prerequisites.md") section for more information.
10. For **Location of model artifacts**, enter the Amazon S3 URI to your ML
    model. For example,
    `s3://amzn-s3-demo-bucket/models/model.tar.gz`.
11. (Optional) For **Tags**, add key-value pairs to create metadata for
    your model.
12. Choose **Create model**.
