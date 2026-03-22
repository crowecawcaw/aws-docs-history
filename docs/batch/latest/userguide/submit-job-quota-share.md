# Submitting jobs to a quota share

Quota management job queues require that all jobs specify a quota share at job submission.
To submit jobs to a quota share, specify the `quotaShareName` in
[SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md").
A `preemptionConfiguration` can optionally be
supplied to limit the number of preemption attempts before a job attempt enters
`FAILED`. To limit the number of preemptions a job experiences, set
`preemptionRetriesBeforeTermination` within
[ServiceJobPreemptionConfiguration](../APIReference/API_ServiceJobPreemptionConfiguration.md "../APIReference/API_ServiceJobPreemptionConfiguration.md")
on job submission.

## Submit a job using the AWS CLI

The following example uses the **submit-service-job** command to submit a
job to a quota share.

```
aws batch submit-service-job \
    --job-name `"my-sagemaker-training-job"` \
    --job-queue `"my-sagemaker-job-queue"` \
    --service-job-type "SAGEMAKER_TRAINING" \
    --quota-share-name `"my_quota_share"` \
    --timeout-config '{"attemptDurationSeconds":`3600`}' \
    --scheduling-priority `5` \
    --service-request-payload `'{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\": [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}'`"
```
