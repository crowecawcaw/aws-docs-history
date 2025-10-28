# Back up and restore your SAP HANA system with the AWS Backint Agent for SAP HANA

When the AWS Backint agent is installed and configured on your Amazon EC2 instance, you can initiate backup and recovery using SQL statements, SAP HANA Cockpit, or SAP HANA Studio.

###### Topics

- [Backup and recovery using SQL statements](#aws-backint-agent-backup-recovery-sql "#aws-backint-agent-backup-recovery-sql")
- [Backup and recovery using SAP HANA Cockpit or SAP HANA Studio](#aws-backint-agent-backup-recovery-sap-hana-cockpit-studio "#aws-backint-agent-backup-recovery-sap-hana-cockpit-studio")
- [Get backup and recovery status](#aws-backint-agent-backup-recovery-status "#aws-backint-agent-backup-recovery-status")
- [Find your backup in an Amazon S3 bucket](#aws-backint-agent-backup-recovery-s3 "#aws-backint-agent-backup-recovery-s3")
- [Schedule and manage backups](#aws-backint-agent-backup-schedule "#aws-backint-agent-backup-schedule")
- [Backup retention](#aws-backint-agent-backup-retention "#aws-backint-agent-backup-retention")

## Backup and recovery using SQL statements

The following are a limited number of examples of SQL statements that you can use to perform backup and recovery. We recommend that you always refer to the SAP, SAP HANA Administration, or SQL Reference guides to find the syntax of all of the other options for your specific SAP HANA version. For more details, see [Backup and Recovery Statements](https://help.sap.com/viewer/4fe29514fd584807ac9f2a04f6754767/2.0.04/en-US/6304145fdb044950a55b1c419775a2a1.html "https://help.sap.com/viewer/4fe29514fd584807ac9f2a04f6754767/2.0.04/en-US/6304145fdb044950a55b1c419775a2a1.html") in the _SAP HANA SQL Reference Guide_.

The following example shows the syntax to initiate a full data backup of the system database.

```
BACKUP DATA USING BACKINT ('/usr/sap/<SID>/SYS/global/hdb/backint/SYSTEMDB/<MY_PREFIX>')
```

The following example shows the syntax to initiate a full data backup of the tenant database.

```
BACKUP DATA FOR <TENANT DB ID> USING BACKINT ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/<MY_PREFIX >')
```

The following example shows the syntax to initiate a differential data backup of the tenant database.

```
BACKUP DATA DIFFERENTIAL FOR <TENANT DB ID> USING BACKINT ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/<MY_PREFIX >')
```

The following example shows the syntax to initiate an incremental data backup of the tenant database.

```
BACKUP DATA INCREMENTAL FOR <TENANT DB ID> USING BACKINT ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/<MY_PREFIX >')
```

The following example shows the syntax to recover your tenant database to a particular point in time.

```
RECOVER DATABASE FOR <TENANT DB ID> UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' USING DATA PATH ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/') USING LOG PATH ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>') USING BACKUP_ID 1234567890123 CHECK ACCESS USING BACKINT
```

The following example shows the syntax to recover your tenant database with a specific data backup using catalogs stored in S3.

```
RECOVER DATA FOR <TENANT DB ID> USING BACKUP_ID 1234567890123 USING CATALOG BACKINT USING DATA PATH ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/') CLEAR LOG
```

The following example shows the syntax to recover your tenant database with a specific data backup without using a catalog.

```
RECOVER DATA FOR <TENANT DB ID>  USING BACKINT ('/usr/sap/<SID>/SYS/global/hdb/backint/DB_<TENANT DB ID>/<MY_PREFIX >') CLEAR LOG
```

With AWS Backint agent, you can perform system copies by restoring a backup of the source database into the target database. To perform system copies using AWS Backint agent, verify the following requirements.

1. You must have AWS Backint agent configured in both the source and target systems.
2. Check the compatibility of the SAP HANA software version of the source and target systems.
3. The AWS Backint agent in your target system should be able to access the Amazon S3 bucket where the backups of the source system are stored. If you use a different Amazon S3 bucket for backups in the source and target systems, you have to adjust the configuration parameters of the AWS Backint agent in the target system to temporarily point to the Amazon S3 bucket where the backups are stored in the source system.
4. If you are performing a system copy across two different AWS accounts, ensure that you have the appropriate IAM permissions and Amazon S3 bucket policies in place. See the [Identity and Access Management](aws-backint-agent-amazon-s3.md#aws-backint-agent-iam "aws-backint-agent-amazon-s3.md#aws-backint-agent-iam") section in this document for details.

The following is the syntax to restore a specific backup of the source tenant database into your target tenant database.

```
RECOVER DATA FOR <TARGET TENANT DB ID>  USING SOURCE '<SOURCE TENANT DB ID>@<SOURCE SYSTEM ID>' USING BACKUP_ID 1234567890123 USING CATALOG BACKINT USING DATA PATH ('/usr/sap/<SOURCE SYSTEM ID>/SYS/global/hdb/backint/DB_<SOURCE TENANT DB ID>/') CLEAR LOG
```

The following is an example of a SQL statement to restore a specific backup of the source tenant database, called `SRC`, in the source system `QAS` into a target tenant database called `TGT`.

```
RECOVER DATA FOR TGT USING SOURCE 'SRC@QAS' USING BACKUP_ID 1234567890123 USING CATALOG BACKINT USING DATA PATH ('/usr/sap/QAS/SYS/global/hdb/backint/DB_SRC/')  CLEAR LOG
```

The following is an example of a SQL statement to perform a point-in-time recovery of a source tenant database, called `SRC`, in a source system `QAS` into a target tenant database called `TGT`.

```
RECOVER DATABASE FOR TGT UNTIL TIMESTAMP '2020-01-31 01:00:00' CLEAR LOG USING SOURCE 'SRC@QAS' USING CATALOG BACKINT USING LOG PATH ('/usr/sap/QAS/SYS/global/hdb/backint/DB_SRC') USING DATA PATH ('/usr/sap/QAS/SYS/global/hdb/backint/DB_SRC/') USING BACKUP_ID 1234567890123 CHECK ACCESS USING BACKINT
```

## Backup and recovery using SAP HANA Cockpit or SAP HANA Studio

In addition to using SQL statements, you can initiate the backup and recovery process from SAP HANA Cockpit or SAP HANA Studio. For more information, see [Backup and Recovery](https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.4.0.0/en-US/7b60ff9fc11a4c36adb2e75b993a06c9.html "https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.4.0.0/en-US/7b60ff9fc11a4c36adb2e75b993a06c9.html") and [Reference: Backup Console (SAP HANA Studio)](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.03/en-US/2febf2472303493fbfe26eeb822f26f4.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.03/en-US/2febf2472303493fbfe26eeb822f26f4.html") in the SAP documentation. Ensure that you are using the latest version of SAP HANA Cockpit or SAP HANA studio to get all of the latest features from SAP.

## Get backup and recovery status

Use your current backup and restore methods to confirm the status of a backup and restore request, and to verify whether the AWS Backint agent is working correctly. For example, if you are using SAP HANA Studio to monitor the progress of a running backup, you can do the same for any backup requests triggered by the AWS Backint agent. For failure scenarios, you can review the AWS Backint agent logs or the SAP HANA backup logs for errors, and take action or reach out to AWS Support for assistance.

## Find your backup in an Amazon S3 bucket

You can verify the backup files in your Amazon S3 bucket from the Amazon S3 console or by using APIs. AWS Backint agent stores your backup files using a designated folder structure within your Amazon S3 bucket. During backup and restore, SAP HANA uses this folder structure to stream data into a pipe that Backint agents can read and write. AWS Backint agent maintains this same folder structure in the Amazon S3 bucket. We recommend that you do not change this structure after you back up your files. Changing the folder structure can cause issues during the restore operation and impact your recoverability.

For system and tenant databases, you can find your data, log, and catalog backups in the following locations. Your data backups will include an additional prefix that you used during the backup.

```
<amzn-s3-demo-bucket>/<optional-my-folder>/<SID>/usr/sap/<SID>/SYS/global/hdb/backint/SYSTEMDB/
```

```
<amzn-s3-demo-bucket>/<optional-my-folder>/<SID>/usr/sap/<SID>/SYS/global/hdb/backint/DB_<Tenant ID>/
```

## Schedule and manage backups

You can use SAP HANA Cockpit to schedule periodic backups of your target SAP HANA database, including log backups. Ensure that you choose Backint as the backup type when scheduling your backup. For more details, see [Schedule Backups](https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.6.0.0/en-US/307452ce29b942c895e5de614043983a.html "https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.6.0.0/en-US/307452ce29b942c895e5de614043983a.html") in the _SAP HANA Administration with SAP HANA Cockpit Guide_.

## Backup retention

Beginning with SAP HANA 2 SPS 03, you can use SAP HANA Cockpit to set the retention policies for your SAP HANA database backups. Based on your retention policies, SAP HANA Cockpit can automatically trigger jobs to delete old backups from catalogs, as well as the physical backups. This process also automatically deletes backup files stored in your Amazon S3 buckets. For more information, see "Retention Policy" under [Backup Configuration Settings](https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.10.0.0/en-US/b495da9a043a499893abc50c5cd367d9.html "https://help.sap.com/viewer/afa922439b204e9caf22c78b6b69e4f2/2.10.0.0/en-US/b495da9a043a499893abc50c5cd367d9.html") in the _SAP HANA Administration with SAP HANA Cockpit Guide_.
