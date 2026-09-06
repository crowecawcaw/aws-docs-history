

# Restoring an RDS Custom for Oracle instance to a point in time
<a name="custom-backup.pitr"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can restore a DB instance to a specific point in time (PITR), creating a new DB instance. To support PITR, your DB instances must have backup retention set to a nonzero value.

The latest restorable time for an RDS Custom for Oracle DB instance depends on several factors, but is typically within 5 minutes of the current time. To see the latest restorable time for a DB instance, use the AWS CLI [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command and look at the value returned in the `LatestRestorableTime` field for the DB instance. To see the latest restorable time for each DB instance in the Amazon RDS console, choose **Automated backups**.

You can restore to any point in time within your backup retention period. To see the earliest restorable time for each DB instance, choose **Automated backups** in the Amazon RDS console.

For general information about PITR, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md).

**Topics**
+ [PITR considerations for RDS Custom for Oracle](#custom-backup.pitr.oracle)

## PITR considerations for RDS Custom for Oracle
<a name="custom-backup.pitr.oracle"></a>

In RDS Custom for Oracle, PITR differs in the following important ways from PITR in Amazon RDS:
+ The restored database has the same name as in the source DB instance. You can't specify a different name. The default is `ORCL`.
+ `AWSRDSCustomIamRolePolicy` requires new permissions. For more information, see [Step 2: Add an access policy to AWSRDSCustomInstanceRoleForRdsCustomInstance](custom-setup-orcl.md#custom-setup-orcl.iam.add-policy).
+ All RDS Custom for Oracle DB instances must have backup retention set to a nonzero value.
+ If you change the operating system or DB instance time zone, PITR might not work. For information about changing time zones, see [Oracle time zone](custom-managing.timezone.md).
+ If you set automation to `ALL_PAUSED`, RDS Custom pauses the upload of archived redo log files, including logs created before the latest restorable time (LRT). We recommend that you pause automation for a brief period.

  To illustrate, assume that your LRT is 10 minutes ago. You pause automation. During the pause, RDS Custom doesn't upload archived redo logs. If your DB instance crashes, you can only recover to a time before the LRT that existed when you paused. When you resume automation, RDS Custom resumes uploading logs. The LRT advances. Normal PITR rules apply. 
+ In RDS Custom, you can manually specify an arbitrary number of hours to retain archived redo logs before RDS Custom deletes them after upload. Specify the number of hours as follows:

  1. Create a text file named `/opt/aws/rdscustomagent/config/redo_logs_custom_configuration.json`.

  1. Add a JSON object in the following format: `{"archivedLogRetentionHours" : "{{num_of_hours}}"}`. The number must be an integer in the range 1–840.
+ Assume that you plug a non-CDB into a container database (CDB) as a PDB and then attempt PITR. The operation succeeds only if you previously backed up the PDB. After you create or modify a PDB, we recommend that you always back it up.
+ We recommend that you don't customize database initialization parameters. For example, modifying the following parameters affects PITR:
  + `CONTROL_FILE_RECORD_KEEP_TIME` affects the rules for uploading and deleting logs.
  + `LOG_ARCHIVE_DEST_n` doesn't support multiple destinations.
  + `ARCHIVE_LAG_TARGET` affects the latest restorable time. `ARCHIVE_LAG_TARGET` is set to `300` because the recovery point objective (RPO) is 5 minutes. To honor this objective, RDS switches the online redo log every 5 minutes and stores it in an Amazon S3 bucket. If the frequency of the log switch causes a performance issue for your RDS Custom for Oracle database, you can scale your DB instance and storage to one with higher IOPS and throughput. If necessary for your recovery plan, you can adjust the setting of the `ARCHIVE_LAG_TARGET` initialization parameter to a value from 60–7200.
+ If you customize database initialization parameters, we strongly recommend that you customize only the following:
  + `COMPATIBLE` 
  + `MAX_STRING_SIZE`
  + `DB_FILES` 
  + `UNDO_TABLESPACE` 
  + `ENABLE_PLUGGABLE_DATABASE` 
  + `CONTROL_FILES` 
  + `AUDIT_TRAIL` 
  + `AUDIT_TRAIL_DEST` 

  For all other initialization parameters, RDS Custom restores the default values. If you modify a parameter that isn't in the preceding list, it might have an adverse effect on PITR and lead to unpredictable results. For example, `CONTROL_FILE_RECORD_KEEP_TIME` affects the rules for uploading and deleting logs.

You can restore an RDS Custom DB instance to a point in time using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="custom-backup.pitr2.CON"></a>

**To restore an RDS Custom DB instance to a specified time**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Automated backups**.

1. Choose the RDS Custom DB instance that you want to restore.

1. For **Actions**, choose **Restore to point in time**.

   The **Restore to point in time** window appears.

1. Choose **Latest restorable time** to restore to the latest possible time, or choose **Custom** to choose a time.

   If you chose **Custom**, enter the date and time to which you want to restore the instance.

   Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time (UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time.

1. For **DB instance identifier**, enter the name of the target restored RDS Custom DB instance. The name must be unique.

1. Choose other options as needed, such as DB instance class.

1. Choose **Restore to point in time**.

## AWS CLI
<a name="custom-backup.pitr2.CLI"></a>

You restore a DB instance to a specified time by using the [ restore-db-instance-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html) AWS CLI command to create a new RDS Custom DB instance.

Use one of the following options to specify the backup to restore from:
+ `--source-db-instance-identifier {{mysourcedbinstance}}`
+ `--source-dbi-resource-id {{dbinstanceresourceID}}`
+ `--source-db-instance-automated-backups-arn {{backupARN}}`

The `custom-iam-instance-profile` option is required.

The following example restores `my-custom-db-instance` to a new DB instance named `my-restored-custom-db-instance`, as of the specified time.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds restore-db-instance-to-point-in-time \
2.     --source-db-instance-identifier {{my-custom-db-instance}}\
3.     --target-db-instance-identifier {{my-restored-custom-db-instance}} \
4.     --custom-iam-instance-profile {{AWSRDSCustomInstanceProfileForRdsCustomInstance}} \
5.     --restore-time {{2022-10-14T23:45:00.000Z}}
```
For Windows:  

```
1. aws rds restore-db-instance-to-point-in-time ^
2.     --source-db-instance-identifier {{my-custom-db-instance}} ^
3.     --target-db-instance-identifier {{my-restored-custom-db-instance}} ^
4.     --custom-iam-instance-profile {{AWSRDSCustomInstanceProfileForRdsCustomInstance}} ^
5.     --restore-time {{2022-10-14T23:45:00.000Z}}
```