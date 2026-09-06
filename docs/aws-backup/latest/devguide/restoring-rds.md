

# Restore an RDS database
<a name="restoring-rds"></a>

Restoring an Amazon RDS database requires specifying multiple restore options. For more information about these options, see [Backing Up and Restoring an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) in the *Amazon RDS User Guide*.

## Use the AWS Backup console to restore Amazon RDS recovery points
<a name="rds-restore-console"></a>

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Protected resources** and the Amazon RDS resource ID you want to restore.

1. On the **Resource details** page, a list of recovery points for the selected resource ID is shown. To restore a resource, in the **Backups** pane, choose the radio button next to the recovery point ID of the resource. In the upper-right corner of the pane, choose **Restore**.

1. In the **Instance specifications** pane, accept the defaults or specify the options that you need.

1. In the **Settings** pane, specify a name that is unique for all DB instances and clusters owned by your AWS account in the current Region. The DB instance identifier is case insensitive, but it is stored as all lowercase, as in "`mydbinstance`". This is a required field. 

1. In the **Network & Security** pane, accept the defaults or specify the options that you need. 

1. In the **Database options** pane, accept the defaults or specify the options that you need. 

1. In the **Encryption** pane, use the default settings. If the source database instance for the snapshot was encrypted, the restored database instance will also be encrypted. This encryption cannot be removed.

1. In the **Log exports** pane, choose the log types to publish to Amazon CloudWatch Logs. The **IAM role** is already defined. 

1. In the **Maintenance** pane, accept the default or specify the option for **Auto minor version upgrade**. 

1. In the **Restore role** pane, choose the IAM role that AWS Backup will assume for this restore. 
**Note**  
If role manager is enabled in your account, AWS Backup selects the default service role for you, and a **Customize** option is available. For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

1. Choose **Restore backup**.

   The **Restore jobs** pane appears. A message at the top of the page provides information about the restore job.

## Use the AWS Backup API, CLI, or SDK to restore Amazon RDS recovery points
<a name="rds-restore-cli"></a>

Use `[StartRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartRestoreJob.html)`. For information on accepted metadata and values, see [`RestoreDBInstanceFromDBSnapshot`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) and [`RestoreDBInstanceToPointInTime`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html) in the *Amazon RDS API Reference*. Additionally, AWS Backup accepts the following information-only attributes. However, including them will not affect the restore:

```
EngineVersion
KmsKeyId       
Encrypted       
vpcId
```