

# Working with storage for Amazon RDS DB instances
<a name="USER_PIOPS.StorageTypes"></a>

To specify how you want your data stored in Amazon RDS, choose a storage type and provide a storage size when you create or modify a DB instance. Later, you can increase the amount or change the type of storage by modifying the DB instance. For more information about which storage type to use for your workload, see [Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage).

If your instances run RDS for Oracle or RDS for SQL Server, you can add up to three additional volumes to each DB instance. You can choose either gp3 or io2 as the volume type, allowing you to optimize costs and performance based on your data access patterns. The maximum storage capacity of a DB instance that uses additional volumes is 256 TiB.

**Topics**
+ [Viewing storage volume details for your DB instance](rds-storage-viewing.md)
+ [Increasing DB instance storage capacity](USER_PIOPS.ModifyingExisting.md)
+ [Removing additional storage volumes](USER_PIOPS.RemovingAdditionalVolumes.md)
+ [Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.Autoscaling.md)
+ [Upgrading the storage file system for a DB instance](USER_PIOPS.UpgradeFileSystem.md)
+ [Modifying settings for Provisioned IOPS SSD storage](User_PIOPS.Increase.md)
+ [I/O-intensive storage modifications](USER_PIOPS.IOIntensive.md)
+ [Modifying settings for General Purpose SSD (gp3) storage](USER_PIOPS.gp3.md)
+ [Using a dedicated log volume (DLV)](USER_PIOPS.dlv.md)