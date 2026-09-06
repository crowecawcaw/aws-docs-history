

# Troubleshooting out-of-memory issues for Aurora MySQL databases
<a name="AuroraMySQLOOM"></a>

When an Aurora MySQL DB instance runs critically low on memory, the operating system can terminate the database process, causing an unplanned restart. To help prevent these restarts, Aurora MySQL includes memory management capabilities that monitor system memory and take automatic recovery actions when memory is low. These actions help prevent database unavailability due to memory exhaustion.

The following parameters control this behavior:
+ `aurora_enable_memory_management` – Available only in Aurora MySQL 8.4.
  + When `ON` (default), Aurora automatically manages memory recovery actions and the `aurora_oom_response` parameter is ignored.
  + Set to `OFF` to manually control recovery actions through `aurora_oom_response`.
+ `aurora_oom_response` – A comma-separated list of recovery actions. An empty string disables all actions. Available in Aurora MySQL version 3. Also available in Aurora MySQL 8.4 but only considered when `aurora_enable_memory_management` is set to `OFF`.

## OOM response actions
<a name="AuroraMySQLOOM.actions"></a>

The following actions can be included in `aurora_oom_response`, listed from least to most aggressive.


| Action | What it does | Notes | 
| --- | --- | --- | 
| print | Logs memory-intensive queries and connections to the error log. No queries or connections are terminated. | Available in Aurora MySQL versions 3 and 8.4. | 
| tune | Shrinks internal table caches (table\_open\_cache, table\_definition\_cache) to free memory. Cache sizes are restored when memory returns to normal. Previously cached entries are not restored; new entries are only added as subsequent queries access them. | Available in Aurora MySQL versions 3 and 8.4. Provisioned instances only – not supported on Serverless v2. | 
| tune\_buffer\_pool | Shrinks the InnoDB buffer pool to free memory. Buffer pool size is restored when memory returns to normal. Previously cached pages that were evicted are not reloaded automatically; new pages are cached only as subsequent queries access them. | Aurora MySQL version 3 (3.06 and higher) and Aurora MySQL 8.4 only. Supported on provisioned instances with 2 vCPUs only. Not supported on Serverless v2. | 
| decline | Rejects new queries with an error while memory is low. | Available in Aurora MySQL versions 3 and 8.4. | 
| kill\_query | Terminates running SELECT queries, starting with the highest memory consumers, until memory returns to normal. DDL, other DML, and transactions are not affected. | Available in Aurora MySQL versions 3 and 8.4. Mutually exclusive with kill\_connect – if both are set, only kill\_connect activates. | 
| kill\_connect | Terminates user connections, rolling back their active transactions and terminating DDL statements. | See version-specific behavior below. | 

**Important**  
You must pair `tune_buffer_pool` with either `kill_query` or `kill_connect` in the `aurora_oom_response` parameter value. Without one of these, buffer pool resizing does not occur even when `tune_buffer_pool` is included.

### kill\_connect version-specific behavior
<a name="AuroraMySQLOOM.actions.kill_connect"></a>


| Aurora MySQL version | Behavior | 
| --- | --- | 
| Aurora MySQL 3.04 – Aurora MySQL 3.10 | Terminates user connections to free enough memory for the database to recover from memory pressure. | 
| Aurora MySQL 3.11\+, Aurora MySQL 8.4 | Terminates user connections to free enough memory for the database to recover from memory pressure. Also terminates any user connection that attempts to allocate memory during memory pressure. | 

On Serverless v2, Aurora responds to memory pressure by first scaling up ACUs to provide additional memory. If memory pressure persists while scaling is in progress, Aurora may terminate existing connections to recover memory. Termination of connections that try to allocate memory only occurs when the instance has reached its configured maximum ACU limit and can no longer scale further.

## Default values by version
<a name="AuroraMySQLOOM.defaults"></a>

Aurora MySQL automatically configures `aurora_oom_response` based on engine version, instance type, and available memory.

