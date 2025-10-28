# Deleting retained automated backups

You can delete retained automated backups when they are no longer needed.

###### To delete a retained automated backup

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated backups**.
3. On the **Retained** tab, choose the retained automated backup that you want to delete.
4. For **Actions**, choose **Delete**.
5. On the confirmation page, enter `delete me` and choose
   **Delete**.
   You can delete a retained automated backup by using the AWS CLI command [delete-db-instance-automated-backup](../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md "../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md") with the
   following option:

- `--dbi-resource-id` – The resource identifier for the source DB instance.

You can find the resource identifier for the source DB instance of a retained automated backup by running the
AWS CLI command [describe-db-instance-automated-backups](../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md "../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md").
The following example deletes the retained automated backup with source DB instance resource identifier
`db-123ABCEXAMPLE`.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance-automated-backup \
    --dbi-resource-id `db-123ABCEXAMPLE`
```

For Windows:

```
aws rds delete-db-instance-automated-backup ^
    --dbi-resource-id `db-123ABCEXAMPLE`
```

You can delete a retained automated backup by using the Amazon RDS API operation [DeleteDBInstanceAutomatedBackup](../APIReference/API_DeleteDBInstanceAutomatedBackup.md "../APIReference/API_DeleteDBInstanceAutomatedBackup.md") with the
following parameter:

- `DbiResourceId` – The resource identifier for the source DB instance.

You can find the resource identifier for the source DB instance of a retained automated backup using the Amazon RDS
API operation [DescribeDBInstanceAutomatedBackups](../APIReference/API_DescribeDBInstanceAutomatedBackups.md "../APIReference/API_DescribeDBInstanceAutomatedBackups.md").

## Disabling automated backups

You might want to temporarily disable automated backups in certain situations, for
example while loading large amounts of data.

###### Important

We highly discourage disabling automated backups because it disables point-in-time
recovery. Disabling automatic backups for a DB instance or Multi-AZ DB cluster
deletes all existing automated backups for the database. If you disable and then
re-enable automated backups, you can restore starting only from the time you
re-enabled automated backups.

###### To disable automated backups immediately

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB instance or Multi-AZ DB cluster that you want to
   modify.
3. Choose **Modify**.
4. For **Backup retention period**, choose **0 days**.
5. Choose **Continue**.
6. Choose **Apply immediately**.
7. Choose **Modify DB instance** or **Modify
   cluster** to save your changes and disable automated
   backups.
   To disable automated backups immediately, use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") or
   [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command and set the backup retention period to 0
   with `--apply-immediately`.

The following example immediately disables automatic backups on a Multi-AZ
DB cluster.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --backup-retention-period 0 \
    `--apply-immediately`
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --backup-retention-period 0 ^
    `--apply-immediately`
```

To know when the modification is in effect, call
`describe-db-instances` for the DB instance (or
`describe-db-clusters` for a Multi-AZ DB cluster) until the value
for backup retention period is 0 and `mydbcluster` status is
available.

```
aws rds describe-db-clusters --db-cluster-identifier `mydcluster`
```

To disable automated backups immediately, call the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") or
[ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md")
operation with the following parameters:

- `DBInstanceIdentifier = mydbinstance` (or
  `DBClusterIdentifier = mydbcluster`)
- `BackupRetentionPeriod = 0`

```
https://rds.amazonaws.com/
    ?Action=ModifyDBInstance
    &DBInstanceIdentifier=mydbinstance
    &BackupRetentionPeriod=0
    &SignatureVersion=2
    &SignatureMethod=HmacSHA256
    &Timestamp=2009-10-14T17%3A48%3A21.746Z
    &AWSAccessKeyId=<&AWS; Access Key ID>
    &Signature=<Signature>
```
