# Amazon ECS task metadata endpoint version 4

The Amazon ECS container agent injects an environment variable into each container, referred to
as the _task metadata endpoint_ which provides various task metadata and
[Docker
stats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") to the container.

The task metadata and network rate stats are sent to CloudWatch Container Insights and can be viewed in the
AWS Management Console. For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").

###### Note

Amazon ECS provides earlier versions of the task metadata endpoint. To avoid the need to
create new task metadata endpoint versions in the future, additional metadata may be
added to the version 4 output. We will not remove any existing metadata or change the
metadata field names.

The environment variable is injected by default into the containers of Amazon ECS tasks
launched on Amazon EC2 Linux instances that are running at least version `1.39.0` of
the Amazon ECS container agent. For Amazon EC2 Windows instances that use `awsvpc` network
mode, the Amazon ECS container agent must be at least version `1.54.0`. For more
information, see [Amazon ECS Linux container instance management](manage-linux.md "manage-linux.md").

###### Note

You can add support for this feature on Amazon EC2 instances using older versions of the
Amazon ECS container agent by updating the agent to the latest version. For more information,
see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

For task metadata example output, see [Amazon ECS task metadata v4 examples](task-metadata-endpoint-v4-examples.md "task-metadata-endpoint-v4-examples.md").

## Task metadata endpoint version 4 paths

The following task metadata endpoint paths are available to containers.

`${ECS_CONTAINER_METADATA_URI_V4}`

This path returns metadata for the container.

`${ECS_CONTAINER_METADATA_URI_V4}/task`

This path returns metadata for the task, including a list of the container
IDs and names for all of the containers associated with the task. For more
information about the response for this endpoint, see [Amazon ECS task metadata V4 JSON response](task-metadata-endpoint-v4-response.md "task-metadata-endpoint-v4-response.md").

`${ECS_CONTAINER_METADATA_URI_V4}/taskWithTags`

This path returns the metadata for the task included in the
`/task` endpoint in addition to the task and container
instance tags that can be retrieved using the
`ListTagsForResource` API. Any errors received when
retrieving the tag metadata will be included in the `Errors`
field in the response.

###### Note

The `Errors` field is only in the response for tasks hosted
on Amazon EC2 Linux instances running at least version `1.50.0` of
the container agent. For Amazon EC2 Windows instances that use
`awsvpc` network mode, the Amazon ECS container agent must be
at least version `1.54.0`

This endpoint requires the `ecs.ListTagsForResource`
permission.

###### Important

When using the
`${ECS_CONTAINER_METADATA_URI_V4}/taskWithTags` endpoint,
be aware that each call makes up to two API requests to
`ecs:ListTagsForResource` (one for container instance
tags and one for task tags) and that any sidecar containers in the task
may make these calls on your behalf. Frequent endpoint calls can result
in API throttling.

Consider implementing caching or batching strategies to reduce the
frequency of calls, especially in high-traffic applications, and
debugging API throttling issues using AWS CloudTrail. For information about
throttling limits for the `ListTagsForResource` API, see
[Request
throttling for the Amazon ECS API](../APIReference/request-throttling.md "../APIReference/request-throttling.md") in the
_Amazon Elastic Container Service API Reference_. For more information about
debugging Amazon ECS API calls using AWS CloudTrail, see [Log Amazon ECS API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

`${ECS_CONTAINER_METADATA_URI_V4}/stats`

This path returns Docker stats for the specific container. For more
information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

For Amazon ECS tasks that use the `awsvpc` or `bridge`
network modes hosted on Amazon EC2 Linux instances running at least version
`1.43.0` of the container agent, there will be additional
network rate stats included in the response. For all other tasks, the
response will only include the cumulative network stats.

`${ECS_CONTAINER_METADATA_URI_V4}/task/stats`

This path returns Docker stats for all of the containers associated with
the task. This can be used by sidecar containers to extract network metrics.
For more information about each of the returned stats, see [ContainerStats](https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats "https://docs.docker.com/engine/api/v1.30/#operation/ContainerStats") in the Docker API documentation.

For Amazon ECS tasks that use the `awsvpc` or `bridge`
network modes hosted on Amazon EC2 Linux instances running at least version
`1.43.0` of the container agent, there will be additional
network rate stats included in the response. For all other tasks, the
response will only include the cumulative network stats.
