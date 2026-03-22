# Amazon ECS task metadata v4 JSON response for tasks on Fargate

The following metadata is returned in the task metadata endpoint
(`${ECS_CONTAINER_METADATA_URI_V4}/task`) JSON response.

`Cluster`

The Amazon Resource Name (ARN) or short name of the Amazon ECS cluster to which the task belongs.

`ServiceName`

The name of the service to which the task belongs. ServiceName will appear for Fargate tasks is associated with a service.

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

The resource limits specified at the task levels such as CPU (expressed in vCPUs) and memory. This
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

`EphemeralStorageMetrics`

The reserved size and current usage of the ephemeral storage of this task.

###### Note

Fargate reserves space on disk. It is only used by Fargate. You aren't billed for it. It isn't shown in these metrics. However, you can see this additional storage in other tools such as `df`.

`Utilized`

The current ephemeral storage usage (in MiB) of this task.

`Reserved`

The reserved ephemeral storage (in MiB) of this task. The size of the ephemeral storage can't be changed in a running task.
You can specify the `ephermalStorage` object in your task definition to change the amount of ephemeral storage.
The `ephermalStorage` is specified in GiB, not MiB. The `ephermalStorage` and the `EphemeralStorageMetrics`
are only available on Fargate Linux platform version 1.4.0 or later.

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

The resource limits specified at the container level such as CPU (expressed in CPU units) and
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

`Snapshotter`

The snapshotter that was used by containerd
to download this container image. Valid values are `overlayfs`,
which is the default, and `soci`, used when lazy loading with a
SOCI index. This parameter is only available for tasks that run on
Linux platform version `1.4.0`.

`RestartCount`

The number of times the container has been restarted.

###### Note

The `RestartCount` metadata is included only if a restart policy is enabled for the container. For more information, see [Restart individual containers in Amazon ECS tasks with container restart policies](container-restart-policy.md "container-restart-policy.md").

`ClockDrift`

The information about the difference between the reference time and the system time. This capability uses Amazon Time Sync Service to measure clock accuracy and provide the clock error bound for containers. For more information, see [Set the time for your Linux instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") in the _Amazon EC2 User Guide for Linux instances_.

`ReferenceTime`

The basis of clock accuracy. Amazon ECS uses the Coordinated Universal Time (UTC) global standard through NTP, for example `2021-09-07T16:57:44Z`.

`ClockErrorBound`

The measure of clock error, defined as the offset to UTC. This error is the difference in milliseconds between the reference time and the system time.

`ClockSynchronizationStatus`

Indicates whether the most recent
synchronization attempt between the system time and the reference time was successful.

The valid values are `SYNCHRONIZED` and `NOT_SYNCHRONIZED`.

`ExecutionStoppedAt`

The time stamp for when the tasks `DesiredStatus` moved to
`STOPPED`. This occurs when an essential container moves to
`STOPPED`.
