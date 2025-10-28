# Job queues

Jobs are submitted to a job queue where they reside until they can be scheduled to run in a compute environment.
An AWS account can have multiple job queues. For example, you can create a queue that uses Amazon EC2 On-Demand instances
for high priority jobs and another queue that uses Amazon EC2 Spot Instances for low-priority jobs. Job queues have a
priority that's used by the scheduler to determine which jobs in which queue should be evaluated for execution
first.

###### Topics

- [Create a job queue](create-job-queue.md "create-job-queue.md")
- [View job queue status](job_queue_viewing_status.md "job_queue_viewing_status.md")
- [Delete a job queue in AWS Batch](delete-job-queue.md "delete-job-queue.md")
- [Fair-share scheduling policies](job_scheduling.md "job_scheduling.md")
- [Resource-aware scheduling](resource-aware-scheduling.md "resource-aware-scheduling.md")
