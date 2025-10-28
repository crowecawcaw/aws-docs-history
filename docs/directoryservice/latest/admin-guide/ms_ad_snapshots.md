# Restoring your AWS Managed Microsoft AD with snapshots

AWS Directory Service provides automated daily snapshots and the ability to take manual snapshots of
data for your AWS Managed Microsoft AD Active Directory. These snapshots can be used to perform a point-in-time restore
for your Active Directory. You are limited to five manual snapshots for each AWS Managed Microsoft AD Active Directory. If you have
already reached this limit, you must delete one of your existing manual snapshots before you can
create another. You cannot take snapshots of AD Connector directories.

###### Note

Snapshot is a global feature of AWS Managed Microsoft AD. If you are using [Configure Multi-Region
replication for AWS Managed Microsoft AD](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"), the following procedures must be
performed in the [Primary Region](multi-region-global-primary-additional.md#multi-region-primary "multi-region-global-primary-additional.md#multi-region-primary"). The changes will be applied across all replicated Regions
automatically. For more information, see [Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

###### Topics

- [Creating a snapshot of your directory](#snapshot_create "#snapshot_create")
- [Restoring your directory from a snapshot](#snapshot_restore "#snapshot_restore")
- [Deleting a snapshot](#snapshot_delete "#snapshot_delete")

## Creating a snapshot of your directory

A snapshot can be used to restore your directory to what it was at the point in time that
the snapshot was taken. To create a manual snapshot of your directory, perform the following
steps.

###### Note

You are limited to 5 manual snapshots for each directory. If you have
already reached this limit, you must delete one of your existing manual snapshots before you
can create another.

Use the following procedure to create a manual snapshot of your AWS Managed Microsoft AD with the
AWS Management Console, AWS CLI, or PowerShell:

AWS Management Console

###### To create a manual snapshot in the AWS Management Console

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, choose the
   **Maintenance** tab.
4. In the **Snapshots** section, choose
   **Actions**, and then select **Create
   snapshot**.
5. In the **Create directory snapshot** dialog box, provide a name
   for the snapshot, if desired. When ready, choose **Create**.

AWS CLI

###### To create a manual snapshot with AWS CLI

- Open the AWS CLI. To create a snapshot of your AWS Managed Microsoft AD, run the following
  command, replacing the Directory ID with your AWS Managed Microsoft AD Directory ID:

```
aws ds create-snapshot --directory-id `d-1234567890` --name ManualSnapshot
```

For more information, see [`create-snapshot`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-snapshot.html").

PowerShell

###### To create a manual snapshot with PowerShell

- Open PowerShell. To create a snapshot of your AWS Managed Microsoft AD, run
  the following command, replacing the Directory ID with your AWS Managed Microsoft AD Directory
  ID:

```
New-DSSnapshot -DirectoryId `d-1234567890` -Name ManualSnapshot
```

For more information, see [`New-DSSnapshot`](../../../powershell/latest/reference/items/New-DSSnapshot.md "../../../powershell/latest/reference/items/New-DSSnapshot.md").

Depending on the size of your directory, it may take several minutes to create the
snapshot. When the snapshot is ready, the **Status** value changes to
`Completed`.

## Restoring your directory from a snapshot

Restoring a directory from a snapshot is equivalent to moving the directory back in time.
Directory snapshots are unique to the directory they were created from. A snapshot can only be
restored to the directory from which it was created. In addition, the maximum supported age of
a manual snapshot is 180 days. For more information, see [Useful shelf life of a system-state backup of Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad "https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad") on the Microsoft website.

###### Warning

We recommend that you contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") before any snapshot restore;
we may be able to help you avoid the need to do a snapshot restore. Any restore from
snapshot can result in data loss as they are a point in time. It is important you understand
that all of the DCs and DNS servers associated with the directory will be offline until the
restore operation has been completed.

Use the following procedure to restore your directory from a snapshot using the AWS Management Console,
AWS CLI, or PowerShell:

AWS Management Console

###### To restore a directory from a snapshot in the AWS Management Console

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, choose the
   **Maintenance** tab.
4. In the **Snapshots** section, select a snapshot in the list,
   choose **Actions**, and then select **Restore
   snapshot**.
5. Review the information in the **Restore directory snapshot**
   dialog box, and choose **Restore**.

AWS CLI

###### To restore a directory from a snapshot with AWS CLI

1. Open the AWS CLI. To list the snapshots for your AWS Managed Microsoft AD, run the following
   command, replacing the Directory ID with your AWS Managed Microsoft AD Directory ID:

```
aws ds describe-snapshots --directory-id `d-1234567890` \
  --query '(sort_by(Snapshots[*].{ID:SnapshotId,Status:Status,Type:Type,StartTime:StartTime}, &StartTime))' \
  --output table
```

2. To restore your AWS Managed Microsoft AD from a snapshot, you can use the [`restore-from-snapshot`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/restore-from-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/restore-from-snapshot.html") command. Ensure you replace the
   `snapshot-id` parameter with the snapshot ID you want to use to restore
   your AWS Managed Microsoft AD:

```
aws ds restore-from-snapshot --snapshot-id `s-1234567890`
```

PowerShell

###### To restore a directory from a snapshot with PowerShell

1. Open PowerShell. To list the snapshots for your AWS Managed Microsoft AD, run the following
   command, replacing the Directory ID with your AWS Managed Microsoft AD Directory ID:

```
Get-DSSnapshot -DirectoryId `d-1234567890` | Sort-Object StartTime | Format-Table
```

2. To restore your AWS Managed Microsoft AD from a snapshot, you can use the [`Restore-DSFromSnapshot`](../../../powershell/latest/reference/items/Restore-DSFromSnapshot.md "../../../powershell/latest/reference/items/Restore-DSFromSnapshot.md") command. Ensure you replace the
   `snapshot-id` parameter with the snapshot ID you want to use to restore
   your AWS Managed Microsoft AD:

```
Restore-DSFromSnapshot -SnapshotId `s-1234567890`
```

For an AWS Managed Microsoft AD directory, it can take from two to three hours for the directory to be
restored. When it has been successfully restored, the **Status** value of the
directory changes to `Active`. Any changes made to the directory after the snapshot
date are overwritten.

## Deleting a snapshot

Use the following procedure to delete a snapshot of your AWS Managed Microsoft AD with the
AWS Management Console, AWS CLI, or PowerShell:

AWS Management Console

###### To delete a snapshot in the AWS Management Console

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, choose the **Maintenance** tab.
4. In the **Snapshots** section, choose **Actions**,
   and then select **Delete snapshot**.
5. Verify that you want to delete the snapshot, and then choose
   **Delete**.

AWS CLI

###### To delete a snapshot with AWS CLI

1. Open the AWS CLI. To list the snapshots for your AWS Managed Microsoft AD, run the following
   command, replacing the Directory ID with your AWS Managed Microsoft AD Directory ID:

```
aws ds describe-snapshots --directory-id `d-1234567890` \
  --query '(sort_by(Snapshots[*].{ID:SnapshotId,Status:Status,Type:Type,StartTime:StartTime}, &StartTime))' \
  --output table
```

2. To delete a snapshot of your AWS Managed Microsoft AD, you can use the [`delete-snapshot`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-snapshot.html") command. Ensure you replace the
   `snapshot-id` parameter with the snapshot ID of the snapshot you want to delete:

```
aws ds delete-snapshot --snapshot-id `s-1234567890`
```

PowerShell

###### To delete a snapshot with PowerShell

1. Open PowerShell. To list the snapshots for your AWS Managed Microsoft AD, run the following
   command, replacing the Directory ID with your AWS Managed Microsoft AD Directory ID:

```
Get-DSSnapshot -DirectoryId `d-1234567890` | Sort-Object StartTime | Format-Table
```

2. To restore your AWS Managed Microsoft AD from a snapshot, you can use the [`Remove-DSnapshot`](../../../powershell/latest/reference/items/Remove-DSSnapshot.md "../../../powershell/latest/reference/items/Remove-DSSnapshot.md") command. Ensure you replace the
   `snapshot-id` parameter with the snapshot ID of the snapshot you want to delete:

```
Remove-DSSnapshot -SnapshotId `s-1234567890`
```
