# Working with storage in RDS for SQL Server

With RDS for SQL Server, you can attach up to three additional volumes to your RDS for SQL Server instance, each
mapped to a unique Windows drive letter. This allows you to distribute database files across
multiple volumes beyond the default `D:` drive. When you add a storage volume,
you get enhanced flexibility for database file management and storage optimization.

Benefits include:

- **Flexible file distribution** – Distribute
  database data files and log files across multiple volumes for improved I/O
  performance.
- **Storage optimization** – Use different
  storage types and configurations for different workload requirements.
- **Scalability** – Add storage capacity without
  modifying existing volumes.

###### On this page

- [Considerations for using additional storage volumes with RDS for SQL Server](#SQLServer.ASV.Considerations "#SQLServer.ASV.Considerations")
- [Add, remove, or modify storage volumes with RDS for SQL Server](#SQLServer.ASV.Management "#SQLServer.ASV.Management")
- [Restore operations for additional storage volumes with RDS for SQL Server](#SQLServer.ASV.Restore "#SQLServer.ASV.Restore")
- [Use cases for additional storage volumes with RDS for SQL Server](#SQLServer.ASV.UseCases "#SQLServer.ASV.UseCases")

## Considerations for using additional storage volumes with RDS for SQL Server

Take note of the following features and limitations when using additional storage
volumes with RDS for SQL Server:

- You can only add storage volumes on SQL Server Standard Edition (SE),
  Enterprise Edition (EE), and Developer Edition (DEV-EE).
- You can add up to 3 additional storage volumes per instance.
- Volume names are automatically mapped to Windows drive letters as
  follows:
  - `rdsdbdata2` – `H:` drive
  - `rdsdbdata3` – `I:` drive
  - `rdsdbdata4` – `J:` drive

- TempDB files continue to use the `T:` drive when using NVMe
  instance storage. SQL Server Audit files and Microsoft Business Intelligence
  (MSBI) files remain on the `D:` drive.
- You can only add General Purpose SSD (gp3) and Provisioned IOPS SSD (io2)
  storage types.
- The minimum storage size of additional storage volumes is the same as the
  limit set for the default `D:` drive. The
  maximum storage size for your DB instance is 256 TiB total across all volumes.
- Adding storage volumes to instances with read replicas or to read replica
  instances isn't supported.
- Adding storage volumes to instances enabled for cross-region automated backup
  isn't supported.
- Configuring additional storage volumes for storage autoscaling isn't
  supported.
- Moving files between volumes after creation isn't supported.
- You can't delete the `D:` volume, but you can delete other storage
  volumes as long as they're empty.
- Modifying the size of existing volumes during snapshot restore or
  point-in-time recovery (PITR) isn't supported. However, you can add
  new storage volumes during restore operations.

## Add, remove, or modify storage volumes with RDS for SQL Server

You can add, modify, and remove additional storage volumes using the AWS CLI or
AWS Management Console. All operations use the `modify-db-instance` API operation with the
`additional-storage-volumes` parameter.

###### Important

Adding or removing additional storage volumes creates a backup pending action and
a point-in-time restore blackout window. This window closes when the backup workflow
completes.

###### Topics

- [Adding storage volumes](#SQLServer.ASV.Adding "#SQLServer.ASV.Adding")
- [Scaling additional storage volumes](#SQLServer.ASV.Scaling "#SQLServer.ASV.Scaling")
- [Removing additional storage volumes](#SQLServer.ASV.Removing "#SQLServer.ASV.Removing")

### Adding storage volumes

You can add up to three storage volumes beyond the default `D:` drive.
To add a new storage volume to your RDS for SQL Server instance, use the
`modify-db-instance` command with the
`additional-storage-volumes` parameter.

The following example adds a new 4,000 GiB General Purpose SSD (gp3) volume named
`rdsdbdata4`.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-sql-server-instance` \
  --region `us-east-1` \
  --additional-storage-volumes '[{"VolumeName":"rdsdbdata4","StorageType":"gp3","AllocatedStorage":4000}]' \
  --apply-immediately
```

### Scaling additional storage volumes

You can modify any storage setting for your additional volumes except for storage
size. The following example modifies the IOPS setting for the
`rdsdbdata2` volume.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-sql-server-instance` \
  --region `us-east-1` \
  --additional-storage-volumes '[{"VolumeName":"rdsdbdata2","IOPS":4000}]' \
  --apply-immediately
```

### Removing additional storage volumes

You can't delete the `D:` volume, but you can delete other storage
volumes when they're empty.

###### Warning

Before you remove an additional storage volume, make sure that no database
files are stored on the volume.

The following example removes the `rdsdbdata4` volume.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-sql-server-instance` \
  --region `us-east-1` \
  --additional-storage-volumes '[{"VolumeName":"rdsdbdata4","SetForDelete":true}]' \
  --apply-immediately
```

## Restore operations for additional storage volumes with RDS for SQL Server

When you restore your database, you can add storage volumes. You can also modify the
storage settings of existing volumes.

###### Topics

- [Snapshot restore](#SQLServer.ASV.SnapshotRestore "#SQLServer.ASV.SnapshotRestore")
- [Point-in-time recovery](#SQLServer.ASV.PITR "#SQLServer.ASV.PITR")
- [Native database restore](#SQLServer.ASV.NativeRestore "#SQLServer.ASV.NativeRestore")

### Snapshot restore

When restoring from a snapshot, you can add new additional storage volumes or
modify the IOPS, throughput, and storage type settings of existing volumes.

The following example restores a DB instance from a snapshot and modifies the IOPS
setting for the `rdsdbdata2` volume:

```
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier `my-restored-instance` \
  --db-snapshot-identifier `my-snapshot` \
  --region `us-east-1` \
  --additional-storage-volumes '[{"VolumeName":"rdsdbdata2","IOPS":5000}]'
```

### Point-in-time recovery

During point-in-time recovery (PITR), you can add new additional storage volumes
with custom configurations.

The following example performs PITR and adds a new 5,000 GiB General Purpose SSD
(gp3) volume:

```
aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier `my-source-instance` \
  --target-db-instance `my-pitr-instance` \
  --use-latest-restorable-time \
  --region `us-east-1` \
  --additional-storage-volumes '[{"VolumeName":"rdsdbdata4","StorageType":"gp3","AllocatedStorage":5000,"IOPS":5000,"StorageThroughput":200}]'
```

### Native database restore

You can use the `rds_restore_database` stored procedure to restore
databases to specific additional storage volumes. Two new parameters support volume
selection:

**`data_file_volume`**

Specifies the drive letter for database data files

**`log_file_volume`**

Specifies the drive letter for database log files

The following example restores a database with data files on the `H:`
drive and log files on the `I:` drive:

```
EXEC msdb.dbo.rds_restore_database
    @restore_db_name='`my_database`',
    @s3_arn_to_restore_from='`arn:aws:s3:::my-bucket/backup-file.bak`',
    @data_file_volume=`'H:'`,
    @log_file_volume=`'I:'`;
```

If you don't specify volume parameters, or if you specify the `D:`
drive for both parameters, the database files are restored to the default
`D:` drive:

```
EXEC msdb.dbo.rds_restore_database
    @restore_db_name='`my_database`',
    @s3_arn_to_restore_from='`arn:aws:s3:::my-bucket/backup-file.bak`';
```

## Use cases for additional storage volumes with RDS for SQL Server

Additional storage volumes support various database management scenarios. The
following sections describe common use cases and implementation approaches.

###### Topics

- [Creating databases on additional storage volumes](#SQLServer.ASV.NewDatabase "#SQLServer.ASV.NewDatabase")
- [Extending storage capacity](#SQLServer.ASV.ExtendStorage "#SQLServer.ASV.ExtendStorage")
- [Moving databases between volumes](#SQLServer.ASV.MoveDatabase "#SQLServer.ASV.MoveDatabase")
- [Archiving data to cost-effective storage](#SQLServer.ASV.ArchiveData "#SQLServer.ASV.ArchiveData")

### Creating databases on additional storage volumes

You can create new databases directly on additional storage volumes using standard
SQL Server `CREATE DATABASE` statements.

The following example creates a database with data files on the `H:`
drive and log files on the `I:` drive:

```
CREATE DATABASE `MyDatabase`
ON (
    NAME = '`MyDatabase_Data`',
    FILENAME = '`H:\rdsdbdata\data\``MyDatabase_Data.mdf`',
    SIZE = 100MB,
    FILEGROWTH = 10MB
)
LOG ON (
    NAME = '`MyDatabase_Log`',
    FILENAME = '`I:\rdsdbdata\data\``MyDatabase_Log.ldf`',
    SIZE = 10MB,
    FILEGROWTH = 10%
);
```

### Extending storage capacity

When the default `D:` drive reaches its maximum capacity, you can add
additional storage volumes, scale existing volumes, and create new data files or log files on the new
volumes.

###### To extend storage capacity

1. Add a storage volume to your instance using the
   `modify-db-instance` command.
2. Add a new data file to the additional storage volume:

```
ALTER DATABASE `MyDatabase`
ADD FILE (
    NAME = '`MyDatabase_Data2`',
    FILENAME = '`H:\rdsdbdata\data\``MyDatabase_Data2.ndf`',
    SIZE = 500MB,
    FILEGROWTH = 50MB
);
```

### Moving databases between volumes

To move a database to a different volume, use the backup and restore approach with
the `rds_backup_database` and `rds_restore_database` stored
procedures. For more information, see [Using native backup and restore](SQLServer.Procedural.Importing.Native.md "SQLServer.Procedural.Importing.Native.md").

###### To move a database to a different volume

1. Back up the database using `rds_backup_database`:

```
EXEC msdb.dbo.rds_backup_database
    @source_db_name='`MyDatabase`',
    @s3_arn_to_backup_to='`arn:aws:s3:::my-bucket/database-backup.bak`';
```

2. Restore the database to the target volume:

```
EXEC msdb.dbo.rds_restore_database
    @restore_db_name='`MyDatabase_New`',
    @s3_arn_to_restore_from='`arn:aws:s3:::my-bucket/database-backup.bak`',
    @data_file_volume='`H:`',
    @log_file_volume='`I:`';
```

3. Drop the database from your old drive to release the
   space. For more information, see [Dropping a database in an Amazon RDS for Microsoft SQL Server DB instance](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md").

### Archiving data to cost-effective storage

For partitioned tables, you can archive older data to additional storage volumes
with different performance characteristics.

###### To archive partitioned data

1. Add a storage volume with appropriate storage type and capacity.
2. Create a new filegroup on the additional storage volume:

```
ALTER DATABASE `MyDatabase`
ADD FILEGROUP `ArchiveFileGroup`;

ALTER DATABASE `MyDatabase`
ADD FILE (
    NAME = '`Archive_Data`',
    FILENAME = '`H:\rdsdbdata\data\``Archive_Data.ndf`',
    SIZE = 1GB,
    FILEGROWTH = 100MB
) TO FILEGROUP `ArchiveFileGroup`;
```

3. Move partitions to the new filegroup using SQL Server partition management
   commands.
