

# Automatic remediation with `jobStateTimeLimitActions`
<a name="sm_job_stuck_in_runnable_time_limit_actions"></a>

You can configure the `jobStateTimeLimitActions` parameter through `[CreateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateJobQueue.html)` and [`UpdateJobQueue`](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateJobQueue.html) API actions. The `jobStateTimeLimitActions` parameter specifies a set of actions that AWS Batch performs on jobs in a specific state. You can set a time threshold in seconds through the `maxTimeSeconds` field.

For job queues connected to `SAGEMAKER_TRAINING` service environments, the only action you can use with `jobStateTimeLimitActions.action` is `TERMINATE`, which will terminate a job.

For example, you can set the `jobStateTimeLimitActions` parameter to wait up to 4 hours for any job in the `RUNNABLE` state that is waiting for sufficient capacity to become available. You can do this by setting `reason` to `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY` and `maxTimeSeconds` to 14400 before terminating the job and allowing the next job to advance to the head of the job queue.

The following `reason` values support `jobStateTimeLimitActions`:
+ `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`
+ `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`
+ `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`