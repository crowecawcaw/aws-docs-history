# Real-time forecasting

Real-time forecasting is useful when you need to generate predictions on-the-fly, such
as for applications that require immediate responses or when forecasting for individual data
points.

By deploying your AutoML model as a real-time endpoint, you can generate forecasts
on-demand and minimize the latency between receiving new data and obtaining predictions.
This makes real-time forecasting well-suited for applications that require immediate,
personalized, or event-driven forecasting capabilities.

For real time forecasting, the dataset should be a subset of the input dataset. The real
time endpoint has an input data size of approximately 6MB and a response timeout limitation
of 60 seconds. We recommend bringing in one or few items at a time.

You can use SageMaker APIs to retrieve the best candidate of an AutoML job and then create a
SageMaker AI endpoint using that candidate.

Alternatively, you can chose the automatic deployment option when creating your Autopilot
experiment. For information on setting up the automatic deployment of models, see [How to enable automatic
deployment](autopilot-create-experiment-timeseries-forecasting.md#timeseries-forecasting-auto-model-deployment "autopilot-create-experiment-timeseries-forecasting.md#timeseries-forecasting-auto-model-deployment").

###### To create a SageMaker AI endpoint using your best model candidate:

1. ###### Retrieve the details of the AutoML job.

The following AWS CLI command example uses the [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") API to obtain details of the AutoML job, including the
information about the best model candidate.

```
aws sagemaker describe-auto-ml-job-v2 --auto-ml-job-name `job-name` --region `region`
```

2. ###### Extract the container definition from [InferenceContainers](../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers "../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers") for the best model candidate.

A container definition is the containerized environment used to host the trained
SageMaker AI model for making predictions.

```
BEST_CANDIDATE=$(aws sagemaker describe-auto-ml-job-v2 \
  --auto-ml-job-name `job-name`
  --region `region` \
  --query 'BestCandidate.InferenceContainers[0]' \
  --output json
```

This command extracts the container definition for the best model candidate and
stores it in the `BEST_CANDIDATE` variable. 3. ###### Create a SageMaker AI model using the best candidate container definition.

Use the container definitions from the previous steps to create a SageMaker AI model by
using the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md")
API.

```
aws sagemaker create-model \
            --model-name '`your-candidate-name>`' \
            --primary-container "$BEST_CANDIDATE"
            --execution-role-arn '`execution-role-arn>`' \
            --region '`region>`
```

The `--execution-role-arn` parameter specifies the IAM role that SageMaker AI
assumes when using the model for inference. For details on the permissions required for
this role, see CreateModel API: Execution Role Permissions. 4. ###### Create a SageMaker AI endpoint configuration using the model.

The following AWS CLI command uses the [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") API to create an endpoint configuration.

```
aws sagemaker create-endpoint-config \
  --production-variants file://production-variants.json \
  --region '`region`'
```

Where the `production-variants.json` file contains the model
configuration, including the model name and instance type.

###### Note

We recommend using [m5.12xlarge](https://aws.amazon.com/ec2/instance-types/m5/ "https://aws.amazon.com/ec2/instance-types/m5/") instances for real-time forecasting.

```
[
    {
      "VariantName": "`variant-name`",
      "ModelName": "`model-name`",
      "InitialInstanceCount": `1`,
      "InstanceType": "`m5.12xlarge`"
    }
  ]
}
```

5. ###### Create the SageMaker AI endpoint using the endpoint configuration.

The following AWS CLI example uses the [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API
to create the endpoint.

```
aws sagemaker create-endpoint \
            --endpoint-name '`endpoint-name>`' \
            --endpoint-config-name '`endpoint-config-name`' \
            --region '`region`'
```

Check the progress of your real-time inference endpoint deployment by using the
[DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md")
API. See the following AWS CLI command as an example.

```
aws sagemaker describe-endpoint \
            --endpoint-name '`endpoint-name`' \
            --region '`region`'
```

After the `EndpointStatus` changes to `InService`, the
endpoint is ready to use for real-time inference. 6. ###### Invoke the SageMaker AI endpoint to make predictions.

```
aws sagemaker invoke-endpoint \
            --endpoint-name '`endpoint-name`' \
            --region '`region`' \
            --body file://input-data-in-bytes.json \
            --content-type '`application/json`' `outfile`
```

Where the `input-data-in-bytes.json` file contains the input data for the
prediction.
