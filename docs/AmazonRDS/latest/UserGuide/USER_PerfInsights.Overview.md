# Database load

_Database load (DB load)_ measures the level of session activity in your
database. `DBLoad` is the key metric in Performance Insights, and Performance Insights collects DB load
every second.

###### Topics

- [Active sessions](#USER_PerfInsights.Overview.ActiveSessions.active-sessions "#USER_PerfInsights.Overview.ActiveSessions.active-sessions")
- [Average active sessions](#USER_PerfInsights.Overview.ActiveSessions.AAS "#USER_PerfInsights.Overview.ActiveSessions.AAS")
- [Average active executions](#USER_PerfInsights.Overview.ActiveSessions.AAE "#USER_PerfInsights.Overview.ActiveSessions.AAE")
- [Dimensions](#USER_PerfInsights.Overview.ActiveSessions.dimensions "#USER_PerfInsights.Overview.ActiveSessions.dimensions")

## Active sessions

A _database session_ represents an application's dialogue with a
relational database. An _active session_ is a
connection that has submitted work to the DB engine and is waiting for a response.

A session is active when it's either running on CPU or waiting for a resource to become
available so that it can proceed. For example, an active session might wait for a
page (or block) to be read into memory, and then consume CPU while it reads data from the page.

## Average active sessions

The _average active sessions (AAS)_ is the unit for the
`DBLoad` metric in Performance Insights. It measures how many sessions
are concurrently active on the database.

Every second, Performance Insights samples the number of sessions concurrently running
a query. For each active session, Performance Insights collects the following
data:

- SQL statement
- Session state (running on CPU or waiting)
- Host
- User running the SQL

Performance Insights calculates the AAS by dividing the total number of sessions by
the number of samples for a specific time period. For example, the following table shows
5 consecutive samples of a running query taken at 1-second intervals.

| Sample | Number of sessions running query | AAS | Calculation                   |
| ------ | -------------------------------- | --- | ----------------------------- |
| 1      | 2                                | 2   | 2 total sessions / 1 sample   |
| 2      | 0                                | 1   | 2 total sessions / 2 samples  |
| 3      | 4                                | 2   | 6 total sessions / 3 samples  |
| 4      | 0                                | 1.5 | 6 total sessions / 4 samples  |
| 5      | 4                                | 2   | 10 total sessions / 5 samples |

In the preceding example, the DB load for the time interval was 2 AAS. This measurement
means that, on average, 2 sessions were active at any given time during the interval
when the 5 samples were taken.

## Average active executions

The _average active executions (AAE)_ per second is related to AAS. To calculate the AAE,
Performance Insights divides the total execution time of a query by the time interval. The following
table shows the AAE calculation for the same query in the preceding table.

| Elapsed time (sec) | Total execution time (sec) | AAE  | Calculation                               |
| ------------------ | -------------------------- | ---- | ----------------------------------------- |
| 60                 | 120                        | 2    | 120 execution seconds/60 elapsed seconds  |
| 120                | 120                        | 1    | 120 execution seconds/120 elapsed seconds |
| 180                | 380                        | 2.11 | 380 execution seconds/180 elapsed seconds |
| 240                | 380                        | 1.58 | 380 execution seconds/240 elapsed seconds |
| 300                | 600                        | 2    | 600 execution seconds/300 elapsed seconds |

In most cases, the AAS and AAE for a query are approximately the same. However, because the inputs to
the calculations are different data sources, the calculations often vary slightly.

## Dimensions

The `db.load` metric is different from the other time-series metrics because you can break it into
subcomponents called _dimensions_. You can think of dimensions as "slice by" categories for
the different characteristics of the `DBLoad` metric.

When you are diagnosing performance issues, the following dimensions are often the most useful:

###### Topics

- [Wait events](#USER_PerfInsights.Overview.ActiveSessions.waits "#USER_PerfInsights.Overview.ActiveSessions.waits")
- [Top SQL](#USER_PerfInsights.Overview.ActiveSessions.top-sql "#USER_PerfInsights.Overview.ActiveSessions.top-sql")
- [Plans](#USER_PerfInsights.Overview.ActiveSessions.plans "#USER_PerfInsights.Overview.ActiveSessions.plans")

For a complete list of dimensions for the Amazon RDS engines, see [DB load sliced by
dimensions](USER_PerfInsights.UsingDashboard.md#USER_PerfInsights.UsingDashboard.Components.AvgActiveSessions.dims "USER_PerfInsights.UsingDashboard.md#USER_PerfInsights.UsingDashboard.Components.AvgActiveSessions.dims").

### Wait events

A _wait event_ causes a SQL statement to wait for a specific event to happen before
it can continue running. Wait events are an important dimension, or category, for DB load because they
indicate where work is impeded.

Every active session is either running on the CPU or waiting. For example, sessions
consume CPU when they search memory for a buffer, perform a calculation, or run
procedural code. When sessions aren't consuming CPU, they might be waiting for a
memory buffer to become free, a data file to be read, or a log to be written to.
The more time that a session waits for resources, the less time it runs on the
CPU.

When you tune a database, you often try to find out the resources that sessions are
waiting for. For example, two or three wait events might account for 90 percent
of DB load. This measure means that, on average, active sessions are spending
most of their time waiting for a small number of resources. If you can find out
the cause of these waits, you can attempt a solution.

Wait events vary by DB engine:

- For information about all MariaDB and MySQL wait
  events, see [Wait Event Summary Tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-wait-summary-tables.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-wait-summary-tables.html") in the MySQL documentation.
- For information about all PostgreSQL wait events, see [The Statistics Collector > Wait Event tables](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE "https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE") in the PostgreSQL documentation.
- For information about all Oracle wait events, see [Descriptions of Wait Events](https://docs.oracle.com/database/121/REFRN/GUID-2FDDFAA4-24D0-4B80-A157-A907AF5C68E2.htm#REFRN-GUID-2FDDFAA4-24D0-4B80-A157-A907AF5C68E2 "https://docs.oracle.com/database/121/REFRN/GUID-2FDDFAA4-24D0-4B80-A157-A907AF5C68E2.htm#REFRN-GUID-2FDDFAA4-24D0-4B80-A157-A907AF5C68E2") in the Oracle documentation.
- For information about all SQL Server wait events, see [Types of Waits](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-wait-stats-transact-sql?view=sql-server-2017#WaitTypes "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-wait-stats-transact-sql?view=sql-server-2017#WaitTypes") in the SQL Server documentation.

###### Note

For Oracle, background processes sometimes do work without an associated SQL statement.
In these cases, Performance Insights reports the type of background process
concatenated with a colon and the wait class associated with that background
process. Types of background process include `LGWR`,
`ARC0`, `PMON`, and so on.

For example, when the archiver is performing I/O, the Performance Insights report for it is
similar to `ARC1:System I/O`. Occasionally, the background process type is also
missing, and Performance Insights only reports the wait class, for example `:System
 I/O`.

### Top SQL

Where wait events show bottlenecks, top SQL shows which queries are contributing the most to DB load. For example,
many queries might be currently running on the database, but a single query might consume 99 percent of the
DB load. In this case, the high load might indicate a problem with the query.

By default, the Performance Insights console displays top SQL queries that are contributing to the
database load. The console also shows relevant statistics for each statement. To diagnose performance
problems for a specific statement, you can examine its execution plan.

### Plans

An _execution plan_, also called simply a _plan_, is a sequence of steps that
access data. For example, a plan for joining tables `t1` and `t2` might loop through
all rows in `t1` and compare each row to a row in `t2`. In a relational database, an
_optimizer_ is built-in code that determines the most efficient plan for a SQL
query.

For DB instances, Performance Insights collects execution plans automatically. To diagnose SQL performance
problems, examine the captured plans for high-resource SQL queries. The plans show how the database
has parsed and run queries.

To learn how to analyze DB load using plans, see:

- Oracle: [Analyzing Oracle execution plans using the Performance
  Insights dashboard for Amazon RDS](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- SQL Server: [Analyzing SQL Server execution plans using the Performance Insights dashboard for Amazon RDS](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")

#### Plan capture

Every five minutes, Performance Insights identifies the most resource-intensive queries and
captures their plans. Thus, you don't need to manually collect and manage a huge number of plans.
Instead, you can use the **Top SQL** tab to focus on the plans for the most
problematic queries.

###### Note

Performance Insights doesn't capture plans for queries whose text exceeds the maximum collectable
query text limit. For more information, see [Accessing more SQL text in the Performance Insights dashboard](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md").

The retention period for execution plans is the same as for your Performance Insights data.
The retention setting is **Default (7 days)**. To retain your performance
data for longer, specify 1–24 months. For more information about retention periods, see
[Pricing and data retention for Performance Insights](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md").

#### Digest queries

The **Top SQL** tab shows digest queries by default. A digest query
doesn't itself have a plan, but all queries that use literal values have plans. For example, a
digest query might include the text `WHERE `email`=?`. The digest might contain two queries,
one with the text `WHERE email=user1@example.com` and another with `WHERE
 email=user2@example.com`. Each of these literal queries might include multiple plans.

When you select a digest query, the console shows all plans for child statements of the selected digest.
Thus, you don't need to look through all the child statements to find the plan. You might see plans that
aren’t in the displayed list of top 10 child statements. The console shows plans for all child queries
for which plans have been collected, regardless of whether the queries are in the top 10.
