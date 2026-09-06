

# SQL statistics for Amazon RDS for SQL Server
<a name="USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer"></a>

Amazon RDS for SQL Server collects SQL statistics both at the statement and digest level. At the statement level, the ID column represents the value of `sql_handle`. At the digest level, the ID column shows the value of `query_hash`. 

SQL Server returns NULL values for `query_hash` for a few statements. For example, ALTER INDEX, CHECKPOINT, UPDATE STATISTICS, COMMIT TRANSACTION, FETCH NEXT FROM Cursor, and a few INSERT statements, SELECT @<variable>, conditional statements, and executable stored procedures. In this case, the `sql_handle` value is displayed as the ID at the digest level for that statement. 

**Topics**
+ [Per-second statistics for SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-second)
+ [Per-call statistics for SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-call)
+ [Primary statistics for SQL Server](#USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.primary)

## Per-second statistics for SQL Server
<a name="USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-second"></a>

The following metrics provide per-second statistics for a SQL Server SQL query.


| Metric | Unit | 
| --- | --- | 
| db.sql.stats.execution\_count\_per\_sec | Number of executions per second | 
| db.sql.stats.total\_elapsed\_time\_per\_sec | Total elapsed time per second | 
| db.sql.stats.total\_rows\_per\_sec | Total rows processed per second | 
| db.sql.stats.total\_logical\_reads\_per\_sec | Total logical reads per second | 
| db.sql.stats.total\_logical\_writes\_per\_sec | Total logical writes per second | 
| db.sql.stats.total\_physical\_reads\_per\_sec | Total physical reads per second | 
| db.sql.stats.total\_worker\_time\_per\_sec | Total CPU time (in ms) | 

The following metrics provide per-second statistics for a SQL Server SQL digest query.


| Metric | Unit | 
| --- | --- | 
| db.sql\_tokenized.stats.execution\_count\_per\_sec | Number of execution per second | 
| db.sql\_tokenized.stats.total\_elapsed\_time\_per\_sec | Total elapsed time per second | 
| db.sql\_tokenized.stats.total\_rows\_per\_sec | Total rows processed per second | 
| db.sql\_tokenized.stats.total\_logical\_reads\_per\_sec | Total logical reads per second | 
| db.sql\_tokenized.stats.total\_logical\_writes\_per\_sec | Total logical writes per second | 
| db.sql\_tokenized.stats.total\_physical\_reads\_per\_sec | Total physical reads per second | 
| db.sql\_tokenized.stats.total\_worker\_time\_per\_sec | Total CPU time (in ms) | 

## Per-call statistics for SQL Server
<a name="USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.per-call"></a>

The following metrics provide per-call statistics for a SQL Server SQL statement.


| Metric | Unit | 
| --- | --- | 
| db.sql.stats.total\_elapsed\_time\_per\_call | Total elapsed time per execution (in ms) | 
| db.sql.stats.total\_rows\_per\_call | Total rows processed per execution | 
| db.sql.stats.total\_logical\_reads\_per\_call | Total logical reads per execution | 
| db.sql.stats.total\_logical\_writes\_per\_call | Total logical writes per execution | 
| db.sql.stats.total\_physical\_reads\_per\_call | Total physical reads per execution | 
| db.sql.stats.total\_worker\_time\_per\_call | Total CPU time per execution (in ms) | 

The following metrics provide per-call statistics for a SQL Server SQL digest query.


| Metric | Unit | 
| --- | --- | 
| db.sql\_tokenized.stats.total\_elapsed\_time\_per\_call | Total elapsed time per execution | 
| db.sql\_tokenized.stats.total\_rows\_per\_call | Total rows processed per execution | 
| db.sql\_tokenized.stats.total\_logical\_reads\_per\_call | Total logical reads per execution | 
| db.sql\_tokenized.stats.total\_logical\_writes\_per\_call | Total logical writes per execution | 
| db.sql\_tokenized.stats.total\_physical\_reads\_per\_call | Total physical reads per execution  | 
| db.sql\_tokenized.stats.total\_worker\_time\_per\_call | Total CPU time per execution (in ms) | 

## Primary statistics for SQL Server
<a name="USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.primary"></a>

The following metrics provide primary statistics for a SQL Server SQL query.


| Metric | Unit | 
| --- | --- | 
| db.sql.stats.execution\_count | Number of executions | 
| db.sql.stats.total\_elapsed\_time | Total elapsed time (in ms) | 
| db.sql.stats.total\_rows | Total rows processed | 
| db.sql.stats.total\_logical\_reads | Total logical reads | 
| db.sql.stats.total\_logical\_writes | Total logical writes | 
| db.sql.stats.total\_physical\_reads | Total physical reads | 
| db.sql.stats.total\_worker\_time | Total CPU time (in ms) | 

The following metrics provide primary statistics for a SQL Server SQL digest query.


| Metric | Unit | 
| --- | --- | 
| db.sql\_tokenized.stats.execution\_count | Number of execution | 
| db.sql\_tokenized.stats.total\_elapsed\_time | Total elapsed time (in ms) | 
| db.sql\_tokenized.stats.total\_rows | Total rows processed | 
| db.sql\_tokenized.stats.total\_logical\_reads | Total logical reads | 
| db.sql\_tokenized.stats.total\_logical\_writes | Total logical writes | 
| db.sql\_tokenized.stats.total\_physical\_reads | Total physical reads | 
| db.sql\_tokenized.stats.total\_worker\_time | Total CPU time (in ms) | 