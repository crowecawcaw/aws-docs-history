# Amazon ECS task metadata available for tasks on

Fargate

Amazon ECS on Fargate provides a method to retrieve various metadata, network metrics,
and [Docker stats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") about your containers and the tasks they are a part of. This
is referred to as the _task metadata endpoint_. The following task
metadata endpoint versions are available for Amazon ECS on Fargate tasks:

- Task metadata endpoint version 4 – Available for tasks that use platform
  version 1.4.0 or later.
- Task metadata endpoint version 3 – Available for tasks that use platform
  version 1.1.0 or later.
  All containers belonging to tasks that are launched with the `awsvpc`
  network mode receive a local IPv4 address within a predefined link-local address range.
  When a container queries the metadata endpoint, the container agent can determine which
  task the container belongs to based on its unique IP address, and metadata and stats for
  that task are returned.

###### Topics

- [Amazon ECS task metadata endpoint version 4 for
  tasks on Fargate](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md")
- [Amazon ECS task metadata endpoint version 3 for
  tasks on Fargate](task-metadata-endpoint-v3-fargate.md "task-metadata-endpoint-v3-fargate.md")
