# Create Lightsail block storage disk

snapshots for backup or baseline

You can create disk snapshots in Amazon Lightsail as backups of your additional block storage
disks.

You can use the snapshot of a disk as a baseline for new disks or for data backup. If you
make periodic snapshots of a disk, the snapshots are incremental. Only the blocks on the device
that have changed after your last snapshot are saved in the new snapshot. Even though snapshots
are saved incrementally, the snapshot deletion process is designed so that you need to retain
only the most recent snapshot to restore the entire disk.

For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

1. In the left navigation pane, choose **Storage**.
2. Choose the name of the block storage disk for which you want to create a
   snapshot.
3. Choose the **Snapshots** tab.
4. Under the **Manual snapshots** section of the page, choose
   **Create snapshot**, then enter a name for your snapshot.

Resource names:

    * Must be unique within each AWS Region in your Lightsail account.
    * Must contain 2 to 255 characters.
    * Must start and end with an alphanumeric character or number.
    * Can include alphanumeric characters, numbers, periods, dashes, and
     underscores.

5. Choose **Create**.

You can see the snapshot you just created with a status of
**Snapshotting...**.

After the snapshot is finished, you can [create another disk from the
snapshot](create-new-block-storage-disk-from-snapshot.md "create-new-block-storage-disk-from-snapshot.md").
