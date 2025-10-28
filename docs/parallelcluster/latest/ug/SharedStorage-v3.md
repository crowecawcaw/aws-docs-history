# `SharedStorage` section

**(Optional)** The shared storage settings for the
cluster.

AWS ParallelCluster supports either using [Amazon EBS](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md"), [FSx for ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md"), and [FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md")
shared storage volumes, [Amazon EFS](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") and [FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md") shared storage file systems, or [File Caches](../../../fsx/latest/FileCacheGuide/what-is.md "../../../fsx/latest/FileCacheGuide/what-is.md").

In the `SharedStorage` section, you can define either external or managed
storage:

- **External storage** refers to an existing volume or file
  system that you manage. AWS ParallelCluster doesn't create or delete it.
- **AWS ParallelCluster managed storage** refers to a volume or
  file system that AWS ParallelCluster created and can delete.
  For [shared storage quotas](shared-storage-quotas-v3.md "shared-storage-quotas-v3.md") and more
  information about how to configure your shared storage, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md") in _Using
  AWS ParallelCluster_.

###### Note

If AWS Batch is used as a scheduler, FSx for Lustre is only available on the cluster head
node.

```
SharedStorage:
  - MountDir: `string`
    Name: `string`
    StorageType: Ebs
    EbsSettings:
      VolumeType: `string`
      Iops: `integer`
      Size: `integer`
      Encrypted: `boolean`
      KmsKeyId: `string`
      SnapshotId: `string`
      Throughput: `integer`
      VolumeId: `string`
      DeletionPolicy: `string`
      Raid:
        Type: `string`
        NumberOfVolumes: `integer`
  - MountDir: `string`
    Name: `string`
    StorageType: Efs
    EfsSettings:
      Encrypted: `boolean`
      KmsKeyId: `string`
      EncryptionInTransit: `boolean`
      IamAuthorization: `boolean`
      PerformanceMode: `string`
      ThroughputMode: `string`
      ProvisionedThroughput: `integer`
      FileSystemId: `string`
      DeletionPolicy: `string`
      AccessPointId: `string`
  - MountDir: `string`
    Name: `string`
    StorageType: FsxLustre
    FsxLustreSettings:
      StorageCapacity: `integer`
      DeploymentType: `string`
      ImportedFileChunkSize: `integer`
      DataCompressionType: `string`
      ExportPath: `string`
      ImportPath: `string`
      WeeklyMaintenanceStartTime: `string`
      AutomaticBackupRetentionDays: `integer`
      CopyTagsToBackups: `boolean`
      DailyAutomaticBackupStartTime: `string`
      PerUnitStorageThroughput: `integer`
      BackupId: `string`
      KmsKeyId: `string`
      FileSystemId: `string`
      AutoImportPolicy: `string`
      DriveCacheType: `string`
      StorageType: `string`
      DeletionPolicy: `string`
      DataRepositoryAssociations:
      - Name: `string`
        BatchImportMetaDataOnCreate: `boolean`
        DataRepositoryPath: `string`
        FileSystemPath: `string`
        ImportedFileChunkSize: `integer`
        AutoExportPolicy: `string`
        AutoImportPolicy: `string`
  - MountDir: `string`
    Name: `string`
    StorageType: FsxOntap
    FsxOntapSettings:
      VolumeId: `string`
  - MountDir: `string`
    Name: `string`
    StorageType: FsxOpenZfs
    FsxOpenZfsSettings:
      VolumeId: `string`
  - MountDir: `string`
    Name: `string`
    StorageType: FileCache
    FileCacheSettings:
      FileCacheId: `string`
```

## `SharedStorage` update

policies

- For managed/external EBS, managed EFS and managed FSx Lustre, the update policy is
  [Update policy: For this
  list values setting, the compute fleet must be stopped or QueueUpdateStrategy must be set to add a new value; the compute
  fleet must be stopped when removing an existing value.](using-pcluster-update-cluster-v3.md#update-policy-update-cluster-v3 "using-pcluster-update-cluster-v3.md#update-policy-update-cluster-v3")
- For external EFS, FSx Lustre, FSx ONTAP, FSx OpenZfs and File Cache, the update policy
  is, [Update policy: This
  setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `SharedStorage` properties

`MountDir` (**Required**, `String`)

The path where the shared storage is mounted.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Name` (**Required**, `String`)

The name of the shared storage. You use this name when you update the
settings.

###### Warning

If you specify AWS ParallelCluster managed shared storage, and you change the value
for `Name`, the existing managed shared storage and data is deleted and new
managed shared storage is created. Changing the value for `Name` with a
cluster update is equivalent to replacing the existing managed shared storage with a
new one. Make sure you back up your data before you change `Name` if you need
to retain the data from the existing shared storage.

[Update policy: For this
list values setting, the compute fleet must be stopped or QueueUpdateStrategy must be set to add a new value; the compute
fleet must be stopped when removing an existing value.](using-pcluster-update-cluster-v3.md#update-policy-update-cluster-v3 "using-pcluster-update-cluster-v3.md#update-policy-update-cluster-v3")

`StorageType` (**Required**, `String`)

The type of the shared storage. Supported values are `Ebs`,
`Efs`, `FsxLustre`, `FsxOntap`, and
`FsxOpenZfs`.

For more information, see [FsxLustreSettings](#SharedStorage-v3-FsxLustreSettings "#SharedStorage-v3-FsxLustreSettings"), [FsxOntapSettings](#SharedStorage-v3-FsxOntapSettings "#SharedStorage-v3-FsxOntapSettings"), and
[FsxOpenZfsSettings](#SharedStorage-v3-FsxOpenZfsSettings "#SharedStorage-v3-FsxOpenZfsSettings").

###### Note

If you use AWS Batch as a scheduler, FSx for Lustre is only available on the cluster
head node.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `EbsSettings`

**(Optional)** The settings for an Amazon EBS volume.

```
EbsSettings:
  VolumeType: `string`
  Iops: `integer`
  Size: `integer`
  Encrypted: `boolean`
  KmsKeyId: `string`
  SnapshotId: `string`
  VolumeId: `string`
  Throughput: `integer`
  DeletionPolicy: `string`
  Raid:
    Type: `string`
    NumberOfVolumes: `integer`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `EbsSettings`

properties

When the [DeletionPolicy](#yaml-SharedStorage-EbsSettings-DeletionPolicy "#yaml-SharedStorage-EbsSettings-DeletionPolicy") is set to `Delete`, a managed volume, with its data, is
deleted if the cluster is deleted or if the volume is removed with a cluster update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md") in _Using
AWS ParallelCluster_.

`VolumeType`
(**Optional**, `String`)

Specifies the [Amazon EBS volume type](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md").
Supported values are `gp2`, `gp3`, `io1`,
`io2`, `sc1`, `st1`, and `standard`. The
default value is `gp3`.

For more information, see [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md") in the
_Amazon EC2 User Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Iops` (**Optional**, `Integer`)

Defines the number of IOPS for `io1`, `io2`, and
`gp3` type volumes.

The default value, supported values, and `volume_iops` to
`volume_size` ratio varies by `VolumeType` and
`Size`.

`VolumeType` = `io1`

Default `Iops` = 100

Supported values `Iops` = 100–64000 †

Maximum `volume_iops` to `volume_size` ratio = 50 IOPS
for each GiB. 5000 IOPS requires a `volume_size` of at least 100
GiB.

`VolumeType` = `io2`

Default `Iops` = 100

Supported values `Iops` = 100–64000 (256000 for
`io2` Block Express volumes) †

Maximum `Iops` to `Size` ratio = 500 IOPS for each
GiB. 5000 IOPS requires a `Size` of at least 10 GiB.

`VolumeType` = `gp3`

Default `Iops` = 3000

Supported values `Iops` = 3000–16000

Maximum `Iops` to `Size` ratio = 500 IOPS for each
GiB. 5000 IOPS requires a `Size` of at least 10 GiB.

† Maximum IOPS is guaranteed only on [Instances
built on the Nitro System](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") provisioned with more than 32,000 IOPS. Other
instances guarantee up to 32,000 IOPS. Unless you [modify the volume](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md"),
earlier `io1` volumes might not reach full performance. `io2`
Block Express volumes support `volume_iops` values up to 256000 on
`R5b` instance types. For more information, see [`io2` Block Express volumes](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express") in the
_Amazon EC2 User Guide_.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Size` (**Optional**, `Integer`)

Specifies the volume size in gibibytes (GiB). The default value is 35.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Encrypted`
(**Optional**, `Boolean`)

Specifies if the volume is encrypted. The default value is
`true`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`KmsKeyId`
(**Optional**, `String`)

Specifies a custom AWS KMS key to use for encryption. This setting requires that the
`Encrypted` setting is set to `true`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`SnapshotId`
(**Optional**, `String`)

Specifies the Amazon EBS snapshot ID if you use a snapshot as the source for the
volume.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`VolumeId`
(**Optional**, `String`)

Specifies the Amazon EBS volume ID. When this is specified for an
`EbsSettings` instance, only the `MountDir` parameter can also
be specified.

The volume must be created in the same Availability Zone as the
`HeadNode`.

###### Note

Multiple Availability Zones is added in AWS ParallelCluster version 3.4.0.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Throughput`
(**Optional**, `Integer`)

The throughput, in MiB/s to provision for a volume, with a maximum of 1,000
MiB/s.

This setting is valid only when `VolumeType` is `gp3`. The
supported range is 125 to 1000, with a default value of 125.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`DeletionPolicy` (**Optional**,
`String`)

Specifies whether the volume should be retained, deleted, or snapshotted when the
cluster is deleted or the volume is removed. The supported values are
`Delete`, `Retain`, and `Snapshot`. The default
value is `Delete`.

When the [DeletionPolicy](#yaml-SharedStorage-EbsSettings-DeletionPolicy "#yaml-SharedStorage-EbsSettings-DeletionPolicy") set to `Delete`, a managed volume, with its data,
is deleted if the cluster is deleted or if the volume is removed with a cluster
update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md").

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`DeletionPolicy` is supported starting with AWS ParallelCluster version
3.2.0.

### `Raid`

**(Optional)** Defines the configuration of a RAID
volume.

```
Raid:
  Type: `string`
  NumberOfVolumes: `integer`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

#### `Raid`

properties

`Type`
(**Required**, `String`)

Defines the type of RAID array. Supported values are "0" (striped) and "1"
(mirrored).

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`NumberOfVolumes` (**Optional**,
`Integer`)

Defines the number of Amazon EBS volumes to use to create the RAID array. The
supported range of values is 2-5. The default value (when the `Raid`
setting is defined) is 2.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `EfsSettings`

**(Optional)** The settings for an Amazon EFS file system.

```
EfsSettings:
  Encrypted: `boolean`
  KmsKeyId: `string`
  EncryptionInTransit: `boolean`
  IamAuthorization: `boolean`
  PerformanceMode: `string`
  ThroughputMode: `string`
  ProvisionedThroughput: `integer`
  FileSystemId: `string`
  DeletionPolicy: `string`
  AccessPointId: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `EfsSettings`

properties

When the [DeletionPolicy](#yaml-SharedStorage-EfsSettings-DeletionPolicy "#yaml-SharedStorage-EfsSettings-DeletionPolicy") set to `Delete`, a managed file system, with its data,
is deleted if the cluster is deleted, or if the file system is removed with a cluster
update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md") in _Using
AWS ParallelCluster_.

`Encrypted`
(**Optional**, `Boolean`)

Specifies if the Amazon EFS file system is encrypted. The default value is
`false`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`KmsKeyId`
(**Optional**, `String`)

Specifies a custom AWS KMS key to use for encryption. This setting requires that the
`Encrypted` setting is set to `true`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`EncryptionInTransit` (**Optional**,
`Boolean`)

If set to `true`, Amazon EFS file systems are mounted using Transport Layer
Security (TLS). By default, this is set to `false`.

###### Note

If AWS Batch is used as scheduler, `EncryptionInTransit` isn't
supported.

###### Note

`EncryptionInTransit` is added starting with AWS ParallelCluster
version 3.4.0.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`IamAuthorization` (**Optional**,
`Boolean`)

`IamAuthorization` is added starting with AWS ParallelCluster version
3.4.0.

If set to `true`, Amazon EFS is authenticated by using the system's IAM
identity. By default, this is set to `false`.

###### Note

If `IamAuthorization` is set to `true`,
`EncryptionInTransit` must also be set to `true`.

###### Note

If AWS Batch is used as scheduler, `IamAuthorization` isn't
supported.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`PerformanceMode` (**Optional**,
`String`)

Specifies the performance mode of the Amazon EFS file system. Supported values are
`generalPurpose` and `maxIO`. The default value is
`generalPurpose`. For more information, see [Performance modes](../../../efs/latest/ug/performance.md#performancemodes "../../../efs/latest/ug/performance.md#performancemodes") in
the _Amazon Elastic File System User Guide_.

We recommend the `generalPurpose` performance mode for most file
systems.

File systems that use the `maxIO` performance mode can scale to higher
levels of aggregate throughput and operations per second. However, there's a trade-off
of slightly higher latencies for most file operations.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`ThroughputMode` (**Optional**,
`String`)

Specifies the throughput mode of the Amazon EFS file system. Supported values are
`bursting` and `provisioned`. The default value is
`bursting`. When `provisioned` is used,
`ProvisionedThroughput` must be specified.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`ProvisionedThroughput` (**Required** when
`ThroughputMode` is `provisioned`, `Integer`)

Defines the provisioned throughput (in MiB/s) of the Amazon EFS file system, measured
in MiB/s. This corresponds to the [ProvisionedThroughputInMibps](../../../efs/latest/ug/API_CreateFileSystem.md#efs-CreateFileSystem-response-ProvisionedThroughputInMibps "../../../efs/latest/ug/API_CreateFileSystem.md#efs-CreateFileSystem-response-ProvisionedThroughputInMibps") parameter in the _Amazon EFS API
Reference_.

If you use this parameter, you must set `ThroughputMode` to
`provisioned`.

The supported range is `1`-`1024`. To request a limit
increase, contact Support.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`FileSystemId`
(**Optional**, `String`)

Defines the Amazon EFS file system ID for an existing file system.

If the cluster is configured to span multiple Availability Zones, you must define
a file system mount target in each Availability Zone that's used by the
cluster.

When this is specified, only `MountDir` can be specified. No other
`EfsSettings` can be specified.

###### If you set this option, the following must be true for the file systems that

you define:

- The file systems have an existing mount target in each of the cluster's
  Availability Zones, with inbound and outbound NFS traffic allowed from the
  `HeadNode` and `ComputeNodes`. Multiple availability zones
  are configured in [Scheduling](Scheduling-v3.md "Scheduling-v3.md") / [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SubnetIds](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SubnetIds "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SubnetIds").

###### To make sure traffic is allowed between the cluster and file system, you

can do one of the following:

    + Configure the security groups of the mount target to allow the traffic to
     and from the CIDR or prefix list of cluster subnets.


    ###### Note

    AWS ParallelCluster validates that ports are open and that the CIDR or
     prefix list is configured. AWS ParallelCluster doesn't validate the content of
     CIDR block or prefix list.
    + Set custom security groups for cluster nodes by using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SecurityGroups](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups") and [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [SecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups"). The custom security groups must be
     configured to allow traffic between the cluster and the file system.


    ###### Note

    If all cluster nodes use custom security groups, AWS ParallelCluster only
     validates that the ports are open. AWS ParallelCluster doesn't validate that
     the source and destination are properly configured.

###### Warning

EFS OneZone is only supported if all compute nodes and the head node are in the
same Availability Zone. EFS OneZone can have only one mount target.

###### Note

Multiple Availability Zones is added in AWS ParallelCluster version 3.4.0.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DeletionPolicy` (**Optional**,
`String`)

Specifies whether the file system should be retained or deleted when the file
system is removed from the cluster or the cluster is deleted. The supported values are
`Delete` and `Retain`. The default value is
`Delete`.

When the [DeletionPolicy](#yaml-SharedStorage-EfsSettings-DeletionPolicy "#yaml-SharedStorage-EfsSettings-DeletionPolicy") is set to `Delete`, a managed file system, with
its data, is deleted if the cluster is deleted, or if the file system is removed with
a cluster update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md").

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`DeletionPolicy` is supported starting with AWS ParallelCluster version
3.3.0.

`AccessPointId` (**Optional**,
`String`)

If this option is specified, the filesystem entry point defined by the `access point ID` will be mounted rather than the filesystem root.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md").

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `FsxLustreSettings`

###### Note

You must define `FsxLustreSettings` if `FsxLustre` is specified
for [StorageType](#yaml-SharedStorage-StorageType "#yaml-SharedStorage-StorageType").

**(Optional)** The settings for an FSx for Lustre file
system.

```
FsxLustreSettings:
  StorageCapacity: `integer`
  DeploymentType: `string`
  ImportedFileChunkSize: `integer`
  DataCompressionType: `string`
  ExportPath: `string`
  ImportPath: `string`
  WeeklyMaintenanceStartTime: `string`
  AutomaticBackupRetentionDays: `integer`
  CopyTagsToBackups: `boolean`
  DailyAutomaticBackupStartTime: `string`
  PerUnitStorageThroughput: `integer`
  BackupId: `string` # BackupId cannot coexist with some of the fields
  KmsKeyId: `string`
  FileSystemId: `string` # FileSystemId cannot coexist with other fields
  AutoImportPolicy: `string`
  DriveCacheType: `string`
  StorageType: `string`
  DeletionPolicy: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

If AWS Batch is used as a scheduler, FSx for Lustre is only available on the cluster head
node.

### `FsxLustreSettings` properties

When the [DeletionPolicy](#yaml-SharedStorage-FsxLustreSettings-DeletionPolicy "#yaml-SharedStorage-FsxLustreSettings-DeletionPolicy") is set to `Delete`, a managed file system, with its
data, is deleted if the cluster is deleted, or if the file system is removed with a cluster
update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md").

`StorageCapacity` (**Required**,
`Integer`)

Sets the storage capacity of the FSx for Lustre file system, in GiB.
`StorageCapacity` is required if you're creating a new file system. Do
not include `StorageCapacity` if `BackupId` or
`FileSystemId` is specified.

- For `SCRATCH_2`, `PERSISTENT_1`, and
  `PERSISTENT_2` deployment types, valid values are 1200 GiB, 2400 GiB,
  and increments of 2400 GiB.
- For `SCRATCH_1` deployment type, valid values are 1200 GiB, 2400
  GiB, and increments of 3600 GiB.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DeploymentType` (**Optional**,
`String`)

Specifies the deployment type of the FSx for Lustre file system. Supported values are
`SCRATCH_1`, `SCRATCH_2`, `PERSISTENT_1`, and
`PERSISTENT_2`. The default value is `SCRATCH_2`.

Choose `SCRATCH_1` and `SCRATCH_2` deployment types when you
need temporary storage and shorter term processing of data. The `SCRATCH_2`
deployment type provides in transit encryption of data and higher burst throughput
capacity than `SCRATCH_1`.

Choose `PERSISTENT_1` deployment type for longer term storage and for
throughput focused workloads that aren't latency sensitive. `PERSISTENT_1`
supports encryption of data in transit. It's available in all AWS Regions where
FSx for Lustre is available.

Choose `PERSISTENT_2` deployment type for longer term storage and for
latency sensitive workloads that require the highest levels of IOPS and throughput.
`PERSISTENT_2` supports SSD storage and offers higher
`PerUnitStorageThroughput` (up to 1000 MB/s/TiB).
`PERSISTENT_2` is available in a limited number of AWS Regions. For
more information about deployment types and the list of AWS Regions where
`PERSISTENT_2` is available, see [File
system deployment options for FSx for Lustre](../../../fsx/latest/LustreGuide/using-fsx-lustre.md#lustre-deployment-types "../../../fsx/latest/LustreGuide/using-fsx-lustre.md#lustre-deployment-types") in the
_Amazon FSx for Lustre User Guide_.

Encryption of data in transit is automatically enabled when you access
`SCRATCH_2`, `PERSISTENT_1`, or `PERSISTENT_2`
deployment type file systems from Amazon EC2 instances that support [this
feature](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md").

Encryption of data in transit for `SCRATCH_2`,
`PERSISTENT_1`, and `PERSISTENT_2` deployment types is
supported when accessed from supported instance types in supported AWS Regions. For
more information, see [Encrypting data in
transit](../../../fsx/latest/LustreGuide/encryption-in-transit-fsxl.md "../../../fsx/latest/LustreGuide/encryption-in-transit-fsxl.md") in the _Amazon FSx for Lustre User Guide_.

###### Note

Support for the `PERSISTENT_2` deployment type was added with
AWS ParallelCluster version 3.2.0.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`ImportedFileChunkSize` (**Optional**,
`Integer`)

For files that are imported from a data repository, this value determines the
stripe count and maximum amount of data for each file (in MiB) that's stored on a
single physical disk. The maximum number of disks that a single file can be striped
across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
GiB). Amazon S3 objects have a maximum size of 5 TB.

###### Note

This parameter isn't supported for file systems that use the
`PERSISTENT_2` deployment type. For instructions on how to configure
data repositories associations, see [Linking your file
system to an S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") in the _Amazon FSx for Lustre User
Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DataCompressionType` (**Optional**,
`String`)

Sets the data compression configuration for the FSx for Lustre file system. The
supported value is `LZ4`. `LZ4` indicates that data compression
is turned on with the LZ4 algorithm. When `DataCompressionType` isn't
specified, data compression is turned off when the file system is created.

For more information, see [Lustre data
compression](../../../fsx/latest/LustreGuide/data-compression.md "../../../fsx/latest/LustreGuide/data-compression.md").

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`ExportPath` (**Optional**,
`String`)

The path in Amazon S3 where the root of your FSx for Lustre file system is exported. This
setting is only supported when the `ImportPath` parameter is specified. The
path must use the same Amazon S3 bucket as specified in `ImportPath`. You can
provide an optional prefix to which new and changed data is to be exported from your
FSx for Lustre file system. If an `ExportPath` value is not provided,
FSx for Lustre sets a default export path,
`s3://`amzn-s3-demo-bucket`/FSxLustre[creation-timestamp]`. The timestamp is in
UTC format, for example
`s3://`amzn-s3-demo-bucket`/FSxLustre20181105T222312Z`.

The Amazon S3 export bucket must be the same as the import bucket specified by
`ImportPath`. If you only specify a bucket name, such as
`s3://`amzn-s3-demo-bucket``, you get a 1:1 mapping of file system objects to
 Amazon S3 bucket objects. This mapping means that the input data in Amazon S3 is overwritten on
 export. If you provide a custom prefix in the export path, such as
 `s3://`amzn-s3-demo-bucket`/[custom-optional-prefix]`, FSx for Lustre exports the
contents of your file system to that export prefix in the Amazon S3 bucket.

###### Note

This parameter isn't supported for file systems that use the
`PERSISTENT_2` deployment type. Configure data repositories
associations as described in [Linking your file
system to an S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") in the _Amazon FSx for Lustre User
Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`ImportPath` (**Optional**,
`String`)

The path to the Amazon S3 bucket (including the optional prefix) that you're using as
the data repository for your FSx for Lustre file system. The root of your FSx for Lustre
file system will be mapped to the root of the Amazon S3 bucket you select. An example is
`s3://`amzn-s3-demo-bucket`/optional-prefix`. If you specify a prefix after the
Amazon S3 bucket name, only object keys with that prefix are loaded into the file
system.

###### Note

This parameter isn't supported for file systems that use the
`PERSISTENT_2` deployment type. Configure data repositories
associations as described in [Linking your file
system to an S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") in the _Amazon FSx for Lustre User
Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`WeeklyMaintenanceStartTime` (**Optional**,
`String`)

The preferred start time to perform weekly maintenance. It's in the
`"d:HH:MM"` format in the UTC+0 time zone. For this format,
`d` is the weekday number from 1 through 7, beginning with Monday and
ending with Sunday. Quotation marks are required for this field.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`AutomaticBackupRetentionDays` (**Optional**, `Integer`)

The number of days to retain automatic backups. Setting this to 0 disables
automatic backups. The supported range is 0-90. The default is 0. This setting is only
valid for use with `PERSISTENT_1` and `PERSISTENT_2` deployment
types. For more information, see [Working with backups](../../../fsx/latest/LustreGuide/using-backups-fsx.md "../../../fsx/latest/LustreGuide/using-backups-fsx.md") in
the _Amazon FSx for Lustre User Guide_.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`CopyTagsToBackups` (**Optional**,
`Boolean`)

If `true`, copy the tags for the FSx for Lustre file system to backups.
This value defaults to `false`. If it's set to `true`, all tags
for the file system are copied to all automatic and user-initiated backups where the
user doesn't specify tags. If this value is `true`, and you specify one or
more tags, only the specified tags are copied to backups. If you specify one or more
tags when you create a user-initiated backup, no tags are copied from the file system,
regardless of this value. This setting is only valid for use with
`PERSISTENT_1` and `PERSISTENT_2` deployment types.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DailyAutomaticBackupStartTime` (**Optional**, `String`)

A recurring daily time, in the `HH:MM` format. `HH` is the
zero-padded hour of the day (00-23). `MM` is the zero-padded minute of the
hour (00-59). For example, `05:00` specifies 5 A.M. daily. This setting is
only valid for use with `PERSISTENT_1` and `PERSISTENT_2`
deployment types.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`PerUnitStorageThroughput` (**Required for
`PERSISTENT_1` and `PERSISTENT_2` deployment types**,
`Integer`)

Describes the amount of read and write throughput for each 1 tebibyte of storage,
in MB/s/TiB. File system throughput capacity is calculated by multiplying ﬁle system
storage capacity (TiB) by the `PerUnitStorageThroughput` (MB/s/TiB). For a
2.4 TiB ﬁle system, provisioning 50 MB/s/TiB of `PerUnitStorageThroughput`
yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that
you provision. This corresponds to the [PerUnitStorageThroughput](../../../AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.md#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput "../../../AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.md#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput") property.

Valid values:

- PERSISTENT_1 SSD storage: 50, 100, 200 MB/s/TiB.
- PERSISTENT_1 HDD storage: 12, 40 MB/s/TiB.
- PERSISTENT_2 SSD storage: 125, 250, 500, 1000 MB/s/TiB.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`BackupId`
(**Optional**, `String`)

Specifies the ID of the backup to use to restore the FSx for Lustre file system
from an existing backup. When the `BackupId` setting is specified, the
`AutoImportPolicy`, `DeploymentType`, `ExportPath`,
`KmsKeyId`, `ImportPath`, `ImportedFileChunkSize`,
`StorageCapacity`, and `PerUnitStorageThroughput` settings
must not be specified. These settings are read from the backup. Additionally, the
`AutoImportPolicy`, `ExportPath`, `ImportPath`, and
`ImportedFileChunkSize` settings must not be specified. This corresponds
to the [BackupId](../../../AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.md#cfn-fsx-filesystem-backupid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.md#cfn-fsx-filesystem-backupid") property.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`KmsKeyId`
(**Optional**, `String`)

The ID of the AWS Key Management Service (AWS KMS) key ID that's used to encrypt the FSx for Lustre file
system's data for persistent FSx for Lustre file systems at rest. If not specified, the
FSx for Lustre managed key is used. The `SCRATCH_1` and `SCRATCH_2`
FSx for Lustre file systems are always encrypted at rest using FSx for Lustre managed keys.
For more information, see [Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md") in the
_AWS Key Management Service API Reference_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`FileSystemId` (**Optional**,
`String`)

Specifies the ID of an existing FSx for Lustre file system.

If this option is specified, only the `MountDir` and
`FileSystemId` settings in the `FsxLustreSettings` are used.
All other settings in the `FsxLustreSettings` are ignored.

###### Note

If AWS Batch scheduler is used, FSx for Lustre is only available on the head
node.

###### Note

The file system must be associated to a security group that allows inbound and
outbound TCP traffic through ports 988, 1021, 1022, and 1023.

Make sure that traffic is allowed between the cluster and file system by doing one
of the following:

- Configure the security groups of the file system to allow the traffic to and
  from the CIDR or prefix list of cluster subnets.

###### Note

AWS ParallelCluster validates that ports are open and that the CIDR or prefix
list is configured. AWS ParallelCluster doesn't validate the content of CIDR block
or prefix list.

- Set custom security groups for cluster nodes by using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") /
  [SecurityGroups](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups") and [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [SecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups"). The custom security groups must be
  configured to allow traffic between the cluster and the file system.

###### Note

If all cluster nodes use custom security groups, AWS ParallelCluster only
validates that the ports are open. AWS ParallelCluster doesn't validate that the
source and destination are properly configured.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AutoImportPolicy` (**Optional**,
`String`)

When you create your FSx for Lustre file system, your existing Amazon S3 objects appear as
file and directory listings. Use this property to choose how FSx for Lustre keeps your
file and directory listings up to date as you add or modify objects in your linked
Amazon S3 bucket. `AutoImportPolicy` can have the following values:

- `NEW` - Automatic import is on. FSx for Lustre automatically imports
  directory listings of any new objects added to the linked Amazon S3 bucket that do not
  currently exist in the FSx for Lustre file system.
- `NEW_CHANGED` - Automatic import is on. FSx for Lustre automatically
  imports file and directory listings of any new objects added to the Amazon S3 bucket
  and any existing objects that are changed in the Amazon S3 bucket after you choose this
  option.
- `NEW_CHANGED_DELETED` - Automatic import is on. FSx for Lustre
  automatically imports file and directory listings of any new objects added to the
  Amazon S3 bucket, any existing objects that are changed in the Amazon S3 bucket, and any
  objects that were deleted in the Amazon S3 bucket after you choose this option.

###### Note

Support for `NEW_CHANGED_DELETED` was added in AWS ParallelCluster
version 3.1.1.

If `AutoImportPolicy` isn't specified, automatic import is off.
FSx for Lustre only updates file and directory listings from the linked Amazon S3 bucket when
the file system is created. FSx for Lustre doesn't update file and directory listings for
any new or changed objects after choosing this option.

For more information, see [Automatically import updates
from your S3 bucket](../../../fsx/latest/LustreGuide/autoimport-data-repo.md "../../../fsx/latest/LustreGuide/autoimport-data-repo.md") in the
_Amazon FSx for Lustre User Guide_.

###### Note

This parameter isn't supported for file systems using the
`PERSISTENT_2` deployment type. For instructions on how to configure
data repositories associations, see [Linking your file
system to an S3 bucket](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md") in the _Amazon FSx for Lustre User
Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DriveCacheType` (**Optional**,
`String`)

Specifies that the file system has an SSD drive cache. This can only be set if the
`StorageType` setting is set to `HDD`, and the
`DeploymentType` setting is set to `PERSISTENT_1`. This
corresponds to the [DriveCacheType](../../../AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.md#cfn-fsx-filesystem-lustreconfiguration-drivecachetype "../../../AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.md#cfn-fsx-filesystem-lustreconfiguration-drivecachetype") property. For more information, see [FSx for Lustre
deployment options](../../../fsx/latest/LustreGuide/using-fsx-lustre.md "../../../fsx/latest/LustreGuide/using-fsx-lustre.md") in the _Amazon FSx for Lustre User Guide_.

The only valid value is `READ`. To disable the SSD drive cache, don’t
specify the `DriveCacheType` setting.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`StorageType` (**Optional**,
`String`)

Sets the storage type for the FSx for Lustre file system that you're creating. Valid
values are `SSD` and `HDD`.

- Set to `SSD` to use solid state drive storage.
- Set to `HDD` to use hard disk drive storage. `HDD` is
  supported on `PERSISTENT` deployment types.

The default value is `SSD`. For more information, see [Storage
Type Options](../../../fsx/latest/WindowsGuide/optimize-fsx-costs.md#storage-type-options "../../../fsx/latest/WindowsGuide/optimize-fsx-costs.md#storage-type-options") in the _Amazon FSx for Windows User Guide_
and [Multiple Storage
Options](../../../fsx/latest/LustreGuide/what-is.md#storage-options "../../../fsx/latest/LustreGuide/what-is.md#storage-options") in the _Amazon FSx for Lustre User Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DeletionPolicy` (**Optional**,
`String`)

Specifies whether the file system should be retained or deleted when the file
system is removed from the cluster or the cluster is deleted. The supported values are
`Delete` and `Retain`. The default value is
`Delete`.

When the [DeletionPolicy](#yaml-SharedStorage-FsxLustreSettings-DeletionPolicy "#yaml-SharedStorage-FsxLustreSettings-DeletionPolicy") is set to `Delete`, a managed file system, with
its data, is deleted if the cluster is deleted, or if the file system is removed with
a cluster update.

For more information, see [Shared storage](shared-storage-quotas-integration-v3.md "shared-storage-quotas-integration-v3.md").

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`DeletionPolicy` is supported starting with AWS ParallelCluster version
3.3.0.

`DataRepositoryAssociations` (**Optional**,
`String`)

List of DRAs (up to 8 per file system)

Each data repository association must have a unique Amazon FSx file system
directory and a unique S3 bucket or prefix associated with it.

You can not use [ExportPath](#yaml-SharedStorage-FsxLustreSettings-ExportPath "#yaml-SharedStorage-FsxLustreSettings-ExportPath") and [ImportPath](#yaml-SharedStorage-FsxLustreSettings-ImportPath "#yaml-SharedStorage-FsxLustreSettings-ImportPath") in the
FsxLustreSettings at the same time as using DRAs.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Name` (**Required**,
`String`)

The name of the DRA. You use this name when you update the settings.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`BatchImportMetaDataOnCreate` (**Optional**,
`Boolean`)

A boolean flag indicating whether an import data repository task to import
metadata should run after the data repository association is created. The task runs if
this flag is set to `true`.

Default value: `false`

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DataRepositoryPath` (**Required**,
`String`)

The path to the Amazon S3 data repository that will be linked to the file system.
The path can be an S3 bucket or prefix in the format
`s3://`amzn-s3-demo-bucket`/myPrefix/`. This path specifies where in the S3 data
repository files will be imported from or exported to.

Cannot overlap with other DRAs

Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`

Minimum: `3`

Maximum: `4357`

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`FileSystemPath` (**Required**,
`String`)

A path on the Amazon FSx for Lustre file system that points to a high-level
directory (such as `/ns1/`) or subdirectory (such as
`/ns1/subdir/`) that will be mapped 1-1 with
`DataRepositoryPath`. The leading forward slash in the name is required.
Two data repository associations cannot have overlapping file system paths. For
example, if a data repository is associated with file system path `/ns1/`,
then you cannot link another data repository with file system path
`/ns1/ns2`.

This path specifies where in your file system files will be exported from or
imported to. This file system directory can be linked to only one Amazon S3 bucket,
and no other S3 bucket can be linked to the directory.

Cannot overlap with other DRAs

###### Note

If you specify only a forward slash (`/`) as the file system path,
you can link only one data repository to the file system. You can only specify
"`/`" as the file system path for the first data repository associated
with a file system.

Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`

Minimum: `1`

Maximum: `4096`

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`ImportedFileChunkSize` (**Optional**,
`Integer`)

For files imported from a data repository, this value determines the stripe count
and maximum amount of data per file (in MiB) stored on a single physical disk. The
maximum number of disks that a single file can be striped across is limited by the
total number of disks that make up the file system or cache.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
GiB). Amazon S3 objects have a maximum size of 5 TB.

Minimum: `1`

Maximum: `4096`

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`AutoExportPolicy` (**Optional**,
`Array of strings`)

The list can contain one or more of the following values:

- `NEW` - New files and directories are automatically exported to the
  data repository as they are added to the file system.
- `CHANGED` - Changes to files and directories on the file system are
  automatically exported to the data repository.
- `DELETED` - Files and directories are automatically deleted on the
  data repository when they are deleted on the file system.

You can define any combination of event types for your
`AutoExportPolicy`.

Maximum: `3`

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`AutoImportPolicy` (**Optional**,
`Array of strings`)

The list can contain one or more of the following values:

- `NEW` - Amazon FSx automatically imports metadata of files added to
  the linked S3 bucket that do not currently exist in the FSx file system.
- `CHANGED` - Amazon FSx automatically updates file metadata and
  invalidates existing file content on the file system as files change in the data
  repository.
- `DELETED` - Amazon FSx automatically deletes files on the file
  system as corresponding files are deleted in the data repository.

You can define any combination of event types for your
`AutoImportPolicy`.

Maximum: `3`

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `FsxOntapSettings`

###### Note

You must define `FsxOntapSettings` if `FsxOntap` is specified for
[StorageType](#yaml-SharedStorage-StorageType "#yaml-SharedStorage-StorageType").

**(Optional)** The settings for an FSx for ONTAP file
system.

```
FsxOntapSettings:
  VolumeId: `string`
```

### `FsxOntapSettings`

properties

`VolumeId`
(**Required**, `String`)

Specifies the volume ID of the existing FSx for ONTAP system.

###### Note

- If an AWS Batch scheduler is used, FSx for ONTAP is only available on the head
  node.
- If the FSx for ONTAP deployment type is `Multi-AZ`, make sure that the
  head node subnet's route table is properly configured.
- Support for FSx for ONTAP was added in AWS ParallelCluster version 3.2.0.
- The file system must be associated to a security group that allows inbound and
  outbound TCP and UDP traffic through ports 111, 635, 2049, and 4046.

Make sure traffic is allowed between the cluster and file system by doing one of the
following actions:

- Configure the security groups of the file system to allow the traffic to and from
  the CIDR or prefix list of cluster subnets.

###### Note

AWS ParallelCluster validates that ports are open and that the CIDR or prefix list
is configured. AWS ParallelCluster doesn't validate the content of CIDR block or prefix
list.

- Set custom security groups for cluster nodes by using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SecurityGroups](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups") and [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [SecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups").
  The custom security groups must be configured to allow traffic between the cluster and
  the file system.

###### Note

If all cluster nodes use custom security groups, AWS ParallelCluster only validates
that the ports are open. AWS ParallelCluster doesn't validate that the source and
destination are properly configured.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `FsxOpenZfsSettings`

###### Note

You must define `FsxOpenZfsSettings` if `FsxOpenZfs` is specified
for [StorageType](#yaml-SharedStorage-StorageType "#yaml-SharedStorage-StorageType").

**(Optional)** The settings for a FSx for OpenZFS file
system.

```
FsxOpenZfsSettings:
  VolumeId: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `FsxOpenZfsSettings` properties

`VolumeId`
(**Required**, `String`)

Specifies the volume ID of the existing FSx for OpenZFS system.

###### Note

- If an AWS Batch scheduler is used, FSx for OpenZFS is only available on the head
  node.
- Support for FSx for OpenZFS was added in AWS ParallelCluster version 3.2.0.
- The file system must be associated to a security group that allows inbound and
  outbound TCP and UDP traffic through ports 111, 2049, 20001, 20002, and 20003.

Make sure that traffic is allowed between the cluster and file system by doing one of
the following:

- Configure the security groups of the file system to allow the traffic to and from
  the CIDR or prefix list of cluster subnets.

###### Note

AWS ParallelCluster validates that ports are open and that the CIDR or prefix list
is configured. AWS ParallelCluster doesn't validate the content of CIDR block or prefix
list.

- Set custom security groups for cluster nodes by using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SecurityGroups](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups") and [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [SecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups").
  The custom security groups must be configured to allow traffic between the cluster and
  the file system.

###### Note

If all cluster nodes use custom security groups, AWS ParallelCluster only validates
that the ports are open. AWS ParallelCluster doesn't validate that the source and
destination are properly configured.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `FileCacheSettings`

###### Note

You must define `FileCacheSettings` if `FileCache` is specified
for [StorageType](#yaml-SharedStorage-StorageType "#yaml-SharedStorage-StorageType").

**(Optional)** The settings for a File Cache.

```
FileCacheSettings:
  FileCacheId: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `FileCacheSettings` properties

`FileCacheId` (**Required**,
`String`)

Specifies the File Cache ID of an existing File Cache.

###### Note

- File Cache doesn't support AWS Batch schedulers.
- Support for File Cache is added in AWS ParallelCluster version 3.7.0.
- The file system must be associated to a security group that allows inbound and
  outbound TCP traffic through port 988.

Make sure that traffic is allowed between the cluster and file system by doing one of
the following:

- Configure the security groups of the File Cache to allow the traffic to and from the
  CIDR or prefix list of cluster subnets.

###### Note

AWS ParallelCluster validates that ports are open and that the CIDR or prefix list
is configured. AWS ParallelCluster doesn't validate the content of CIDR block or prefix
list.

- Set custom security groups for cluster nodes by using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SecurityGroups](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups") and [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [SecurityGroups](HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups "HeadNode-v3.md#yaml-HeadNode-Networking-SecurityGroups").
  The custom security groups must be configured to allow traffic between the cluster and
  the file system.

###### Note

If all cluster nodes use custom security groups, AWS ParallelCluster only validates
that the ports are open. AWS ParallelCluster doesn't validate that the source and
destination are properly configured.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")
