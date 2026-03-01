# Amazon ECS task metadata V4 JSON response

The following information is returned from the task metadata endpoint
(`${ECS_CONTAINER_METADATA_URI_V4}/task`) JSON response. This includes
metadata associated with the task in addition to the metadata for each container within
the task.

`Cluster`

The Amazon Resource Name (ARN) or short name of the Amazon ECS cluster to which the task belongs.

`ServiceName`

The name of the service to which the task belongs. ServiceName will appear for Amazon EC2 and Amazon ECS Anywhere container instances if the task is associated with a service.

###### Note

The `ServiceName` metadata is only included when using Amazon ECS container agent version `1.63.1` or later.

`VPCID`

The VPC ID of the Amazon EC2 container instance. This field only appears for Amazon EC2 instances.

###### Note

The `VPCID` metadata is only included when using Amazon ECS container agent version `1.63.1` or later.

`TaskARN`

The Amazon Resource Name (ARN) of the task to which the container
belongs.

`Family`

The family of the Amazon ECS task definition for the task.

`Revision`

The revision of the Amazon ECS task definition for the task.

`DesiredStatus`

The desired status for the task from Amazon ECS.

`KnownStatus`

The known status for the task from Amazon ECS.

`Limits`

The resource limits specified at the task level, such as CPU (expressed in vCPUs) and memory. This
parameter is omitted if no resource limits are defined.

`PullStartedAt`

The timestamp for when the first container image pull began.

`PullStoppedAt`

The timestamp for when the last container image pull finished.

`AvailabilityZone`

The Availability Zone the task is in.

###### Note

The Availability Zone metadata is only available for Fargate tasks using platform version 1.4 or later (Linux) or 1.0.0 (Windows).

`LaunchType`

The launch type the task is using. When using cluster capacity providers, this indicates whether the task is using Fargate or EC2 infrastructure.

###### Note

This `LaunchType` metadata is only included when using Amazon ECS Linux container agent version `1.45.0` or later (Linux) or 1.0.0 or later (Windows).

`Containers`

A list of container metadata for each container associated with the task.

`DockerId`

The Docker ID for the container.

When you use Fargate, the id is a 32-digit hex followed by a 10 digit number.

`Name`

The name of the container as specified in the task definition.

`DockerName`

The name of the container supplied to Docker. The Amazon ECS container
agent generates a unique name for the container to avoid name collisions
when multiple copies of the same task definition are run on a single
instance.

`Image`

The image for the container.

`ImageID`

The SHA-256 digest of the image manifest. This is the digest that can be used to pull the image using the format `repository-url/image@sha256:digest`.

`Ports`

Any ports exposed for the container. This parameter is omitted if
there are no exposed ports.

`Labels`

Any labels applied to the container. This parameter is omitted if
there are no labels applied.

`DesiredStatus`

The desired status for the container from Amazon ECS.

`KnownStatus`

The known status for the container from Amazon ECS.

`ExitCode`

The exit code for the container. This parameter is omitted if the
container has not exited.

`Limits`

The resource limits specified at the container level, such as CPU (expressed in CPU units) and
memory. This parameter is omitted if no resource limits are
defined.

`CreatedAt`

The time stamp for when the container was created. This parameter is
omitted if the container has not been created yet.

`StartedAt`

The time stamp for when the container started. This parameter is
omitted if the container has not started yet.

`FinishedAt`

The time stamp for when the container stopped. This parameter is
omitted if the container has not stopped yet.

`Type`

The type of the container. Containers that are specified in your task
definition are of type `NORMAL`. You can ignore other
container types, which are used for internal task resource provisioning
by the Amazon ECS container agent.

`LogDriver`

The log driver the container is using.

###### Note

This `LogDriver` metadata is only included when using Amazon ECS Linux container agent version `1.45.0` or later.

`LogOptions`

The log driver options defined for the container.

###### Note

This `LogOptions` metadata is only included when using Amazon ECS Linux container agent version `1.45.0` or later.

`ContainerARN`

The Amazon Resource Name (ARN) of the container.

###### Note

This `ContainerARN` metadata is only included when using Amazon ECS Linux container agent version `1.45.0` or later.

`Networks`

The network information for the container, such as the network mode
and IP address. This parameter is omitted if no network information is
defined.

`RestartCount`

The number of times the container has been restarted.

###### Note

The `RestartCount` metadata is included only if a restart policy is enabled for the container. For more information, see [Restart individual containers in Amazon ECS tasks with container restart policies](container-restart-policy.md "container-restart-policy.md").

`ExecutionStoppedAt`

The time stamp for when the tasks `DesiredStatus` moved to
`STOPPED`. This occurs when an essential container moves to
`STOPPED`.
