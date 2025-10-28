# Protecting your data with volume backups

With FSx for ONTAP, you can protect your data by taking automatic daily backups and user-initiated backups of the
volumes on your file system. Creating regular backups for your volumes
is a best practice that helps support your data retention and compliance needs.
You can restore volume backups to any existing FSx for ONTAP file system you have
access to that is in the same AWS Region where the backup is stored. Working with Amazon FSx
backups makes it is easy to create, view, restore, and delete backups of your volumes.

Amazon FSx supports backing up ONTAP volumes with an `OntapVolumeType` of read-write (RW).

###### Note

Amazon FSx doesn't support backing up data protection (DP) volumes, load sharing mirror (LSM) volumes,
or destination volumes for FlexCache and SnapMirror.

###### Topics

- [How backups work](#how-backups-work "#how-backups-work")
- [Storage requirements](#storage-requirements "#storage-requirements")
- [Automatic daily backups](#automatic-backups "#automatic-backups")
- [User-initiated backups](#user-initiated-backups "#user-initiated-backups")
- [Copying tags to backups](#copy-tags-to-backups "#copy-tags-to-backups")
- [Using AWS Backup with Amazon FSx](#aws-backup-and-fsx "#aws-backup-and-fsx")
- [Restoring backups to a new volume](#restoring-backups "#restoring-backups")
- [Backup and restore performance](#backup-performance "#backup-performance")
- [Backing up SnapLock volumes](#snaplock-backup "#snaplock-backup")
- [Creating user-initiated backups](creating-backups.md "creating-backups.md")
- [Restoring a backup to a new volume](to-restore-backups.md "to-restore-backups.md")
- [Restoring a subset of data](data-subset-restore.md "data-subset-restore.md")
- [Monitoring progress when restoring a backup](monitor-backup-restore.md "monitor-backup-restore.md")
- [Deleting backups](how-to-delete-backups.md "how-to-delete-backups.md")

## How backups work

All Amazon FSx backups (automatic daily backups and user-initiated backups) are incremental, which
means that they only store changes in the data since the previous backup was completed. This minimizes both the time required to create a
backup and the amount of storage used by each backup. Incremental backups optimize storage costs
by not storing duplicate data. FSx for ONTAP backups are per volume, with each backup containing only the
data of one specific volume. Amazon FSx backups are stored redundantly across multiple Availability Zones
to achieve high durability.

Amazon FSx backups use snapshots – point-in-time, read-only images of your volumes – to maintain
incrementality between backups. Each time a backup is taken, Amazon FSx first takes a snapshot of your
volume. The backup snapshot is stored in your volume, and consumes storage space on the volume.
Amazon FSx then compares this snapshot to the previous backup snapshot (if one exists) and copies only
the changed data into your backup.

If no prior backup snapshot exists, then the entire contents
of the most recent backup snapshot is copied into your backup. After the latest backup snapshot
is successfully taken, Amazon FSx deletes the previous backup snapshot. The snapshot used for the
latest backup remains in your volume until the next backup is taken, when the process repeats.
To optimize backup storage costs, ONTAP preserves a volume's storage efficiency
savings in its backups.

When you [delete](how-to-delete-backups.md "how-to-delete-backups.md") a backup, only the data unique to that
backup is deleted. Each Amazon FSx backup contains all of the information that is needed to create a
new volume from the backup, effectively restoring a point-in-time snapshot of the volume.

There are limits to the number of backups that you can store per AWS account and per volume.
For more information, see [Quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits") and
[Resource quotas for each file
system](limits.md#limits-ontap-resources-file-system "limits.md#limits-ontap-resources-file-system").

## Storage requirements

Your volume and your file system must each have enough
available SSD storage capacity to store a backup snapshot. When taking a backup
snapshot, the additional storage capacity consumed by the snapshot cannot cause the
volume to exceed 98% SSD storage utilization. If this happens, the backup will fail. You can
[increase a volume's](manage-volume-capacity.md "manage-volume-capacity.md") or
[file system's](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage") SSD storage
at anytime to ensure that your backups won't be interrupted.

## Automatic daily backups

When you create a file system, automatic daily backups are enabled by default for your file system's volumes.
You can enable or disable automatic daily backups for existing file systems at any time. Automatic daily backups for all volumes occur
during the file system's daily backup window, which is automatically set when you create a file system.
You can modify the daily backup window at any time. For optimal [backup performance](#backup-performance "#backup-performance"), we recommend that
you choose a daily backup window that is outside of the normal operating hours
when clients and applications are accessing the data on your volumes.

Using the console, you can set the retention period for automatic daily backups to a value from 1 to 90 days
when creating a file system or at any time. The default automatic daily backup
retention period is 30 days. Amazon FSx deletes an automatic daily backup once its retention period expires.
Using the AWS CLI and API, you can set the retention period to a value from 0 to 90 days; setting it to 0
turns off automatic daily backups.

Automatic daily backups, the daily backup window, and the backup retention period are file system settings, and
apply to all volumes on your file system. You can use the Amazon FSx console, the AWS CLI, or
API to change these settings. For more information, see [Updating file systems](updating-file-system.md "updating-file-system.md").

You can't create a volume backup (automatic daily backups or user-initiated backups) if the volume is offline.
For more information, see [Viewing offline volumes](offline-volumes.md "offline-volumes.md").

###### Note

Automatic daily backups have a maximum retention period of 90 days, but
[user-initiated backups](#user-initiated-backups "#user-initiated-backups") that you
create, which include backups created using AWS Backup, are retained
forever unless you or AWS Backup deletes them.

You can manually [delete](how-to-delete-backups.md "how-to-delete-backups.md") an automatic daily backup using the Amazon FSx console, CLI, and API.
When you delete a volume, you also delete the automatic daily backups for that volume.
Amazon FSx provides the option to create a final backup of a volume before you delete it. The final
backup is kept forever, unless you delete it.

## User-initiated backups

With Amazon FSx, you can manually take backups of your file system's volumes at any time
using the AWS Management Console, AWS CLI, and API. Your user-initiated
backups are incremental relative to other backups that may have been created for a volume
and are retained forever, unless you delete them. User-initiated backups are retained
even after you delete the volume or the file system the backups were created on. You can
[delete user-initiated backups](how-to-delete-backups.md "how-to-delete-backups.md") only by using the Amazon FSx console,
API, or CLI. They are never automatically deleted by Amazon FSx.

For instructions on how to create a user-initiated backup, see
[Creating user-initiated backups](creating-backups.md "creating-backups.md").

## Copying tags to backups

When you create or update a volume using the CLI or API, you can enable
`CopyTagsToBackups` to [automatically copy any tags](creating-volumes.md#create-volume-cli "creating-volumes.md#create-volume-cli")
on your volume to its backups. However, if you add any tags while creating a user-initiated backup,
including naming a backup when you use the console, Amazon FSx does _not_ copy
tags from the volume, even if `CopyTagsToBackups` is enabled.

## Using AWS Backup with Amazon FSx

AWS Backup is a simple and cost-effective way to protect your data by backing up your
Amazon FSx for NetApp ONTAP volumes. AWS Backup is a unified backup service designed to simplify the creation,
restoration, and deletion of backups, while providing improved reporting and auditing. Using AWS Backup
makes it easier to develop a centralized backup strategy for legal, regulatory, and professional
compliance. It also makes protecting your AWS storage volumes, databases, and file systems
simpler by providing a central place where you can do the following:

- Configure and audit the AWS resources that you want to back up.
- Automate backup scheduling.
- Set retention policies.
- Monitor all recent backup, copy, and restore activity.

AWS Backup uses the built-in backup functionality of Amazon FSx. Backups created using the AWS Backup console
have the same level of file system consistency and performance, are incremental relative to any
other Amazon FSx user-initiated backups taken of your volume, and offer the
same restore options as backups taken using the Amazon FSx console. Using AWS Backup to manage these
backups provides additional functionality, including the ability to create scheduled backups as
frequently as every hour. You can add an additional layer of defense to protect backups from
inadvertent or malicious deletions by storing them in a
[backup vault](../../../aws-backup/latest/devguide/vaults.md "../../../aws-backup/latest/devguide/vaults.md").

Backups created by AWS Backup are considered user-initiated backups, and they count toward the
user-initiated backup quota for Amazon FSx. For more information, see
[Quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits").
You can view and restore backups created by AWS Backup using the
Amazon FSx console, CLI, and API. However, you can't delete backups created by AWS Backup in the Amazon FSx
console, CLI, or API. For more information, see [Getting started with AWS Backup](../../../aws-backup/latest/devguide/getting-started.md "../../../aws-backup/latest/devguide/getting-started.md")
in the AWS Backup Developer Guide.

AWS Backup can't back up volumes that are offline.

You can use tags to select which of your FSx for ONTAP resources are protected
in a backup plan. These tags must be applied at the volume level rather than the
file system level as a whole. For more information, see
[Assigning resources to a backup plan](../../../aws-backup/latest/devguide/assigning-resources.md "../../../aws-backup/latest/devguide/assigning-resources.md")
in the AWS Backup Developer Guide.

## Restoring backups to a new volume

You can restore a volume backup to a new volume on a file system that is in the same AWS Region
that the backup is stored in. You cannot restore a backup to a file system that is located in a different AWS Region than
the backup.

When restoring a backup on FSx for ONTAP second-generation file systems,
clients can mount and read data from a volume while it is being restored.
Clients can mount the volume you are restoring and read the file data once Amazon FSx has loaded all the metadata onto the
new volume and the volume reports a lifecycle status of `CREATED`. You can find a volume's lifecycle state
on the [Volumes detail](viewing-volumes.md "viewing-volumes.md") page in the Amazon FSx console and in the response of the
[describe-volumes](../../../v2/documentation/api/latest/reference/fsx/describe-volumes.md "../../../v2/documentation/api/latest/reference/fsx/describe-volumes.md") CLI command.

When reading data from a volume while it is being restored from a backup,
if the data has not been downloaded onto the volume yet, you will incur read latencies of up to tens of
milliseconds for the first access. These reads are cached in the SSD tier, and you can expect sub-millisecond
read latencies for subsequent reads.

The amount of time it takes for Amazon FSx to make a volume available for read-only access is proportional to the amount of file
metadata stored in the backup. File metadata typically consumes 1-7% of the overall backup data depending on the average file size
in your data set (small file data sets consume more metadata than large file data sets).

When you restore a FlexGroup volume backup to a file system that has a different number of
[high-availability (HA) pairs](HA-pairs.md "HA-pairs.md") than the original file system, Amazon FSx
adds additional constituent volumes to ensure that the constituents are evenly distributed.

###### Note

Amazon FSx does not support read access to data while a volume is being
restored from a backup for either SnapLock volumes or for any volumes on first-generation file systems.
When restoring these backups, the volume becomes available to mount and access data after the restore
process is completed, and all metadata and data are loaded onto the new volume.

When restoring a backup, all data is initially written to the SSD storage tier. While the restore is in progress, data is
tiered to the capacity pool storage in accordance with the [tiering policy](volume-storage-capacity.md#volume-data-tiering "volume-storage-capacity.md#volume-data-tiering") of volume being restored.
Since data is first written to the SSD tier, Amazon FSx will pause the restoration process if the
file system runs out of SSD storage space. The restore automatically resumes as soon as sufficient
SSD space becomes available to continue the process. If the restored volume's tiering policy is `All`,
a periodic background process tiers the data to the capacity pool.
If the restored volume's tiering policy is `Snapshot Only` or `Auto`,
data is tiered to the capacity pool if the SSD utilization for the file system is greater than 50%,
and the cooling rate is determined by the tiering policy’s cooling period.

If your workload requires consistent sub-millisecond read latencies when restoring a backup
to a new volume on second-generation file systems, we recommend that you set the volume’s tiering policy to
`None` when initiating the restore, and then wait until all data has been fully downloaded onto the volume
before you access it. All data will be loaded into SSD storage before you attempt to access it,
providing you with consistent low-latency access to your data.

For step-by-step instructions on how to restore a backup to a new volume,
see [Restoring a backup to a new volume](to-restore-backups.md "to-restore-backups.md").

On second-generation file systems you can also restore just a subset of data from a backup without having to wait for the entire
restore operation to complete. Restoring just a subset of a backup's data enables you to resume operations faster
in the event of accidental deletion, modification, or corruption of data.
For more information, see [Restoring a subset of data](data-subset-restore.md "data-subset-restore.md").

You can monitor the progress when restoring a backup on a second-generation file system in the AWS Management Console, AWS CLI, and API.
For more information, see [Monitoring progress when restoring a backup](monitor-backup-restore.md "monitor-backup-restore.md").

###### Note

- You can't create a volume snapshot or perform snapshot-based
  operations such as cloning, SnapMirror replication, and creating backups of a volume while it is
  being restored from a backup.
- A restored volume always has the same volume style as the original volume.
  You can't change the volume style when restoring.

## Backup and restore performance

A variety of factors can influence the performance of backup and restore operations.
Backup and restore operations are background processes, which means they have a lower priority relative to
client IO operations. Client IO operations include NFS, CIFS, and iSCSI data and metadata reads and writes.
All background processes utilize only the unused portion
of your file system’s throughput capacity, and can take from a few minutes to a few hours to complete
depending on the size of your backup and the amount of unused throughput capacity on your file system.

Other factors that affect backup and restore performance include the storage tier in which your data is
stored and the dataset profile. We recommend that you create the first backups of your volumes
when most of the data is on SSD storage. Datasets containing mostly small files will typically have
lower performance as compared to similarly sized datasets that contain mostly large files.
This is because processing large numbers of small files consumes more CPU cycles and network overhead
than processing fewer large files.

Generally, you can expect the following backup rates when backing up data stored in the SSD storage tier:

- 750 MBps across several concurrent backups containing mostly large files.
- 100 MBps across several concurrent backups containing mostly small files.

Generally, you can expect the following restore rates:

- 250 MBps across several concurrent restores containing mostly large files.
- 100 MBps across several concurrent restores containing mostly small files.

## Backing up SnapLock volumes

You can back up [SnapLock](snaplock.md "snaplock.md") volumes for additional data protection. When you restore a
SnapLock volume, the volume's original settings—such as the default retention,
minimum retention, and maximum retention—are preserved. Write once, read many
(WORM) settings and Legal Hold are also preserved.

###### Note

You can't back up a SnapLock FlexGroup volume.

You can restore a SnapLock volume's backup as a SnapLock or a non-SnapLock volume. However, you can't
restore a non-SnapLock volume's backup as a SnapLock volume.

For more information, see [How SnapLock works](how-snaplock-works.md "how-snaplock-works.md").
