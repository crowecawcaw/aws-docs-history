# Control costs and concurrency

On a traditional render farm, fixed infrastructure creates indirect limits on
concurrency and cost. A shared file system's throughput caps how fast workers can access
data. A fixed number of render nodes limits how many jobs run at the same time. These
bottlenecks slow down rendering, but they also prevent unexpected spending.

With AWS Deadline Cloud, you have precise, direct controls over both cost and concurrency. You
can scale rapidly to finish jobs quickly, with budgets that enforce hard dollar caps and
fleet settings that limit peak concurrency. Unlike a traditional farm, you don't need to
trade render speed for cost control—you can have both.

With Deadline Cloud, you can also limit resource usage for other reasons, such as matching a
fixed number of software licenses. The following mechanisms each operate at a different
level. You can combine them to match your organization's requirements.

## Comparison of cost and concurrency controls

The following table summarizes the controls available in Deadline Cloud. Choose one or more
based on what you want to limit.

| Control                    | Level         | What it does                                                                                                                                 | Best for                                                                                                                                                  |
| -------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fleet maximum worker count | Fleet         | Caps the total number of workers that can run simultaneously in<br>a fleet, regardless of how many jobs are queued.                          | Hard cap on peak compute across all jobs in a fleet. Replaces<br>the natural limit of a fixed number of render nodes.                                     |
| Job maximum worker count   | Job           | Caps the number of workers assigned to a single job. Other<br>workers in the fleet remain available for other jobs.                          | Preventing a single large job from consuming the entire fleet<br>while smaller jobs wait.                                                                 |
| Resource limits            | Farm or queue | Caps the number of tasks that can simultaneously use a shared<br>resource (such as software licenses or a file server).                      | Matching concurrency to a constrained resource shared across<br>jobs or queues. Replaces the natural limit of file system<br>throughput or license count. |
| Budgets with limit actions | Queue         | Tracks cumulative spending on a queue. When spending reaches a<br>threshold, an action stops scheduling new work or cancels running<br>work. | Enforcing a dollar cap on total spending for a project or time<br>period.                                                                                 |
| Job priority               | Job           | Determines which jobs are processed first when multiple jobs<br>compete for the same workers.                                                | Ensuring urgent work processes before less-critical jobs without<br>changing fleet capacity.                                                              |

## Fleet maximum worker count

The **maximum worker count** setting on a fleet limits
how many workers can run simultaneously. When the fleet reaches this maximum, it stops
starting new workers even if more jobs are waiting. This setting is the most direct replacement
for the natural concurrency limit of a fixed-size render farm.

Use this setting when you want to cap your peak compute cost at the fleet level.
For example, setting the maximum to 50 workers means you never pay for more than 50
concurrent instances, regardless of queue depth.

For more information, see [Auto scaling configuration](auto-scaling-configuration.md "auto-scaling-configuration.md").

## Job maximum worker count

The **max-worker-count** option on a job limits how
many workers can process that specific job. When the maximum is reached, no more workers
are assigned to the job even if workers are available in the fleet. Other jobs in the
queue can still use the remaining workers.

Use this setting when you want to prevent a single large job from monopolizing the
fleet. For example, if your fleet has 100 workers and you submit a 10,000-frame job with
`--max-worker-count 50`, the remaining 50 workers stay available for other
jobs. You can also change this value after submission.

```
deadline bundle submit my_job --max-worker-count 50
```

## Resource limits

**Resource limits** cap the number of tasks that can
simultaneously use a constrained resource, such as floating software licenses or a file
server with limited throughput. Limits are defined at the farm level and associated with
one or more queues. Steps in a job that declare a limit requirement only run tasks up to
the available count.

Use limits when you have a shared resource with a fixed capacity. For example, if
you have 25 floating licenses for a renderer, create a limit of 25. With this limit, no
more than 25 tasks use that license concurrently across all queues that share it.

For more information, see [Create resource
limits for jobs](../developerguide/build-job-limits.md "../developerguide/build-job-limits.md") in the _Deadline Cloud Developer Guide_.

## Budgets with limit actions

An Deadline Cloud **budget** tracks cumulative estimated
spending on a queue over a time period. You configure _limit actions_
that trigger when spending reaches a threshold. Available actions include:

- **Stop scheduling new work** –
  Running tasks complete, but the fleet stops accepting new tasks.
- **Stop all work immediately** – All
  running tasks are canceled and no new tasks are assigned.

Use budgets when you want to enforce a dollar cap for a project or billing period.
You can create multiple thresholds with different actions. For example, stop scheduling
at $5,000 remaining to allow current work to finish gracefully, and cancel all work if
 spending reaches $0 remaining.

For more information, see [Control costs with a budget](using-budget-manager.md "using-budget-manager.md").

## Job priority

**Job priority** influences the order in which jobs
are processed when multiple jobs compete for workers in the same queue. Priority ranges
from 0 to 100, with higher numbers generally processed first. Jobs with the same
priority are processed in the order received.

Priority does not limit concurrency or cost directly. Instead, it helps ensure that
the most important work gets workers first when the fleet is at capacity. Combine
priority with a fleet maximum worker count to control both which jobs run first and how
much compute runs in total.

## Choose the right controls for your workflow

The following scenarios illustrate common combinations:

"I want a hard cap on what I spend per month"

Create a budget on each queue with a monthly dollar limit and a
stop-scheduling action.

"I want to limit how many instances run at once, like my old fixed
farm"

Set the maximum worker count on your fleet. This directly replaces
the natural concurrency limit of a fixed-size farm.

"I have 50 licenses and don't want jobs to fail because they can't get
one"

Create a resource limit of 50 and associate it with the relevant
queues. Jobs that declare the limit only schedule tasks when a license
is available.

"I don't want one huge job to starve smaller jobs"

Set `--max-worker-count` on large jobs to reserve fleet
capacity for other work. Optionally, set higher priority on the smaller
jobs.

"I want a combination of cost control and fair sharing"

Set a fleet maximum worker count, use per-job max worker counts for
large jobs, and add a budget as a safety net. This combination gives you a peak
capacity limit, per-job fairness, and a dollar backstop.
