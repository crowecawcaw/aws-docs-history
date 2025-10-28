# Restoring a subset of data

You can restore a subset of data from a backup while it is being restored to a new volume
on second-generation file systems without having to wait until the entire backup data set has been fully restored.

The following procedure lists the steps to take when you need to recover a subset of data when
restoring a backup, and can't wait for the entire restore to complete:

###### To restore a subset of data while restoring a backup

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the **Backups** page, locate the backup that contains the version
   of the data that you want to restore.
3. In the upper right **Actions** menu, choose **Restore backup**.
   The **Create volume from backup page appears.**
4. Choose the FSx for ONTAP **File system** and **Storage virtual machine**
   that you want to restore the backup to from the dropdown menus.
5. Under **Volume details**, configure the volume to meet your needs.
6. Choose **Confirm** to create the volume.
7. [Monitor the progress](monitor-backup-restore.md "monitor-backup-restore.md") of the backup restore.
8. [Mount the volume](supported-fsx-clients.md "supported-fsx-clients.md") being restored when it reports
   a lifecycle status of `CREATED`.
9. Locate the subset of the data on the volume you need to copy.
10. Copy the data to the existing volume that your application uses.
11. Once the required data from the backup has been copied over to the target location,
    you can delete the volume being restored before it completes to optimize utilization of
    file system resources.
