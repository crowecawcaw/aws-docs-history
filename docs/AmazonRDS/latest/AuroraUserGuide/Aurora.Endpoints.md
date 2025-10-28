# Instance endpoints for Amazon Aurora

An _instance endpoint_ connects to a specific DB
instance within an Aurora cluster. Each DB instance in a DB cluster has its own unique
instance endpoint. So there is one instance endpoint for the current primary DB instance of
the DB cluster, and there is one instance endpoint for each of the Aurora Replicas in the DB
cluster.

The instance endpoint provides direct control over connections to the DB cluster, for
scenarios where using the cluster endpoint or reader endpoint might not be appropriate. For
example, your client application might require more fine-grained connection balancing based
on workload type. In this case, you can configure multiple clients to connect to different
Aurora Replicas in a DB cluster to distribute read workloads. For an example that uses
instance endpoints to improve connection speed after a failover for Aurora PostgreSQL, see [Fast failover with
Amazon Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md"). For an example that uses instance
endpoints to improve connection speed after a failover for Aurora MySQL, see [MariaDB
Connector/J failover support - case Amazon Aurora](https://mariadb.org/mariadb-connectorj-failover-support-case-amazon-aurora/ "https://mariadb.org/mariadb-connectorj-failover-support-case-amazon-aurora/").

The following example illustrates an instance endpoint for a DB instance in an
Aurora MySQL DB cluster.

```
mydbinstance.c7tj4example.us-east-1.rds.amazonaws.com:3306
```

Each DB instance in an Aurora cluster has its own built-in instance endpoint, whose name
and other attributes are managed by Aurora. You can't create, delete, or modify this
kind of endpoint. You might be familiar with instance endpoints if you use Amazon RDS. However,
with Aurora you typically use the writer and reader endpoints more often than the instance
endpoints.

In day-to-day Aurora operations, the main way that you use instance endpoints is to
diagnose capacity or performance issues that affect one specific instance in an Aurora
cluster. While connected to a specific instance, you can examine its status variables,
metrics, and so on. Doing this can help you determine what's happening for that
instance that's different from what's happening for other instances in the
cluster.

In advanced use cases, you might configure some DB instances differently than others. In
this case, use the instance endpoint to connect directly to an instance that is smaller,
larger, or otherwise has different characteristics than the others. Also, set up failover
priority so that this special DB instance is the last choice to take over as the primary
instance. We recommend that you use custom endpoints instead of the instance endpoint in
such cases. Doing so simplifies connection management and high availability as you add more
DB instances to your cluster.
