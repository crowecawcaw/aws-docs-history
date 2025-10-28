# Delete Endpoints and Resources

Delete endpoints to stop incurring charges.

## Delete Endpoint

Delete your endpoint programmatically using AWS SDK for Python (Boto3), with the AWS CLI, or
interactively using the SageMaker AI console.

SageMaker AI frees up all of the resources that were deployed when the endpoint was created.
Deleting an endpoint will not delete the endpoint configuration or the SageMaker AI model. See
[Delete Endpoint
Configuration](#realtime-endpoints-delete-endpoint-config "#realtime-endpoints-delete-endpoint-config") and [Delete Model](#realtime-endpoints-delete-model "#realtime-endpoints-delete-model") for information on how to delete
your endpoint configuration and SageMaker AI model.

AWS SDK for Python (Boto3)
Use the [`DeleteEndpoint`](../APIReference/API_DeleteEndpoint.md "../APIReference/API_DeleteEndpoint.md") API to delete your endpoint.
Specify the name of your endpoint for the `EndpointName`
field.

```
import boto3

# Specify your AWS Region
aws_region=`'<aws_region>'`

# Specify the name of your endpoint
endpoint_name=`'<endpoint_name>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Delete endpoint
sagemaker_client.delete_endpoint(EndpointName=endpoint_name)
```

AWS CLI
Use the [`delete-endpoint`](../../../cli/latest/reference/sagemaker/delete-endpoint.md "../../../cli/latest/reference/sagemaker/delete-endpoint.md") command to delete your
endpoint. Specify the name of your endpoint for the
`endpoint-name` flag.

```
aws sagemaker delete-endpoint --endpoint-name `<endpoint-name>`
```

SageMaker AI Console
Delete your endpoint interactively with the SageMaker AI console.

1. In the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") navigation menu, choose
   **Inference**.
2. Choose **Endpoints** from the drop down menu. A
   list of endpoints created in you AWS account will appear by name,
   Amazon Resource Name (ARN), creation time, status, and a time stamp
   of when the endpoint was last updated.
3. Select the endpoint you want to delete.
4. Select the **Actions** dropdown button in the top
   right corner.
5. Choose **Delete**.

## Delete Endpoint

Configuration

Delete your endpoint configuration programmaticially using AWS SDK for Python (Boto3), with the
AWS CLI, or interactively using the SageMaker AI console. Deleting an endpoint configuration does
not delete endpoints created using this configuration. See [Delete Endpoint](#realtime-endpoints-delete-endpoint "#realtime-endpoints-delete-endpoint") for information on how to
delete your endpoint.

Do not delete an endpoint configuration in use by an endpoint that is live or while
the endpoint is being updated or created. You might lose visibility into the instance
type the endpoint is using if you delete the endpoint configuration of an endpoint that
is active or being created or updated.

AWS SDK for Python (Boto3)
Use the [`DeleteEndpointConfig`](../APIReference/API_DeleteEndpointConfig.md "../APIReference/API_DeleteEndpointConfig.md") API to delete your
endpoint. Specify the name of your endpoint configuration for the
`EndpointConfigName` field.

```
import boto3

# Specify your AWS Region
aws_region=`'<aws_region>'`

# Specify the name of your endpoint configuration
endpoint_config_name=`'<endpoint_name>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Delete endpoint configuration
sagemaker_client.delete_endpoint_config(EndpointConfigName=endpoint_config_name)

```

You can optionally use the [`DescribeEndpointConfig`](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") API to return
information about the name of the your deployed models (production variants)
such as the name of your model and the name of the endpoint configuration
associated with that deployed model. Provide the name of your endpoint for
the `EndpointConfigName` field.

```
# Specify the name of your endpoint
endpoint_name=`'<endpoint_name>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Store DescribeEndpointConfig response into a variable that we can index in the next step.
response = sagemaker_client.describe_endpoint_config(EndpointConfigName=endpoint_name)

# Delete endpoint
endpoint_config_name = response['ProductionVariants'][0]['EndpointConfigName']

# Delete endpoint configuration
sagemaker_client.delete_endpoint_config(EndpointConfigName=endpoint_config_name)

```

For more information about other response elements returned by
`DescribeEndpointConfig`, see [`DescribeEndpointConfig`](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") in the [SageMaker API Reference guide](../APIReference/API_Operations_Amazon_SageMaker_Service.md "../APIReference/API_Operations_Amazon_SageMaker_Service.md").

AWS CLI
Use the [`delete-endpoint-config`](../../../cli/latest/reference/sagemaker/delete-endpoint-config.md "../../../cli/latest/reference/sagemaker/delete-endpoint-config.md") command to delete your
endpoint configuration. Specify the name of your endpoint configuration for
the `endpoint-config-name` flag.

```
aws sagemaker delete-endpoint-config \
                        --endpoint-config-name `<endpoint-config-name>`
```

You can optionally use the [`describe-endpoint-config`](../../../cli/latest/reference/sagemaker/describe-endpoint-config.md "../../../cli/latest/reference/sagemaker/describe-endpoint-config.md") command to return
information about the name of the your deployed models (production variants)
such as the name of your model and the name of the endpoint configuration
associated with that deployed model. Provide the name of your endpoint for
the `endpoint-config-name` flag.

```
aws sagemaker describe-endpoint-config --endpoint-config-name `<endpoint-config-name>`
```

This will return a JSON response. You can copy and paste, use a JSON
parser, or use a tool built for JSON parsing to obtain the endpoint
configuration name associated with that endpoint.

SageMaker AI Console
Delete your endpoint configuration interactively with the SageMaker AI
console.

1. In the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") navigation menu, choose
   **Inference**.
2. Choose **Endpoint configurations** from the
   dropdown menu. A list of endpoint configurations created in you
   AWS account will appear by name, Amazon Resource Name (ARN), and
   creation time.
3. Select the endpoint configuration you want to delete.
4. Select the **Actions** dropdown button in the top
   right corner.
5. Choose **Delete**.

## Delete Model

Delete your SageMaker AI model programmaticially using AWS SDK for Python (Boto3), with the AWS CLI, or
interactively using the SageMaker AI console. Deleting a SageMaker AI model only deletes the model entry
that was created in SageMaker AI. Deleting a model does not delete model artifacts, inference
code, or the IAM role that you specified when creating the model.

AWS SDK for Python (Boto3)
Use the [`DeleteModel`](../APIReference/API_DeleteModel.md "../APIReference/API_DeleteModel.md") API to delete your SageMaker AI model.
Specify the name of your model for the `ModelName` field.

```
import boto3

# Specify your AWS Region
aws_region=`'<aws_region>'`

# Specify the name of your endpoint configuration
model_name=`'<model_name>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Delete model
sagemaker_client.delete_model(ModelName=model_name)

```

You can optionally use the [`DescribeEndpointConfig`](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") API to return
information about the name of the your deployed models (production variants)
such as the name of your model and the name of the endpoint configuration
associated with that deployed model. Provide the name of your endpoint for
the `EndpointConfigName` field.

```
# Specify the name of your endpoint
endpoint_name=`'<endpoint_name>'`

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Store DescribeEndpointConfig response into a variable that we can index in the next step.
response = sagemaker_client.describe_endpoint_config(EndpointConfigName=endpoint_name)

# Delete endpoint
model_name = response['ProductionVariants'][0]['ModelName']
sagemaker_client.delete_model(ModelName=model_name)

```

For more information about other response elements returned by
`DescribeEndpointConfig`, see [`DescribeEndpointConfig`](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") in the [SageMaker API Reference guide](../APIReference/API_Operations_Amazon_SageMaker_Service.md "../APIReference/API_Operations_Amazon_SageMaker_Service.md").

AWS CLI
Use the [`delete-model`](../../../cli/latest/reference/sagemaker/delete-model.md "../../../cli/latest/reference/sagemaker/delete-model.md") command to delete your SageMaker AI
model. Specify the name of your model for the `model-name`
flag.

```
aws sagemaker delete-model \
                        --model-name `<model-name>`
```

You can optionally use the [`describe-endpoint-config`](../../../cli/latest/reference/sagemaker/describe-endpoint-config.md "../../../cli/latest/reference/sagemaker/describe-endpoint-config.md") command to return
information about the name of the your deployed models (production variants)
such as the name of your model and the name of the endpoint configuration
associated with that deployed model. Provide the name of your endpoint for
the `endpoint-config-name` flag.

```
aws sagemaker describe-endpoint-config --endpoint-config-name `<endpoint-config-name>`
```

This will return a JSON response. You can copy and paste, use a JSON
parser, or use a tool built for JSON parsing to obtain the name of the model
associated with that endpoint.

SageMaker AI Console
Delete your SageMaker AI model interactively with the SageMaker AI console.

1. In the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") navigation menu, choose
   **Inference**.
2. Choose **Models** from the dropdown menu. A list
   of models created in you AWS account will appear by name, Amazon
   Resource Name (ARN), and creation time.
3. Select the model you want to delete.
4. Select the **Actions** dropdown button in the top
   right corner.
5. Choose **Delete**.
