# Monitor Microsoft SQL Server resource governor using system views for your RDS for SQL Server instance

Resource Governor statistics are cumulative since the last server restart. If you need to collect statistics starting from a certain time, you can reset statistics using the following Amazon RDS stored procedure:

```
EXEC msdb.dbo.rds_alter_resource_governor_configuration
@reset_statistics = 1;
```

## Resource pool runtime statistics

For each resource pool, resource governor tracks CPU and memory utilization, out-of-memory events,
memory grants, I/O, and other statistics. For more information,
see [sys.dm_resource_governor_resource_pools](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-resource-governor-resource-pools-transact-sql?view=sql-server-ver17 "https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-resource-governor-resource-pools-transact-sql?view=sql-server-ver17").

The following query returns a subset of available statistics for all resource pools:

```
SELECT rp.pool_id,
       rp.name AS resource_pool_name,
       wg.workload_group_count,
       rp.statistics_start_time,
       rp.total_cpu_usage_ms,
       rp.target_memory_kb,
       rp.used_memory_kb,
       rp.out_of_memory_count,
       rp.active_memgrant_count,
       rp.total_memgrant_count,
       rp.total_memgrant_timeout_count,
       rp.read_io_completed_total,
       rp.write_io_completed_total,
       rp.read_bytes_total,
       rp.write_bytes_total,
       rp.read_io_stall_total_ms,
       rp.write_io_stall_total_ms
FROM sys.dm_resource_governor_resource_pools AS rp
OUTER APPLY (
            SELECT COUNT(1) AS workload_group_count
            FROM sys.dm_resource_governor_workload_groups AS wg
            WHERE wg.pool_id = rp.pool_id
            ) AS wg;
```
