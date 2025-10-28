# Create Amazon EBS snapshots

You can create an Amazon EBS snapshot of an Amazon EBS volume to create a point-in-time backup of that volume.
You can either create snapshots of **individual Amazon EBS volumes**, or
you can create **multi-volume snapshots** of all, or a subset, of the
volumes attached to an Amazon EC2 instance.

Snapshot creation is asynchronous. The snapshot is created immediately, but it remains in the
`pending` state until all of data has been transferred to Amazon S3. This can take several
hours to complete, depending on the number of modified blocks on the volume. You can continue to
use the volume during this time without impacting the snapshot. The snapshot includes only the data
that was written to the volume at the time the snapshot was requested. It does not include data
that has been cached by applications or the operating system.

###### Tip

To ensure consistent and complete snapshots, we recommend that you pause writes to the volume
before you create the snapshot. If you can't pause writes to the volume, we recommend that you
unmount the volume, from within the instance, before you create the snapshot. You can remount
and resume writes once the snapshot enters the `pending` state.

If you create a snapshot of a volume that serves as the root device for an Amazon EC2 instance, we
recommend that you stop the instance before taking the snapshot.

###### Contents

- [Snapshot encryption](#create-snapshot-encryption "#create-snapshot-encryption")
- [Snapshot destinations](#create-snapshot-destinations "#create-snapshot-destinations")
- [Automating snapshots](#create-snapshots-automate "#create-snapshots-automate")
- [Considerations for creating snapshots](#create-snapshots-considerations "#create-snapshots-considerations")
- [Create snapshot of a volume](ebs-create-snapshot.md "ebs-create-snapshot.md")
- [Create multi-volume snapshots](ebs-create-snapshots.md "ebs-create-snapshots.md")

## Snapshot encryption

A snapshot automatically gets the same encryption status as the volume from which it is created.
Snapshots created from unencrypted volumes are not encrypted. Snapshots created from encrypted
volumes are automatically encrypted using the same KMS key as the volume.

###### Tip

If you need to create an encrypted snapshot from an unencrypted volume, first create the
unencrypted snapshot of the volume, and then create an encrypted copy of that snapshot.

## Snapshot destinations

The location of the source resource (volume or instance) determines where you can create
snapshots.

- If the source resource is in a Region, you must create snapshots in the same Region as
  the source resource.
- If the source resource is in a Local Zone, you can create snapshots in the same Local
  Zone or in its parent Region. For more information, see [Local snapshots in Local Zones](snapshots-localzones.md "snapshots-localzones.md").
- If the source resource is on an Outpost, you can create snapshots on the same Outpost
  or in its parent Region. For more information, see [Amazon EBS local snapshots on Outposts](snapshots-outposts.md "snapshots-outposts.md").

## Automating snapshots

You can automate snapshot creation using [Amazon Data Lifecycle Manager](snapshot-lifecycle.md "snapshot-lifecycle.md") and
[AWS Backup](../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md "../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md").

## Considerations for creating snapshots

- We recommend that you do not create snapshots of volumes that are attached to Amazon EC2 instances that
  are hibernated or that are enabled for hibernation. For more information, see [How Amazon EC2
  instance hibernation works](../../../AWSEC2/latest/UserGuide/instance-hibernate-overview.md#instance-hibernate-limitations "../../../AWSEC2/latest/UserGuide/instance-hibernate-overview.md#instance-hibernate-limitations").
- Although you can take a snapshot of a volume while a previous snapshot of that volume is
  in the `pending` status, having multiple snapshots in the `pending` state
  for the same volume can result in reduced volume performance until the snapshots complete.
- There are limits on the number of snapshots you can have in the `pending` state, and
  on the number of concurrent snapshots you can request per volume type. For more information, see
  [Quotas for Amazon EBS](ebs-resource-quotas.md "ebs-resource-quotas.md").
  If you exceed one of these quotas, wait for the current snapshots to complete and then try again.
