# Managing a Multi-AZ deployment for RDS Custom for SQL Server

In a Multi-AZ DB instance deployment for RDS Custom for SQL Server, Amazon RDS automatically provisions and
maintains a synchronous standby replica in a different Availability Zone (AZ). The primary
DB instance is synchronously replicated across Availability Zones to a standby replica to
provide data redundancy.

###### Important

A Multi-AZ deployment for RDS Custom for SQL Server is different than Multi-AZ for RDS for SQL Server. Unlike Multi-AZ for
RDS for SQL Server, you must set up prerequisites for RDS Custom for SQL Server before creating your Multi-AZ DB
instance because RDS Custom runs inside your own account, which requires permissions.

If you don't complete the prerequisites, your Multi-AZ DB instance might fail to run,
or automatically revert to a Single-AZ DB instance. For more information about
prerequisites, see [Prerequisites for a Multi-AZ deployment with RDS Custom for SQL Server](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md").

Running a DB instance with high availability can enhance availability during planned
system maintenance. In the event of planned database maintenance or unplanned service
disruption, Amazon RDS automatically fails over to the up-to-date secondary DB instance. This
functionality lets database operations resume quickly without manual intervention. The
primary and standby instances use the same endpoint, whose physical network address
transitions to the secondary replica as part of the failover process. You don't have to
reconfigure your application when a failover occurs.

![RDS Custom for SQL Server supports Multi-AZ.](images/custom-sqlserver-multiaz-architecture.png)
You can create an RDS Custom for SQL Server Multi-AZ deployment by specifying Multi-AZ when creating an
RDS Custom DB instance. You can use the console to convert existing RDS Custom for SQL Server DB instances to
Multi-AZ deployments by modifying the DB instance and specifying the Multi-AZ option. You
can also specify a Multi-AZ DB instance deployment with the AWS CLI or Amazon RDS API.

The RDS console shows the Availability Zone of the standby replica (the secondary AZ).
You can also use the `describe-db-instances` CLI command or the `DescribeDBInstances`
API operation to find the secondary AZ.

RDS Custom for SQL Server DB instances with Multi-AZ deployment can have increased write and commit latency
compared to a Single-AZ deployment. This increase can happen because of the synchronous data
replication between DB instances. You might have a change in latency if your deployment
fails over to the standby replica, although AWS is engineered with low-latency network
connectivity between Availability Zones.

###### Note

For production workloads, we recommend that you use a DB instance class with Provisioned
IOPS (input/output operations per second) for fast, consistent performance. For more information about DB instance classes,
see [Requirements and limitations for Amazon RDS Custom for SQL Server](custom-reqs-limits-MS.md "custom-reqs-limits-MS.md").

###### Topics

- [Region and version availability](#custom-sqlserver-multiaz.regionversion "#custom-sqlserver-multiaz.regionversion")
- [Limitations for a Multi-AZ deployment with RDS Custom for SQL Server](#custom-sqlserver-multiaz.limitations "#custom-sqlserver-multiaz.limitations")
- [Prerequisites for a Multi-AZ deployment with RDS Custom for SQL Server](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md")
- [Creating an RDS Custom for SQL Server Multi-AZ deployment](#custom-sqlserver-multiaz.creating "#custom-sqlserver-multiaz.creating")
- [Modifying an RDS Custom for SQL Server Single-AZ deployment to a Multi-AZ deployment](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md")
- [Modifying an RDS Custom for SQL Server Multi-AZ deployment to a Single-AZ deployment](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md")
- [Failover process for an RDS Custom for SQL Server Multi-AZ deployment](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md")

## Region and version availability

Multi-AZ deployments for RDS Custom for SQL Server are supported for the following SQL Server editions:

- SQL Server 2022 and 2019: Enterprise, Standard, Web, and Developer Edition

###### Note

Multi-AZ deployments for RDS Custom for SQL Server aren't supported on SQL Server 2019 CU8 (15.00.4073.23) or lower versions.

Multi-AZ deployments for RDS Custom for SQL Server are available in all Regions where RDS Custom for SQL Server
is available. For more information on Region availability of Multi-AZ deployments for RDS Custom for SQL Server, see [Supported
Regions and DB engines for RDS Custom for SQL Server](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq").

## Limitations for a Multi-AZ deployment with RDS Custom for SQL Server

Multi-AZ deployments with RDS Custom for SQL Server have the following limitations:

- Cross-Region Multi-AZ deployments aren't supported.
- You can’t configure the secondary DB instance to accept database read activity.
- When you use a Custom Engine Version (CEV) with a Multi-AZ deployment, your secondary DB instance will also use the same CEV.
  The secondary DB instance can't use a different CEV.

## Creating an RDS Custom for SQL Server Multi-AZ deployment

To create an RDS Custom for SQL Server Multi-AZ deployment, follow the steps in
[Creating and connecting to a DB instance for
Amazon RDS Custom for SQL Server](custom-creating-sqlserver.md "custom-creating-sqlserver.md").

###### Important

To simplify setup, we recommend that you use the latest CloudFormation template file provided in the network setup instructions.
For more information, see
[Configuring with CloudFormation](custom-setup-sqlserver.md#custom-setup-sqlserver.cf "custom-setup-sqlserver.md#custom-setup-sqlserver.cf").

Creating a Multi-AZ deployment takes a few minutes to complete.
