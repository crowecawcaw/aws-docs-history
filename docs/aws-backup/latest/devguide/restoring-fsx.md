# Restore an FSx file system

The restore options that are available when you use AWS Backup to restore Amazon FSx file systems
are the same as using the native Amazon FSx backup. You can use a backup's recovery point to
create a new file system and restore a point-in-time snapshot of another file system.

AWS Backup supports restoring file systems that use Intelligent Tiering storage for both
FSx for Lustre and FSx for OpenZFS file systems. Intelligent Tiering file systems have specific
configuration requirements during restore operations.

When restoring Amazon FSx file systems, AWS Backup creates a new file system and populates it with
the data (Amazon FSx for NetApp ONTAP allows restoring a volume to an existing file system). This is
similar to how native Amazon FSx backs up and restores file systems. Restoring a backup to a new
file system takes the same amount of time as creating a new file system. The data restored
from the backup is lazy-loaded onto the file system. You might therefore experience slightly
higher latency during the process.

###### Note

You can't restore to an existing Amazon FSx file system, and you can't restore individual
files or folders.

FSx for ONTAP doesn’t support backing up certain volume types, including DP
(data-protection) volumes, LS (load-sharing) volumes, full volumes, or volumes on file
systems that are full. For more information, please see [FSx for ONTAP Working with
backups](../../../fsx/latest/ONTAPGuide/using-backups.md "../../../fsx/latest/ONTAPGuide/using-backups.md").

AWS Backup vaults that contain recovery points of Amazon FSx file systems are visible outside
of AWS Backup. You can restore the recovery points using Amazon FSx but you can't delete
them.

You can see backups created by the built-in Amazon FSx automatic backup functionality
from the AWS Backup console. You can also recover these backups using AWS Backup. However, you can't
delete these backups or change the automatic backup schedules of your Amazon FSx file systems
using AWS Backup.

## Use the AWS Backup console to restore Amazon FSx recovery

points

You can restore most Amazon FSx backups created by AWS Backup using the AWS Backup console, API, or
AWS CLI.

This section shows you how to use the AWS Backup console to restore Amazon FSx file
systems.

###### Topics

###### To restore an FSx for Windows File Server file system

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, and
   then choose the Amazon FSx resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points
   for the selected resource ID is shown. Choose the recovery point ID of the
   resource.
4. In the upper-right corner of the pane, choose **Restore** to
   open the **Restore backup** page.
5. In the **File system details** section, the ID of your backup
   is shown under **Backup ID**, and the file system type is shown
   under **File system type**. You can restore both FSx for Windows File Server and
   FSx for Lustre file systems.
6. For **Deployment type**, accept the default. You can't change
   the deployment type of a file system during restore.
7. Choose the **Storage type** to use. If the storage capacity
   of your file system is less than 2,000 GiB, you can't use the
   **HDD** storage type.
8. For **Throughput capacity**, choose **Recommended
   throughput capacity** to use the recommended 16 MB per second (MBps)
   rate, or choose **Specify throughput capacity** and enter a new
   rate.
9. In the **Network and security** section, provide the required
   information.
10. If you are restoring an FSx for Windows File Server file system, provide the**Windows authentication** information used to access the file system, or
    you can create a new one.

###### Note

When restoring a backup, you can't change the type of Active Directory on
the file system.

For more information about Microsoft Active Directory, see [Working with Active Directory in Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/aws-ad-integration-fsxW.md "../../../fsx/latest/WindowsGuide/aws-ad-integration-fsxW.md") in
the _Amazon FSx for Windows File Server User Guide_. 11. (Optional) In the **Backup and maintenance** section, provide
the information to set your backup preferences. 12. In the **Restore role** section, choose the IAM role that
AWS Backup will use to create and manage your backups on your behalf. We recommend that
you choose the **Default role**. If there is no default role, one
is created for you with the correct permissions. You can also provide your own
IAM role. 13. Verify all your entries, and choose **Restore
Backup**.

AWS Backup supports Amazon FSx for Lustre file systems that have persistent storage
deployment type and are not linked to a data repository like Amazon S3.

