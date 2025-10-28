# Testing your gateway

You test your Volume Gateway setup by performing the following tasks:

1. Write data to the volume.
2. Take a snapshot.
3. Restore the snapshot to another volume.
   You verify the setup for a gateway by taking a snapshot backup of your volume and storing
   the snapshot in AWS. You then restore the snapshot to a new volume. Your gateway copies
   the data from the specified snapshot in AWS to the new volume.

###### Note

Restoring data from Amazon Elastic Block Store (Amazon EBS) volumes that are encrypted is not
supported.

###### To create an Amazon EBS snapshot of a storage volume on Microsoft Windows

1. On your Windows computer, copy some data to your mapped storage volume.

The amount of data copied doesn't matter for this demonstration. A small file is
enough to demonstrate the restore process. 2. In the navigation pane of the Storage Gateway console, choose
**Volumes**. 3. Choose the storage volume that you created for the gateway.

This gateway should have only one storage volume. Choose the volume displays its
properties. 4. For **Actions**, choose **Create EBS snapshot**
to create a snapshot of the volume.

Depending on the amount of data on the disk and the upload bandwidth, it might
take a few seconds to complete the snapshot. Note the volume ID for the volume from
which you create a snapshot. You use the ID to find the snapshot. 5. In the **Create EBS Snapshot** dialog box, provide a description
for your snapshot. 6. (Optional) For **Tags**, enter a key and value to add tags to the
snapshot. A tag is a case-sensitive key-value pair that helps you manage, filter,
and search for your snapshots. 7. Choose **Create Snapshot**. Your snapshot is stored as an Amazon EBS
snapshot. Note your snapshot ID. The number of snapshots created for your volume is
displayed in the snapshot column. 8. In the **EBS snapshots** column, choose the link for the volume
that you created the snapshot for to see your EBS snapshot on the Amazon EC2
console.

###### To restore a snapshot to another volume

See [Creating a storage volume](GettingStartedCreateVolumes.md "GettingStartedCreateVolumes.md").
