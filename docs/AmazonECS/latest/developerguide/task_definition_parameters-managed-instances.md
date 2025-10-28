# Amazon ECS task definition

parameters for Amazon ECS Managed Instances

Task definitions are split into separate parts: the task family, the AWS Identity and Access Management (IAM)
task role, the network mode, container definitions, volumes, and capacity. The family and
container definitions are required in a task definition. In contrast, task role, network
mode, volumes, and capacity are optional.

You can use these parameters in a JSON file to configure your task definition.

The following are more detailed descriptions for each task definition parameter for
Amazon ECS Managed Instances.

## Family

`family`

Type: String

Required: Yes

When you register a task definition, you give it a family, which is
similar to a name for multiple versions of the task definition, specified
with a revision number. The first task definition that's registered into a
particular family is given a revision of 1, and any task definitions
registered after that are given a sequential revision number.

## Capacity

When you register a task definition, you can specify the capacity that Amazon ECS should
validate the task definition against. If the task definition doesn't validate against
the compatibilities specified, a client exception is returned. For more information, see
[Amazon ECS launch types](launch_types.md "launch_types.md").

The following parameter is allowed in a task definition.

`requiresCompatibilities`

Type: String array

Required: No

Valid Values: `MANAGED_INSTANCES`

The capacity to validate the task definition against. This initiates a
check to ensure that all of the parameters that are used in the task
definition meet the requirements for Amazon ECS Managed Instances.

## Task role

`taskRoleArn`

Type: String

Required: No

When you register a task definition, you can provide a task role for an
IAM role that allows the containers in the task permission to call the
AWS APIs that are specified in its associated policies on your behalf. For
more information, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

## Task execution role

`executionRoleArn`

Type: String

Required: Conditional

The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container
agent permission to make AWS API calls on your behalf. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

###### Note

The task execution IAM role is required depending on the
requirements of your task. The role is required for private ECR image pulls and using the `awslogs` log driver.

## Network mode

`networkMode`

Type: String

Required: No

Default: `awsvpc`

The Docker networking mode to use for the containers in the task. For
Amazon ECS tasks that are hosted on Amazon ECS Managed Instances, the valid values are
`awsvpc` and `host`. If no network mode is
specified, the default network mode is `awsvpc`.

If the network mode is `host`, the task uses
the host's network which bypasses Docker's built-in virtual network
by mapping container ports directly to the ENI of the Amazon EC2 instance that hosts
the task. Dynamic port mappings can’t be used in this network mode. A container
in a task definition that uses this mode must specify a specific
`hostPort` number. A port number on a host can’t be used by multiple
tasks. As a result, you can’t run multiple tasks of the same task definition
on a single Amazon EC2 instance.

###### Important

When running tasks that use the `host` network mode, do not
run containers using the root user (UID 0) for better security. As a
security best practice, always use a non-root user.

If the network mode is `awsvpc`, the task is allocated an
elastic network interface, and you must specify a
`NetworkConfiguration` when you create a service or run a
task with the task definition. For more information, see [Amazon ECS task networking for
Amazon ECS Managed Instances](managed-instance-networking.md "managed-instance-networking.md").

The `host` and `awsvpc` network modes offer the
highest networking performance for containers because they use the Amazon EC2
network stack. With the `host` and `awsvpc` network
modes, exposed container ports are mapped directly to the corresponding host
port (for the `host` network mode) or the attached elastic
network interface port (for the `awsvpc` network mode). Because
of this, you can't use dynamic host port mappings.

## Runtime platform

`operatingSystemFamily`

Type: String

Required: No

Default: LINUX

When you register a task definition, you specify the operating system
family.

The valid value for this field is `LINUX`.

All task definitions that are used in a service must have the same value
for this parameter.

When a task definition is part of a service, this value must match the
service `platformFamily` value.

`cpuArchitecture`

Type: String

Required: Conditional

When you register a task definition, you specify the CPU architecture. The
valid values are `X86_64` and `ARM64`.

If you don't specify a value, Amazon ECS attempts to place tasks on the available CPU
architecture based on the capacity provider configuration. To ensure that
tasks are placed on a specific CPU architecture, specify a value for
`cpuArchitecture` in the task definition.

All task definitions that are used in a service must have the same value
for this parameter.

For more information about `ARM64`, see [Amazon ECS task definitions for 64-bit ARM workloads](ecs-arm64.md "ecs-arm64.md").

## Task size

When you register a task definition, you can specify the total CPU and memory used for
the task. This is separate from the `cpu` and `memory` values at
the container definition level. For tasks that are hosted on Amazon EC2 instances, these
fields are optional.

###### Note

Task-level CPU and memory parameters are ignored for Windows containers. We
recommend specifying container-level resources for Windows containers.

`cpu`

Type: String

Required: Conditional

The hard limit of CPU units to present for the task. You can specify CPU
values in the JSON file as a string in CPU units or virtual CPUs (vCPUs).
For example, you can specify a CPU value either as `1024` in CPU
units or `1 vCPU` in vCPUs. When the task definition is
registered, a vCPU value is converted to an integer indicating the CPU
units.

This field is optional. If your cluster doesn't have any registered
container instances with the requested CPU units available, the task fails.
Supported values are between `0.125` vCPUs and `10`
vCPUs.

`memory`

Type: String

Required: Conditional

The hard limit of memory to present to the task. You can specify memory
values in the task definition as a string in mebibytes (MiB) or gigabytes
(GB). For example, you can specify a memory value either as
`3072` in MiB or `3 GB`in GB. When the task
definition is registered, a GB value is converted to an integer indicating
the MiB.

This field is optional and any value can be used. If a task-level memory
value is specified, then the container-level memory value is optional. If
your cluster doesn't have any registered container instances with the
requested memory available, the task fails. You can maximize your resource
utilization by providing your tasks as much memory as possible for a
particular instance type. For more information, see [Reserving Amazon ECS Linux container instance memory](memory-management.md "memory-management.md").

## Other task definition

parameters

The following task definition parameters can be used when registering task definitions
in the Amazon ECS console by using the **Configure via JSON** option. For
more information, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").

###### Topics

