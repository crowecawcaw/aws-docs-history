

# synch/mutex/innodb/temp\_pool\_manager\_mutex
<a name="ams-waits.io-temppoolmanager"></a>

The `synch/mutex/innodb/temp_pool_manager_mutex` wait event occurs when a session is waiting to acquire a mutex for managing the pool of session temporary tablespaces.

**Topics**
+ [Supported engine versions](#ams-waits.io-temppoolmanager.context.supported)
+ [Context](#ams-waits.io-temppoolmanager.context)
+ [Likely causes of increased waits](#ams-waits.io-temppoolmanager.causes)
+ [Actions](#ams-waits.io-temppoolmanager.actions)

## Supported engine versions
<a name="ams-waits.io-temppoolmanager.context.supported"></a>

This wait event information is supported for the following engine versions:
+ Aurora MySQL version 3

## Context
<a name="ams-waits.io-temppoolmanager.context"></a>

Aurora MySQL version 3.x and higher uses `temp_pool_manager_mutex` to control multiple sessions accessing the temporary tablespace pool at the same time. Aurora MySQL manages storage through an Aurora cluster volume for persistent data and local storage for temporary files. A temporary tablespace is needed when a session creates a temporary table on the Aurora cluster volume. 

When a session first requests a temporary tablespace, MySQL allocates session temporary tablespaces from the shared pool. A session can hold up to 2 temporary tablespaces at a time for the following table types:
+ User-created temporary tables
+ Optimizer-generated internal temporary tables

The default `TempTable` engine uses the following overflow mechanism to handle temporary tables:
+ Stores tables in RAM up to the [`temptable_max_ram`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram) limit.
+ Moves to memory-mapped files on local storage when RAM is full.
+ Uses the shared cluster volume when memory-mapped files reach their [`temptable_max_mmap`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap) limit.

After temporary tables exceed both RAM and local storage limits, MySQL manages them using on-disk tablespace.

When a session requires an on-disk temporary table, MySQL:
+ Looks for available `INACTIVE` tablespaces in the pool to reuse.
+ Creates 10 new tablespaces if no `INACTIVE` spaces exist.

When a session disconnects, MySQL:
+ Truncates the session's temporary tablespaces.
+ Marks them as INACTIVE in the pool for reuse.
+ Maintains the current pool size until server restart.
+ Returns to the default pool size (10 tablespaces) after restart.

## Likely causes of increased waits
<a name="ams-waits.io-temppoolmanager.causes"></a>

Common situations that cause this wait event:
+ Concurrent sessions creating internal temporary tables on the cluster volume.
+ Concurrent sessions creating user temporary tables on the cluster volume.
+ Sudden termination of sessions using active tablespaces.
+ Tablespace pool expansion during heavy write workloads.
+ Concurrent queries accessing `INFORMATION_SCHEMA.`

## Actions
<a name="ams-waits.io-temppoolmanager.actions"></a>

We recommend different actions depending on the causes of your wait event.

**Topics**
+ [Monitor and optimize temporary table usage](#ams-waits.io-temppoolmanager.actions.monitor)
+ [Review queries using INFORMATION\_SCHEMA](#ams-waits.io-temppoolmanager.actions.schema-queries)
+ [Increase innodb\_sync\_array\_size parameter](#ams-waits.io-temppoolmanager.actions.sync_array)
+ [Implement connection pooling](#ams-waits.io-temppoolmanager.actions.connection_pooling)

### Monitor and optimize temporary table usage
<a name="ams-waits.io-temppoolmanager.actions.monitor"></a>

To monitor and optimize temporary table usage, use one of these methods:
+ Check the `Created_tmp_disk_tables` counter in Performance Insights to track on-disk temporary table creation across your Aurora cluster.
+ Run this command in your database to directly monitor temporary table creation: `mysql> show status like '%created_tmp_disk%'`.

**Note**  
Temporary table behavior differs between Aurora MySQL reader nodes and writer nodes. For more information, see [New temporary table behavior in Aurora MySQL version 3](ams3-temptable-behavior.md).

After identifying queries creating temporary tables, take these optimization steps:
+ Use `EXPLAIN` to examine query execution plans and identify where and why temporary tables are being created.
+ Modify queries to reduce temporary table usage where possible.

If query optimization alone doesn't resolve performance issues, consider adjusting these configuration parameters:
+  [`temptable_max_ram`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_ram)- Controls maximum RAM usage for temporary tables.
+  [`temptable_max_mmap`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_temptable_max_mmap) - Sets the limit for memory-mapped file storage.
+ [`tmp_table_size`](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_tmp_table_size)- Applies when `aurora_tmptable_enable_per_table_limit` is enabled (disabled by default).

**Important**  
Note that certain query conditions will always require on-disk temporary tables, regardless of configuration settings. For more information `TempTable` storage engine, see [ Use the TempTable storage engine on Amazon RDS for MySQL and Amazon Aurora MySQL ](https://aws.amazon.com/blogs/database/use-the-temptable-storage-engine-on-amazon-rds-for-mysql-and-amazon-aurora-mysql/).

### Review queries using INFORMATION\_SCHEMA
<a name="ams-waits.io-temppoolmanager.actions.schema-queries"></a>

When you query `INFORMATION_SCHEMA` tables, MySQL creates InnoDB temporary tables on the cluster volume. Each session needs a temporary tablespace for these tables, which can lead to performance issues during high concurrent access.

To improve performance:
+ Use `PERFORMANCE_SCHEMA` instead of `INFORMATION_SCHEMA` where possible.
+ If you must use `INFORMATION_SCHEMA`, reduce how often you run these queries.

### Increase innodb\_sync\_array\_size parameter
<a name="ams-waits.io-temppoolmanager.actions.sync_array"></a>

The `innodb_sync_array_size` parameter controls the size of the mutex/lock wait array in MySQL. The default value of `1` works for general workloads, but increasing it can reduce thread contention during high concurrency.

When your workload shows increasing numbers of waiting threads:
+ Monitor the number of waiting threads in your workload.
+ Set `innodb_sync_array_size` equal to or higher than your instance's vCPU count to split the thread coordination structure and reduce contention.

**Note**  
To determine the number of vCPUs available on your RDS instance, see the vCPU specifications in [ Amazon RDS instance types ](https://aws.amazon.com/rds/instance-types/).

### Implement connection pooling
<a name="ams-waits.io-temppoolmanager.actions.connection_pooling"></a>

MySQL assigns a dedicated tablespace to each session that creates a temporary table. This tablespace remains active until the database connection ends. To manage your resources more efficiently:
+ Implement connection pooling to limit the number of active temporary tablespaces.
+ Reuse existing connections instead of creating new ones for each operation.