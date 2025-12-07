# Enabling automated

backups

If your DB instance doesn't have automated backups enabled, you can enable them at
any time. You enable automated backups by setting the backup retention period to a
positive nonzero value. When automated backups are turned on, your DB instance is taken offline and a backup is immediately created.

###### Note

If you manage your backups in AWS Backup, you can't enable automated backups. For
more information, see [Using AWS Backup to manage automated backups for Amazon RDS](AutomatedBackups.md "AutomatedBackups.md").

###### To enable automated backups immediately

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose
   the DB instance or Multi-AZ DB cluster that you want to modify.
3. Choose **Modify**.
4. For **Backup retention period**, choose a positive nonzero
   value, for example three days.
5. Choose **Continue**.
6. Choose **Apply immediately**.
7. Choose **Modify DB instance** or **Modify
   cluster** to save your changes and enable automated
   backups.
   To enable automated backups, use the AWS CLI [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") or [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command.

Include the following parameters:

- `--db-instance-identifier` (or `--db-cluster-identifier`
  for a Multi-AZ DB cluster)
- `--backup-retention-period`
- `--apply-immediately` or `--no-apply-immediately`
  In the following example, we enable automated backups by setting the backup retention period to three days. The changes are applied
  immediately.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my_db_instance`  \
    --backup-retention-period `3` \
    `--apply-immediately`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my_db_instance`  ^
    --backup-retention-period `3` ^
    `--apply-immediately`
```

To enable automated backups, use the RDS API [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") or [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation with the following required
parameters:

- `DBInstanceIdentifier` or `DBClusterIdentifier`
- `BackupRetentionPeriod`

## Viewing automated

backups

To view your automated backups, choose **Automated backups** in
the navigation pane. To view individual snapshots associated with an automated
backup, choose **Snapshots** in the navigation pane. Alternatively,
you can describe individual snapshots associated with an automated backup. From
there, you can restore a DB instance directly from one of those snapshots.

Automated snapshot names follow the pattern
`rds:<database-name>-yyyy-mm-dd-hh-mm`, with
`yyyy-mm-dd-hh-mm` representing the date and time the snapshot was
created.

To describe the automated backups for your existing DB instances using the AWS CLI,
use one of the following commands:

```
aws rds describe-db-instance-automated-backups --db-instance-identifier `DBInstanceIdentifier`
```

or

```
aws rds describe-db-instance-automated-backups --dbi-resource-id `DbiResourceId`
```

To describe the retained automated backups for your existing DB instances using
the RDS API, call the [`DescribeDBInstanceAutomatedBackups`](../APIReference/API_DescribeDBInstanceAutomatedBackups.md "../APIReference/API_DescribeDBInstanceAutomatedBackups.md") action with one of
the following parameters:

- `DBInstanceIdentifier`
- `DbiResourceId`
