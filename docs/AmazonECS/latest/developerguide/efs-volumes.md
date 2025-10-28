# Use Amazon EFS volumes with Amazon ECS

Amazon Elastic File System (Amazon EFS) provides simple, scalable file storage for use with your Amazon ECS
tasks. With Amazon EFS, storage capacity is elastic. It grows and shrinks automatically as
you add and remove files. Your applications can have the storage they need and when they
need it.

You can use Amazon EFS file systems with Amazon ECS to export file system data across your fleet
of container instances. That way, your tasks have access to the same persistent storage,
no matter the instance on which they land. Your task definitions must reference volume
mounts on the container instance to use the file system.

For a tutorial, see [Configuring Amazon EFS file systems for Amazon ECS using the
console](tutorial-efs-volumes.md "tutorial-efs-volumes.md").

## Considerations

Consider the following when using Amazon EFS volumes:

- For tasks that run on EC2, Amazon EFS file system
  support was added as a public preview with Amazon ECS-optimized AMI version
  `20191212` with container agent version 1.35.0. However,
  Amazon EFS file system support entered general availability with
  Amazon ECS-optimized AMI version `20200319` with container agent version
  1.38.0, which contained the Amazon EFS access point and IAM authorization
  features. We recommend that you use Amazon ECS-optimized AMI version
  `20200319` or later to use these features. For more
  information, see [Amazon ECS-optimized Linux AMIs](ecs-optimized_AMI.md "ecs-optimized_AMI.md").

###### Note

If you create your own AMI, you must use container agent 1.38.0 or
later, `ecs-init` version 1.38.0-1 or later, and run the
following commands on your Amazon EC2 instance to enable the Amazon ECS volume
plugin. The commands are dependent on whether you're using Amazon Linux 2 or Amazon Linux
as your base image.

Amazon Linux 2

```
`yum install amazon-efs-utils
systemctl enable --now amazon-ecs-volume-plugin`
```

Amazon Linux

```
`yum install amazon-efs-utils
sudo shutdown -r now`
```

- For tasks that are hosted on Fargate, Amazon EFS file systems are supported
  on platform version 1.4.0 or later (Linux). For more information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").
- When using Amazon EFS volumes for tasks that are hosted on Fargate, Fargate
  creates a supervisor container that's responsible for managing the Amazon EFS volume.
  The supervisor container uses a small amount of the task's memory and CPU. The
  supervisor container is visible when querying the task metadata version 4
  endpoint. Additionally, it is visible in CloudWatch Container Insights as the container name
  `aws-fargate-supervisor`. For more information when using the
  EC2, see [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md"). For more information when using
  the Fargate, see [Amazon ECS task metadata endpoint version 4 for
  tasks on Fargate](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md").
- Using Amazon EFS volumes or specifying an `EFSVolumeConfiguration`
  isn't supported on external instances.
- Using Amazon EFS volumes is supported for tasks that run on Amazon ECS Managed Instances.
- We recommend that you set the
  `ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION` parameter in the
  agent configuration file to a value that is less than the default (about 1
  hour). This change helps prevent EFS mount credential expiration and allows
  for cleanup of mounts that are not in use. For more
  information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

## Use Amazon EFS access points

Amazon EFS access points are application-specific entry points into an EFS file system
for managing application access to shared datasets. For more information about Amazon EFS
access points and how to control access to them, see [Working with Amazon EFS Access
Points](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") in the _Amazon Elastic File System User Guide_.

Access points can enforce a user identity, including the user's POSIX groups, for
all file system requests that are made through the access point. Access points can
also enforce a different root directory for the file system. This is so that clients
can only access data in the specified directory or its subdirectories.

###### Note

When creating an EFS access point, specify a path on the file system to serve
as the root directory. When referencing the EFS file system with an access point
ID in your Amazon ECS task definition, the root directory must either be omitted or
set to `/`, which enforces the path set on the EFS access
point.

You can use an Amazon ECS task IAM role to enforce that specific applications use a
specific access point. By combining IAM policies with access points, you can
provide secure access to specific datasets for your applications. For more
information about how to use task IAM roles, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").
