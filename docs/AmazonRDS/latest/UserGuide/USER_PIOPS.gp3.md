# Modifying settings for General Purpose SSD (gp3) storage

You can modify the settings for a DB instance that uses General Purpose SSD (gp3)
storage by using the Amazon RDS console, AWS CLI, or Amazon RDS API. Specify the storage type,
allocated storage, amount of Provisioned IOPS, and storage throughput that you
require.

Although you can reduce the amount of Provisioned IOPS and storage throughput for your
DB instance, you can't reduce the storage size.

In most cases, scaling storage doesn't require any outage. After you modify the storage IOPS for a DB instance, the
status of the DB instance is **storage-optimization**. You can expect elevated latencies, but still within the
single-digit millisecond range, during storage optimization. The DB instance is fully operational after a storage
modification.

###### Note

After storage optimization completes on the instance, you can make additional storage modifications. You can perform a maximum
of four storage modifications within any 24-hour period.

For information on the ranges of allocated storage, Provisioned IOPS, and storage throughput available for each database
engine, see [gp3 storage (recommended)](CHAP_Storage.md#gp3-storage "CHAP_Storage.md#gp3-storage").

###### To change the storage performance settings for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.

To filter the list of DB instances, for **Filter
databases** enter a text string for Amazon RDS to use to filter
the results. Only DB instances whose names contain the string
appear. 3. Choose the DB instance with gp3 storage that you want to modify. 4. Choose **Modify**. 5. On the **Modify DB instance page**, choose **General Purpose SSD (gp3)** for
**Storage type**, then do the following:

    1. For **Provisioned IOPS**, choose a
     value.


    If the value that you specify for either **Allocated
     storage** or **Provisioned IOPS**
     is outside the limits supported by the other parameter, a
     warning message appears. This message gives the range of values
     required for the other parameter.
    2. For **Storage throughput**, choose a
     value.


    If the value that you specify for either **Provisioned
     IOPS** or **Storage throughput**
     is outside the limits supported by the other parameter, a
     warning message appears. This message gives the range of values
     required for the other parameter.

6. Choose **Continue**. 7. Choose **Apply immediately** in the
**Scheduling of modifications** section to apply
the changes to the DB instance immediately. Or choose **Apply
during the next scheduled maintenance window** to apply the
changes during the next maintenance window. 8. Review the parameters to be changed, and choose **Modify DB instance** to complete the
modification.

The new value for Provisioned IOPS appears in the **Status** column.
To change the storage performance settings for a DB instance, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the following
parameters:

- `--storage-type` – Set to `gp3` for General Purpose SSD (gp3).
- `--allocated-storage` – Amount of storage to be allocated for the DB instance, in
  gibibytes.
- `--iops` – The new amount of Provisioned IOPS for the DB instance, expressed in I/O
  operations per second.
- `--storage-throughput` – The new storage throughput for the DB instance, expressed in
  MiBps.
- `--apply-immediately` – Use `--apply-immediately` to apply changes immediately.
  Use `--no-apply-immediately` (the default) to apply changes during the next maintenance
  window.
  To change the storage performance settings for a DB instance, use the Amazon RDS API operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following
  parameters:

- `StorageType` – Set to `gp3` for General Purpose SSD (gp3).
- `AllocatedStorage` – Amount of storage to be allocated for the DB instance, in
  gibibytes.
- `Iops` – The new IOPS rate for the DB instance, expressed in I/O operations per
  second.
- `StorageThroughput` – The new storage throughput for the DB instance, expressed in
  MiBps.
- `ApplyImmediately` – Set this option to `True` to apply changes immediately. Set
  this option to `False` (the default) to apply changes during the next maintenance window.
