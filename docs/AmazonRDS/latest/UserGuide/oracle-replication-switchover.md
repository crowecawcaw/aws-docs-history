

# Performing an Oracle Data Guard switchover
<a name="oracle-replication-switchover"></a>

A *switchover* is a role reversal between a primary database and a standby database. During a switchover, the original primary database transitions to a standby role, while the original standby database transitions to the primary role.

In an Oracle Data Guard environment, a primary database supports one or more standby databases. You can perform a managed, switchover-based role transition from a primary database to a standby database.

**Topics**
+ [Overview of Oracle Data Guard switchover](#oracle-replication-switchover.overview)
+ [Requirements for the Oracle Data Guard switchover](oracle-switchover.preparing.md)
+ [Initiating the Oracle Data Guard switchover](oracle-switchover.initiating.md)
+ [Monitoring the Oracle Data Guard switchover](oracle-switchover.monitoring.md)

## Overview of Oracle Data Guard switchover
<a name="oracle-replication-switchover.overview"></a>

Amazon RDS supports a fully managed, switchover-based role transition for Oracle Database replicas. You can only initiate a switchover to a standby database that is mounted or open read-only. 

The replicas can reside in separate AWS Regions or in different Availability Zones (AZs) of a single Region. All AWS Regions are supported. 

![Switch over a standby instance to make it the primary DB instance.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/read-replica-switchover.png)


A switchover differs from a read replica promotion. In a switchover, the source and replica DB instances change roles. In a promotion, a read replica becomes a source DB instance, but the source DB instance doesn't become a replica. For more information, see [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.Promote.md).

**Topics**
+ [Benefits of Oracle Data Guard switchover](#oracle-replication-switchover.overview.benefits)
+ [Supported Oracle Database versions](#oracle-replication-switchover.overview.engine-support)
+ [Cost of Oracle Data Guard switchover](#oracle-replication-switchover.overview.cost)
+ [How Oracle Data Guard switchover works](#oracle-replication-switchover.overview.how-it-works)

### Benefits of Oracle Data Guard switchover
<a name="oracle-replication-switchover.overview.benefits"></a>

Just as for RDS for Oracle read replicas, a managed switchover relies on Oracle Data Guard. The operation is designed to have zero data loss. Amazon RDS automates the following aspects of the switchover:
+ Reverses the roles of your primary database and specified standby database, putting the new standby database in the same state (mounted or read-only) as the original standby
+ Ensures data consistency
+ Maintains your replication configuration after the transition
+ Supports repeated reversals, allowing your new standby database to return to its original primary role

### Supported Oracle Database versions
<a name="oracle-replication-switchover.overview.engine-support"></a>

Oracle Data Guard switchover is supported for Oracle Database 19c and higher releases.

### Cost of Oracle Data Guard switchover
<a name="oracle-replication-switchover.overview.cost"></a>

The Oracle Data Guard switchover feature doesn't incur additional costs. Oracle Database Enterprise Edition includes support for standby databases in mounted mode. To open standby databases in read-only mode, you need the Oracle Active Data Guard option.

### How Oracle Data Guard switchover works
<a name="oracle-replication-switchover.overview.how-it-works"></a>

Oracle Data Guard switchover is a fully managed operation. You initiate the switchover for a standby database by issuing the CLI command `switchover-read-replica`. Then Amazon RDS modifies the primary and standby roles in your replication configuration.

The *original standby* and *original primary* are the roles that exist before the switchover. The *new standby* and *new primary* are the roles that exist after the switchover. A *bystander replica* is a replica database that serves as a standby database in the Oracle Data Guard environment but is not switching roles.

**Topics**
+ [Stages of the Oracle Data Guard switchover](#oracle-replication-switchover.overview.how-it-works.during-switchover)
+ [After the Oracle Data Guard switchover](#oracle-replication-switchover.overview.how-it-works.after-switchover)

#### Stages of the Oracle Data Guard switchover
<a name="oracle-replication-switchover.overview.how-it-works.during-switchover"></a>

To perform the switchover, Amazon RDS must take the following steps:

1. Block new transactions on the original primary database. During the switchover, Amazon RDS interrupts replication for all databases in your Oracle Data Guard configuration. During the switchover, the original primary database can't process write requests.

1. Ship unapplied transactions to the original standby database, and apply them.

1. Restart the new standby database in read-only or mounted mode. The mode depends on the open state of the original standby database before the switchover.

1. Open the new primary database in read/write mode.

#### After the Oracle Data Guard switchover
<a name="oracle-replication-switchover.overview.how-it-works.after-switchover"></a>

Amazon RDS switches the roles of the primary and standby database. You are responsible for reconnecting your application and performing any other desired configuration.

**Topics**
+ [Success criteria](#oracle-replication-switchover.overview.how-it-works.after-switchover.success)
+ [Connection to the new primary database](#oracle-replication-switchover.overview.how-it-works.after-switchover.connection)
+ [Configuration of the new primary database](#oracle-replication-switchover.overview.how-it-works.after-switchover.success.configuration)

##### Success criteria
<a name="oracle-replication-switchover.overview.how-it-works.after-switchover.success"></a>

The Oracle Data Guard switchover is successful when the original standby database does the following:
+ Transitions to its role as new primary database
+ Completes its reconfiguration

To limit downtime, your new primary database becomes active as soon as possible. Because Amazon RDS configures bystander replicas asynchronously, these replicas might become active after the original primary database.

##### Connection to the new primary database
<a name="oracle-replication-switchover.overview.how-it-works.after-switchover.connection"></a>

Amazon RDS won't propagate your current database connections to the new primary database after the switchover. After the Oracle Data Guard switchover completes, reconnect your application to the new primary database.

##### Configuration of the new primary database
<a name="oracle-replication-switchover.overview.how-it-works.after-switchover.success.configuration"></a>

To perform a switchover to the new primary database, Amazon RDS changes the mode of the original standby database to open. The change in role is the only change to the database. Amazon RDS doesn't set up features such as Multi-AZ replication.

If you perform a switchover to a cross-Region replica with different options, the new primary database keeps its own options. Amazon RDS won't migrate the options on the original primary database. If the original primary database had options such as SSL, NNE, OEM, and OEM\_AGENT, Amazon RDS doesn't propagate them to the new primary database.

**Note**  
Because the switchover changes only the database role, the new primary database isn't protected by Multi-AZ until you enable it. After the switchover completes, review the new primary database and, if needed, enable Multi-AZ and reconfigure any options (such as SSL, NNE, OEM, and OEM\_AGENT) that your application requires.