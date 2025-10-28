# Shared storage

AWS ParallelCluster supports either using [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md"),
[FSx for ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md"), and [FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md")
shared storage volumes, [Amazon EFS](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") and [FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md")
shared storage file systems, or [File Caches](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md"). We recommend that you follow the
[AWS well-architected framework reliability pillar](../../../wellarchitected/latest/reliability-pillar/back-up-data.md "../../../wellarchitected/latest/reliability-pillar/back-up-data.md")
guidance and back up your volumes and file systems.

Select a storage system that meets your HPC application I/O requirements. You can optimize each file system based on your specific use case. For more information,
see [storage options overview](../../../whitepapers/latest/aws-overview/storage-services.md "../../../whitepapers/latest/aws-overview/storage-services.md").

**Amazon EBS volumes** are attached to the head node and shared with compute nodes through NFS. This option can be cost effective, but performance
depends on the head node resources as storage needs scale. This can become a bottleneck as more compute nodes are added to the cluster and the
throughput demand increases.

**Amazon EFS files systems** scale as storage needs change. You can configure these file systems for a variety of use cases. Use Amazon EFS file systems
to run parallelized and latency sensitive applications on your cluster.

**FSx for Lustre file systems** can process massive data sets at up to hundreds of gigabytes per second throughput, millions of IOPS,
and sub-millisecond latencies. Use FSx for Lustre file systems for demanding high performance compute environments.

In the [SharedStorage section](SharedStorage-v3.md "SharedStorage-v3.md"), you can define either external or AWS ParallelCluster managed storage:

- **External storage** refers to an existing volume or file system that you manage. AWS ParallelCluster doesn't
  create or delete this storage.
- **Managed storage** refers to a volume or file system that AWS ParallelCluster created and can delete.
  External storage

You can configure AWS ParallelCluster to attach external storage to the cluster when the cluster is created or updated. Similarly you can configure it
to detach external storage from the cluster when the cluster is deleted or updated. Your data is preserved and you can use it for long-term permanent
shared storage outside of the cluster lifecycle.

###### Note

Versions of AWS ParallelCluster prior to 3.8 do not allow for externally managed filesystems to be mounted at `/home`. Starting from version 3.8,
AWS ParallelCluster allows you to use `/home` as a mount point for an external managed filesystem. You can mount an externally managed file system to
`/home` by specifying `/home` as the value to the [MountDir](SharedStorage-v3.md#yaml-SharedStorage-MountDir "SharedStorage-v3.md#yaml-SharedStorage-MountDir") parameter under the [SharedStorage section](SharedStorage-v3.md "SharedStorage-v3.md").

Amazon File Cache is not suitable for use as the system `/home` directory and therefore is not supported at this time for mounting `/home`.

When specifying a `/home` directory under the [SharedStorage section](SharedStorage-v3.md "SharedStorage-v3.md") the [SharedStorageType](HeadNode-v3.md#yaml-HeadNode-SharedStorageType "HeadNode-v3.md#yaml-HeadNode-SharedStorageType")
configuration option will be overridden, meaning the settings under [SharedStorage section](SharedStorage-v3.md "SharedStorage-v3.md") will be used instead.

When mounting an external filesystem to the `/home` directory AWS ParallelCluster copies the head node's `/home` contents to the external filesystem, without overwriting existing files on the external storage.
This includes transferring the cluster's SSH key for the default user, if it is absent on the external filesystem. For more information refer to [AWS ParallelCluster shared storage considerations](shared-storage-working-considerations-v3.md "shared-storage-working-considerations-v3.md").

AWS ParallelCluster managed storage

AWS ParallelCluster managed storage is dependent on the lifecycle of the cluster by default in the configuration. The `SharedStorage`
`DeletionPolicy` configuration parameter is set to `Delete` by default.

By default, an AWS ParallelCluster managed file system or volume and its data are deleted if one of the following is true.

- You delete the cluster.
- You change the managed shared storage configuration `Name`.
- You remove the managed shared storage from the configuration.
  Set `DeletionPolicy` to `Retain` to persist your managed shared file system or volume and data.
  We recommend that you backup your data regularly to avoid the loss of data. You can use [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") to centrally manage backups for all of your storage options.

You can remove the life cycle dependency with configuration settings. For more information, see [Convert AWS ParallelCluster managed storage to external storage](shared-storage-conversion-v3.md "shared-storage-conversion-v3.md").

For information on shared storage quotas, see [Quotas for shared storage](shared-storage-quotas-v3.md "shared-storage-quotas-v3.md").

For more information about shared storage and switching to new AWS ParallelCluster versions, see [Best practices: moving a cluster to a new AWS ParallelCluster minor or patch version](best-practices-v3.md#best-practices-cluster-upgrades-v3 "best-practices-v3.md#best-practices-cluster-upgrades-v3").

You can configure AWS ParallelCluster to attach external storage to the cluster when the cluster is created or updated. Similarly, you can
configure it to detach external storage from the cluster when the cluster is deleted or updated. Your data is preserved and you can use it for long
term permanent shared storage solutions that are independent of the cluster lifecycle.

By default, managed storage is dependent on the lifecycle of the cluster. You can remove the dependency with configuration settings that are
described in [Convert AWS ParallelCluster managed storage to external storage](shared-storage-conversion-v3.md "shared-storage-conversion-v3.md").

With specific settings, you can optimize each of the supported storage solutions for your use cases.

For shared storage quotas, see [Quotas for shared storage](shared-storage-quotas-v3.md "shared-storage-quotas-v3.md").

For more information about shared storage and switching to new AWS ParallelCluster versions, see [Best practices: moving a cluster to a new AWS ParallelCluster minor or patch version](best-practices-v3.md#best-practices-cluster-upgrades-v3 "best-practices-v3.md#best-practices-cluster-upgrades-v3").

The following topics describe how to configure shared storage for each storage service that AWS ParallelCluster supports.

###### Topics

- [Amazon Elastic Block Store](shared-storage-config-ebs-v3.md "shared-storage-config-ebs-v3.md")
- [Amazon Elastic File System](shared-storage-config-efs-v3.md "shared-storage-config-efs-v3.md")
- [Amazon FSx for Lustre](shared-storage-config-fsxlustre-v3.md "shared-storage-config-fsxlustre-v3.md")
- [Configure FSx for ONTAP, FSx for OpenZFS, and File Cache shared storage](shared-storage-config-ontap-zfs-v3.md "shared-storage-config-ontap-zfs-v3.md")
- [Working with shared storage in AWS ParallelCluster](shared-storage-considerations-v3.md "shared-storage-considerations-v3.md")
- [Quotas for shared storage](shared-storage-quotas-v3.md "shared-storage-quotas-v3.md")
