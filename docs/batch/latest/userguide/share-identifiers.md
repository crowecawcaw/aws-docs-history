# Use share identifiers to identify workloads

You can use share identifiers to tag jobs and differentiate between users and workloads.
The AWS Batch scheduler tracks usage for each share identifier by using the `*(T \* weightFactor)*` formula, where _`T`_
is the vCPU usage over time. The scheduler picks jobs with the lowest usage from the share identifier.
You can use a share identifier without overriding it.

###### Note

Share identifiers are unique within a job queue and are not aggregated across job
queues.

You can set fair-share scheduling priority to configure the order that jobs are run in on a share
identifier. Jobs with a higher scheduling priority are scheduled first. If you don’t specify a
fair-share scheduling policy, all jobs that are submitted to the job queue are scheduled in FIFO order.
When you submit a job, you can’t specify a share identifier or fair-share scheduling priority.

###### Note

Attached compute resources are allocated equally among all share identifiers unless
explicitly overridden.
