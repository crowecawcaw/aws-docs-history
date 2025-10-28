# Protecting your data with snapshots

A _snapshot_ is a read-only image of an FSx for OpenZFS
volume at a point in time. Snapshots offer protection against accidental deletion or modification
of files in your volumes. With snapshots, your users can easily view and restore
individual folders and files from an earlier snapshot. Doing this enables users to
easily undo changes and compare file versions.

Because snapshots are stored alongside your ﬁle system's data, they consume
the ﬁle system's storage capacity. However, snapshots consume storage capacity only for
the changed portions of ﬁles since the last snapshot.

Snapshots are stored in the `.zfs/snapshot` directory at the root of a volume.

###### Topics

- [Using snapshots to create volumes](#snapshots-volumes "#snapshots-volumes")
- [Creating a snapshot](#creating-snapshots "#creating-snapshots")
- [Deleting a snapshot](#deleting-snapshots "#deleting-snapshots")
- [Viewing a snapshot](#viewing-snapshots "#viewing-snapshots")
- [Restoring a volume from a snapshot](#restore-volume-from-snapshot "#restore-volume-from-snapshot")
- [Restoring individual files and folders](#snapshots-user-restore "#snapshots-user-restore")
- [Setting up a custom snapshot schedule](custom-snapshot-schedule.md "custom-snapshot-schedule.md")

## Using snapshots to create volumes

You can use a snapshot to create a clone volume or a full-copy volume.

A clone volume is a writable copy that is initialized with the same data as
the snapshot from which it was created. Clone volumes provide an easy way to
support multiple users or applications in parallel from a shared dataset, as well
as quickly test new changes to your databases or applications. Clone volumes are
created almost instantly and initially consume no additional storage capacity.
(They only consume capacity for incremental changes to the source snapshot.)
However, each clone volume maintains a dependency on its source snapshot, so
you cannot delete this source snapshot while the clone volume is in use. To
split a clone from its source snapshot and remove this dependency, you must
create a new full-copy volume from that clone.

A full-copy volume is also initialized with the same data as its source
snapshot, but is a fully independent writable copy. However, because a full-copy
volume requires transferring all of the data from the source snapshot, it can
take a significantly longer time to create than a clone volume. Once a
full-copy volume is created, it is identical to a standard FSx for OpenZFS
volume and does not maintain any relationship to its source snapshot.

For more information on creating clone and full-copy volumes,
see [Managing Amazon FSx for OpenZFS volumes](managing-volumes.md "managing-volumes.md").

## Creating a snapshot

You can create an FSx for OpenZFS snapshot using the Amazon FSx console, the AWS CLI, and the
Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, under **OpenZFS**, choose
   **Snapshots**. Then in the **Snapshots** pane,
   choose **Create snapshot**.

You can also create a snapshot directly by navigating to the **Snapshots**
tab of an individual volume and choosing **Create snapshot**. 3. In the **File system** field of the **Create snapshot**
dialog box, choose the file system to create the snapshot on. 4. In the **Volume** field, choose an existing volume
you want to take a snapshot of. 5. In the **Snapshot name** field, provide a name for the
snapshot. You can use a maximum of 203 alphanumeric characters, and the special
characters . - \_ : 6. Choose **Confirm** to create the snapshot.
The snapshot is ready for use when its status is **Available**.

- To create an FSx for OpenZFS snapshot, use the [create-snapshot](../../../cli/latest/reference/fsx/create-snapshot.md "../../../cli/latest/reference/fsx/create-snapshot.md")
  CLI command (or the equivalent [CreateSnapshot](../APIReference/API_CreateSnapshot.md "../APIReference/API_CreateSnapshot.md") API operation), as shown in the following example.

```
`aws fsx create-snapshot \
 --volume-id fsvol-123 \
 --name snapshot2`
```

The command example uses the following parameters:

- `volume-id` - The ID of the volume that you are taking a snapshot of.
- `name` - The name of the source snapshot.
  After successfully creating the snapshot, Amazon FSx returns its description in
  JSON format.

## Deleting a snapshot

You can delete an FSx for OpenZFS snapshot using the Amazon FSx console, the AWS CLI, and the
Amazon FSx API. After deletion, the snapshot no longer exists, and its data is gone. Deleting
a snapshot doesn't affect snapshots stored in a file system backup.

###### Note

A snapshot can't be deleted if it was previously cloned and that clone
is still available. Before you can delete the snapshot, you must first delete all
of the snapshot's clones.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, under **OpenZFS**,choose
   **Snapshots**.
3. In the **Snapshots** page, choose the snapshot that
   you want to delete.
4. In the **Summary** page for the snapshot, choose
   **Delete**.

- To delete an FSx for OpenZFS volume, use the [delete-volume](../../../cli/latest/reference/fsx/delete-snapshot.md "../../../cli/latest/reference/fsx/delete-snapshot.md") CLI command (or the equivalent [DeleteVolume](../APIReference/API_DeleteSnapshot.md "../APIReference/API_DeleteSnapshot.md") API operation), as shown in the following example.

```
`aws fsx delete-snapshot --snapshot-id fsvolsnap-1234`
```

## Viewing a snapshot

You can see the FSx for OpenZFS volumes that are currently on your file system using the
Amazon FSx console, the AWS CLI, and the Amazon FSx API and SDKs.

###### To view the snapshots on your file system:

- **Using the console** – Choose a file
  system to view the **File systems** detail page. Choose the
  **Volumes** tab to list all the volumes on the file
  system, and then choose a volume. The volume's **Summary**
  page has a **Snapshots** tab that lists the snapshots for
  the volume.
- **Using the CLI or API** – Use the
  [describe-snapshots](../../../cli/latest/reference/fsx/describe-snapshots.md "../../../cli/latest/reference/fsx/describe-snapshots.md") CLI command or the [DescribeSnapshots](../APIReference/API_DescribeSnapshots.md "../APIReference/API_DescribeSnapshots.md") API operation.

## Restoring a volume from a snapshot

You can return a volume to a state saved by a specified snapshot. You use
the [restore-volume-from-snapshot](../../../cli/latest/reference/fsx/restore-volume-from-snapshot.md "../../../cli/latest/reference/fsx/restore-volume-from-snapshot.md")
CLI command (or the equivalent [RestoreVolumeFromSnapshot](../APIReference/API_RestoreVolumeFromSnapshot.md "../APIReference/API_RestoreVolumeFromSnapshot.md") API operation), as shown in the following example.

```
`aws fsx restore-volume-from-snapshot \
 --volume-id fsvol-12345 \
 --snapshot-id fsvolsnap-67890 \
 --options DELETE_INTERMEDIATE_SNAPSHOTS DELETE_CLONED_VOLUMES`
```

The command example uses the following parameters:

- `volume-id` - The ID of the volume that you are restoring.
- `snapshot-id` - The ID of the source snapshot. Specifies the snapshot
  you are restoring from.
- `DELETE_INTERMEDIATE_SNAPSHOTS` - Deletes snapshots between the
  current state and the specified snapshot. `restore-volume-from-snapshot`
  will fail if there are intermediate snapshots and this option isn't used.
- `DELETE_CLONED_VOLUMES` - Deletes any volumes cloned from this
  volume. `restore-volume-from-snapshot` will fail if there are any cloned
  volumes and this option isn't used.

## Restoring individual files and folders

Using the snapshots on your Amazon FSx file system, your users can quickly restore
previous versions of individual files or folders. Doing this enables them to recover deleted or
changed files stored on the shared file system. They do this in a self-service manner directly on
their desktop without administrator assistance. This self-service approach increases productivity
and reduces administrative workload.

Linux, macOS, and Windows clients can view snapshots in the `.zfs/snapshot` directory
hidden at the root of a volume. The `.zfs` directory is hidden, so it will not appear in
any `ls` or `dir` results. You must also specify the `crossmnt` option
in the `NFS exports` configuration of your FSx for OpenZFS volume to enable your clients to
navigate to this directory.

###### To restore a file from a snapshot (Linux, macOS, and Windows clients)

1. If the original file still exists and you do not want it overwritten by the file in a snapshot,
   then use your Linux, macOS, or Windows client to rename the original file or move it to a different directory.
2. In the `.zfs/snapshot` directory, locate the snapshot that contains the version of the file
   that you want to restore.
3. Copy the file from the `.zfs/snapshot` directory to the directory in which the file
   originally existed.

Data in snapshots is read only. If you want to make modifications to files and folders in a snapshot,
you must save a copy of the files and folders to a writable location and make modifications to these copies.
