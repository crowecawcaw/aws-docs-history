# Job queues on Amazon ECS Managed Instances

AWS Batch job queues for Amazon ECS Managed Instances follow the same model as Fargate: a job
queue can only contain compute environments of the same platform type. You cannot mix Amazon ECS
Managed Instances compute environments with Fargate or Amazon EC2 compute environments in the same
job queue.

###### Important

For Amazon ECS Managed Instances job queues, Spot compute environments cannot be ordered before
On-Demand compute environments in the `computeEnvironmentOrder`. If your job queue
includes both On-Demand and Spot compute environments, all On-Demand environments must appear
before any Spot environments in the ordering.

The following features are supported for Amazon ECS Managed Instances job queues:

- Fair-share scheduling policies
- Job queue snapshot
- Blocked job queue detection
- Resource-aware scheduling (consumable resources)
- Job state time limit actions
