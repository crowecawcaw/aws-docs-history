# Create resource limits for jobs

Jobs submitted to Deadline Cloud may depend on resources that are shared between multiple jobs. For
example, a farm may have more workers than floating licences for a specific resource. Or a
shared file server may only be able to serve data to a limited number of workers at the same
time. In some cases, one or more jobs can claim all of these resources, causing errors due to
unavailable resources when new workers start.

To help solve this, you can use _limits_ for these constrained
resources. Deadline Cloud accounts for the availability of constrained resources and uses that
information to ensure that resources are available as new workers start up so that jobs have a
lower likelihood of failing due to unavailable resources.

Limits are created for the entire farm. Jobs submitted to a queue can only acquire limits
associated with the queue. If you specify a limit for a job that is not associated with the
queue, the job isn't compatible and won't run.

To use a limit, you

- [Create a limit](job-limit-create.md "job-limit-create.md")
- [Associate a limit and a queue](job-limit-associate.md "job-limit-associate.md")
- [Submit a job requiring limits](job-limit-job.md "job-limit-job.md")

###### Note

If you run a job that has constrained resources in a queue that is not associated with a
limit, that job can consume all of the resources. If you have a constrained resource, make
sure that all of the steps in jobs in queues that use the resource are associated with a
limit.

For limits defined in a farm, associated with a queue, and specified in a job, one of four
things can happen:

- If you create a limit, associate it with a queue, and specify the limit in a job's
  template, the job runs and uses only the resources defined in the limit.
- If you create a limit, specify it in a job template, but don't associate the limit
  with a queue, the job is marked incompatible and won't run.
- If you create a limit, don't associate it with a queue, and don't specify the limit in
  a job's template, the job runs but does not use the limit.
- If you don't use a limit at all, the job runs.
  If you associate a limit to multiple queues, the queues share the resources constrained by
  the limit. For example, if you create a limit of 100, and one queue is using 60 resources,
  other queues can only use 40 resources. When a resource is released, it can be taken by a task
  from any queue.

Deadline Cloud provides two AWS CloudFormation metrics to help you monitor the resources provided by a
limit. You can monitor the current number of resources in use and the maximum number of
resources available in the limit. For more information, see [Resource limit metrics](cloudwatch-metrics.md#cloudwatch-metrics-limits "cloudwatch-metrics.md#cloudwatch-metrics-limits") in the _Deadline Cloud Developer Guide_.

You apply a limit to a job step in a job template. When you specify the amount requirement
name of a limit in the `amounts` section of the `hostRequirements` of a
step and a limit with the same `amountRequirementName` is associated with the job's
queue, tasks scheduled for this step are constrained by the limit for the resource.

If a step requires a resource that is constrained by a limit that is reached, tasks in
that step won't be picked up by additional workers.

You can apply more than one limit to a job step. For example, if the step uses two
different software licenses, you can apply a separate limit for each license. If a step
requires two limits and the limit for one of the resources is reached, tasks in that step
won't be picked up by additional workers until the resources become available.

## Stopping and deleting limits

When you stop or delete the association between a queue and a limit, a job using the
limit stops scheduling tasks from steps that require this limit and blocks the creation of
new sessions for a step.

Tasks that are in the READY state remain ready, and tasks automatically resume with the
association between the queue and the limit becomes active again. You don't need to requeue
any jobs.

When you stop or delete the association between a queue and a limit, you have two
choices on how to stop running tasks:

- _Stop and cancel tasks_ – Workers with sessions that
  acquired the limit cancel all tasks.
- _Stop and finish running tasks_ – Workers with sessions
  that acquired the limit complete their tasks.

When you delete a limit using the console, workers first stop running tasks immediately
or eventually when they complete. When the association is deleted, the following happens:

- Steps requiring the limit are marked not compatible.
- The entire job containing those steps is canceled, including steps that don't
  require the limit.
- The job is marked not compatible.

If the queue associated with the limit has an associated fleet with a fleet capability
that matches the amount requirement name of the limit, that fleet will continue to process
jobs with the specified limit.
