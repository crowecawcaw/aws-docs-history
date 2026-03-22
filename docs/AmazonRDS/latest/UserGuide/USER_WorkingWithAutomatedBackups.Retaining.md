# Retaining automated backups

###### Note

You can only retain automated backups of DB instances, not Multi-AZ DB
clusters.

When you delete a DB instance, you can choose to retain automated backups. Automated backups can be retained
for a number of days equal to the backup retention period configured for the DB instance at the time when you delete it.

Retained automated backups contain system snapshots and transaction logs from a DB instance.
They also include your DB instance properties like allocated storage and DB instance
class, which are required to restore it to an active instance.

Retained automated backups and manual snapshots incur billing charges until they're deleted. For more information, see
[Retention costs](#USER_WorkingWithAutomatedBackups.RetentionCosts "#USER_WorkingWithAutomatedBackups.RetentionCosts").

You can retain automated backups for RDS instances running the
Db2, MariaDB, MySQL,
PostgreSQL, Oracle, and Microsoft SQL Server engines.

You can restore or remove retained automated backups using the AWS Management Console, RDS API, and AWS CLI.

###### Topics

- [Retention period](#USER_WorkingWithAutomatedBackups.RetentionPeriods "#USER_WorkingWithAutomatedBackups.RetentionPeriods")
- [Viewing retained backups](#USER_WorkingWithAutomatedBackups.viewing-retained "#USER_WorkingWithAutomatedBackups.viewing-retained")
- [Restoration](#USER_WorkingWithAutomatedBackups.Restoration "#USER_WorkingWithAutomatedBackups.Restoration")
- [Retention costs](#USER_WorkingWithAutomatedBackups.RetentionCosts "#USER_WorkingWithAutomatedBackups.RetentionCosts")
- [Limitations](#USER_WorkingWithAutomatedBackups.Limits "#USER_WorkingWithAutomatedBackups.Limits")

## Retention period

The system snapshots and transaction logs in a retained automated backup expire the same way that they expire for the
source DB instance. Because there are no new snapshots or logs created for this instance, the retained automated backups
eventually expire completely. Effectively, they live as long their last system snapshot would have done, based on the
settings for retention period the source instance had when you deleted it. Retained automated backups are removed by the
system after their last system snapshot expires.

You can remove a retained automated backup in the same way that you can delete a DB instance. You can remove retained
automated backups using the console or the RDS API operation `DeleteDBInstanceAutomatedBackup`.

Final snapshots are independent of retained automated backups. We strongly suggest
that you take a final snapshot even if you retain automated backups because the
retained automated backups eventually expire. The final snapshot doesn't
expire.

## Viewing retained backups

To view your retained automated backups, choose **Automated backups** in the navigation pane, then choose
**Retained**. To view individual snapshots associated with a retained automated backup, choose
**Snapshots** in the navigation pane. Alternatively, you can describe individual snapshots associated
with a retained automated backup. From there, you can restore a DB instance directly from one of those snapshots.

To describe your retained automated backups using the AWS CLI, use the following command:

```
aws rds describe-db-instance-automated-backups --dbi-resource-id `DbiResourceId`
```

To describe your retained automated backups using the RDS API, call the [`DescribeDBInstanceAutomatedBackups`](../APIReference/API_DescribeDBInstanceAutomatedBackups.md "../APIReference/API_DescribeDBInstanceAutomatedBackups.md")
action with the `DbiResourceId` parameter.

## Restoration

For information on restoring DB instances from automated backups, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

## Retention costs

The cost of a retained automated backup is the cost of total storage of the system snapshots that are associated with it.
There is no additional charge for transaction logs or instance metadata. All other pricing rules for backups apply to
restorable instances.

For example, suppose that your total allocated storage of running instances is 100 GB. Suppose also that you have 50 GB of
manual snapshots plus 75 GB of system snapshots associated with a retained automated backup. In this case, you are charged
only for the additional 25 GB of backup storage, like this: (50 GB + 75 GB) – 100 GB = 25 GB.

## Limitations

The following limitations apply to retained automated backups:

- The maximum number of retained automated backups in one AWS Region is 40. It's not included in the DB
  instances quota. You can have 40 running DB instances and an additional 40 retained automated backups at the same
  time.
- Retained automated backups don't contain information about parameters or option groups.
- You can restore a deleted instance to a point in time that is within the retention period at the time of deletion.
- You can't modify a retained automated backup. That's because it consists of system backups, transaction logs,
  and the DB instance properties that existed at the time that you deleted the source instance.
