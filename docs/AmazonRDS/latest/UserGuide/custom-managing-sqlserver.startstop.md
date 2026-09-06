

# Starting and stopping an RDS Custom for SQL Server DB instance
<a name="custom-managing-sqlserver.startstop"></a>

You can start and stop your RDS Custom for SQL Server DB instance. The same general requirements and limitations for RDS for SQL Server DB instances apply to stopping and starting your RDS Custom for SQL Server DB instances. For more information, see [Stopping an Amazon RDS DB instance temporarily](USER_StopInstance.md).

The following considerations also apply to starting and stopping your RDS Custom for SQL Server DB instance:
+ Modifying an EC2 instance attribute of an RDS Custom for SQL Server DB instance while the DB instance is `STOPPED` isn't supported.
+ You can stop and start an RDS Custom for SQL Server DB instance only if it's configured for a single Availability Zone. You can't stop an RDS Custom for SQL Server DB instance in a Multi-AZ configuration.
+ A `SYSTEM` snapshot will be created when you stop an RDS Custom for SQL Server DB instance. The snapshot will be automatically deleted when you start the RDS Custom for SQL Server DB instance again.
+ If you delete your EC2 instance while your RDS Custom for SQL Server DB instance is stopped, the `C:` drive will be replaced when you start the RDS Custom for SQL Server DB instance again.
+ The `C:\` drive, hostname, and your custom configurations are persisted when you stop an RDS Custom for SQL Server DB instance, as long as you don't modify the instance type.
+ The following actions will result in RDS Custom placing the DB instance outside the support perimeter, and you're still charged for DB instance hours:
  + Starting the underlying EC2 instance while Amazon RDS is stopped. To resolve, you can call the `start-db-instance` Amazon RDS API, or stop the EC2 so the RDS Custom instance returns to `STOPPED`.
  + Stopping underlying EC2 instance when the RDS Custom for SQL Server DB instance is `ACTIVE`.

For more details about stopping and starting DB instances, see [Stopping an Amazon RDS DB instance temporarily](USER_StopInstance.md), and [Starting an Amazon RDS DB instance that was previously stopped](USER_StartInstance.md).