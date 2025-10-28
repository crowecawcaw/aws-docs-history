# Reference: Amazon EC2 launch template examples

The following are example MIME multi-part files that you can use to create your own templates.

###### Examples

- [Example: Mount an existing Amazon EFS file
  system](#example-mount-an-existing-amazon-efs-file-system "#example-mount-an-existing-amazon-efs-file-system")
- [Example: Override default Amazon ECS
  container agent configuration](#example-override-default-amazon-ecs-container-agent-configuration "#example-override-default-amazon-ecs-container-agent-configuration")
- [Example: Mount an existing
  Amazon FSx for Lustre file system](#example-mount-an-existing-amazon-fsx-for-lustre-file-system "#example-mount-an-existing-amazon-fsx-for-lustre-file-system")

## Example: Mount an existing Amazon EFS file

system

This example MIME multi-part file configures the compute resource to install the `amazon-efs-utils`
package and mount an existing Amazon EFS file system at `/mnt/efs`.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- amazon-efs-utils

runcmd:
- file_system_id_01=`fs-abcdef123`
- efs_directory=/mnt/efs

- mkdir -p ${efs_directory}
- echo "${file_system_id_01}:/ ${efs_directory} efs tls,_netdev" >> /etc/fstab
- mount -a -t efs defaults

--==MYBOUNDARY==--
```

## Example: Override default Amazon ECS

container agent configuration

This example MIME multi-part file overrides the default Docker image cleanup settings for a compute
resource.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
echo ECS_IMAGE_CLEANUP_INTERVAL=60m >> /etc/ecs/ecs.config
echo ECS_IMAGE_MINIMUM_CLEANUP_AGE=60m >> /etc/ecs/ecs.config

--==MYBOUNDARY==--
```

## Example: Mount an existing

Amazon FSx for Lustre file system

This example MIME multi-part file configures the compute resource to install the `lustre2.10`
package from the Extras Library and mount an existing FSx for Lustre file system at `/scratch` and
a mount name of `fsx`. This example is for Amazon Linux 2. For installation instructions for other Linux
distributions, see [Installing
the Lustre Client](../../../fsx/latest/LustreGuide/install-lustre-client.md "../../../fsx/latest/LustreGuide/install-lustre-client.md") in the _Amazon FSx for Lustre User Guide_. For more information, see [Mounting your Amazon FSx file system
automatically](../../../fsx/latest/LustreGuide/mount-fs-auto-mount-onreboot.md "../../../fsx/latest/LustreGuide/mount-fs-auto-mount-onreboot.md") in the _Amazon FSx for Lustre User Guide_.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- file_system_id_01=`fs-0abcdef1234567890`
- region=`us-east-2`
- fsx_directory=`/scratch`
- amazon-linux-extras install -y lustre2.10
- mkdir -p ${fsx_directory}
- mount -t lustre ${file_system_id_01}.fsx.${region}.amazonaws.com@tcp:`fsx` ${fsx_directory}

--==MYBOUNDARY==--
```

In the [volumes](../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-volumes "../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-volumes") and [mountPoints](../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-mountPoints "../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-mountPoints") members of the container properties the mount points must be mapped into the
container.

```
{
    "volumes": [
        {
            "host": {
                "sourcePath": "`/scratch`"
            },
            "name": "`Scratch`"
        }
    ],
    "mountPoints": [
        {
            "containerPath": "`/scratch`",
            "sourceVolume": "`Scratch`"
        }
    ],
}
```
