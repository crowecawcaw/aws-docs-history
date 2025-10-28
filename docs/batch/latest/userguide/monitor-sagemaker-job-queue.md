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

Get detailed information about a specific service job:

```
aws batch describe-service-job --jobId `job-id`
```
