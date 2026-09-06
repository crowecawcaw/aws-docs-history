

# Jobs stuck in RUNNABLE due to capacity
<a name="job_stuck_in_runnable_capacity"></a>

**Insufficient instance capacity**  
All connected compute environments have insufficient capacity errors. When requested, AWS Batch detects Amazon EC2 instances that experience insufficient capacity errors. Manually canceling the job will allow the subsequent job to move to the head of the queue.  
+ **`statusReason` message while the job is stuck:** `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY - Service cannot fulfill the capacity requested for instance type [instanceTypeName]`
+ **`reason` used for `jobStateTimeLimitActions`:** `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`
+ **`statusReason` message after the job is canceled by `jobStateTimeLimitActions`:** `Canceled by JobStateTimeLimit action due to reason: CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`

**Note:**

1. The AWS Batch service role requires `autoscaling:DescribeScalingActivities` permission for this detection to work. If you use the [Using service-linked roles for AWS Batch](using-service-linked-roles.md) service-linked role (SLR) or the [AWS managed policy: **AWSBatchServiceRole** policy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSBatchServiceRolePolicy) managed policy, then you don't need to take any action because their permission policies are updated.

1. If you use the SLR or the managed policy, you must add the `autoscaling:DescribeScalingActivities` and `ec2:DescribeSpotFleetRequestHistory` permissions so that you can receive blocked job queue events and updated job status when in `RUNNABLE`. In addition, AWS Batch needs these permissions to perform `cancellation` actions through the `jobStateTimeLimitActions` parameter even if they are configured on the job queue.

1. In the case of a multi-node parallel (MNP) job, if the attached high-priority, Amazon EC2 compute environment experiences `insufficient capacity` errors, it blocks the queue even if a lower priority compute environment does experience this error.