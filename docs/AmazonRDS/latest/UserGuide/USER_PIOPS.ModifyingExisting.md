# Adding storage volumes

For RDS for Oracle and RDS for SQL Server DB instances, you can add up to three storage volumes to increase your
total storage capacity up to 256 TiB per instance. Additional storage volumes allow
you to use different storage types (gp3 and io2) to optimize costs and performance
based on your data access patterns.

###### Note

For RDS for Oracle DB instances, you can add a storage volume with the
minimum storage size of 200 GiB.

You can add, modify, or remove additional storage volumes using the AWS Management
Console or AWS CLI. You can configure the volumes with different allocated
storage, IOPS, and throughput settings. For example, you might place
high-performance data on an io2 volume and historical data on a gp3 volume.

The additional volumes must use the volume names shown in the following table.

| RDS for Oracle volume name | RDS for SQL Server volume name |
| -------------------------- | ------------------------------ |
| `rdsdbdata2`               | `H:`                           |
| `rdsdbdata3`               | `I:`                           |
| `rdsdbdata4`               | `J:`                           |

###### To add an additional storage volume to a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the DB instance that you want to modify.
4. Choose **Modify**.
5. In the **Storage** section, choose **Add additional storage volume**.
6. Configure the additional storage volume:
   - **Volume name** – Choose `rdsdbdata2`,
     `rdsdbdata3`, or
     `rdsdbdata4`.
   - **Storage type** – Choose **General Purpose SSD
     (gp3)** or **Provisioned IOPS SSD
     (io2)**.
   - **Allocated storage** – Enter the storage size in GiB (minimum
     200 GiB).
   - For io2 storage, configure **Provisioned IOPS**.
   - For gp3 storage, optionally configure **Storage throughput**.

7. Choose **Continue**.
8. When the settings are as you want them, choose **Modify DB
   instance**.

###### Important

When you are adding an additional storage volume using the
`modify-db-instance` operation, the RDS adds the storage
volume immediately regardless of the `--no-apply-immediately`
parameter. If you have other modifications in the request, RDS applies
them based on the schedule modifications. See [Using the schedule modifications
setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

To add an additional storage volume to a DB instance, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the
`--additional-storage-volumes` as a JSON array specifying the
additional storage volumes to add or modify.

The following example adds an additional storage volume named `rdsdbdata2`
with 5000 GiB of gp3 storage to `mydbinstance`.

When you add an additional storage volume, RDS applies the change
immediately regardless of the `--no-apply-immediately`
parameter.

```
aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --additional-storage-volumes '[
        {
            "VolumeName": "rdsdbdata2",
            "StorageType": "gp3",
            "AllocatedStorage": 5000,
            "StorageThroughput": 725
        }
    ]'
```

To add an additional storage volume to a DB instance, use the Amazon RDS API operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the
`AdditionalStorageVolumes` parameter as an array of
additional storage volume specifications.

When you are adding an additional storage volume using the
ModifyDBInstance API operation, RDS adds the storage volume immediately
regardless of the `ApplyImmediately` option being True or
False.
