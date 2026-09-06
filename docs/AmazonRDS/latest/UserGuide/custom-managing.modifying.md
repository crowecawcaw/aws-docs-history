

# Modifying your RDS Custom for Oracle DB instance
<a name="custom-managing.modifying"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

Modifying an RDS Custom for Oracle DB instance is similar to modifying an Amazon RDS DB instance. You can change settings such as the following:
+ DB instance class
+ Storage allocation and type
+ Backup retention period
+ Deletion protection
+ Option group
+ CEV (see [Upgrading an RDS Custom for Oracle DB instance](custom-upgrading-modify.md))
+ Port

**Topics**
+ [Requirements and limitations when modifying your DB instance storage](#custom-managing.storage-modify)
+ [Requirements and limitations when modifying your DB instance class](#custom-managing.instance-class-reqs)
+ [How RDS Custom creates your DB instance when you modify the instance class](#custom-managing.instance-class-resources)
+ [Modifying your RDS Custom for Oracle DB instance](#custom-managing.modifying.procedure)

## Requirements and limitations when modifying your DB instance storage
<a name="custom-managing.storage-modify"></a>

Consider the following requirements and limitations when you modify the storage for an RDS Custom for Oracle DB instance:
+ The minimum allocated storage for RDS Custom for Oracle is 40 GiB, and the maximum is 64 TiB.
+ As with Amazon RDS, you can't decrease the allocated storage. This is a limitation of Amazon EBS volumes.
+ Storage autoscaling isn't supported for RDS Custom DB instances.
+ Any storage volumes that you attach manually to your RDS Custom DB instance are outside the support perimeter.

  For more information, see [RDS Custom support perimeter](custom-concept.md#custom-troubleshooting.support-perimeter).
+ Magnetic (standard) Amazon EBS storage isn't supported for RDS Custom. You can choose only the io1, io2, gp2, or gp3 SSD storage types.

For more information about Amazon EBS storage, see [Amazon RDS DB instance storage](CHAP_Storage.md). For general information about storage modification, see [Working with storage for Amazon RDS DB instances](USER_PIOPS.StorageTypes.md).

## Requirements and limitations when modifying your DB instance class
<a name="custom-managing.instance-class-reqs"></a>

Consider the following requirements and limitations when you modify the instance class for an RDS Custom for Oracle DB instance:
+ Your DB instance must be in the `available` state.
+ Your DB instance must have a minimum of 100 MiB of free space on the root volume, data volume, and binary volume.
+ You can assign only a single elastic IP (EIP) to your RDS Custom for Oracle DB instance when using the default elastic network interface (ENI). If you attach multiple ENIs to your DB instance, the modify operation fails.
+ All RDS Custom for Oracle tags must be present.
+ If you use RDS Custom for Oracle replication, note the following requirements and limitations:
  + For primary DB instances and read replicas, you can change the instance class for only one DB instance at a time.
  + If your RDS Custom for Oracle DB instance has an on-premises primary or replica database, make sure to manually update private IP addresses on the on-premises DB instance after the modification completes. This action is necessary to preserve Oracle DataGuard functionality. RDS Custom for Oracle publishes an event when the modification succeeds.
  + You can't modify your RDS Custom for Oracle DB instance class when the primary or read replica DB instances have FSFO (Fast-Start Failover) configured.

## How RDS Custom creates your DB instance when you modify the instance class
<a name="custom-managing.instance-class-resources"></a>

When you modify your instance class, RDS Custom creates your DB instance as follows:
+ Creates the Amazon EC2 instance.
+ Creates the root volume from the latest DB snapshot. RDS Custom for Oracle doesn't retain information added to the root volume after the latest DB snapshot.
+ Creates Amazon CloudWatch alarms.
+ Creates an Amazon EC2 SSH key pair if you have deleted the original key pair. Otherwise, RDS Custom for Oracle retains the original key pair.
+ Creates new resources using the tags that are attached to your DB instance when you initiate the modification. RDS Custom doesn't transfer tags to the new resources when they are attached directly to underlying resources.
+ Transfers the binary and data volumes with the most recent modifications to the new DB instance.
+ Transfers the elastic IP address (EIP). If the DB instance is publicly accessible, then RDS Custom temporarily attaches a public IP address to the new DB instance before transferring the EIP. If the DB instance isn't publicly accessible, RDS Custom doesn't create public IP addresses.

## Modifying your RDS Custom for Oracle DB instance
<a name="custom-managing.modifying.procedure"></a>

You can modify the DB instance class or storage using the console, AWS CLI, or RDS API.

### Console
<a name="custom-managing.modifying.procedure.CON"></a>

**To modify an RDS Custom for Oracle DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the DB instance that you want to modify.

1. Choose **Modify**.

1. (Optional) In **Instance configuration**, choose a value for **DB instance class**. For supported classes, see [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances).

1. (Optional) In **Storage**, make the following changes as needed:

   1. Enter a new value for **Allocated storage**. It must be greater than the current value, and from 40 GiB–64 TiB.

   1. Change the value for **Storage type** to **General Purpose SSD (gp2)**, **General Purpose SSD (gp3)**, **Provisioned IOPS (io1)**, or **Provisioned IOPS (io2)**.

   1. If you specified a storage type other than **General Purpose SSD (gp2)**, you can change the **Provisioned IOPS** value.

1. (Optional) In **Additional configuration**, make the following changes as needed:

   1. For **Option group**, choose a new option group. For more information, see [Working with option groups in RDS Custom for Oracle](custom-oracle-option-groups.md).

1. Choose **Continue**.

1. Choose **Apply immediately** or **Apply during the next scheduled maintenance window**.

1. Choose **Modify DB instance**.

### AWS CLI
<a name="custom-managing.modifying.procedure.CLI"></a>

To modify the storage for an RDS Custom for Oracle DB instance, use the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) AWS CLI command. Set the following parameters as needed:
+ `--db-instance-class` – A new instance class. For supported classes, see [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances).
+ `--allocated-storage` – Amount of storage to be allocated for the DB instance, in gibibytes. It must be greater than the current value, and from 40–65,536 GiB.
+ `--storage-type` – The storage type: gp2, gp3, io1, or io2.
+ `--iops` – Provisioned IOPS for the DB instance, if using the io1, io2, or gp3 storage types.
+ `--apply-immediately` – Use `--apply-immediately` to apply the storage changes immediately.

  Or use `--no-apply-immediately` (the default) to apply the changes during the next maintenance window.

The following example changes the DB instance class of `my-cfo-instance` to `db.m5.16xlarge`. The command also changes the storage size to `1024` (1 TiB), storage type to `io2`, Provisioned IOPS to `3000`, and option group to `cfo-ee-19-mt`.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-cfo-instance}} \
    --db-instance-class {{db.m5.16xlarge}} \
    --storage-type {{io2}} \
    --iops {{3000}} \
    --allocated-storage {{1024}} \
    --option-group {{cfo-ee-19-mt}} \
    --apply-immediately
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-cfo-instance}} ^
    --db-instance-class {{db.m5.16xlarge}} ^
    --storage-type {{io2}} ^
    --iops {{3000}} ^
    --allocated-storage {{1024}} ^
    --option-group {{cfo-ee-19-mt}} ^
    --apply-immediately
```