- [Ephemeral
  storage](#task_definition_ephemeralStorage-managed-instances "#task_definition_ephemeralStorage-managed-instances")
- [IPC mode](#task_definition_ipcmode-managed-instances "#task_definition_ipcmode-managed-instances")
- [PID mode](#task_definition_pidmode-managed-instances "#task_definition_pidmode-managed-instances")
- [Proxy configuration](#proxyConfiguration-managed-instances "#proxyConfiguration-managed-instances")
- [Tags](#tags-managed-instances "#tags-managed-instances")
- [Elastic Inference
  accelerator](#elastic-Inference-accelerator-managed-instances "#elastic-Inference-accelerator-managed-instances")
- [Placement constraints](#constraints-managed-instances "#constraints-managed-instances")
- [Volumes](#volumes-managed-instances "#volumes-managed-instances")

### Ephemeral

storage

`ephemeralStorage`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: [EphemeralStorage](../APIReference/API_EphemeralStorage.md "../APIReference/API_EphemeralStorage.md") object

Required: No

The amount of ephemeral storage (in GB) to allocate for the task. This
parameter is used to expand the total amount of ephemeral storage
available, beyond the default amount, for tasks that are hosted on
AWS Fargate. For more information, see [Use bind mounts with Amazon ECS](bind-mounts.md "bind-mounts.md").

### IPC mode

`ipcMode`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: String

Required: No

The IPC resource namespace to use for the containers in the task. The
valid values are `host`, `task`, or
`none`. If `host` is specified, then all the
containers that are within the tasks that specified the
`host` IPC mode on the same container instance share the
same IPC resources with the host Amazon EC2 instance. If `task` is
specified, all the containers that are within the specified task share
the same IPC resources. If `none` is specified, then IPC
resources within the containers of a task are private and not shared
with other containers in a task or on the container instance. If no
value is specified, then the IPC resource namespace sharing depends on
the Docker daemon setting on the container instance.

### PID mode

`pidMode`

Type: String

Required: No

The process namespace to use for the containers in the task. The valid
values are `host` or `task`. If `host`
is specified, then all the containers that are within the tasks that
specified the `host` PID mode on the same container instance
share the same process namespace with the host Amazon EC2 instance. If
`task` is specified, all the containers that are within
the specified task share the same process namespace. If no value is
specified, the default is a private namespace.

If the `host` PID mode is used, there's a heightened risk
of undesired process namespace exposure.

### Proxy configuration

`proxyConfiguration`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: [ProxyConfiguration](../APIReference/API_ProxyConfiguration.md "../APIReference/API_ProxyConfiguration.md") object

Required: No

The configuration details for the App Mesh proxy.

### Tags

The metadata that you apply to a task definition to help you categorize and
organize them. Each tag consists of a key and an optional value. You define both of
them.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have
  only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources,
  remember that other services may have restrictions on allowed characters.
  Generally allowed characters are: letters, numbers, and spaces representable
  in UTF-8, and the following characters: + - = . \_ : / @.
- Tag keys and values are case-sensitive.
- Don't use `aws:`, `AWS:`, or any upper or lowercase
  combination of such as a prefix for either keys or values as it is reserved
  for AWS use. You can't edit or delete tag keys or values with this prefix.
  Tags with this prefix do not count against your tags per resource
  limit.

`key`

Type: String

Required: No

One part of a key-value pair that make up a tag. A key is a general
label that acts like a category for more specific tag values.

`value`

Type: String

Required: No

The optional part of a key-value pair that make up a tag. A value acts
as a descriptor within a tag category (key).

### Elastic Inference

accelerator

`inferenceAccelerator`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: [InferenceAccelerator](../APIReference/API_InferenceAccelerator.md "../APIReference/API_InferenceAccelerator.md") object

Required: No

The Elastic Inference accelerators to use for the containers in the
task.

### Placement constraints

`placementConstraints`

Type: Array of [TaskDefinitionPlacementConstraint](../APIReference/API_TaskDefinitionPlacementConstraint.md "../APIReference/API_TaskDefinitionPlacementConstraint.md") objects

Required: No

An array of placement constraint objects to use for the task. You can
specify a maximum of 10 constraints per task (this limit includes
constraints in the task definition and those specified at
runtime).

Amazon ECS supports the `distinctInstace` and
`memberOf` placement constraints for tasks running on
Amazon ECS Managed Instances. The following attributes are supported for tasks
that use the `memberOf` placement constraint:

- `ecs.subnet-id`
- `ecs.availability-zone`
- `ecs.cpu-architecture`
- `ecs.instance-type`

For more information about placement constraints, see [Define which container
instances Amazon ECS uses for tasks](task-placement-constraints.md "task-placement-constraints.md").

### Volumes

When you register a task definition, you can optionally specify a list of volumes
that are passed to the Docker daemon on a container instance. This allows you to use
data volumes in your tasks.

For more information about volume types and other parameters, see [Storage options for Amazon ECS tasks](using_data_volumes.md "using_data_volumes.md").

`name`

Type: String

Required: Yes

The name of the volume. Up to 255 letters (uppercase and lowercase),
numbers, and hyphens are allowed. This name is referenced in the
`sourceVolume` parameter of container definition
`mountPoints`.

`host`

Type: [HostVolumeProperties](../APIReference/API_HostVolumeProperties.md "../APIReference/API_HostVolumeProperties.md") object

Required: No

This parameter is specified when you're using bind mount host volumes.
The contents of the `host` parameter determine whether your
bind mount host volume persists on the host container instance and where
it's stored. If the `host` parameter is empty, then the
Docker daemon assigns a host path for your data volume. However, the
data isn't guaranteed to persist after the containers that are
associated with it stop running.

`dockerVolumeConfiguration`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: [DockerVolumeConfiguration](../APIReference/API_DockerVolumeConfiguration.md "../APIReference/API_DockerVolumeConfiguration.md") object

Required: No

This parameter is specified when you're using Docker volumes.

`efsVolumeConfiguration`

Type: [EFSVolumeConfiguration](../APIReference/API_EFSVolumeConfiguration.md "../APIReference/API_EFSVolumeConfiguration.md") object

Required: No

This parameter is specified when you're using an Amazon EFS file
system for task storage.

`fsxWindowsFileServerVolumeConfiguration`

###### Note

This parameter isn't supported for tasks running on
Amazon ECS Managed Instances.

Type: [FSxWindowsFileServerVolumeConfiguration](../APIReference/API_FSxWindowsFileServerVolumeConfiguration.md "../APIReference/API_FSxWindowsFileServerVolumeConfiguration.md") object

Required: No

This parameter is specified when you're using Amazon FSx for Windows
File Server file system for task storage.

`configuredAtLaunch`

Type: Boolean

Required: No

Indicates whether the volume should be configured at launch time. This
is used to create Amazon EBS volumes for standalone tasks or tasks
created as part of a service. Each task definition revision may only
have one volume configured at launch in the volume configuration.

## Container definitions

When you register a task definition, you must specify a list of container definitions that
are passed to the Docker daemon on a container instance. The following
parameters are allowed in a container definition.

###### Topics

- [Name](#container_definition_name-managed-instances "#container_definition_name-managed-instances")
- [Image](#container_definition_image-managed-instances "#container_definition_image-managed-instances")
- [Memory](#container_definition_memory-managed-instances "#container_definition_memory-managed-instances")
- [CPU](#container_definition_cpu-managed-instances "#container_definition_cpu-managed-instances")
- [Port mappings](#container_definition_portmappings-managed-instances "#container_definition_portmappings-managed-instances")
- [Private Repository
  Credentials](#container_definition_repositoryCredentials-managed-instances "#container_definition_repositoryCredentials-managed-instances")
- [Essential](#container_definition_essential-managed-instances "#container_definition_essential-managed-instances")
- [Entry point](#container_definition_entrypoint-managed-instances "#container_definition_entrypoint-managed-instances")
- [Command](#container_definition_command-managed-instances "#container_definition_command-managed-instances")
- [Working directory](#container_definition_workingdirectory-managed-instances "#container_definition_workingdirectory-managed-instances")
- [Advanced container definition
  parameters](#advanced_container_definition_params-managed-instances "#advanced_container_definition_params-managed-instances")
- [Linux parameters](#container_definition_linuxparameters-managed-instances "#container_definition_linuxparameters-managed-instances")

### Name

`name`

Type: String

Required: Yes

The name of a container. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. If you're linking
multiple containers in a task definition, the `name` of one
container can be entered in the `links` of another container.
This is to connect the containers.

### Image

`image`

Type: String

Required: Yes

The image used to start a container. This string is passed directly to
the Docker daemon. By default, images in the
Docker Hub registry are available. You can also
specify other repositories with either
``repository-url`/`image`:`tag``
or
``repository-url`/`image`@`digest``.
Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to `Image` in the
docker create-container command and the `IMAGE` parameter of
the docker run command.

- When a new task starts, the Amazon ECS container agent pulls the
  latest version of the specified image and tag for the container
  to use. However, subsequent updates to a repository image aren't
  propagated to already running tasks.
- Whenyou don't specify a tag or digest in the image path in the
  task defintion, the Amazon ECS container agent pulls the latest
  version of the specified image.
- However, subsequent updates to a repository image aren't
  propagated to already running tasks.
- Images in private registries are supported. For more
  information, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").
- Images in Amazon ECR repositories can be specified by using either
  the full `registry/repository:tag` or
  `registry/repository@digest` naming convention
  (for example,
  ``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-web-app`:`latest``
or
``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-web-app`@`sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE``).
- Images in official repositories on Docker Hub
  use a single name (for example, `ubuntu` or
  `mongo`).
- Images in other repositories on Docker Hub are
  qualified with an organization name (for example,
  `amazon/amazon-ecs-agent`).
- Images in other online repositories are qualified further by a
  domain name (for example,
  `quay.io/assemblyline/ubuntu`).

`versionConsistency`

Type: String

Valid values: `enabled`|`disabled`

Required: No

Specifies whether Amazon ECS will resolve the container image tag
provided in the container definition to an image digest. By default, this behavior is `enabled`. If you set the value for a container as
`disabled`, Amazon ECS will not resolve the container image tag
to a digest and will use the original image URI specified in the container definition for deployment.
For more information about container image resolution, see [Container image
resolution](deployment-type-ecs.md#deployment-container-image-stability "deployment-type-ecs.md#deployment-container-image-stability").

### Memory

`memory`

Type: Integer

Required: No

The amount (in MiB) of memory to present to the container. If your
container attempts to exceed the memory specified here, the container is
killed. The total amount of memory reserved for all containers within a
task must be lower than the task `memory` value, if one is
specified. This parameter maps to `Memory` in the docker
create-container command and the `--memory` option to docker
run.

The Docker 20.10.0 or later daemon reserves a minimum of 6 MiB of memory for a
container. So, don't specify less than 6 MiB of memory for your containers.

The Docker 19.03.13-ce or earlier daemon reserves a minimum of 4 MiB of memory for a
container. So, don't specify less than 4 MiB of memory for your containers.

###### Note

If you're trying to maximize your resource utilization by providing your tasks
as much memory as possible for a particular instance type, see [Reserving Amazon ECS Linux container instance memory](memory-management.md "memory-management.md").

`memoryReservation`

Type: Integer

Required: No

The soft limit (in MiB) of memory to reserve for the container. When
system memory is under contention, Docker attempts to
keep the container memory to this soft limit. However, your container
can use more memory when needed. The container can use up to the hard
limit that's specified with the `memory` parameter (if
applicable) or all of the available memory on the container instance,
whichever comes first. This parameter maps to
`MemoryReservation` in the docker create-container
command and the `--memory-reservation` option to docker
run.

If a task-level memory value isn't specified, you must specify a
non-zero integer for one or both of `memory` or
`memoryReservation` in a container definition. If you
specify both, `memory` must be greater than
`memoryReservation`. If you specify
`memoryReservation`, then that value is subtracted from
the available memory resources for the container instance that the
container is placed on. Otherwise, the value of `memory` is
used.

For example, suppose that your container normally uses 128 MiB of
memory, but occasionally bursts to 256 MiB of memory for short periods
of time. You can set a `memoryReservation` of 128 MiB, and a
`memory` hard limit of 300 MiB. This configuration allows
the container to only reserve 128 MiB of memory from the remaining
resources on the container instance. At the same time, this
configuration also allows the container to use more memory resources
when needed.

The Docker 20.10.0 or later daemon reserves a minimum of 6 MiB of memory for a
container. So, don't specify less than 6 MiB of memory for your containers.

The Docker 19.03.13-ce or earlier daemon reserves a minimum of 4 MiB of memory for a
container. So, don't specify less than 4 MiB of memory for your containers.

###### Note

If you're trying to maximize your resource utilization by providing your tasks
as much memory as possible for a particular instance type, see [Reserving Amazon ECS Linux container instance memory](memory-management.md "memory-management.md").

### CPU

`cpu`

Type: Integer

Required: No

The number of `cpu` units reserved for the container. This
parameter maps to `CpuShares` in the docker create-container
command and the `--cpu-shares` option to docker run.

This field is optional for tasks using EC2 capacity providers, and the
only requirement is that the total amount of CPU reserved for all
containers within a task be lower than the task-level `cpu`
value.

###### Note

You can determine the number of CPU units that are available per
EC2 instance type by multiplying the vCPUs listed for that instance
type on the [Amazon EC2 Instances](http://aws.amazon.com/ec2/instance-types/ "http://aws.amazon.com/ec2/instance-types/") detail page by 1,024.

Linux containers share unallocated CPU units with other containers on
the container instance with the same ratio as their allocated amount. For
example, if you run a single-container task on a single-core instance
type with 512 CPU units specified for that container, and that's the only
task running on the container instance, that container could use the full
1,024 CPU units at any given time. However, if you launched another copy
of the same task on that container instance, each task is guaranteed a
minimum of 512 CPU units when needed. Moreover, each container could
float to higher CPU usage if the other container was not using it. If
both tasks were 100% active all of the time, they would be limited to 512
CPU units.

On Linux container instances, the Docker daemon on the container
instance uses the CPU value to calculate the relative CPU share ratios
for running containers. For more information, see [CPU share constraint](https://docs.docker.com/engine/reference/run/#cpu-share-constraint "https://docs.docker.com/engine/reference/run/#cpu-share-constraint") in the Docker documentation. The minimum
valid CPU share value that the Linux kernel allows is 2. However, the CPU
parameter isn't required, and you can use CPU values below 2 in your
container definitions. For CPU values below 2 (including null), the
behavior varies based on your Amazon ECS container agent version:

- **Agent versions less than or equal to
  1.1.0:** Null and zero CPU values are passed to
  Docker as 0, which Docker then converts to 1,024 CPU shares. CPU
  values of 1 are passed to Docker as 1, which the Linux kernel
  converts to two CPU shares.
- **Agent versions greater than or equal to
  1.2.0:** Null, zero, and CPU values of 1 are passed
  to Docker as 2.

On Windows container instances, the CPU limit is enforced as an absolute
limit, or a quota. Windows containers only have access to the specified
amount of CPU that's described in the task definition. A null or zero CPU
value is passed to Docker as `0`, which Windows interprets as
1% of one CPU.

### Port mappings

`portMappings`

Type: Object array

Required: No

Port mappings expose your container's network ports to the outside
world. this allows clients to access your application. It's also used
for inter-container communication within the same task.

For task definitions that use
the `awsvpc` network mode, only specify the
`containerPort`. The `hostPort` is always
ignored, and the container port is automatically mapped to a random
high-numbered port on the host.

Most fields of this parameter (including `containerPort`,
`hostPort`, `protocol`) map to
`PortBindings` in thedocker create-container command and
the `--publish` option to docker run. If the network mode of
a task definition is set to `host`, host ports must either be
undefined or match the container port in the port mapping.

###### Note

After a task reaches the `RUNNING` status, manual and
automatic host and container port assignments are visible in the
following locations:

- Console: The **Network Bindings** section
  of a container description for a selected task.
- AWS CLI: The `networkBindings` section of the
  **describe-tasks** command output.
- API: The `DescribeTasks` response.
- Metadata: The task metadata endpoint.

`appProtocol`

Type: String

Required: No

The application protocol that's used for the port mapping.
This parameter only applies to Service Connect. We
recommend that you set this parameter to be consistent with
the protocol that your application uses. If you set this
parameter, Amazon ECS adds protocol-specific connection handling
to the service connect proxy. If you set this parameter,
Amazon ECS adds protocol-specific telemetry in the Amazon ECS console
and CloudWatch.

If you don't set a value for this parameter, then TCP is
used. However, Amazon ECS doesn't add protocol-specific telemetry
for TCP.

For more information, see [Use Service Connect to connect Amazon ECS services with short
names](service-connect.md "service-connect.md").

Valid protocol values: `"HTTP" | "HTTP2" | "GRPC"`

`containerPort`

Type: Integer

Required: Yes, when `portMappings` are
used

The port number on the container that's bound to the
user-specified or automatically assigned host port.

For tasks that use the `awsvpc` network mode,
you use `containerPort` to specify the exposed
ports.

`containerPortRange`

Type: String

Required: No

The port number range on the container that's bound to the
dynamically mapped host port range.

You can only set this parameter by using the
`register-task-definition` API. The option is
available in the `portMappings` parameter. For
more information, see [register-task-definition](../../../cli/latest/reference/ecs/register-task-definition.md "../../../cli/latest/reference/ecs/register-task-definition.md") in the _AWS Command Line Interface Reference_.

The following rules apply when you specify a
`containerPortRange`:

- You must use the `awsvpc` network mode.
- The container instance must have at least version
  1.67.0 of the container agent and at least version
  1.67.0-1 of the `ecs-init`
  package.
- You can specify a maximum of 100 port ranges for
  each container.
- You don't specify a `hostPortRange`.
  The value of the `hostPortRange` is set
  as follows:
  - For containers in a task with the
    `awsvpc` network mode, the
    `hostPort` is set to the same value as
    the `containerPort`. This is a static
    mapping strategy.

- The `containerPortRange` valid values
  are between 1 and 65535.
- A port can only be included in one port mapping
  for each container.
- You can't specify overlapping port ranges.
- The first port in the range must be less than last
  port in the range.
- Docker recommends that you turn off
  the docker-proxy in the Docker daemon
  config file when you have a large number of
  ports.

For more information, see [Issue #11185](https://github.com/moby/moby/issues/11185 "https://github.com/moby/moby/issues/11185") on GitHub.

For information about how to turn off the
docker-proxy in the Docker daemon
config file, see [Docker daemon](bootstrap_container_instance.md#bootstrap_docker_daemon "bootstrap_container_instance.md#bootstrap_docker_daemon") in the
_Amazon ECS Developer Guide_.

You can call [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") to view the
`hostPortRange`, which are the host ports
that are bound to the container ports.

The port ranges aren't included in the Amazon ECS task events,
which are sent to EventBridge. For more information, see [Automate responses to Amazon ECS errors using EventBridge](cloudwatch_event_stream.md "cloudwatch_event_stream.md").

`hostPortRange`

Type: String

Required: No

The port number range on the host that's used with the
network binding. This is assigned by Docker
and delivered by the Amazon ECS agent.

`hostPort`

Type: Integer

Required: No

The port number on the container instance to reserve for
your container.

The `hostPort` can either be kept blank or be the same value as
`containerPort`.

The default ephemeral port range Docker
version 1.6.0 and later is listed on the instance under
`/proc/sys/net/ipv4/ip_local_port_range`.
If this kernel parameter is unavailable, the default
ephemeral port range from `49153–65535` is used.
Don't attempt to specify a host port in the ephemeral port
range. This is because these are reserved for automatic
assignment. In general, ports under `32768` are
outside of the ephemeral port range.

The default reserved ports are `22` for SSH,
the Docker ports `2375` and
`2376`, and the Amazon ECS container agent ports
`51678-51680`. Any host port that was
previously user-specified for a running task is also
reserved while the task is running. After a task stops, the
host port is released. The current reserved ports are
displayed in the `remainingResources` of
**describe-container-instances** output.
A container instance might have up to 100 reserved ports at
a time, including the default reserved ports. Automatically
assigned ports don't count toward the 100 reserved ports
quota.

`name`

Type: String

Required: No, required for Service Connect and VPC Lattice to be
configured in a service

The name that's used for the port mapping. This parameter
only applies to Service Connect and VPC Lattice. This parameter is the name
that you use in the Service Connect and VPC Lattice configuration of a
service.

For more information, see [Use Service Connect to connect Amazon ECS services with short
names](service-connect.md "service-connect.md").

In the following example, both of the required fields for
Service Connect and VPC Lattice are used.

```

"portMappings": [
    {
        "name": `string`,
        "containerPort": `integer`
    }
]

```

`protocol`

Type: String

Required: No

The protocol that's used for the port mapping. Valid
values are `tcp` and `udp`. The
default is `tcp`.

###### Important

Only `tcp` is supported for
Service Connect. Remember that `tcp` is
implied if this field isn't set.

If you're specifying a host port, use the following syntax.

```
"portMappings": [
    {
        "containerPort": integer,
        "hostPort": integer
    }
    ...
]
```

If you want an automatically assigned host port, use the following
syntax.

```
"portMappings": [
    {
        "containerPort": integer
    }
    ...
]
```

### Private Repository

Credentials

`repositoryCredentials`

Type: [RepositoryCredentials](../APIReference/API_RepositoryCredentials.md "../APIReference/API_RepositoryCredentials.md") object

Required: No

The repository credentials for private registry authentication.

For more information, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").

`credentialsParameter`

Type: String

Required: Yes, when `repositoryCredentials`
are used

The Amazon Resource Name (ARN) of the secret containing the private
repository credentials.

For more information, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").

###### Note

When you use the Amazon ECS API, AWS CLI, or AWS SDKs, if
the secret exists in the same Region as the task that
you're launching then you can use either the full ARN or
the name of the secret. When you use the AWS Management Console, you
must specify the full ARN of the secret.

The following is a snippet of a task definition that shows
the required parameters:

```

"containerDefinitions": [
    {
        "image": "`private-repo/private-image`",
        "repositoryCredentials": {
            "credentialsParameter": "`arn:aws:secretsmanager:region:aws_account_id:secret:secret_name`"
        }
    }
]

```

### Essential

`essential`

Type: Boolean

Required: No

If the `essential` parameter of a container is marked as
`true`, and that container fails or stops for any reason,
all other containers that are part of the task are stopped. If the
`essential` parameter of a container is marked as
`false`, its failure doesn't affect the rest of the
containers in a task. If this parameter is omitted, a container is assumed
to be essential.

All tasks must have at least one essential container. If you have an
application that's composed of multiple containers, group containers that
are used for a common purpose into components, and separate the different
components into multiple task definitions. For more information, see [Architect your application for Amazon ECS](application_architecture.md "application_architecture.md").

### Entry point

`entryPoint`

Type: String array

Required: No

The entry point that's passed to the container. This parameter maps to
`Entrypoint` in the docker create-container command and the
`--entrypoint` option to docker run.

```
"entryPoint": ["string", ...]
```

### Command

`command`

Type: String array

Required: No

The command that's passed to the container. This parameter maps to
`Cmd` in the docker create-container command and the
`COMMAND` parameter to docker run. If there are multiple
arguments, each argument is a separated string in the array.

```
"command": ["string", ...]
```

### Working directory

`workingDirectory`

Type: String

Required: No

The working directory to run commands inside the container in. This
parameter maps to `WorkingDir` in the docker create-container
command and the `--workdir` option to docker run.

### Advanced container definition

parameters

The following advanced container definition parameters provide extended capabilities
to the docker run command that's used to launch containers on your Amazon ECS container
instances.

###### Topics

- [Restart policy](#container_definition_restart_policy-managed-instances "#container_definition_restart_policy-managed-instances")
- [Health check](#container_definition_healthcheck-managed-instances "#container_definition_healthcheck-managed-instances")
- [Environment](#container_definition_environment-managed-instances "#container_definition_environment-managed-instances")
- [Security](#container_definition_security-managed-instances "#container_definition_security-managed-instances")
- [Network settings](#container_definition_network-managed-instances "#container_definition_network-managed-instances")
- [Storage and logging](#container_definition_storage-managed-instances "#container_definition_storage-managed-instances")
- [Resource requirements](#container_definition_resourcerequirements-managed-instances "#container_definition_resourcerequirements-managed-instances")
- [Container timeouts](#container_definition_timeout-managed-instances "#container_definition_timeout-managed-instances")
- [Container dependency](#container_definition_dependency-managed-instances "#container_definition_dependency-managed-instances")
- [System controls](#container_definition_systemcontrols-managed-instances "#container_definition_systemcontrols-managed-instances")
- [Interactive](#container_definition_interactive-managed-instances "#container_definition_interactive-managed-instances")
- [Pseudo terminal](#container_definition_pseudoterminal-managed-instances "#container_definition_pseudoterminal-managed-instances")

#### Restart policy

`restartPolicy`

The container restart policy and associated configuration parameters.
When you set up a restart policy for a container, Amazon ECS can restart the
container without needing to replace the task. For more information, see
[Restart individual containers in Amazon ECS tasks with
container restart policies](container-restart-policy.md "container-restart-policy.md").

`enabled`

Type: Boolean

Required: Yes

Specifies whether a restart policy is enabled for the
container.

`ignoredExitCodes`

Type: Integer array

Required: No

A list of exit codes that Amazon ECS will ignore and not
attempt a restart on. You can specify a maximum of 50
container exit codes. By default, Amazon ECS does not ignore any
exit codes.

`restartAttemptPeriod`

Type: Integer

Required: No

A period of time (in seconds) that the container must run
for before a restart can be attempted. A container can be
restarted only once every `restartAttemptPeriod`
seconds. If a container isn't able to run for this time
period and exits early, it will not be restarted. You can
set a minimum `restartAttemptPeriod` of 60
seconds and a maximum `restartAttemptPeriod` of
1800 seconds. By default, a container must run for 300
seconds before it can be restarted.

#### Health check

`healthCheck`

The container health check command and the associated configuration
parameters for the container. For more information, see [Determine Amazon ECS task health using container health
checks](healthcheck.md "healthcheck.md").

`command`

A string array that represents the command that the
container runs to determine if it's healthy. The string
array can start with `CMD` to run the command
arguments directly, or `CMD-SHELL` to run the
command with the container's default shell. If neither is
specified, `CMD` is used.

When registering a task definition in the AWS Management Console, use a
comma separated list of commands. These commands are
converted to a string after the task definition is created.
An example input for a health check is the following.

```
CMD-SHELL, curl -f http://localhost/ || exit 1
```

When registering a task definition using the AWS Management Console
JSON panel, the AWS CLI, or the APIs, enclose the list of
commands in brackets. An example input for a health check is
the following.

```
[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]
```

An exit code of 0, with no `stderr` output,
indicates success, and a non-zero exit code indicates
failure.

`interval`

The period of time (in seconds) between each health check.
You can specify between 5 and 300 seconds. The default value
is 30 seconds.

`timeout`

The period of time (in seconds) to wait for a health check
to succeed before it's considered a failure. You can specify
between 2 and 60 seconds. The default value is 5
seconds.

`retries`

The number of times to retry a failed health check before
the container is considered unhealthy. You can specify
between 1 and 10 retries. The default value is three
retries.

`startPeriod`

The optional grace period to provide containers time to bootstrap in before failed
health checks count towards the maximum number of retries.
You can specify a value between 0 and 300 seconds. By
default, `startPeriod` is disabled.

If a health check succeeds within the `startPeriod`, then the container is considered healthy and any subsequent failures count toward the maximum number of retries.

#### Environment

`cpu`

Type: Integer

Required: No

The number of `cpu` units the Amazon ECS container agent
reserves for the container. On Linux, this parameter maps to
`CpuShares`
in the
[Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate") section.

This field is optional for tasks that run on Amazon ECS Managed Instances. The total amount of CPU reserved for all the containers
that are within a task must be lower than the task-level
`cpu` value.

Linux containers share unallocated CPU units with other
containers on the container instance with the same ratio as their
allocated amount. For example, assume that you run a single-container
task on a single-core instance type with 512 CPU units specified for
that container. Moreover, that task is the only task running on the
container instance. In this example, the container can use the full
1,024 CPU unit share at any given time. However, assume then that you
launched another copy of the same task on that container instance. Each
task is guaranteed a minimum of 512 CPU units when needed. Similarly, if
the other container isn't using the remaining CPU, each container can
float to higher CPU usage. However, if both tasks were 100% active all
of the time, they are limited to 512 CPU units.

On Linux container instances, the Docker
daemon on the container instance uses the CPU value to calculate the
relative CPU share ratios for running containers. The minimum valid CPU
share value that the Linux kernel allows is 2, and the maximum valid CPU
share value that the Linux kernel allows is 262144. However, the CPU
parameter isn't required, and you can use CPU values below two and above
262144 in your container definitions. For CPU values below two
(including null) and above 262144, the behavior varies based on your
Amazon ECS container agent version:

For more examples, see [How Amazon ECS manages CPU and memory resources](https://aws.amazon.com/blogs/containers/how-amazon-ecs-manages-cpu-and-memory-resources/ "https://aws.amazon.com/blogs/containers/how-amazon-ecs-manages-cpu-and-memory-resources/").

`gpu`

Type: [ResourceRequirement](../APIReference/API_ResourceRequirement.md "../APIReference/API_ResourceRequirement.md") object

Required: No

The number of physical `GPUs` that the Amazon ECS container
agent reserves for the container. The number of GPUs reserved for all
containers in a task must not exceed the number of available GPUs on the
container instance the task is launched on. For more information, see
[Amazon ECS task definitions for GPU workloads](ecs-gpu.md "ecs-gpu.md").

`Elastic Inference
 accelerator`

###### Note

This parameter isn't supported for containers that are hosted on
Amazon ECS Managed Instances.

Type: [ResourceRequirement](../APIReference/API_ResourceRequirement.md "../APIReference/API_ResourceRequirement.md") object

Required: No

For the `InferenceAccelerator` type, the `value`
matches the `deviceName` for an
`InferenceAccelerator` specified in a task definition.
For more information, see [Elastic Inference accelerator
name](task_definition_parameters.md#elastic-Inference-accelerator "task_definition_parameters.md#elastic-Inference-accelerator").

`essential`

Type: Boolean

Required: No

Suppose that the `essential` parameter of a container is
marked as `true`, and that container fails or stops for any
reason. Then, all other containers that are part of the task are
stopped. If the `essential` parameter of a container is
marked as `false`, then its failure doesn't affect the rest
of the containers in a task. If this parameter is omitted, a container
is assumed to be essential.

All tasks must have at least one essential container. Suppose that you
have an application that's composed of multiple containers. Then, group
containers that are used for a common purpose into components, and
separate the different components into multiple task definitions. For
more information, see [Architect your application for Amazon ECS](application_architecture.md "application_architecture.md").

```
"essential": true|false
```

`entryPoint`

###### Important

Early versions of the Amazon ECS container agent don't properly handle
`entryPoint` parameters. If you have problems using
`entryPoint`, update your container agent or enter
your commands and arguments as `command` array items
instead.

Type: String array

Required: No

The entry point that's passed to the container.

```
"entryPoint": ["string", ...]
```

`command`

Type: String array

Required: No

The command that's passed to the container. This parameter maps to
`Cmd` in the create-container command and the
`COMMAND` parameter to docker run. If there are multiple
arguments, make sure that each argument is a separated string in the
array.

```
"command": ["string", ...]
```

`workingDirectory`

Type: String

Required: No

The working directory to run commands inside the container in. This
parameter maps to `WorkingDir` in the
[Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/reference/api/engine/version/v1.38/ "https://docs.docker.com/reference/api/engine/version/v1.38/") and
the `--workdir` option to [**docker run**](https://docs.docker.com/reference/cli/docker/container/run/ "https://docs.docker.com/reference/cli/docker/container/run/").

```
"workingDirectory": "string"
```

`environmentFiles`

Type: Object array

Required: No

A list of files containing the environment variables to pass to a
container. This parameter maps to the `--env-file` option to
the docker run command.

You can specify up to 10 environment files. The file must have a
`.env` file extension. Each line in an environment file
contains an environment variable in `VARIABLE=VALUE` format.
Lines that start with `#` are treated as comments and are
ignored.

If there are individual environment variables specified in the
container definition, they take precedence over the variables contained
within an environment file. If multiple environment files are specified
that contain the same variable, they're processed from the top down. We
recommend that you use unique variable names. For more information, see
[Pass an individual environment
variable to an Amazon ECS container](taskdef-envfiles.md "taskdef-envfiles.md").

`value`

Type: String

Required: Yes

The Amazon Resource Name (ARN) of the Amazon S3 object
containing the environment variable file.

`type`

Type: String

Required: Yes

The file type to use. The only supported value is
`s3`.

`environment`

Type: Object array

Required: No

The environment variables to pass to a container. This parameter maps
to `Env` in the docker create-container command and the
`--env` option to the docker run command.

###### Important

We do not recommend using plaintext environment variables for
sensitive information, such as credential data.

`name`

Type: String

Required: Yes, when `environment` is
used

The name of the environment variable.

`value`

Type: String

Required: Yes, when `environment` is
used

The value of the environment variable.

```
"environment" : [
    { "name" : "string", "value" : "string" },
    { "name" : "string", "value" : "string" }
]
```

`secrets`

Type: Object array

Required: No

An object that represents the secret to expose to your container. For
more information, see [Pass sensitive data to an Amazon ECS
container](specifying-sensitive-data.md "specifying-sensitive-data.md").

`name`

Type: String

Required: Yes

The value to set as the environment variable on the
container.

`valueFrom`

Type: String

Required: Yes

The secret to expose to the container. The supported
values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret
or the full ARN of the parameter in the AWS Systems Manager Parameter
Store.

###### Note

If the Systems Manager Parameter Store parameter or Secrets Manager
parameter exists in the same AWS Region as the task
that you're launching, you can use either the full ARN
or name of the secret. If the parameter exists in a
different Region, then the full ARN must be
specified.

```
"secrets": [
    {
        "name": "environment_variable_name",
        "valueFrom": "arn:aws:ssm:`region`:`aws_account_id`:parameter/`parameter_name`"
    }
]
```

#### Security

`privileged`

Type: Boolean

Required: No

When this parameter is `true`, the container is given
elevated privileges on the host container instance (similar to the
`root` user). This parameter maps to
`Privileged` in the docker create-container command and the
`--privileged` option to docker run.

`user`

Type: String

Required: No

The user to use inside the container. This parameter maps to
`User` in the docker create-container command and the
`--user` option to docker run.

###### Important

When running tasks using the `host` network mode, don't
run containers using the root user (UID 0). We recommend using a
non-root user for better security.

You can specify the `user` using the following formats. If
specifying a UID or GID, you must specify it as a positive integer.

- `user`
- `user:group`
- `uid`
- `uid:gid`
- `user:gid`
- `uid:group`

`readonlyRootFilesystem`

Type: Boolean

Required: No

When this parameter is `true`, the container is given a
read-only root filesystem. This parameter maps to
`ReadonlyRootfs` in the docker create-container command and
the `--read-only` option to docker run.

`dockerSecurityOptions`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: String array

Required: No

A list of strings to provide custom labels for SELinux and AppArmor
multi-level security systems. This field isn't valid for containers in
tasks using Fargate.

`ulimits`

Type: Array of [Ulimit](../APIReference/API_Ulimit.md "../APIReference/API_Ulimit.md") objects

Required: No

A list of `ulimits` to set in the container. If a ulimit
value is specified in a task definition, it overrides the default values
set by Docker. This parameter maps to `Ulimits` in the docker
create-container command and the `--ulimit` option to docker
run. Valid naming values are displayed in the [Ulimit](../APIReference/API_Ulimit.md "../APIReference/API_Ulimit.md") data type.

Amazon ECS tasks that are hosted on Fargate use the default resource limit
values set by the operating system with the exception of the
`nofile` resource limit parameter which Fargate overrides.
The `nofile` resource limit sets a restriction on the number of
open files that a container can use. The default `nofile` soft
limit is `1024` and the default hard limit is
`65535`.

This parameter requires version 1.18 of the Docker Remote API or
greater on your container instance. To check the Docker Remote API version
on your container instance, log in to your container instance and run the
following command: `sudo docker version --format
 '{{.Server.APIVersion}}'`

`dockerLabels`

###### Note

This parameter isn't supported for containers that are hosted on
Amazon ECS Managed Instances.

Type: String to string map

Required: No

A key/value map of labels to add to the container. This parameter maps
to `Labels` in the docker create-container command and the
`--label` option to docker run.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance.

```
"dockerLabels": {"string": "string"
      ...}
```

#### Network settings

`disableNetworking`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: Boolean

Required: No

When this parameter is true, networking is off within the
container.

The default is `false`.

```
"disableNetworking": true|false
```

`links`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: String array

Required: No

The `link` parameter allows containers to communicate with
each other without the need for port mappings. This parameter is only
supported if the network mode of a task definition is set to
`bridge`. The `name:internalName` construct is
analogous to `name:alias` in Docker links.
Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed..

###### Important

Containers that are collocated on the same container instance
might communicate with each other without requiring links or host
port mappings. The network isolation on a container instance is
controlled by security groups and VPC settings.

```
"links": ["name:internalName", ...]
```

`hostname`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: String

Required: No

The hostname to use for your container. This parameter maps to
`Hostname` in the docker create-container and the
`--hostname` option to docker run.

```
"hostname": "string"
```

`dnsServers`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: String array

Required: No

A list of DNS servers that are presented to the container.

```
"dnsServers": ["string", ...]
```

`extraHosts`

###### Note

This parameter isn't supported for tasks
that use the `awsvpc` network mode.

Type: Object array

Required: No

A list of hostnames and IP address mappings to append to the
`/etc/hosts` file on the container.

This parameter maps to `ExtraHosts` in the docker
create-container command and the `--add-host` option to
docker run.

```
"extraHosts": [
      {
        "hostname": "string",
        "ipAddress": "string"
      }
      ...
    ]
```

`hostname`

Type: String

Required: Yes, when `extraHosts` are
used

The hostname to use in the `/etc/hosts`
entry.

`ipAddress`

Type: String

Required: Yes, when `extraHosts` are
used

The IP address to use in the
`/etc/hosts` entry.

#### Storage and logging

`readonlyRootFilesystem`

Type: Boolean

Required: No

When this parameter is true, the container is given read-only access
to its root file system. This parameter maps to
`ReadonlyRootfs` in the docker create-container command
the `--read-only` option to docker run.

The default is `false`.

```
"readonlyRootFilesystem": true|false
```

`mountPoints`

Type: Object array

Required: No

The mount points for the data volumes in your container. This parameter maps to `Volumes` in the
create-container Docker API and
the `--volume` option to docker run.

Windows containers can mount whole directories on the same drive as
`$env:ProgramData`. Windows containers cannot mount
directories on a different drive, and mount points cannot be used across
drives. You must specify mount points to attach an Amazon EBS volume directly to an Amazon ECS task.

`sourceVolume`

Type: String

Required: Yes, when `mountPoints` are
used

The name of the volume to mount.

`containerPath`

Type: String

Required: Yes, when `mountPoints` are
used

The path in the container where the volume will be mounted.

`readOnly`

Type: Boolean

Required: No

If this value is `true`, the container has
read-only access to the volume. If this value is
`false`, then the container can write to the
volume. The default value is `false`.

For tasks that run on EC2 instances running the Windows operating system, leave the value as the default of `false`.

`volumesFrom`

Type: Object array

Required: No

Data volumes to mount from another container. This parameter maps to
`VolumesFrom` in the docker create-container command and
the `--volumes-from` option to docker run.

`sourceContainer`

Type: String

Required: Yes, when `volumesFrom` is
used

The name of the container to mount volumes from.

`readOnly`

Type: Boolean

Required: No

If this value is `true`, the container has
read-only access to the volume. If this value is
`false`, then the container can write to the
volume. The default value is `false`.

```
"volumesFrom": [
                {
                  "sourceContainer": "string",
                  "readOnly": true|false
                }
              ]
```

`logConfiguration`

Type: [LogConfiguration](../APIReference/API_LogConfiguration.md "../APIReference/API_LogConfiguration.md") Object

Required: No

The log configuration specification for the container.

For example task definitions that use a log configuration, see [Example Amazon ECS task definitions](example_task_definitions.md "example_task_definitions.md").

This parameter maps to `LogConfig` in the docker
create-container command and the `--log-driver` option to
docker run. By default, containers use the same logging driver that the
Docker daemon uses. However, the container might use
a different logging driver than the Docker daemon by
specifying a log driver with this parameter in the container definition.
To use a different logging driver for a container, the log system must
be configured properly on the container instance (or on a different log
server for remote logging options).

Consider the following when specifying a log configuration for your
containers:

- Amazon ECS supports a subset of the logging drivers that are
  available to the Docker daemon.
- This parameter requires version 1.18 or later of the
  Docker Remote API on your container
  instance.

```
"logConfiguration": {
      "logDriver": "awslogs",""splunk", "awsfirelens",
      "options": {"`string`": "`string`"
        ...},
	"secretOptions": [{
		"name": "`string`",
		"valueFrom": "`string`"
	}]
}
```

`logDriver`

Type: String

Valid values:
`"awslogs","splunk","awsfirelens"`

Required: Yes, when `logConfiguration` is
used

The log driver to use for the container. By default, the
valid values that are listed earlier are log drivers that
the Amazon ECS container agent can communicate with.

The supported log drivers are `awslogs`,
`splunk`, and
`awsfirelens`.

For more information about how to use the
`awslogs` log driver in task definitions to
send your container logs to CloudWatch Logs, see [Send Amazon ECS logs to CloudWatch](using_awslogs.md "using_awslogs.md") .

For more information about using the
`awsfirelens` log driver, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

###### Note

If you have a custom driver that isn't listed, you can
fork the Amazon ECS container agent project that's [available on GitHub](https://github.com/aws/amazon-ecs-agent "https://github.com/aws/amazon-ecs-agent") and customize it to
work with that driver. We encourage you to submit pull
requests for changes that you want to have included.
However, we don't currently support running modified
copies of this software.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance.

`options`

Type: String to string map

Required: No

The key/value map of configuration options to send to the
log driver.

The options you can specify depend on the log driver. Some
of the options you can specify when you use the
`awslogs` router to route logs to Amazon CloudWatch
include the following:

`awslogs-create-group`

Required: No

Specify whether you want the log group to be
created automatically. If this option isn't
specified, it defaults to
`false`.

###### Note

Your IAM policy must include the
`logs:CreateLogGroup` permission before
you attempt to use
`awslogs-create-group`.

`awslogs-region`

Required: Yes

Specify the AWS Region that the
`awslogs` log driver is to send your
Docker logs to. You can choose to send all of your
logs from clusters in different Regions to a
single region in CloudWatch Logs. This is so that they're
all visible in one location. Otherwise, you can
separate them by Region for more granularity. Make
sure that the specified log group exists in the
Region that you specify with this option.

`awslogs-group`

Required: Yes

Make sure to specify a log group that the
`awslogs` log driver sends its log
streams to.

`awslogs-stream-prefix`

Required: Yes

Use the `awslogs-stream-prefix`
option to associate a log stream with the
specified prefix, the container name, and the ID
of the Amazon ECS task that the container belongs to.
If you specify a prefix with this option, then the
log stream takes the following format.

```
`prefix-name`/`container-name`/`ecs-task-id`
```

If you don't specify a prefix with this
option, then the log stream is named after the
container ID that's assigned by the Docker daemon
on the container instance. Because it's difficult
to trace logs back to the container that sent them
with just the Docker container ID (which is only
available on the container instance), we recommend
that you specify a prefix with this option.

For Amazon ECS services, you can use the service
name as the prefix. Doing so, you can trace log
streams to the service that the container belongs
to, the name of the container that sent them, and
the ID of the task that the container belongs
to.

You must specify a stream-prefix for your logs
to have your logs appear in the Log pane when
using the Amazon ECS console.

`awslogs-datetime-format`

Required: No

This option defines a multiline start pattern
in Python `strftime` format. A log
message consists of a line that matches the
pattern and any following lines that don’t match
the pattern. The matched line is the delimiter
between log messages.

One example of a use case for using this
format is for parsing output such as a stack dump,
which might otherwise be logged in multiple
entries. The correct pattern allows it to be
captured in a single entry.

For more information, see [awslogs-datetime-format](https://docs.docker.com/engine/logging/drivers/awslogs/#awslogs-datetime-format "https://docs.docker.com/engine/logging/drivers/awslogs/#awslogs-datetime-format").

You cannot configure both the
`awslogs-datetime-format` and
`awslogs-multiline-pattern`
options.

###### Note

Multiline logging performs regular
expression parsing and matching of all log
messages. This might have a negative impact on
logging performance.

`awslogs-multiline-pattern`

Required: No

This option defines a multiline start pattern
that uses a regular expression. A log message
consists of a line that matches the pattern and
any following lines that don’t match the pattern.
The matched line is the delimiter between log
messages.

For more information, see [awslogs-multiline-pattern](https://docs.docker.com/engine/logging/drivers/awslogs/#awslogs-multiline-pattern "https://docs.docker.com/engine/logging/drivers/awslogs/#awslogs-multiline-pattern").

This option is ignored if
`awslogs-datetime-format` is also
configured.

You cannot configure both the
`awslogs-datetime-format` and
`awslogs-multiline-pattern`
options.

###### Note

Multiline logging performs regular
expression parsing and matching of all log
messages. This might have a negative impact on
logging performance.

`mode`

Required: No

Valid values: `non-blocking` |
`blocking`

This option defines the delivery mode of log
messages from the container to the `awslogs` log
driver. The delivery
mode you choose affects application availability
when the flow of logs from the container is
interrupted.

If you use the `blocking` mode and
the flow of logs to CloudWatch is interrupted, calls
from container code to write to the
`stdout` and `stderr`
streams will block. The logging thread of the
application will block as a result. This may cause
the application to become unresponsive and lead to
container healthcheck failure.

If you use the `non-blocking` mode,
the container's logs are instead stored in an
in-memory intermediate buffer configured with the
`max-buffer-size` option. This prevents
the application from becoming unresponsive when
logs cannot be sent to CloudWatch. We recommend using
this mode if you want to ensure service
availability and are okay with some log loss. For
more information, see [Preventing log loss with non-blocking mode in the
`awslogs` container log
driver](https://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/ "https://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/").

`max-buffer-size`

Required: No

Default value: `1m`

When `non-blocking` mode is used,
the `max-buffer-size` log option
controls the size of the buffer that's used for
intermediate message storage. Make sure to specify
an adequate buffer size based on your application.
When the buffer fills up, further logs cannot be
stored. Logs that cannot be stored are lost.

To route logs using the `splunk` log router,
you need to specify a `splunk-token` and a
`splunk-url`.

When you use the `awsfirelens` log router to
route logs to an AWS service or AWS Partner Network destination for
log storage and analytics, you can set the
`log-driver-buffer-limit` option to limit the
number of events that are buffered in memory, before being
sent to the log router container. It can help to resolve
potential log loss issue because high throughput might
result in memory running out for the buffer inside of
Docker. For more information, see [Configuring Amazon ECS logs for high
throughput](firelens-docker-buffer-limit.md "firelens-docker-buffer-limit.md").

Other options you can specify when using
`awsfirelens` to route logs depend on the
destination. When you export logs to Amazon Data Firehose, you can
specify the AWS Region with `region` and a name
for the log stream with `delivery_stream`.

When you export logs to Amazon Kinesis Data Streams, you can specify an
AWS Region with `region` and a data stream name
with `stream`.

When you export logs to Amazon OpenSearch Service, you can specify
options like `Name`, `Host` (OpenSearch Service
endpoint without protocol), `Port`,
`Index`, `Type`,
`Aws_auth`, `Aws_region`,
`Suppress_Type_Name`, and
`tls`.

When you export logs to Amazon S3, you can specify the bucket
using the `bucket` option. You can also specify
`region`, `total_file_size`,
`upload_timeout`, and
`use_put_object` as options.

This parameter requires version 1.19 of the Docker Remote API or greater on your container instance.

`secretOptions`

Type: Object array

Required: No

An object that represents the secret to pass to the log
configuration. Secrets that are used in log configuration
can include an authentication token, certificate, or
encryption key. For more information, see [Pass sensitive data to an Amazon ECS
container](specifying-sensitive-data.md "specifying-sensitive-data.md").

`name`

Type: String

Required: Yes

The value to set as the environment variable
on the container.

`valueFrom`

Type: String

Required: Yes

The secret to expose to the log configuration
of the container.

```
"logConfiguration": {
	"logDriver": "splunk",
	"options": {
		"splunk-url": "https://cloud.splunk.com:8080",
		"splunk-token": "...",
		"tag": "...",
		...
	},
	"secretOptions": [{
		"name": "`splunk-token`",
		"valueFrom": "`/ecs/logconfig/splunkcred`"
	}]
}
```

`firelensConfiguration`

Type: [FirelensConfiguration](../APIReference/API_FirelensConfiguration.md "../APIReference/API_FirelensConfiguration.md") Object

Required: No

The FireLens configuration for the container. This is used to specify
and configure a log router for container logs. For more information, see
[Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

```
{
    "firelensConfiguration": {
        "type": "fluentd",
        "options": {
            "KeyName": ""
        }
    }
}
```

`options`

Type: String to string map

Required: No

The key/value map of options to use when configuring the
log router. This field is optional and can be used to
specify a custom configuration file or to add additional
metadata, such as the task, task definition, cluster, and
container instance details to the log event. If specified,
the syntax to use is
`"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::`amzn-s3-demo-bucket`/fluent.conf|filepath"}`.
For more information, see [Example Amazon ECS task definition: Route logs to FireLens](firelens-taskdef.md "firelens-taskdef.md").

`type`

Type: String

Required: Yes

The log router to use. The valid values are
`fluentd` or `fluentbit`.

#### Resource requirements

`resourceRequirements`

Type: Array of [ResourceRequirement](../APIReference/API_ResourceRequirement.md "../APIReference/API_ResourceRequirement.md") objects

Required: No

The type and amount of a resource to assign to a container. The only
supported resource is a GPU.

`type`

Type: String

Required: Yes

The type of resource to assign to a container. The supported
value is `GPU`.

`value`

Type: String

Required: Yes

The value for the specified resource type.

If the `GPU` type is used, the value is the number of
physical `GPUs` the Amazon ECS container agent reserves for
the container. The number of GPUs that's reserved for all
containers in a task can't exceed the number of available GPUs on
the container instance the task is launched on.

GPUs aren't available for tasks that are running on Fargate.

#### Container timeouts

`startTimeout`

Type: Integer

Required: No

Example values: `120`

Time duration (in seconds) to wait before giving up on resolving
dependencies for a container.

For example, you specify two containers in a task definition with
`containerA` having a dependency on
`containerB` reaching a `COMPLETE`,
`SUCCESS`, or `HEALTHY` status. If a
`startTimeout` value is specified for
`containerB` and it doesn't reach the desired status
within that time, then `containerA` doesn't start.

###### Note

If a container doesn't meet a dependency constraint or times out
before meeting the constraint, Amazon ECS doesn't progress dependent
containers to their next state.

The maximum
value is 600 seconds (10 minutes).

`stopTimeout`

Type: Integer

Required: No

Example values: `120`

Time duration (in seconds) to wait before the container is forcefully
killed if it doesn't exit normally on its own.

If the parameter
isn't specified, then the default value of 30 seconds is used. The
maximum value is 86400 seconds (24 hours).

#### Container dependency

`dependsOn`

Type: Array of [ContainerDependency](../APIReference/API_ContainerDependency.md "../APIReference/API_ContainerDependency.md") objects

Required: No

The dependencies defined for container startup and shutdown. A
container can contain multiple dependencies. When a dependency is
defined for container startup, for container shutdown it is reversed.
For an example, see [Container
dependency](example_task_definitions.md#example_task_definition-containerdependency "example_task_definitions.md#example_task_definition-containerdependency").

###### Note

If a container doesn't meet a dependency constraint or times out
before meeting the constraint, Amazon ECS doesn't progress dependent
containers to their next state.

This parameter requires that the task or service uses platform version
`1.3.0` or later (Linux) or
`1.0.0` (Windows).

```
"dependsOn": [
    {
        "containerName": "`string`",
        "condition": "`string`"
    }
]
```

`containerName`

Type: String

Required: Yes

The container name that must meet the specified
condition.

`condition`

Type: String

Required: Yes

The dependency condition of the container. The following
are the available conditions and their behavior:

- `START` – This condition emulates
  the behavior of links and volumes today. The
  condition validates that a dependent container is
  started before permitting other containers to
  start.
- `COMPLETE` – This condition
  validates that a dependent container runs to
  completion (exits) before permitting other
  containers to start. This can be useful for
  non-essential containers that run a script and then
  exit. This condition can't be set on an essential
  container.
- `SUCCESS` – This condition is the
  same as `COMPLETE`, but it also requires
  that the container exits with a `zero`
  status. This condition can't be set on an essential
  container.
- `HEALTHY` – This condition
  validates that the dependent container passes its
  container health check before permitting other
  containers to start. This requires that the
  dependent container has health checks configured in
  the task definition. This condition is confirmed
  only at task startup.

#### System controls

`systemControls`

Type: [SystemControl](../APIReference/API_SystemControl.md "../APIReference/API_SystemControl.md") object

Required: No

A list of namespace kernel parameters to set in the container. This
parameter maps to `Sysctls` in the docker create-container
commandand the `--sysctl` option to docker run. For example,
you can configure `net.ipv4.tcp_keepalive_time` setting to
maintain longer lived connections.

We don't recommend that you specify network-related
`systemControls` parameters for multiple containers in a
single task that also uses either the `awsvpc` or
`host` network mode. Doing this has the following
disadvantages:

- If you set `systemControls` for any container, it
  applies to all containers in the task. If you set different
  `systemControls` for multiple containers in a
  single task, the container that's started last determines which
  `systemControls` take effect.

If you're setting an IPC resource namespace to use for the containers
in the task, the following conditions apply to your system controls. For
more information, see [IPC mode](task_definition_parameters.md#task_definition_ipcmode "task_definition_parameters.md#task_definition_ipcmode").

- For tasks that use the `host` IPC mode, IPC
  namespace `systemControls` aren't supported.
- For tasks that use the `task` IPC mode, IPC
  namespace `systemControls` values apply to all
  containers within a task.

```
"systemControls": [
    {
         "namespace":"`string`",
         "value":"`string`"
    }
]
```

`namespace`

Type: String

Required: No

The namespace kernel parameter to set a `value`
for.

Valid IPC namespace values: `"kernel.msgmax" |
 "kernel.msgmnb" | "kernel.msgmni" | "kernel.sem" |
 "kernel.shmall" | "kernel.shmmax" | "kernel.shmmni" |
 "kernel.shm_rmid_forced"`, and
`Sysctls` that start with
`"fs.mqueue.*"`

Valid network namespace values: `Sysctls` that
start with `"net.*"`. On Fargate, only
namespaced `Sysctls` that exist within the
container are accepted.

All of these values are supported by
Fargate.

`value`

Type: String

Required: No

The value for the namespace kernel parameter that's
specified in `namespace`.

#### Interactive

`interactive`

Type: Boolean

Required: No

When this parameter is `true`, you can deploy containerized
applications that require `stdin` or a `tty` to be
allocated. This parameter maps to `OpenStdin` in the docker
create-container command and the `--interactive` option to
docker run.

The default is `false`.

#### Pseudo terminal

`pseudoTerminal`

Type: Boolean

Required: No

When this parameter is `true`, a TTY is allocated. This
parameter maps to `Tty` in the docker create-container
command and the `--tty` option to docker run.

The default is `false`.

### Linux parameters

`linuxParameters`

Type: [LinuxParameters](../APIReference/API_LinuxParameters.md "../APIReference/API_LinuxParameters.md") object

Required: No

Linux-specific modifications that are applied to the container, such as
Linux kernel capabilities.

`capabilities`

Type: [KernelCapabilities](../APIReference/API_KernelCapabilities.md "../APIReference/API_KernelCapabilities.md") object

Required: No

The Linux capabilities for the container that are added to or
dropped from the default configuration provided by Docker.

`devices`

Type: Array of [Device](../APIReference/API_Device.md "../APIReference/API_Device.md") objects

Required: No

Any host devices to expose to the container. This parameter maps
to `Devices` in the docker create-container command and
the `--device` option to docker run.

`initProcessEnabled`

Type: Boolean

Required: No

Run an `init` process inside the container that
forwards signals and reaps processes. This parameter maps to the
`--init` option to docker run.

`maxSwap`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: Integer

Required: No

The total amount of swap memory (in MiB) a container can use. This
parameter is translated to the `--memory-swap` option to
docker run where the value is the sum of the container memory plus
the `maxSwap` value.

`swappiness`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: Integer

Required: No

This allows you to tune a container's memory swappiness behavior.
A `swappiness` value of `0` causes swapping
not to happen unless absolutely necessary. A
`swappiness` value of `100` causes pages
to be swapped very aggressively. Valid values are whole numbers
between `0` and `100`. If the
`swappiness` parameter isn't specified, a default
value of `60` is used. If a value isn't specified for
`maxSwap`, then this parameter is ignored. This
parameter maps to the `--memory-swappiness` option to
docker run.

`sharedMemorySize`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: Integer

Required: No

The size (in MiB) of the `/dev/shm` volume. This
parameter maps to the `--shm-size` option to docker
run.

`tmpfs`

###### Note

This parameter isn't supported for tasks running on Amazon ECS Managed Instances.

Type: Array of [Tmpfs](../APIReference/API_Tmpfs.md "../APIReference/API_Tmpfs.md") objects

Required: No

The container path, mount options, and size (in MiB) of the tmpfs
mount. This parameter maps to the `--tmpfs` option to
docker run.
