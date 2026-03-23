# Oracle database hints and PostgreSQL DB query planning

With AWS DMS, you can optimize query performance by using Oracle database hints and PostgreSQL query planning techniques. Oracle database hints provide instructions to the optimizer on how to execute a SQL statement, while PostgreSQL query planning involves analyzing the execution plan to identify and address performance bottlenecks.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                           |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | Very limited set of hints in PostgreSQL. Index hints and optimizer hints as comments. Syntax differences. |

## Oracle usage

Oracle provides users with the ability to influence how the query optimizer behaves and the decisions made to generate query run plans. Controlling the behavior of the database optimizer is performed using database hints. They can be defined as a directive operation to the optimizer and alter the decisions of how run plans are generated.

Oracle supports over 60 different database hints, and each database hint can have 0 or more arguments. Database hints are divided into different categories such as optimizer hints, join order hints, and parallel execution hints.

###### Note

Database hints are embedded directly into the SQL queries immediately following the `SELECT` keyword using the format `/* <DB_HINT> */`.

**Examples**

Force the Query Optimizer to use a specific index for data access.

```
SELECT /* INDEX(EMP, IDX_EMP_HIRE_DATE)*/ *
  FROM EMPLOYEES EMP
  WHERE HIRE_DATE >= '01-JAN-2010';

Run Plan
Plan hash value: 3035503638
Id  Operation                    Name           Rows  Bytes  Cost (%CPU)  Time
0   SELECT STATEMENT                            1     62     2 (0)        00:00:01
1   TABLE ACCESS BY INDEX ROWID  EMPLOYEES      1     62     2 (0)        00:00:01
2   INDEX RANGE SCAN             IDX_HIRE_DATE  1            1 (0)        00:00:01

Predicate Information (identified by operation id):
2 - access("HIRE_DATE">=TO_DATE(' 2010-01-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss'))
```

For more information, see [Comments](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Comments.html#GUID-D316D545-89E2-4D54-977F-FC97815CD62El "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Comments.html#GUID-D316D545-89E2-4D54-977F-FC97815CD62El") and [Influencing the Optimizer](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/influencing-the-optimizer.html#GUID-8758EF88-1CC6-41BD-8581-246702414D1D "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/influencing-the-optimizer.html#GUID-8758EF88-1CC6-41BD-8581-246702414D1D") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t support database hints to influence the behavior of the query planner and we can’t influence how execution plans are generated from within SQL queries. Although database hints are not directly supported, session parameters (also known as Query Planning Parameters) can influence the behavior of the query optimizer at a session level.

**Examples**

Set the query planner to use indexes instead of full table scans (disable `SEQSCAN`).

```
SET ENABLE_SEQSCAN=FALSE;
```

Set the query planner’s estimated cost of a disk page fetch that is part of a series of sequential fetches (`SEQ_PAGE_COST`) and set the planner’s estimate of the cost of a non-sequentially-fetched disk page (`RANDOM_PAGE_COST`). Reducing the value of `RANDOM_PAGE_COST` relative to `SEQ_PAGE_COST` will cause the query planner to prefer index scans, while raising the value will make index scans more expensive.

```
SET SEQ_PAGE_COST to 4;
SET RANDOM_PAGE_COST to 1;
```

Turn on or turn off the query planner’s use of nested-loops when performing joins. While it is impossible to completely disable the usage of nested-loop joins, setting the `ENABLE_NESTLOOP` to an `OFF` value discourages the query planner from choosing nested-loop joins compared to alternative join methods.

```
SET ENABLE_NESTLOOP to FALSE;
```

For more information, see [Query Planning](https://www.postgresql.org/docs/13/runtime-config-query.html "https://www.postgresql.org/docs/13/runtime-config-query.html") in the _PostgreSQL documentation_.
