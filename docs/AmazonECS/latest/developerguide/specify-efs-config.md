# Specify an Amazon EFS file system in an Amazon ECS task definition

To use Amazon EFS file system volumes for your containers, you must specify the volume
and mount point configurations in your task definition. The following task
definition JSON snippet shows the syntax for the `volumes` and
`mountPoints` objects for a container.

```
{
    "containerDefinitions": [
        {
            "name": "`container-using-efs`",
            "image": "`public.ecr.aws/amazonlinux/amazonlinux:latest`",
            "entryPoint": [
                "sh",
                "-c"
            ],
            "command": [
                "ls -la `/mount/efs`"
            ],
            "mountPoints": [
                {
                    "sourceVolume": "`myEfsVolume`",
                    "containerPath": "`/mount/efs`",
                    "readOnly": `true`
                }
            ]
        }
    ],
    "volumes": [
        {
            "name": "`myEfsVolume`",
            "efsVolumeConfiguration": {
                "fileSystemId": "`fs-1234`",
                "rootDirectory": "`/path/to/my/data`",
                "transitEncryption": "`ENABLED`",
                "transitEncryptionPort": `integer`,
                "authorizationConfig": {
                    "accessPointId": "`fsap-1234`",
                    "iam": "`ENABLED`"
                }
            }
        }
    ]
}
```

`efsVolumeConfiguration`

Type: Object

Required: No

This parameter is specified when using Amazon EFS volumes.

`fileSystemId`

Type: String

Required: Yes

The Amazon EFS file system ID to use.

`rootDirectory`

Type: String

Required: No

The directory within the Amazon EFS file system to mount as the
root directory inside the host. If this parameter is
omitted, the root of the Amazon EFS volume is used. Specifying
`/` has the same effect as omitting this
parameter.

###### Important

If an EFS access point is specified in the
`authorizationConfig`, the root directory
parameter must either be omitted or set to
`/`, which enforces the path set on the
EFS access point.

`transitEncryption`

Type: String

Valid values: `ENABLED` |
`DISABLED`

Required: No

Specifies whether to enable encryption for Amazon EFS data in
transit between the Amazon ECS host and the Amazon EFS server. If
Amazon EFS IAM authorization is used, transit encryption must be
enabled. If this parameter is omitted, the default value of
`DISABLED` is used. For more information, see
[Encrypting Data in Transit](../../../efs/latest/ug/encryption-in-transit.md "../../../efs/latest/ug/encryption-in-transit.md") in the
_Amazon Elastic File System User Guide_.

`transitEncryptionPort`

Type: Integer

Required: No

The port to use when sending encrypted data between the
Amazon ECS host and the Amazon EFS server. If you don't specify a
transit encryption port, it uses the port selection strategy
that the Amazon EFS mount helper uses. For more information, see
[EFS Mount
Helper](../../../efs/latest/ug/efs-mount-helper.md "../../../efs/latest/ug/efs-mount-helper.md") in the
_Amazon Elastic File System User Guide_.

`authorizationConfig`

Type: Object

Required: No

The authorization configuration details for the Amazon EFS file
system.

`accessPointId`

Type: String

Required: No

The access point ID to use. If an access point
is specified, the root directory value in the
`efsVolumeConfiguration` must either be
omitted or set to `/`, which enforces
the path set on the EFS access point. If an access
point is used, transit encryption must be enabled
in the `EFSVolumeConfiguration`. For
more information, see [Working
with Amazon EFS Access Points](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") in the
_Amazon Elastic File System User Guide_.

`iam`

Type: String

Valid values: `ENABLED` |
`DISABLED`

Required: No

Specifies whether to use the Amazon ECS task IAM
role defined in a task definition when mounting
the Amazon EFS file system. If enabled, transit
encryption must be enabled in the
`EFSVolumeConfiguration`. If this
parameter is omitted, the default value of
`DISABLED` is used. For more
information, see [IAM Roles for Tasks](task-iam-roles.md "task-iam-roles.md").
