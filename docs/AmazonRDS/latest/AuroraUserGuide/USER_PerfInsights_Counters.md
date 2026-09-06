

# Detailed Database Metrics
<a name="USER_PerfInsights_Counters"></a>

Counter metrics are operating system and database performance metrics. These metrics are exposed through the Performance Insights API. To help identify and analyze performance problems, you can correlate counter metrics with DB load. You must append a statistic function to the metric to get the metric values. For example, the supported functions for `os.memory.active` metric are `.avg`, `.min`, `.max`, `.sum`, and `.sample_count`. 

The counter metrics are collected one time each minute. The OS metrics collection depends on whether Enhanced Monitoring is turned on or off. If Enhanced Monitoring is turned off, the OS metrics are collected one time each minute. If Enhanced Monitoring is turned on, the OS metrics are collected for the selected time period. For more information about turning Enhanced Monitoring on or off, see [Turning Enhanced Monitoring on and off](USER_Monitoring.OS.Enabling.md#USER_Monitoring.OS.Enabling.Procedure).

**Topics**
+ [Operating system counters](#USER_PerfInsights_Counters.OS)
+ [Detailed Database Metrics for Aurora MySQL](#USER_PerfInsights_Counters.Aurora_MySQL)
+ [Detailed Database Metrics for Aurora PostgreSQL](#USER_PerfInsights_Counters.Aurora_PostgreSQL)

## Operating system counters
<a name="USER_PerfInsights_Counters.OS"></a>

The following operating system counters, which are prefixed with `os`, are available through the Performance Insights API for Aurora PostgreSQL and Aurora MySQL.

You can use `ListAvailableResourceMetrics` API for the list of available counter metrics for your DB instance. For more information, see [ ListAvailableResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceMetrics) in the Amazon RDS Performance Insights API Reference guide.


| Counter | Type | Unit | Metric | Description | 
| --- | --- | --- | --- | --- | 
| Active | Memory | Kilobytes | os.memory.active | The amount of assigned memory, in kilobytes. | 
| Buffers | Memory | Kilobytes | os.memory.buffers | The amount of memory used for buffering I/O requests prior to writing to the storage device, in kilobytes. | 
| Cached | Memory | Kilobytes | os.memory.cached | The amount of memory used for caching file system–based I/O, in kilobytes. | 
| DB Cache | Memory | Bytes | os.memory.db.cache | The amount of memory used for page cache by database process including tmpfs (shmem), in bytes. | 
| DB Resident Set Size | Memory | Bytes | os.memory.db.residentSetSize | The amount of memory used for anonymous and swap cache by database process not including tmpfs (shmem), in bytes. | 
| DB Swap | Memory | Bytes | os.memory.db.swap |  The amount of memory used for swap by database process, in bytes. | 
| Dirty | Memory | Kilobytes | os.memory.dirty | The amount of memory pages in RAM that have been modified but not written to their related data block in storage, in kilobytes. | 
| Free | Memory | Kilobytes | os.memory.free | The amount of unassigned memory, in kilobytes. | 
| Huge Pages Free | Memory | Pages | os.memory.hugePagesFree | The number of free huge pages. Huge pages are a feature of the Linux kernel. | 
| Huge Pages Rsvd | Memory | Pages | os.memory.hugePagesRsvd | The number of committed huge pages. | 
| Huge Pages Size | Memory | Kilobytes | os.memory.hugePagesSize | The size for each huge pages unit, in kilobytes. | 
| Huge Pages Surp | Memory | Pages | os.memory.hugePagesSurp | The number of available surplus huge pages over the total. | 
| Huge Pages Total | Memory | Pages | os.memory.hugePagesTotal | The total number of huge pages. | 
| Inactive | Memory | Kilobytes | os.memory.inactive | The amount of least-frequently used memory pages, in kilobytes. | 
| Mapped | Memory | Kilobytes | os.memory.mapped | The total amount of file-system contents that is memory mapped inside a process address space, in kilobytes. | 
| Out of Memory Kill Count | Memory | Kills | os.memory.outOfMemoryKillCount | The number of OOM kills that happened over the last collection interval. | 
| Page Tables | Memory | Kilobytes | os.memory.pageTables | The amount of memory used by page tables, in kilobytes. | 
| Slab | Memory | Kilobytes | os.memory.slab | The amount of reusable kernel data structures, in kilobytes. | 
| Total | Memory | Kilobytes | os.memory.total | The total amount of memory, in kilobytes. | 
| Writeback | Memory | Kilobytes | os.memory.writeback | The amount of dirty pages in RAM that are still being written to the backing storage, in kilobytes. | 
| Guest | Cpu Utilization | Percentage | os.cpuUtilization.guest | The percentage of CPU in use by guest programs. | 
| Idle | Cpu Utilization | Percentage | os.cpuUtilization.idle | The percentage of CPU that is idle. | 
| Irq | Cpu Utilization | Percentage | os.cpuUtilization.irq | The percentage of CPU in use by software interrupts. | 
| Nice | Cpu Utilization | Percentage | os.cpuUtilization.nice | The percentage of CPU in use by programs running at lowest priority. | 
| Steal | Cpu Utilization | Percentage | os.cpuUtilization.steal | The percentage of CPU in use by other virtual machines. | 
| System | Cpu Utilization | Percentage | os.cpuUtilization.system | The percentage of CPU in use by the kernel. | 
| Total | Cpu Utilization | Percentage | os.cpuUtilization.total | The total percentage of the CPU in use. This value includes the nice value. | 
| User | Cpu Utilization | Percentage | os.cpuUtilization.user | The percentage of CPU in use by user programs. | 
| Wait | Cpu Utilization | Percentage | os.cpuUtilization.wait | The percentage of CPU unused while waiting for I/O access. | 
|  Aurora Storage Aurora Storage Bytes Rx  | Disk IO | Bytes per second | os.diskIO.auroraStorage.auroraStorageBytesRx | The number of bytes received from Aurora storage per second. | 
|  Aurora Storage Aurora Storage Bytes Tx  | Disk IO | Bytes per second | os.diskIO.auroraStorage.auroraStorageBytesTx | The number of bytes uploaded to aurora storage per second. | 
| Aurora Storage Disk Queue Depth | Disk IO | Requests | os.diskIO.auroraStorage.diskQueueDepth | The length of Aurora storage disk queue. | 
| Aurora Storage Read IOs PS | Disk IO | Requests per second | os.diskIO.auroraStorage.readIOsPS | The number of read operations per second. | 
| Aurora Storage Read Latency | Disk IO | Milliseconds | os.diskIO.auroraStorage.readLatency | The average latency of a read I/O request to Aurora storage, in milliseconds. | 
| Aurora Storage Read Throughput | Disk IO | Bytes per second | os.diskIO.auroraStorage.readThroughput | The amount of network throughput used by requests to the DB cluster, in bytes per second. | 
| Aurora Storage Write IOs PS | Disk IO | Requests per second | os.diskIO.auroraStorage.writeIOsPS | The number of write operations per second. | 
| Aurora Storage Write Latency | Disk IO | Milliseconds | os.diskIO.auroraStorage.writeLatency | The average latency of a write I/O request to Aurora storage, in milliseconds. | 
| Aurora Storage Write Throughput | Disk IO | Bytes per second | os.diskIO.auroraStorage.writeThroughput | The amount of network throughput used by responses from the DB cluster, in bytes per second. | 
| Rdstemp Avg Queue Len | Disk IO | Requests | os.diskIO.rdstemp.avgQueueLen | The number of requests waiting in the I/O device's queue. | 
| Rdstemp Avg Req Sz | Disk IO | Requests | os.diskIO.rdstemp.avgReqSz | The number of requests waiting in the I/O device's queue. | 
| Rdstemp Await | Disk IO | Milliseconds | os.diskIO.rdstemp.await | The number of milliseconds required to respond to requests, including queue time and service time. | 
| Rdstemp Read IOs PS | Disk IO | Requests | os.diskIO.rdstemp.readIOsPS | The number of read operations per second. | 
| Rdstemp Read KB | Disk IO | Kilobytes | os.diskIO.rdstemp.readKb | The total number of kilobytes read. | 
| Rdstemp Read KB PS | Disk IO | Kilobytes per second | os.diskIO.rdstemp.readKbPS | The number of kilobytes read per second. | 
| Rdstemp Rrqm PS | Disk IO | Requests per second | os.diskIO.rdstemp.rrqmPS | The number of merged read requests queued per second. | 
| Rdstemp TPS | Disk IO | Transactions per second | os.diskIO.rdstemp.tps | The number of I/O transactions per second. | 
| Rdstemp Util | Disk IO | Percentage | os.diskIO.rdstemp.util | The percentage of CPU time during which requests were issued. | 
| Rdstemp Write IOs PS | Disk IO | Requests per second | os.diskIO.rdstemp.writeIOsPS | The number of write operations per second. | 
| Rdstemp Write KB | Disk IO | Kilobytes | os.diskIO.rdstemp.writeKb | The total number of kilobytes written. | 
| Rdstemp Write KB PS | Disk IO | Kilobytes per second | os.diskIO.rdstemp.writeKbPS | The number of kilobytes written per second. | 
| Rdstemp Wrqm PS | Disk IO | Requests per second | os.diskIO.rdstemp.wrqmPS | The number of merged write requests queued per second. | 
| Blocked | Tasks | Tasks | os.tasks.blocked | The number of tasks that are blocked. | 
| Running | Tasks | Tasks | os.tasks.running | The number of tasks that are running. | 
| Sleeping | Tasks | Tasks | os.tasks.sleeping | The number of tasks that are sleeping. | 
| Stopped | Tasks | Tasks | os.tasks.stopped | The number of tasks that are stopped. | 
| Total | Tasks | Tasks | os.tasks.total | The total number of tasks. | 
| Zombie | Tasks | Tasks | os.tasks.zombie | The number of child tasks that are inactive with an active parent task. | 
| One | Load Average Minute | Processes | os.loadAverageMinute.one | The number of processes requesting CPU time over the last minute. | 
| Fifteen | Load Average Minute | Processes | os.loadAverageMinute.fifteen | The number of processes requesting CPU time over the last 15 minutes. | 
| Five | Load Average Minute | Processes | os.loadAverageMinute.five | The number of processes requesting CPU time over the last 5 minutes. | 
| Cached | Swap | Kilobytes | os.swap.cached | The amount of swap memory, in kilobytes, used as cache memory. | 
| Free | Swap | Kilobytes | os.swap.free | The amount of swap memory free, in kilobytes.  | 
| In | Swap | Kilobytes | os.swap.in | The amount of memory, in kilobytes, swapped in from disk. | 
| Out | Swap | Kilobytes | os.swap.out | The amount of memory, in kilobytes, swapped out to disk. | 
| Total | Swap | Kilobytes | os.swap.total | The total amount of swap memory available in kilobytes. | 
| Max Files | File Sys | Files | os.fileSys.maxFiles | The maximum number of files that can be created for the file system across all storage volumes. | 
| Used Files | File Sys | Files | os.fileSys.usedFiles | The number of files in the file system across all storage volumes. | 
| Used File Percent | File Sys | Files | os.fileSys.usedFilePercent | The percentage of available files in use across all storage volumes. | 
| Used Percent | File Sys | Percentage | os.fileSys.usedPercent | The percentage of the file-system disk space in use across all storage volumes. | 
| Used | File Sys | Kilobytes | os.fileSys.used | The amount of disk space used by files in the file system across all storage volumes, in kilobytes. | 
| Total | File Sys | Kilobytes | os.fileSys.total | The total disk space available for the file system across all storage volumes, in kilobytes. | 
| Max Files | File Sys | Files | os.fileSys.<volumeName>.maxFiles | The maximum number of files that can be created for the storage volume. | 
| Used Files | File Sys | Files | os.fileSys.<volumeName>.usedFiles | The number of files in the storage volume. | 
| Used File Percent | File Sys | Files | os.fileSys.<volumeName>.usedFilePercent | The percentage of available files in use in the storage volume. | 
| Used Percent | File Sys | Percentage | os.fileSys.<volumeName>.usedPercent | The percentage of the storage volume disk space in use. | 
| Used | File Sys | Kilobytes | os.fileSys.<volumeName>.used | The amount of disk space used by files in the storage volume, in kilobytes. | 
| Total | File Sys | Kilobytes | os.fileSys.<volumeName>.total | The total disk space available in the storage volume, in kilobytes. | 
| Rx | Network | Bytes per second | os.network.rx | The number of bytes received per second. | 
| Tx | Network | Bytes per second | os.network.tx | The number of bytes uploaded per second. | 
| Acu Utilization | General | Percentage | os.general.acuUtilization | The percentage of current capacity out of the maximum configured capacity. | 
| Max Configured Acu | General | ACUs | os.general.maxConfiguredAcu | The maximum capacity configured by the user, in Aurora capacity units (ACUs). | 
| Min Configured Acu | General | ACUs | os.general.minConfiguredAcu | The minimum capacity configured by the user, in ACUs. | 
| Num VCPUs | General | vCPUs | os.general.numVCPUs | The number of virtual CPUs (vCPUs) for the DB instance. | 
| Serverless Database Capacity | General | ACUs | os.general.serverlessDatabaseCapacity | The current capacity of the instance, in ACUs. | 

## Detailed Database Metrics for Aurora MySQL
<a name="USER_PerfInsights_Counters.Aurora_MySQL"></a>

The following database counters are available through the Performance Insights API for Aurora MySQL.

**Topics**
+ [Native counters for Aurora MySQL](#USER_PerfInsights_Counters.Aurora_MySQL.Native)
+ [Non-native counters for Aurora MySQL](#USER_PerfInsights_Counters.Aurora_MySQL.NonNative)

### Native counters for Aurora MySQL
<a name="USER_PerfInsights_Counters.Aurora_MySQL.Native"></a>

Native metrics are defined by the database engine and not by Amazon Aurora. You can find definitions for these native metrics in [Server status variables](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html) in the MySQL documentation.


| Counter | Type | Unit | Metric | 
| --- | --- | --- | --- | 
| Com\_analyze | SQL | Queries per second | db.SQL.Com\_analyze | 
| Com\_optimize | SQL | Queries per second | db.SQL.Com\_optimize | 
| Com\_select | SQL | Queries per second | db.SQL.Com\_select | 
| Innodb\_rows\_deleted | SQL | Rows per second | db.SQL.Innodb\_rows\_deleted | 
| Innodb\_rows\_inserted | SQL | Rows per second | db.SQL.Innodb\_rows\_inserted | 
| Innodb\_rows\_read | SQL | Rows per second | db.SQL.Innodb\_rows\_read | 
| Innodb\_rows\_updated | SQL | Rows per second | db.SQL.Innodb\_rows\_updated | 
| Queries | SQL | Queries per second | db.SQL.Queries | 
| Questions | SQL | Queries per second | db.SQL.Questions | 
| Select\_full\_join | SQL | Queries per second | db.SQL.Select\_full\_join | 
| Select\_full\_range\_join | SQL | Queries per second | db.SQL.Select\_full\_range\_join | 
| Select\_range | SQL | Queries per second | db.SQL.Select\_range | 
| Select\_range\_check | SQL | Queries per second | db.SQL.Select\_range\_check | 
| Select\_scan | SQL | Queries per second | db.SQL.Select\_scan | 
| Slow\_queries | SQL | Queries per second | db.SQL.Slow\_queries | 
| Sort\_merge\_passes | SQL | Queries per second | db.SQL.Sort\_merge\_passes | 
| Sort\_range | SQL | Queries per second | db.SQL.Sort\_range | 
| Sort\_rows | SQL | Queries per second | db.SQL.Sort\_rows | 
| Sort\_scan | SQL | Queries per second | db.SQL.Sort\_scan | 
| Total\_query\_time | SQL | Milliseconds | db.SQL.Total\_query\_time | 
| Table\_locks\_immediate | Locks | Requests per second | db.Locks.Table\_locks\_immediate | 
| Table\_locks\_waited | Locks | Requests per second | db.Locks.Table\_locks\_waited | 
| Innodb\_row\_lock\_time | Locks | Milliseconds (average) | db.Locks.Innodb\_row\_lock\_time | 
| Aborted\_clients | Users | Connections | db.Users.Aborted\_clients | 
| Aborted\_connects | Users | Connections | db.Users.Aborted\_connects | 
| Connections | Users | Connections | db.Users.Connections | 
| External\_threads\_connected | Users | Connections | db.Users.External\_threads\_connected | 
| max\_connections | Users | Connections | db.Users.max\_connections | 
| Threads\_connected | Users | Connections | db.Users.Threads\_connected | 
| Threads\_created | Users | Connections | db.Users.Threads\_created | 
| Threads\_running | Users | Connections | db.Users.Threads\_running | 
| Created\_tmp\_disk\_tables | Temp | Tables per second | db.Temp.Created\_tmp\_disk\_tables | 
| Created\_tmp\_tables | Temp | Tables per second | db.Temp.Created\_tmp\_tables | 
| Innodb\_buffer\_pool\_pages\_data | Cache | Pages | db.Cache.Innodb\_buffer\_pool\_pages\_data | 
| Innodb\_buffer\_pool\_pages\_total | Cache | Pages | db.Cache.Innodb\_buffer\_pool\_pages\_total | 
| Innodb\_buffer\_pool\_read\_requests | Cache | Pages per second | db.Cache.Innodb\_buffer\_pool\_read\_requests | 
| Innodb\_buffer\_pool\_reads | Cache | Pages per second | db.Cache.Innodb\_buffer\_pool\_reads | 
| Opened\_tables | Cache | Tables | db.Cache.Opened\_tables | 
| Opened\_table\_definitions | Cache | Tables | db.Cache.Opened\_table\_definitions | 
| Qcache\_hits | Cache | Queries | db.Cache.Qcache\_hits | 

### Non-native counters for Aurora MySQL
<a name="USER_PerfInsights_Counters.Aurora_MySQL.NonNative"></a>

Non-native counter metrics are counters defined by Amazon RDS. A non-native metric can be a metric that you get with a specific query. A non-native metric also can be a derived metric, where two or more native counters are used in calculations for ratios, hit rates, or latencies.


| Counter | Type | Unit | Metric | Description | Definition | 
| --- | --- | --- | --- | --- | --- | 
| active\_transactions | Transactions | db.Transactions.active\_transactions | The total active transactions. | SELECT COUNT(1) AS active\_transactions FROM INFORMATION\_SCHEMA.INNODB\_TRX | 
| innodb\_buffer\_pool\_hit\_rate | Cache | db.Cache.innoDB\_buffer\_pool\_hit\_rate | The percentage of reads that InnoDB could satisfy from the buffer pool. | 100 \* innodb\_buffer\_pool\_read\_requests / (innodb\_buffer\_pool\_read\_requests \+ innodb\_buffer\_pool\_reads) | 
| innodb\_buffer\_pool\_hits | Cache | Pages per second | db.Cache.innoDB\_buffer\_pool\_hits | The number of reads that InnoDB could satisfy from the buffer pool. | innodb\_buffer\_pool\_read\_requests - innodb\_buffer\_pool\_reads | 
| innodb\_buffer\_pool\_usage | Cache | Percentage | db.Cache.innoDB\_buffer\_pool\_usage | The percentage of the InnoDB buffer pool that contains data (pages). When using compressed tables, this value can vary. For more information, see the information about `Innodb_buffer_pool_pages_data` and `Innodb_buffer_pool_pages_total` in [Server status sariables](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html) in the MySQL documentation.  | Innodb\_buffer\_pool\_pages\_data / Innodb\_buffer\_pool\_pages\_total \* 100.0 | 
| innodb\_deadlocks | Locks | db.Locks.innodb\_deadlocks | The total number of deadlocks. | SELECT COUNT AS innodb\_deadlocks FROM INFORMATION\_SCHEMA.INNODB\_METRICS WHERE NAME='lock\_deadlocks' | 
| innodb\_lock\_timeouts | Locks | db.Locks.innodb\_lock\_timeouts | The total number of deadlocks that timed out. | SELECT COUNT AS innodb\_lock\_timeouts FROM INFORMATION\_SCHEMA.INNODB\_METRICS WHERE NAME='lock\_timeouts' | 
| innodb\_row\_lock\_waits | Locks | db.Locks.innodb\_row\_lock\_waits | The total number of row locks that resulted in a wait. | SELECT COUNT AS innodb\_row\_lock\_waits FROM INFORMATION\_SCHEMA.INNODB\_METRICS WHERE NAME='lock\_row\_lock\_waits' | 
| innodb\_rows\_changed | SQL | db.SQL.innodb\_rows\_changed | The total InnoDB row operations. | db.SQL.Innodb\_rows\_inserted \+ db.SQL.Innodb\_rows\_deleted \+ db.SQL.Innodb\_rows\_updated | 
| query\_cache\_hit\_rate | Cache | Percentage | db.Cache.query\_cache\_hit\_rate | The hit ratio for the MySQL result set cache (query cache). | Qcache\_hits / (QCache\_hits \+ Com\_select) \* 100 | 
| temp\_disk\_tables\_percent | Temp | db.Temp.temp\_disk\_tables\_percent | The percentage of temporary tables that are created on disk by the server when running statements. | (db.Temp.Created\_tmp\_disk\_tables / db.Temp.Created\_tmp\_tables) \* 100 | 
| trx\_rseg\_history\_len | Transactions | None | db.Transactions.trx\_rseg\_history\_len | A list of the undo log pages for committed transactions that is maintained by the InnoDB transaction system to implement multi-version concurrency control. For more information about undo log records details, see [https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html](https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html) in the MySQL documentation. | SELECT COUNT AS trx\_rseg\_history\_len FROM INFORMATION\_SCHEMA.INNODB\_METRICS WHERE NAME='trx\_rseg\_history\_len'  | 

## Detailed Database Metrics for Aurora PostgreSQL
<a name="USER_PerfInsights_Counters.Aurora_PostgreSQL"></a>

The following database counters are available through the Performance Insights API for Aurora PostgreSQL.

**Topics**
+ [Native counters for Aurora PostgreSQL](#USER_PerfInsights_Counters.Aurora_PostgreSQL.Native)
+ [Non-native counters for Aurora PostgreSQL](#USER_PerfInsights_Counters.Aurora_PostgreSQL.NonNative)

### Native counters for Aurora PostgreSQL
<a name="USER_PerfInsights_Counters.Aurora_PostgreSQL.Native"></a>

Native metrics are defined by the database engine and not by Amazon Aurora. You can find definitions for these native metrics in [Viewing Statistics](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-VIEWS) in the PostgreSQL documentation.


| Counter | Type | Unit | Metric | 
| --- | --- | --- | --- | 
| tup\_deleted | SQL | Tuples per second | db.SQL.tup\_deleted | 
| tup\_fetched | SQL | Tuples per second | db.SQL.tup\_fetched | 
| tup\_inserted | SQL | Tuples per second | db.SQL.tup\_inserted | 
| tup\_returned | SQL | Tuples per second | db.SQL.tup\_returned | 
| tup\_updated | SQL | Tuples per second | db.SQL.tup\_updated | 
| blks\_hit | Cache | Blocks per second | db.Cache.blks\_hit | 
| buffers\_alloc | Cache | Blocks per second | db.Cache.buffers\_alloc | 
| buffers\_checkpoint | Checkpoint | Blocks per second | db.Checkpoint.buffers\_checkpoint | 
| checkpoints\_req | Checkpoint | Checkpoints per minute | db.Checkpoint.checkpoints\_req | 
| checkpoint\_sync\_time | Checkpoint | Milliseconds per checkpoint | db.Checkpoint.checkpoint\_sync\_time | 
| checkpoints\_timed | Checkpoint | Checkpoints per minute | db.Checkpoint.checkpoints\_timed | 
| checkpoint\_write\_time | Checkpoint | Milliseconds per checkpoint | db.Checkpoint.checkpoint\_write\_time | 
| maxwritten\_clean | Checkpoint | Bgwriter clean stops per minute | db.Checkpoint.maxwritten\_clean | 
| deadlocks | Concurrency | Deadlocks per minute | db.Concurrency.deadlocks | 
| blk\_read\_time | I/O | Milliseconds | db.IO.blk\_read\_time | 
| blks\_read | I/O | Blocks per second | db.IO.blks\_read | 
| buffers\_backend | I/O | Blocks per second | db.IO.buffers\_backend | 
| buffers\_backend\_fsync | I/O | Blocks per second | db.IO.buffers\_backend\_fsync | 
| buffers\_clean | I/O | Blocks per second | db.IO.buffers\_clean | 
| temp\_bytes | Temp | Bytes per second | db.Temp.temp\_bytes | 
| temp\_files | Temp | Files per minute | db.Temp.temp\_files | 
| xact\_commit | Transactions | Commits per second | db.Transactions.xact\_commit | 
| xact\_rollback | Transactions | Rollbacks per second | db.Transactions.xact\_rollback | 
| numbackends | User | Connections | db.User.numbackends | 
| archived\_count | WAL | Files per minute | db.WAL.archived\_count | 

### Non-native counters for Aurora PostgreSQL
<a name="USER_PerfInsights_Counters.Aurora_PostgreSQL.NonNative"></a>

Non-native counter metrics are counters defined by Amazon Aurora. A non-native metric can be a metric that you get with a specific query. A non-native metric also can be a derived metric, where two or more native counters are used in calculations for ratios, hit rates, or latencies.


| Counter | Type | Unit | Metric | Description | Definition | 
| --- | --- | --- | --- | --- | --- | 
| checkpoint\_sync\_latency | Checkpoint | Milliseconds | db.Checkpoint.checkpoint\_sync\_latency | The total amount of time that has been spent in the portion of checkpoint processing where files are synchronized to disk. | checkpoint\_sync\_time / (checkpoints\_timed \+ checkpoints\_req) | 
| checkpoint\_write\_latency | Checkpoint | Milliseconds | db.Checkpoint.checkpoint\_write\_latency | The total amount of time that has been spent in the portion of checkpoint processing where files are written to disk. | checkpoint\_write\_time / (checkpoints\_timed \+ checkpoints\_req) | 
| local\_blks\_read | I/O | Blocks | db.IO.local\_blks\_read | Total number of local blocks read. | Not applicable | 
| local\_blk\_read\_time | I/O | Milliseconds | db.IO.local\_blk\_read\_time | If track\_io\_timing is enabled, it tracks the total time spent reading local data file blocks, in milliseconds, otherwise the value is zero. For more information, see [track\_io\_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING). | Not applicable | 
| num\_blocked\_sessions | Locks | db.Locks.num\_blocked\_sessions | The number of blocked sessions. | – | 
| orcache\_blks\_hit | I/O | Queries | db.IO.orcache\_blks\_hit | Total number of shared blocks hits from optimized reads cache. | Not applicable | 
| orcache\_blk\_read\_time | I/O | Milliseconds | db.IO.orcache\_blk\_read\_time | If track\_io\_timing is enabled, it tracks the total time spent reading data file blocks from Optimized Reads cache, in milliseconds, otherwise the value is zero. For more information, see [track\_io\_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING). | Not applicable | 
| read\_latency | I/O | Milliseconds | db.IO.read\_latency | The time spent reading data file blocks by backends in this instance. | blk\_read\_time / blks\_read | 
| storage\_blks\_read | I/O | Blocks | db.IO.storage\_blks\_read | Total number of shared blocks read from aurora storage. | Not applicable | 
| storage\_blk\_read\_time | I/O | Milliseconds | db.IO.storage\_blk\_read\_time | If track\_io\_timing is enabled, it tracks the total time spent reading data file blocks from Aurora storage, in milliseconds, otherwise the value is zero. For more information, see [track\_io\_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING). | Not applicable | 
| active\_count | State | Sessions | db.state.active\_count | The number of sessions in the active state. | Not applicable | 
| idle\_count | State | Sessions | db.state.idle\_count | The number of sessions in the idle state. | Not applicable | 
| idle\_in\_transaction\_aborted\_count | State | Sessions | db.state.idle\_in\_transaction\_aborted\_count | The number of sessions in the idle in transaction (aborted) state. | Not applicable | 
| idle\_in\_transaction\_count | State | Sessions | db.state.idle\_in\_transaction\_count | The number of sessions in the idle in transaction state. | Not applicable | 
| idle\_in\_transaction\_max\_time | State | Seconds | db.state.idle\_in\_transaction\_max\_time | The duration of the longest running transaction in the idle in transaction state, in seconds. | Not applicable | 
| logical\_reads | SQL | Blocks | db.SQL.logical\_reads | The total number of blocks hit and read. | blks\_hit \+ blks\_read | 
| queries\_started | SQL | Queries | db.SQL.queries | The number of queries started. | Not applicable | 
| queries\_finished | SQL | Queries | db.SQL.queries | The number of queries finished. | Not applicable | 
| total\_query\_time | SQL | Milliseconds | db.SQL.total\_query\_time | The total time spent executing statements, in milliseconds. | Not applicable | 
| active\_transactions | Transactions | Transactions | db.Transactions.active\_transactions | The number of active transactions. | Not applicable | 
| blocked\_transactions | Transactions | Transactions | db.Transactions.blocked\_transactions | The number of blocked transactions. | Not applicable | 
| commit\_latency | Transactions | Microseconds | db.Transactions.commit\_latency | The average duration of commit operations. | db.Transactions.duration\_commits / db.Transactions.xact\_commit | 
| duration\_commits | Transactions | Milliseconds | db.Transactions.duration\_commits | The total transaction time spent in the last minute, in milliseconds. | Not applicable | 
| max\_used\_xact\_ids | Transactions | Transactions | db.Transactions.max\_used\_xact\_ids | The number of transactions that haven't been vacuumed. | Not applicable | 
| oldest\_inactive\_logical\_replication\_slot\_xid\_age | Transactions | Length | db.Transactions.oldest\_inactive\_logical\_replication\_slot\_xid\_age | The age of the oldest transaction in an inactive logical replication slot. | Not applicable | 
| oldest\_active\_logical\_replication\_slot\_xid\_age | Transactions | Length | db.Transactions.oldest\_active\_logical\_replication\_slot\_xid\_age | The age of the oldest transaction in an active logical replication slot. | Not applicable | 
| oldest\_reader\_feedback\_xid\_age | Transactions | Length | db.Transactions.oldest\_reader\_feedback\_xid\_age | The age of the oldest transaction of a long‐running transaction on an Aurora reader instance or Aurora global DB reader instance. | Not applicable | 
| oldest\_prepared\_transaction\_xid\_age | Transactions | Length | db.Transactions.oldest\_prepared\_transaction\_xid\_age | The age of the oldest prepared transaction. | Not applicable | 
| oldest\_running\_transaction\_xid\_age | Transactions | Length | db.Transactions.oldest\_running\_transaction\_xid\_age | The age of the oldest running transaction. | Not applicable | 
| max\_connections | Users | Users | db.User.max\_connections | The maximum number of connections allowed for a database as configured in max\_connections parameter. | Not applicable | 
| total\_auth\_attempts | Users | Users | db.User.total\_auth\_attempts | The number of connection attempts to this instance. | Not applicable | 
| archive\_failed\_count | WAL | Files per minute | db.WAL.archive\_failed\_count | The number of failed attempts for archiving WAL files, in files per minute. | Not applicable | 