# Amazon ECS task metadata v3 JSON response

The following information is returned from the task metadata endpoint
(`${ECS_CONTAINER_METADATA_URI}/task`) JSON response.

`Cluster`

The Amazon Resource Name (ARN) or short name of the Amazon ECS cluster to which the task belongs.

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

The Availability Zone metadata is only available for Fargate tasks using platform version 1.4 or later (Linux) or 1.0.0 or later (Windows).

`Containers`

A list of container metadata for each container associated with the task.

`DockerId`

The Docker ID for the container.

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

`Networks`

The network information for the container, such as the network mode
and IP address. This parameter is omitted if no network information is
defined.

`ClockDrift`

The information about the difference between the reference time and the system time. This applies to the Linux operating system. This capability uses Amazon Time Sync Service to measure clock accuracy and provide the clock error bound for containers. For more information, see [Set the time for your Linux instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") in the _Amazon EC2 User Guide for Linux instances_.

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
