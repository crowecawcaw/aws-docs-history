

# Jobs stuck in a `RUNNABLE` status
<a name="sm_job_stuck_in_runnable"></a>

If AWS Batch detects that you have a `RUNNABLE` job blocking the front of the queue, you'll receive [Service job queue blocked events](batch-service-job-queue-blocked-events.md) from with the reason. The same reason is also updated into the `statusReason` field as a part of `[ListServiceJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListServiceJobs.html)` and `[DescribeServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html)` API calls.

Optionally, you can configure the `jobStateTimeLimitActions` parameter through `[CreateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateJobQueue.html)` and [`UpdateJobQueue`](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateJobQueue.html) API actions. The `jobStateTimeLimitActions` parameter specifies a set of actions that AWS Batch performs on jobs in a specific state. You can set a time threshold in seconds through the `maxTimeSeconds` field.

For job queues connected to `SAGEMAKER_TRAINING` service environments, the only action you can use with `jobStateTimeLimitActions.action` is `TERMINATE`, which will terminate a job.

For example, you can set the `jobStateTimeLimitActions` parameter to wait up to 4 hours for any job in the `RUNNABLE` state that is waiting for sufficient capacity to become available. You can do this by setting `reason` to `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY` and `maxTimeSeconds` to 14400 before terminating the job and allowing the next job to advance to the head of the job queue.

The following sections each describe a distinct type of blocked reason that AWS Batch can infer. Each section includes:
+ The `statusReason` set on `ListServiceJobs` and `DescribeServiceJob` API actions.
+ The `reason` value for `jobStateTimeLimitActions` configuration.
+ The `statusReason` displayed if `jobStateTimeLimitActions` triggers a termination.

**Topics**
+ [Jobs stuck in `RUNNABLE` due to capacity](sm_job_stuck_in_runnable_capacity.md)
+ [Jobs stuck in `RUNNABLE` due to misconfiguration](sm_job_stuck_in_runnable_misconfiguration.md)
+ [Automatic remediation with `jobStateTimeLimitActions`](sm_job_stuck_in_runnable_time_limit_actions.md)