# Oracle SGA and PGA memory sizing and MySQL memory buffers

With AWS DMS, you can optimize memory utilization for migrated databases by configuring Oracle System Global Area (SGA) and Program Global Area (PGA) memory sizes, as well as MySQL memory buffers. The SGA is a group of shared memory structures that contain data and control information for an Oracle database instance, while the PGA is a memory region that contains data and control information for a server process. MySQL memory buffers, such as the buffer pool and query cache, manage data caching and query performance.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                       |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | Different cache names, similar usage. |

## Oracle usage

An Oracle instance allocates several individual pools of server RAM used as various caches for the database. These include the Buffer Cache, Redo Buffer, Java Pool, Shared Pool, Large Pool, and others. The caches reside in the System Global Area (SGA) and are shared across all Oracle sessions.

In addition to the SGA, each Oracle session is granted an additional area of memory for session-private operations (sorting, private SQL cursors elements, and so on) called the Private Global Area (PGA).

You can control cache size for individual caches or globally, and automatically, by an Oracle database. Setting a unified memory size parameter enables Oracle to automatically manage individual cache sizes.

- All Oracle memory parameters are set using the `ALTER SYSTEM` command.
- Some changes to memory parameters require an instance restart.

Some of the common Oracle parameters that control memory allocations include:

- `db_cache_size` — The size of the cache used for database data.
- `log_buffer` — The cache used to store Oracle redo log buffers until they are written to disk.
- `shared_pool_size` — The cache used to store shared cursors, stored procedures, control structures, and other structures.
- `large_pool_size` — The caches used for parallel queries and RMAN backup/restore operations.
- `Java_pool_size` — The caches used to store Java code and JVM context.

While these parameters can be configured individually, most database administrators choose to let Oracle automatically manage RAM. Database administrators configure the overall size of the SGA, and Oracle sizes individual caches based on workload characteristics.

- `sga_max_size` — Specifies the hard-limit maximum size of the SGA.
- `sga_target` — Sets the required soft-limit for the SGA and the individual caches within it.

Oracle also provides control over how much private memory is dedicated for each session. Database Administrators configure the total size of memory available for all connecting sessions, and Oracle allocates individual dedicated chunks from the total amount of available memory for each session.

- `pga_aggregate_target` — A soft-limit controlling the total amount of memory available for all sessions combined.
- `pga_aggregate_limit` — A hard-limit for the total amount of memory available for all sessions combined (Oracle 12c only).

In addition, instead of manually configuring the SGA and PGA memory areas, you can also configure one overall memory limit for both the SGA and PGA and let Oracle automatically balance memory between the various memory pools. This behavior is configured by the `memory_target` and `memory_max_target` parameters.

For more information, see [Memory Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/memory-architecture.html#GUID-913335DF-050A-479A-A653-68A064DCCA41 "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/memory-architecture.html#GUID-913335DF-050A-479A-A653-68A064DCCA41") and [Database Memory Allocation](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/database-memory-allocation.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/database-memory-allocation.html") in the _Oracle documentation_.

## MySQL usage

Such as other databases, MySQL uses different memory buffers for different purposes. In MySQL, there are several storage engines that use different memory buffers. This section refers to InnoDB only.

MySQL provides control over how server RAM is allocated. Some of the most important MySQL memory parameters include:

| Memory pool parameter                      | Description                                                                                    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `innodb_buffer_pool_size`                  | The memory area where InnoDB caches table and index data.                                      |
| `optimizer_trace_max_mem_size`             | Buffer for optimizer traces.                                                                   |
| `binlog_cache_size`                        | The size of the cache holding changes to the binary log during a transaction.                  |
| `host_cache_size`                          | Buffer area to store data on connections.                                                      |
| `innodb_ft_cache_size`                     | Very similar to innodb_buffer_pool_size but only for data related to `FULL_TEXT` indexes.      |
| `stored_program_cache`                     | Cached stored routines per connection.                                                         |
| `sort_buffer_size`                         | Size of sort buffers used to sort data during creation of an InnoDB index.                     |
| Total memory available for a MySQL cluster | Controlled by selecting the `DB Instance Class` during instance creation:<br>DB Instance Class |

###### Note

You can configure cluster-level parameters such as `innodb_buffer_pool_size` and `binlog_cache_size` using parameter groups in the Amazon Relational Database Service console.

### Examples

View the configured values for database parameters.

```
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SHOW VARIABLES LIKE 'binlog_cache_size';
SHOW VARIABLES LIKE 'stored_program_cache';
```

View the configured values for all database parameters.

```
SELECT * FROM information_schema.GLOBAL_VARIABLES
```

Use the `SET SESSION` command to modify the value of parameters that support session-specific settings. Changing the value for one session has no effect on other sessions.

```
SET SESSION sort_buffer_size = 1000000;
```

## Summary

Use the table below as a general reference only. Functionality may not be identical across Oracle and MySQL.

| Description                                                  | Oracle                                           | MySQL                                                                                                                                                                              |
| ------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Memory for caching table data                                | `db_cache_size`                                  | `innodb_buffer_pool_size`                                                                                                                                                          |
| Memory for transaction log records                           | `log_buffer`                                     | `binlog_cache_size`                                                                                                                                                                |
| Memory for parallel queries                                  | `large_pool_size`                                | N/A                                                                                                                                                                                |
| Java code and JVM                                            | `Java_pool_size`                                 | N/A                                                                                                                                                                                |
| Maximum amount of physical memory available for the instance | `sga_max_size` or `memory_max_size`              | Configured by the Amazon Relational Database Service or Amazon Aurora instance class.<br>Consider the following example:<br>`<br>db.r3.large: 15.25GB<br>db.r3.xlarge: 30.5GB<br>` |
| Total amount of private memory for all sessions              | `pga_aggregate_target` and `pga_aggregate_limit` | `max_digest_length`                                                                                                                                                                |
| View values for all database parameters                      | `<br>SELECT<br>• FROM v$parameter;<br>`          | `<br>SELECT<br>• FROM information_schema.GLOBAL_VARIABLES<br>`                                                                                                                     |
| Configure a session-level parameter                          | `<br>ALTER SESSION SET ...<br>`                  | `<br>SET SESSION ...<br>`                                                                                                                                                          |
| Configure instance-level parameter                           | `<br>ALTER SYSTEM SET ...<br>`                   | Configured through parameter groups in the Amazon Relational Database Service console.                                                                                             |

For more information, see [InnoDB Startup Options and System Variables](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html") and [How MySQL Uses Memory](https://dev.mysql.com/doc/refman/5.7/en/memory-use.html "https://dev.mysql.com/doc/refman/5.7/en/memory-use.html") in the _MySQL documentation_.
