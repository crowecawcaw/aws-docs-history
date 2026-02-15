# Monitor service jobs in an AWS Batch queue

You can monitor the status of jobs in your SageMaker Training job queue using
`list-service-jobs`, and `get-job-queue-snapshot`.

View running jobs in your queue:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status RUNNING
```

View jobs waiting in the queue:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status RUNNABLE
```

View jobs that have been submitted to SageMaker but not yet running:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status SCHEDULED
```

Get a snapshot of jobs at the front of your queue:

```
aws batch get-job-queue-snapshot --job-queue my-sm-training-fifo-jq
```

This command shows the order of upcoming service jobs in your queue.

## Get detailed service job information

Use the [`DescribeServiceJob`](../APIReference/API_DescribeServiceJob.md "../APIReference/API_DescribeServiceJob.md") operation to get comprehensive information about a
specific service job, including its current status, service resource identifiers, and detailed
attempt information.

View detailed information about a specific job:

```
aws batch describe-service-job \
  --job-id `a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d`
```

This command returns comprehensive information about the job, including:

- Job ARN and current status
- Service resource identifiers (such as SageMaker Training job ARN)
- Scheduling priority and retry configuration
- Service request payload containing the original service parameters
- Detailed attempt information with start and stop times
- Status messages from the target service

## Monitor SageMaker Training jobs

When monitoring SageMaker Training jobs through AWS Batch, you can access both AWS Batch job
information and the underlying SageMaker Training job details.

The service resource identifier in the job details contains the SageMaker Training job
ARN:

```
{
  "latestAttempt": {
    "serviceResourceId": {
      "name": "TrainingJobArn",
      "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/my-training-job"
    }
  }
}
```

You can use this ARN to get additional details directly from SageMaker:

```
aws sagemaker describe-training-job \
  --training-job-name `my-training-job`
```

Monitor job progress by checking both AWS Batch status and SageMaker Training job status. The
AWS Batch job status shows the overall job lifecycle, while the SageMaker Training job status provides
service-specific details about the training process.
