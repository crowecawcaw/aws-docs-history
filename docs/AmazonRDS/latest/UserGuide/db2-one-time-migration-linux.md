# Migrating from Linux to Linux for Amazon RDS for Db2

With this migration approach, you back up your self-managed Db2 database to an Amazon S3
bucket. Then, you use Amazon RDS stored procedures to restore your Db2 database to an
Amazon RDS for Db2 DB instance. For more information about using Amazon S3, see [Integrating an Amazon RDS for Db2 DB instance with
Amazon S3](db2-s3-integration.md "db2-s3-integration.md").

Backup and restore for RDS for Db2 follows the IBM Db2 supported upgrade paths and
restrictions. For more information, see [Supported upgrade paths for Db2 servers](https://www.ibm.com/docs/en/db2/11.5?topic=servers-supported-upgrade-paths-db2 "https://www.ibm.com/docs/en/db2/11.5?topic=servers-supported-upgrade-paths-db2") and [Upgrade
restrictions for Db2 servers](https://www.ibm.com/docs/en/db2/11.5?topic=servers-upgrade-restrictions "https://www.ibm.com/docs/en/db2/11.5?topic=servers-upgrade-restrictions") in the IBM Db2 documentation.

###### Topics

- [Limitations and recommendations for
  using native restore](#db2-linux-migration-limitations "#db2-linux-migration-limitations")
- [Backing up your database to Amazon S3](#db2-linux-backing-up-database "#db2-linux-backing-up-database")
- [Creating a default automatic
  storage group](#db2-linux-creating-auto-storage-group "#db2-linux-creating-auto-storage-group")
- [Restoring your Db2 database](#db2-linux-restoring-db2-database "#db2-linux-restoring-db2-database")

## Limitations and recommendations for

using native restore

The following limitations and recommendations apply to using native restore:

- Amazon RDS only supports migrating on-premises versions of Db2 that match supported
  RDS for Db2 versions. For more information about the supported versions, see [Supported Db2 minor versions on
  Amazon RDS](Db2.Concepts.md#Db2.Concepts.VersionMgmt.Supported "Db2.Concepts.md#Db2.Concepts.VersionMgmt.Supported").
- Amazon RDS only supports offline and online backups for native restore. Amazon RDS
  doesn't support incremental or Delta backups.
- You can't restore from an Amazon S3 bucket in an AWS Region that is different
  from the Region where your RDS for Db2 DB instance is located.
- Amazon S3 limits the size of files that are uploaded to an Amazon S3 bucket to 5 TB. If
  your database backup file exceeds 5 TB, then split the backup file into smaller
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
  Upload any backup files that you want to migrate to Amazon RDS. We recommend that you
  use offline backups for migrations that can handle downtime. If you already have
  an S3 bucket, you can use that bucket. If you don't have an S3 bucket, see
  [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

###### Note

If your database is large and would take a long time to transfer to an S3
bucket, you can order an AWS Snow Family device and ask AWS to perform
the backup. After you copy your files to the device and return it to the
Snow Family team, the team transfers your backed-up images to your S3
bucket. For more information, see the [AWS Snow Family documentation](../../../snowball.md "../../../snowball.md").

- _An IAM role to access the S3 bucket_: If
  you already have an IAM role, you can use that role. If you don't have a role,
  see [Step 2: Create an IAM role and attach your
  IAM policy](db2-s3-integration.md#db2-creating-iam-role "db2-s3-integration.md#db2-creating-iam-role").
- _An IAM policy with trust relationships and
  permissions attached to your IAM role_: For more information,
  see [Step 1: Create an IAM policy](db2-s3-integration.md#db2-creating-iam-policy "db2-s3-integration.md#db2-creating-iam-policy").
- _The IAM role added to your RDS for Db2 DB
  instance_: For more information, see [Step 3: Add your IAM role to your RDS for Db2 DB
  instance](db2-s3-integration.md#db2-adding-iam-role "db2-s3-integration.md#db2-adding-iam-role").

## Creating a default automatic

storage group

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

4. Deactivate the database and stop all database services. In the following
   example, replace `source_database` with the name of the
   database that you created the storage group for.

```
db2 deactivate db `source_database`
```

5. Back up the database. In the following example, replace
   `source_database` with the name of the database
   that you created the storage group for. Replace
   `file_system_path` with the absolute path to where
   you want to back up the database.

```
db2 backup database `source_database` to `file_system_path`
```

## Restoring your Db2 database

After you back up your database on Amazon S3 and create an automatic storage group, you are
ready to restore your Db2 database to your RDS for Db2 DB instance.

###### To restore your Db2 database from your Amazon S3 bucket to your RDS for Db2 DB

instance

1.  Connect to your RDS for Db2 DB instance. For more information, see [Connecting to your Db2 DB instance](USER_ConnectToDb2DBInstance.md "USER_ConnectToDb2DBInstance.md").
2.  (Optional) To ensure that your database is configured with the optimal
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

3.  Restore your database by calling `rdsadmin.restore_database`. For
    more information, see [rdsadmin.restore_database](db2-sp-managing-databases.md#db2-sp-restore-database "db2-sp-managing-databases.md#db2-sp-restore-database").