###### Note

You can only restore your backup to a file system of the same deployment type, storage
class, throughput capacity, storage capacity, data compression type, and AWS Region
as the original. You can increase your restored file system's storage capacity after
it becomes available.

###### To restore an Amazon FSx for Lustre file system

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, and
   then choose the Amazon FSx resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points
   for the selected resource ID is shown. Choose the recovery point ID of the
   resource.
4. In the upper-right corner of the pane, choose **Restore** to
   open the **Restore backup to new file system** page.
5. In the **Settings** section, the ID of your backup is shown
   under **Backup ID**, and the file system type is shown under
   **File system type**. **File system type**
   should be **Lustre**.
6. Choose a **Deployment type**. AWS Backup only supports the
   persistent deployment type. You can't change the deployment type of a file system
   during restore.

Persistent deployment type is for long-term storage. For detailed information
about FSx for Lustre deployment options, see [Using Available Deployment
Options for Amazon FSx for Lustre File Systems](../../../fsx/latest/LustreGuide/using-fsx-lustre.md "../../../fsx/latest/LustreGuide/using-fsx-lustre.md") in the
_Amazon FSx for Lustre User Guide_. 7. Choose the **Throughput per unit storage** that you want to
use.

###### Note

Throughput per unit storage cannot be configured for file systems using
Intelligent-Tiering storage class. 8. (Optional) For file systems using Intelligent-Tiering storage class, choose
the SSD read cache sizing mode and capacity. For more information, see the FSx
documentation for [managing provisioned SSD read cache](../../../fsx/latest/LustreGuide/managing-ssd-read-cache.md "../../../fsx/latest/LustreGuide/managing-ssd-read-cache.md"). 9. (Optional) For file systems using Intelligent-Tiering storage class, choose whether
to enable EFA (Elastic Fabric Adapter). To enable EFA, make sure that your security
group allows all inbound and outbound traffic within the security group. 10. Specify the **Storage capacity** to use. Enter a capacity
between 32 GiB and 64,436 GiB.

###### Note

For Intelligent Tiering file systems, storage capacity is elastic and cannot be
specified during restore. The capacity will automatically scale based on your data usage. 11. In the **Network and security** section, provide the required
information. 12. (Optional) In the **Backup and maintenance** section, provide
the information to set your backup preferences. 13. In the **Restore role** section, choose the IAM role that
AWS Backup will use to create and manage your backups on your behalf. We recommend that
you choose the **Default role**. If there is no default role, one
is created for you with the correct permissions. You can also provide your IAM
role. 14. Verify all your entries, and choose **Restore
Backup**.

###### To restore Amazon FSx for NetApp ONTAP volumes:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, and
   then choose the Amazon FSx resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. Choose the recovery point ID of the resource.
4. In the upper-right corner of the pane, choose **Restore** to
   open the **Restore** page.

The first section, **File system details**, displays the
recovery point ID, the file system ID, and the file system type. 5. Under **Restore options**, there are several selections. First,
choose the **File system** from the dropdown menu. 6. Next, choose the preferred **Storage virtual machine** from the
dropdown menu. 7. Enter a name for your volume. 8. Specify the **Junction Path**, which is location within your
file system where your volume will be mounted. 9. Specify the **Volume size** in megabytes (MB) that you are
creating. 10. (_Optional_) You can choose to **Enable storage
efficiency** by checking the box. This will allow deduplication,
compression, and compaction. 11. In the **Capacity pool tiering policy** dropdown menu, select
the tiering preference. 12. In the **Restore permissions**, choose the IAM role that AWS Backup
will use to restore backups. 13. Verify all your entries, and choose **Restore Backup**.

###### Note

Restoring from a backup with a given storage class to a file system with a
different storage class is not supported.

###### To restore an FSx for OpenZFS file system

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources**, and
   then choose the Amazon FSx resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. Choose the recovery point ID of the resource.
4. In the upper-right corner of the pane, choose **Restore** to
   open the **Restore backup** page.

