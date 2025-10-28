# Fargate Linux platform version change

log

The following are the available Linux platform versions. For information about
platform version deprecation, see [AWS Fargate Linux platform version deprecation](platform-versions-retired.md "platform-versions-retired.md").

## 1.4.0

The following is the changelog for platform version `1.4.0`.

- Beginning on November 5, 2020, any new Amazon ECS task launched on
  Fargate using platform version `1.4.0` will be able
  to use the following features:
  - When using Secrets Manager to store sensitive data, you can inject a
    specific JSON key or a specific version of a secret as an
    environment variable or in a log configuration. For more
    information, see [Pass sensitive data to an Amazon ECS
    container](specifying-sensitive-data.md "specifying-sensitive-data.md").
  - Specify environment variables in bulk using the
    `environmentFiles` container definition parameter.
    For more information, see [Pass an individual environment
    variable to an Amazon ECS container](taskdef-envfiles.md "taskdef-envfiles.md").
  - Tasks run in a VPC and subnet enabled for IPv6 will be assigned
    both a private IPv4 address and an IPv6 address. For more
    information, see [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md").
  - The task metadata endpoint version 4 provides additional metadata
    about your task and container including the task launch type, the
    Amazon Resource Name (ARN) of the container, and the log driver and
    log driver options used. When querying the `/stats`
    endpoint you also receive network rate stats for your containers.
    For more information, see [Task metadata endpoint version 4](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md").

- Beginning on July 30, 2020, any new Amazon ECS task launched on
  Fargate using platform version `1.4.0` will be able
  to route UDP traffic using a Network Load Balancer to their Amazon ECS on Fargate tasks. For
  more information, see [Use load balancing to distribute Amazon ECS service
  traffic](service-load-balancing.md "service-load-balancing.md").
- Beginning on May 28, 2020, any new Amazon ECS task launched on
  Fargate using platform version `1.4.0` will have
  its ephemeral storage encrypted with an AES-256 encryption algorithm using
  an AWS owned encryption key. For more information, see [Fargate task ephemeral storage for Amazon ECS](fargate-task-storage.md "fargate-task-storage.md")
  and [Storage options for Amazon ECS tasks](using_data_volumes.md "using_data_volumes.md").
- Added support for using Amazon EFS file system volumes for persistent task
  storage. For more information, see [Use Amazon EFS volumes with Amazon ECS](efs-volumes.md "efs-volumes.md").
- The ephemeral task storage has been increased to a minimum of 20 GB for
  each task. For more information, see [Fargate task ephemeral storage for Amazon ECS](fargate-task-storage.md "fargate-task-storage.md").
- The network traffic behavior to and from tasks has been updated. Starting
  with platform version 1.4.0, all Fargate tasks receive a single elastic
  network interface (referred to as the task ENI) and all network traffic
  flows through that ENI within your VPC and will be visible to you through
  your VPC flow logs. For more information about networking for the Amazon EC2
  launch type, see [Amazon ECS
  task networking options for EC2](task-networking.md "task-networking.md"). For more information about networking for the
  Fargate, see [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md").
- Task ENIs add support for jumbo frames. Network interfaces are configured
  with a maximum transmission unit (MTU), which is the size of the largest
  payload that fits within a single frame. The larger the MTU, the more
  application payload can fit within a single frame, which reduces per-frame
  overhead and increases efficiency. Supporting jumbo frames will reduce
  overhead when the network path between your task and the destination
  supports jumbo frames, such as all traffic that remains within your
  VPC.
- CloudWatch Container Insights will include network performance metrics for Fargate tasks.
  For more information, see [Monitor Amazon ECS containers using Container Insights with
  enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").
- Added support for the task metadata endpoint version 4 which provides
  additional information for your Fargate tasks, including network stats for
  the task and which Availability Zone the task is running in. For more
  information, see [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md") and [Amazon ECS task metadata endpoint version 4 for
  tasks on Fargate](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md").
- Added support for the `SYS_PTRACE` Linux parameter in container
  definitions. For more information, see [Linux parameters](task_definition_parameters.md#container_definition_linuxparameters "task_definition_parameters.md#container_definition_linuxparameters").
- The Fargate container agent replaces the use of the Amazon ECS container
  agent for all Fargate tasks. Usually, this change does not have an effect
  on how your tasks run.
- The container runtime is now using Containerd instead of Docker. Most
  likely, this change does not have an effect on how your tasks run. You will
  notice that some error messages that originate with the container runtime
  changes from mentioning Docker to more general errors. For more information,
  see [Amazon ECS stopped
  task error messages](stopped-task-error-codes.md "stopped-task-error-codes.md").
- Based on Amazon Linux 2.
