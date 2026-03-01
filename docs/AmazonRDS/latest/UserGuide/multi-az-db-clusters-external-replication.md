# Setting up external replication from Multi-AZ DB clusters for Amazon RDS

You can set up replication between a Multi-AZ DB cluster and a database that is external to Amazon RDS.

External replication allows Multi-AZ DB clusters to replicate data between an RDS DB instance and an external
database, either on-premises or in another cloud environment. It's beneficial for disaster
recovery, data migration, and maintaining consistency between systems in different
locations. The section covers the prerequisites for setting up replication, how to configure
the process, and key considerations like replication latency, bandwidth, and compatibility
with different database engines.

## RDS for MySQL

To set up external replication for an RDS for MySQL Multi-AZ DB cluster, you must retain binary log files on
the DB instances within the cluster for long enough to ensure that the changes are applied to
the replica before Amazon RDS deletes the binlog file. To do so, configure binary log
retention by calling the `mysql.rds_set_configuration` stored procedure and
specifying the `binlog retention hours` parameter. For more information, see
[binlog retention hours](mysql-stored-proc-configuring.md#mysql_rds_set_configuration-usage-notes.binlog-retention-hours "mysql-stored-proc-configuring.md#mysql_rds_set_configuration-usage-notes.binlog-retention-hours").

The default value for `binlog retention hours` is `NULL`, which means
that binary logs aren't retained (0 hours). If you want to set up external replication
for a Multi-AZ DB cluster, you must set the parameter to a value other than `NULL`.

You can only configure binary log retention from the writer DB instance of the Multi-AZ DB cluster, and the
setting is propagated to all reader DB instances asynchronously.

In addition, we highly recommend enabling GTID-based replication on your external replica.
Then, if one of the DB instances fails, you can resume replication from another healthy
DB instance within the cluster. For more information, see [Replication
with Global Transaction Identifiers](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids.html "https://dev.mysql.com/doc/refman/8.0/en/replication-gtids.html") in the MySQL documentation.

## RDS for PostgreSQL

To set up external replication for an RDS for PostgreSQL Multi-AZ DB cluster, you must enable logical
replication. For instructions, see [Setting up PostgreSQL logical replication with Multi-AZ DB clusters for Amazon RDS](USER_MultiAZDBCluster_LogicalRepl.md "USER_MultiAZDBCluster_LogicalRepl.md").
