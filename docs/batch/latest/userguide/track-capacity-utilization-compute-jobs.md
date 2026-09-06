

# Track compute job capacity utilization
<a name="track-capacity-utilization-compute-jobs"></a>

AWS Batch provides multiple API operations that you can use together to track capacity utilization for ECS, EKS, and Fargate compute jobs in a queue. The monitoring workflow depends on the type of scheduling policy that is attached to your job queue.

For job queues that use a *first-in, first-out (FIFO)* scheduling policy:

1. Check total queue utilization (`GetJobQueueSnapshot`).

1. List jobs by status, such as `RUNNABLE` and `RUNNING` (`ListJobs`).

1. Examine any given job (`DescribeJobs`).

For job queues that use a *fair-share (FSS)* scheduling policy:

1. Check total queue utilization (`GetJobQueueSnapshot`).

1. View per-share utilization (`GetJobQueueSnapshot`).

1. List jobs by status and share that are actively contributing to utilization, such as `RUNNABLE` and `RUNNING` (`ListJobs`).

1. Examine any given job (`DescribeJobs`).

The following sections walk through each step in detail.

For information about tracking capacity utilization for service jobs, see [Track service job capacity utilization](track-capacity-utilization-service-jobs.md).

**Topics**
+ [Check queue utilization](#capacity-utilization-snapshots-compute)
+ [View per-share utilization](#share-utilization-monitoring-compute)
+ [List compute jobs by status and share](#list-compute-jobs-by-share)
+ [Examine a specific compute job](#examine-compute-job)

## Check queue utilization
<a name="capacity-utilization-snapshots-compute"></a>

The `queueUtilization` field in the [`GetJobQueueSnapshot`](https://docs.aws.amazon.com/batch/latest/APIReference/API_GetJobQueueSnapshot.html) response provides a point-in-time view of how much compute capacity is consumed by jobs dispatched from a queue. Capacity is measured in vCPUs for compute jobs.

For job queues that use a fair-share scheduling policy, the response also includes a per-share breakdown so you can see how capacity is distributed across shares. For more information, see [View per-share utilization](#share-utilization-monitoring-compute).

### View capacity utilization (AWS CLI)
<a name="capacity-snapshots-compute-cli"></a>

Use the [get-job-queue-snapshot](https://docs.aws.amazon.com/cli/latest/reference/batch/get-job-queue-snapshot.html) command to retrieve a snapshot of the capacity utilization for a job queue.

```
aws batch get-job-queue-snapshot \
    --job-queue {{my-job-queue}}
```

The response varies depending on the scheduling policy that is attached to your job queue. Choose the tab for your scheduling policy type to see an example response.

------
#### [ First-in, first-out (FIFO) ]

The following is an example response for a FIFO job queue running compute jobs. Because a FIFO queue does not use a scheduling policy, the response does not include per-share utilization.

```
{
    "frontOfQueue": {
        "jobs": [],
        "lastUpdatedAt": 1700000000000
    },
    "queueUtilization": {
        "totalCapacityUsage": [
            {
                "capacityUnit": "vCPU",
                "quantity": 96.0
            }
        ],
        "lastUpdatedAt": 1700000000000
    }
}
```

In this example, the queue consumes a total of 96 vCPUs across all dispatched jobs.

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
                "capacityUnit": "vCPU",
                "quantity": 192.0
            }
        ],
        "fairshareUtilization": {
            "activeShareCount": 2,
            "topCapacityUtilization": [
                {
                    "shareIdentifier": "team-a",
                    "capacityUsage": [
                        {
                            "capacityUnit": "vCPU",
                            "quantity": 128.0
                        }
                    ]
                },
                {
                    "shareIdentifier": "team-b",
                    "capacityUsage": [
                        {
                            "capacityUnit": "vCPU",
                            "quantity": 64.0
                        }
                    ]
                }
            ]
        },
        "lastUpdatedAt": 1700000000000
    }
}
```

In this example, the `totalCapacityUsage` field shows that the queue consumes a total of 192 vCPUs. The `fairshareUtilization` object shows the per-share breakdown. The share `team-a` consumes 128 vCPUs and the share `team-b` consumes 64 vCPUs.

------

## View per-share utilization
<a name="share-utilization-monitoring-compute"></a>

For job queues with a fair-share scheduling policy, the `queueUtilization` response from `GetJobQueueSnapshot` includes a `fairshareUtilization` object with a `topCapacityUtilization` array that lists the top active shares by consumption.

This information helps you:
+ Identify which shares consume the most resources.
+ Verify that fair-share scheduling is distributing resources as expected.
+ Detect shares that may be saturating or under-utilizing their allocation.
+ Determine whether to adjust share weights in your scheduling policy.

For more information about fair-share scheduling policies, see [Fair-share scheduling policies](job_scheduling.md).

## List compute jobs by status and share
<a name="list-compute-jobs-by-share"></a>

After you identify the overall queue and per-share utilization, use the [`ListJobs`](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListJobs.html) API operation to find the compute jobs that are actively contributing to utilization. You can filter by job status to see jobs that are `RUNNING`, `RUNNABLE`, or in another state. For queues with a fair-share scheduling policy, you can also filter by share identifier to narrow results to a specific share.

**Note**  
The `SHARE_IDENTIFIER` filter is the only filter that can be combined with the `jobStatus` parameter. When you use other filters, the `jobStatus` parameter is ignored.

### List compute jobs (AWS CLI)
<a name="list-compute-jobs-by-share-cli"></a>

Use the [list-jobs](https://docs.aws.amazon.com/cli/latest/reference/batch/list-jobs.html) command with the `--job-status` parameter to filter by status.

View running compute jobs in your queue:

```
aws batch list-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNING
```

View compute jobs waiting to be dispatched:

```
aws batch list-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNABLE
```

For queues with a fair-share scheduling policy, use the `--filters` parameter with `SHARE_IDENTIFIER` to list jobs for a specific share. This is useful when you identify a share with high capacity consumption and want to see which jobs are responsible.

List only `RUNNING` compute jobs for a share from a fair-share queue:

```
aws batch list-jobs \
    --job-queue {{my-job-queue}} \
    --job-status RUNNING \
    --filters name=SHARE_IDENTIFIER,values="{{team-a}}"
```

The following is an example response for listing running compute jobs.

```
{
    "jobSummaryList": [
        {
            "jobArn": "arn:aws:batch:us-east-1:123456789012:job/b5e7d839-9ff9-5d76-9f3b-0b6f9g5c8e4f",
            "jobId": "b5e7d839-9ff9-5d76-9f3b-0b6f9g5c8e4f",
            "jobName": "my-data-processing-job",
            "status": "RUNNING",
            "shareIdentifier": "team-a",
            "createdAt": 1700000000000,
            "startedAt": 1700000120000,
            "capacityUsage": [
                {
                    "capacityUnit": "vCPU",
                    "quantity": 4.0
                }
            ],
            "container": {
                "exitCode": null
            },
            "jobDefinition": "arn:aws:batch:us-east-1:123456789012:job-definition/my-job-def:1"
        }
    ]
}
```

## Examine a specific compute job
<a name="examine-compute-job"></a>

After you identify a compute job of interest, use the [`DescribeJobs`](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html) operation to get comprehensive information about the job, including its current status, container details, and resource configuration.

View detailed information about a specific compute job:

```
aws batch describe-jobs \
    --jobs {{b5e7d839-9ff9-5d76-9f3b-0b6f9g5c8e4f}}
```

This command returns comprehensive information about the job, including:
+ Job ARN and current status
+ Container configuration and resource requirements (vCPUs and memory)
+ Job definition and compute environment details
+ Scheduling priority and retry configuration
+ Detailed attempt information with start and stop times
+ Log stream information for accessing container logs