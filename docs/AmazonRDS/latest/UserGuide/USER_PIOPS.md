# Using a dedicated log volume (DLV)

You can use a dedicated log volume (DLV) for a DB instance that uses Provisioned IOPS (PIOPS) storage. A DLV moves PostgreSQL
database transaction logs and MySQL/MariaDB redo logs and binary logs to a storage volume that's separate from the volume
containing the database tables. A DLV makes transaction write logging more efficient and consistent. DLVs are ideal for
databases with large allocated storage, high I/O per second (IOPS) requirements, or latency-sensitive workloads.

DLVs are supported for PIOPS storage (io1 and io2 Block Express) and are created with a fixed size of 1,024 GiB and 3,000 Provisioned IOPS.

Amazon RDS supports DLVs in all AWS Regions for the following versions:

- MariaDB 10.6.7 and higher 10 versions
- MySQL 8.0.28 and higher 8.0 versions, MySQL 8.4.3 and higher 8.4 versions
- PostgreSQL 13.10 and higher 13 versions, 14.7 and higher 14 versions, and 15.2 and higher 15 versions
  RDS supports DLVs with Multi-AZ deployments. When you modify or create a Multi-AZ instance, a DLV is created for both the
  primary and the secondary.

RDS supports DLVs with read replicas. If the primary DB instance has a DLV enabled, all read replicas created after enabling DLV
will also have a DLV. Any read replicas created before the switch to DLV will not have it enabled unless explicitly modified to do so.
We recommend all read replicas attached to a primary instance before DLV was enabled also be manually modified to have A DLV.

###### Note

We recommend DLVs for database configurations of 5 TiB or greater.

For more information on the benefits of DLVs, see the following blog posts:

