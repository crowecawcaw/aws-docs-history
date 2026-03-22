# Modifying settings for Provisioned IOPS SSD storage

You can modify the settings for a DB instance that uses Provisioned IOPS SSD storage by using the Amazon RDS console,
AWS CLI, or Amazon RDS API. Specify the storage type, allocated storage, and the amount of Provisioned IOPS that you
require. The range depends on your database engine and instance type.

Although you can reduce the amount of IOPS provisioned for your instance, you can't reduce the storage size.

In most cases, scaling storage doesn't require any outage and doesn't degrade performance of the server. After you modify
the storage IOPS for a DB instance, the status of the DB instance is **storage-optimization**.

###### Note

Storage optimization can take several hours. You can't make further storage modifications for either six (6) hours or
until storage optimization has completed on the instance, whichever is longer.

For information on the ranges of allocated storage and Provisioned IOPS available for each database engine, see [Provisioned IOPS SSD storage](CHAP_Storage.md#USER_PIOPS "CHAP_Storage.md#USER_PIOPS").

###### To change the Provisioned IOPS settings for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.

To filter the list of DB instances, for **Filter databases** enter a text string for
Amazon RDS to use to filter the results. Only DB instances whose names contain the string appear. 3. Choose the DB instance with Provisioned IOPS that you want to modify. 4. Choose **Modify**. 5. On the **Modify DB instance** page, choose **Provisioned IOPS SSD (io1)** or
**Provisioned IOPS SSD (io2)** for **Storage type**. 6. For **Provisioned IOPS**, enter a value.

If the value that you specify for either **Allocated storage** or
**Provisioned IOPS** is outside the limits
supported by the other parameter, a warning message is displayed. This
message gives the range of values required for the other parameter. 7. Choose **Continue**. 8. Choose **Apply immediately** in the **Scheduling of
modifications** section to apply the changes to the DB
instance immediately. Or choose **Apply during the next
scheduled maintenance window** to apply the changes during
the next maintenance window. 9. Review the parameters to be changed, and choose **Modify DB instance** to
complete the modification.

The new value for allocated storage or for Provisioned IOPS appears in the **Status** column.
To change the Provisioned IOPS setting for a DB instance, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the following
parameters:

- `--storage-type` – Set to `io1` or `io2` for Provisioned IOPS.
- `--allocated-storage` – Amount of storage to be allocated for the DB instance, in gibibytes.
- `--iops` – The new amount of Provisioned IOPS for the DB instance, expressed in I/O operations per second.
- `--apply-immediately` – Use `--apply-immediately` to apply changes immediately. Use
  `--no-apply-immediately` (the default) to apply changes during the next maintenance
  window.
  To change the Provisioned IOPS settings for a DB instance, use the Amazon RDS API operation
  [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following
  parameters:

- `StorageType` – Set to `io1` or `io2` for Provisioned IOPS.
- `AllocatedStorage` – Amount of storage to be allocated for the DB instance, in gibibytes.
- `Iops` – The new IOPS rate for the DB instance, expressed in I/O operations per second.
- `ApplyImmediately` – Set this option to `True` to apply changes immediately. Set this option to
  `False` (the default) to apply changes during the next maintenance window.
