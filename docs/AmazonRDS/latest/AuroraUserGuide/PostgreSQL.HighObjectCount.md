

# Managing high object counts in Amazon Aurora PostgreSQL
<a name="PostgreSQL.HighObjectCount"></a>

While PostgreSQL limitations are theoretical, having extremely high object counts in a database will cause noticeable performance impact to various operations. This documentation covers several common object types that, when having a high total count can lead to several possible impacts.

The following table provides a summary of object types and their potential impacts:


**Object types and potential impacts**  

| Type of Object | Autovacuum | Logical Replication | Major Version Upgrade | pg\_dump / pg\_restore | General Performance | Instance Restart | 
| --- | --- | --- | --- | --- | --- | --- | 
| [Relations](#PostgreSQL.HighObjectCount.Relations) | x |  | x | x | x |  | 
| [Temporary tables](#PostgreSQL.HighObjectCount.TempTables) | x |  |  |  | x |  | 
| [Unlogged tables](#PostgreSQL.HighObjectCount.UnloggedTables) |  | x |  |  |  | x | 
| [Partitions](#PostgreSQL.HighObjectCount.Partitions) |  |  |  |  | x |  | 
| [Temporary files](#PostgreSQL.HighObjectCount.TempFiles) |  |  |  |  | x |  | 
| [Sequences](#PostgreSQL.HighObjectCount.Sequences) |  | x |  |  |  |  | 
| [Large objects](#PostgreSQL.HighObjectCount.LargeObjects) |  | x | x |  |  |  | 

## Relations
<a name="PostgreSQL.HighObjectCount.Relations"></a>

There is not a specific hard limit regarding the number of tables in a PostgreSQL database. The theoretical limit is extremely high, but there are other practical limits that need to be kept in mind during database design.

**Impact: Autovacuum falling behind**  
Autovacuum can struggle to keep up with transaction ID growth or table bloat due to lack of workers compared to amount of work.  
**Recommended action:** There are several factors for tuning autovacuum to keep up properly with a given number of tables and given workload. See [Best practices for working with PostgreSQL autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.html#AuroraPostgreSQL.BestPractices.Autovacuum) for suggestions on how to determine appropriate autovacuum settings. Use the [postgres\_get\_av\_diag utility](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Functions.html) to monitor problems with transaction ID growth.

**Impact: Major version upgrade / pg\_dump and restore**  
Amazon RDS uses the "--link" option during pg\_upgrade execution to avoid having to make copies of datafiles, the schema metadata is still required to be restored into the new version of the database. Even with parallel pg\_restore, if there are a significant number of relations this will increase the amount of downtime.

**Impact: General performance degradation**  
General performance degradation due to catalog size. Each table and its associated columns will add to `pg_attribute`, `pg_class` and `pg_depend` tables which are frequently used in normal database operations. There won't be a specific wait event visible, but shared buffer efficiency will be impacted.  
**Recommended action:** Regularly check table bloat for these specific tables and occasionally perform a `VACUUM FULL` on these specific tables. Be aware that `VACUUM FULL` on catalog tables requires an `ACCESS EXCLUSIVE` lock which means no other queries will be able to access them until the operation completes.

**Approximate threshold:** [Millions](#PostgreSQL.HighObjectCount.Note)

## Temporary tables
<a name="PostgreSQL.HighObjectCount.TempTables"></a>

Using temporary tables is useful for test data or intermediate results and is a common pattern seen in many database engines. The implications of heavy use in PostgreSQL must be understood to avoid some of the pitfalls. Each temporary table create and drop will add rows to system catalog tables, which when they become bloated, will cause general performance issues.

**Impact: Autovacuum falling behind**  
Temporary tables aren't vacuumed by autovacuum but will hold on to transaction IDs during their existence and can lead to wraparound if not removed.  
**Recommended action:** Temporary tables will live for the duration of the session that created them or can be dropped manually. A best practice of avoiding long-running transactions with temporary tables will prevent these tables from contributing to maximum used transaction ID growth.

**Impact: General performance degradation**  
General performance degradation due to catalog size. When sessions continuously create and drop temporary tables, it will add to `pg_attribute`, `pg_class` and `pg_depend` tables which are frequently used in normal database operations. There won't be a specific wait event visible, but shared buffer efficiency will be impacted.  
**Recommended action:**  
+ Regularly check table bloat for these specific tables and occasionally perform a `VACUUM FULL` on these specific tables. Be aware that `VACUUM FULL` on catalog tables requires an `ACCESS EXCLUSIVE` lock which means no other queries will be able to access them until the operation completes.
+ If temporary tables are heavily used, prior to a major version upgrade, a `VACUUM FULL` of these specific catalog tables is highly recommended to reduce downtime.

**General best practices:**
+ Reduce the use of temporary tables by using common table expressions to produce intermediate results. These can sometimes complicate the queries needed, but will eliminate the impacts listed above.
+ Reuse temporary tables by using the `TRUNCATE` command to clear the contents instead of doing drop/create steps. This will also eliminate the problem of transaction ID growth caused by temporary tables.

**Approximate threshold:** [Tens of thousands](#PostgreSQL.HighObjectCount.Note)

## Unlogged tables
<a name="PostgreSQL.HighObjectCount.UnloggedTables"></a>

Unlogged tables can offer performance gains as they won't generate any WAL information. They must be used carefully as they offer no durability during database crash recovery as they will be truncated. This is an expensive operation in PostgreSQL as each unlogged table is truncated serially. While this operation is fast for a low number of unlogged tables, when they number in the thousands it can start to add notable delay during startup.

**Impact: Logical replication**  
Unlogged tables are generally not included in logical replication, including [Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html), because logical replication relies on the WAL to capture and transfer changes. Read more on how to configure Aurora PostgreSQL to [replicate unlogged tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-unlogged-tables.html#aurora-postgresql-unlogged-tables-logicalrep).

**Impact: Reader Nodes**  
You can access unlogged tables only from the writer node in the Aurora DB cluster. See [Working with unlogged tables in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-unlogged-tables.html) for full details.

**General best practices:**
+ Unlogged tables provide limited performance benefits in Aurora PostgreSQL compared to standard PostgreSQL, so evaluate whether normal tables are more appropriate.

**Approximate threshold:** [Thousands](#PostgreSQL.HighObjectCount.Note)

## Partitions
<a name="PostgreSQL.HighObjectCount.Partitions"></a>

Partitioning can increase query performance and provide a logical organization of data. In ideal scenarios, partitioning is organized so that partition pruning can be used during query planning and execution. Using too many partitions can have negative impacts on query performance and database maintenance. The choice of how to partition a table should be made carefully, as the performance of query planning and execution can be negatively affected by poor design. See [PostgreSQL documentation](https://www.postgresql.org/docs/current/ddl-partitioning.html) for details about partitioning.

**Impact: General performance degradation**  
Sometimes planning time overhead will increase and explain plans for your queries will become more complicated, making it difficult to identify tuning opportunities. For PostgreSQL versions earlier than 18, many partitions with high workload can lead to `LWLock:LockManager` waits.  
**Recommended action:** Determine a minimum number of partitions that will allow you to complete both the organization of your data while at the same time providing performant query execution.

**Impact: Maintenance complexity**  
Very high number of partitions will introduce maintenance difficulties like pre-creation and removal. Autovacuum will treat partitions as normal relations and have to perform regular cleanup, therefore requiring enough workers to complete the task.  
**Recommended action:**  
+ Ensure you precreate partitions so that workload isn't blocked when a new partition is needed (for example, monthly based partitions) and old partitions are rolled off.
+ Ensure you have enough autovacuum workers to perform normal cleanup maintenance of all partitions.

**Approximate threshold:** [Hundreds](#PostgreSQL.HighObjectCount.Note)

## Temporary files
<a name="PostgreSQL.HighObjectCount.TempFiles"></a>

Different than temporary tables mentioned above, temporary files are created by PostgreSQL when a complex query might perform several sort or hash operations at the same time, with each operation using instance memory to store results up to the value specified in the `work_mem` parameter. When the instance memory is not sufficient, temporary files are created to store the results. See [Managing temporary files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ManagingTempFiles.html) for more details on temporary files. If your workload generates high numbers of these files, there can be several impacts.

**Impact: FreeLocalStorage consumption**  
Temporary files are a necessary part of PostgreSQL when query results are unable to fit in work\_mem. Generally this is fine. However, when the workload uses this extensively, that indicates large queries are continually running and you will observe a decrease in FreeLocalStorage. See [Managing temporary files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ManagingTempFiles.html) for more details.

**General best practices:**
+ Monitor your temp file usage with [Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html).
+ Tune queries that are generating significant temporary files to see if it's possible to reduce the total number of temp files.

**Approximate threshold:** [Thousands](#PostgreSQL.HighObjectCount.Note)

## Sequences
<a name="PostgreSQL.HighObjectCount.Sequences"></a>

Sequences are the underlying object used for auto-incrementing columns in PostgreSQL and they provide uniqueness and a key for the data. These can be used on individual tables with no consequence during normal operations with one exception of logical replication.

In PostgreSQL, logical replication does not currently replicate a sequence's current value to any subscriber. To learn more, see the [Restrictions page in PostgreSQL documentation](https://www.postgresql.org/docs/current/logical-replication-restrictions.html).

**Impact: Extended switchover time**  
If you plan to use [Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) for any type of configuration change or upgrade, it is important to understand the impact of a high number of sequences on switchover. One of the last phases of a switchover will synchronize the current value of sequences, and if there are several thousand, this will increase the overall switchover time.  
**Recommended action:** If your database workload would allow for the use of a shared UUID instead of a sequence-per-table approach, this would cut down on the synchronization step during a switchover.

**Approximate threshold:** [Thousands](#PostgreSQL.HighObjectCount.Note)

## Large objects
<a name="PostgreSQL.HighObjectCount.LargeObjects"></a>

Large objects are stored in a single system table named pg\_largeobject. Each large object also has an entry in the system table pg\_largeobject\_metadata. These objects are created, modified and cleaned up much differently than standard relations. Large objects are not handled by autovacuum and must be periodically cleaned up via a separate process called vacuumlo. See managing large objects with the lo module for examples on managing large objects.

**Impact: Logical replication**  
Large objects are not currently replicated in PostgreSQL during logical replication. To learn more, see the [Restrictions page in PostgreSQL documentation](https://www.postgresql.org/docs/current/logical-replication-restrictions.html). In a [Blue/Green](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) configuration, this means large objects in the blue environment aren't replicated to the green environment.

**Impact: Major version upgrade**  
An upgrade can run out of memory and fail if there are millions of large objects and the instance cannot handle them during an upgrade. The PostgreSQL major version upgrade process comprises of two broad phases: dumping the schema via pg\_dump and restoring it through pg\_restore. If your database has millions of large objects you need to ensure your instance has sufficient memory to handle the pg\_dump and pg\_restore during an upgrade and scale it to a larger instance type.

**General best practices:**
+ Regularly use the vacuumlo utility to remove any orphaned large objects you may have.
+ Consider using the BYTEA datatype for storing your large objects in the database.

**Approximate threshold:** [Millions](#PostgreSQL.HighObjectCount.Note)

## Approximate thresholds
<a name="PostgreSQL.HighObjectCount.Note"></a>

The approximate thresholds mentioned in this topic are only used to provide an estimate of how far a particular resource can scale. They represent the general range where the described impacts become more likely, but actual behavior depends on your specific workload, instance size, and configuration. While it may be possible to exceed these estimates, care and maintenance must be adhered to so as to avoid the impacts listed.