- [Enhance
  database performance with Amazon RDS dedicated log volumes](https://aws.amazon.com/blogs/database/enhance-database-performance-with-amazon-rds-dedicated-log-volumes/ "https://aws.amazon.com/blogs/database/enhance-database-performance-with-amazon-rds-dedicated-log-volumes/")
- [Benchmark
  Amazon RDS for PostgreSQL with dedicated log volumes](https://aws.amazon.com/blogs/database/benchmark-amazon-rds-for-postgresql-with-dedicated-log-volumes/ "https://aws.amazon.com/blogs/database/benchmark-amazon-rds-for-postgresql-with-dedicated-log-volumes/")
- [Maximizing performance of AWS
  RDS for MySQL with dedicated log volumes](https://www.percona.com/blog/maximizing-performance-of-aws-rds-for-mysql-with-dedicated-log-volumes/ "https://www.percona.com/blog/maximizing-performance-of-aws-rds-for-mysql-with-dedicated-log-volumes/") in the Percona documentation
  For information on the ranges of allocated storage, Provisioned IOPS, and storage throughput available for each database engine, see
  [Provisioned IOPS SSD storage](CHAP_Storage.md#USER_PIOPS "CHAP_Storage.md#USER_PIOPS").

###### Topics

- [Considerations when enabling and
  disabling DLV](#USER_PIOPS.dlv.considerations "#USER_PIOPS.dlv.considerations")
- [Enabling DLV when you create a DB instance](#USER_PIOPS.create-dlv "#USER_PIOPS.create-dlv")
- [Enabling DLV on an existing DB instance](#USER_PIOPS.modify-dlv "#USER_PIOPS.modify-dlv")
- [Monitoring DLV storage](#USER_PIOPS.dlv.monitoring "#USER_PIOPS.dlv.monitoring")

## Considerations when enabling and

disabling DLV

Enabling and disabling DLV can be time consuming and cause downtime. The process
involves copying all transaction logs or redo and binary logs (depending on the
database engine) to the new volume when enabling, or back to the original storage
when disabling. The duration of this operation is influenced by several
factors:

- Number of transaction logs:
  - Larger databases with more transactions generate more logs,
    increasing the time required for copying.
  - Transaction logs can accumulate on the primary DB instance if
    replication slots are inactive or if replication is lagging,
    increasing the time required for copying. Make sure that replication
    is current, and remove any unnecessary slots.

- Storage configuration:
  - DB instance EBS bandwidth – Higher bandwidth allows for
    faster data transfer.
  - Number of Provisioned IOPS – More input/output operations
    per second (IOPS) can speed up the copying process.

- Database activity – High levels of database activity during
  configuration can slow down the process.

To minimize downtime, we recommend that you plan and schedule during periods of
low activity or maintenance windows.

## Enabling DLV when you create a DB instance

You can use the AWS Management Console, AWS CLI, or RDS API to create a DB instance with DLV enabled.

###### To enable DLV on a new DB instance

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  Choose **Create database**.
3.  On the **Create DB instance page**, choose a DB engine that supports DLV.
4.  For **Storage**:

        1. Choose either **Provisioned IOPS SSD (io1)** or **Provisioned IOPS SSD
         (io2)**.
        2. Enter the **Allocated storage** and **Provisioned IOPS** that
         you want.
        3. Expand **Dedicated Log Volume**, then select **Turn on Dedicated Log
         Volume**.

    ![Enabling DLV on a new DB instance.](images/enable-dlv.png)

5.  Choose other settings as needed.
6.  Choose **Create database**.
    After the database is created, the value for Dedicated Log Volume appears on the **Configuration** tab of the database details page.

To enable DLV when you create a DB instance using Provisioned IOPS storage, use the AWS CLI command [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md"). Set the following parameters:

- `--dedicated-log-volume` – Enables a dedicated
  log volume.
- `--storage-type` – Set to `io1` or `io2` for Provisioned
  IOPS.
- `--allocated-storage` – Amount of storage to be allocated for the DB instance, in
  gibibytes.
- `--iops` – The amount of Provisioned IOPS for the DB instance, expressed in I/O
  operations per second.
  To enable DLV when you create a DB instance using Provisioned IOPS storage, use the Amazon RDS API operation [CreateDBInstance](../APIReference/API_CretaeDBInstance.md "../APIReference/API_CretaeDBInstance.md"). Set the following parameters:

- `DedicatedLogVolume` – Set to `true`
  to enable a dedicated log volume.
- `StorageType` – Set to `io1` or `io2` for Provisioned IOPS.
- `AllocatedStorage` – Amount of storage to be allocated for the DB instance, in
  gibibytes.
- `Iops` – The IOPS rate for the DB instance, expressed in I/O operations per
  second.

## Enabling DLV on an existing DB instance

You can use the AWS Management Console, AWS CLI, or RDS API to modify a DB instance to enable DLV.

After you modify the DLV setting for a DB instance, you must reboot the DB instance.

###### To enable DLV on an existing DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.

To filter the list of DB instances, for **Filter databases** enter a text string for
Amazon RDS to use to filter the results. Only DB instances whose names contain the string appear. 3. Choose the DB instance with Provisioned IOPS storage that you want to modify. 4. Choose **Modify**. 5. On the **Modify DB instance page**:

    1. For **Storage**, expand **Dedicated Log Volume**, then select
     **Turn on Dedicated Log Volume**.

6. Choose **Continue**.
7. Choose **Apply immediately** to apply the changes to the DB instance immediately. Or
   choose **Apply during the next scheduled maintenance window** to apply the changes during
   the next maintenance window.
8. Review the parameters to be changed, and choose **Modify DB instance** to complete the
   modification.
   The new value for Dedicated Log Volume appears on the **Configuration** tab of the
   database details page.

To enable or disable DLV on an existing DB instance using Provisioned IOPS storage, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the following
parameters:

- `--dedicated-log-volume` – Enables a dedicated
  log volume.

Use `--no-dedicated-log-volume` (the default) to
disable a dedicated log volume.

- `--apply-immediately` – Use
  `--apply-immediately` to apply changes
  immediately.

Use `--no-apply-immediately` (the default) to apply
changes during the next maintenance window.
To enable or disable DLV on an existing DB instance using Provisioned IOPS storage, use the Amazon RDS API operation
[`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following
parameters:

- `DedicatedLogVolume` – Set this option to
  `true` to enable a dedicated log volume.

Set this option to `false` to disable a dedicated log
volume. This is the default value.

- `ApplyImmediately` – Set this option to
  `True` to apply changes immediately.

Set this option to `False` (the default) to apply
changes during the next maintenance window.

## Monitoring DLV storage

You can monitor the DLV storage usage by using the `FreeStorageSpaceLogVolume`
metric in CloudWatch.

You can use the following query for RDS for PostgreSQL to find the size occupied by transaction
logs:

```
SELECT pg_size_pretty(COALESCE(sum(size), 0)) AS total_wal_generated_size
FROM pg_catalog.pg_ls_waldir();
```

If the DLV runs out of storage, the DB instance will enter the `storage-full`
state, causing downtime.
