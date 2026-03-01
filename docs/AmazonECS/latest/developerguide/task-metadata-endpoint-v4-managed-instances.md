# Amazon ECS task metadata endpoint version 4 for tasks on Amazon ECS Managed Instances

###### Important

If you are using Amazon ECS tasks hosted on Amazon EC2 instances, see [Amazon ECS task
metadata endpoint](task-metadata-endpoint.md "task-metadata-endpoint.md").

Beginning with Amazon ECS Managed Instances, an environment variable
named `ECS_CONTAINER_METADATA_URI_V4` is injected into each container in a task.
When you query the task metadata endpoint version 4, various task metadata and [Docker
stats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") are available to tasks.

The task metadata endpoint is on by default for all Amazon ECS tasks run on Amazon ECS Managed Instances.

###### Note

To avoid the need to create new task metadata endpoint versions in the future,
additional metadata may be added to the version 4 output. We will not remove any
existing metadata or change the metadata field names.

## Amazon ECS Managed Instances task metadata endpoint version 4 paths

The following task metadata endpoints are available to containers:

`${ECS_CONTAINER_METADATA_URI_V4}`

This path returns metadata for the container.

`${ECS_CONTAINER_METADATA_URI_V4}/task`

This path returns metadata for the task, including a list of the container
IDs and names for all of the containers associated with the task. For more
information about the response for this endpoint, see [Amazon ECS task metadata v4 JSON response for tasks on Amazon ECS Managed Instances](task-metadata-endpoint-v4-managed-instances-response.md "task-metadata-endpoint-v4-managed-instances-response.md").

`${ECS_CONTAINER_METADATA_URI_V4}/stats`

This path returns Docker stats for the Docker container. For more
information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

###### Note

Amazon ECS tasks on Amazon ECS Managed Instances require that the container run for ~1
second prior to returning the container stats.

`${ECS_CONTAINER_METADATA_URI_V4}/task/stats`

This path returns Docker stats for all of the containers associated with
the task. For more information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

###### Note

Amazon ECS tasks on Amazon ECS Managed Instances require that the container run for ~1
second prior to returning the container stats.
