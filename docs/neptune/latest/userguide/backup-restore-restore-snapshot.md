# Restoring from a DB Cluster Snapshot

When you create an Amazon Neptune snapshot of a DB cluster, Neptune creates a storage
volume snapshot of the cluster, backing up all its data and not just individual instances.
You can later create a new DB cluster by restoring from this DB cluster snapshot. When you
restore the DB cluster, you provide the name of the DB cluster snapshot to restore from,
and then provide a name for the new DB cluster that is created by the restore.

###### Contents

- [Things to keep in mind
  about restoring a Neptune DB cluster from a snapshot](backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-considerations "backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-considerations")
  - [You cannot restore
    to an existing DB cluster](backup-restore-restore-snapshot.md#backup-restore-restores-to-new-cluster "backup-restore-restore-snapshot.md#backup-restore-restores-to-new-cluster")
  - [No instances are restored](backup-restore-restore-snapshot.md#backup-restore-restore-no-restored-instances "backup-restore-restore-snapshot.md#backup-restore-restore-no-restored-instances")
  - [No custom parameter group is restored](backup-restore-restore-snapshot.md#backup-restore-restore-default-parameters "backup-restore-restore-snapshot.md#backup-restore-restore-default-parameters")
  - [No custom security
    groups are restored](backup-restore-restore-snapshot.md#backup-restore-restore-default-security-group "backup-restore-restore-snapshot.md#backup-restore-restore-default-security-group")
  - [You can't restore from
    a shared encrypted snapshot](backup-restore-restore-snapshot.md#backup-restore-restore-not-shared-and-encrypted "backup-restore-restore-snapshot.md#backup-restore-restore-not-shared-and-encrypted")
  - [A restored DB cluster
    uses as much storage as before](backup-restore-restore-snapshot.md#backup-restore-restore-same-storage-allocation "backup-restore-restore-snapshot.md#backup-restore-restore-same-storage-allocation")

- [How to restore from a snapshot](backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring "backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring")
  - [Using the Console to
    Restore from a Snapshot](backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring-console "backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring-console")

## Things to keep in mind

about restoring a Neptune DB cluster from a snapshot

### You cannot restore

to an existing DB cluster

The restore process always creates a new DB cluster, so you can't restore to a
DB cluster that already exists.

### No instances are restored

A new DB cluster created by a restore has no instances associated with it.

As soon as the restore is complete and your new DB cluster is available,
explicitly create the instances that you will need. You can do this on the Neptune
console, or using the [CreateDBInstance](api-instances.md#CreateDBInstance "api-instances.md#CreateDBInstance")
API.

### No custom parameter group is restored

A new DB cluster created by a restore automatically has the default DB parameter group
associated with it.

As soon as the restore is complete and your new DB cluster is available,
associate any custom DB parameter group that the instance you restored from was using.
To do that, use the **Modify** command on the Neptune console,
or the [ModifyDBInstance](api-instances.md#ModifyDBInstance "api-instances.md#ModifyDBInstance")
API.

###### Important

We recommend that you save a custom parameter group being used in
a DB cluster that you are creating a snapshot of. Then, when you restore from that
snapshot, you can easily associate the correct parameter group with the restored
DB cluster.

### No custom security

groups are restored

A new DB cluster created by a restore automatically has the default security group
associated with it.

As soon as the restore is complete and your new DB cluster is available,
associate any custom security groups that the instance you restored from was using.
To do that, use the **Modify** command on the Neptune console,
or the [ModifyDBInstance](api-instances.md#ModifyDBInstance "api-instances.md#ModifyDBInstance")
API.

### You can't restore from

a shared encrypted snapshot

You cannot restore a DB cluster from a DB cluster snapshot that is both
shared and encrypted.

Instead, make an unshared copy of the snapshot and restore from the copy.

### A restored DB cluster

uses as much storage as before

When you restore a DB cluster from a DB cluster snapshot, the amount of storage
allocated to the new cluster is the same as was allocated to the DB cluster from which the
snapshot was made, regardless of how much of that allocated storage is actually being used.

In other words, the "high water mark" for which you are billed does not
change. Resetting the high water mark requires exporting the data from your graph and then
reloading it onto a new DB cluster (see [Neptune storage billing](feature-overview-storage.md#feature-overview-storage-billing "feature-overview-storage.md#feature-overview-storage-billing")).

## How to restore from a snapshot

You can restore a DB cluster from a DB cluster snapshot using the AWS Management Console,
the AWS CLI, or the Neptune API.

### Using the Console to

Restore from a Snapshot

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB cluster snapshot that you want to restore from.
4. Choose **Actions**, **Restore Snapshot**.
5. On the **Restore DB Instance** page, in the **DB Instance
   Identifier** box, enter the name for your restored DB cluster.
6. Choose **Restore DB Instance**.
7. If you want to restore the functionality of the DB cluster to that of the DB cluster
   that the snapshot was created from, you must modify the DB cluster to use the security
   group. The next steps assume that your DB cluster is in a virtual private cloud (VPC).
   If your DB cluster is not in a VPC, use the Amazon EC2 console to locate the security group
   that you need for the DB cluster.
   1. Open the Amazon VPC console at
      [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
   2. In the navigation pane, choose **Security Groups**.
   3. Choose the security group that you want to use for your DB clusters. If necessary, add rules
      to link the security group to a security group for an EC2 instance.
