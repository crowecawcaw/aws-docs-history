# Deploy Autopilot models for real-time inference

After you train your Amazon SageMaker Autopilot models, you can set up an endpoint and obtain predictions
interactively. The following section describes the steps for deploying your model to a SageMaker AI real-time
inference endpoint to get predictions from your model.

## Real-time

inferencing

Real-time inference is ideal for inference workloads where you have real-time,
interactive, low latency requirements. This section shows how you can use real-time
inferencing to obtain predictions interactively from your model.

You can use SageMaker APIs to manually deploy the model that produced the best validation
metric in an Autopilot experiment as follows.

Alternatively, you can chose the automatic deployment option when creating your Autopilot
experiment. For information on setting up the automatic deployment of models, see
`ModelDeployConfig` in the request parameters of `CreateAutoMLJobV2`. This creates an endpoint automatically.

###### Note

To avoid incurring unnecessary charges, you can delete unneeded endpoint and resources
created from model deployment. For information about pricing of instances by Region, see
[Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

1. **Obtain the candidate container definitions**

Obtain the candidate container definitions from [InferenceContainers](../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers "../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers"). A container definition for inference refers to the
containerized environment designed for deploying and running your trained SageMaker AI model to
make predictions.

The following AWS CLI command example uses the [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") API to obtain candidate definitions for the best model
candidate.

```
aws sagemaker describe-auto-ml-job-v2 --auto-ml-job-name `job-name` --region `region`
```

2. **List candidates**

The following AWS CLI command example uses the [ListCandidatesForAutoMLJob](../APIReference/API_ListCandidatesForAutoMLJob.md "../APIReference/API_ListCandidatesForAutoMLJob.md") API to list all model candidates.

```
aws sagemaker list-candidates-for-auto-ml-job --auto-ml-job-name `<job-name>` --region `<region>`
```

3. **Create a SageMaker AI model**

Use the container definitions from the previous steps and a candidate of your choice
to create a SageMaker AI model by using the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API. See
the following AWS CLI command as an example.

```
aws sagemaker create-model --model-name '`<your-candidate-name>`' \
                    --containers ['`<container-definition1`>, `<container-definition2>`, `<container-definition3>`]' \
                    --execution-role-arn '`<execution-role-arn>`' --region '`<region>`
```

4. **Create an endpoint configuration**

The following AWS CLI command example uses the [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") API to create an endpoint configuration.

```
aws sagemaker create-endpoint-config --endpoint-config-name '`<your-endpoint-config-name>`' \
                    --production-variants '`<list-of-production-variants>`' \
                    --region '`<region>`'
```

5. **Create the endpoint**

The following AWS CLI example uses the [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API
to create the endpoint.

```
aws sagemaker create-endpoint --endpoint-name '`<your-endpoint-name>`' \
                    --endpoint-config-name '`<endpoint-config-name-you-just-created>`' \
                    --region '`<region>`'
```

Check the progress of your endpoint deployment by using the [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") API. See the following AWS CLI command as an example.

```
aws sagemaker describe-endpoint —endpoint-name '`<endpoint-name>`' —region `<region>`
```

After the `EndpointStatus` changes to `InService`, the
endpoint is ready to use for real-time inference. 6. **Invoke the endpoint**

The following command structure invokes the endpoint for real-time
inferencing.

```
aws sagemaker invoke-endpoint --endpoint-name '`<endpoint-name>`' \
                  --region '`<region>`' --body '`<your-data>`' [--content-type] '`<content-type>`' `<outfile>`
```
