# Comparing automatic and manual snapshots

The following are key features of Amazon DocumentDB (with MongoDB compatibility) automatic and manual
snapshots.

###### Amazon DocumentDB automatic snapshots have the following key features:

- **Automatic snapshot naming**
  — Automatic snapshot names follow the pattern
  `rds:<cluster-name>-yyyy-mm-dd-hh-mm`, with
  `yyyy-mm-dd-hh-mm` representing the date and time the
  snapshot was created.
- **Created automatically on a schedule**
  — When you create or modify a cluster, you can set the
  _backup retention period_ to an integer value
  from 1 to 35 days. By default, new clusters have a backup
  retention period of 1 day. The backup retention period defines
  the number of days that automatic snapshots are kept before being
  automatically deleted. You can't disable automatic backups on
  Amazon DocumentDB clusters.

In addition to setting the backup retention period, you also
set the _backup window_, the time of day
during which automatic snapshots are created.

- **Deleting automatic snapshots**
  — Automatic snapshots are deleted when you delete the
  automatic snapshot's cluster. You can't manually delete an
  automatic snapshot.
- **Incremental** — During
  the backup retention period, database updates are recorded so
  that there is an incremental record of changes.
- **Restoring from an automatic snapshot**
  — You can restore from an automatic snapshot using the
  AWS Management Console or the AWS CLI. When you restore from a snapshot using
  the AWS CLI, you must add instances separately after the cluster is
  _available_.
- **Sharing** — You can't
  share an Amazon DocumentDB automated cluster snapshot. As a workaround, you
  can create a manual snapshot by copying the automated snapshot,
  and then share that copy. For more information about copying a
  snapshot, see [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md").
  For more information about restoring a cluster from a snapshot,
  see [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md "backup_restore-restore_from_snapshot.md").
- **You can restore from any point within
  the backup retention period** — Because database
  updates are incrementally recorded, you can restore your cluster
  to any point in time within the backup retention period.

When you restore from an automatic snapshot or from a
point-in-time restore using the AWS CLI, you must add instances
separately after the cluster is _available_.

###### Amazon DocumentDB manual snapshots have the following key features:

- **Created on demand** —
  Amazon DocumentDB manual snapshots are created on demand using the Amazon DocumentDB
  Management Console or AWS CLI.
- **Deleting a manual snapshot**
  —A manual snapshot is deleted only when you explicitly
  delete it using either the Amazon DocumentDB console or AWS CLI. A manual
  snapshot is not deleted when you delete its cluster.
- **Full backups** — When a
  manual snapshot is taken, a full backup of your cluster's data is
  created and stored.
- **Manual snapshot naming**
  — You specify the manual snapshot name. Amazon DocumentDB does not
  add a `datetime` stamp to the name, so you must add
  that information if you want it included in the name.
- **Restoring from a manual snapshot**
  —You can restore from a manual snapshot using the console
  or the AWS CLI. When you restore from a snapshot using the AWS CLI,
  you must add instances separately after the cluster is
  _available_.
- **Service Quotas** — You
  are limited to a maximum of 100 manual snapshots per AWS Region.
- **Sharing** — You can
  share manual cluster snapshots, which can be copied by
  authorized AWS accounts. You can share encrypted or unencrypted
  manual snapshots. For more information about copying a snapshot,
  see [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md").
- **You restore to when the manual snapshot
  was taken** —When you restore from a manual
  snapshot, you restore to when the manual snapshot was taken.

When you restore from a snapshot using the AWS CLI, you must add
instances separately after the cluster is
_available_.
