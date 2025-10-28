# Amazon ECS task metadata available for tasks on

Amazon ECS Managed Instances

Amazon ECS on Amazon ECS Managed Instances provides a method to retrieve various metadata, network metrics,
and [Docker stats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") about your containers and the tasks they are a part of. This
is referred to as the _task metadata endpoint_. The task
metadata endpoint version 4 is available for Amazon ECS tasks on Amazon ECS Managed Instances.

All containers belonging to tasks that are launched with the `awsvpc`
network mode receive a local IPv4 address within a predefined link-local address range.
When a container queries the metadata endpoint, the container agent can determine which
task the container belongs to based on its unique IP address, and metadata and stats for
that task are returned.

###### Topics

- [Amazon ECS task metadata endpoint version 4 for
  tasks on Amazon ECS Managed Instances](task-metadata-endpoint-v4-managed-instances.md "task-metadata-endpoint-v4-managed-instances.md")
