# Amazon ECS task metadata endpoint version 3

###### Important

The task metadata version 3 endpoint is no longer being actively maintained.
We recommend that you update the task metadata version 4 endpoint to get the
latest metadata endpoint information. For more information, see [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md").

If you are using Amazon ECS tasks hosted on AWS Fargate, see [Amazon ECS task metadata endpoint version 3 for tasks on
Fargate](task-metadata-endpoint-v3-fargate.md "task-metadata-endpoint-v3-fargate.md").

Beginning with version 1.21.0 of the Amazon ECS container agent, the agent injects an
environment variable called `ECS_CONTAINER_METADATA_URI` into each
container in a task. When you query the task metadata version 3 endpoint, various
task metadata and [Docker
stats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") are available to tasks. For tasks that use the `bridge`
network mode, network metrics are available when querying the `/stats`
endpoints.

The task metadata endpoint version 3 feature is enabled by default for tasks
that use Fargate on platform version v1.3.0 or
later and tasks that use EC2 and are launched on
Amazon EC2 Linux infrastructure running at least version 1.21.0 of the Amazon ECS
container agent or on Amazon EC2 Windows infrastructure running at least version
`1.54.0` of the Amazon ECS container agent and use `awsvpc`
network mode. For more information, see [Amazon ECS Linux container instance management](manage-linux.md "manage-linux.md").

You can add support for this feature on older container instances by updating
the agent to the latest version. For more information, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

###### Important

For tasks using Fargate and platform
versions prior to v1.3.0, the task metadata version 2 endpoint is supported.
For more information, see [Amazon ECS task metadata endpoint version 2](task-metadata-endpoint-v2.md "task-metadata-endpoint-v2.md").

## Task Metadata endpoint version 3 paths

The following task metadata endpoints are available to containers:

`${ECS_CONTAINER_METADATA_URI}`

This path returns metadata JSON for the container.

`${ECS_CONTAINER_METADATA_URI}/task`

This path returns metadata JSON for the task, including a list of
the container IDs and names for all of the containers associated
with the task. For more information about the response for this
endpoint, see [Amazon ECS task metadata v3 JSON response](task-metadata-endpoint-v3-response.md "task-metadata-endpoint-v3-response.md").

`${ECS_CONTAINER_METADATA_URI}/taskWithTags`

This path returns the metadata for the task included in the
`/task` endpoint in addition to the task and
container instance tags that can be retrieved using the
`ListTagsForResource` API.

`${ECS_CONTAINER_METADATA_URI}/stats`

This path returns Docker stats JSON for the specific Docker
container. For more information about each of the returned stats,
see [ContainerStats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") in the Docker API documentation.

`${ECS_CONTAINER_METADATA_URI}/task/stats`

This path returns Docker stats JSON for all of the containers
associated with the task. For more information about each of the
returned stats, see [ContainerStats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") in the Docker API documentation.
