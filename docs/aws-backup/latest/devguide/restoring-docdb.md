# Restoring a DocumentDB cluster

## Use the AWS Backup console to restore Amazon DocumentDB recovery points

Restoring a Amazon DocumentDB cluster requires that you specify multiple restore options. For
information about these options, see [Restoring from a Cluster Snapshot](../../../documentdb/latest/developerguide/backup_restore-restore_from_snapshot.md "../../../documentdb/latest/developerguide/backup_restore-restore_from_snapshot.md") in the
_Amazon DocumentDB Developer Guide_.

###### To restore a Amazon DocumentDB cluster

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and the
   Amazon DocumentDB resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. Ensure you are on the console page **Restore Amazon DocumentDB cluster
   snapshots**.
5. For **Restore options**, you can configure the following:
   - **Engine version** - Select the DocumentDB engine version for the restored cluster.

###### Note

Instance class and number of instances cannot be configured during the restore process. The restored DocumentDB cluster will use the default instance configuration. You can modify the instance class and add or remove instances after the restore completes by using the Amazon DocumentDB console or API. 6. In the **Settings** pane, input a unique name for your DB cluster
identifier.

You can use letters, numbers, and hyphens, though you cannot have two consecutive
hyphens or end the name with a hyphen. The final name will be all lowercase. 7. In the **Database options** pane, select the database
port.

This is the TCP/IP port that the DB instance or cluster will use for application
connections. The connection string of any application connecting to the DB instance or
cluster must specify its port number. Both the security group applied to the DB
instance or cluster and your organization firewalls must allow connections to the
port. All DB instances in a DB cluster use the same port. 8. Also in the **Database options** pane, select the DB cluster
parameter group.

This is the parameter group associated with this instance's DB cluster. The DB
cluster parameter group acts as a container for engine configuration values that are
applied to every DB instance in the cluster. 9. In the **Encryption** pane, select the key that will be used to
encrypt this database volume. The default is `aws/rds`. You may
alternatively use a customer managed key (CMK). 10. In the **Log exports** pane, choose the log types to publish to
Amazon CloudWatch Logs. The **IAM role** is already defined. 11. In the **Restore role** pane, choose either the default IAM role
for the restore job or a different IAM role. 12. In the Protected resource tags pane, you may optionally choose to copy tags from
the backup to the restored database cluster. 13. After specifying all your settings, choose **Restore
backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job. 14. After your restore finishes, attach your restored Amazon DocumentDB cluster to an Amazon RDS
instance.

## Use the AWS Backup API, CLI, or SDK to restore Amazon DocumentDB recovery points

First, restore your cluster. Use `StartRestoreJob`. You can specify the following metadata during Amazon DocumentDB
restores:

```
availabilityZones
backtrackWindow
copyTagsToSnapshot // Boolean
databaseName // string
dbClusterIdentifier // string
dbClusterParameterGroupName // string
dbSubnetGroupName // string
enableCloudwatchLogsExports // string
enableIAMDatabaseAuthentication // Boolean
engine // string
engineMode // string
engineVersion // string
kmsKeyId // string
port // integer
optionGroupName // string
scalingConfiguration
vpcSecurityGroupIds // string



```

Then, attach your restored Amazon DocumentDB cluster to an Amazon RDS instance using
`create-db-instance`.

- For Linux, macOS, or Unix:

```
aws docdb create-db-instance --db-instance-identifier `sample-instance` /
                  --db-cluster-identifier `sample-cluster` --engine docdb --db-instance-class `db.r5.large`
```

- For Windows:

```
aws docdb create-db-instance --db-instance-identifier `sample-instance` ^
                  --db-cluster-identifier `sample-cluster` --engine docdb --db-instance-class `db.r5.large`
```
