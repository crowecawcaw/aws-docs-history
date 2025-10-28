# Considerations and limitations for archiving Amazon EBS snapshots

Keep the following in mind when archiving Amazon EBS snapshots.

###### Considerations

- The minimum archive period is 90 days. If you delete or permanently restore an archived snapshot
  before the minimum archive period of 90 days, you are billed for remaining days in the archive tier,
  rounded to the nearest hour. For more information, see [Pricing and billing for archiving Amazon EBS snapshots](snapshot-archive-pricing.md "snapshot-archive-pricing.md").
- It can take up to 72 hours to restore an archived snapshot from the archive tier to the standard
  tier, depending on the size of the snapshot.
- Archived snapshots are always full snapshots. A full snapshot contains all the blocks written to the
  volume at the time the snapshot was created. The full snapshot will likely be larger than the incremental
  snapshot from which it was created. However, if you have only one snapshot of a volume on the standard
  tier, the size of the full snapshot in the archive tier will be the same size as the snapshot in standard
  tier. This is because the first snapshot taken of a volume is always a full snapshot. To get the full
  snapshot size, use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") AWS CLI command.
- Archiving is recommended for monthly, quarterly, or yearly snapshots. Archiving daily incremental
  snapshots of a single volume can lead to higher costs when compared to keeping them in the standard tier.
- When a snapshot is archived, the data of the snapshot that is referenced by other snapshots in the
  snapshot lineage are retained in the standard tier. Data and storage costs associated with the referenced
  data that is retained on the standard tier are allocated to the next snapshot in the lineage. This ensures
  that subsequent snapshots in the lineage are not affected by the archival.
- If you delete an archived snapshot that matches a Recycle Bin retention rule, the archived snapshot is
  retained in the Recycle Bin for the retention period defined in the retention rule. To use the snapshot, you
  must first recover it from the Recycle Bin and then restore it from the archive tier. For more information,
  see [Recycle Bin](recycle-bin.md "recycle-bin.md") and [Pricing and billing for archiving Amazon EBS snapshots](snapshot-archive-pricing.md "snapshot-archive-pricing.md").
- You can't use an archived snapshot in a block device mapping or to create an Amazon EBS volume.
- You can archive snapshots created by AWS Backup using the AWS Backup console, APIs, or command line tools. For more
  information, see [Creating a backup plan](../../../aws-backup/latest/devguide/creating-a-backup-plan.md "../../../aws-backup/latest/devguide/creating-a-backup-plan.md") in the _AWS Backup Developer Guide_.

###### Limitations

- You can archive snapshots that are in the `completed` state only.
- You can archive only snapshots that you own in your account. To archive a snapshot that is shared with
  you, first copy the snapshot to your account and then archive the snapshot copy.
- Before you can use an archived snapshot, you must first restore it to the standard
  tier. Restoring to the standard tier is required to create a volume from the snapshot
  through the `CreateVolume` and `RunInstances` API operations as well
  as to share or copy a snapshot. For more information, see [Restore an archived Amazon EBS snapshot](restore-archived-snapshot.md "restore-archived-snapshot.md").
- You can archive a snapshot that is associated with one or more AMIs only if all of the associated
  AMIs are disabled. For more information, see [Disable an AMI](../../../AWSEC2/latest/UserGuide/disable-an-ami.md "../../../AWSEC2/latest/UserGuide/disable-an-ami.md").
- You can't enable a disabled AMI if the associated snapshots are temporarily restored. All of the
  associated snapshots must be permanently restored before you can enable the AMI.
- You can't cancel the snapshot archive or snapshot restore process after it has been started.
- You can't share archived snapshots. If you archive a snapshot that you have shared with other accounts,
  the accounts with which the snapshot is shared lose access after the snapshot is archived.
- You can't copy an archived snapshot. If you need to copy an archived snapshot, you must first restore
  it.
- You can't enable fast snapshot restore for an archived snapshot. Fast snapshot restore is automatically
  disabled when a snapshot is archived. If you need to use fast snapshot restore, you must manually enable it
  after restoring the snapshot.
