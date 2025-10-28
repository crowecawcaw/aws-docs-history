# Protecting your data with snapshots

A _snapshot_ is a read-only image of an Amazon FSx for NetApp ONTAP
volume at a point in time. Snapshots offer protection against accidental deletion or modification
of files in your volumes. With snapshots, your users can easily view and restore
individual files or folders from an earlier snapshot to
undo changes, recover deleted content, and compare file versions.

A snapshot contains the data that has changed since the last snapshot which consumes
the ﬁle system's SSD storage capacity. Snapshots are not
included in any volume [backups](using-backups.md "using-backups.md"). Snapshots
are enabled by default on your volumes using the `default` snapshot policy.
Snapshots are stored in the `.snapshot` directory at the root of a volume.
You can store a maximum of 1,023 snapshots per volume at any point in time. Once you
reach this limit, you must [delete an existing snapshot](#delete-snapshots "#delete-snapshots") before a new snapshot of your
volume can be created.

###### Topics

- [Snapshot policies](#snapshot-policies "#snapshot-policies")
- [Restoring files from snapshots](user-restore-all-clients.md "user-restore-all-clients.md")
- [Viewing the common snapshot](common-snapshot.md "common-snapshot.md")
- [Updating your volume's snapshot reserve](modify-snapshot-reserve.md "modify-snapshot-reserve.md")
- [Disabling automatic snapshots](disable-snapshots.md "disable-snapshots.md")
- [Deleting snapshots](#delete-snapshots "#delete-snapshots")
- [Deleting snapshots](manually-delete-snapshots.md "manually-delete-snapshots.md")
- [Snapshot reserve](#snapshot-reserve "#snapshot-reserve")

## Snapshot policies

The snapshot policy defines how the system creates snapshots for a volume. The policy
specifies when to create snapshots, how many copies to retain, and how to name them. There are three
built-in snapshot policies for FSx for ONTAP:

- `default`
- `default-1weekly`
- `none`

By default, every volume is associated with the file system's `default`
snapshot policy. We recommend using this policy for most workloads.

The `default` policy automatically creates snapshots on the following schedule,
with the oldest snapshot copies deleted to make room for newer copies:

- A maximum of six hourly snapshots taken five minutes past the hour.
- A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after
  midnight.
- A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.

###### Note

Snapshot times are based on the file system's time zone, which defaults to Coordinated
Universal Time (UTC). You can set an FSx for ONTAP file system's time zone by using the
`timezone -timezone `time_zone`` ONTAP CLI command. For more information
about accessing the ONTAP CLI, see [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli").

The `default-1weekly` policy works in the same way as the
`default` policy, except that it only retains one snapshot from the weekly schedule.

The `none` policy doesn't take any snapshots. You can assign
this policy to volumes to prevent automatic snapshots from being taken.

You can also create a custom snapshot policy using the ONTAP CLI or
REST API. For more information, see [Create a Snapshot Policy](https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html "https://docs.netapp.com/us-en/ontap/data-protection/create-snapshot-policy-task.html") in the _NetApp ONTAP Product
Documentation_. You can
choose a snapshot
policy while creating or updating a volume in the Amazon FSx console, the AWS CLI, or the Amazon FSx API.
For more information, see
[Creating volumes](creating-volumes.md "creating-volumes.md") and
[Updating volumes](updating-volumes.md "updating-volumes.md").

## Deleting snapshots

Snapshots consume storage capacity only for the data on a volume that has changed since the
last snapshot. For this reason, if your workload writes data rapidly, snapshots from old data
can take up a significant amount of a volume's storage capacity.

For example, the
[`volume show-space`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-show-space.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-show-space.html")
ONTAP CLI command output shows 140
KB of `User Data`. However, the volume had 9.8 GB of `User Data` before
the user data was deleted. Even if you've deleted the files from your volume, a snapshot might
still reference old user data. Because of this, `Snapshot Reserve` and `Snapshot
 Spill` in the prior example take up a total of 9.8 GB of space, even though there is
virtually no user data on the volume.

To free up space on volumes, you can delete older snapshots that you no longer need. Because snapshots are incremental,
you do not reclaim the amount of storage equal to the size of the snapshot when you delete it. You can
see the amount of storage you can reclaim when deleting a snapshot by using the
[volume snapshot compute-reclaimable -vserver](https://docs.netapp.com/us-en/ontap-cli-9141/volume-snapshot-compute-reclaimable.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-snapshot-compute-reclaimable.html") ONTAP
ClI command, using your data to replace `svm_name`, `vol_name`, and `snapshot_name`.

```
`fsid8970abc52::>` `volume snapshot compute-reclaimable -vserver `svm_name` -volume `vol_name` -snapshot `snapshot_name``
`A total of 667648 bytes can be reclaimed.`
```

You can delete snapshots either by creating a [snapshot auto-delete policy](snapshot-autodelete-policy.md "snapshot-autodelete-policy.md")
or by [manually deleting snapshots](manually-delete-snapshots.md "manually-delete-snapshots.md").
Deleting a snapshot deletes the changed data stored on the snapshot.

## Snapshot reserve

Snapshot copy reserve sets a specific percent of a volume's storage capacity for storing Snapshot copies,
with a default value of 5 percent. The Snapshot copy reserve must have sufficient space allocated for the Snapshot copies, including
[volume backups](using-backups.md "using-backups.md"). If the Snapshot copies exceeds the Snapshot reserve space,
you must delete existing Snapshot copies from the active file system to recover the storage capacity for the
use of the file system. You can also modify the percent of disk space that is allotted to Snapshot copies.

Whenever Snapshots consume more than 100% of the Snapshot reserve, they begin to occupy primary SSD storage
space. This process is called Snapshot spill. When the Snapshots continue to occupy the active file system space,
the file system is at risk of becoming full. If the file system becomes full due to Snapshot spill, you can create files
only after you delete enough Snapshots.

When enough disk space is available for snapshots in the snapshot reserve, deleting files
from the primary SSD tier frees disk space for new files, while the Snapshot copies that reference
those files consume only the space in the Snapshot copy reserve.

Because there is no way to prevent Snapshots from consuming disk space greater than the amount reserved
for them (the Snapshot reserve), it is important to reserve enough disk space for Snapshots so that the primary
SSD tier always has space available to create new files or modify existing ones.

If a snapshot is created when the disks are full, deleting files from the primary SSD tier does
not create any free space because all that data is also referenced by the newly created Snapshot.
You must [delete the Snapshot](#delete-snapshots "#delete-snapshots") in order to free up storage
in order to create or update any files.

You can modify the amount of Snapshot reserve on a volume using the NetApp ONTAP CLI.
For more information, see [Updating your volume's snapshot reserve](modify-snapshot-reserve.md "modify-snapshot-reserve.md").
