# Delete a job queue in AWS Batch

When you no longer need your job queue, you can disable and delete the job
queue.

Delete a job queue (AWS Batch console)

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Job queues** and then choose a
   job queue.
3. Choose **Actions** and then **Disable**.
4. Once the job queue's state is **Disabled**, choose
   **Actions** and then **Delete**.
5. In the modal window choose **Delete job queue**.

Delete a job queue (AWS CLI)

1. Disable the job queue to prevent new job submissions:

```
aws batch update-job-queue \
  --job-queue `my-sm-training-fifo-jq` \
  --state DISABLED
```

2. Wait for any running jobs to complete, then delete the job queue:

```
aws batch delete-job-queue \
  --job-queue `my-sm-training-fifo-jq`
```
