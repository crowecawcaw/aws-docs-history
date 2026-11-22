

# Migrating from Linux to Linux for Amazon RDS for Db2

Migrating from on-premises Linux to Amazon RDS for Db2 (deployed on Linux only) requires you to back up your self-managed Db2 database to an Amazon S3 bucket. Then, you use Amazon RDS stored procedures to restore your Db2 database to an RDS for Db2 DB instance. For more information about using Amazon S3, see [Integrating an Amazon RDS for Db2 DB instance with Amazon S3](db2-s3-integration.md).

Backup and restore for RDS for Db2 follows the IBM Db2 Db2 supported upgrade paths and restrictions. For more information, see [Supported upgrade paths for Db2 servers](https://www.ibm.com/docs/en/db2/11.5?topic=servers-supported-upgrade-paths-db2) and [Upgrade restrictions for Db2 servers](https://www.ibm.com/docs/en/db2/11.5?topic=servers-upgrade-restrictions) in the IBM Db2 Db2 documentation.

**Topics**
+ [Limitations and recommendations](#db2-migration-linux-linux-limitations)
+ [Backing up your database to Amazon S3](#db2-migration-linux-linux-backing-up-database)
+ [Creating a default automatic storage group](#db2-migration-linux-linux-creating-auto-storage-group)
+ [Restoring your Db2 database (same version or version upgrade)](#db2-migration-linux-linux-restore)
+ [Restoring your Db2 database with near-zero downtime](#db2-migration-linux-linux-near-zero)

## Limitations and recommendations
<a name="db2-migration-linux-linux-limitations"></a>

The following limitations and recommendations apply to the three restore paths: same-version restore, version-upgrade restore, and near-zero downtime restore. The matrix below shows which apply to each approach. A value of *Applies* indicates that the item applies to that approach. *Not applicable* indicates that the item doesn't apply to that approach.


| No. | Limitation or recommendation | Restore (same version) | Restore (version upgrade) | Restore (near-zero downtime) | 
| --- | --- | --- | --- | --- | 
| 1 | Supports offline and online backups. No incremental or Delta backups. The on-premises and RDS for Db2 versions must match. | Applies | Not applicable | Not applicable | 
| 2 | Supports offline only backups. No incremental or Delta backups. | Not applicable | Applies | Not applicable | 
| 3 | Supports an online only backup (database kept in rollforward-pending while archive logs upload). The on-premises and RDS for Db2 versions must match. | Not applicable | Not applicable | Applies | 
| 4 | No cross-Region restore (the Amazon S3 bucket must be in the same Region as the DB instance). | Applies | Applies | Applies | 
| 5 | Amazon S3 limits the size of uploaded files to 5 TB. Split larger backup files. | Applies | Applies | Applies | 
| 6 | No non-fenced external routines, incremental restores, or Delta restores. | Applies | Applies | Applies | 
| 7 | No restore from an encrypted source (you can restore to an encrypted Amazon RDS instance). | Applies | Applies | Applies | 
| 8 | USE\_STREAMING\_RESTORE affects storage sizing. TRUE streams the backup. FALSE downloads and extracts the backup. | Applies | Applies | Applies | 
| 9 | The maximum restored database size equals the maximum supported size minus temporary restore space. | Applies | Applies | Applies | 

**Post-restore hardening** applies to all restore paths:
+ RDS for Db2 revokes authorities higher than `DBADM` and caps the master user at `DBADM`.
+ The restore process sets the database configuration parameter `connect_proc` to null.
+ The restore process applies archive logging or circular logging based on the native backup image setting.
+ The restore process removes audit policies and cataloged storage-access aliases that are carried in the backup image.

## Backing up your database to Amazon S3
<a name="db2-migration-linux-linux-backing-up-database"></a>

To back up your database on Amazon S3, you need the following AWS components:
+ *An Amazon S3 bucket to store your backup files*: Upload any backup files that you want to migrate to Amazon RDS. If you already have an Amazon S3 bucket, you can use that bucket. If you don't have an Amazon S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon S3 User Guide*.
+ *An IAM role to access the Amazon S3 bucket*: If you already have an AWS Identity and Access Management (IAM) role, you can use that role. If you don't have a role, see [Step 2: Create an IAM role and attach your IAM policy](db2-s3-integration.md#db2-creating-iam-role).
+ *An IAM policy with trust relationships and permissions attached to your IAM role*: For more information, see [Step 1: Create an IAM policy](db2-s3-integration.md#db2-creating-iam-policy).
+ *The IAM role added to your RDS for Db2 DB instance*: For more information, see [Step 3: Add your IAM role to your RDS for Db2 DB instance](db2-s3-integration.md#db2-adding-iam-role).

**Note**  
If your database is large and would take a long time to transfer to an Amazon S3 bucket, you can order an AWS Snow Family device and ask AWS to perform the backup. After you copy your files to the device and return it to the Snow Family team, the team transfers your backed-up images to your Amazon S3 bucket. For more information, see the [AWS Snow Family documentation](https://docs.aws.amazon.com/snowball/).

## Creating a default automatic storage group
<a name="db2-migration-linux-linux-creating-auto-storage-group"></a>

Your source database must have a default automatic storage group. If your database doesn't have a default automatic storage group, you must create one.

**To create a default automatic storage group**

1. Connect to your source database. In the following example, replace {{source\_database}} with the name of your database.

   ```bash
   db2 connect to {{source_database}}
   ```

1. Create an automatic storage group and set it as the default. In the following example, replace {{storage\_path}} with the absolute path to where the storage group is located.

   ```bash
   db2 "create stogroup IBMSTOGROUP ON {{storage_path}} set as default"
   ```

1. Terminate the backend process by running the following command.

   ```bash
   db2 terminate
   ```

## Restoring your Db2 database (same version or version upgrade)
<a name="db2-migration-linux-linux-restore"></a>

After you back up your database on Amazon S3 and create an automatic storage group, you are ready to restore your Db2 database to your RDS for Db2 DB instance.

**To restore your Db2 database from your Amazon S3 bucket to your RDS for Db2 DB instance**

1. Back up your database on premises.

   1. To prepare for backup, deactivate the database and stop all database services. In the following example, replace {{source\_database}} with the name of the database that you created the storage group for.

      ```bash
      db2 deactivate db {{source_database}}
      ```

   1. Back up the database. In the following example, replace {{source\_database}} with the name of the database that you created the storage group for. Replace {{file\_system\_path}} with the absolute path to where you want to back up the database. After the backup is complete, copy the backup file to your Amazon S3 bucket. For more information, see [BACKUP DATABASE command](https://www.ibm.com/docs/en/db2/11.5.x?topic=commands-backup-database) in the IBM Db2 documentation.

      ```bash
      db2 backup database {{source_database}} to {{file_system_path}}
      ```

1. Connect to the `rdsadmin` database with the {{master\_username}} and {{master\_password}} for your RDS for Db2 DB instance.

   ```bash
   db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
   ```

1. (Optional) To ensure that your database is configured with the optimal restore settings, check the values for the following parameters by calling [rdsadmin.show\_configuration](db2-sp-managing-databases.md#db2-sp-show-configuration):
   + `RESTORE_DATABASE_NUM_BUFFERS`
   + `RESTORE_DATABASE_PARALLELISM`
   + `RESTORE_DATABASE_NUM_MULTI_PATHS`
   + `USE_STREAMING_RESTORE`

   Use [rdsadmin.set\_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration) to modify these values as needed. Properly configuring these parameters can improve performance when you restore databases with large volumes of data. Set `USE_STREAMING_RESTORE` to `TRUE` to reduce storage requirements and improve restoration speed compared to downloading and extracting the full backup file.

1. To restore your database, call [rdsadmin.restore\_database](db2-sp-managing-databases.md#db2-sp-restore-database).

## Restoring your Db2 database with near-zero downtime
<a name="db2-migration-linux-linux-near-zero"></a>

With near-zero downtime restore, Amazon RDS keeps your database in a rollforward-pending state as you upload your archived transaction logs, which helps prevent disruptions to ongoing operations.

**To back up and restore your database for near-zero downtime migration**

1. Perform an online backup of your source database. For more information, see [BACKUP DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-backup-database) in the IBM Db2 documentation.

1. Copy the backup of your database to an Amazon S3 bucket. For information about using Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. Connect to the `rdsadmin` server with the {{master\_username}} and {{master\_password}} for your RDS for Db2 DB instance.

   ```bash
   db2 connect to rdsadmin user {{master_username}} using {{master_password}}
   ```

1. (Optional) To ensure that your database is configured with the optimal settings, check the values for the following parameters by calling [rdsadmin.show\_configuration](db2-sp-managing-databases.md#db2-sp-show-configuration):
   + `RESTORE_DATABASE_NUM_BUFFERS`
   + `RESTORE_DATABASE_PARALLELISM`
   + `RESTORE_DATABASE_NUM_MULTI_PATHS`
   + `USE_STREAMING_RESTORE`

   Use [rdsadmin.set\_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration) to modify these values as needed. Properly configuring these parameters can improve performance when you restore databases with large volumes of data. Set `USE_STREAMING_RESTORE` to `TRUE` to reduce storage requirements and improve restoration speed compared to downloading and extracting the full backup file.

1. Restore the backup on the RDS for Db2 server by calling `rdsadmin.restore_database`. Set `backup_type` to `ONLINE`. For more information, see [rdsadmin.restore\_database](db2-sp-managing-databases.md#db2-sp-restore-database).

After you restore the backup, apply your archive logs and switch your applications to the RDS for Db2 DB instance.

**To apply logs and cut over to your RDS for Db2 DB instance**

1. Copy your archive logs from your source server to your Amazon S3 bucket. Upload archive log files to a dedicated prefix that doesn't contain backup images or other non-log files. Archive log files must use the standard Db2 naming format (`S{{sequence}}.LOG`). For more information, see [Archive logging](https://www.ibm.com/docs/en/db2/11.5?topic=logging-archive) in the IBM Db2 documentation.

   For example, if your backup files are at `backups/TESTDB/`, upload your archive logs to a separate prefix such as `archiveLogs/TESTDB/`.

1. Apply archive logs as many times as needed by calling `rdsadmin.rollforward_database`. Set the `s3_prefix` to the dedicated archive log prefix, for example `archiveLogs/TESTDB/`. Ensure that the prefix contains only archive log files in the `S{{sequence}}.LOG` format. Set `complete_rollforward` to `FALSE` to keep the database in a `ROLL-FORWARD PENDING` state. For more information, see [rdsadmin.rollforward\_database](db2-sp-managing-databases.md#db2-sp-rollforward-database).

1. Bring the database online by calling `rdsadmin.complete_rollforward` after you apply all of the archive logs. For more information, see [rdsadmin.complete\_rollforward](db2-sp-managing-databases.md#db2-sp-complete-rollforward).

1. Switch application connections to the RDS for Db2 server by either updating your application endpoints for the database or by updating the DNS endpoints to redirect traffic to the RDS for Db2 server. You can also use the Db2 automatic client reroute feature on your self-managed Db2 database with the RDS for Db2 database endpoint. For more information, see [Automatic client reroute description and setup](https://www.ibm.com/docs/en/db2/11.5?topic=reroute-configuring-automatic-client) in the IBM Db2 documentation.

1. (Optional) Shut down your source database.