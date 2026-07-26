# Amazon EBS snapshots

You can back up the data on your Amazon EBS volumes by making point-in-time copies, known as
_Amazon EBS snapshots_. A snapshot is an **incremental backup**,
which means that we save only the blocks on the volume that have changed since the most
recent snapshot. This minimizes the time required to create the snapshot and saves on
storage costs by not duplicating data.

###### Important

AWS does not automatically back up the data stored on your EBS volumes. For data resiliency
and disaster recovery, it is your responsibility to create EBS snapshots on a regular basis,
or to set up automatic snapshot creation by using [Automate backups with Amazon Data Lifecycle Manager](snapshot-lifecycle.md "snapshot-lifecycle.md") or [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md").

Snapshots are stored in Amazon S3, in S3 buckets that you can't access directly. You can create
and manage your snapshots using the Amazon EC2 console or the Amazon EC2 API. You can't access your snapshots
using the Amazon S3 console or the Amazon S3 API.

Snapshot data is automatically replicated across all Availability Zones in the Region. This
provides high availability and durability for snapshot data, and enables you to restore volumes
in any Availability Zones in that Region.

Each snapshot contains all of the information that is needed to restore your data (from
the moment when the snapshot was taken) to a new EBS volume. When you create an EBS volume
from a snapshot, the new volume begins as an exact replica of the volume that was used to
create the snapshot.

For more information, see the [Amazon EBS Snapshots](https://aws.amazon.com/ebs/snapshots/ "https://aws.amazon.com/ebs/snapshots/")
product page.

###### Snapshot events

You can track the status of your EBS snapshots through CloudWatch Events. For more information, see
[EBS snapshot events](ebs-cloud-watch-events.md#snapshot-events "ebs-cloud-watch-events.md#snapshot-events").

###### Snapshot pricing

Charges for your snapshots are based on the amount of data stored. Because snapshots are
incremental, deleting a snapshot might not reduce your data storage costs. Data referenced
exclusively by a snapshot is removed when that snapshot is deleted, but data referenced by
other snapshots is preserved. For more information, see [Amazon Elastic Block Store Volumes and Snapshots](../../../awsaccountbilling/latest/aboutv2/checklistforunwantedcharges.md#checkebsvolumes "../../../awsaccountbilling/latest/aboutv2/checklistforunwantedcharges.md#checkebsvolumes") in the _AWS Billing User Guide_.

###### Contents

- [How Amazon EBS snapshots work](how_snapshots_work.md "how_snapshots_work.md")
- [Amazon EBS snapshot lifecycle](ebs-snapshot-lifecycle.md "ebs-snapshot-lifecycle.md")
- [Amazon EBS fast snapshot restore](ebs-fast-snapshot-restore.md "ebs-fast-snapshot-restore.md")
- [Amazon EBS snapshot lock](ebs-snapshot-lock.md "ebs-snapshot-lock.md")
- [Block public access for Amazon EBS snapshots](block-public-access-snapshots.md "block-public-access-snapshots.md")
- [Amazon EBS local snapshots on Outposts](snapshots-outposts.md "snapshots-outposts.md")
- [Local snapshots in Local Zones](snapshots-localzones.md "snapshots-localzones.md")
