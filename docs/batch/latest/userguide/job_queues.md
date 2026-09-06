

# Job queues
<a name="job_queues"></a>

Jobs are submitted to a job queue where they reside until they can be scheduled to run in a compute environment. An AWS account can have multiple job queues. For example, you can create a queue that uses Amazon EC2 On-Demand instances for high priority jobs and another queue that uses Amazon EC2 Spot Instances for low-priority jobs. Job queues have a priority that's used by the scheduler to determine which jobs in which queue should be evaluated for execution first.

**Important**  
For Amazon ECS Managed Instances job queues that include both On-Demand and Spot compute environments, all On-Demand compute environments must be ordered before any Spot compute environments in the `computeEnvironmentOrder`. For more information, see [Job queues on Amazon ECS Managed Instances](ecs-managed-instances-job-queues.md).

**Topics**
+ [Create a job queue](create-job-queue.md)
+ [View a job queue in AWS Batch](job_queue_viewing_status.md)
+ [Delete a job queue in AWS Batch](delete-job-queue.md)
+ [Fair-share scheduling policies](job_scheduling.md)
+ [Resource-aware scheduling](resource-aware-scheduling.md)
+ [Quota management](quota-management.md)
+ [Track service job capacity utilization](track-capacity-utilization-service-jobs.md)
+ [Track compute job capacity utilization](track-capacity-utilization-compute-jobs.md)