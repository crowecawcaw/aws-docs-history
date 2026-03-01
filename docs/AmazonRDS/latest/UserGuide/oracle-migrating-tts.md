# Migrating using Oracle transportable tablespaces

You can use the Oracle transportable tablespaces feature to copy a set of tablespaces from
an on-premises Oracle database to an RDS for Oracle DB instance. At the physical level, you transfer
source data files and metadata files to your target DB instance using either Amazon EFS or Amazon S3. The
transportable tablespaces feature uses the `rdsadmin.rdsadmin_transport_util`
package. For syntax and semantics of this package, see [Transporting tablespaces](rdsadmin_transport_util.md "rdsadmin_transport_util.md").

For blog posts that explain how to transport tablespaces, see [Migrate
Oracle Databases to AWS using transportable tablespace](https://aws.amazon.com/blogs/database/migrate-oracle-databases-to-aws-using-transportable-tablespace/ "https://aws.amazon.com/blogs/database/migrate-oracle-databases-to-aws-using-transportable-tablespace/") and [Amazon RDS for Oracle
Transportable Tablespaces using RMAN](https://aws.amazon.com/blogs/database/amazon-rds-for-oracle-transportable-tablespaces-using-rman/ "https://aws.amazon.com/blogs/database/amazon-rds-for-oracle-transportable-tablespaces-using-rman/").

###### Topics

- [Overview of Oracle transportable tablespaces](#oracle-migrating-tts.overview "#oracle-migrating-tts.overview")
- [Phase 1: Set up your source host](#oracle-migrating-tts.setup-phase "#oracle-migrating-tts.setup-phase")
- [Phase 2: Prepare the full tablespace backup](#oracle-migrating-tts.initial-br-phase "#oracle-migrating-tts.initial-br-phase")
- [Phase 3: Make and transfer incremental backups](#oracle-migrating-tts.roll-forward-phase "#oracle-migrating-tts.roll-forward-phase")
- [Phase 4: Transport the tablespaces](#oracle-migrating-tts.final-br-phase "#oracle-migrating-tts.final-br-phase")
- [Phase 5: Validate the transported tablespaces](#oracle-migrating-tts.validate "#oracle-migrating-tts.validate")
- [Phase 6: Clean up leftover files](#oracle-migrating-tts.cleanup "#oracle-migrating-tts.cleanup")

## Overview of Oracle transportable tablespaces

A transportable tablespace set consists of data files for the set of tablespaces being
transported and an export dump file containing tablespace metadata. In a physical
migration solution such as transportable tablespaces, you transfer physical files: data
files, configuration files, and Data Pump dump files.

###### Topics

- [Advantages and disadvantages of transportable tablespaces](#oracle-migrating-tts.overview.benefits "#oracle-migrating-tts.overview.benefits")
- [Limitations for transportable tablespaces](#oracle-migrating-tts.limitations "#oracle-migrating-tts.limitations")
- [Prerequisites for transportable tablespaces](#oracle-migrating-tts.requirements "#oracle-migrating-tts.requirements")

### Advantages and disadvantages of transportable tablespaces

We recommend that you use transportable tablespaces when you need to migrate one
or more large tablespaces to RDS with minimum downtime. Transportable tablespaces
offer the following advantages over logical migration:

- Downtime is lower than most other Oracle migration solutions.
- Because the transportable tablespace feature copies only physical files,
  it avoids the data integrity errors and logical corruption that can occur in
  logical migration.
- No additional license is required.
- You can migrate a set of tablespaces across different platforms and
  endianness types, for example, from an Oracle Solaris platform to Linux.
  However, transporting tablespaces to and from Windows servers isn't
  supported.

###### Note

Linux is fully tested and supported. Not all UNIX variations have been
tested.

If you use transportable tablespaces, you can transport data using either Amazon S3 or
Amazon EFS:

- When you use EFS, your backups remain in the EFS file system for the
  duration of the import. You can remove the files afterward. In this
  technique, you don't need to provision EBS storage for your DB instance. For this
  reason, we recommend using Amazon EFS instead of S3. For more information, see
  [Amazon EFS integration](oracle-efs-integration.md "oracle-efs-integration.md").
- When you use S3, you download RMAN backups to EBS storage attached to your
  DB instance. The files remain in your EBS storage during the import. After the
  import, you can free up this space, which remains allocated to your
  DB instance.

The primary disadvantage of transportable tablespaces is that you need relatively
advanced knowledge of Oracle Database. For more information, see [Transporting Tablespaces Between Databases](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-F7B2B591-AA88-4D16-8DCF-712763923FFB "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-F7B2B591-AA88-4D16-8DCF-712763923FFB") in the _Oracle
Database Administrator’s Guide_.

### Limitations for transportable tablespaces

Oracle Database limitations for transportable tablespaces apply when you use this
feature in RDS for Oracle. For more information, see [Limitations on Transportable Tablespaces](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-DAB51E42-9BBC-4001-B5CB-0ECDBE128787 " https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-DAB51E42-9BBC-4001-B5CB-0ECDBE128787") and [General Limitations on Transporting Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-28800719-6CB9-4A71-95DD-4B61AA603173 "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/transporting-data.html#GUID-28800719-6CB9-4A71-95DD-4B61AA603173") in the _Oracle
Database Administrator’s Guide_. Note the following additional
limitations for transportable tablespaces in RDS for Oracle:

- Neither the source or target database can use Standard Edition 2 (SE2).
  Only Enterprise Edition is supported.
- You can't use an Oracle Database 11g database as a source. The RMAN
  cross-platform transportable tablespaces feature relies on the RMAN
  transport mechanism, which Oracle Database 11g doesn't support.
- You can't migrate data from an RDS for Oracle DB instance using transportable
  tablespaces. You can only use transportable tablespaces to migrate data to
  an RDS for Oracle DB instance.
- The Windows operating system isn't supported.
- You can't transport tablespaces into a database at a lower release level.
  The target database must be at the same or later release level as the source
  database. For example, you can’t transport tablespaces from Oracle Database
  21c into Oracle Database 19c.
- You can't transport administrative tablespaces such as `SYSTEM`
  and `SYSAUX`.
- You can't transport non-data objects such as PL/SQL packages, Java
  classes, views, triggers, sequences, users, roles, and temporary tables. To
  transport non-data objects, create them manually or use Data Pump metadata
  export and import. For more information, see [My Oracle Support Note 1454872.1](https://support.oracle.com/knowledge/Oracle%20Cloud/1454872_1.html "https://support.oracle.com/knowledge/Oracle%20Cloud/1454872_1.html").
- You can't transport tablespaces that are encrypted or use encrypted
  columns.
- If you transfer files using Amazon S3, the maximum supported file size is 5
  TiB.
- If the source database uses Oracle options such as Spatial, you can't
  transport tablespaces unless the same options are configured on the target
  database.
- You can't transport tablespaces into an RDS for Oracle DB instance in an Oracle
  replica configuration. As a workaround, you can delete all replicas,
  transport the tablespaces, and then recreate the replicas.

### Prerequisites for transportable tablespaces

Before you begin, complete the following tasks:

- Review the requirements for transportable tablespaces described in the
  following documents in My Oracle Support:
  - [Reduce Transportable Tablespace Downtime using Cross Platform
    Incremental Backup (Doc ID 2471245.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2471245.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=2471245.1")
  - [Transportable Tablespace (TTS) Restrictions and Limitations:
    Details, Reference, and Version Where Applicable (Doc ID
    1454872.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=1454872.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=1454872.1")
  - [Primary Note for Transportable Tablespaces (TTS) -- Common
    Questions and Issues (Doc ID 1166564.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=1166564.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=1166564.1")

- Plan for endianness conversion. If you specify the source platform ID,
  RDS for Oracle converts the endianness automatically. To learn how to find
  platform IDs, see [Data Guard Support for Heterogeneous Primary and Physical Standbys in
  Same Data Guard Configuration (Doc ID 413484.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=413484.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=413484.1").
- Make sure that the transportable tablespace feature is enabled on your
  target DB instance. The feature is enabled only if you don't get an
  `ORA-20304` error when you run the following query:

```
SELECT * FROM TABLE(rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files);
```

If the transportable tablespace feature isn't enabled, reboot your DB instance.
For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

- Make sure that the time zone file is the same in the source and target
  databases.
- Make sure that the database character sets on the source and target
  databases meet either of the following requirements:
  - The character sets are the same.
  - The character sets are compatible. For a list of compatibility
    requirements, see [General Limitations on Transporting Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/spmdu/general-limitations-on-transporting-data.html#GUID-28800719-6CB9-4A71-95DD-4B61AA603173 "https://docs.oracle.com/en/database/oracle/oracle-database/19/spmdu/general-limitations-on-transporting-data.html#GUID-28800719-6CB9-4A71-95DD-4B61AA603173") in the Oracle
    Database documentation.

- If you plan to transfer files using Amazon S3, do the following:
  - Make sure that an Amazon S3 bucket is available for file transfers, and
    that the Amazon S3 bucket is in the same AWS Region as your DB instance. For
    instructions, see [Create a bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the _Amazon Simple Storage Service Getting
    Started Guide_.
  - Prepare the Amazon S3 bucket for Amazon RDS integration by following the
    instructions in [Configuring IAM permissions for RDS for Oracle integration with Amazon S3](oracle-s3-integration.md "oracle-s3-integration.md").

- If you plan to transfer files using Amazon EFS, make sure that you have
  configured EFS according to the instructions in [Amazon EFS integration](oracle-efs-integration.md "oracle-efs-integration.md").
- We strongly recommend that you turn on automatic backups in your target
  DB instance. Because the [metadata import step](#oracle-migrating-tts.transport.import-dmp "#oracle-migrating-tts.transport.import-dmp") can potentially fail, it's important to be
  able to restore your DB instance to its state before the import, thereby avoiding
  the necessity to back up, transfer, and import your tablespaces
  again.

## Phase 1: Set up your source host

In this step, you copy the transport tablespaces scripts provided by My Oracle Support
and set up necessary configuration files. In the following steps, the _source
host_ is running the database that contains the tablespaces to be
transported to your _target instance_.

###### To set up your source host

1. Log in to your source host as the owner of your Oracle home.
2. Make sure that your `ORACLE_HOME` and `ORACLE_SID`
   environment variables point to your source database.
3. Log in to your database as an administrator, and verify that the time zone
   version, DB character set, and national character set are the same as in your
   target database.

```
SELECT * FROM V$TIMEZONE_FILE;
SELECT * FROM NLS_DATABASE_PARAMETERS
  WHERE PARAMETER IN ('NLS_CHARACTERSET','NLS_NCHAR_CHARACTERSET');
```

4. Set up the transportable tablespace utility as described in [Oracle Support note 2471245.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2471245.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=2471245.1").

The setup includes editing the `xtt.properties` file on
your source host. The following sample `xtt.properties` file
specifies backups of three tablespaces in the `/dsk1/backups`
directory. These are the tablespaces that you intend to transport to your target
DB instance. It also specifies the source platform ID to convert the endianness
automatically.

###### Note

For valid platform IDs, see [Data Guard Support for Heterogeneous Primary and Physical Standbys in
Same Data Guard Configuration (Doc ID 413484.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?id=413484.1 "https://support.oracle.com/epmos/faces/DocumentDisplay?id=413484.1").

```
#linux system
platformid=`13`
#list of tablespaces to transport
tablespaces=`TBS1,TBS2,TBS3`
#location where backup will be generated
src_scratch_location=`/dsk1/backups`
#RMAN command for performing backup
usermantransport=`1`
```

## Phase 2: Prepare the full tablespace backup

In this phase, you back up your tablespaces for the first time, transfer the backups
to your target host, and then restore them using the procedure
`rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces`. When this
phase is complete, the initial tablespace backups reside on your target DB instance and can be
updated with incremental backups.

###### Topics

- [Step 1: Back up the tablespaces on your source host](#oracle-migrating-tts.backup-full "#oracle-migrating-tts.backup-full")
- [Step 2: Transfer the backup files to your target DB instance](#oracle-migrating-tts.transfer-full "#oracle-migrating-tts.transfer-full")
- [Step 3: Import the tablespaces on your target DB instance](#oracle-migrating-tts.initial-tts-import "#oracle-migrating-tts.initial-tts-import")

### Step 1: Back up the tablespaces on your source host

In this step, you use the `xttdriver.pl` script to make a full
backup of your tablespaces. The output of `xttdriver.pl` is
stored in the `TMPDIR` environment variable.

###### To back up your tablespaces

1. If your tablespaces are in read-only mode, log in to your source database
   as a user with the `ALTER TABLESPACE` privilege, and place your
   tablespaces in read/write mode. Otherwise, skip to the next step.

The following example places `tbs1`, `tbs2`, and
`tbs3` in read/write mode.

```
ALTER TABLESPACE tbs1 READ WRITE;
ALTER TABLESPACE tbs2 READ WRITE;
ALTER TABLESPACE tbs3 READ WRITE;
```

2. Back up your tablespaces using the `xttdriver.pl`
   script. Optionally, you can specify `--debug` to run the script
   in debug mode.

```
export TMPDIR=`location_of_log_files`
cd `location_of_xttdriver.pl`
$ORACLE_HOME/perl/bin/perl xttdriver.pl --backup
```

### Step 2: Transfer the backup files to your target DB instance

In this step, copy the backup and configuration files from your scratch location
to your target DB instance. Choose one of the following options:

- If the source and target hosts share an Amazon EFS file system, use an
  operating system utility such as `cp` to copy your backup files
  and the `res.txt` file from your scratch location to a
  shared directory. Then skip to [Step 3: Import the tablespaces on your target DB instance](#oracle-migrating-tts.initial-tts-import "#oracle-migrating-tts.initial-tts-import").
- If you need to stage your backups to an Amazon S3 bucket, complete the
  following steps.

![Transfer files using either Amazon S3 or Amazon EFS.](images/oracle-tts.png)

#### Step 2.2: Upload the backups to your Amazon S3 bucket

Upload your backups and the `res.txt` file from your
scratch directory to your Amazon S3 bucket. For more information, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon Simple Storage Service User
Guide_.

#### Step 2.3: Download the backups from your Amazon S3 bucket to your target DB instance

In this step, you use the procedure
`rdsadmin.rdsadmin_s3_tasks.download_from_s3` to download your
backups to your RDS for Oracle DB instance.

###### To download your backups from your Amazon S3 bucket

1. Start SQL\*Plus or Oracle SQL Developer and log in to your RDS for Oracle
   DB instance.
2. Download the backups from the Amazon S3 bucket to your target DB instance by
   using the Amazon RDS procedure
   `rdsadmin.rdsadmin_s3_tasks.download_from_s3` to d. The
   following example downloads all of the files from an Amazon S3 bucket named
   `amzn-s3-demo-bucket` to the
   `DATA_PUMP_DIR`
   directory.

```
EXEC UTL_FILE.FREMOVE ('`DATA_PUMP_DIR`', 'res.txt');
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
  p_bucket_name    =>  '`amzn-s3-demo-bucket`',
  p_directory_name =>  '`DATA_PUMP_DIR`')
AS TASK_ID FROM DUAL;
```

The `SELECT` statement returns the ID of the task in a
`VARCHAR2` data type. For more information, see [Downloading files from an Amazon S3 bucket to an Oracle DB instance](oracle-s3-integration.md#oracle-s3-integration.using.download "oracle-s3-integration.md#oracle-s3-integration.using.download").

### Step 3: Import the tablespaces on your target DB instance

To restore your tablespaces to your target DB instance, use the procedure
`rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces`. This
procedure automatically converts the data files to the correct endian format.

If you import from a platform other than Linux, specify the source platform using
the parameter `p_platform_id` when you call
`import_xtts_tablespaces`. Make sure that the platform ID that you
specify matches the one specified in the `xtt.properties` file in
[Step 2: Export tablespace metadata on your source host](#oracle-migrating-tts.transport.export "#oracle-migrating-tts.transport.export").

###### Import the tablespaces on your target DB instance

1. Start an Oracle SQL client and log in to your target RDS for Oracle DB instance as the
   master user.
2. Run the procedure
   `rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces`,
   specifying the tablespaces to import and the directory containing the
   backups.

The following example imports the tablespaces `TBS1`,
`TBS2`, and `TBS3` from the directory
`DATA_PUMP_DIR`. The source platform is AIX-Based Systems
(64-bit), which has the platform ID of `6`. You can find the platform IDs by
querying `V$TRANSPORTABLE_PLATFORM`.

```
VAR task_id CLOB

BEGIN
  :task_id:=rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces(
        '`TBS1,TBS2,TBS3`',
        '`DATA_PUMP_DIR`',
        p_platform_id => 6);
END;
/

PRINT task_id
```

3. (Optional) Monitor progress by querying the table
   `rdsadmin.rds_xtts_operation_info`. The
   `xtts_operation_state` column shows the value
   `EXECUTING`, `COMPLETED`, or
   `FAILED`.

```
SELECT * FROM rdsadmin.rds_xtts_operation_info;
```

###### Note

For long-running operations, you can also query
`V$SESSION_LONGOPS`, `V$RMAN_STATUS`, and
`V$RMAN_OUTPUT`. 4. View the log of the completed import by using the task ID from the
previous step.

```
SELECT * FROM TABLE(rdsadmin.rds_file_util.read_text_file('BDUMP', 'dbtask-'||'&task_id'||'.log'));
```

Make sure that the import succeeded before continuing to the next
step.

## Phase 3: Make and transfer incremental backups

In this phase, you make and transfer incremental backups periodically while the source
database is active. This technique reduces the size of your final tablespace backup. If
you take multiple incremental backups, you must copy the `res.txt`
file after the last incremental backup before you can apply it on the target
instance.

The steps are the same as in [Phase 2: Prepare the full tablespace backup](#oracle-migrating-tts.initial-br-phase "#oracle-migrating-tts.initial-br-phase"), except that the import step
is optional.

## Phase 4: Transport the tablespaces

In this phase, you back up your read-only tablespaces and export Data Pump metadata,
transfer these files to your target host, and import both the tablespaces and the
metadata.

###### Topics

- [Step 1: Back up your read-only tablespaces](#oracle-migrating-tts.final-backup "#oracle-migrating-tts.final-backup")
- [Step 2: Export tablespace metadata on your source host](#oracle-migrating-tts.transport.export "#oracle-migrating-tts.transport.export")
- [Step 3: (Amazon S3 only) Transfer the backup and export files to your target DB instance](#oracle-migrating-tts.transport "#oracle-migrating-tts.transport")
- [Step 4: Import the tablespaces on your target DB instance](#oracle-migrating-tts.restore-full "#oracle-migrating-tts.restore-full")
- [Step 5: Import tablespace metadata on your target DB instance](#oracle-migrating-tts.transport.import-dmp "#oracle-migrating-tts.transport.import-dmp")

### Step 1: Back up your read-only tablespaces

This step is identical to [Step 1: Back up the tablespaces on your source host](#oracle-migrating-tts.backup-full "#oracle-migrating-tts.backup-full"), with one key difference: you
place your tablespaces in read-only mode before backing up your tablespaces for the
last time.

The following example places `tbs1`, `tbs2`, and
`tbs3` in read-only mode.

```
ALTER TABLESPACE tbs1 READ ONLY;
ALTER TABLESPACE tbs2 READ ONLY;
ALTER TABLESPACE tbs3 READ ONLY;
```

### Step 2: Export tablespace metadata on your source host

Export your tablespace metadata by running the `expdb` utility
on your source host. The following example exports tablespaces
`TBS1`, `TBS2`, and
`TBS3` to dump file
`xttdump.dmp` in directory
`DATA_PUMP_DIR`.

```
expdp `username`/`pwd` \
dumpfile=`xttdump.dmp` \
directory=`DATA_PUMP_DIR` \
statistics=NONE \
transport_tablespaces=`TBS1`,`TBS2`,`TBS3` \
transport_full_check=y \
logfile=`tts_export.log`
```

If `DATA_PUMP_DIR` is a shared directory in Amazon EFS, skip
to [Step 4: Import the tablespaces on your target DB instance](#oracle-migrating-tts.restore-full "#oracle-migrating-tts.restore-full").

### Step 3: (Amazon S3 only) Transfer the backup and export files to your target DB instance

If you are using Amazon S3 to stage your tablespace backups and Data Pump export file,
complete the following steps.

#### Step 3.1: Upload the backups and dump file from your source host to your Amazon S3 bucket

Upload your backup and dump files from your source host to your Amazon S3 bucket.
For more information, see [Uploading
objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon Simple Storage Service User Guide_.

#### Step 3.2: Download the backups and dump file from your Amazon S3 bucket to your target DB instance

In this step, you use the procedure
`rdsadmin.rdsadmin_s3_tasks.download_from_s3` to download your
backups and dump file to your RDS for Oracle DB instance. Follow the steps in [Step 2.3: Download the backups from your Amazon S3 bucket to your target DB instance](#oracle-migrating-tts.download-full "#oracle-migrating-tts.download-full").

### Step 4: Import the tablespaces on your target DB instance

Use the procedure
`rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces` to restore
the tablespaces. For syntax and semantics of this procedure, see [Importing transported tablespaces to your DB instance](rdsadmin_transport_util_import_xtts_tablespaces.md "rdsadmin_transport_util_import_xtts_tablespaces.md")

###### Important

After you complete your final tablespace import, the next step is [importing the Oracle Data
Pump metadata](#oracle-migrating-tts.transport.export "#oracle-migrating-tts.transport.export"). If the import fails, it's important to return your
DB instance to its state before the failure. Thus, we recommend that you create a DB
snapshot of your DB instance by following the instructions in [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md"). The
snapshot will contain all imported tablespaces, so if the import fails, you
don’t need to repeat the backup and import process.

If your target DB instance has automatic backups turned on, and Amazon RDS doesn't detect
that a valid snapshot was initiated before you import the metadata, RDS attempts
to create a snapshot. Depending on your instance activity, this snapshot might
or might not succeed. If a valid snapshot isn't detected or a snapshot can't be
initiated, the metadata import exits with errors.

###### Import the tablespaces on your target DB instance

1. Start an Oracle SQL client and log in to your target RDS for Oracle DB instance as the
   master user.
2. Run the procedure
   `rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces`,
   specifying the tablespaces to import and the directory containing the
   backups.

The following example imports the tablespaces
`TBS1`, `TBS2`, and
`TBS3` from the directory
`DATA_PUMP_DIR`.

```
BEGIN
  :task_id:=rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces('`TBS1,TBS2,TBS3`','`DATA_PUMP_DIR`');
END;
/
PRINT task_id
```

3. (Optional) Monitor progress by querying the table
   `rdsadmin.rds_xtts_operation_info`. The
   `xtts_operation_state` column shows the value
   `EXECUTING`, `COMPLETED`, or
   `FAILED`.

```
SELECT * FROM rdsadmin.rds_xtts_operation_info;
```

###### Note

For long-running operations, you can also query
`V$SESSION_LONGOPS`, `V$RMAN_STATUS`, and
`V$RMAN_OUTPUT`. 4. View the log of the completed import by using the task ID from the
previous step.

```
SELECT * FROM TABLE(rdsadmin.rds_file_util.read_text_file('BDUMP', 'dbtask-'||'&task_id'||'.log'));
```

Make sure that the import succeeded before continuing to the next
step. 5. Take a manual DB snapshot by following the instructions in [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").

### Step 5: Import tablespace metadata on your target DB instance

In this step, you import the transportable tablespace metadata into your RDS for Oracle
DB instance using the procedure
`rdsadmin.rdsadmin_transport_util.import_xtts_metadata`. For syntax
and semantics of this procedure, see [Importing transportable tablespace metadata into your DB instance](rdsadmin_transport_util_import_xtts_metadata.md "rdsadmin_transport_util_import_xtts_metadata.md"). During the
operation, the status of the import is shown in the table
`rdsadmin.rds_xtts_operation_info`.

###### Important

Before you import metadata, we strongly recommend that you confirm that a DB
snapshot was successfully created after you imported your tablespaces. If the
import step fails, restore your DB instance, address the import errors, and then
attempt the import again.

###### Import the Data Pump metadata into your RDS for Oracle DB instance

1. Start your Oracle SQL client and log in to your target DB instance as the master
   user.
2. Create the users that own schemas in your transported tablespaces, if
   these users don't already exist.

```
CREATE USER `tbs_owner` IDENTIFIED BY `password`;
```

3. Import the metadata, specifying the name of the dump file and its
   directory location.

```
BEGIN
  rdsadmin.rdsadmin_transport_util.import_xtts_metadata('`xttdump.dmp`','`DATA_PUMP_DIR`');
END;
/
```

4. (Optional) Query the transportable tablespace history table to see the
   status of the metadata import.

```
SELECT * FROM rdsadmin.rds_xtts_operation_info;
```

When the operation completes, your tablespaces are in read-only
mode. 5. (Optional) View the log file.

The following example lists the contents of the BDUMP directory and then
queries the import log.

```
SELECT * FROM TABLE(rdsadmin.rds_file_util.listdir(p_directory => 'BDUMP'));

SELECT * FROM TABLE(rdsadmin.rds_file_util.read_text_file(
  p_directory => 'BDUMP',
  p_filename => 'rds-xtts-import_xtts_metadata-2023-05-22.01-52-35.560858000.log'));
```

## Phase 5: Validate the transported tablespaces

In this optional step, you validate your transported tablespaces using the procedure
`rdsadmin.rdsadmin_rman_util.validate_tablespace`, and then place your
tablespaces in read/write mode.

###### To validate the transported data

1. Start SQL\*Plus or SQL Developer and log in to your target DB instance as the master
   user.
2. Validate the tablespaces using the procedure
   `rdsadmin.rdsadmin_rman_util.validate_tablespace`.

```
SET SERVEROUTPUT ON
BEGIN
    rdsadmin.rdsadmin_rman_util.validate_tablespace(
        p_tablespace_name     => '`TBS1`',
        p_validation_type     => 'PHYSICAL+LOGICAL',
        p_rman_to_dbms_output => TRUE);
    rdsadmin.rdsadmin_rman_util.validate_tablespace(
        p_tablespace_name     => '`TBS2`',
        p_validation_type     => 'PHYSICAL+LOGICAL',
        p_rman_to_dbms_output => TRUE);
    rdsadmin.rdsadmin_rman_util.validate_tablespace(
        p_tablespace_name     => '`TBS3`',
        p_validation_type     => 'PHYSICAL+LOGICAL',
        p_rman_to_dbms_output => TRUE);
END;
/
```

3. Place your tablespaces in read/write mode.

```
ALTER TABLESPACE `TBS1` READ WRITE;
ALTER TABLESPACE `TBS2` READ WRITE;
ALTER TABLESPACE `TBS3` READ WRITE;
```

## Phase 6: Clean up leftover files

In this optional step, you remove any unneeded files. Use the
`rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files` procedure to
list data files that were orphaned after a tablespace import, and then use
`rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files` procedure to
delete them. For syntax and semantics of these procedures, see [Listing orphaned files after a tablespace import](rdsadmin_transport_util_list_xtts_orphan_files.md "rdsadmin_transport_util_list_xtts_orphan_files.md") and [Deleting orphaned data files after a tablespace import](rdsadmin_transport_util_cleanup_incomplete_xtts_import.md "rdsadmin_transport_util_cleanup_incomplete_xtts_import.md").

###### To clean up leftover files

1. Remove old backups in `DATA_PUMP_DIR` as
   follows:
   1. List the backup files by running
      `rdsadmin.rdsadmin_file_util.listdir`.

   ```
   SELECT * FROM TABLE(rdsadmin.rds_file_util.listdir(p_directory => '`DATA_PUMP_DIR`'));
   ```

   2. Remove the backups one by one by calling
      `UTL_FILE.FREMOVE`.

   ```
   EXEC UTL_FILE.FREMOVE ('`DATA_PUMP_DIR`', '`backup_filename`');
   ```

2. If you imported tablespaces but didn't import metadata for these tablespaces,
   you can delete the orphaned data files as follows:
   1. List the orphaned data files that you need to delete. The following
      example runs the procedure
      `rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files`.

   ```
   SQL> SELECT * FROM TABLE(rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files);

   FILENAME       FILESIZE
   -------------- ---------
   datafile_7.dbf 104865792
   datafile_8.dbf 104865792
   ```

   2. Delete the orphaned files by running the procedure
      `rdsadmin.rdsadmin_transport_util.cleanup_incomplete_xtts_import`.

   ```
   BEGIN
     rdsadmin.rdsadmin_transport_util.cleanup_incomplete_xtts_import('`DATA_PUMP_DIR`');
   END;
   /
   ```

   The cleanup operation generates a log file that uses the name format
   `rds-xtts-delete_xtts_orphaned_files-`YYYY-MM-DD.HH24-MI-SS.FF`.log`
   in the `BDUMP` directory. 3. Read the log file generated in the previous step. The following
   example reads log
   `rds-xtts-delete_xtts_orphaned_files-`2023-06-01.09-33-11.868894000`.log`.

   ```
   SELECT *
   FROM TABLE(rdsadmin.rds_file_util.read_text_file(
          p_directory => 'BDUMP',
          p_filename  => 'rds-xtts-delete_xtts_orphaned_files-`2023-06-01.09-33-11.868894000`.log'));

   TEXT
   --------------------------------------------------------------------------------
   orphan transported datafile datafile_7.dbf deleted.
   orphan transported datafile datafile_8.dbf deleted.
   ```

3. If you imported tablespaces and imported metadata for these tablespaces, but
   you encountered compatibility errors or other Oracle Data Pump issues, clean up
   the partially transported data files as follows:
   1. List the tablespaces that contain partially transported data files by
      querying `DBA_TABLESPACES`.

   ```
   SQL> SELECT TABLESPACE_NAME FROM DBA_TABLESPACES WHERE PLUGGED_IN='YES';

   TABLESPACE_NAME
   --------------------------------------------------------------------------------
   TBS_3
   ```

   2. Drop the tablespaces and the partially transported data files.

   ```
   DROP TABLESPACE `TBS_3` INCLUDING CONTENTS AND DATAFILES;
   ```
