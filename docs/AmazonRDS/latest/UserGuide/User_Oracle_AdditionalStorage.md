# Working with storage in RDS for Oracle

Every RDS for Oracle instance has a primary storage volume. To increase storage capacity,
you can attach up to three additional storage volumes to your DB instance. Depending on your workload
requirements, choose between gp3 and io2 storage for each volume.
For example, you might put frequently accessed data on an io2 volume and historical data on a gp3 volume.

Use additional storage volumes to enable the following benefits:

- **Enhanced capacity** – Scale your total storage up
  to 256 TiB per DB instance by attaching up to three additional storage volumes.
- **Flexible storage configuration and performance optimization** –
  Mix different storage types (gp3 and io2) to optimize for both cost and
  performance based on your data access patterns. Separate frequently accessed data
  on high-performance io2 storage from archival data on cost-effective gp3 storage.
- **Expand and reduce storage capacity as needed** – Attach a volume when
  you need additional storage, as during data migration, and then later delete the volume.
  In this way, you can expand and reduce the total DB instance storage.
- **Online data movement** – Use the built-in capabilities
  of Oracle database to move data between volumes without downtime.

###### Note

You can remove additional storage volumes, but you can't remove the primary volume.

###### Topics

- [Considerations for using additional storage volumes with RDS for Oracle](#User_Oracle_AdditionalStorage.considerations "#User_Oracle_AdditionalStorage.considerations")
- [Limitations of using additional storage volumes with RDS for Oracle](#User_Oracle_AdditionalStorage.limitations "#User_Oracle_AdditionalStorage.limitations")
- [Database management operations with additional storage volumes in RDS for Oracle](#User_Oracle_AdditionalStorage.DBManagement "#User_Oracle_AdditionalStorage.DBManagement")
- [Add, remove, or modify storage volumes with RDS for Oracle](User_Oracle_AdditionalStorage.md "User_Oracle_AdditionalStorage.md")
- [Backing up and restoring data with additional storage volumes in RDS for Oracle](User_Oracle_AdditionalStorage.md "User_Oracle_AdditionalStorage.md")
- [Use cases for additional storage volumes in RDS for Oracle](User_Oracle_AdditionalStorage.md "User_Oracle_AdditionalStorage.md")

## Considerations for using additional storage volumes with RDS for Oracle

Consider the following when using additional storage volumes with RDS for Oracle:

- You can add up to 3 additional storage volumes per instance.
- Additional storage volumes must use the following volume names:
  - rdsdbdata2
  - rdsdbdata3
  - rdsdbdata4

- You can only add General Purpose SSD (gp3) and Provisioned IOPS SSD (io2)
  storage types.
- You can use Oracle’s online relocation capabilities to move data between
  volumes while your applications continue running.
- When you create an additional storage volume by modifying the DB instance,
  RDS immediately creates the storage volume regardless of the schedule modifications setting.
  Adding a storage volume is an online operation and does not impact your database performance.
  See [Using the schedule modifications
  setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

For optimal performance, check the following when you are using additional storage
volumes:

- Data movement planning
  - Schedule large movements during off-peak hours
  - Break large operations into smaller chunks
  - Monitor system resources during moves

- Resource management
  - Keep sufficient free space on both volumes
  - Monitor I/O patterns using AWR or Statspack
  - Watch for storage-full scenarios

- Best practices
  - Use online datafile relocation operations where possible
  - Maintain appropriate indexes
  - Regularly monitor space usage

When using additional storage volumes with replicas:

- When you are creating an RDS for Oracle replica for a DB instance that has additional storage volumes,
  RDS automatically configures additional storage volumes on the replica. However, any subsequent modifications
  made in storage volumes of your primary DB instance are not automatically applied to the replica.
- When managing datafile locations across volumes, we recommend using parameter group settings
  instead of session-level changes to ensure consistent behavior between
  primary and replica instances.

## Limitations of using additional storage volumes with RDS for Oracle

The following limitations apply to using additional storage volumes with RDS for Oracle:

- You can’t add a storage volume to the instance types with less than 64GiB
  memory because they don’t have sufficient memory to support large storage
  volumes.
- The minimum storage size is 200GiB for additional storage volumes.
  The primary storage volume of your DB instance should be equal to or larger than 200GiB
  to attach additional storage volumes. The maximum storage size for your DB instance
  is 256 TiB total across all volumes.
- The following capabilities aren’t supported for DB instances with
  additional storage volumes:
  - Cross-region automated backups
  - Cross-region read replica
  - Storage autoscaling (for additional storage volumes)
  - Cross-account snapshot copy
  - Public snapshots

- You can't delete the primary storage volume (`rdsdbdata`),
  but you can delete other additional storage volumes as long as they're empty.
- You can't store the online redo logs, archived redo logs, and control files
  in additional storage volumes. These files can only be stored in the primary storage
  volume (`rdsdbdata`).

## Database management operations with additional storage volumes in RDS for Oracle

You can perform database management operations such as creating tablespaces or
moving data between storage volumes while using additional storage volumes in RDS for Oracle.
For more information about database management operations with additional storage volumes, see the following sections:

- [Specifying
  database file locations in RDS for Oracle](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.DatabaseFileLocations "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.DatabaseFileLocations")
- [Creating and sizing tablespaces in RDS for Oracle](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CreatingTablespacesAndDatafiles "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CreatingTablespacesAndDatafiles")
- [Moving data
  files between volumes in RDS for Oracle](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.MovingDatafiles "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.MovingDatafiles")
