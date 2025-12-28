# Oracle SGA and PGA memory sizing and PostgreSQL memory buffers

With AWS DMS, you can optimize database performance by properly sizing memory components like Oracle’s System Global Area (SGA) and Program Global Area (PGA), as well as PostgreSQL’s memory buffers.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                      |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------ |
| Two star feature compatibility | N/A                                | N/A                       | Different cache names, similar usage |

## Oracle usage

An Oracle instance allocates several individual “pools” of server RAM used as various caches for the database. These include the Buffer Cache, Redo Buffer, Java Pool, Shared Pool, Large Pool, and others. The caches reside in the System Global Area (SGA) and are shared across all Oracle sessions.

In addition to the SGA, each Oracle session is granted an additional area of memory for session-private operations (sorting, private SQL cursors elements, and so on) called the Private Global Area (PGA).

Cache size can be controlled for individual caches or globally, and automatically, by an Oracle database. Setting a unified “memory size” parameter enables Oracle to automatically manage individual cache sizes.

- All Oracle memory parameters are set using the `ALTER SYSTEM` command.
- Some changes to memory parameters require an instance restart.

Some of the common Oracle parameters that control memory allocations include:

- `db_cache_size` — The size of the cache used for database data.
- `log_buffer` — The cache used to store Oracle redo log buffers until they are written to disk.
- `shared_pool_size` — The cache used to store shared cursors, stored procedures, control structures, and other structures.
- `large_pool_size` — The cache used for parallel queries and RMAN backup/restore operations.
- `Java_pool_size` — The cache used to store Java code and JVM context.

While these parameters can be configured individually, most database administrators choose to let Oracle automatically manage RAM. Database administrators configure the overall size of the SGA, and Oracle sizes individual caches based on workload characteristics.

- `sga_max_size` — Specifies the hard-limit maximum size of the SGA.
- `sga_target` — Sets the required soft-limit for the SGA and the individual caches within it.

Oracle also allows control over how much private memory is dedicated for each session. Database Administrators configure the total size of memory available for all connecting sessions, and Oracle allocates individual dedicated chunks from the total amount of available memory for each session.

- `pga_aggregate_target` — A soft-limit controlling the total amount of memory available for all sessions combined.
- `pga_aggregate_limit` — A hard-limit for the total amount of memory available for all sessions combined (Oracle 12c only).

In addition, instead of manually configuring the SGA and PGA memory areas, you can also configure one overall memory limit for both the SGA and PGA and let Oracle automatically balance memory between the various memory pools. This behavior is enabled using the `memory_target` and `memory_max_target` parameters.

For more information, see [Memory Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/memory-architecture.html#GUID-913335DF-050A-479A-A653-68A064DCCA41 "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/memory-architecture.html#GUID-913335DF-050A-479A-A653-68A064DCCA41") and [Database Memory Allocation](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/database-memory-allocation.html#GUID-E9265077-B296-485A-BC2C-0AF55762D1EC "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/database-memory-allocation.html#GUID-E9265077-B296-485A-BC2C-0AF55762D1EC") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL provides us with control over how server RAM is allocated. The following table includes some of the most important PostgreSQL memory parameters.

| Memory pool parameter                         | Description                                                                                                                          |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `shared_buffers`                              | Used to cache database data read from disk. Approximate Oracle Database Buffer Cache equivalent.                                     |
| `wal_buffers`                                 | Used to store WAL (Write-Ahead-Log) records before they are written to disk. Approximate Oracle Redo Log Buffer equivalent.          |
| `work_mem`                                    | Used for parallel queries and SQL sort operations. Approximate Oracle PGA equivalent and/or the Large Pool (for parallel workloads). |
| `maintenance_work_mem`                        | Memory used for certain backend database operations such as `VACUUM`, `CREATE INDEX`, `ALTER TABLE ADD FOREIGN KEY`.                 |
| `temp_buffers`                                | Memory buffers used by each database session for reading data from temporary tables.                                                 |
| Total memory available for PostgreSQL cluster | Controlled by choosing the \*_DB Instance Class_<br>• during instance creation.<br>Instance creation                                 |

Cluster level parameters, such as `shared_buffers` and `wal_buffers`, are configured using parameter groups in the Amazon RDS Management Console.

**Examples**

View the configured values for database parameters.

```
show shared_buffers

show work_mem

show temp_buffers
```

View the configured values for all database parameters.

```
select * from pg_settings;
```

Use of the `SET SESSION` command to modify the value of parameters that support session-specific settings. Changing the value using the `SET SESSION` command for one session will have no effect on other sessions.

```
SET SESSION work_mem='100MB';
```

If a `SET SESSION` command is issued within a transaction that is aborted or rolled back, the effects of the `SET SESSION` command disappear. Once the transaction is committed, the effects will become persistent until the end of the session, unless overridden by another execution of `SET SESSION`.

Use of the `SET LOCAL` command to modify the current value of those parameters that can be set locally to a single transaction. Changing the value using the `SET LOCAL` command for one transaction will have no subsequent effect on other transactions from the same session. After issuing a `COMMIT` or `ROLLBACK`, the session-level settings will take effect.

```
SET LOCAL work_mem='100MB';
```

Reset a value of a run-time parameter to its default value.

```
RESET work_mem;
```

Changing parameter values can also be done with a direct update to the `pg_settings` table.

```
UPDATE pg_settings SET setting = '100MB' WHERE name = 'work_mem';
```

## Summary

Use the following table as a general reference only. Functionality may not be identical across Oracle and PostgreSQL.

| Description                                                  | Oracle                                       | PostgreSQL                                                                                                                   |
| ------------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Memory for caching table data                                | db_cache_size                                | shared_buffers                                                                                                               |
| Memory for transaction log records                           | log_buffer                                   | wal_buffers                                                                                                                  |
| Memory for parallel queries                                  | large_pool_size                              | work_mem                                                                                                                     |
| Java code and JVM                                            | Java_pool_size                               | N/A                                                                                                                          |
| Maximum amount of physical memory available for the instance | sga_max_size or memory_max_size              | Configured by the Amazon RDS/Aurora instance class<br>For example:<br>`<br>db.r3.large: 15.25GB<br>db.r3.xlarge: 30.5GB<br>` |
| Total amount of private memory for all sessions              | pga_aggregate_target and pga_aggregate_limit | temp_buffers (for reading data from temp tables), work_mem (for sorts)                                                       |
| View values for all database parameters                      | `<br>SELECT<br>• FROM v$parameter;<br>`      | `<br>Select<br>• from pg_settings;<br>`                                                                                      |
| Configure a session-level parameter                          | `<br>ALTER SESSION SET ...<br>`              | `<br>SET SESSION ...<br>`                                                                                                    |
| Configure instance-level parameter                           | `<br>ALTER SYSTEM SET ...<br>`               | Configured by parameter groups in the Amazon RDS Management Console.                                                         |

For more information, see [Write Ahead Log](https://www.postgresql.org/docs/13/runtime-config-wal.html "https://www.postgresql.org/docs/13/runtime-config-wal.html") and [Resource Consumption](https://www.postgresql.org/docs/13/runtime-config-resource.html "https://www.postgresql.org/docs/13/runtime-config-resource.html") in the _PostgreSQL documentation_.