In the **File system details** section, the ID of your backup
is shown under **Backup ID**, and the file system type is shown
under **File system type**. File system type should be
**FSx for OpenZFS**. 5. Under **Restore options**, you may select **Quick
restore** or **Standard restore**. Quick restore will
use the default settings of the source file system. If you are doing Quick Restore,
skip to Step 7.

If you choose Standard restore, specify the additional following
configurations:

    1. **Provisioned SSD IOPS**: You can choose the
     **Automatic radio button** or you can choose the
     **User-provisioned option** if available.


    ###### Note

    SSD IOPS cannot be set for file systems using Intelling-Tiering storage
     class
    2. **Throughput capacity**: You can choose the
     **Recommended throughput capacity** of 64 MB/sec (for SSD
     storage class), and 160 MB/sec (for Intelligent-Tiering storage class), or you
     can choose to **Specify throughput capacity**.
    3. (*Optional*) **VPC security groups**:
     You can specify VPC security groups to associate with your file system’s network
     interface.
    4. **Encryption key**: Specify the AWS Key Management Service key to protect
     the restored file system data at rest.
    5. (*Optional*) **Root Volume
     configuration**: This configuration is collapsed by default. You may
     expand it by clicking the down-pointing carat (arrow). Creating a file system
     from a backup will create a new file system; the volumes and snapshots will
     retain their source configurations.
    6. (*Optional*) **Backup and maintenance**:
     To set a scheduled backup, click the down-pointing carat (arrow) to expand the
     section. You may choose the backup window, hour and minute, retention period,
     and weekly maintenance window.

6. The **SSD Storage capacity** will display the file system’s
   storage capacity.

###### Note

For Intelligent Tiering file systems, storage capacity is elastic and cannot
be specified during restore. The capacity will automatically scale based on your
data usage. 7. (Optional) For file systems using Intelligent-Tiering storage class, choose
the SSD read cache sizing mode and capacity. For more information, see the FSx
documentation for [managing provisioned SSD read cache](../../../fsx/latest/OpenZFSGuide/managing-ssd-read-cache.md "../../../fsx/latest/OpenZFSGuide/managing-ssd-read-cache.md"). 8. Choose the **Virtual Private Cloud** (VPC) from which your file
system can be accessed. 9. In the **Subnet** dropdown menu, choose the subnet in which
your file system’s network interface resides. 10. In the **Restore role** section, choose the IAM role that AWS Backup
will use to create and manage your backups on your behalf. We recommend that you
choose the **Default role**. If there is no default role, one is
created for you with the correct permissions. You can also choose an IAM
role. 11. Verify all your entries, and choose **Restore Backup**.

## Use the AWS Backup API, CLI, or SDK to restore Amazon FSx recovery

points

To restore Amazon FSx using the API or CLI, use `StartRestoreJob`. You can specify the following metadata during an Amazon FSx
restore:

```
StorageCapacity
StorageType
VpcId
KmsKeyId
SecurityGroupIds
SubnetIds
DeploymentType
WeeklyMaintenanceStartTime
DailyAutomaticBackupStartTime
AutomaticBackupRetentionDays
CopyTagsToBackups
WindowsConfiguration
LustreConfiguration
OntapConfiguration
OpenZFSConfiguration
aws:backup:request-id
```

###### Note

Storage capacity cannot be specified for Intelligent Tiering file systems as they use
elastic storage that scales automatically based on data usage.

You can specify the following metadata during an FSx for Windows File Server restore:

- ThroughputCapacity
- PreferredSubnetId
- ActiveDirectoryId

You can specify the following subfields of `LustreConfiguration`
in the metadata during an FSx for Lustre restore:

- `PerUnitStorageThroughput` - Specifies the throughput
  capacity per unit of storage provisioned, measured in MB/s per TiB of storage.
- `DriveCacheType` - The type of drive cache used by
  `PERSISTENT_1` file systems that are provisioned with HDD storage
  devices. This parameter is required when `StorageType` is set to
  HDD.
