# View job queue status

After you create a job queue and submit the jobs, it is important to be able to monitor its
progress. You can use the **Job details** page to review, manage, and monitor
your job queue.

## View job queue information

From the AWS Batch console, select **Job queues** in navigation pane and
choose your desired job queue to view its details. On this page, you can review and manage your
job queue and see additional information about the queue’s operations, such as the job queue
snapshot, job state limits, environment order, tags, and the job queue’s JSON code.

### Job queue details

This section provides an overview and maintenance options for the job queue. It is
important to note that you can find the Amazon Resource Name (ARN) in this section.

To find this information through the AWS Command Line Interface, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name, or the
corresponding ARN.

### Job queue snapshot

This section provides a static list of the first 100 `RUNNABLE`jobs that are in
queue. You can use the search field to narrow the list by searching for information from any
column in the results section. The jobs in the snapshot results area are sorted according to the
job queue’s run strategy. For first-in-first-out (FIFO) job queues, the ordering of the jobs is
based on the submission time. For [fair-share
scheduling](fair-share-scheduling.md "fair-share-scheduling.md") job queues, the ordering of the jobs is based on the job priority and share
usage.

Because the results are a snapshot of the job queue, the results list doesn’t automatically
update. To update the list, choose the refresh at the top of the section. Choose the job’s name
hyperlink to navigate to **Job details** and view the job’s status and other
related information.

To find this information through the AWS CLI, use the [`GetJobQueueSnapshot`](../APIReference/API_GetJobQueueSnapshot.md "../APIReference/API_GetJobQueueSnapshot.md") operation along with the job queue name or the
corresponding ARN.

```
aws batch get-job-queue-snapshot --job-queue my-sm-training-fifo-jq
```

### Job state limits

Use this tab to review configuration information about the amount of time that a job can
remain in a `RUNNABLE` state before it’s canceled.

To find this information through the AWS CLI, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name or the
corresponding ARN.

### Environment order

If your job queue runs in multiple environments, this tab provides their order and an
overview.

To find this information through the AWS CLI, use the [`DescribeJobQueues`](../APIReference/API_DescribeJobQueues.md "../APIReference/API_DescribeJobQueues.md") operation along with the job queue name or the
corresponding ARN.

### Tags

Use this tab to review and manage tags that are associated to this job queue.

### JSON

Use this tab to copy the JSON code that’s associated with this job queue. You can then
reuse the JSON for AWS CloudFormation templates and AWS CLI scripts.

## Monitor service jobs

You can monitor the status of service jobs in your job queue using several AWS Batch commands.
Service jobs are jobs that run on AWS services such as SageMaker Training, where AWS Batch provides
scheduling and queuing capabilities while the target service handles job execution.

### List service jobs by status

Use the [`ListServiceJobs`](../APIReference/API_ListServiceJobs.md "../APIReference/API_ListServiceJobs.md")
operation to view service jobs in your queue filtered by status. Service jobs can have the
following statuses:

- `SUBMITTED` - Job has been submitted but not yet processed
- `PENDING` - Job is pending and waiting for resources
- `RUNNABLE` - Job is ready to run and waiting in the queue
- `STARTING` - Job is being started
- `RUNNING` - Job is currently running
- `SCHEDULED` - Job has been submitted to the target service but not yet
  running
- `SUCCEEDED` - Job completed successfully
- `FAILED` - Job failed to complete

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

View all succeeded jobs:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status SUCCEEDED
```

View failed jobs for troubleshooting:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status FAILED
```

### Filter service jobs

You can filter service jobs by name using pattern matching. If a filter value ends with an
asterisk (\*), it matches any job name that begins with the string before the '\*'.

Find jobs with names starting with "training":

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --filters name=JOB_NAME,values=training*
```

Find jobs with specific names:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --filters name=JOB_NAME,values=my-training-job-1,my-training-job-2
```

Combine status and name filters:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --job-status RUNNING \
  --filters name=JOB_NAME,values=production*
```

### Handle large result sets

When you have many service jobs, use pagination to manage the results effectively.

Limit the number of results returned:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --max-results 10
```

Use the next token to get additional results:

```
aws batch list-service-jobs \
  --job-queue `my-sm-training-fifo-jq` \
  --max-results 10 \
  --next-token `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
```

### Get detailed service job information

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

### Monitor SageMaker Training jobs

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

### Terminate service jobs

Use the [`TerminateServiceJob`](../APIReference/API_TerminateServiceJob.md "../APIReference/API_TerminateServiceJob.md") operation to stop a running service job.

Terminate a specific service job:

```
aws batch terminate-service-job \
  --job-id `a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d` \
  --reason "Job terminated by user request"
```

When you terminate a service job, AWS Batch stops the job and notifies the target service.
For SageMaker Training jobs, this will stop the training job in SageMaker AI as well.
