# Specify Amazon EBS volume configuration at Amazon ECS deployment

After you register a task definition with the `configuredAtLaunch`
parameter set to `true`, you can configure an Amazon EBS volume at deployment when
you run a standalone task, or when you create or update a service. For more information
about deferring volume configuration to launch time using the
`configuredAtLaunch` parameter, see [Defer volume configuration to launch time in an Amazon ECS task definition](specify-ebs-config.md "specify-ebs-config.md").

To configure a volume, you can use the Amazon ECS APIs, or you can pass a JSON file as
input for the following AWS CLI commands:

- `run-task` to run a standalone ECS task.
- `start-task`
  to run a standalone ECS task in a specific container instance. This command is
  not applicable for Fargate tasks.
- `create-service` to create a new ECS service.
- `update-service` to update an existing service.

###### Note

For a container in your task to write to the mounted Amazon EBS volume, the container must have appropriate file system permissions. When you specify a non-root user in your container definition, Amazon ECS automatically configures the volume with group-based permissions that allow the specified user to read and write to the volume. If no user is specified, the container runs as root and has full access to the volume.

You can also configure an Amazon EBS volume by using the AWS Management Console. For more information,
see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md"),
[Creating an Amazon ECS rolling update deployment](create-service-console-v2.md "create-service-console-v2.md"), and [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").

The following JSON snippet shows all the parameters of an Amazon EBS volume that can be
configured at deployment. To use these parameters for volume configuration, replace the
`user input placeholders` with your own
information. For more information about these parameters, see [Volume configurations](service_definition_parameters.md#sd-volumeConfigurations "service_definition_parameters.md#sd-volumeConfigurations").

```
"volumeConfigurations": [
        {
            "name": "`ebs-volume`",
            "managedEBSVolume": {
                "encrypted": `true`,
                "kmsKeyId": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
                "volumeType": "`gp3`",
                "sizeInGiB": `10`,
                "snapshotId": "`snap-12345`",
                "volumeInitializationRate":`100`,
                "iops": `3000`,
                "throughput": `125`,
                "tagSpecifications": [
                    {
                        "resourceType": "volume",
                        "tags": [
                            {
                                "key": "`key1`",
                                "value": "`value1`"
                            }
                        ],
                        "propagateTags": "`NONE`"
                    }
                ],
                "roleArn": "arn:aws:iam::`1111222333`:role/ecsInfrastructureRole",
                 "terminationPolicy": {
                    "deleteOnTermination": `true`//can't be configured for service-managed tasks, always true
                },
                "filesystemType": "`ext4`"
            }
        }
    ]
```

###### Important

Ensure that the `volumeName` you specify in the configuration is the
same as the `volumeName` you specify in your task definition.

For information about checking the status of volume attachment, see [Troubleshooting Amazon EBS volume attachments to Amazon ECS tasks](troubleshoot-ebs-volumes.md "troubleshoot-ebs-volumes.md"). For
information about the Amazon ECS infrastructure AWS Identity and Access Management (IAM) role necessary for EBS
volume attachment, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

The following are JSON snippet examples that show the configuration of Amazon EBS volumes.
These examples can be used by saving the snippets in JSON files and passing the files as
parameters (using the `--cli-input-json
 file://`filename`parameter) for AWS CLI commands.
 Replace the`user input placeholders`` with your
own information.

## Configure a volume for a standalone task

The following snippet shows the syntax for configuring Amazon EBS volumes for
attachment to a standalone task. The following JSON snippet shows the syntax for
configuring the `volumeType`, `sizeInGiB`,
`encrypted`, and `kmsKeyId` settings. The configuration
specified in the JSON file is used to create and attach an EBS volume to the
standalone task.

```
{
   "cluster": "`mycluster`",
   "taskDefinition": "`mytaskdef`",
   "volumeConfigurations": [
        {
            "name": "`datadir`",
            "managedEBSVolume": {
                "volumeType": "`gp3`",
                "sizeInGiB": `100`,
                "roleArn":"arn:aws:iam::`1111222333`:role/ecsInfrastructureRole",
                "encrypted": `true`,
                "kmsKeyId": "arn:aws:kms:`region`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
            }
        }
   ]
}
```

## Configure a volume at service creation

The following snippet shows the syntax for configuring Amazon EBS volumes for
attachment to tasks managed by a service. The volumes are sourced from the snapshot
specified using the `snapshotId` parameter at a rate of 200 MiB/s. The
configuration specified in the JSON file is used to create and attach an EBS volume
to each task managed by the service.

```
{
   "cluster": "`mycluster`",
   "taskDefinition": "`mytaskdef`",
   "serviceName": "`mysvc`",
   "desiredCount": `2`,
   "volumeConfigurations": [
        {
            "name": "`myEbsVolume`",
            "managedEBSVolume": {
              "roleArn":"arn:aws:iam::`1111222333`:role/ecsInfrastructureRole",
              "snapshotId": "`snap-12345`",
              "volumeInitializationRate": 200
            }
        }
   ]
}
```

## Configure a volume at service update

The following JSON snippet shows the syntax for updating a service that previously
did not have Amazon EBS volumes configured for attachment to tasks. You must provide the
ARN of a task definition revision with `configuredAtLaunch` set to
`true`. The following JSON snippet shows the syntax for configuring
the `volumeType`, `sizeInGiB`, `throughput`, and
`iops`, and `filesystemType` settings. This configuration
is used to create and attach an EBS volume to each task managed by the
service.

```
{
   "cluster": "`mycluster`",
   "taskDefinition": "`mytaskdef`",
   "service": "`mysvc`",
   "desiredCount": `2`,
   "volumeConfigurations": [
        {
            "name": "`myEbsVolume`",
            "managedEBSVolume": {
              "roleArn":"arn:aws:iam::`1111222333`:role/ecsInfrastructureRole",
               "volumeType": "`gp3`",
                "sizeInGiB": `100`,
                 "iops": `3000`,
                "throughput": `125`,
                "filesystemType": "`ext4`"
            }
        }
   ]
}
```

### Configure a service to no longer utilize Amazon EBS volumes

The following JSON snippet shows the syntax for updating a service to no
longer utilize Amazon EBS volumes. You must provide the ARN of a task definition
with `configuredAtLaunch` set to `false`, or a task
definition without the `configuredAtLaunch` parameter. You must also
provide an empty `volumeConfigurations` object.

```
{
   "cluster": "`mycluster`",
   "taskDefinition": "`mytaskdef`",
   "service": "`mysvc`",
   "desiredCount": `2`,
   "volumeConfigurations": []
}
```

## Termination policy for Amazon EBS volumes

When an Amazon ECS task terminates, Amazon ECS uses the `deleteOnTermination`
value to determine whether the Amazon EBS volume that's associated with the terminated
task should be deleted. By default, EBS volumes that are attached to tasks are
deleted when the task is terminated. For standalone tasks, you can change this
setting to instead preserve the volume upon task termination.

###### Note

Volumes that are attached to tasks that are managed by a service are not
preserved and are always deleted upon task termination.

## Tag Amazon EBS volumes

You can tag Amazon EBS volumes by using the `tagSpecifications` object.
Using the object, you can provide your own tags and set propagation of tags from the
task definition or the service, depending on whether the volume is attached to a
standalone task or a task in a service. The maximum number of tags that can be
attached to a volume is 50.

###### Important

Amazon ECS automatically attaches the `AmazonECSCreated` and
`AmazonECSManaged` reserved tags to an Amazon EBS volume. This means
you can control the attachment of a maximum of 48 additional tags to a volume.
These additional tags can be user-defined, ECS-managed, or propagated
tags.

If you want to add Amazon ECS-managed tags to your volume, you must set
`enableECSManagedTags` to `true` in your
`UpdateService`, `CreateService`,`RunTask` or
`StartTask` call. If you turn on Amazon ECS-managed tags, Amazon ECS will tag
the volume automatically with cluster and service information
(`aws:ecs:`clusterName`` and
 `aws:ecs:`serviceName``). For more
information about tagging Amazon ECS resources, see [Tagging your Amazon ECS
resources](ecs-using-tags.md "ecs-using-tags.md").

The following JSON snippet shows the syntax for tagging each Amazon EBS volume that is
attached to each task in a service with a user-defined tag. To use this example for
creating a service, replace the `user input
 placeholders` with your own information.

```
{
   "cluster": "`mycluster`",
   "taskDefinition": "`mytaskdef`",
   "serviceName": "`mysvc`",
   "desiredCount": `2`,
   "enableECSManagedTags": true,
   "volumeConfigurations": [
        {
            "name": "`datadir`",
            "managedEBSVolume": {
                "volumeType": "`gp3`",
                "sizeInGiB": `100`,
                 "tagSpecifications": [
                    {
                        "resourceType": "volume",
                        "tags": [
                            {
                                "key": "`key1`",
                                "value": "`value1`"
                            }
                        ],
                        "propagateTags": "`NONE`"
                    }
                ],
                "roleArn":"arn:aws:iam:`1111222333`:role/ecsInfrastructureRole",
                "encrypted": `true`,
                "kmsKeyId": "arn:aws:kms:`region`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
            }
        }
   ]
}
```

###### Important

You must specify a `volume` resource type to tag Amazon EBS
volumes.
