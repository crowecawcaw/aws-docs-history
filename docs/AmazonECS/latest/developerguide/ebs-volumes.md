# Use Amazon EBS volumes with Amazon ECS

Amazon Elastic Block Store (Amazon EBS) volumes provide highly available, cost-effective, durable,
high-performance block storage for data-intensive workloads. Amazon EBS volumes can be used with
Amazon ECS tasks for high throughput and transaction-intensive applications. For more information about Amazon EBS volumes, see [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") in the _Amazon EBS
User Guide_.

Amazon EBS volumes that are attached to Amazon ECS
tasks are managed by Amazon ECS on your behalf. During standalone task launch, you can provide the configuration that will be used to
attach one EBS volume to the task. During service creation or update, you can provide the
configuration that will be used to attach one EBS volume per task to each task managed by
the Amazon ECS service. You can either configure new, empty volumes for attachment, or you can
use snapshots to load data from existing volumes.

###### Note

When you use snapshots to configure volumes, you can specify a
`volumeInitializationRate`, in MiB/s, at which data is fetched from the
snapshot to create volumes that are fully initialized in a predictable amount of time.
For more information about volume initialization, see [Initialize Amazon EBS volumes](../../../ebs/latest/userguide/initalize-volume.md "../../../ebs/latest/userguide/initalize-volume.md") in
the _Amazon EBS User Guide_. For more information about configuring Amazon EBS
volumes, see [Defer volume configuration to launch time in an
Amazon ECS task definition](specify-ebs-config.md "specify-ebs-config.md") and
[Specify Amazon EBS volume configuration at Amazon ECS
deployment](configure-ebs-volume.md "configure-ebs-volume.md").

Volume configuration is deferred to launch time using the `configuredAtLaunch`
parameter in the task definition. By providing volume configuration at launch time rather
than in the task definition, you get to create task definitions that aren't constrained to a
specific data volume type or specific EBS volume settings. You can then reuse your task
definitions across different runtime environments. For example, you can provide more
throughput during deployment for your production workloads than your pre-prod
environments.

Amazon EBS volumes attached to tasks can be encrypted with AWS Key Management Service (AWS KMS) keys to protect
your data. For more information see, [Encrypt data stored in Amazon EBS volumes attached to
Amazon ECS tasks](ebs-kms-encryption.md "ebs-kms-encryption.md").

To monitor your volume's performance, you can also use Amazon CloudWatch metrics. For more
information about Amazon ECS metrics for Amazon EBS volumes, see [Amazon ECS CloudWatch metrics](available-metrics.md "available-metrics.md") and [Amazon ECS
Container Insights metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md").

Attaching an Amazon EBS volume to a task is supported in all commercial and China [AWS Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region") that support Amazon ECS.

## Supported operating systems and capacity

The following table provides the supported operating system and capacity
configurations.

| Capacity                     | Linux                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Windows                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fargate                      | Amazon EBS volumes are supported on platform version `1.4.0`<br>or later (Linux). For more information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").                                                                                                                                                                                                                                                                                                                                                                                | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| EC2                          | Amazon EBS volumes are supported for tasks hosted on Nitro-based instances with<br>Amazon ECS-optimized Amazon Machine Images (AMIs). For more information about<br>instance types, see [Instance<br>types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the _Amazon EC2 User Guide_.<br>Amazon EBS volumes are supported on ECS-optimized AMI<br>`20231219` or later. For more information, see [Retrieving Amazon ECS-Optimized AMI<br>metadata](retrieve-ecs-optimized_AMI.md "retrieve-ecs-optimized_AMI.md"). | Tasks hosted on Nitro-based instances with<br>Amazon ECS-optimized Amazon Machine Images (AMIs). For more information about<br>instance types, see [Instance<br>types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the _Amazon EC2 User Guide_.<br>Amazon EBS volumes are supported on ECS-optimized AMI<br>`20241017` or later. For more information, see [Retrieving Amazon ECS-Optimized Windows AMI<br>metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md"). |
| Amazon ECS Managed Instances | Amazon EBS volumes are supported for tasks hosted on Amazon ECS Managed Instances on Linux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Not supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Considerations

Consider the following when using Amazon EBS volumes:

- You can't configure Amazon EBS volumes for attachment to Fargate
  Amazon ECS tasks in the `use1-az3` Availability Zone.
- The magnetic (`standard`) Amazon EBS volume type is not supported for
  tasks hosted on Fargate. For more information about Amazon EBS volume
  types, see [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md") in
  the _Amazon EC2 User Guide_.
- An Amazon ECS infrastructure IAM role is required when creating a service or a
  standalone task that is configuring a volume at deployment. You can attach the
  AWS managed `AmazonECSInfrastructureRolePolicyForVolumes` IAM
  policy to the role, or you can use the managed policy as a guide to create and
  attach your own policy with permissions that meet your specific needs. For more
  information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
- You can attach at most one Amazon EBS volume to each Amazon ECS task, and it must be a
  new volume. You can't attach an existing Amazon EBS volume to a task. However, you
  can configure a new Amazon EBS volume at deployment using the snapshot of an existing
  volume.
- To use Amazon EBS volumes with Amazon ECS services, the deployment controller must be
  `ECS`. Both rolling and blue/green deployment strategies are supported when
  using this deployment controller.
- For a container in your task to write to the mounted Amazon EBS volume, the container must have appropriate file system permissions. When you specify a non-root user in your container definition, Amazon ECS automatically configures the volume with group-based permissions that allow the specified user to read and write to the volume. If no user is specified, the container runs as root and has full access to the volume.
- Amazon ECS automatically adds the reserved tags `AmazonECSCreated` and
  `AmazonECSManaged` to the attached volume. If you remove these
  tags from the volume, Amazon ECS won't be able to manage the volume on your behalf.
  For more information about tagging Amazon EBS volumes, see [Tagging Amazon EBS volumes](specify-ebs-config.md#ebs-volume-tagging "specify-ebs-config.md#ebs-volume-tagging"). For more information about tagging Amazon ECS
  resources, see [Tagging your Amazon ECS
  resources](ecs-using-tags.md "ecs-using-tags.md").
- Provisioning volumes from a snapshot of an Amazon EBS volume that contains
  partitions isn't supported.
- Volumes that are attached to tasks that are managed by a service aren't
  preserved and are always deleted upon task termination.
- You can't configure Amazon EBS volumes for attachment to Amazon ECS tasks that are
  running on AWS Outposts.
