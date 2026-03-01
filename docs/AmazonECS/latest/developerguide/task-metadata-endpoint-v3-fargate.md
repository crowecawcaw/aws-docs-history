# Amazon ECS task metadata endpoint version 3 for tasks on Fargate

###### Important

The task metadata version 3 endpoint is no longer being actively maintained. We
recommend that you update the task metadata version 4 endpoint to get the latest
metadata endpoint information. For more information, see [Amazon ECS task metadata endpoint version 4 for tasks on Fargate](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md").

Beginning with Fargate platform version `1.1.0`, an environment variable
named `ECS_CONTAINER_METADATA_URI` is injected into each container in a task.
When you query the task metadata version 3 endpoint, various task metadata and [Docker
stats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") are available to tasks.

The task metadata endpoint feature is enabled by default for Amazon ECS tasks hosted on
Fargate that use platform version `1.1.0` or later. For more
information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").

## Task metadata endpoint paths for tasks on Fargate

The following API endpoints are available to containers:

`${ECS_CONTAINER_METADATA_URI}`

This path returns metadata JSON for the container.

`${ECS_CONTAINER_METADATA_URI}/task`

This path returns metadata JSON for the task, including a list of the
container IDs and names for all of the containers associated with the task.
For more information about the response for this endpoint, see [Amazon ECS task metadata v3 JSON response for tasks on Fargate](task-metadata-endpoint-v3-fargate-response.md "task-metadata-endpoint-v3-fargate-response.md").

`${ECS_CONTAINER_METADATA_URI}/stats`

This path returns Docker stats JSON for the specific Docker container. For
more information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

`${ECS_CONTAINER_METADATA_URI}/task/stats`

This path returns Docker stats JSON for all of the containers associated
with the task. For more information about each of the returned stats, see
[ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.
