

# Jobs stuck in a `RUNNABLE` status
<a name="job_stuck_in_runnable"></a>

Suppose that your compute environment contains compute resources, but your jobs don't progress beyond the `RUNNABLE` status. Then, it's likely that something is preventing the jobs from being placed on a compute resource and causing your job queues to be blocked. Here's how to know if your job is waiting for its turn or stuck and blocking the queue.

If AWS Batch detects that you have a `RUNNABLE` job at the head and blocking the queue, you'll receive a [Job queue blocked events](batch-job-queue-blocked-events.md) event from Amazon CloudWatch Events with the reason. The same reason is also updated into the `statusReason` field as a part of `[ListJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListJobs.html)` and `[DescribeJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html)` API calls.

Specific reasons are inferred by AWS Batch based on the state of connected compute environments and fall into three categories: capacity issues, misconfiguration, and invalid compute environments. Optionally, you can configure the `jobStateTimeLimitActions` parameter on your job queue to automatically cancel jobs that remain stuck in `RUNNABLE` for longer than a specified threshold. If none of the specific reasons in the following sections match your situation, or if your `statusReason` shows `UNDETERMINED`, see [Jobs stuck in RUNNABLE with undetermined root cause](job_stuck_in_runnable_undetermined.md) and [Common causes of jobs stuck in RUNNABLE without a `statusReason`](job_stuck_in_runnable_common_causes.md) for manual troubleshooting steps.

**Topics**
+ [Jobs stuck in RUNNABLE due to capacity](job_stuck_in_runnable_capacity.md)
+ [Jobs stuck in RUNNABLE due to misconfiguration](job_stuck_in_runnable_misconfiguration.md)
+ [Jobs stuck in RUNNABLE due to invalid compute environments](job_stuck_in_runnable_invalid_ce.md)
+ [Jobs stuck in RUNNABLE with undetermined root cause](job_stuck_in_runnable_undetermined.md)
+ [Automatic remediation with `jobStateTimeLimitActions`](job_stuck_in_runnable_time_limit_actions.md)
+ [Common causes of jobs stuck in RUNNABLE without a `statusReason`](job_stuck_in_runnable_common_causes.md)