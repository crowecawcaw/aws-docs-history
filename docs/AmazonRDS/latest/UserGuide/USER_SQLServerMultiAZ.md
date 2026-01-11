# Microsoft SQL Server Multi-AZ deployment limitations, notes, and

recommendations

The following are some limitations when working with Multi-AZ deployments on RDS for SQL Server DB instances:

- Cross-Region Multi-AZ isn't supported.
- Stopping an RDS for SQL Server DB instance in a multi-AZ deployment isn't supported.
- You can't configure the secondary DB instance to accept database read activity.
- Multi-AZ with Always On Availability Groups (AGs) supports in-memory optimization.
- Multi-AZ with Always On Availability Groups (AGs) doesn't support Kerberos
  authentication for the availability group listener. This is because the listener
  has no Service Principal Name (SPN).
- Multi-AZ with block level repcation is currently only supported for SQL Server Web Edition instances.
- You can't rename a database on a SQL Server DB instance that is in a SQL
  Server Multi-AZ deployment. If you need to rename a database on such an
  instance, first turn off Multi-AZ for the DB instance, then rename the database.
  Finally, turn Multi-AZ back on for the DB instance.
- You can only restore Multi-AZ DB instances that are backed up using the full
  recovery model.
- Multi-AZ deployments have a limit of 10,000 SQL Server Agent jobs.

If you need a higher limit, request an increase by contacting Support. Open the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") page, sign in if necessary, and choose **Create case**. Choose
**Service limit increase**. Complete and submit the form.

- You can't have an offline database on a SQL Server DB instance that is in a SQL Server Multi-AZ deployment.
- RDS for SQL Server doesn't replicate MSDB database permissions to the secondary instance.
  If you need these permissions on the secondary instance, you must recreate them manually.
- Volume metrics are not available for the secondary host of the instance using block level replication.
  The following are some notes about working with Multi-AZ deployments on RDS for SQL Server DB instances:

- Amazon RDS exposes the Always On AGs [availability group listener endpoint](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover "https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover"). The endpoint is visible in
  the console, and is returned by the `DescribeDBInstances` API
  operation as an entry in the endpoints field.
- Amazon RDS supports [availability group multisubnet failovers](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover "https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover").
- To use SQL Server Multi-AZ with a SQL Server DB instance in a virtual private cloud (VPC),
  first create a DB subnet group that has subnets in at least two distinct
  Availability Zones. Then assign the DB subnet group to the primary replica of
  the SQL Server DB instance.
- When a DB instance is modified to be a Multi-AZ deployment, during the modification it has a status of
  **modifying**. Amazon RDS creates the standby, and makes a backup of the primary DB instance. After the
  process is complete, the status of the primary DB instance becomes **available**.
- Multi-AZ deployments maintain all databases on the same node. If a database on the primary host fails over, all your SQL Server
  databases fail over as one atomic unit to your standby host. Amazon RDS provisions a new healthy host, and replaces the
  unhealthy host.
- Multi-AZ with DBM, AGs, or block level replication supports a single standby replica.
- Users, logins, and permissions are automatically replicated for you on the secondary. You don't need to recreate them.
  User-defined server roles are replicated in DB instances that use Always On AGs or block level replication for Multi-AZ deployments.
- In Multi-AZ deployments, RDS for SQL Server creates SQL Server logins to allow Always On AGs or Database Mirroring.
  RDS creates logins with the following pattern, `db_<dbiResourceId>_node1_login`,
  `db_<dbiResourceId>_node2_login`, and `db_<dbiResourceId>_witness_login`.
- RDS for SQL Server creates a SQL Server login to allow access to read replicas.
  RDS creates a login with the following pattern, `db_<readreplica_dbiResourceId>_node_login`.
- In Multi-AZ deployments, SQL Server Agent jobs are replicated from the primary host to the secondary host when the job replication
  feature is turned on. For more information, see [Turning on SQL Server Agent job replication](Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.Replicate "Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.Replicate").
- You might observe elevated latencies compared to a standard DB instance deployment (in a
  single Availability Zone) because of the synchronous data replication.
- Failover times are affected by the time it takes to complete the recovery process. Large transactions increase the failover
  time.
- In SQL Server Multi-AZ deployments, reboot with failover reboots only the primary DB instance. After the failover, the
  primary DB instance becomes the new secondary DB instance. Parameters might not be updated for Multi-AZ instances. For
  reboot without failover, both the primary and secondary DB instances reboot, and parameters are updated after the
  reboot. If the DB instance is unresponsive, we recommend reboot without failover.
  The following are some recommendations for working with Multi-AZ deployments on RDS for Microsoft SQL Server DB instances:

- For databases used in production or preproduction, we recommend the following
  options:
  - Multi-AZ deployments for high availability
  - "Provisioned IOPS" for fast, consistent performance
  - "Memory optimized" rather than "General purpose"

- You can't select the Availability Zone (AZ) for the secondary instance, so
  when you deploy application hosts, take this into account. Your database might
  fail over to another AZ, and the application hosts might not be in the same AZ
  as the database. For this reason, we recommend that you balance your application
  hosts across all AZs in the given AWS Region.
- For best performance, don't enable Database Mirroring, Always On AGs, or block level replication during a large data
  load operation. If you want your data load to be as fast as possible, finish
  loading data before you convert your DB instance to a Multi-AZ deployment.
- Applications that access the SQL Server databases should have exception handling that catches connection errors. The following
  code sample shows a try/catch block that catches a communication error. In this example, the `break`
  statement exits the `while` loop if the connection is successful, but retries up to 10 times if an exception
  is thrown.

```
int RetryMaxAttempts = 10;
int RetryIntervalPeriodInSeconds = 1;
int iRetryCount = 0;
while (iRetryCount < RetryMaxAttempts)
{
   using (SqlConnection connection = new SqlConnection(DatabaseConnString))
   {
      using (SqlCommand command = connection.CreateCommand())
      {
         command.CommandText = "INSERT INTO SOME_TABLE VALUES ('SomeValue');";
         try
         {
            connection.Open();
            command.ExecuteNonQuery();
            break;
         }
         catch (Exception ex)
         {
            Logger(ex.Message);
            iRetryCount++;
         }
         finally {
            connection.Close();
         }
      }
   }
   Thread.Sleep(RetryIntervalPeriodInSeconds * 1000);
}
```

- Don't use the `Set Partner Off` command when working with
  Multi-AZ instances using DBM or AGs. This command is not supported on
  instances using block level replication. For example, don't do the following.

```
--Don't do this
ALTER DATABASE db1 SET PARTNER off

```

- Don't set the recovery mode to `simple`. For example,
  don't do the following.

```
--Don't do this
ALTER DATABASE db1 SET RECOVERY simple

```

- Don't use the `DEFAULT_DATABASE` parameter when creating new
  logins on Multi-AZ DB instances unless using block level replication for high availability,
  because these settings can't be applied to the standby mirror. For example, don't do the following.

```
--Don't do this
CREATE LOGIN [test_dba] WITH PASSWORD=foo, DEFAULT_DATABASE=[db2]

```

Also, don't do the following.

```
--Don't do this
ALTER LOGIN [test_dba] WITH DEFAULT_DATABASE=[db3]

```
