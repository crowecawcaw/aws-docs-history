# Runtime Monitoring for Amazon ECS Fargate workloads

If you use EC2 container instances, you must manually configure Runtime Monitoring. For more
information, see [Runtime Monitoring for EC2 workloads on Amazon ECS](ecs-guard-duty-configure-manual.md "ecs-guard-duty-configure-manual.md").

You can have GuardDuty manage the security agent on your container instances. This option
is only available for Fargate. This option ( GuardDuty agent management) is available in GuardDuty

When you use GuardDuty agent management, GuardDuty performs the following operations:

- Creates VPC endpoints for GuardDuty for each VPC that hosts a cluster.
- Retrieves, and installs the latest GuardDuty security agent as a sidecar container
  on all new standalone Fargate tasks, and new service deployments.

A new service deployment happens the first time you launch a service, or when
you update an existing service with the **force new
deployment** option.
