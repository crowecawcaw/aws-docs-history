# Job dependencies

When you submit an AWS Batch job, you can specify the job IDs that the job depends on. When you
do so, the AWS Batch scheduler ensures that your job is run only after the specified dependencies
have successfully completed. After they succeed, the dependent job transitions from `PENDING`
to `RUNNABLE` and then to `STARTING` and `RUNNING`. If any of
the job dependencies fail, the dependent job automatically transitions from `PENDING`
to `FAILED`.

For example, Job A can express a dependency on up to 20 other jobs that must succeed before
it can run. You can then submit additional jobs that have a dependency on Job A and up to 19
other jobs.

For array jobs, you can specify a `SEQUENTIAL` type dependency without specifying
a job ID so that each child array job completes sequentially, starting at index 0. You can also
specify an `N_TO_N` type dependency with a job ID. That way, each index child of this
job must wait for the corresponding index child of each dependency to complete before it can begin.
For more information, see [Array jobs](array_jobs.md "array_jobs.md").

To submit an AWS Batch job with dependencies, see [Tutorial: submit a job](submit_job.md "submit_job.md").

[Resource-aware scheduling](resource-aware-scheduling.md "resource-aware-scheduling.md") lets you
schedule jobs based on consumable resources that are needed to run your jobs. You specify the
consumable resources which are needed for a job to run, and Batch takes these resource dependencies
into account when it schedules a job. You can reduce the underutilization of compute resources
by allocating only the jobs that have all the required resources available. Resource-aware scheduling
is available for both FIFO and fair-share scheduling policies and can be used with all compute
platforms supported by Batch including EKS, ECS, and Fargate. It can be used with Array
jobs, Multi-node parallel (MNP) jobs, and with regular Batch jobs.