In Aurora MySQL 8.4, when `aurora_enable_memory_management` is `ON` (the default), Aurora automatically manages memory recovery actions, and the `aurora_oom_response` value is not used. When set to `OFF`, Aurora uses the `aurora_oom_response` value directly, which is empty by default – meaning no recovery actions are taken unless you explicitly configure them. The following defaults table applies to Aurora MySQL version 3 only.

**Small instance threshold:** ≤2 GiB for versions 3.04 and 3.05. ≤4 GiB for version 3.06 and higher.

**Large instance threshold:** >2 GiB for versions 3.04 and 3.05. >4 GiB for version 3.06 and higher.


| Version | Instance size | Provisioned | Serverless v2 | 
| --- | --- | --- | --- | 
| Aurora MySQL 3.04–Aurora MySQL 3.05 | Small | print,tune | print | 
|  | Large | disabled | disabled | 
| Aurora MySQL 3.06 | Small | print,tune,decline,kill\_connect | print | 
|  | Large | disabled | disabled | 
| Aurora MySQL 3.07 | Small | print,tune,decline,kill\_connect | print | 
|  | Large | print | print | 
| Aurora MySQL 3.08 | Small | print,tune,tune\_buffer\_pool,decline,kill\_connect | print | 
|  | Large | print | print | 
| Aurora MySQL 3.09–Aurora MySQL 3.10 | Small | print,tune,tune\_buffer\_pool,decline,kill\_connect | print | 
|  | Large | print,decline,kill\_connect | print,decline,kill\_connect | 
| Aurora MySQL 3.11\+ | Small | print,tune,tune\_buffer\_pool,decline,kill\_connect | print,decline,kill\_connect | 
|  | Large | print,decline,kill\_connect | print,decline,kill\_connect | 

## Aurora Serverless v2
<a name="AuroraMySQLOOM.serverless"></a>

The `tune` and `tune_buffer_pool` actions are not supported on Aurora Serverless v2. All other actions work the same as on provisioned instances.

Memory thresholds adjust dynamically as the instance scales its ACUs. The Serverless v2 column in the defaults table above shows the effective defaults for each version.

## Monitoring
<a name="AuroraMySQLOOM.monitoring"></a>

You can monitor OOM avoidance activity through the following methods.

### Error log
<a name="AuroraMySQLOOM.monitoring.errorlog"></a>

When memory recovery actions are taken, Aurora MySQL writes messages to the database error log. The message prefix varies by version and may change in future releases:
+ **Aurora MySQL version 3:** Messages are prefixed with `OOM crash avoidance:`.
+ **Aurora MySQL version 8.4:** Messages are prefixed with `Aurora memory management:`.

These messages include:
+ Memory pressure detected and recovered notifications with total and available memory
+ Details of queries or connections terminated for memory recovery
+ Candidate queries identified by the `print` action

