# Assigning job priority

You can assign each Amazon S3 Batch Operations job a numeric priority, which can be any
 positive integer. S3 Batch Operations prioritizes jobs according to the assigned
 priority. Jobs with a higher priority (or a higher numeric value for the priority
 parameter) are evaluated first. Priority is determined in descending order. For example,
 a job queue with a priority value of 10 is given scheduling preference over a job queue
 with a priority value of 1. 

You can change a job's priority while the job is running. If you submit a new job with
 a higher priority while a job is running, the lower-priority job can pause to allow the
 higher-priority job to run.

Changing a job's priority doesn't affect the job's processing speed.

###### Note

S3 Batch Operations honors job priorities on a best-effort basis. Although
 jobs with higher priorities generally take precedence over jobs with lower
 priorities, Amazon S3 doesn't guarantee strict ordering of jobs.

###### How to update job priority in the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Batch Operations**.
3. Select the specific job that you would like to manage.
4. Choose **Action**. In the dropdown list, choose **Update priority**.
The following example updates the job priority by using the AWS CLI. A higher
 number indicates a higher execution priority. To use the following example
 command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control update-job-priority \
    --region `us-west-2` \
    --account-id `account-id` \
    --priority `98` \
    --job-id `00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c`
```
To update the priority of an S3 Batch Operations job using the AWS SDK for Java, you can use the S3Control client to modify the job's execution priority, which determines the order in which jobs are processed relative to other jobs in the queue.

For more information about job priority, see [Assigning job priority](batch-ops-job-priority.md "batch-ops-job-priority.md").

For examples of how to update job priority with the AWS SDK for Java, see [Update the priority of a batch job](../API/s3-control_example_s3-control_UpdateJobPriority_section.md "../API/s3-control_example_s3-control_UpdateJobPriority_section.md") in the *Amazon S3 API Reference*.
