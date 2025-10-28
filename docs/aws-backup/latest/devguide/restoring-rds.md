# Restore an RDS database

Restoring an Amazon RDS database requires specifying multiple restore options. For more
information about these options, see [Backing Up and Restoring an Amazon RDS DB Instance](../../../AmazonRDS/latest/UserGuide/CHAP_CommonTasks.md "../../../AmazonRDS/latest/UserGuide/CHAP_CommonTasks.md") in the
_Amazon RDS User Guide_.

## Use the AWS Backup console to restore Amazon RDS recovery

points

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and the
   Amazon RDS resource ID you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. In the **Instance specifications** pane, accept the defaults or
   specify the options that you need.
5. In the **Settings** pane, specify a name that is unique for all
   DB instances and clusters owned by your AWS account in the current Region. The DB
   instance identifier is case insensitive, but it is stored as all lowercase, as in
   "`mydbinstance`". This is a required field.
6. In the **Network & Security** pane, accept the defaults or
   specify the options that you need.
7. In the **Database options** pane, accept the defaults or specify
   the options that you need.
8. In the **Encryption** pane, use the default settings. If the
   source database instance for the snapshot was encrypted, the restored database
   instance will also be encrypted. This encryption cannot be removed.
9. In the **Log exports** pane, choose the log types to publish to
   Amazon CloudWatch Logs. The **IAM role** is already defined.
10. In the **Maintenance** pane, accept the default or specify the
    option for **Auto minor version upgrade**.
11. In the **Restore role** pane, choose the IAM role that AWS Backup
    will assume for this restore.
12. Choose **Restore backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job.

## Use the AWS Backup API, CLI, or SDK to restore Amazon RDS recovery

points

Use `StartRestoreJob`. For information on accepted metadata and values, see
[`RestoreDBInstanceFromDBSnapshot`](../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.md") and [`RestoreDBInstanceToPointInTime`](../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.md") in the _Amazon RDS API
Reference_. Additionally, AWS Backup accepts the following information-only
attributes. However, including them will not affect the restore:

```
EngineVersion
KmsKeyId
Encrypted
vpcId
```
