# Replicating EFS file systems

For expanded resilience and data protection, you can replicate your EFS file
system in an AWS Region. When you enable replication on an EFS file system, Amazon EFS
automatically and transparently replicates the data and metadata on the source file system to a
destination file system. In the event of a disaster or when performing game day exercises, you can
fail over to your replica file system. To resume operations, you can then fail back to the primary
file system.

To manage the process of creating the destination file system and keeping it synced with the
source file system, Amazon EFS uses a _replication configuration_.

After you create the replication configuration, Amazon EFS automatically keeps the source and
destination file systems synchronized. Changes made to the source file system are not transferred
to the destination file system in a point-in-time consistent manner. Instead they're transferred
based on the **Last synced time** for the replication. The **Last sync
time** indicates when the last successful sync between the source and destination was
completed. Changes made to your source file system as of the last synced time are replicated to
the destination file system, while changes made to the source file system after the last synced
time may not be replicated. For more information, see [Viewing replication details](monitoring-replication-status.md "monitoring-replication-status.md").

Replication is available in all AWS Regions in which Amazon EFS is available. To replicate an
EFS file system in a Region that is disabled by default, you must first
opt in to the Region. For more information, see [Specify which
AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable "../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable") in the _AWS General Reference
Guide_. If you opt out of a Region later, Amazon EFS pauses all replication
activities for the Region. To resume replication activities for the
Region, opt in to the AWS Region again.

###### Note

Replication does not support using tags for attribute-based access control (ABAC).

###### Topics

- [Costs](#efs-replication-costs "#efs-replication-costs")
- [Replication performance](#efs-replication-performance "#efs-replication-performance")
- [Required IAM permissions](#efs-replication-permissions "#efs-replication-permissions")
- [Configuring replication to new EFS file
  system](create-replication.md "create-replication.md")
- [Configuring replication to an existing
  EFS file system](replicate-existing-destination.md "replicate-existing-destination.md")
- [Replicating EFS file systems across AWS
  accounts](cross-account-replication.md "cross-account-replication.md")
- [Viewing replication details](monitoring-replication-status.md "monitoring-replication-status.md")
- [Deleting replication configurations](delete-replications.md "delete-replications.md")
- [Using the replica](replication-fail-over.md "replication-fail-over.md")

## Costs

To facilitate replication, Amazon EFS creates hidden directories and metadata on the destination
file system. These equate to approximately 12 mebibytes (MiB) of metered data for which you are
billed. For more information about metering file system storage, see [How Amazon EFS reports file system and object
sizes](metered-sizes.md "metered-sizes.md").

## Replication performance

When you create new replications or reverse the direction of existing replications during
the failback process, Amazon EFS performs an initial sync, which includes a series of one-time setup
actions to support the replication. Replicated data is accessible in the destination file system
only after the initial sync completes. The amount of time that the initial sync takes to finish
depends on factors such as the size of the source file system and the number of files in it.

After the initial replication is finished, Amazon EFS maintains a Recovery Point Objective (RPO)
of 15 minutes for most file systems. However, if the source file system has files that change
very frequently and has either more than 100 million files or files that are larger than 100 GB,
replication may take longer than 15 minutes. For information about monitoring when the last
replication successfully finished, see [Viewing replication details](monitoring-replication-status.md "monitoring-replication-status.md").

You can monitor when the last successful sync occurred using the console, the AWS Command Line Interface
(AWS CLI), the API, and Amazon CloudWatch. In CloudWatch, use the [TimeSinceLastSync](efs-metrics.md "efs-metrics.md") EFS metric. For more information, see [Viewing replication details](monitoring-replication-status.md "monitoring-replication-status.md").

## Required IAM permissions

Amazon EFS uses either the EFS service-linked role named
`AWSServiceRoleForAmazonElasticFileSystem` or the IAM role that you specify to
synchronize replication between the source and destination file systems. To provide an IAM
role, the IAM user or role creating the replication configuration must have
`iam:PassRole` permission. For more information, see [Grant a user permissions to pass a role to
an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the _AWS Identity and Access Management User Guide_.

- For more information about the `iam:CreateServiceLinkedRole`, see the example
  in [Using service-linked roles for Amazon EFS](using-service-linked-roles.md "using-service-linked-roles.md").
- For more information about a custom IAM role – see [Create an IAM role with a custom trust
  policy](cross-account-replication.md#replication-create-iam-role "cross-account-replication.md#replication-create-iam-role").

###### Note

If you are performing cross-account replication, then you must provide an IAM role when
you create the replication configuration. Using the service-linked role is not permitted. For
more information, see [Replicating EFS file systems across AWS
accounts](cross-account-replication.md "cross-account-replication.md").

The service-linked role or IAM role that you provide when creating the replication
configuration must have the following permissions for replication.

- `elasticfilesystem:DescribeFileSystems`
- `elasticfilesystem:CreateFileSystem`
- `elasticfilesystem:CreateReplicationConfiguration`
- `elasticfilesystem:DeleteReplicationConfiguration`
- `elasticfilesystem:DescribeReplicationConfigurations`

You can use the `AmazonElasticFileSystemFullAccess` managed policy to
automatically get all required EFS permissions. For more information, see [AWS managed policy: AmazonElasticFileSystemFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess").
