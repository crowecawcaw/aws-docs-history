# Retaining automated backups

When you delete a provisioned or Aurora Serverless v2 DB cluster, you can retain automated backups. This allows you to restore a
DB cluster to a specific point in time within the backup retention period, even after the cluster is deleted.

_Retained automated backups_ contain system snapshots and
transaction logs from a DB cluster. They also include DB cluster properties, such as DB
instance class, which are required to restore it to an active cluster.

You can restore or remove retained automated backups using the AWS Management Console, RDS API, and AWS CLI.

###### Note

You can't retain automated backups for Aurora Serverless v1 DB clusters.

###### Topics

- [Retention period](#Aurora.Managing.Backups.Retaining.Period "#Aurora.Managing.Backups.Retaining.Period")
- [Retention costs](#Aurora.Managing.Backups.Retaining.Costs "#Aurora.Managing.Backups.Retaining.Costs")
- [Prevent automated backup deletion](#aurora-copy-snapshot.Retention "#aurora-copy-snapshot.Retention")
- [Limitations](#Aurora.Managing.Backups.Retaining.Limits "#Aurora.Managing.Backups.Retaining.Limits")
- [Viewing retained automated backups for Amazon Aurora](Aurora.Managing.Backups.Retaining.md "Aurora.Managing.Backups.Retaining.md")
- [Deleting retained automated backups for Amazon Aurora](Aurora.Managing.Backups.Retaining.md "Aurora.Managing.Backups.Retaining.md")

## Retention period

The system snapshots and transaction logs in a retained automated backup expire the same way that they expire for the
source DB cluster. The settings for the retention period of the source cluster also apply to the automated backups. Because
no new snapshots or logs are created for this cluster, the retained automated backups eventually expire completely. After
the retention period is over, you continue to retain manual DB cluster snapshots, but all of the automated backups
expire.

You can remove retained automated backups using the console, AWS CLI or RDS API. For more information, see [Deleting retained automated backups for Amazon Aurora](Aurora.Managing.Backups.Retaining.md "Aurora.Managing.Backups.Retaining.md").

Unlike a retained automated backup, a final snapshot doesn't expire. We strongly
suggest that you take a final snapshot even if you retain automated backups, because
the retained automated backups eventually expire.

## Retention costs

There is no additional charge for backup storage of up to 100% of your total Aurora database storage for each Aurora DB
cluster. There is also no additional charge up to one day when you retain automated backups after deleting a DB cluster.
Backups that you retain for more than one day are charged.

There is no additional charge for transaction logs or instance metadata. All other pricing rules for backups apply to
restorable clusters. For more information, see the [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing")
page.

## Prevent automated backup deletion

Amazon RDS deletes automated backups in several situations:

- At the end of their retention period.
- When you delete a DB cluster.

If you want to keep an automated backup for a longer period, copy it to create a manual snapshot, which is retained until you delete it.
Amazon RDS storage costs might apply to manual snapshots if they exceed your default storage space.

For more information about copying a DB cluster snapshot, see [DB cluster snapshot copying](aurora-copy-snapshot.md "aurora-copy-snapshot.md").

For more information about backup storage costs, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

## Limitations

The following limitations apply to retained automated backups:

- The maximum number of retained automated backups in one AWS Region is 40.
  It's not included in the quota for DB clusters. You can have up to 40
  running DB clusters, 40 running DB instances, and 40 retained automated backups
  for DB clusters at the same time.

For more information, see [Quotas in Amazon Aurora](CHAP_Limits.md#RDS_Limits.Limits "CHAP_Limits.md#RDS_Limits.Limits").

- Retained automated backups don't contain information about parameters or option groups.
- You can restore a deleted cluster to a point in time that is within the
  retention period at the time of deletion.
- You can't modify a retained automated backup because it consists of system
  backups, transaction logs, and the DB cluster properties that existed at the
  time that you deleted the source cluster.
- Cross-Region automated backup replication isn't supported for Aurora DB clusters. Aurora
  doesn't support automatically replicating snapshots and transaction logs to
  another AWS Region. For disaster recovery across Regions, you must manually
  copy Aurora snapshots to your desired destination Region.