- `DataReadCacheConfiguration` - Specifies the provisioned SSD read
  cache for Intelligent Tiering file systems. Required when `StorageType`
  is set to `INTELLIGENT_TIERING`. See
  [LustreReadCacheConfiguration](../../../fsx/latest/APIReference/API_LustreReadCacheConfiguration.md "../../../fsx/latest/APIReference/API_LustreReadCacheConfiguration.md") for more details.
- `EfaEnabled` - Specifies whether Elastic Fabric Adapter (EFA)
  and GPUDirect Storage (GDS) support is enabled for the FSx for Lustre file system.
  For complete details about all available parameters in
  `LustreConfiguration`, please see
  [CreateFileSystemLustreConfiguration](../../../fsx/latest/APIReference/API_CreateFileSystemLustreConfiguration.md "../../../fsx/latest/APIReference/API_CreateFileSystemLustreConfiguration.md") in the
  _Amazon FSx API Reference_.

You can specify the following metadata during an FSx for ONTAP restore:

- Name #name of volume to be created
- OntapConfiguration: # ontap configuration
- `junctionPath`
- `sizeInMegabytes`
- `storageEfficiencyEnabled`
- `storageVirtualMachineId`
- `tieringPolicy`

You can specify the following subfields of `OpenZFSConfiguration`
in the metadata during an FSx for OpenZFS restore:

- `ThroughputCapacity` - Specifies the throughput
  capacity of the restored file system, measured in MB/s.
- `DiskIopsConfiguration` - When specifying Iops for SSD storage
  class, use a value between 0 and 160,000. Do not include Mode when Iops is
  specified.
- `ReadCacheConfiguration` - Specifies the provisioned SSD read
  cache for Intelligent Tiering file systems. Required when `StorageType`
  is set to `INTELLIGENT_TIERING`. See
  [OpenZFSReadCacheConfiguration](../../../fsx/latest/APIReference/API_OpenZFSReadCacheConfiguration.md "../../../fsx/latest/APIReference/API_OpenZFSReadCacheConfiguration.md") for more details.
  For complete details about all available parameters in
  `OpenZFSConfiguration`, please see
  [CreateFileSystemOpenZFSConfiguration](../../../fsx/latest/APIReference/API_CreateFileSystemOpenZFSConfiguration.md "../../../fsx/latest/APIReference/API_CreateFileSystemOpenZFSConfiguration.md") in the
  _Amazon FSx API Reference_.

Example CLI restore command:

```
aws backup start-restore-job --recovery-point-arn "arn:aws:fsx:us-west-2:1234:backup/backup-1234" --iam-role-arn "arn:aws:iam::1234:role/Role" --resource-type "FSx" --region us-west-2 --metadata 'SubnetIds="[\"subnet-1234\",\"subnet-5678\"]",StorageType=HDD,SecurityGroupIds="[\"sg-bb5efdc4\",\"sg-0faa52\"]",WindowsConfiguration="{\"DeploymentType\": \"MULTI_AZ_1\",\"PreferredSubnetId\": \"subnet-1234\",\"ThroughputCapacity\": \"32\"}"'
```

Example restore metadata:

```
"restoreMetadata":  "{\"StorageType\":\"SSD\",\"KmsKeyId\":\"arn:aws:kms:us-east-1:`123456789012`:key/`123456a-123b-123c-defg-1h2i2345678`\",\"StorageCapacity\":\"1200\",\"VpcId\":\"vpc-0ab0979fa431ad326\",\"FileSystemType\":\"LUSTRE\",\"LustreConfiguration\":\"{\\\"WeeklyMaintenanceStartTime\\\":\\\"4:10:30\\\",\\\"DeploymentType\\\":\\\"PERSISTENT_1\\\",\\\"PerUnitStorageThroughput\\\":50,\\\"CopyTagsToBackups\\\":true}\",\"FileSystemId\":\"fs-0ca11fb3d218a35c2\",\"SubnetIds\":\"[\\\"subnet-0e66e94eb43235351\\\"]\"}"
```
