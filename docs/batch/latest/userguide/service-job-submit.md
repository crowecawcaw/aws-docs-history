# Submit a service job in AWS Batch

To submit service jobs to AWS Batch, you use the [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") API. You can submit jobs using the AWS CLI or SDK.

If you don't already have an execution role then you must create one before you can submit your service job. To create the SageMaker AI execution role, see [How to use SageMaker AI execution
roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md") in the _[SageMaker AI Developer
guide](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md")_.

## Service job submission workflow

When you submit a service job, AWS Batch follows this workflow:

1. AWS Batch receives your `SubmitServiceJob` request and validates the AWS Batch-specific parameters. The `serviceRequestPayload` is passed through without validation.
2. The job enters the `SUBMITTED` state and is placed in the specified job queue
3. AWS Batch evaluates if there is available capacity in the service environment
   for `RUNNABLE` jobs at the front of the queue
4. If capacity is available, the job moves to `SCHEDULED` and the job
   has been passed to SageMaker AI
5. When capacity has been acquired and SageMaker AI has downloaded the service job data, the service job will start initialization and the job is changed to `STARTING`.
6. When SageMaker AI starts to execute the job its status is changed to `RUNNING`.
7. While SageMaker AI executes the job, AWS Batch monitors its progress and maps service
   states to AWS Batch job states. For details about how service job states are
   mapped, see [Mapping AWS Batch service job status to SageMaker AI
   status](service-job-status.md "service-job-status.md")
8. When the service job is completed it moves to `SUCCEEDED` and any output is ready to be downloaded.

## Prerequisites

Before submitting a service job, ensure you have:

- **Service environment** – A service environment
  that defines capacity limits. For more information, see [Create a service environment in
  AWS Batch](create-service-environments.md "create-service-environments.md").
- **SageMaker job queue** – A SageMaker job queue
  to provide job scheduling. For more information, see [Create a SageMaker Training job queue in AWS Batch](create-sagemaker-job-queue.md "create-sagemaker-job-queue.md").
- **IAM permissions** – Permissions to create and manage AWS Batch
  job queues and service environments. For more information, see
  [AWS Batch IAM policies, roles, and permissions](IAM_policies.md "IAM_policies.md").

## Submit a service job with the AWS CLI

The following shows how to submit a service job using the AWS CLI:

```
aws batch submit-service-job \
    --job-name "my-sagemaker-training-job" \
    --job-queue "my-sagemaker-job-queue" \
    --service-job-type "SAGEMAKER_TRAINING" \
    --service-request-payload '{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\":  [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}'
    --client-token "unique-token-12345"
```

For more information about the `serviceRequestPayload` parameters, see [Service job payloads in AWS Batch](service-job-payload.md "service-job-payload.md").
