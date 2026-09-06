

# Track service job capacity utilization
<a name="track-capacity-utilization-service-jobs"></a>

AWS Batch provides multiple API operations that you can use together to track capacity utilization for service jobs in a queue. The monitoring workflow depends on the type of scheduling policy that is attached to your job queue.

For job queues that use a *first-in, first-out (FIFO)* scheduling policy:

1. Check total queue utilization (`GetJobQueueSnapshot`).

1. List jobs by status, such as `SCHEDULED` and `RUNNING` (`ListServiceJobs`).

1. Examine any given job (`DescribeServiceJob`).

For job queues that use a *fair-share (FSS)* or *quota-management (QM)* scheduling policy:

1. Check total queue utilization (`GetJobQueueSnapshot`).

1. View per-share utilization (`GetJobQueueSnapshot`).

1. List jobs by status and share that are actively contributing to utilization, such as `SCHEDULED` and `RUNNING` (`ListServiceJobs`).

1. Examine any given job (`DescribeServiceJob`).

The following sections walk through each step in detail.

For information about tracking capacity utilization for ECS, EKS, and Fargate compute jobs, see [Track compute job capacity utilization](track-capacity-utilization-compute-jobs.md).

**Topics**
+ [Check queue utilization](#capacity-utilization-snapshots-service)
+ [View per-share utilization](#share-utilization-monitoring-service)
+ [List service jobs by status and share](#list-service-jobs-by-share)
+ [Examine a specific service job](#examine-service-job)

## Check queue utilization
<a name="capacity-utilization-snapshots-service"></a>

The `queueUtilization` field in the [`GetJobQueueSnapshot`](https://docs.aws.amazon.com/batch/latest/APIReference/API_GetJobQueueSnapshot.html) response provides a point-in-time view of how much compute capacity is consumed by jobs dispatched from a queue. Capacity is measured in instance count for service jobs.

For job queues that use a fair-share or quota-management scheduling policy, the response also includes a per-share breakdown so you can see how capacity is distributed across shares. For more information, see [View per-share utilization](#share-utilization-monitoring-service).

### View capacity utilization (AWS CLI)
<a name="capacity-snapshots-service-cli"></a>

Use the [get-job-queue-snapshot](https://docs.aws.amazon.com/cli/latest/reference/batch/get-job-queue-snapshot.html) command to retrieve a snapshot of the capacity utilization for a job queue.

```
aws batch get-job-queue-snapshot \
    --job-queue {{my-job-queue}}
```

The response varies depending on the scheduling policy that is attached to your job queue. Choose the tab for your scheduling policy type to see an example response.

------
#### [ First-in, first-out (FIFO) ]

The following is an example response for a FIFO job queue. Because a FIFO queue does not use a scheduling policy, the response does not include per-share utilization.

```
{
    "frontOfQueue": {
        "jobs": [],
        "lastUpdatedAt": 1700000000000
    },
    "queueUtilization": {
        "totalCapacityUsage": [
            {
                "capacityUnit": "ml.m5.large",
                "quantity": 9.0
            }
        ],
        "lastUpdatedAt": 1700000000000
    }
}
```

In this example, the queue consumes a total of 9 instances across all dispatched jobs.

------
#### [ Fair-share scheduling (FSS) ]

The following is an example response for a fair-share job queue. The `queueUtilization` object contains a point-in-time snapshot of the total capacity consumed by all dispatched jobs from the queue, along with a per-share breakdown.

```
{
    "frontOfQueue": {
        "jobs": [],
        "lastUpdatedAt": 1700000000000
    },
    "queueUtilization": {
        "totalCapacityUsage": [
            {
                "capacityUnit": "NUM_INSTANCES",
                "quantity": 9.0
            }
        ],
        "fairshareUtilization": {
            "activeShareCount": 2,
            "topCapacityUtilization": [
                {
                    "shareIdentifier": "team-a",
                    "capacityUsage": [
                        {
                            "capacityUnit": "NUM_INSTANCES",
                            "quantity": 5.0
                        }
                    ]
                },
                {
                    "shareIdentifier": "team-b",
                    "capacityUsage": [
                        {
                            "capacityUnit": "NUM_INSTANCES",
                            "quantity": 4.0
                        }
                    ]
                }
            ]
        },
        "lastUpdatedAt": 1700000000000
    }
}
```

In this example, the `totalCapacityUsage` field shows that the queue consumes a total of 9 instances. The `fairshareUtilization` object shows the per-share breakdown. The share `team-a` consumes 5 instances and the share `team-b` consumes 4 instances.

------
#### [ Quota management (QM) ]

The following is an example response for a quota-management job queue. The `queueUtilization` object contains a point-in-time snapshot of the total capacity consumed by all dispatched jobs from the queue, along with a per-quota-share breakdown. The `frontOfQuotaShares` object shows the first `RUNNABLE` job per quota share.

```
{
    "frontOfQueue": {
        "jobs": [],
        "lastUpdatedAt": 1700000000000
    },
    "frontOfQuotaShares": {
        "quotaShares": {
            "team-a-share": [],
            "team-b-share": []
        },
        "lastUpdatedAt": 1700000000000
    },
    "queueUtilization": {
        "totalCapacityUsage": [
            {
                "capacityUnit": "ml.m5.large",
                "quantity": 9.0
            }
        ],
        "quotaShareUtilization": {
            "topCapacityUtilization": [
                {
                    "quotaShareName": "team-a-share",
                    "capacityUsage": [
                        {
                            "capacityUnit": "ml.m5.large",
                            "quantity": 5.0
                        }
                    ]
                },
                {
                    "quotaShareName": "team-b-share",
                    "capacityUsage": [
                        {
                            "capacityUnit": "ml.m5.large",
                            "quantity": 4.0
                        }
                    ]
                }
            ]
        },
        "lastUpdatedAt": 1700000000000
    }
}
```

In this example, the `totalCapacityUsage` field shows that the queue consumes a total of 9 instances. The `quotaShareUtilization` object shows the per-quota-share breakdown. The quota share `team-a-share` consumes 5 instances and the quota share `team-b-share` consumes 4 instances. The `frontOfQuotaShares` object shows the first `RUNNABLE` job for each quota share, along with the earliest time the job reached that position.

------

## View per-share utilization
<a name="share-utilization-monitoring-service"></a>

For job queues with a fair-share or quota-management scheduling policy, the `queueUtilization` response from `GetJobQueueSnapshot` includes a utilization object with a `topCapacityUtilization` array that lists the top active shares by consumption.

This information helps you:
+ Identify which shares consume the most resources.
+ Verify that resources are distributed across shares as expected.
+ Detect shares that may be saturating or under-utilizing their allocation.
+ Determine whether to adjust your scheduling policy configuration.

For more information about fair-share scheduling policies, see [Fair-share scheduling policies](job_scheduling.md).

For more information about quota shares, see [Quota shares](quota-shares.md).

## List service jobs by status and share
<a name="list-service-jobs-by-share"></a>

After you identify the overall queue and per-share utilization, use the [`ListServiceJobs`](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListServiceJobs.html) API operation to find the service jobs that are actively contributing to utilization. You can filter by job status to see jobs that are `RUNNING`, `SCHEDULED`, or in another state. For queues with a fair-share or quota-management scheduling policy, you can also filter by share identifier to narrow results to a specific share.

**Note**  
The `SHARE_IDENTIFIER` and `QUOTA_SHARE_NAME` filters are the only filters that can be combined with the `jobStatus` parameter. When you use other filters, the `jobStatus` parameter is ignored.

### List service jobs (AWS CLI)
<a name="list-service-jobs-by-share-cli"></a>

Use the [list-service-jobs](https://docs.aws.amazon.com/cli/latest/reference/batch/list-service-jobs.html) command with the `--job-status` parameter to filter by status.

View running service jobs in your queue:

```
aws batch list-service-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNING
```

For queues with a fair-share scheduling policy, use the `--filters` parameter with `SHARE_IDENTIFIER` to list jobs for a specific share. For queues with quota-management scheduling policy, use `QUOTA_SHARE_NAME` to list jobs for a specific quota share. This is useful when you identify a share with high capacity consumption and want to see which jobs are responsible.

List only `RUNNING` service jobs for a share from a fair-share queue:

```
aws batch list-service-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNING \
    --filters name=SHARE_IDENTIFIER,values="{{team-a}}"
```

For queues with a quota-management scheduling policy, use the `QUOTA_SHARE_NAME` filter:

```
aws batch list-service-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNING \
    --filters name=QUOTA_SHARE_NAME,values="{{my-quota-share}}"
```

The following is an example response for listing running service jobs filtered by share identifier in a fair-share queue.

```
{
    "jobSummaryList": [
        {
            "jobArn": "arn:aws:batch:us-east-1:123456789012:service-job/a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
            "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
            "jobName": "my-training-job",
            "serviceJobType": "SAGEMAKER_TRAINING",
            "status": "RUNNING",
            "shareIdentifier": "team-a",
            "createdAt": 1700000000000,
            "scheduledAt": 1700000060000,
            "startedAt": 1700000120000,
            "capacityUsage": [
                {
                    "capacityUnit": "ml.m5.large",
                    "quantity": 5.0
                }
            ],
            "latestAttempt": {
                "serviceResourceId": {
                    "name": "TrainingJobArn",
                    "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/my-training-job"
                }
            }
        }
    ]
}
```

In this example, the response includes the `shareIdentifier` field showing the job belongs to the `team-a` share, and the `capacityUsage` array showing that the job consumes 5 `ml.m5.large` instances. The `latestAttempt` object contains the service resource identifier that you can use to get additional details from the target service.

## Examine a specific service job
<a name="examine-service-job"></a>

After you identify a service job of interest, use the [`DescribeServiceJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html) operation to get comprehensive information about the job, including its current status, service resource identifiers, and detailed attempt information.

View detailed information about a specific service job:

```
aws batch describe-service-job \
    --job-id {{a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d}}
```

This command returns comprehensive information about the job, including:
+ Job ARN and current status
+ Service resource identifiers (such as SageMaker Training job ARN)
+ Scheduling priority and retry configuration
+ Service request payload containing the original service parameters
+ Detailed attempt information with start and stop times
+ Status messages from the target service

### Examine underlying SageMaker Training job
<a name="track-sagemaker-training-jobs"></a>

When monitoring SageMaker Training jobs through AWS Batch, you can access both AWS Batch job information and the underlying SageMaker Training job details.

The service resource identifier in the job details contains the SageMaker Training job ARN:

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
    --training-job-name {{my-training-job}}
```

Monitor job progress by checking both AWS Batch status and SageMaker Training job status. The AWS Batch job status shows the overall job lifecycle, while the SageMaker Training job status provides service-specific details about the training process.