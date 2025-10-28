# Create a Model

The following example shows how to create a model using the AWS SDK for Python (Boto3). The first few lines define:

- `sagemaker_client`: A low-level SageMaker AI client object that makes it easy to send and
  receive requests to AWS services.
- `sagemaker_role`: A string variable with the SageMaker AI IAM role Amazon Resource Name
  (ARN).
- `aws_region`: A string variable with the name of your AWS region.

```
import boto3

# Specify your AWS Region
aws_region=`'<aws_region>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Role to give SageMaker permission to access AWS services.
sagemaker_role= "arn:aws:iam::`<account>:role/*`"
```

Next, specify the location of the pre-trained model stored in Amazon S3. In this
example, we use a pre-trained XGBoost model named
`demo-xgboost-model.tar.gz`. The full Amazon S3 URI is stored in a
string variable `model_url`:

```
#Create a variable w/ the model S3 URI
s3_bucket = `'<your-bucket-name>'` # Provide the name of your S3 bucket
bucket_prefix='saved_models'
model_s3_key = f"{bucket_prefix}/demo-xgboost-model.tar.gz"

#Specify S3 bucket w/ model
model_url = f"s3://{s3_bucket}/{model_s3_key}"
```

Specify a primary container. For the primary container, you specify the Docker image
that contains inference code, artifacts (from prior training), and a custom environment
map that the inference code uses when you deploy the model for predictions.

In this example, we specify an XGBoost built-in algorithm container image:

```
from sagemaker import image_uris

# Specify an AWS container image.
container = image_uris.retrieve(region=aws_region, framework='xgboost', version='0.90-1')
```

Create a model in Amazon SageMaker AI with `CreateModel`. Specify the following:

- `ModelName`: A name for your model (in this example it is stored as a string
  variable called `model_name`).
- `ExecutionRoleArn`: The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker AI
  can assume to access model artifacts and Docker images for deployment on ML
  compute instances or for batch transform jobs.
- `PrimaryContainer`: The location of the primary Docker image containing inference
  code, associated artifacts, and custom environment maps that the inference
  code uses when the model is deployed for predictions.

```
model_name = `'<The_name_of_the_model>'`

#Create model
create_model_response = sagemaker_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    PrimaryContainer = {
        'Image': container,
        'ModelDataUrl': model_url,
    })
```

See [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") description in
the SageMaker API Reference Guide for a full list of API parameters.

If you're using a SageMaker AI provided container, you can increase the model server
timeout and payload sizes from the default values to the framework‐supported
maximums by setting environment variables in this step. You might not be able to
leverage the maximum timeout and payload sizes that Asynchronous Inference supports if you don't
explicitly set these variables. The following example shows how you can set the
environment variables for a PyTorch Inference container based on TorchServe.

```
model_name = `'<The_name_of_the_model>'`

#Create model
create_model_response = sagemaker_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    PrimaryContainer = {
        'Image': container,
        'ModelDataUrl': model_url,
        'Environment': {
            'TS_MAX_REQUEST_SIZE': '100000000',
            'TS_MAX_RESPONSE_SIZE': '100000000',
            'TS_DEFAULT_RESPONSE_TIMEOUT': '1000'
        },
    })
```

After you finish creating your endpoint, you should test that you've set the
environment variables correctly by printing them out from your
`inference.py` script. The following table lists the environment
variables for several frameworks that you can set to change the default
values.

| Framework                                      | Environment variables                                                                                            |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| PyTorch 1.8 (based on TorchServe)              | 'TS_MAX_REQUEST_SIZE': '100000000' 'TS_MAX_RESPONSE_SIZE': '100000000' 'TS_DEFAULT_RESPONSE_TIMEOUT': '1000'     |
| PyTorch 1.4 (based on MMS)                     | 'MMS_MAX_REQUEST_SIZE': '1000000000' 'MMS_MAX_RESPONSE_SIZE': '1000000000' 'MMS_DEFAULT_RESPONSE_TIMEOUT': '900' |
| HuggingFace Inference Container (based on MMS) | 'MMS_MAX_REQUEST_SIZE': '2000000000' 'MMS_MAX_RESPONSE_SIZE': '2000000000' 'MMS_DEFAULT_RESPONSE_TIMEOUT': '900' |
