# Amazon EBS fast snapshot restore

Amazon EBS fast snapshot restore (FSR) enables you to create a volume from a snapshot that
is fully initialized at creation. This eliminates the latency of I/O operations on
a block when it is accessed for the first time. Volumes that are created using fast
snapshot restore instantly deliver all of their provisioned performance.

To get started, enable fast snapshot restore for specific snapshots in specific
Availability Zones. Each snapshot and Availability Zone pair refers to one fast
snapshot restore. When you create a volume from one of these snapshots in one of
its enabled Availability Zones, the volume is restored using fast snapshot restore.

You must explicitly enable fast snapshot restore for each snapshot. For example,
if you create a new snapshot from a volume that was restored from a fast snapshot
restore-enabled snapshot, the new snapshot is not automatically enabled for fast
snapshot restore. If you copy a snapshot that is enabled for fast snapshot restore,
the snapshot copy is not automatically enabled for fast snapshot restore.

The number of volumes that you can restore with the full performance benefit
of fast snapshot restore is determined by volume creation credits for the snapshot.
For more information see [Amazon EBS fast snapshot restore volume creation credits](volume-creation-credits.md "volume-creation-credits.md").

You can enable fast snapshot restore for snapshots that you own and for public
and private snapshots that are shared with you.

###### Contents

- [Considerations](#fsr-considerations "#fsr-considerations")
- [Pricing and Billing](#fsr-pricing "#fsr-pricing")
- [Amazon EBS fast snapshot restore volume creation credits](volume-creation-credits.md "volume-creation-credits.md")
- [Configure fast snapshot restore for an Amazon EBS snapshot](manage-fsr-enable.md "manage-fsr-enable.md")
- [Check the fast snapshot restore state for an Amazon EBS snapshot](view-fsr-enabled-snapshots.md "view-fsr-enabled-snapshots.md")
- [View Amazon EBS volumes restored using fast snapshot restore](view-fast-restored-volumes.md "view-fast-restored-volumes.md")

## Considerations

- Fast snapshot restore is not supported with AWS Outposts, Local Zones, and Wavelength Zones.
- Fast snapshot restore can be enabled on snapshots with a size of 16 TiB or
  less.
- Volumes provisioned with performance up to 64,000 IOPS and 1,000 MiB/s
  throughput receive the full performance benefit of fast snapshot restore. For
  volumes provisioned with performance greater than 64,000 IOPS or 1,000 MiB/s
  throughput, we recommend that you [initialize
  the volume](initalize-volume.md#ebs-initialize "initalize-volume.md#ebs-initialize") to receive its full performance.
- You can enable up to 5 snapshots for fast snapshot restore per Region. The
  quota applies to snapshots that you own and snapshots that are shared with you.
  If you enable fast snapshot restore for a snapshot that is shared with you, it counts
  towards your fast snapshot restore quota. It does not count towards the snapshot
  owner's fast snapshot restore quota.
- Amazon EBS emits Amazon CloudWatch events when the fast snapshot restore state for a snapshot
  changes. For more information, see [EBS fast snapshot restore events](ebs-cloud-watch-events.md#fast-snapshot-restore-events "ebs-cloud-watch-events.md#fast-snapshot-restore-events").

## Pricing and Billing

You are billed for each minute that fast snapshot restore is enabled for a snapshot in a particular
Availability Zone. Charges are pro-rated with a minimum of one hour.

For example, if you enable fast snapshot restore for one snapshot in `US-East-1a`
for one month (30 days), you are billed **$540**
(`1` snapshot x `1` AZ x `720` hours x
`$0.75` per hour). If you enable fast snapshot restore for two snapshots
in `us-east-1a`, `us-east-1b`, and `us-east-1c` for the
same period, you are billed **$3240** (`2`
snapshots x `3` AZs x `720` hours x `$0.75` per
hour).

If you enable fast snapshot restore for a public or private snapshot that is shared
with you, your account is billed; the snapshot owner is not billed. When a snapshot
that is shared with you is deleted or unshared by the snapshot owner, fast snapshot
restore is disabled for the snapshot in your account and billing is stopped.

For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").
