# Migrating from Linux to Linux with near-zero downtime for Amazon RDS for Db2

With this migration approach, you migrate a Linux-based Db2 database from
one self-managed Db2 database (source) to Amazon RDS for Db2. This approach results in minimal to
no outage or downtime for the application or users. This approach backs up your database and
restores it with log replay, which helps prevent disruptions to ongoing operations and
provides high availability of your database.

To achieve near-zero downtime migration, RDS for Db2 implements restore with log replay. This
approach takes a backup of your self-managed Linux-based Db2 database and
restores it on the RDS for Db2 server. With Amazon RDS stored procedures, you then apply subsequent
transaction logs to bring the database up to date.

###### Topics

- [Limitations and recommendations for near-zero downtime migration](#db2-near-zero-downtime-migration-limitations "#db2-near-zero-downtime-migration-limitations")
- [Backing up your database to Amazon S3](#db2-near-zero-downtime-backing-up-database "#db2-near-zero-downtime-backing-up-database")
- [Creating a default automatic storage group](#db2-near-zero-migration-creating-auto-storage-group "#db2-near-zero-migration-creating-auto-storage-group")
- [Migrating your Db2 database](#db2-migrating-db2-database "#db2-migrating-db2-database")

## Limitations and recommendations for near-zero downtime migration

The following limitations and recommendations apply to using near-zero downtime
migration:

- Amazon RDS requires an online backup for near-zero downtime migration. This is
  because Amazon RDS keeps your database in a rollforward pending state as you upload
  your archived transaction logs. For more information, see [Migrating your Db2 database](#db2-migrating-db2-database "#db2-migrating-db2-database").
- You can't restore from an Amazon S3 bucket in an AWS Region that is different
  from the Region where your RDS for Db2 DB instance is located.
- Amazon S3 limits the size of files uploaded to an S3 bucket to 5 TB. If your
  database backup file exceeds 5 TB, then split the backup file into smaller
  files.
- Amazon RDS doesn't support non-fenced external routines, incremental restores, or
  Delta restores.
- You can't restore from an encrypted source database, but you can restore to an
  encrypted Amazon RDS DB instance.

The restoration process differs depending on your configuration.

If you set `USE_STREAMING_RESTORE` to `TRUE`, Amazon RDS directly
streams your backup from your S3 bucket during restoration. Streaming significantly
reduces storage requirements. You only need to provision storage space equal to or
greater than either the size of the backup or the size of the original database,
whichever is larger.

If you set `USE_STREAMING_RESTORE` to `FALSE`, Amazon RDS first
downloads the backup to your RDS for Db2 DB instance and then extracts the backup.
Extraction requires additional storage space. You must provision storage space equal to
or greater than the sum of the size of the backup plus the size of the original
database.

The maximum size of the restored database equals the maximum supported database size
minus any space required for temporary storage during the restoration process.

## Backing up your database to Amazon S3

To back up your database on Amazon S3, you need the following AWS components:

- _An Amazon S3 bucket to store your backup files_:
  Upload any backup files that you want to migrate to Amazon RDS. Amazon RDS requires an
  online backup for near-zero downtime migration. If you already have an S3
  bucket, you can use that bucket. If you don't have an S3 bucket, see [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

###### Note

If your database is large and would take a long time to transfer to an S3
bucket, you can order an AWS Snow Family device and ask AWS to perform
the backup. After you copy your files to the device and return it to the
Snow Family team, the team transfers your backed-up images to your S3
bucket. For more information, see the [AWS Snow Family documentation](../../../snowball.md "../../../snowball.md").

- _An IAM role to access the S3 bucket_: If
  you already have an AWS Identity and Access Management (IAM) role, you can use that role. If you don't
  have a role, see [Step 2: Create an IAM role and attach your IAM policy](db2-s3-integration.md#db2-creating-iam-role "db2-s3-integration.md#db2-creating-iam-role").
- _An IAM policy with trust relationships and
  permissions attached to your IAM role_: For more information,
  see [Step 1: Create an IAM policy](db2-s3-integration.md#db2-creating-iam-policy "db2-s3-integration.md#db2-creating-iam-policy").
- _The IAM role added to your RDS for Db2 DB
  instance_: For more information, see [Step 3: Add your IAM role to your RDS for Db2 DB instance](db2-s3-integration.md#db2-adding-iam-role "db2-s3-integration.md#db2-adding-iam-role").

## Creating a default automatic storage group

Your source database must have a default automatic storage group. If your database
doesn't have a default automatic storage group, you must create one.

###### To create a default automatic storage group

1. Connect to your source database. In the following example, replace
   `source_database` with the name of your
   database.

```
db2 connect to `source_database`
```

2. Create an automatic storage group and set it as the default. In the following
   example, replace `storage_path` with the absolute path
   to where the storage group is located.

```
db2 "create stogroup IBMSTOGROUP ON `storage_path` set as default"
```

3. Terminate backend processes.

```
db2 terminate
```

## Migrating your Db2 database

After you set up for near-zero downtime migration, you are ready to migrate your Db2
database from your Amazon S3 bucket to your RDS for Db2 DB instance.

###### To perform a near-zero downtime migration of backup files from your Amazon S3 bucket to your RDS for Db2 DB instance

1. Perform an online backup of your source database. For more information, see
   [BACKUP DATABASE command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-backup-database "https://www.ibm.com/docs/en/db2/11.5?topic=commands-backup-database") in the IBM Db2
   documentation.
2. Copy the backup of your database to an Amazon S3 bucket. For information about
   using Amazon S3, see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md").
3. Connect to the `rdsadmin` server with the
   `master_username` and
   `master_password` for your RDS for Db2 DB
   instance.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

4.  (Optional) To ensure that your database is configured with the optimal
    settings, check the values for the following parameters by calling [rdsadmin.show_configuration](db2-sp-managing-databases.md#db2-sp-show-configuration "db2-sp-managing-databases.md#db2-sp-show-configuration"):

        * `RESTORE_DATABASE_NUM_BUFFERS`
        * `RESTORE_DATABASE_PARALLELISM`
        * `RESTORE_DATABASE_NUM_MULTI_PATHS`
        * `USE_STREAMING_RESTORE`

    Use [rdsadmin.set_configuration](db2-sp-managing-databases.md#db2-sp-set-configuration "db2-sp-managing-databases.md#db2-sp-set-configuration") to modify these values as
    needed. Properly configuring these parameters can significantly improve
    performance when restoring databases with large volumes of data. For most
    migration scenarios, we recommend setting `USE_STREAMING_RESTORE` to
    `TRUE` because it reduces storage requirements and can improve
    restoration speed.

5.  Restore the backup on the RDS for Db2 server by calling
    `rdsadmin.restore_database`. Set `backup_type` to
    `ONLINE`. For more information, see [rdsadmin.restore_database](db2-sp-managing-databases.md#db2-sp-restore-database "db2-sp-managing-databases.md#db2-sp-restore-database").
6.  Copy your archive logs from your source server to your S3 bucket. For more
    information, see [Archive
    logging](https://www.ibm.com/docs/en/db2/11.5?topic=logging-archive "https://www.ibm.com/docs/en/db2/11.5?topic=logging-archive") in the IBM Db2 documentation.
7.  Apply archive logs as many times as needed by calling
    `rdsadmin.rollforward_database`. Set
    `complete_rollforward` to `FALSE` to keep the database
    in a `ROLL-FORWARD PENDING` state. For more information, see [rdsadmin.rollforward_database](db2-sp-managing-databases.md#db2-sp-rollforward-database "db2-sp-managing-databases.md#db2-sp-rollforward-database").
8.  After you apply all of the archive logs, bring the database online by calling
    `rdsadmin.complete_rollforward`. For more information, see [rdsadmin.complete_rollforward](db2-sp-managing-databases.md#db2-sp-complete-rollforward "db2-sp-managing-databases.md#db2-sp-complete-rollforward").
9.  Switch application connections to the RDS for Db2 server by either updating your
    application endpoints for the database or by updating the DNS endpoints to
    redirect traffic to the RDS for Db2 server. You can also use the Db2 automatic
    client reroute feature on your self-managed Db2 database with the RDS for Db2
    database endpoint. For more information, see [Automatic client reroute description and setup](https://www.ibm.com/docs/en/db2/11.5?topic=reroute-configuring-automatic-client "https://www.ibm.com/docs/en/db2/11.5?topic=reroute-configuring-automatic-client") in the IBM Db2
    documentation.
10. (Optional) Shut down your source database.
