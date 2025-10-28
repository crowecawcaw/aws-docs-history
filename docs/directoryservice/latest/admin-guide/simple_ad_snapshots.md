# Restoring your Simple AD with snapshot

AWS Directory Service provides the ability to take manual snapshots of data for your Simple AD
directory. These snapshots can be used to perform a point-in-time restore for your directory.
You cannot take snapshots of AD Connector directories.

###### Topics

- [Creating a snapshot of your directory](#simple_ad_snapshot_create "#simple_ad_snapshot_create")
- [Restoring your directory from a snapshot](#simple_ad_snapshot_restore "#simple_ad_snapshot_restore")
- [Deleting a snapshot](#simple_ad_snapshot_delete "#simple_ad_snapshot_delete")

## Creating a snapshot of your directory

A snapshot can be used to restore your directory to what it was at the point in time
that the snapshot was taken. To create a manual snapshot of your directory, perform the
following steps.

###### Note

You are limited to 5 manual snapshots for each directory. If you
have already reached this limit, you must delete one of your existing manual
snapshots before you can create another.

###### To create a manual snapshot

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Maintenance** tab.
4. In the **Snapshots** section, choose
   **Actions**, and then select **Create snapshot**.
5. In the **Create directory snapshot** dialog box, provide a
   name for the snapshot, if desired. When ready, choose **Create**.

Depending on the size of your directory, it may take several minutes to create the
snapshot. When the snapshot is ready, the **Status** value changes to
`Completed`.

## Restoring your directory from a snapshot

Restoring a directory from a snapshot is equivalent to moving the directory back in
time. Directory snapshots are unique to the directory they were created from. A snapshot can only be restored to the directory from which it was created. In addition, the maximum supported age of a manual snapshot is 180
days. For more information, see [Useful shelf life of a system-state backup of Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad "https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad") on the Microsoft
website.

###### Warning

We recommend that you contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") before any snapshot
restore; we may be able to help you avoid the need to do a snapshot restore. Any restore
from snapshot can result in data loss as they are a point in time. It is important you
understand that all of the DCs and DNS servers associated with the directory will be offline
until the restore operation has been completed.

To restore your directory from a snapshot, perform the following steps.

###### To restore a directory from a snapshot

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Maintenance** tab.
4. In the **Snapshots** section, select a snapshot in the list, choose
   **Actions**, and then select **Restore snapshot**.
5. Review the information in the **Restore directory snapshot** dialog box,
   and choose **Restore**.

For a Simple AD directory, it may take several minutes for the directory to be restored.
When it has been successfully restored, the **Status** value of the directory
changes to `Active`. Any changes made to the directory after the snapshot date are
overwritten.

## Deleting a snapshot

###### To delete a snapshot

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Maintenance** tab.
4. In the **Snapshots** section, choose
   **Actions**, and then select **Delete snapshot**.
5. Verify that you want to delete the
   snapshot, and then choose **Delete**.
