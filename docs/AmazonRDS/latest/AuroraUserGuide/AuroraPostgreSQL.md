# Performance and scaling for

Amazon Aurora PostgreSQL

The following section discusses managing performance and scaling for an Amazon Aurora PostgreSQL
DB cluster. It also includes information about other maintenance tasks.

###### Topics

- [Scaling
  Aurora PostgreSQL DB instances](#AuroraPostgreSQL.Managing.Performance.InstanceScaling "#AuroraPostgreSQL.Managing.Performance.InstanceScaling")
- [Maximum connections to an
  Aurora PostgreSQL DB instance](#AuroraPostgreSQL.Managing.MaxConnections "#AuroraPostgreSQL.Managing.MaxConnections")
- [Temporary storage limits for
  Aurora PostgreSQL](#AuroraPostgreSQL.Managing.TempStorage "#AuroraPostgreSQL.Managing.TempStorage")
- [Huge pages for Aurora PostgreSQL](#AuroraPostgreSQL.Managing.HugePages "#AuroraPostgreSQL.Managing.HugePages")
- [Testing
  Amazon Aurora PostgreSQL by using fault injection queries](AuroraPostgreSQL.Managing.md "AuroraPostgreSQL.Managing.md")
- [Displaying volume status for an
  Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Managing.md "AuroraPostgreSQL.Managing.md")
- [Specifying the RAM disk for the
  stats_temp_directory](AuroraPostgreSQL.Managing.md "AuroraPostgreSQL.Managing.md")
- [Managing temporary files with
  PostgreSQL](PostgreSQL.md "PostgreSQL.md")

## Scaling

Aurora PostgreSQL DB instances

You can scale Aurora PostgreSQL DB instances in two ways, instance scaling and read
scaling. For more information about read scaling, see [Read scaling](Aurora.Managing.md#Aurora.Managing.Performance.ReadScaling "Aurora.Managing.md#Aurora.Managing.Performance.ReadScaling").

You can scale your Aurora PostgreSQL DB cluster by modifying the DB instance class for
each DB instance in the DB cluster. Aurora PostgreSQL supports several DB instance classes
optimized for Aurora. Don't use db.t2 or db.t3 instance classes for larger Aurora
clusters of size greater than 40 terabytes (TB).

###### Note

We recommend using the T DB instance classes only for development and test
servers, or other non-production servers. For more details on the T instance
classes, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

Scaling isn't instantaneous. It can take 15 minutes or more to complete the
change to a different DB instance class. If you use this approach to modify the DB
instance class, you apply the change during the next scheduled maintenance window
(rather than immediately) to avoid affecting users.

As an alternative to modifying the DB instance class directly, you can minimize
downtime by using the high availability features of Amazon Aurora. First, add an Aurora
Replica to your cluster. When creating the replica, choose the DB instance class size
that you want to use for your cluster. When the Aurora Replica is synchronized with the
cluster, you then failover to the newly added Replica. To learn more, see [Aurora Replicas](Aurora.md#Aurora.Replication.Replicas "Aurora.md#Aurora.Replication.Replicas")
and [Fast failover with
Amazon Aurora PostgreSQL](AuroraPostgreSQL.BestPractices.md "AuroraPostgreSQL.BestPractices.md").

For detailed specifications of the DB instance classes supported by Aurora PostgreSQL, see
[Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

## Maximum connections to an

Aurora PostgreSQL DB instance

An Aurora PostgreSQL DB cluster allocates resources based on the DB instance class and its
available memory. Each connection to the DB cluster consumes incremental amounts of
these resources, such as memory and CPU. Memory consumed per connection varies based on
query type, count, and whether temporary tables are used. Even an idle connection
consumes memory and CPU. That's because when queries run on a connection, more
memory is allocated for each query and it's not released completely, even when
processing stops. Thus, we recommend that you make sure your applications aren't
holding on to idle connections: each one of these wastes resources and affects
performance negatively. For more information, see [Resources consumed
by idle PostgreSQL connections](https://aws.amazon.com/blogs/database/resources-consumed-by-idle-postgresql-connections/ "https://aws.amazon.com/blogs/database/resources-consumed-by-idle-postgresql-connections/").

The maximum number of connections allowed by an Aurora PostgreSQL DB instance is
determined by the `max_connections` parameter value specified in the
parameter group for that DB instance. The ideal setting for the
`max_connections` parameter is one that supports all the client
connections your application needs, without an excess of unused connections, plus at
least 3 more connections to support AWS automation. Before modifying the
`max_connections` parameter setting, we recommend that you consider the
following:

- If the `max_connections` value is too low, the Aurora PostgreSQL DB
  instance might not have sufficient connections available when clients attempt to
  connect. If this happens, attempts to connect using `psql` raise
  error messages such as the following:

```
psql: FATAL: remaining connection slots are reserved for non-replication superuser connections
```

- If the `max_connections` value exceeds the number of connections
  that are actually needed, the unused connections can cause performance to
  degrade.

The default value of `max_connections` is derived from the following
Aurora PostgreSQL `LEAST` function:

`LEAST({DBInstanceClassMemory/9531392},5000)`.

If you want to change the value for `max_connections`, you need to create a
custom DB cluster parameter group and change its value there. After applying your custom
DB parameter group to your cluster, be sure to reboot the primary instance so the new
value takes effect. For more information, see [Amazon Aurora PostgreSQL
parameters](AuroraPostgreSQL.Reference.md "AuroraPostgreSQL.Reference.md") and [Creating a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Tip

If your applications frequently open and close connections, or keep a large number
of long-lived connections open, we recommend that you use Amazon RDS Proxy. RDS Proxy is a
fully managed, highly available database proxy that uses connection pooling to share
database connections securely and efficiently. To learn more about RDS Proxy, see
[Amazon RDS Proxy for Aurora](rds-proxy.md "rds-proxy.md").

For details about how Aurora Serverless v2 instances handle this parameter, see [Maximum connections for Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.max-connections "aurora-serverless-v2.md#aurora-serverless-v2.max-connections").

## Temporary storage limits for

Aurora PostgreSQL

Aurora PostgreSQL stores tables and indexes in the Aurora storage subsystem. Aurora PostgreSQL
uses separate temporary storage for non-persistent temporary files. This includes files
that are used for such purposes as sorting large data sets during query processing or
for index build operations. For more information, see the article [How can I
troubleshoot local storage issues in Aurora PostgreSQL-Compatible
instances?](https://repost.aws/knowledge-center/postgresql-aurora-storage-issue "https://repost.aws/knowledge-center/postgresql-aurora-storage-issue").

These local storage volumes are backed by Amazon Elastic Block Store and can be extended by using a
larger DB instance class. For more information about storage, see [Amazon Aurora
storage](Aurora.Overview.md "Aurora.Overview.md"). You can also increase your
local storage for temporary objects by using an NVMe enabled instance type and Aurora
Optimized Reads-enabled temporary objects. For more information, see [Improving query performance for
Aurora PostgreSQL with Aurora Optimized Reads](AuroraPostgreSQL.optimized.md "AuroraPostgreSQL.optimized.md").

###### Note

You might see `storage-optimization` events when scaling DB instances,
for example, from db.r5.2xlarge to db.r5.4xlarge.

The following table shows the maximum amount of temporary storage available for each
Aurora PostgreSQL DB instance class. For more information on DB instance class support for
Aurora, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md").

| DB instance class | Maximum temporary storage available (GiB) |
| ----------------- | ----------------------------------------- |
| db.x2g.16xlarge   | 1829                                      |
| db.x2g.12xlarge   | 1606                                      |
| db.x2g.8xlarge    | 1071                                      |
| db.x2g.4xlarge    | 535                                       |
| db.x2g.2xlarge    | 268                                       |
| db.x2g.xlarge     | 134                                       |
| db.x2g.large      | 67                                        |
| db.r8g.48xlarge   | 3072                                      |
| db.r8g.24xlarge   | 1536                                      |
| db.r8g.16xlarge   | 998                                       |
| db.r8g.12xlarge   | 749                                       |
| db.r8g.8xlarge    | 499                                       |
| db.r8g.4xlarge    | 250                                       |
| db.r8g.2xlarge    | 125                                       |
| db.r8g.xlarge     | 63                                        |
| db.r8g.large      | 31                                        |
| db.r7g.16xlarge   | 1008                                      |
| db.r7g.12xlarge   | 756                                       |
| db.r7g.8xlarge    | 504                                       |
| db.r7g.4xlarge    | 252                                       |
| db.r7g.2xlarge    | 126                                       |
| db.r7g.xlarge     | 63                                        |
| db.r7g.large      | 32                                        |
| db.r7i.48xlarge   | 3072                                      |
| db.r7i.24xlarge   | 1500                                      |
| db.r7i.16xlarge   | 1008                                      |
| db.r7i.12xlarge   | 748                                       |
| db.r7i.8xlarge    | 504                                       |
| db.r7i.4xlarge    | 249                                       |
| db.r7i.2xlarge    | 124                                       |
| db.r7i.xlarge     | 62                                        |
| db.r7i.large      | 31                                        |
| db.r6g.16xlarge   | 1008                                      |
| db.r6g.12xlarge   | 756                                       |
| db.r6g.8xlarge    | 504                                       |
| db.r6g.4xlarge    | 252                                       |
| db.r6g.2xlarge    | 126                                       |
| db.r6g.xlarge     | 63                                        |
| db.r6g.large      | 32                                        |
| db.r6i.32xlarge   | 1829                                      |
| db.r6i.24xlarge   | 1500                                      |
| db.r6i.16xlarge   | 1008                                      |
| db.r6i.12xlarge   | 748                                       |
| db.r6i.8xlarge    | 504                                       |
| db.r6i.4xlarge    | 249                                       |
| db.r6i.2xlarge    | 124                                       |
| db.r6i.xlarge     | 62                                        |
| db.r6i.large      | 31                                        |
| db.r5.24xlarge    | 1500                                      |
| db.r5.16xlarge    | 1008                                      |
| db.r5.12xlarge    | 748                                       |
| db.r5.8xlarge     | 504                                       |
| db.r5.4xlarge     | 249                                       |
| db.r5.2xlarge     | 124                                       |
| db.r5.xlarge      | 62                                        |
| db.r5.large       | 31                                        |
| db.r4.16xlarge    | 960                                       |
| db.r4.8xlarge     | 480                                       |
| db.r4.4xlarge     | 240                                       |
| db.r4.2xlarge     | 120                                       |
| db.r4.xlarge      | 60                                        |
| db.r4.large       | 30                                        |
| db.t4g.large      | 16.5                                      |
| db.t4g.medium     | 8.13                                      |
| db.t3.large       | 16                                        |
| db.t3.medium      | 7.5                                       |

###### Note

NVMe enabled instance types can increase the temporary space available by up to
the total NVMe size. For more information, see [Improving query performance for
Aurora PostgreSQL with Aurora Optimized Reads](AuroraPostgreSQL.optimized.md "AuroraPostgreSQL.optimized.md").

You can monitor the temporary storage available for a DB instance with the
`FreeLocalStorage` CloudWatch metric,
-->
described in [Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.md "Aurora.AuroraMonitoring.md"). (This doesn't apply to
Aurora Serverless v2.)

For some workloads, you can reduce the amount of temporary storage by allocating more
memory to the processes that are performing the operation. To increase the memory
available to an operation, increasing the values of the [work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM") or [maintenance_work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM") PostgreSQL parameters.

## Huge pages for Aurora PostgreSQL

_Huge pages_ are a memory management feature that
reduces overhead when a DB instance is working with large contiguous chunks of memory,
such as that used by shared buffers. This PostgreSQL feature is supported by all
currently available Aurora PostgreSQL versions.

`Huge_pages` parameter is turned on by default for all DB instance classes
other than t3.medium,db.t3.large,db.t4g.medium,db.t4g.large instance classes. You can't
change the `huge_pages` parameter value or turn off this feature in the
supported instance classes of Aurora PostgreSQL.

On Aurora PostgreSQL DB instances that don't support the huge pages memory feature, specific
process memory usage might increase without corresponding workload changes.

The system allocates shared memory segments like the buffer cache during server
startup. When huge memory pages aren't available, the system doesn't charge these
allocations to the postmaster process. Instead, it includes the memory in the process
that first accessed each 4KB page in the shared memory segment.

###### Note

Active connections share allocated memory as needed, regardless of how shared
memory usage is tracked across processes.
