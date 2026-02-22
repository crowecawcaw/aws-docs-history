# Read replica

configuration with PostgreSQL

RDS for PostgreSQL uses PostgreSQL native streaming replication to create a read-only copy
of a source DB instance. This read replica DB instance is an asynchronously created
physical replica of the source DB instance. It's created by a special connection
that transmits write ahead log (WAL) data from the source DB instance to the read
replica. For more information, see [Streaming Replication](https://www.postgresql.org/docs/14/warm-standby.html#STREAMING-REPLICATION "https://www.postgresql.org/docs/14/warm-standby.html#STREAMING-REPLICATION") in the PostgreSQL documentation.

PostgreSQL asynchronously streams database changes to this secure connection as
they're made on the source DB instance. You can encrypt communications from your client
applications to the source DB instance or any read replicas by setting the
`ssl` parameter to `1`. For more information, see [Using SSL with a PostgreSQL DB
instance](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md") .

PostgreSQL uses a _replication_ role to perform streaming
replication. The role is privileged, but you can't use it to modify any data. PostgreSQL
uses a single process for handling replication.

You can create a PostgreSQL read replica without affecting operations or users of the
source DB instance. Amazon RDS sets the necessary parameters and permissions for you, on the
source DB instance and the read replica, without affecting the service. A snapshot is
taken of the source DB instance, and this snapshot is used to create the read replica.
If you delete the read replica at some point in the future, no outage occurs.

You can create up to 15 read replicas from one source DB instance within the same
Region. As of RDS for PostgreSQL 14.1, you can also create up to three levels of read replica
in a chain (cascade) from a source DB instance. For more information, see [Using cascading
read replicas with RDS for PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md"). In all cases,
the source DB instance needs to have automated backups configured. You do this by
setting the backup retention period on your DB instance to any value other than 0. For
more information, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").

You can create read replicas for your RDS for PostgreSQL DB instance in the same
AWS Region as your source DB instance. This is known as _in-Region_
replication. You can also create read replicas in different AWS Regions than the
source DB instance. This is known as _cross-Region_ replication. For
more information about setting up cross-Region read replicas, see [Creating a read replica in a different
AWS Region](USER_ReadRepl.md "USER_ReadRepl.md"). The various
mechanisms supporting the replication process for in-Region and cross-Region differ
slightly depending on the RDS for PostgreSQL version as explained in [How
streaming replication works for different RDS for PostgreSQL versions](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md").

For replication to operate effectively, each read replica should have the same amount
of compute and storage resources as the source DB instance. If you scale the source DB
instance, be sure to also scale the read replicas.

Amazon RDS overrides any incompatible parameters on a read replica if they prevent the read
replica from starting. For example, suppose that the `max_connections`
parameter value is higher on the source DB instance than on the read replica. In that
case, Amazon RDS updates the parameter on the read replica to be the same value as that on
the source DB instance.

RDS for PostgreSQL read replicas have access to external databases that are available
through foreign data wrappers (FDWs) on the source DB instance. For example, suppose
that your RDS for PostgreSQL DB instance is using the `mysql_fdw` wrapper to
access data from RDS for MySQL. If so, your read replicas can also access that data. Other
supported FDWs include `oracle_fdw`, `postgres_fdw`, and
`tds_fdw`. For more information, see [Working
with the supported foreign data wrappers for Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.md "Appendix.PostgreSQL.CommonDBATasks.Extensions.md").

## Using RDS for PostgreSQL read replicas with Multi-AZ configurations

You can create a read replica from a single-AZ or Multi-AZ DB instance. You can
use Multi-AZ deployments to improve the durability and availability of critical
data, with a standby replica. A _standby replica_
is a dedicated read replica that can assume the workload if the source DB fails
over. You can't use your standby replica to serve read traffic. However, you
can create read replicas from high-traffic Multi-AZ DB instances to offload
read-only queries. To learn more about Multi-AZ deployments, see [Multi-AZ DB instance deployments for Amazon RDS](Concepts.md "Concepts.md").

If the source DB instance of a Multi-AZ deployment fails over to a standby, the
associated read replicas switch to using the standby (now primary) as their
replication source. The read replicas might need to restart, depending on the
RDS for PostgreSQL version, as follows:

- PostgreSQL 13 and higher versions –
  Restarting isn't required. The read replicas are automatically
  synchronized with the new primary. However, in some cases your client
  application might cache Domain Name Service (DNS) details for your read
  replicas. If so, set the time-to-live (TTL) value to less than 30 seconds.
  Doing this prevents the read replica from holding on to a stale IP address
  (and thus, prevents it from synchronizing with the new primary). To learn
  more about this and other best practices, see [Amazon RDS basic operational
  guidelines](CHAP_BestPractices.md#CHAP_BestPractices.DiskPerformance "CHAP_BestPractices.md#CHAP_BestPractices.DiskPerformance").
- PostgreSQL 12 and all earlier versions
  – The read replicas restart automatically after a fail over to the
  standby replica because the standby (now primary) has a different IP address
  and a different instance name. Restarting synchronizes the read replica with
  the new primary.

To learn more about failover, see [Failing over a Multi-AZ DB instance for Amazon RDS](Concepts.MultiAZ.md "Concepts.MultiAZ.md"). To learn more about how read
replicas work in a Multi-AZ deployment, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

To provide failover support for a read replica, you can create the read replica as
a Multi-AZ DB instance so that Amazon RDS creates a standby of your replica in another
Availability Zone (AZ). Creating your read replica as a Multi-AZ DB instance is
independent of whether the source database is a Multi-AZ DB instance.
