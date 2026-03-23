# Query hints and plan guides

This topic provides reference information about the differences in feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL, specifically regarding database hints and query optimization. You can understand how SQL Server’s hint functionality, which allows direct influence over query execution plans, contrasts with PostgreSQL’s approach. While PostgreSQL doesn’t support database hints in the same way, it offers alternative methods to influence query planning through session parameters.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                 |
| ------------------------------ | ---------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | Very limited set of hints<br>• Index hints and optimizer hints as comments. Syntax differences. |

## SQL Server Usage

SQL Server hints are instructions that override automatic choices made by the query processor for DML and DQL statements. The term hint is misleading because, in reality, it forces an override to any other choice of run plan.

### JOIN Hints

You can explicitly add `LOOP`, `HASH`, `MERGE`, and `REMOTE` hints to a `JOIN` statement. For example, `…​ Table1 INNER LOOP JOIN Table2 ON …​`.

These hints force the optimizer to use nested loops, hash match, or merge physical join algorithms.

`REMOTE` enables processing a join with a remote table on the local server.

### Table Hints

Table hints override the default behavior of the query optimizer. Table hints are used to explicitly force a particular locking strategy or access method for a table operation clause. These hints don’t modify the defaults and apply only for the duration of the DML or DQL statement.

Some common table hints are `INDEX = <Index value>`, `FORCESEEK`, `NOLOCK`, and `TABLOCKX`.

### Query Hints

Query hints affect the entire set of query operators, not just the individual clause in which they appear. Query hints may be `JOIN` hints, table hints, or from a set of hints that are only relevant for query hints.

Some common table hints include `OPTIMIZE FOR`, `RECOMPILE`, `FORCE ORDER`, `FAST <rows>`.

You can specify query hints after the query itself following the `WITH` options clause.

### Plan Guides

Plan guides provide similar functionality to query hints in the sense they allow explicit user intervention and control over query optimizer plan choices. Plan guides can use either query hints or a full fixed, pre-generated plan attached to a query. The difference between query hints and plan guides is the way they are associated with a query.

While query or table hints need to be explicitly stated in the query text, they aren’t an option if you have no control over the source code generating these queries. If an application uses ad-hoc queries instead of stored procedures, views, and functions, the only way to affect query plans is to use plan guides. They are often used to mitigate performance issues with third-party software.

A plan guide consists of the statement whose run plan needs to be adjusted and either an `OPTION` clause that lists the desired query hints or a full XML query plan that is enforced as long it is valid.

At run time, SQL Server matches the text of the query specified by the guide and attaches the OPTION hints. Alternatively, it assigns the provided plan for running.

SQL Server supports three types of plan guides:

- **Object plan guides** target statements that run within the scope of a code object such as a stored procedure, function, or trigger. If the same statement is found in another context, the plan guide is not be applied.
- **SQL plan guides** are used for matching general ad-hoc statements not within the scope of code objects. In this case, any instance of the statement regardless of the originating client is assigned the plan guide.
- **Template plan guides** can be used to abstract statement templates that differ only in parameter values. You can use them to override the `PARAMETERIZATION` database option setting for a family of queries.

### Syntax

The following example uses query hints in a `SELECT` statement. You can use query hints in all DQL and DML statements.

```
SELECT <statement>
OPTION
(
{{HASH|ORDER} GROUP
|{CONCAT |HASH|MERGE} UNION
|{LOOP|MERGE|HASH} JOIN
|EXPAND VIEWS
|FAST <Rows>
|FORCE ORDER
|{FORCE|DISABLE} EXTERNALPUSHDOWN
|IGNORE_NONCLUSTERED_COLUMNSTORE_INDEX
|KEEP PLAN
|KEEPFIXED PLAN
|MAX_GRANT_PERCENT = <Percent>
|MIN_GRANT_PERCENT = <Percent>
|MAXDOP <Number of Processors>
|MAXRECURSION <Number>
|NO_PERFORMANCE_SPOOL
|OPTIMIZE FOR (@<Variable> {UNKNOWN|= <Value>}[,...])
|OPTIMIZE FOR UNKNOWN
|PARAMETERIZATION {SIMPLE|FORCED}
|RECOMPILE
|ROBUST PLAN
|USE HINT ('<Hint>' [,...])
|USE PLAN N'<XML Plan>'
|TABLE HINT (<Object Name> [,<Table Hint>[[,...]])
});
```

The following example creates a plan guide.

```
EXECUTE sp_create_plan_guide @name = '<Plan Guide Name>'
  ,@stmt = '<Statement>'
  ,@type = '<OBJECT|SQL|TEMPLATE>'
  ,@module_or_batch = 'Object Name>'|'<Batch Text>'| NULL
  ,@params = '<Parameter List>'|NULL }
  ,@hints = 'OPTION(<Query Hints>'|'<XML Plan>'|NULL;
```

### Examples

Limit parallelism for a sales report query.

```
EXEC sp_create_plan_guide
  @name = N'SalesReportPlanGuideMAXDOP',
  @stmt = N'SELECT *
    FROM dbo.fn_SalesReport(GETDATE())
  @type = N'SQL',
  @module_or_batch = NULL,
  @params = NULL,
  @hints = N'OPTION (MAXDOP 1)';
```

Use table and query hints.

```
SELECT *
FROM MyTable1 AS T1
  WITH (FORCESCAN)
  INNER LOOP JOIN
  MyTable2 AS T2
  WITH (TABLOCK, HOLDLOCK)
  ON T1.Col1 = T2.Col1
WHERE T1.Date BETWEEN DATEADD(DAY, -7, GETDATE()) AND GETDATE()
```

For more information, see [Hints (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql?view=sql-server-ver15") and [Plan Guides](https://docs.microsoft.com/en-us/sql/relational-databases/performance/plan-guides?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/performance/plan-guides?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL doesn’t support database hints to influence the behavior of the query planner, and you can’t influence how run plans are generated from within SQL queries. Although database hints aren’t directly supported, session parameters (also known as Query Planning Parameters) can influence the behavior of the query optimizer at the session level.

### Examples

Configure the query planner to use indexes instead of full table scans (disable SEQSCAN).

```
SET ENABLE_SEQSCAN=FALSE;
```

Set the query planner’s estimated cost of a disk page fetch that is part of a series of sequential fetches (`SEQ_PAGE_COST`) and set the planner’s estimate of the cost of a non-sequentially-fetched disk page (`RANDOM_PAGE_COST`). Reducing the value of `RANDOM_PAGE_COST` relative to `SEQ_PAGE_COST` causes the query planner to prefer index scans, while raising the value makes index scans more expensive.

```
SET SEQ_PAGE_COST to 4;
SET RANDOM_PAGE_COST to 1;
```

Turn on or turn off the query planner’s use of nested-loops when performing joins. While it is impossible to completely disable the usage of nested-loop joins, setting the ENABLE_NESTLOOP to OFF discourages the query planner from choosing nested-loop joins compared to alternative join methods.

```
SET ENABLE_NESTLOOP to FALSE;
```

For more information, see [Query Planning](https://www.postgresql.org/docs/13/static/runtime-config-query.html "https://www.postgresql.org/docs/13/static/runtime-config-query.html") in the _PostgreSQL documentation_.
