

# Automatic remediation with `jobStateTimeLimitActions`
<a name="job_stuck_in_runnable_time_limit_actions"></a>

Optionally, you can configure the `jobStateTimeLimitActions` parameter through `[CreateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateJobQueue.html)` and [`UpdateJobQueue`](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateJobQueue.html) API actions.

**Note**  
Currently, for job queues connected to Amazon ECS, Amazon EKS, or Fargate compute environments, the only action you can use with `jobStateLimitActions.action` is to cancel a job.

The `jobStateTimeLimitActions` parameter is used to specify a set of actions that AWS Batch performs on jobs in a specific state. You can set a time threshold in seconds through the `maxTimeSeconds` field.

When a job has been in a `RUNNABLE` state with the defined `statusReason`, AWS Batch performs the action specified after `maxTimeSeconds` have elapsed.

For example, you can set the `jobStateTimeLimitActions` parameter to wait up to 4 hours for any job in the `RUNNABLE` state that is waiting for sufficient capacity to become available. You can do this by setting `statusReason` to `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY` and `maxTimeSeconds` to 14400 before cancelling the job and allowing the next job to advance to the head of the job queue.

The `statusReason` values returned by the `ListJobs` and `DescribeJobs` API actions are the same values you can define for the `jobStateTimeLimitActions.statusReason` parameter. However, not all `statusReason` values support automatic remediation.

The following `statusReason` values support `jobStateTimeLimitActions`:
+ `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`
+ `MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE`
+ `MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT`

The following `statusReason` values do not support `jobStateTimeLimitActions` and require manual investigation:
+ `MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS`
+ `ACTION_REQUIRED`
+ `UNDETERMINED`