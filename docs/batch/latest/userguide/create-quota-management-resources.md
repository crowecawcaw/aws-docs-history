

# Create quota management resources
<a name="create-quota-management-resources"></a>

Quota management requires specific settings when creating an associated scheduling policy, service environment, and job queue.

## Prerequisites
<a name="quota-management-resources-prerequisites"></a>

Before creating quota management resources, ensure you have:
+ **IAM permissions** – Permissions to create and manage AWS Batch job queues, scheduling policies, and service environments. For more information, see [AWS Batch IAM policies, roles, and permissions](IAM_policies.md).

------
#### [ Configure quota management resources (AWS Batch console) ]

The AWS Batch console provides an integrated workflow for creating all resources necessary for quota management. The quota management job queue creation workflow creates quota management enabled scheduling policies and service environments as well.

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane, choose **Job queues** and then **Create**.

1. For **Orchestration type**, choose **SageMaker Training**.

1. For **Job queue configuration**:

   1. For **Name**, enter the name of the job queue.

   1. For **Priority**, enter a value between 0 and 1000. A job queue with a higher priority is given preference for service environments.

1. For **Scheduling**:

   1. For **Scheduling algorithm**, choose **Quota management**.

   1. For **Scheduling policy ARN**:
      + If a scheduling policy already exists that specifies quota management, select it from the dropdown.
      + Otherwise, choose **Create scheduling policy**.

        1. A sidebar opens to configure the quota management scheduling policy.

        1. Provide a **Name** for the scheduling policy.

        1. Choose **Create**. The **Scheduling policy ARN** field is now populated.

1. For **Service environment** configuration, under **Connected service environment**:
**Note**  
Quota management enabled service environments can only be connected to a single quota management enabled job queue.

   1. If a service environment has already been created that is compatible with quota management and is not yet connected to a quota management-enabled job queue, select it from the dropdown.

   1. Otherwise, choose **Create a service environment**. A sidebar opens to configure the service environment.

      1. Provide a **Name** for the service environment.

      1. Provide at least one capacity limit (and at most 5). For each capacity limit, choose an **Instance type** from the dropdown and a **Maximum number of instances**.

1. (Optional) For **Job state limits**:

   1. For **Misconfiguration**, choose either `SERVICE_ENVIRONMENT_MAX_RESOURCE` and enter the **Maximum runnable time (seconds)**.

   1. For **Capacity**, choose `INSUFFICIENT_INSTANCE_CAPACITY` and enter the **Maximum runnable time (seconds)**.

1. Choose **Create job queue**.

------
#### [ Configure quota management resources (AWS CLI) ]

To configure quota management via the AWS CLI, create a scheduling policy, service environment, and job queue. Both the scheduling policy and service environment must be compatible with quota management and created before creating the job queue.

**Create a scheduling policy**

Use the `create-scheduling-policy` command to create a quota management compatible scheduling policy. Provide a quota share policy during creation:

```
aws batch create-scheduling-policy \
  --name {{my-qm-sagemaker-scheduling-policy}} \
  --quota-share-policy idleResourceAssignmentStrategy="FIFO"
```

Verify the scheduling policy was created successfully:

```
aws batch describe-scheduling-policies \
  --arns {{arn-for-my-qm-sagemaker-scheduling-policy}}
```

**Create a service environment**

Use the `create-service-environment` command to create a quota management enabled service environment. Ensure that the capacity limits use instance types that SageMaker Training jobs accept, such as `ml.g6.xlarge` or `ml.p4d.24xlarge`.

```
aws batch create-service-environment \
  --service-environment-name {{my-qm-sagemaker-service-env}} \
  --service-environment-type SAGEMAKER_TRAINING \
  --capacity-limits capacityUnit={{instance_type}},maxCapacity={{instance_count}}
```

Verify the service environment was created successfully:

```
aws batch describe-service-environments \
  --service-environments {{my-qm-sagemaker-service-env}}
```

**Create a job queue**

Use the `create-job-queue` command to create a quota management enabled job queue. The following criteria must be met:
+ A single `SAGEMAKER_TRAINING` service environment must be provided which is not currently connected to another job queue.
+ The service environment must express capacity limits in terms of instance types, such as `ml.m6i.xlarge`, rather than `NUM_INSTANCES`.
+ A scheduling policy must be connected which contains a `quotaSharePolicy`.
+ The `jobQueueType` must be `SAGEMAKER_TRAINING`.

```
aws batch create-job-queue \
  --job-queue-name {{my-qm-sagemaker-jq}} \
  --job-queue-type SAGEMAKER_TRAINING \
  --priority 1 \
  --service-environment-order order=1,serviceEnvironment={{my-qm-sagemaker-service-env}} \
  --scheduling-policy-arn {{arn-for-my-qm-sagemaker-scheduling-policy}}
```

Verify the job queue was created successfully:

```
aws batch describe-job-queues \
  --job-queues {{my-qm-sagemaker-jq}}
```

Ensure that:
+ The `state` is `ENABLED`
+ The `status` is `VALID`
+ The `statusReason` is `JobQueue Healthy`

------