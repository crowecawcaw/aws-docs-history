# Service job payloads in AWS Batch

When you submit service jobs using [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md"), you
provide two key parameters that define the job: `serviceJobType`, and
`serviceRequestPayload`.

- The `serviceJobType` specifies which AWS service will execute the job. For
  SageMaker Training jobs, this value is `SAGEMAKER_TRAINING`.
- The `serviceRequestPayload` is a JSON-encoded string that contains the complete
  request that would normally be sent directly to the target service. For SageMaker Training jobs,
  this payload contains the same parameters you would use with the SageMaker AI [CreateTrainingJob](../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md "../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md") API.
  For a complete list of all available parameters and their descriptions, see the SageMaker AI
  [CreateTrainingJob](../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md "../../../sagemaker/latest/APIReference/API_CreateTrainingJob.md")
  API reference. All parameters supported by `CreateTrainingJob` can be included in
  your service job payload.

For examples of more training job configurations, see [APIs, CLI, and SDKs](../../../sagemaker/latest/dg/api-and-sdk-reference-overview.md "../../../sagemaker/latest/dg/api-and-sdk-reference-overview.md") in the [SageMaker AI Developer Guide](../../../sagemaker/latest/dg/gs.md "../../../sagemaker/latest/dg/gs.md").

We recommend using the PySDK for service job creation because PySDK has helper classes and
utilities. For an example of using PySDK, see [SageMaker AI examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples") on
GitHub.

## Example service job payload

The following example shows a simple service job payload for a SageMaker Training job that
runs a "hello world" training script:

This payload would be passed as a JSON string to the
`serviceRequestPayload` parameter when calling
`SubmitServiceJob`.

```
{
  "TrainingJobName": "my-simple-training-job",
  "RoleArn": "arn:aws:iam::123456789012:role/SageMakerExecutionRole",
  "AlgorithmSpecification": {
    "TrainingInputMode": "File",
    "TrainingImage": "763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:2.0.0-cpu-py310",
    "ContainerEntrypoint": [
      "echo",
      "hello world"
    ]
  },
  "ResourceConfig": {
    "InstanceType": "ml.c5.xlarge",
    "InstanceCount": 1,
    "VolumeSizeInGB": 1
  },
  "OutputDataConfig": {
    "S3OutputPath": "s3://your-output-bucket/output"
  },
  "StoppingCondition": {
    "MaxRuntimeInSeconds": 30
  }
}
```
