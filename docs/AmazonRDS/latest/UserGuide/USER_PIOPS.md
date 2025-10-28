# Upgrading the storage file system for a DB

instance

Most RDS DB instances offer a maximum storage size of 64 TiB for RDS for MariaDB, MySQL, and PostgreSQL
databases. However, some older 32-bit file systems have lower storage capacities. To
determine the storage capacity of your DB instance, use the [describe-valid-db-instance-modifications](../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md "../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md") AWS CLI command.

RDS checks whether your storage system has a 16 TiB storage size, a file size limit of 2
TiB, or non-optimized writes. If your DB instances meet these conditions, RDS alerts you that
your file system configuration is eligible for an upgrade. You can check the upgrade
eligibility of a DB instance on the **Storage** panel of the DB instance details
page.

![Check the storage configuration upgrade eligibility of a DB instance.](images/upgrade-storage-config.png)
If your DB instance is eligible for a file system upgrade, use either of the following
techniques:

- Create a blue/green deployment and specify **Upgrade storage file system
  configuration**.

This option upgrades the file system in the green environment to the preferred
configuration. You can then switch over the blue/green deployment, which
promotes the green environment to be the new production environment. For
detailed instructions, see [Creating a blue/green deployment in Amazon RDS](blue-green-deployments-creating.md "blue-green-deployments-creating.md").

- Create a DB instance read replica and specify **Upgrade storage file system
  configuration**.

This option upgrades the file system of the read replica to the preferred
configuration. You can then promote the read replica to be a standalone
instance. For detailed instructions, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").
During the storage upgrade, your database engine isn't available. Upgrading the storage
configuration is an I/O-intensive operation and leads to longer creation times for read
replicas and blue/green deployments. The storage upgrade process is faster when both of
the following conditions are met:

- The source DB instance uses Provisioned IOPS SSD (io1 or io2 Block Express)
  storage.
- You provisioned the green environment or read replica with an instance size of
  4xlarge or larger.
  Storage upgrades involving General Purpose SSD (gp2) storage can deplete your I/O
  credit balance, resulting in longer upgrade times. For more information, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

During a storage upgrade, RDS increases the allocated storage size by 10% for the green
instance or read replica if both of the following conditions are met:

- The storage consumption on your source DB instance is greater than or equal to 90%
  of the allocated storage size.
- Storage autoscaling is enabled.
  RDS turns off autoscaling when the new storage size is greater than or equal to the
  maximum allocated storage that was set for the instance. If storage autoscaling is
  disabled before the storage upgrade begins, the storage size doesn't increase during the
  upgrade.
