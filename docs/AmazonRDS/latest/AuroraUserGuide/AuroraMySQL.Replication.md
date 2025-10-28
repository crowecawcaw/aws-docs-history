# Replication between Aurora and MySQL or between Aurora and another Aurora DB

cluster (binary log replication)

Because Amazon Aurora MySQL is compatible with MySQL, you can set up replication between a MySQL database and an Amazon Aurora MySQL DB
cluster. This type of replication uses the MySQL binary log replication, also referred to as _binlog
replication_. If you use binary log replication with Aurora, we recommend that your MySQL database run MySQL
version 5.5 or later. You can set up replication where your Aurora MySQL DB cluster is the replication source or the replica. You
can replicate with an Amazon RDS MySQL DB instance, a MySQL database external to Amazon RDS, or another Aurora MySQL DB cluster.

###### Note

You can't use binlog replication to or from certain types of Aurora DB clusters. In particular, binlog replication
isn't available for Aurora Serverless v1 clusters. If the `SHOW MASTER STATUS` and `SHOW
 SLAVE STATUS` (Aurora MySQL version 2) or `SHOW REPLICA STATUS` (Aurora MySQL version 3) statement returns
no output, check that the cluster you're using supports binlog replication.

You can also replicate with an RDS for MySQL DB instance or Aurora MySQL DB cluster in
another AWS Region. When you're performing replication across AWS Regions, make sure
that your DB clusters and DB instances are publicly accessible. If the Aurora MySQL DB
clusters are in private subnets in your VPC, use VPC peering between the AWS Regions.
For more information, see [A DB cluster in a VPC
accessed by an EC2 instance in a different VPC](USER_VPC.md#USER_VPC.Scenario3 "USER_VPC.md#USER_VPC.Scenario3").

If you want to configure replication between an Aurora MySQL DB cluster and an Aurora MySQL DB cluster in another AWS Region,
you can create an Aurora MySQL DB cluster as a read replica in a different AWS Region from the source DB cluster. For more
information, see [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

With Aurora MySQL version 2 and 3, you can replicate between Aurora MySQL and an external source or target that uses global
transaction identifiers (GTIDs) for replication. Ensure that the GTID-related parameters in the Aurora MySQL DB cluster have
settings that are compatible with the GTID status of the external database. To learn how to do this, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md"). In Aurora MySQL version 3.01 and higher, you can
choose how to assign GTIDs to transactions that are replicated from a source that doesn't use GTIDs. For information about
the stored procedure that controls that setting, see [mysql.rds_assign_gtids_to_anonymous_transactions (Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_assign_gtids_to_anonymous_transactions "mysql-stored-proc-gtid.md#mysql_assign_gtids_to_anonymous_transactions").

###### Warning

When you replicate between Aurora MySQL and MySQL, make sure that you use only InnoDB tables. If you have MyISAM tables
that you want to replicate, you can convert them to InnoDB before setting up replication with the following command.

```
alter table <schema>.<table_name> engine=innodb, algorithm=copy;
```

In the following sections, set up replication, stop replication, scale reads for your database, optimize binlog replication, and set up enhanced binlog.

###### Topics

- [Setting up binary log replication for Aurora MySQL](AuroraMySQL.Replication.MySQL.md "AuroraMySQL.Replication.MySQL.md")
- [Stopping binary log replication for Aurora MySQL](AuroraMySQL.Replication.MySQL.md "AuroraMySQL.Replication.MySQL.md")
- [Scaling reads for your MySQL database with Amazon Aurora](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Optimizing binary log replication for Aurora MySQL](binlog-optimization.md "binlog-optimization.md")
- [Setting up enhanced binlog for Aurora MySQL](AuroraMySQL.Enhanced.md "AuroraMySQL.Enhanced.md")
