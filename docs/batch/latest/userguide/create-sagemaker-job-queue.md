# Create a SageMaker Training job queue in AWS Batch

SageMaker Training job queues integrate directly with the
SageMaker AI service to provide serverless job scheduling without requiring you to manage underlying
compute infrastructure.

## Prerequisites

Before creating a SageMaker Training job queue, ensure you have:

- **Service environment** – A service environment
  that defines capacity limits. For more information, see [Create a service environment in
  AWS Batch](create-service-environments.md "create-service-environments.md").
- **IAM permissions** – Permissions to create and manage AWS Batch
  job queues and service environments. For more information, see
  [AWS Batch IAM policies, roles, and permissions](IAM_policies.md "IAM_policies.md").

Create a SageMaker Training job queue (AWS Batch console)1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/"). 2. In the navigation pane, choose **Job queues** and the **Create**. 3. For **Orchestration type**, choose **SageMaker Training**. 4. For **Job queue configuration**:

    1. For **Name**, enter the name of the Job queue.
    2. for **Priority**, enter a value between 0 and 1000. A Job queue with a higher priority is given preference for service environments.
    3. (Optional) For **Scheduling policy Amazon Resource Name (ARN)**, choose an existing
     scheduling policy.
    4. For **Connected service environments**, select a service
     environment from the list to associate with the job queue.

5. (Optional) For **Job state limits**:
   1. For **Misconfiguration**, choose `SERVICE_ENVIRONMENT_MAX_RESOURCE` and enter the **Maximum runnable time (seconds)**.
   2. For **Capacity**, choose `INSUFFICIENT_INSTANCE_CAPACITY` and enter the **Maximum runnable time (seconds)**.

6. Choose **Create job queue**

Create a SageMaker Training job queue (AWS CLI)Use the `create-job-queue` command to create a SageMaker Training job queue.

The following example creates a basic SageMaker Training job queue that uses a
service environment:

```
aws batch create-job-queue \
  --job-queue-name my-sm-training-fifo-jq \
  --job-queue-type SAGEMAKER_TRAINING \
  --priority 1 \
  --service-environment-order order=1,serviceEnvironment=`ExampleServiceEnvironment`
```

Replace `ExampleServiceEnvironment` with the name of
your service environment.

The command returns output similar to the following:

```
{
  "jobQueueName": "my-sm-training-fifo-jq",
  "jobQueueArn": "arn:aws:batch:`region`:`account`:job-queue/my-sm-training-fifo-jq"
}
```

After creating your job queue, verify that it was created successfully and is in a
valid state.

Use the `describe-job-queues` command to view details about your job queue:

```
aws batch describe-job-queues --job-queues my-sm-training-fifo-jq
```

The command returns output similar to the following:

```
{
  "jobQueues": [
    {
      "jobQueueName": "my-sm-training-fifo-jq",
      "jobQueueArn": "arn:aws:batch:`region`:`account`:job-queue/my-sm-training-fifo-jq",
      "state": "ENABLED",
      "status": "VALID",
      "statusReason": "JobQueue Healthy",
      "priority": 1,
      "computeEnvironmentOrder": [],
      "serviceEnvironmentOrder": [
        {
          "order": 1,
          "serviceEnvironment": "arn:aws:batch:`region`:`account`:service-environment/`ExampleServiceEnvironment`"
        }
      ],
      "jobQueueType": "SAGEMAKER_TRAINING",
      "tags": {},
      "jobStateTimeLimitActions": []
    }
  ]
}
```

Ensure that:

- The `state` is `ENABLED`
- The `status` is `VALID`
- The `statusReason` is `JobQueue Healthy`
- The `jobQueueType` is `SAGEMAKER_TRAINING`
- The `serviceEnvironmentOrder` references your service environment
