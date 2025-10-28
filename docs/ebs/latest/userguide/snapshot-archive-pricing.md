# Pricing and billing for archiving Amazon EBS snapshots

Archived snapshots are billed at a rate of $0.0125 per GB-month. For example, if you archive a 100
GiB snapshot, you are billed $1.25 (100 GiB \* $0.0125) per month.

Snapshot restores are billed at a rate of $0.03 per GB of data restored. For example, if
you restore a 100 GiB snapshot from the archive tier, you are billed one time for $3 (100 GiB \*
$0.03).

After the snapshot is restored to the standard tier, the snapshot is billed at the standard rate
for snapshots of $0.05 per GB-month.

For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

###### Billing for the minimum archive period

The minimum archive period is 90 days. If you delete or permanently restore an archived snapshot
before the minimum archive period of 90 days, you are billed a pro-rated charge equal to the archive
tier storage charge for the remaining days, rounded to the nearest hour. For example, if you delete
or permanently restore an archived snapshot after 40 days, you are billed for the remaining 50 days
of the minimum archive period.

###### Note

Temporarily restoring an archived snapshot before the minimum archive period of 90 days does not
incur this charge.

###### Temporary restores

When you temporarily restore a snapshot, the snapshot is restored from the archive tier to the
standard tier, and a copy of the snapshot remains in the archive tier. You are billed for both the
snapshot in the standard tier and the snapshot copy in the archive tier for the duration of the
temporary restore period. When the temporarily restored snapshot is removed from the standard tier,
you are no longer billed for it, and you are billed for the snapshot in the archive tier only.

###### Permanent restores

When you permanently restore a snapshot, the snapshot is restored from the archive tier to the
standard tier, and the snapshot is deleted from the archive tier. You are billed for the snapshot in
the standard tier only.

###### Deleting snapshots

If you delete a snapshot while it is being archived, you are billed for the snapshot data that has
already been moved to the archive tier. This data is subject to the minimum archive period of 90 days
and billed accordingly upon deletion. For example, if you archive a 100 GiB snapshot, and you delete
the snapshot after only 40 GiB has been archived, you are billed $1.50 for the minimum archive period
of 90 days for the 40 GiB that has already been archived ($0.0125 per GB-month \* 40 GB \* (90 days \* 24
hours) / (24 hours/day \* 30-day month).

If you delete a snapshot while it is being restored from the archive tier, you are billed for the
snapshot restore for the full size of the snapshot (snapshot size \* $0.03). For example, if you restore
a 100 GiB snapshot from the archive tier, and you delete the snapshot at any point before the snapshot
restore completes, you are billed $3 (100 GiB snapshot size \* $0.03).

###### Recycle Bin

Archived snapshots are billed at the rate for archived snapshots while they are in the Recycle
Bin. Archived snapshots that are in the Recycle Bin are subject to the minimum archive period of 90
days and they are billed accordingly if they are deleted by Recycle Bin before the minimum archive
period. In other words, if a retention rule deletes an archived snapshot from the Recycle Bin before
the minimum period of 90 days, you are billed for the remaining days.

If you delete a snapshot that matches a retention rule while the snapshot is being archived, the
archived snapshot is retained in the Recycle Bin for the retention period defined in the retention rule.
It is billed at the rate for archived snapshots.

If you delete a snapshot that matches a retention rule while the snapshot is being restored, the
restored snapshot is retained in the Recycle Bin for the remainder of the retention period, and billed
at the standard snapshot rate. To use the restored snapshot, you must first recover it from the Recycle
Bin.

For more information, see [Recycle Bin](recycle-bin.md "recycle-bin.md").

###### Cost tracking

Archived snapshots appear in the AWS Cost and Usage Report with their same resource ID and Amazon
Resource Name (ARN). For more information, see the [AWS Cost and Usage Report User Guide](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md").

You can use the following usage types to identify the associated costs:

- `SnapshotArchiveStorage` — fee for monthly data storage
- `SnapshotArchiveRetrieval` — one-time fee for snapshot restores
- `SnapshotArchiveEarlyDelete` — fee for deleting or permanently restoring
  a snapshot before the minimum archive period (90 days)
