

# Setting trace flags in RDS for Microsoft SQL Server
<a name="Appendix.SQLServer.CommonDBATasks.TraceFlags"></a>

A SQL Server trace flag is a setting you can turn on or off to change how the database engine behaves. You can use trace flags to enable hidden features, fix performance problems, or override default server behavior. In effect, each trace flag acts as an on/off switch that changes the default behavior of SQL Server.

For a complete list of trace flags available in Microsoft SQL Server, see [DBCC TRACEON - Trace Flags](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver17#trace-flags) in the Microsoft documentation.

As a managed service, RDS for SQL Server restricts global server-level settings. You can configure only specific trace flags as startup parameters through RDS for SQL Server [DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/parameter-groups-overview.html). The following table lists the supported trace flags in RDS for SQL Server.

**Important**  
We strongly recommend that you test and validate thoroughly before you enable trace flags in production. Trace flags are useful for performance tuning and troubleshooting, but incorrect usage can cause instability, suboptimal query plans, or resource issues.


| Trace flag | Description | 
| --- | --- | 
| 647 | Skips a data validation check introduced in SQL Server 2012 that can cause `ALTER TABLE... ADD` column operations to run significantly slower. | 
| 652 | Disables page pre-fetching for scans. When enabled, SQL Server stops loading pages into the buffer pool ahead of time. This might degrade performance for queries that rely on pre-fetching. | 
| 692 | Disables fast inserts while bulk loading data into heap or clustered indexes (supported on SQL Server 2016 and later). | 
| 1204 | Returns the resources and types of locks participating in a deadlock and the current command affected. | 
| 1211 | Disables lock escalation based on memory pressure or number of locks. SQL Server will not escalate row or page locks to table locks. | 
| 1222 | Returns deadlock information in XML format (enhanced version of 1204). | 
| 1224 | Disables lock escalation based on the number of locks (memory pressure can still activate lock escalation). | 
| 1448 | Allows the replication log reader to advance without waiting for asynchronous secondaries to acknowledge changes. The log reader still waits for synchronous secondaries in `SYNCHRONIZED` state. It does not advance beyond their minimum acknowledged log sequence number (LSN). | 
| 2528 | Disables parallel checking of objects by `DBCC CHECKDB`, `DBCC CHECKFILEGROUP`, and `DBCC CHECKTABLE`. | 
| 3654 | Used for troubleshooting memory leaks or unfreed memory conditions. When active, if such an issue is detected, SQL Server triggers an assertion failure and generates a mini dump. The dump results from the underlying memory error being caught by enhanced tracing, not from the trace flag itself. | 
| 4138 | Disables row goal adjustments for queries using `TOP`, `OPTION (FAST N)`, `IN`, or `EXISTS`. This forces SQL Server to generate a full plan without row goal optimizations. | 
| 4139 | Adjusts the histogram at query compile time for better cardinality estimation, regardless of whether the leading column is ascending, descending, or stationary. | 
| 4199 | Controls multiple query optimizer changes previously made under multiple trace flags. | 
| 4616 | Makes server-level metadata visible to application roles. | 
| 6527 | Disables generation of a memory dump on the first occurrence of an out-of-memory exception in Common Language Runtime (CLR) integration. | 
| 7745 | Prevents Query Store from flushing data to disk during database shutdown. | 
| 8285 | Fixes an assertion error (`IndexRowScanner.cpp: m_versionStatus.IsVisible()`) in databases with change data capture (CDC) or Read Committed Snapshot Isolation (RCSI) enabled. It prevents stack dumps by converting assertions to controlled error messages (SQL Server 2022 Cumulative Update (CU) 6 or later) or suppressing them (SQL Server 2019). | 
| 8780 | Gives the optimizer more time to find a better plan. | 
| 9432 | Disables the fix from SQL Server 2019 CU14 that corrected wrong results in parallel plans using `SESSION_CONTEXT`. Used alongside trace flag 11042 to prevent access violation dumps when sessions are reset for reuse. | 
| 9481 | Forces the query optimizer to use the legacy cardinality estimation model (SQL Server 2012 and earlier), regardless of the database compatibility level. Alternatives: at the database level, use `ALTER DATABASE SCOPED CONFIGURATION`; at the query level, use the `QUERYTRACEON` query hint. | 
| 9492 | Disables parallelism for `SELECT INTO` (bulk insert) operations at the instance level to reduce `LATCH_EX` waits on `METADATA_SEQUENCE_GENERATOR`. Might slightly reduce performance but improves overall stability. | 
| 9592 | Enables log stream compression for synchronous availability groups. Log stream compression is disabled by default on synchronous availability groups because compression adds latency. Enabling it can reduce network bandwidth usage between replicas at the cost of additional CPU and some added latency. Applies to: SQL Server 2016 (13.0) and later. | 
| 11024 | In SQL Server 2017, auto-update of incremental statistics on partitioned tables can be delayed. This happens because the root node's modification count resets to zero if no single partition exceeds its local threshold, even when the combined count exceeds the root threshold. Trace flag 11024 fixes this by keeping the root node's modification count as the true sum of all partition modifications, ensuring timely statistics updates. Applies to: SQL Server 2017 CU3 and later. | 
| 11042 | SQL Server 2019 CU14 fixed wrong results in parallel plans using `SESSION_CONTEXT`. However, this fix can cause access violation dumps when sessions are reset for reuse. Workaround: enable both trace flags together: trace flag 11042 (disables parallelism for `SESSION_CONTEXT`) and trace flag 9432 (disables the original CU14 fix). Note: This is a known issue still present in the latest SQL Server versions. A permanent fix from Microsoft is pending in a future CU. | 
| 12502 | Fixes high `PREEMPTIVE_OS_QUERYREGISTRY` waits by disabling external authorization policies for on-premises SQL Server instances. Applies to: SQL Server 2022 CU5\+. | 
| 12618 | Allows the Automatic Plan Correction (APC) feature to perform multiple consecutive regression checks on the same plan, enabling it to gather more statistics before deciding on a correction. Applies to: SQL Server 2022 CU4 and later. | 
| 12656 | Adds a 5-minute delay before Automatic Plan Correction (APC) runs its regression check after detecting a plan change. This avoids skewed results from fast-running queries and accounts for longer-running or timeout-prone queries affected by the change. Applies to: SQL Server 2022 CU4\+. | 

**Note**  
From SQL Server 2016 Service Pack 1 (SP1) and later, we recommend that you use the `USE HINT` query hint at the query level instead of trace flags 4138 and 4139. Always test thoroughly before you apply this change in production.

**Important**  
Unflushed Query Store data might be lost during shutdown when you use trace flag 7745. For an immediate SQL Server shutdown, use `SHUTDOWN WITH NOWAIT` instead of this trace flag.