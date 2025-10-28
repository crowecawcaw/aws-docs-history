# Snapshots in

Amazon Lightsail

You can create point-in-time snapshots of instances, databases, and block storage disks in
Amazon Lightsail, and use them as baselines to create new resources or for data backup. A
snapshot contains all of the data that is needed to restore your resource (from the moment when
the snapshot was taken). When you restore a resource by creating it from a snapshot, the new
resource begins as an exact replica of the original resource that was used to create the
snapshot. You will be billed a [snapshot
storage fee](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/") for snapshots on your Lightsail account; whether they are manual
snapshots, automatic snapshots, copied snapshots, or system disk snapshots. If you experience
data corruption or a disk failure, you can create a disk from a snapshot that you have taken and
replace the old disk. You can also use snapshots to provision new disks and attach them during a
new instance launch.

_Contents_

- [Manual snapshots](#manual-snapshots "#manual-snapshots")
- [Automatic snapshots](#automatic-snapshots "#automatic-snapshots")
- [System disk snapshots](#system-disk-snapshots "#system-disk-snapshots")
- [Create new resources from
  snapshots](#rehydrating-snapshots "#rehydrating-snapshots")
- [Copy snapshots](#copying-snapshots "#copying-snapshots")
- [Export snapshots to
  Amazon EC2](#exporting-snapshots "#exporting-snapshots")
- [Delete snapshots](#deleting-snapshots "#deleting-snapshots")

## Manual snapshots

Create manual snapshots of instances, managed databases, and block storage disks at any
time. Manual snapshots are stored indefinitely until you delete them.

For more information about creating manual snapshots, see the following guides:

- [Create a snapshot
  of your Linux or Unix instance](lightsail-how-to-create-a-snapshot-of-your-instance.md "lightsail-how-to-create-a-snapshot-of-your-instance.md")
- [Create a snapshot
  of your Windows Server instance](prepare-windows-based-instance-and-create-snapshot.md "prepare-windows-based-instance-and-create-snapshot.md")
- [Create a snapshot of
  your database](amazon-lightsail-creating-a-database-snapshot.md "amazon-lightsail-creating-a-database-snapshot.md")
- [Create a block storage disk
  snapshot](create-block-storage-disk-snapshot.md "create-block-storage-disk-snapshot.md")

## Automatic snapshots

If you're hosting critical information on your Lightsail instance or block storage disk,
you should back them up often by creating manual snapshots. However, it's not always easy to
find the time to perform frequent administrative tasks. If that's the case for you, then use
automatic snapshots to have Lightsail create daily backups of your instance or block storage
disk on your behalf, without manual interaction. The latest seven daily automatic snapshots
are stored before the oldest one is replaced with the newest one.

For more information about automatic snapshots, see the following guides:

- [Enable or disable
  automatic instance snapshots](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md")
- [Change the automatic
  snapshot time for instances or disks](amazon-lightsail-changing-automatic-snapshot-time.md "amazon-lightsail-changing-automatic-snapshot-time.md")
- [Delete automatic
  snapshots](amazon-lightsail-deleting-automatic-snapshots.md "amazon-lightsail-deleting-automatic-snapshots.md")

###### Important

All automatic snapshots associated with a resource are deleted when you delete the
source resource. This behavior differs from manual snapshots, which are kept in your
Lightsail account even after you delete the source resource. To keep your automatic
snapshots when you delete the source resource, see [Keep automatic
snapshots](amazon-lightsail-keeping-automatic-snapshots.md "amazon-lightsail-keeping-automatic-snapshots.md").

## System disk snapshots

If your instance becomes unresponsive and you need to access the files on the system disk,
you can back up the instance root volume by creating a snapshot of it. Then, you can access
the files in the system disk by creating a new block storage disk from the snapshot and
attaching it to another instance. For more information, see [Create a snapshot of an
instance root volume](amazon-lightsail-create-an-instance-root-volume-snapshot.md "amazon-lightsail-create-an-instance-root-volume-snapshot.md").

## Create new resources from snapshots

Use snapshots to create new Lightsail resources using the same plan, or larger plan,
than the original resource. Snapshots can't be used to create new resources using a smaller
Lightsail plan. When you create a resource based on a snapshot, the new resource begins as a
replica of the original resource that was used to create the snapshot.

For more information, see the following guides:

- [Create an instance from
  a snapshot](lightsail-how-to-create-instance-from-snapshot.md "lightsail-how-to-create-instance-from-snapshot.md")
- [Create a database
  from a snapshot](amazon-lightsail-creating-a-database-from-snapshot.md "amazon-lightsail-creating-a-database-from-snapshot.md")
- [Create a block storage
  disk from a snapshot](create-new-block-storage-disk-from-snapshot.md "create-new-block-storage-disk-from-snapshot.md")
- [Create a
  larger instance, block storage disk, or database from a snapshot](how-to-create-larger-instance-from-snapshot-using-console.md "how-to-create-larger-instance-from-snapshot-using-console.md")

## Copy snapshots

Instance and block storage disk snapshots can be copied from one Amazon Web Services (AWS) Region
to another within the same Lightsail account. Database snapshots cannot be copied between
regions. For more information, see [Copy snapshots from
one AWS Region to another](amazon-lightsail-copying-snapshots-from-one-region-to-another.md "amazon-lightsail-copying-snapshots-from-one-region-to-another.md").

## Export snapshots to Amazon EC2

Lightsail is the easiest way to get started with AWS. However, there are limitations
with Lightsail that are not present in Amazon EC2 or other AWS services. Export your
Lightsail instance and block storage disk snapshots to Amazon EC2 to take advantage of the wider
range of instance types available, and use the full range of services in AWS. For more
information, see [Export snapshots to
Amazon EC2](amazon-lightsail-exporting-snapshots.md "amazon-lightsail-exporting-snapshots.md").

###### Note

Snapshots of cPanel & WHM (CentOS 7) instances cannot be exported to Amazon EC2.

## Delete snapshots

Delete Lightsail snapshots when you no longer need them to avoid incurring a monthly
[snapshot storage fee](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/"). For
more information, see [Delete
snapshots](amazon-lightsail-deleting-snapshots.md "amazon-lightsail-deleting-snapshots.md").
