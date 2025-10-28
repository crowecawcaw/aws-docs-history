# Deploy a Compiled Model

Using the AWS CLI

You must satisfy the [prerequisites](neo-deployment-hosting-services-prerequisites.md "neo-deployment-hosting-services-prerequisites.md") section if the model was compiled using AWS SDK for Python (Boto3), AWS CLI,
or the Amazon SageMaker AI console. Follow the steps below to create and deploy a SageMaker Neo-compiled
model using the [AWS CLI](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### Topics

- [Deploy the Model](#neo-deploy-cli "#neo-deploy-cli")

## Deploy the Model

After you have satisfied the [prerequisites](neo-deployment-hosting-services-prerequisites.md "neo-deployment-hosting-services-prerequisites.md"), use the `create-model`,
`create-enpoint-config`, and `create-endpoint` AWS CLI
commands. The following steps explain how to use these commands to deploy a model
compiled with Neo:

### Create a

Model

From [Neo Inference Container Images](neo-deployment-hosting-services-container-images.md "neo-deployment-hosting-services-container-images.md"), select the inference image URI and
then use `create-model` API to create a SageMaker AI model. You can do this
with two steps:

1. Create a `create_model.json` file. Within the file, specify
   the name of the model, the image URI, the path to the
   `model.tar.gz` file in your Amazon S3 bucket, and your SageMaker AI
   execution role:

```
{
    "ModelName": `"insert model name"`,
    "PrimaryContainer": {
        "Image": `"insert the ECR Image URI"`,
        "ModelDataUrl": `"insert S3 archive URL"`,
        "Environment": {`"See details below"`}
    },
    "ExecutionRoleArn": `"ARN for AmazonSageMaker-ExecutionRole"`
}
```

If you trained your model using SageMaker AI, specify the following
environment variable:

```
"Environment": {
    "SAGEMAKER_SUBMIT_DIRECTORY" : `"[Full S3 path for *.tar.gz file containing the training script]"`
}
```

If you did not train your model using SageMaker AI, specify the following
environment variables:

MXNet and PyTorch

```
"Environment": {
    "SAGEMAKER_PROGRAM": "inference.py",
    "SAGEMAKER_SUBMIT_DIRECTORY": `"/opt/ml/model/code"`,
    "SAGEMAKER_CONTAINER_LOG_LEVEL": "20",
    "SAGEMAKER_REGION": `"insert your region"`,
    "MMS_DEFAULT_RESPONSE_TIMEOUT": "500"
}
```

TensorFlow

```
"Environment": {
    "SAGEMAKER_PROGRAM": "inference.py",
    "SAGEMAKER_SUBMIT_DIRECTORY": `"/opt/ml/model/code"`,
    "SAGEMAKER_CONTAINER_LOG_LEVEL": "20",
    "SAGEMAKER_REGION": `"insert your region"`
}
```

###### Note

The `AmazonSageMakerFullAccess` and
`AmazonS3ReadOnlyAccess` policies must be
attached to the `AmazonSageMaker-ExecutionRole` IAM
role. 2. Run the following command:

```
aws sagemaker create-model --cli-input-json file://create_model.json
```

For the full syntax of the `create-model` API, see
[`create-model`](../../../cli/latest/reference/sagemaker/create-model.md "../../../cli/latest/reference/sagemaker/create-model.md").

### Create an Endpoint Configuration

After creating a SageMaker AI model, create the endpoint configuration using the
`create-endpoint-config` API. To do this, create a JSON file with
your endpoint configuration specifications. For example, you can use the
following code template and save it as `create_config.json`:

```
{
    "EndpointConfigName": `"<provide your endpoint config name>"`,
    "ProductionVariants": [
        {
            "VariantName": `"<provide your variant name>"`,
            "ModelName": "my-sagemaker-model",
            "InitialInstanceCount": 1,
            "InstanceType": `"<provide your instance type here>"`,
            "InitialVariantWeight": 1.0
        }
    ]
}
```

Now run the following AWS CLI command to create your endpoint configuration:

```
aws sagemaker create-endpoint-config --cli-input-json file://create_config.json
```

For the full syntax of the `create-endpoint-config` API, see
[`create-endpoint-config`](../../../cli/latest/reference/sagemaker/create-endpoint-config.md "../../../cli/latest/reference/sagemaker/create-endpoint-config.md").

### Create

an Endpoint

After you have created your endpoint configuration, create an endpoint using
the `create-endpoint` API:

```
aws sagemaker create-endpoint --endpoint-name `'<provide your endpoint name>'` --endpoint-config-name `'<insert your endpoint config name>'`
```

For the full syntax of the `create-endpoint` API, see [`create-endpoint`](../../../cli/latest/reference/sagemaker/create-endpoint.md "../../../cli/latest/reference/sagemaker/create-endpoint.md").
