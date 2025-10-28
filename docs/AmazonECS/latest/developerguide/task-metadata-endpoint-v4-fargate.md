# Amazon ECS task metadata endpoint version 4 for

tasks on Fargate

###### Important

If you are using Amazon ECS tasks hosted on Amazon EC2 instances, see [Amazon ECS task
metadata endpoint](task-metadata-endpoint.md "task-metadata-endpoint.md").

Beginning with Fargate platform version `1.4.0`, an environment variable
named `ECS_CONTAINER_METADATA_URI_V4` is injected into each container in a task.
When you query the task metadata endpoint version 4, various task metadata and [Docker
stats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") are available to tasks.

The task metadata endpoint version 4 functions like the version 3 endpoint but provides
additional network metadata for your containers and tasks. Additional network metrics are
available when querying the `/stats` endpoints as well.

The task metadata endpoint is on by default for all Amazon ECS tasks run on AWS Fargate that
use platform version `1.4.0` or later.

###### Note

To avoid the need to create new task metadata endpoint versions in the future,
additional metadata may be added to the version 4 output. We will not remove any
existing metadata or change the metadata field names.

## Fargate task metadata

endpoint version 4 paths

The following task metadata endpoints are available to containers:

`${ECS_CONTAINER_METADATA_URI_V4}`

This path returns metadata for the container.

`${ECS_CONTAINER_METADATA_URI_V4}/task`

This path returns metadata for the task, including a list of the container
IDs and names for all of the containers associated with the task. For more
information about the response for this endpoint, see [Amazon ECS task metadata v4 JSON response for tasks on Fargate](task-metadata-endpoint-v4-fargate-response.md "task-metadata-endpoint-v4-fargate-response.md").

`${ECS_CONTAINER_METADATA_URI_V4}/stats`

This path returns Docker stats for the Docker container. For more
information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

###### Note

Amazon ECS tasks on AWS Fargate require that the container run for ~1
second prior to returning the container stats.

`${ECS_CONTAINER_METADATA_URI_V4}/task/stats`

This path returns Docker stats for all of the containers associated with
the task. For more information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

###### Note

Amazon ECS tasks on AWS Fargate require that the container run for ~1
second prior to returning the container stats.
