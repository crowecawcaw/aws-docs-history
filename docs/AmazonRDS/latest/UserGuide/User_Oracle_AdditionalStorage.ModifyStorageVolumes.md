# Add, remove, or modify storage volumes with RDS for Oracle

You can add, modify, and remove additional storage volumes using the AWS Management Console or AWS CLI.
All operations use the `modify-db-instance` command with the `additional-storage-volumes` parameter.

###### Important

Adding or removing additional storage volumes creates a backup pending action and a blackout window.
The blackout window closes when the backup workflow completes.

## Adding storage volumes

You can add up to three storage volumes beyond the primary storage volume.
To add a new storage volume to your RDS for Oracle DB instance, use the `modify-db-instance` command with the
`additional-storage-volumes` parameter.

The following code snippet adds a mew 5,000 GiB general purpose SSD (gp3) volume with 4000 provision IOPS name `rdsdbdata3`.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-oracle-instance` \
  --region us-east-1 \
  --additional-storage-volumes '[
        {
            "VolumeName":"rdsdbdata3",
            "StorageType":"gp3",
            "AllocatedStorage":5000
            "IOPS":4000}
    ]' \
  --apply-immediately
```

## Modifying storage volumes

You can modify storage type, allocated storage size, IOPS, and storage throughput settings of your
additional storage volume. The following code snippet modifies the IOPS setting for the `rdsdbdata2`
volume.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-oracle-instance` \
  --region us-east-1 \
  --additional-storage-volumes '[
        {
            "VolumeName":"rdsdbdata2",
            "IOPS":8000}
    ]' \
  --apply-immediately
```

###### Note

You can’t reduce the storage allocation for an additional storage volume once you’ve added it to the instance.

## Removing storage volumes

You can remove additional storage volumes from RDS for Oracle DB instances when they are no longer needed.
Before removing a volume, make sure that you have moved all database files from the volume
and no database objects are referencing it. Verify that the volume status is `Not-in-use`.
You can remove additional storage volumes, but you can't remove the primary storage volume.

###### Warning

Before you remove an additional storage volume, make sure that no database files
are stored on the volume. Removing a volume with active database files
causes database corruption.

The following example removes the `rdsdbdata4` volume.

```
aws rds modify-db-instance \
  --db-instance-identifier `my-oracle-instance` \
  --region us-east-1 \
  --additional-storage-volumes '[
        {
            "VolumeName":"rdsdbdata2",
            "SetForDelete":true}
    ]' \
  --apply-immediately
```
