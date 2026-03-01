# Specify a bind mount in an Amazon ECS task definition

For Amazon ECS tasks that are hosted on either
Fargate or Amazon EC2 instances, the following task
definition JSON snippet shows the syntax for the `volumes`,
`mountPoints`, and `ephemeralStorage` objects for a task
definition.

```
{
   "family": "",
   ...
   "containerDefinitions" : [
      {
         "mountPoints" : [
            {
               "containerPath" : "`/path/to/mount_volume`",
               "sourceVolume" : "`string`"
            }
          ],
          "name" : "`string`"
       }
    ],
    ...
    "volumes" : [
       {
          "name" : "`string`"
       }
    ],
    "ephemeralStorage": {
	   "sizeInGiB": `integer`
    }
}
```

For Amazon ECS tasks that are hosted on Amazon EC2 instances, you can use the
optional `host` parameter and a `sourcePath` when specifying
the task volume details. When it's specified, it ties the bind mount to the
lifecycle of the task rather than the container.

```
"volumes" : [
    {
        "host" : {
            "sourcePath" : "`string`"
        },
        "name" : "`string`"
    }
]
```

The following describes each task definition parameter in more detail.

`name`

Type: String

Required: No

The name of the volume. Up to 255 letters (uppercase and lowercase),
numbers, hyphens (`-`), and underscores (`_`) are allowed. This name is referenced
in the `sourceVolume` parameter of the container definition
`mountPoints` object.

`host`

Required: No

The `host` parameter is used to tie the lifecycle of the bind
mount to the host Amazon EC2 instance, rather than the task, and where it
is stored. If the `host` parameter is empty, then the Docker
daemon assigns a host path for your data volume, but the data is not
guaranteed to persist after the containers associated with it stop
running.

Windows containers can mount whole directories on the same drive as
`$env:ProgramData`.

###### Note

The `sourcePath` parameter is supported only when using tasks that are hosted on Amazon EC2 instances.

`sourcePath`

Type: String

Required: No

When the `host` parameter is used, specify a
`sourcePath` to declare the path on the host
Amazon EC2 instance that is presented to the container. If
this parameter is empty, then the Docker daemon assigns
a host path for you. If the `host` parameter
contains a `sourcePath` file location, then the
data volume persists at the specified location on the host
Amazon EC2 instance until you delete it manually. If the
`sourcePath` value does not exist on the host
Amazon EC2 instance, the Docker daemon creates it. If the
location does exist, the contents of the source path folder
are exported.

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

`ephemeralStorage`

Type: Object

Required: No

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate using platform version `1.4.0` or later (Linux) or `1.0.0` or later (Windows).

You can use the Copilot CLI, CloudFormation, the AWS SDK or the CLI to specify ephemeral storage for a bind mount.