To view the error log, see [Aurora MySQL error logs](USER_LogAccess.MySQL.LogFileSize.md#USER_LogAccess.MySQL.Errorlog).

### Amazon CloudWatch metrics
<a name="AuroraMySQLOOM.monitoring.cloudwatch"></a>

The following CloudWatch metrics track OOM avoidance activity at the instance level.


| Metric | Description | Available from | Unit | 
| --- | --- | --- | --- | 
| AuroraMemoryHealthState | Indicates the memory health state. 0 means healthy (no memory pressure), 5 means moderate memory pressure, 10 means critical memory pressure. | Aurora MySQL 3.06.1\+, Aurora MySQL 8.4 | Gauge | 
| AuroraMemoryNumDeclinedSqlTotal | The incremental number of queries declined as part of OOM avoidance. | Aurora MySQL 3.06.1\+, Aurora MySQL 8.4 | Count | 
| AuroraMemoryNumKillConnTotal | The incremental number of connections closed as part of OOM avoidance. | Aurora MySQL 3.06.1\+, Aurora MySQL 8.4 | Count | 
| AuroraMemoryNumKillQueryTotal | The incremental number of queries terminated as part of OOM avoidance. | Aurora MySQL 3.06.1\+, Aurora MySQL 8.4 | Count | 
| AuroraMillisecondsSpentInOomRecovery | The amount of time since memory health dropped below the normal state. | Aurora MySQL 3.08.0\+, Aurora MySQL 8.4 | Milliseconds | 
| AuroraNumOomRecoverySuccessful | The number of times memory health was restored to the normal state. | Aurora MySQL 3.08.0\+, Aurora MySQL 8.4 | Count | 
| AuroraNumOomRecoveryTriggered | The number of times memory health dropped below the normal state. | Aurora MySQL 3.08.0\+, Aurora MySQL 8.4 | Count | 

The following general CloudWatch metrics are also useful for monitoring memory pressure:


| Metric | Description | Unit | 
| --- | --- | --- | 
| FreeableMemory | The amount of available memory. Reports the MemAvailable value from /proc/meminfo. | Bytes | 
| SwapUsage | The amount of swap space used. | Bytes | 

For the full list of Aurora MySQL instance-level metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.Metrics.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances).

### Global status variables
<a name="AuroraMySQLOOM.monitoring.statusvars"></a>

The following status variables provide information about OOM state. Available in Aurora MySQL version 3.06.0 and higher.


| Variable | Description | 
| --- | --- | 
| Aurora\_oom\_response | The currently active OOM response actions for this DB instance. | 
| aurora\_oom\_avoidance\_recovery\_state | Whether OOM recovery is ACTIVE or INACTIVE. | 
| aurora\_oom\_status | Current memory health state of the database: healthy (no memory pressure), moderate memory pressure, or critical memory pressure. Available in version 3 only. | 

To query: `SHOW GLOBAL STATUS LIKE 'aurora_oom%';`

For the full list of Aurora MySQL global status variables, see [Aurora MySQL global status variables](AuroraMySQL.Reference.GlobalStatusVars.md).

### Performance Insights
<a name="AuroraMySQLOOM.monitoring.pi"></a>

If Performance Insights is enabled, you can use OS-level memory metrics to monitor memory pressure and detect OOM events. The following metrics are available under the `os.memory` and `os.swap` counters:


| Metric | Description | 
| --- | --- | 
| os.memory.outOfMemoryKillCount | The number of OOM kills over the last collection interval. A non-zero value indicates the operating system terminated a process due to memory exhaustion, which typically results in a database restart. | 
| os.memory.total | The total amount of memory, in kilobytes. | 
| os.memory.free | The amount of unassigned memory, in kilobytes. | 
| os.memory.active | The amount of assigned memory, in kilobytes. | 
| os.memory.cached | The amount of memory used for caching file system I/O, in kilobytes. | 
| os.memory.dirty | The amount of memory pages modified but not yet written to storage, in kilobytes. | 
| os.memory.inactive | The amount of least-frequently used memory pages, in kilobytes. | 
| os.memory.db.residentSetSize | The amount of memory used by the database process (excluding shared memory), in bytes. | 
| os.memory.db.cache | The amount of memory used for page cache by the database process, in bytes. | 
| os.memory.db.swap | The amount of swap memory used by the database process, in bytes. | 
| os.swap.in | The amount of memory swapped in from disk, in kilobytes. | 
| os.swap.out | The amount of memory swapped out to disk, in kilobytes. | 

You can monitor `os.memory.outOfMemoryKillCount` to detect when the OS killed the database process due to out of memory. For the full list of OS counters, see [Operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS).

### Performance Schema
<a name="AuroraMySQLOOM.monitoring.perfschema"></a>

If `performance_schema` is enabled, you can use memory summary tables to identify which components and connections are consuming the most memory. For more information, see [Troubleshooting memory usage issues for Aurora MySQL databases](ams-workload-memory.md).