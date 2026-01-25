# Multi-AZ DB instance deployments for Amazon RDS

Amazon RDS provides high availability and failover support for DB instances using Multi-AZ
deployments with a single standby DB instance. This type of deployment is called a
_Multi-AZ DB instance deployment_. Amazon RDS uses several different
technologies to provide this failover support. Multi-AZ deployments for MariaDB, MySQL,
Oracle, PostgreSQL, and RDS Custom for SQL Server DB instances use the Amazon failover technology. Microsoft SQL Server
DB instances use SQL Server Database Mirroring (DBM) or Always On Availability Groups (AGs).
For information on SQL Server version support for Multi-AZ, see [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md "USER_SQLServerMultiAZ.md"). For information
on working with RDS Custom for SQL Server for Multi-AZ, see [Managing a Multi-AZ deployment for RDS Custom for SQL Server](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md").

In a Multi-AZ DB instance deployment, Amazon RDS automatically provisions and maintains a
synchronous standby replica in a different Availability Zone. The primary DB instance is
synchronously replicated across Availability Zones to a standby replica to provide data
redundancy and minimize latency spikes during system backups. Running a DB instance with
high availability can enhance availability during planned system maintenance. It can also
help protect your databases against DB instance failure and Availability Zone disruption.
For more information on Availability Zones, see [Regions, Availability Zones, and Local Zones](Concepts.md "Concepts.md").

###### Note

The high availability option isn't a scaling solution for read-only scenarios. You
can't use a standby replica to serve read traffic. To serve read-only traffic, use
a Multi-AZ DB cluster or a read replica instead. For more information about Multi-AZ DB
clusters, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md"). For more information about read
replicas, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

![High availability scenario](images/con-multi-AZ.png)
Using the RDS console, you can create a Multi-AZ DB instance deployment by simply specifying Multi-AZ
when creating a DB instance. You can use the console to convert existing DB instances to
Multi-AZ DB instance deployments by modifying the DB instance and specifying the Multi-AZ option. You
can also specify a Multi-AZ DB instance deployment with the AWS CLI or Amazon RDS API. Use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") or [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") CLI command,
or the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") or
[ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API
operation.

The RDS console shows the Availability Zone of the standby replica (called the secondary AZ).
You can also use the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") CLI command or the [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md") API
operation to find the secondary AZ.

DB instances using Multi-AZ DB instance deployments can have increased write and commit
latency compared to a Single-AZ deployment. This can happen because of the synchronous data
replication that occurs. You might have a change in latency if your deployment fails over to
the standby replica, although AWS is engineered with low-latency network connectivity
between Availability Zones. For production workloads, we recommend that you use Provisioned
IOPS (input/output operations per second) for fast, consistent performance. For more
information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").
