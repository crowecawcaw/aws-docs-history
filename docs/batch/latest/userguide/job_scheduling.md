# Fair-share scheduling policies

The AWS Batch scheduler evaluates when, where, and how to run jobs that are submitted to a job
queue. If you don’t specify a scheduling policy when you create a job queue, the AWS Batch job
scheduler defaults to a first-in, first-out (FIFO) strategy. A FIFO strategy might cause
important jobs to get “stuck” behind jobs that were submitted earlier. By specifying a different
scheduling policy, you can allocate compute resources according to your specific needs.

###### Note

If you want to schedule the specific order that jobs are run in, use the `dependsOn` parameter in [SubmitJob](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") to specify the
dependencies for each job.

If you create a scheduling policy and attach it to a job queue, fair-share scheduling is
turned on. If the job queue has a scheduling policy, the scheduling policy determines the order
that jobs are run in. For more information, see [Use fair-share scheduling policies to assign share identifiers](scheduling-policies.md "scheduling-policies.md").

###### Topics

- [Use share identifiers to identify workloads](share-identifiers.md "share-identifiers.md")
- [Use fair-share scheduling policies to assign share identifiers](scheduling-policies.md "scheduling-policies.md")
- [Use fair-share scheduling to help schedule jobs](fair-share-scheduling.md "fair-share-scheduling.md")
- [Tutorial: Create a scheduling policy](create-scheduling-policy.md "create-scheduling-policy.md")
- [Reference: Scheduling policy template](scheduling-policy-template.md "scheduling-policy-template.md")
