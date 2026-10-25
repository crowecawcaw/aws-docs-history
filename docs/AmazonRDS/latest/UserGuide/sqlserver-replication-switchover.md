

# Performing a SQL Server switchover
<a name="sqlserver-replication-switchover"></a>

A *switchover* is a role reversal between a primary DB instance and a read replica. During a switchover, the primary DB instance becomes a replica. At the same time, the read replica becomes the new primary.

You can perform a managed, switchover-based role transition from an RDS for SQL Server primary DB instance to its read replica.

Before you initiate a switchover, make sure that your replication environment meets the requirements and limitations. For more information, see [Preparing for a SQL Server switchover](sqlserver-switchover.preparing.md).

**Topics**
+ [Overview of the SQL Server switchover](#sqlserver-replication-switchover.overview)
+ [Preparing for a SQL Server switchover](sqlserver-switchover.preparing.md)
+ [Initiating the SQL Server switchover](sqlserver-switchover.initiating.md)
+ [Monitoring the SQL Server switchover](sqlserver-switchover.monitoring.md)

## Overview of the SQL Server switchover
<a name="sqlserver-replication-switchover.overview"></a>

Amazon RDS supports a fully managed, switchover-based role transition for RDS for SQL Server read replicas. You can switch over a read replica to the primary role, and the current primary DB instance becomes a read replica. Use a switchover when you want to move the primary role to a different Availability Zone or AWS Region.

The read replica can reside in a separate AWS Region or in a different Availability Zone (AZ) of the same Region.

![Diagram showing a primary DB instance and read replica before a switchover, and their reversed primary and replica roles after the switchover.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/sqlserver-read-replica-switchover.png)


A switchover differs from a read replica promotion. In a switchover, the source and replica DB instances change roles. In a promotion, a read replica becomes a source DB instance, but the source DB instance doesn't become a replica. The promoted read replica detaches from the source DB instance, and the replication relationship between the two DB instances is broken. For more information, see [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.Promote.md).

**Topics**
+ [Benefits of the SQL Server switchover](#sqlserver-replication-switchover.overview.benefits)
+ [Supported SQL Server versions](#sqlserver-replication-switchover.overview.engine-support)
+ [Cost of the SQL Server switchover](#sqlserver-replication-switchover.overview.cost)
+ [How the SQL Server switchover works](#sqlserver-replication-switchover.overview.how-it-works)

### Benefits of the SQL Server switchover
<a name="sqlserver-replication-switchover.overview.benefits"></a>

The switchover is designed to have zero data loss. Amazon RDS automates the following aspects of the switchover:
+ Reverses the roles of your primary DB instance and specified read replica
+ Brings the original primary DB instance online as the new read replica in read-only mode
+ Ensures data consistency
+ Maintains your replication configuration after the transition
+ Preserves the configuration of each DB instance, such as backup retention, option groups, parameter groups, and features, after the transition
+ Supports repeated reversals, allowing your new read replica to return to its original primary role

### Supported SQL Server versions
<a name="sqlserver-replication-switchover.overview.engine-support"></a>

Switchover is supported for SQL Server versions 2022–2025 on the Enterprise Edition (EE) engine.

### Cost of the SQL Server switchover
<a name="sqlserver-replication-switchover.overview.cost"></a>

The switchover feature doesn't incur additional costs.

### How the SQL Server switchover works
<a name="sqlserver-replication-switchover.overview.how-it-works"></a>

The switchover is a fully managed operation. You initiate the switchover for a read replica by issuing the CLI command `switchover-read-replica`. Then Amazon RDS modifies the primary and replica roles in your replication configuration.

The *original replica* and *original primary* are the roles that exist before the switchover. The *new replica* and *new primary* are the roles that exist after the switchover.

**Topics**
+ [Stages of the SQL Server switchover](#sqlserver-replication-switchover.overview.how-it-works.during-switchover)
+ [After the SQL Server switchover](#sqlserver-replication-switchover.overview.how-it-works.after-switchover)

#### Stages of the SQL Server switchover
<a name="sqlserver-replication-switchover.overview.how-it-works.during-switchover"></a>

Before you initiate a switchover, stop your applications and disconnect all connections to both the primary DB instance and the read replica. Keep the applications stopped for the duration of the switchover. For the preparation steps that you're responsible for, see [Preparing for a SQL Server switchover](sqlserver-switchover.preparing.md).

To perform the switchover, Amazon RDS must take the following steps:

1. Block new transactions on the original primary DB instance. During the switchover, the original primary DB instance can't process write requests.

1. Interrupt replication for all databases in your replication configuration.

1. Drop open connections on both the original primary DB instance and the original read replica.

1. Send unapplied transactions to the original read replica, and apply them.

1. Bring the original read replica online as the new primary DB instance in read/write mode.

1. Bring the original primary DB instance online as the new read replica in read-only mode.

#### After the SQL Server switchover
<a name="sqlserver-replication-switchover.overview.how-it-works.after-switchover"></a>

Amazon RDS switches the roles of the primary DB instance and read replica. After the switchover completes, reconnect your application and perform any other configuration that you need.

**Topics**
+ [Success criteria](#sqlserver-replication-switchover.overview.how-it-works.after-switchover.success)
+ [Connection to the new primary DB instance](#sqlserver-replication-switchover.overview.how-it-works.after-switchover.connection)
+ [Configuration of the new primary DB instance](#sqlserver-replication-switchover.overview.how-it-works.after-switchover.configuration)

##### Success criteria
<a name="sqlserver-replication-switchover.overview.how-it-works.after-switchover.success"></a>

The SQL Server switchover is successful when the original read replica does the following:
+ Transitions to its role as new primary DB instance
+ Completes its reconfiguration

To limit downtime, your new primary DB instance becomes active as soon as possible.

##### Connection to the new primary DB instance
<a name="sqlserver-replication-switchover.overview.how-it-works.after-switchover.connection"></a>

Your current database connections don't transfer to the new primary DB instance after the switchover. After the switchover completes, reconnect your application to the new primary DB instance.

Each DB instance keeps its own endpoint. After the switchover, the endpoint of the original primary DB instance accepts only read-only connections.

##### Configuration of the new primary DB instance
<a name="sqlserver-replication-switchover.overview.how-it-works.after-switchover.configuration"></a>

The change in role is the only change to the DB instance.

If you perform a switchover to a cross-Region replica with different options, the new primary DB instance keeps its own options. Amazon RDS won't migrate the options on the original primary DB instance to the new primary DB instance.

**Note**  
After the switchover completes, review the new primary DB instance and reconfigure any option groups and parameter groups that your application requires.