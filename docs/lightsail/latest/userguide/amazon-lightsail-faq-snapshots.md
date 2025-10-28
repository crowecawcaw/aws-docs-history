# Manual and automatic snapshots

## What are snapshots?

Snapshots are point-in-time backups of instances, databases, or block storage disks. You
can create a snapshot of your resources at any time, or you can enable automatic snapshots
on instances and disks to have Lightsail create snapshots for you. You can use snapshots
as baselines to create new resources or to back up your data. A snapshot contains all of the
data that is needed to restore your resource (from the moment when the snapshot was taken).
When you restore a resource by creating it from a snapshot, the new resource begins as an
exact replica of the original resource that was used to create the snapshot.

You can manually take snapshots of your Lightsail instances, disks, and databases, or
you can use [automatic
snapshots](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md") to instruct Lightsail to take daily snapshots of your instances and
disks automatically. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

## What are automatic snapshots?

Automatic snapshots are a way to schedule daily snapshots of your Linux/Unix instances
in Amazon Lightsail. You can pick a time of the day, and Lightsail will automatically take
a snapshot for you each day at the time you chose and always keep your seven most recent
automatic snapshots. Enabling snapshots is free, you only pay for the actual storage used by
your snapshots.

## What are the differences

between manual and automatic snapshots?

Automatic snapshots cannot be tagged or exported directly to Amazon EC2. However, automatic
snapshots can be copied and converted into manual snapshots. To copy an automatic snapshot
into a manual one, choose **Keep** from the automatic snapshot’s context
menu to copy it as a manual snapshot.

## What resources support snapshots?

Manual snapshots can be created for instances, databases, and disks.

Automatic snapshots can be enabled for Linux or Unix instances using the Lightsail
console, Lightsail API, or AWS CLI, and for disks using only the Lightsail API, or AWS CLI.
Automatic snapshots are not currently supported for Windows instances, or managed
databases.

## How long can I store snapshots?

Manual snapshots are stored until you choose to delete them. For more information, see
[Deleting snapshots in
Amazon Lightsail](amazon-lightsail-deleting-snapshots.md "amazon-lightsail-deleting-snapshots.md").

Automatic snapshots are stored until they are replaced by a newer automatic snapshots.
Lightsail stores the latest seven automatic snapshots before deleting the oldest one and
replacing it with the newest one. However, you can keep a specific automatic snapshot by
copying it as a manual snapshot. For more information, see [Keeping automatic snapshots of
instances or disks in Amazon Lightsail](amazon-lightsail-keeping-automatic-snapshots.md "amazon-lightsail-keeping-automatic-snapshots.md"). You will be billed the [snapshot storage fee](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/") for the
automatic snapshots stored in your account.

## How are automatic snapshots

enabled?

Automatic snapshots can be enabled using the Lightsail console, Lightsail API, or
AWS CLI when you create a Linux or Unix instance, or later after the instance is
running.

Automatic snapshots can also be enabled for disks when you create them or after they're
created; however, it can only be done using the Lightsail API, or AWS CLI.

For more information, see [Enabling or disabling automatic
snapshots for instances or disks in Amazon Lightsail](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md").

## When are automatic snapshots

created?

When you enable automatic snapshots, a default time is set based on the AWS Region
where the resource is located. You can change the automatic snapshot to your preferred time
of day, in hourly increments. For more information, see [Changing the automatic
snapshot time for instances or disks in Amazon Lightsail](amazon-lightsail-changing-automatic-snapshot-time.md "amazon-lightsail-changing-automatic-snapshot-time.md").

## How many snapshots can I store?

You can store as many manual snapshots as you’d like. However, only the latest seven
automatic snapshots are stored before the oldest one is replaced with the newest one.

## How are snapshots billed?

You only pay for the snapshots stored on your Lightsail account. Lightsail snapshots
(manual and automatic) cost $0.05 USD/GB-month to store.

## Will I lose my snapshots if I disable

automatic snapshots?

No. If you disable automatic snapshots, Lightsail will stop creating a daily snapshot,
and your existing automatic snapshots will be kept. When you re-enable automatic snapshots,
Lightsail will resume taking daily snapshots, deleting the oldest one and replacing it
with the newest one.

## What should I do if I don’t want an

automatic snapshot to be replaced?

You can keep a specific automatic snapshot by copying it as a manual snapshot. For more
information, see [Keeping
automatic snapshots of instances or disks in Amazon Lightsail](amazon-lightsail-keeping-automatic-snapshots.md "amazon-lightsail-keeping-automatic-snapshots.md").

## Can I delete an automatic

snapshot?

You can delete an automatic snapshot at any time by choosing **Delete**
from the automatic snapshot’s context menu. For more information, see [Delete automatic instance
snapshots](amazon-lightsail-deleting-automatic-snapshots.md "amazon-lightsail-deleting-automatic-snapshots.md").

## How can I use snapshots?

Snapshots can be used as a baseline or to create new resources if something goes wrong
with the original resource. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

Snapshots can also be exported to Amazon EC2 to create new resources within that service. For
more information, see [Export snapshots
to Amazon EC2](amazon-lightsail-exporting-snapshots.md "amazon-lightsail-exporting-snapshots.md").
