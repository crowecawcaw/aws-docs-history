# Create an Endpoint Configuration

Once you have a model, create an endpoint configuration with
[`CreateEndpointConfig`](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md").
Amazon SageMaker AI hosting services uses this configuration to deploy models.
In the configuration, you identify one or more models, created using with
[`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md"), to
deploy the resources that you want Amazon SageMaker AI to provision. Specify the `AsyncInferenceConfig` object and provide an
output Amazon S3 location for `OutputConfig`. You can optionally specify
[Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") topics on which to send
notifications about prediction results. For more information about Amazon SNS topics, see
[Configuring Amazon SNS](../../../sns/latest/dg/sns-configuring.md "../../../sns/latest/dg/sns-configuring.md").

The following example shows how to create an endpoint configuration using AWS SDK for Python (Boto3):

```
import datetime
from time import gmtime, strftime

# Create an endpoint config name. Here we create one based on the date
# so it we can search endpoints based on creation time.
endpoint_config_name = f"XGBoostEndpointConfig-{strftime('%Y-%m-%d-%H-%M-%S', gmtime())}"

# The name of the model that you want to host. This is the name that you specified when creating the model.
model_name=`'<The_name_of_your_model>'`

create_endpoint_config_response = sagemaker_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name, # You will specify this name in a CreateEndpoint request.
    # List of ProductionVariant objects, one for each model that you want to host at this endpoint.
    ProductionVariants=[
        {
            "VariantName": `"variant1"`, # The name of the production variant.
            "ModelName": model_name,
            "InstanceType": `"ml.m5.xlarge"`, # Specify the compute instance type.
            "InitialInstanceCount": `1` # Number of instances to launch initially.
        }
    ],
    AsyncInferenceConfig={
        "OutputConfig": {
            # Location to upload response outputs when no location is provided in the request.
            "S3OutputPath": f"s3://{s3_bucket}/{bucket_prefix}/output"
            # (Optional) specify Amazon SNS topics
            "NotificationConfig": {
                "SuccessTopic": "arn:aws:sns:`aws-region:account-id:topic-name`",
                "ErrorTopic": "arn:aws:sns:`aws-region:account-id:topic-name`",
            }
        },
        "ClientConfig": {
            # (Optional) Specify the max number of inflight invocations per instance
            # If no value is provided, Amazon SageMaker will choose an optimal value for you
            "MaxConcurrentInvocationsPerInstance": 4
        }
    }
)

print(f"Created EndpointConfig: {create_endpoint_config_response['EndpointConfigArn']}")
```

In the aforementioned example, you specify the following keys for
`OutputConfig` for the `AsyncInferenceConfig` field:

- `S3OutputPath`: Location to upload response outputs when no location is provided in the request.
- `NotificationConfig`: (Optional) SNS topics that post notifications to you when an
  inference request is successful (`SuccessTopic`) or if it fails
  (`ErrorTopic`).
  You can also specify the following optional argument for `ClientConfig` in
  the `AsyncInferenceConfig` field:

- `MaxConcurrentInvocationsPerInstance`: (Optional) The maximum number of concurrent
  requests sent by the SageMaker AI client to the model container.
