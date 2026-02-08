# Modifying the storage for an RDS Custom for SQL Server DB instance

Modifying storage for an RDS Custom for SQL Server DB instance is similar to modifying storage for an Amazon RDS DB instance, but you can only do the
following:

- Increase the allocated storage size.
- Change the storage type. You can use available storage types such as General Purpose or Provisioned IOPS. Provisioned IOPS
  is supported for the gp3, io1, and io2 Block Express storage types.
- Change the provisioned IOPS, if you're using the volume types that support Provisioned IOPS.
  The following limitations apply to modifying the storage for an RDS Custom for SQL Server DB instance:

- The minimum allocated storage size for RDS Custom for SQL Server is 20 GiB. The maximum storage limit for io1, gp2, and gp3 is 16 TiB while io2 supports 64 TiB.
- As with Amazon RDS, you can't decrease the allocated storage. This is a limitation of Amazon Elastic Block Store (Amazon EBS) volumes.
  For more information, see [Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md")
- Storage autoscaling isn't supported for RDS Custom for SQL Server DB instances.
- Any storage volumes that you manually attach to your RDS Custom DB instance are not considered for storage scaling.
  Only the RDS-provided default data volumes, i.e., the D drive, are considered for storage scaling.

For more information, see [RDS Custom support
perimeter](custom-concept.md#custom-troubleshooting.support-perimeter "custom-concept.md#custom-troubleshooting.support-perimeter").

- Scaling storage usually doesn't cause any outage or performance degradation of the DB instance. After you modify
  the storage size for a DB instance, the status of the DB instance is **storage-optimization**.
- Storage optimization can take several hours. You can't make further storage modifications for either six (6) hours or until storage
  optimization has completed on the instance, whichever is longer. For more information, see [Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md")
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

For general information about storage modification, see [Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md").

###### Important

Do not modify storage for your RDS Custom for SQL Server DB instance using Amazon EC2 or Amazon EBS consoles or APIs. Direct storage modifications outside of Amazon RDS console or
APIs result in an `unsupported-configuration` state for your database.

When you make direct storage changes using Amazon EC2 or Amazon EBS, Amazon RDS cannot track or manage your database instance state. This might cause:

- High availability failover mechanisms from functioning correctly
- Database replication setups to break
- Redundancy features to fail
  Modify storage only through Amazon RDS console or APIs to keep your database in a supported state. See
  [Fixing unsupported
  configurations in RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported "custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported") for recovery steps.

###### To modify the storage for an RDS Custom for SQL Server DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to modify.
4. Choose **Modify**.
5. Make the following changes as needed:
   1. Enter a new value for **Allocated storage**. It must be greater than the current value, and from 20
      GiB–16 TiB.
   2. Change the value for **Storage type**. You can choose from the available General Purpose
      or Provisioned IOPS storage types. Provisioned IOPS is supported for the gp3, io1, and io2 Block Express
      storage types.
   3. If you're specifying a storage type that supports Provisioned IOPS, you can define the
      **Provisioned IOPS** value.

6. Choose **Continue**.
7. Choose **Apply immediately** or **Apply during the next scheduled maintenance
   window**.
8. Choose **Modify DB instance**.
   To modify the storage for an RDS Custom for SQL Server DB instance, use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") AWS CLI command. Set the following parameters as needed:

- `--allocated-storage` – Amount of storage to be allocated for the DB instance, in gibibytes. It must be
  greater than the current value, and from 20–16,384 GiB.
- `--storage-type` – The storage type, for example, gp2, gp3, io1, or io2.
- `--iops` – Provisioned IOPS for the DB instance. You can specify this only for storage types
  that support Provisioned IOPS (gp3, io1, and io2).
- `--apply-immediately` – Use `--apply-immediately` to apply the storage changes
  immediately.

Or use `--no-apply-immediately` (the default) to apply the changes during the next maintenance window.
The following example changes the storage size of my-custom-instance to 200 GiB, storage type to io1, and Provisioned IOPS to 3000.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier my-custom-instance \
    --storage-type io1 \
    --iops 3000 \
    --allocated-storage 200 \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier my-custom-instance ^
    --storage-type io1 ^
    --iops 3000 ^
    --allocated-storage 200 ^
    --apply-immediately
```
