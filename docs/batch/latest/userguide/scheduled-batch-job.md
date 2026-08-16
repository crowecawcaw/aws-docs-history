# Tutorial: Create a scheduled AWS Batch job

You can use Amazon EventBridge Scheduler to submit an AWS Batch job on a recurring schedule, such as
every hour, or once at a specific date and time. EventBridge Scheduler invokes the AWS Batch [SubmitJob](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") API operation on the schedule that you define, using an IAM execution
role that grants EventBridge Scheduler permission to submit jobs on your behalf.

This procedure works for all AWS Batch jobs on Amazon ECS, Amazon EKS, and AWS Fargate. You can also use
it to schedule service jobs, such as SageMaker Training jobs, by targeting the [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md") API operation instead.

###### Note

Scheduled rules are a legacy Amazon EventBridge feature. If you have existing scheduled rules that
submit AWS Batch jobs, they will continue to work. For new schedules, we recommend Amazon EventBridge
Scheduler.

###### Important

The resources that you create in this tutorial might result in charges to your AWS
account. A recurring schedule continues to submit jobs, and each submitted job uses compute
resources, until you delete the schedule. When you finish, delete the resources that you
created to stop incurring charges. For more information, see the pricing pages for [Amazon EventBridge](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/") and [AWS Batch](https://aws.amazon.com/batch/pricing/ "https://aws.amazon.com/batch/pricing/").

## Prerequisites

Before you begin, you need the following:

- A job queue and a valid job definition. To create these, see [Getting started with AWS Batch tutorials](Batch_GetStarted.md "Batch_GetStarted.md"). To schedule a service
  job, you need a service environment and a SageMaker job queue instead. To create these, see
  [Getting started with AWS Batch on SageMaker AI](getting-started-sagemaker.md "getting-started-sagemaker.md").
- An IAM execution role that EventBridge Scheduler assumes to call
  `SubmitJob` on your behalf. The role must include a policy that grants the
  `batch:SubmitJob` permission. To schedule a service job, grant the
  `batch:SubmitServiceJob` permission instead. As a security best practice,
  scope the policy to the job queue and job definition that the schedule uses:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "batch:SubmitJob",
      "Resource": [
        "arn:aws:batch:us-east-1:111122223333:job-queue/my-job-queue",
        "arn:aws:batch:us-east-1:111122223333:job-definition/my-job-definition:*"
      ]
    }
  ]
}
```

The role must also have a trust policy that allows the
`scheduler.amazonaws.com` service principal to assume it. For more
information, see [Set up an
execution role](../../../scheduler/latest/UserGuide/setting-up.md#setting-up-execution-role "../../../scheduler/latest/UserGuide/setting-up.md#setting-up-execution-role") in the _Amazon EventBridge Scheduler User
Guide_.

## Step 1: Define the schedule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. From the navigation bar, select the AWS Region to use. Choose the same Region as the
   job queue that you want to submit jobs to.
3. In the navigation pane, under **Scheduler**, choose
   **Schedules**.
4. Choose **Create schedule**.
5. For **Schedule name**, enter a name for your schedule. The name can
   contain up to 64 characters, and can include letters, numbers, hyphens (-), underscores
   (\_), and periods (.). The name must be unique within the schedule group in the selected
   Region.
6. (Optional) For **Description**, enter a description for the
   schedule.
7. For **Schedule group**, keep **default**, or choose a
   schedule group that you have created.
8. For **Occurrence**, choose one of the following:

   - **Recurring schedule** – Runs the job repeatedly. For
     **Schedule type**, choose **Cron-based schedule**
     and enter a cron expression to run the job at a specific time, such as 8:00 a.m. on the
     first Monday of every month, or choose **Rate-based schedule** and
     enter a rate expression to run the job at a regular rate, such as every 10 minutes. For
     more information, see [Schedule types on Amazon EventBridge
     Scheduler](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md") in the _Amazon EventBridge Scheduler User
     Guide_.
   - **One-time schedule** – Runs the job once at the date and time
     that you specify.

9. For **Flexible time window**, choose **Off** to run
   the job exactly on schedule, or choose a time window to allow EventBridge Scheduler to invoke the
   job within that window after the scheduled time.
10. Choose **Next**.

## Step 2: Select the target

1. On the **Select target** page, choose **All APIs**,
   and then search for **Batch**.
2. Choose **AWS Batch**, and then choose the API operation that matches
   your job type:

   - **SubmitJob** – For AWS Batch jobs on Amazon ECS, Amazon EKS, and
     AWS Fargate.
   - **SubmitServiceJob** – For service jobs, such as SageMaker Training
     jobs.

3. For **Input**, provide the request parameters that EventBridge Scheduler
   passes to the API operation as a JSON object.

###### Important

Parameter names in the input JSON must be in PascalCase (for example,
`JobQueue`), not the camelCase shown in the request syntax of the
_AWS Batch API Reference_ (for example,
`jobQueue`).

SubmitJob
The following parameters are required:

    * `JobName` – A name for the submitted job.
    * `JobQueue` – The name or Amazon Resource Name (ARN) of the job queue to submit the
     job to.
    * `JobDefinition` – The job definition to use, specified as the
     name (uses the latest active revision), name and revision
     (`name:revision`), or the full ARN.

For example:

```
{
  "JobName": "my-scheduled-job",
  "JobQueue": "my-job-queue",
  "JobDefinition": "my-job-definition"
}
```

You can also include any other `SubmitJob` request parameter. For
example, to submit an array job with 10 child jobs and retry the job up to 3 times
if it fails:

```
{
  "JobName": "my-scheduled-job",
  "JobQueue": "my-job-queue",
  "JobDefinition": "my-job-definition",
  "ArrayProperties": {
    "Size": 10
  },
  "RetryStrategy": {
    "Attempts": 3
  }
}
```

For all available parameters, see [SubmitJob](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") in the
_AWS Batch API Reference_.

SubmitServiceJob
The following parameters are required:

    * `JobName` – A name for the submitted service job.
    * `JobQueue` – The name or ARN of the SageMaker job queue to submit
     the service job to.
    * `ServiceJobType` – The type of service job. For SageMaker Training
     jobs, specify `SAGEMAKER_TRAINING`.
    * `ServiceRequestPayload` – A JSON-encoded string that contains the
     request that AWS Batch sends to the target service. For more information, see
     [Service job payloads in AWS Batch](service-job-payload.md "service-job-payload.md").

For example:

```
{
  "JobName": "my-scheduled-training-job",
  "JobQueue": "my-sagemaker-job-queue",
  "ServiceJobType": "SAGEMAKER_TRAINING",
  "ServiceRequestPayload": "{\"TrainingJobName\": \"my-training-job\", \"RoleArn\": \"arn:aws:iam::111122223333:role/SageMakerExecutionRole\", \"AlgorithmSpecification\": {\"TrainingImage\": \"763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:2.0.0-cpu-py310\", \"TrainingInputMode\": \"File\"}, \"OutputDataConfig\": {\"S3OutputPath\": \"s3://amzn-s3-demo-bucket/output\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.c5.xlarge\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}, \"StoppingCondition\": {\"MaxRuntimeInSeconds\": 300}}"
}
```

For all available parameters, see [SubmitServiceJob](../APIReference/API_SubmitServiceJob.md "../APIReference/API_SubmitServiceJob.md")
in the _AWS Batch API Reference_. 4. Choose **Next**.

## Step 3: Configure schedule settings

1. (Optional) On the **Settings** page, configure the following:

   - **Schedule state** – Turn the schedule off if you don't want it to
     start running as soon as it's created.
   - **Action after schedule completion** – Choose whether EventBridge
     Scheduler deletes the schedule after its last invocation.
   - **Retry policy** – Configure the maximum age of an unprocessed
     event and the number of times EventBridge Scheduler retries the invocation if it
     fails.
   - **Dead-letter queue (DLQ)** – Choose an Amazon SQS queue to receive
     invocations that can't be delivered to the target.

2. For **Permissions**, choose **Use existing role**,
   and then select the execution role that you created as a prerequisite.
3. Choose **Next**.

## Step 4: Review and create

- Review the schedule details. To make changes to any section, choose
  **Edit** next to that section. When you're finished, choose
  **Create schedule**.

After the schedule runs, you can verify that the job was submitted on the AWS Batch console
**Jobs** page.

## Step 5: Clean up resources

When you no longer need the schedule, delete it to stop submitting jobs and to avoid
incurring charges.

1. In the EventBridge console navigation pane, under **Scheduler**, choose
   **Schedules**.
2. Select the schedule that you created, choose **Delete**, and then
   confirm the deletion.
3. (Optional) If you no longer need the execution role that you created as a
   prerequisite, delete it. For more information, see [Delete an IAM role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in
   the _IAM User Guide_.

###### Note

Deleting the schedule doesn't affect jobs that were already submitted. To stop a job
that is already submitted or running, use the [TerminateJob](../APIReference/API_TerminateJob.md "../APIReference/API_TerminateJob.md") API operation.
To stop a service job, use the [TerminateServiceJob](../APIReference/API_TerminateServiceJob.md "../APIReference/API_TerminateServiceJob.md")
API operation.

For more information about creating schedules, see [Getting started with Amazon EventBridge
Scheduler](../../../scheduler/latest/UserGuide/getting-started.md "../../../scheduler/latest/UserGuide/getting-started.md") in the _Amazon EventBridge Scheduler User Guide_.
