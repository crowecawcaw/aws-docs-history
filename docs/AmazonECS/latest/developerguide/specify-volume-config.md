# Specify a Docker volume in an Amazon ECS task definition

Before your containers can use data volumes, you must specify the volume and mount
point configurations in your task definition. This section describes the volume
configuration for a container. For tasks that use a Docker volume, specify a
`dockerVolumeConfiguration`. For tasks that use a bind mount host
volume, specify a `host` and optional `sourcePath`.

The following task definition JSON shows the syntax for the `volumes`
and `mountPoints` objects for a container.

```
{
    "containerDefinitions": [
        {
            "mountPoints": [
                {
                    "sourceVolume": "`string`",
                    "containerPath": "`/path/to/mount_volume`",
                    "readOnly": boolean
                }
            ]
        }
    ],
    "volumes": [
        {
            "name": "`string`",
            "dockerVolumeConfiguration": {
                "scope": "`string`",
                "autoprovision": boolean,
                "driver": "`string`",
                "driverOpts": {
                    "`key`": "`value`"
                },
                "labels": {
                    "`key`": "`value`"
                }
            }
        }
    ]
}
```

`name`

Type: String

Required: No

The name of the volume. Up to 255 letters (uppercase and lowercase),
numbers, hyphens (`-`), and underscores (`_`) are allowed. This name is referenced
in the `sourceVolume` parameter of the container definition
`mountPoints` object.

`dockerVolumeConfiguration`

Type: [DockerVolumeConfiguration](../APIReference/API_DockerVolumeConfiguration.md "../APIReference/API_DockerVolumeConfiguration.md") Object

Required: No

This parameter is specified when using Docker volumes. Docker volumes are
supported only when running tasks on EC2 instances. Windows containers support only
the use of the `local` driver. To use bind mounts, specify a
`host` instead.

`scope`

Type: String

Valid Values: `task` | `shared`

Required: No

The scope for the Docker volume, which determines its lifecycle. Docker volumes that are scoped to a `task` are
automatically provisioned when the task starts and destroyed when the task stops. Docker volumes
that are scoped as `shared` persist after the task stops.

`autoprovision`

Type: Boolean

Default value: `false`

Required: No

If this value is `true`, the Docker volume is created if it
doesn't already exist. This field is used only if the `scope` is
`shared`. If the `scope` is `task`, then this parameter must be omitted.

`driver`

Type: String

Required: No

The Docker volume driver to use. The driver value must match the driver
name provided by Docker because this name is used for task placement. If the driver
was installed by using the Docker plugin CLI, use `docker plugin ls`
to retrieve the driver name from your container instance. If the driver was
installed by using another method, use Docker plugin discovery to retrieve the
driver name.

`driverOpts`

Type: String

Required: No

A map of Docker driver-specific options to pass through. This parameter
maps to `DriverOpts` in the Create a
volume section of Docker.

`labels`

Type: String

Required: No

Custom metadata to add to your Docker volume.

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
