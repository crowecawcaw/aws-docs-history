# Multi-AZ failover with additional storage volumes

Multi-AZ deployments support DB instances with additional storage volumes. During a failover, RDS automatically fails over
to the standby instance with any additional storage volumes attached to the DB instance.
This process ensures data consistency and availability.

When you configure a Multi-AZ deployment for a DB instance with additional storage volumes, Amazon RDS
automatically replicates all volumes to the standby instance in a different Availability
Zone. The replicated storage includes:

- The primary storage volume
- All additional storage volumes attached to your DB instance
  During a failover, Amazon RDS promotes the standby instance and ensures that all storage volumes
  are available and consistent. The failover maintains the same storage configuration,
  including volume names, storage types, and performance characteristics.

After a successful failover, you can verify that all storage volumes are properly attached
and accessible by viewing the storage configuration details. For more information, see
[Viewing storage volume details for your DB instance](rds-storage-viewing.md "rds-storage-viewing.md").

The failover time for DB instances with additional storage volumes is similar to DB instances with only
primary storage.
