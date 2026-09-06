

# Jobs stuck in RUNNABLE with undetermined root cause
<a name="job_stuck_in_runnable_undetermined"></a>

AWS Batch has detected a blocked queue but is unable to determine the reason. If none of the specific reasons in the preceding sections match your situation, the root cause may require manual investigation. For common causes and manual troubleshooting steps, see [Common causes of jobs stuck in RUNNABLE without a `statusReason`](job_stuck_in_runnable_common_causes.md).
+ **`statusReason` message while the job is stuck:** `UNDETERMINED - Batch job is blocked, root cause is undetermined.`

Note: You can't configure a programmable action through the `jobStateTimeLimitActions` parameter to resolve this error.

For more information about troubleshooting, see [Why is my AWS Batch job stuck in RUNNABLE on AWS](https://repost.aws/knowledge-center/batch-job-stuck-runnable-status) in *re:Post*.