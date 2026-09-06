

# Restoring a DB cluster to a specified time using AWS Backup
<a name="aurora-pitr-bkp"></a>

You can use AWS Backup to manage your automated backups, and then to restore them to a specified time. To do this, you create a backup plan in AWS Backup and assign your DB cluster as a resource. Then you enable continuous backups for PITR in the backup rule. For more information on backup plans and backup rules, see the [*AWS Backup Developer Guide*](https://docs.aws.amazon.com/aws-backup/latest/devguide).

## Enabling continuous backups in AWS Backup
<a name="aurora-pitr-bkp.enable"></a>

You enable continuous backups in backup rules.

**To enable continuous backups for PITR**

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Backup plans**.

1. Under **Backup plan name**, select the backup plan that you use to back up your DB cluster.

1. Under the **Backup rules** section, choose **Add backup rule**.

   The **Add backup rule** page displays.

1. Select the **Enable continuous backups for point-in-time recovery (PITR)** check box.  
![Enable continuous backups for point-in-time recovery (PITR).](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/add_backup_rule_continuous_v2.png)

1. Choose other settings as needed, then choose **Add backup rule**.

## Restoring from a continuous backup in AWS Backup
<a name="aurora-pitr-bkp.restore"></a>

You restore to a specified time from a backup vault.

### Console
<a name="aurora-pitr-bkp.restore.CON"></a>

You can use the AWS Management Console to restore a DB cluster to a specified time.

**To restore from a continuous backup in AWS Backup**

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Backup vaults**.

1. Choose the backup vault that contains your continuous backup, for example **Default**.

   The backup vault detail page displays.

1. Under **Recovery points**, select the recovery point for the automated backup.

   It has a backup type of **Continuous** and a name with `continuous:cluster-{{AWS-Backup-job-number}}`.

1. For **Actions**, choose **Restore**.

   The **Restore backup** page displays.  
![Restore backup page for point-in-time recovery (PITR).](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/backup_vault_pitr.png)

1. For **Restore to point in time**, select **Specify date and time** to restore to a specific point in time.

1. Choose other settings as needed for restoring the DB cluster, then choose **Restore backup**.

   The **Jobs** page displays, showing the **Restore jobs** pane. A banner provides information about the restore job.

After the DB cluster is restored, you must add the primary (writer) DB instance to it. To create the primary instance for your DB cluster, call the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command. Include the name of the DB cluster as the `--db-cluster-identifier` parameter value.

### CLI
<a name="aurora-pitr-bkp.restore.CLI"></a>

You use the [start-restore-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html) AWS CLI command to restore the DB cluster to a specified time. The following parameters are required:
+ `--recovery-point-arn` – The Amazon Resource Name (ARN) for the recovery point from which to restore.
+ `--resource-type` – Use `Aurora`.
+ `--iam-role-arn` – The ARN for the IAM role that you use for AWS Backup operations.
+ `--metadata` – The metadata that you use to restore the DB cluster. The following parameters are required:
  + `DBClusterIdentifier`
  + `Engine`
  + `RestoreToTime` or `UseLatestRestorableTime`

The following example shows how to restore a DB cluster to a specified time.

```
aws backup start-restore-job \
--recovery-point-arn arn:aws:backup:eu-central-1:123456789012:recovery-point:continuous:cluster-itsreallyjustanexample1234567890-487278c2 \
--resource-type Aurora \
--iam-role-arn arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole \
--metadata '{"DBClusterIdentifier":"backup-pitr-test","Engine":"aurora-mysql","RestoreToTime":"2023-09-01T17:00:00.000Z"}'
```

The following example shows how to restore a DB cluster to the latest restorable time.

```
aws backup start-restore-job \
--recovery-point-arn arn:aws:backup:eu-central-1:123456789012:recovery-point:continuous:cluster-itsreallyjustanexample1234567890-487278c2 \
--resource-type Aurora \
--iam-role-arn arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole \
--metadata '{"DBClusterIdentifier":"backup-pitr-latest","Engine":"aurora-mysql","UseLatestRestorableTime":"true"}'
```

After the DB cluster is restored, you must add the primary (writer) DB instance to it. To create the primary instance for your DB cluster, call the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command. Include the name of the DB cluster as the `--db-cluster-identifier` parameter value.