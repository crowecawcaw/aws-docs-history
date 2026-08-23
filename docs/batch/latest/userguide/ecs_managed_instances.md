# Amazon ECS Managed Instances compute environments

With Amazon ECS Managed Instances, you run containers on Amazon EC2 instances that Amazon ECS fully manages
on your behalf. You don't need to configure Auto Scaling groups, select specific AMIs, or manage
instance lifecycle. Amazon ECS handles instance provisioning, scaling, patching, and termination
automatically based on the resource requirements of your jobs.

Use Amazon ECS Managed Instances when your jobs need GPU instances, large vCPU or memory
allocations, or specific Amazon EC2 instance types that exceed Fargate limits, without the overhead
of managing Auto Scaling groups or AMIs. You specify the maximum vCPUs for your compute
environment and optionally constrain which instance types are available. Amazon ECS handles the
rest.

Amazon ECS Managed Instances is only available for AWS Batch compute environments that use Amazon ECS as
the orchestrator. AWS Batch does not support Amazon ECS Managed Instances for Amazon EKS compute
environments.

###### Topics

- [When to use Amazon ECS Managed Instances](when-to-use-ecs-managed-instances.md "when-to-use-ecs-managed-instances.md")
- [Job definitions on Amazon ECS Managed Instances](ecs-managed-instances-job-definitions.md "ecs-managed-instances-job-definitions.md")
- [Job queues on Amazon ECS Managed Instances](ecs-managed-instances-job-queues.md "ecs-managed-instances-job-queues.md")
- [Compute environments on Amazon ECS Managed Instances](ecs-managed-instances-compute-environments.md "ecs-managed-instances-compute-environments.md")
