

# Preemption
<a name="preemption"></a>

Quota management is the only AWS Batch scheduling algorithm to incorporate **preemption**, where AWS Batch stops a `SCHEDULED`, `STARTING`, or `RUNNING` job to create capacity for a `RUNNABLE` job.

## Cross-share preemption
<a name="cross-share-preemption"></a>

Quota management uses **cross-share preemption** to restore borrowed capacity back to a quota share when jobs arrive.

Administrators lowering a quota share's capacity limits can also make `SCHEDULED`, `STARTING`, or `RUNNING` jobs within that quota share eligible for preemption, if the capacity consumed by that quota share is now above its configured capacity limits.

## In-share preemption
<a name="in-share-preemption"></a>

Quota shares can be configured to enable **in-share preemption**, which allows higher priority `RUNNABLE` jobs to trigger preemptions of lower priority jobs within the same quota share that have entered `SCHEDULED`, `STARTING`, or `RUNNING`.

## Preemption selection algorithm
<a name="preemption-selection-algorithm"></a>

When choosing which jobs to preempt, AWS Batch considers the number and type of instances a job is borrowing, relative priorities of the jobs and the duration of the jobs, and applies a custom heuristic. You can use the [UpdateServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateServiceJob.html) API call to update the `schedulingPriority` of a job after submission. This can be useful to either lower the priority of a `RUNNING` job (increasing likelihood of preemption) or raise the priority of a `RUNNABLE` job in a quota share with in-share preemption enabled, making it possible for the job to preempt an already-running job.

## Preemption retries
<a name="preemption-retries"></a>

The default is for preempted jobs to be re-queued as `RUNNABLE` without limit. To limit the number of preemptions a job experiences, set `preemptionRetriesBeforeTermination` on job submission. When `preemptionRetriesBeforeTermination` is set to 0, jobs go to `FAILED` on their first preemption.

A sliding window of recent preemption attempts is stored on the job, and visible via [DescribeServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html).