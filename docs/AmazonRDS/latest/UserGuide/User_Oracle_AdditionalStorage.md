# Backing up and restoring data with additional storage volumes in RDS for Oracle

You can use automated backups and create a DB snapshot with your DB instance with additional storage volumes.
All backup operations include both the primary volume and additional storage volumes.
You can also use point-in-time recovery for your DB instance with additional storage volumes.
When you restore your database, you can add storage volumes.
You can also modify the storage settings of existing volumes. You cannot delete
additional storage volumes when you restore your database from a snapshot.

###### Topics

- [Creating manual snapshots](#User_Oracle_AdditionalStorage.BackupRestore.ManualSnapshots "#User_Oracle_AdditionalStorage.BackupRestore.ManualSnapshots")
- [Restoring manual snapshots](#User_Oracle_AdditionalStorage.BackupRestore.RestoreSnapshots "#User_Oracle_AdditionalStorage.BackupRestore.RestoreSnapshots")
- [Point-in-time recovery](#User_Oracle_AdditionalStorage.BackupRestore.PitR "#User_Oracle_AdditionalStorage.BackupRestore.PitR")

## Creating manual snapshots

The following example creates a manual snapshot of your database with additional storage volumes:

```
aws rds create-db-snapshot \
--db-instance-identifier `my-oracle-asv-instance` \
--db-snapshot-identifier `my-snapshot`
```

## Restoring manual snapshots

When restoring from a snapshot, you can add new additional storage volumes or modify
the IOPS or throughput settings of existing volumes.
The following example restores a DB instance from a snapshot and modifies the IOPS setting for the `rdsdbdata2` volume:

```
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier `my-restored-instance` \
  --db-snapshot-identifier `my-snapshot` \
  --region us-east-1 \
  --additional-storage-volumes '[
        {
            "VolumeName":"rdsdbdata2",
            "IOPS":5000
        }
    ]'
```

## Point-in-time recovery

During point-in-time recovery (PITR), you can add new additional storage volumes with custom configurations.
The following example performs PITR and adds a new 5,000 GiB General Purpose SSD (gp3) with
5000 IOPS and 200 MB/s storage throughput for the `rdsdbdata2` volume:

```
aws rds restore-db-instance-to-point-in-time \
  --source-db-instance-identifier `my-source-instance`my-source-instance \
  --target-db-instance `my-pitr-instance`\
  --use-latest-restorable-time \
  --region us-east-1 \
  --additional-storage-volumes '[
        {
            "VolumeName":"rdsdbdata2",
            "StorageType":"gp3",
            "AllocatedStorage":5000,
            "IOPS":5000,
            "StorageThroughput":200
        }
    ]'
```
