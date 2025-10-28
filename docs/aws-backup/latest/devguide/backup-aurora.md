# Amazon Aurora DSQL backups

You can use AWS Backup to create backups of your Amazon Aurora DSQL single-Region and
multi-Region clusters. Amazon Aurora DSQL cluster backups are always full backups.

Backup creation for Amazon Aurora DSQL clusters use the standard creation backup process.
For more information, see the following:

- [Creating an on-demand backup using AWS Backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md")
- [Create a backup plan](creating-a-backup-plan.md "creating-a-backup-plan.md")
  To use AWS Backup to create backups of your Amazon Aurora DSQL clusters, you must enable
  protection for Aurora DSQL. For more information, see [Service Opt-in](getting-started.md#service-opt-in "getting-started.md#service-opt-in").

When you backup a multi-Region cluster, consider the following items:

- A multi-Region cluster backup requires a separate backup for each Region within the
  cluster; a backup in one Region doesn't create a recovery point for all Regions in a
  multi-Region cluster.
- As a best practice, AWS Backup recommends you create a recovery point in one Region and
  copy it to another related Region. For [multi-Region restore](restore-auroradsql.md#restore-auroradsql-multiregion "restore-auroradsql.md#restore-auroradsql-multiregion"), you need a recovery point in one supported Region, and a
  copy of that recovery point in another Region within the same Regional triplet.

The following supported triplets are available. Where there are more than
Regions, choose three in the same grouping.

    + US East (N. Virginia); US East (Ohio); US West (N. California)
    + Europe (Ireland); Europe (London); Europe (Paris); Europe (Frankfurt)
    + Asia Pacific (Tokyo); Asia Pacific (Seoul); Asia Pacific (Osaka)

AWS Backup recommends that you add the backup copy rule to the backup plan. If you do not add
the copy rule to the backup plan, you must manually copy the backup to the required Region
in which to perform the restore, which will increase your Recovery Time Objective (RTO)
times.

For information about restoring an Aurora DSQL recovery point (backup), see [Amazon Aurora DSQL restore](restore-auroradsql.md "restore-auroradsql.md").
