

# Quota shares
<a name="quota-shares"></a>

**Quota shares** are virtual queues that are nested under a job queue. A maximum of 20 can be attached to any job queue. Quota shares enable allocating a compute quota to a team or project, via the use of **capacity limits**; a quota share requires at least one capacity limit be provided and supports a maximum of 5 capacity limits. Each capacity limit should be expressed as instance limits for supported SageMaker Training job instances types.

## Quota share resource sharing strategy
<a name="quota-share-resource-sharing"></a>

Quota shares also have explicit resource sharing configuration.
+ If a quota share's idle compute should be reserved for only its jobs, select `RESERVE`.
+ If a quota share's idle compute can be lent to other quota shares, select `LEND`.
+ If a quota share's idle compute can be lent to other quota shares, and jobs from the quota share should be allowed to borrow idle compute, select `LEND_AND_BORROW` with a configured borrow limit.

## Capacity restoration via preemption
<a name="capacity-limit-restoration"></a>

AWS Batch will perform **cross-share preemption** to restore borrowed capacity back to a quota share when jobs arrive. When choosing which jobs to preempt, AWS Batch considers the number and type of instances a job is borrowing, relative priorities of the jobs and the duration of the job, and applies a custom heuristic.

Administrators lowering a quota share's capacity limits can also make `SCHEDULED`, `STARTING`, or `RUNNING` jobs within that quota share eligible for preemption even if `LEND` or `RESERVE` was selected as the resource sharing strategy, if the capacity already consumed by that quota share is above its lowered capacity limits.