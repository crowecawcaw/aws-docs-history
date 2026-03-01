# Working with MySQL read replicas

Following, you can find specific information about working with read replicas on
RDS for MySQL. For general information about read replicas and instructions for using them,
see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

For more information about MySQL read replicas, see the following topics.

- [Configuring replication filters with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Configuring delayed replication with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Updating read replicas with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Working with Multi-AZ read replica deployments with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Using cascading read replicas with RDS for MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Monitoring replication lag for MySQL read replicas](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Starting and stopping replication with MySQL read replicas](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md")
- [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md")

## Configuring read replicas with MySQL

Before a MySQL DB instance can serve as a replication source, make sure to enable
automatic backups on the source DB instance. To do this, set the backup retention
period to a value other than 0. This requirement also applies to a read replica that
is the source DB instance for another read replica. Automatic backups are supported
for read replicas running any version of MySQL. You can configure
replication based on binary log coordinates for a MySQL DB instance.

You can configure replication using global transaction identifiers (GTIDS) on the
following versions:

- RDS for MySQL version 5.7.44 and higher 5.7 versions
- RDS for MySQL version 8.0.28 and higher 8.0 versions
- RDS for MySQL version 8.4.3 and higher 8.4 versions

For more information, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

You can create up to 15 read replicas from one DB instance within the same Region. For
replication to operate effectively, each read replica should have the same amount of
compute and storage resources as the source DB instance. If you scale the source DB
instance, also scale the read replicas.

RDS for MySQL supports cascading read replicas. To learn how to configure cascading read replicas,
see [Using cascading read replicas with RDS for MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md").

You can run multiple read replica create and delete actions at the same time that reference
the same source DB instance. When you perform these actions, stay within the limit of 15 read replicas
for each source instance.

A read replica of a MySQL DB instance can't use a lower DB engine
version than its source DB instance.

### Preparing MySQL DB instances that use MyISAM

If your MySQL DB instance uses a nontransactional engine such as MyISAM, you need
to perform the following steps to successfully set up your read replica. These
steps are required to make sure that the read replica has a consistent copy of
your data. These steps are not required if all of your tables use a
transactional engine such as InnoDB.

1. Stop all data manipulation language (DML) and data definition language (DDL) operations on
   non-transactional tables in the source DB instance and wait for them to
   complete. SELECT statements can continue running.
2. Flush and lock the tables in the source DB instance.
3. Create the read replica using one of the methods in the following sections.
4. Check the progress of the read replica creation using, for example, the
   `DescribeDBInstances` API operation. Once the read
   replica is available, unlock the tables of the source DB instance and
   resume normal database operations.
