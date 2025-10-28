# Configuring active-active clusters for RDS for MySQL

An active-active cluster in Amazon RDS is a database configuration where multiple nodes
actively handle read and write operations, distributing the workload across instances to
improve availability and scalability. Each node in the cluster is synchronized to maintain
data consistency, enabling high availability and faster failover in case of node
failure

You can set up an active-active cluster for RDS for MySQL by using the MySQL Group
Replication plugin. The Group Replication plugin is supported for RDS for MySQL DB instances
running the following versions:

- All MySQL 8.4 versions
- MySQL 8.0.35 and higher minor versions
  For information about MySQL Group Replication, see [Group
  Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication.html") in the MySQL documentation. The MySQL documentation contains
  detailed information about this feature, while this topic describes how to configure and
  manage the plugin on your RDS for MySQL DB instances.

###### Note

For the sake of brevity, all mentions of "active-active" cluster in this topic refer to
active-active clusters using the MySQL Group Replication plugin.

## Use cases for active-active

clusters

The following cases are good candidates for using active-active clusters:

- Applications that need all of the DB instances in the cluster to support write
  operations. The Group Replication plugin keeps the data consistent on each DB
  instance in the active-active cluster. For more information about how this
  works, see [Group Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication-summary.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-summary.html") in the MySQL documentation.
- Applications that require continuous availability of the database. With an
  active-active cluster, the data is retained on the all of the DB instances in
  the cluster. If one DB instance fails, the application can reroute traffic to
  another DB instance in the cluster.
- Applications that might need to split read and write operations among
  different DB instances in the cluster for load balancing purposes. With an
  active-active cluster, your applications can send read traffic to specific DB
  instances and write traffic to others. You can also switch which DB instances to
  send reads or writes to at any time.

###### Topics

- [Limitations
  and considerations for active-active clusters](mysql-active-active-clusters-considerations-limitations.md "mysql-active-active-clusters-considerations-limitations.md")
- [Preparing for a
  cross-VPC active-active cluster](mysql-active-active-clusters-cross-vpc-prerequisites.md "mysql-active-active-clusters-cross-vpc-prerequisites.md")
- [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md "mysql-active-active-clusters-parameters.md")
- [Converting an existing DB instance to an active-active cluster](mysql-active-active-clusters-converting.md "mysql-active-active-clusters-converting.md")
- [Setting up an active-active cluster with new DB instances](mysql-active-active-clusters-setting-up.md "mysql-active-active-clusters-setting-up.md")
- [Adding a DB instance to an active-active cluster](mysql-active-active-clusters-adding.md "mysql-active-active-clusters-adding.md")
- [Monitoring active-active clusters](mysql-active-active-clusters-monitoring.md "mysql-active-active-clusters-monitoring.md")
- [Stopping Group Replication on a
  DB instance in an active-active cluster](mysql-active-active-clusters-stopping.md "mysql-active-active-clusters-stopping.md")
- [Renaming a DB instance in an active-active cluster](mysql-active-active-clusters-renaming.md "mysql-active-active-clusters-renaming.md")
- [Removing a DB instance from an
  active-active cluster](mysql-active-active-clusters-remove.md "mysql-active-active-clusters-remove.md")
