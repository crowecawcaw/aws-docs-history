# Query hints and plan guides

This topic provides reference information about query hints and their compatibility between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can use this knowledge to understand the differences in query optimization techniques when migrating from SQL Server to Aurora MySQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                      | Key differences |
| ------------------------------ | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Two star feature compatibility | Three star automation level        | [Query Hints](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.queryhints "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.queryhints") | Difference.     |

## SQL Server Usage

SQL Server _hints_ are instructions that override automatic choices made by the query processor for DML and DQL statements. The term hint is misleading because, in reality, it forces an override to any other choice of the run plan.

### JOIN Hints

You can explicitly add `LOOP`, `HASH`, `MERGE`, and `REMOTE` hints to a `JOIN`. For example, `…​ Table1 INNER LOOP JOIN Table2 ON …​`. These hints force the optimizer to use nested loops, hash match, or merge physical join algorithms. `REMOTE` enables processing a join with a remote table on the local server.

### Table Hints

Table hints override the default behavior of the query optimizer. Table hints are used to explicitly force a particular locking strategy or access method for a table operation clause. These hints don’t modify the defaults and apply only for the duration of the DML or DQL statement. Some common table hints are `INDEX = <Index value>`, `FORCESEEK`, `NOLOCK`, and `TABLOCKX`.

### Query Hints

Query hints affect the entire set of query operators, not just the individual clause in which they appear. Query hints may be `JOIN` hints, table hints, or from a set of hints that are only relevant for query hints.

Some common table hints include `OPTIMIZE FOR`, `RECOMPILE`, `FORCE ORDER`, and `FAST <rows>`.

Query hints are specified after the query itself following the `WITH` options clause.

### Plan Guides

Plan guides provide similar functionality to query hints in the sense they allow explicit user intervention and control over query optimizer plan choices. Plan guides can use either query hints or a full fixed, pre-generated plan attached to a query. The difference between query hints and plan guides is the way they are associated with a query.

While query or table hints need to be explicitly stated in the query text, they aren’t an option if you have no control over the source code generating these queries. If an application uses one-time queries instead of stored procedures, views, and functions, the only way to affect query plans is to use plan guides. They are often used to mitigate performance challenges with third-party software.

A plan guide consists of the statement whose run plan needs to be adjusted and either an `OPTION` clause that lists the desired query hints or a full XML query plan that is enforced as long it is valid.

At run time, SQL Server matches the text of the query specified by the guide and attaches the OPTION hints. Or, it assigns the provided plan for run.

SQL Server supports three types of plan guides.

- **Object plan guides** target statements that run within the scope of a code object such as a stored procedure, function, or trigger. If the same statement is found in another context, the plan guide isn’t be applied.
- **SQL plan guides** are used for matching general ad-hoc statements not within the scope of code objects. In this case, any instance of the statement regardless of the originating client is assigned the plan guide.
- **Template plan guides** can be used to abstract statement templates that differ only in parameter values. It can be used to override the `PARAMETERIZATION` database option setting for a family of queries.

### Syntax

Use the following syntax to create query hints.

###### Note

The following syntax is for `SELECT`. Query hints can be used in all DQL and DML statements.

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

Use the following syntax to create a plan guide:

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

For more information, see [Hints](https://docs.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql?view=sql-server-ver15") and [Plan Guides](https://docs.microsoft.com/en-us/sql/relational-databases/performance/plan-guides?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/performance/plan-guides?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports two types of hints: optimizer hints and index hints. Unlike SQL Server, MySQL doesn’t provide a feature similar to plan guides.

### Index Hints

The index hints should appear familiar to SQL Server users although the syntax is somewhat different. Index hints are placed directly after the table name as with SQL Server, but the keywords are different.

#### Syntax

```
SELECT ...
FROM <Table Name>
    USE {INDEX|KEY}
        [FOR {JOIN|ORDER BY|GROUP BY}] (<Index List>)
    | IGNORE {INDEX|KEY}
        [FOR {JOIN|ORDER BY|GROUP BY}] (<Index List>)
    | FORCE {INDEX|KEY}
        [FOR {JOIN|ORDER BY|GROUP BY}] (<Index List>)
...n
```

The `USE INDEX` hint limits the optimizer’s choice to one of the indexes listed in the <Index List> allow list. Alternatively, indexes can be added to the deny list using the IGNORE keyword.

The `FORCE INDEX` hint is similar to `USE INDEX` (`index_list`), but with strong favor towards seek against scan. This hint is similar to the `FORCESEEK` hint in SQL Server, although the Aurora MySQL optimizer can choose a scan if other options aren’t valid.

The hints use the actual index names; not column names. You can refer to primary keys using the keyword `PRIMARY`.

###### Note

In Aurora MySQL, the primary key is the clustered index. For more information see [Indexes](chap-sql-server-aurora-mysql.md "chap-sql-server-aurora-mysql.md").

The syntax for index Aurora MySQL hints has the following characteristics:

- Omitting the `<Index List>` is allowed for `USE INDEX` only. It translates to don’t use any indexes, which is equivalent to a clustered index scan.
- Index hints can be further scoped down using the `FOR` clause. Use `FOR JOIN`, `FOR ORDER BY`, or `FOR GROUP BY` to limit the hint applicability to that specific query processing phase.
- Multiple index hints can be specified for the same or different scope.

### Optimizer Hints

Optimizer hints give developers or administrators control over some of the optimizer decision tree. They are specified within the statement text as a comment with the `+` prefix.

Optimizer hints may pertain to different scopes and are valid in only one or two scopes. The available scopes for optimizer hints in descending scope width order are:

- Global hints affect the entire statement. Only `MAX_EXECUTION TIME` is a global optimizer hint.
- Query-level hints affect a query block within a composed statement such as `UNION` or a subquery.
- Table-level hints affect a table within a query block.
- Index-level hints affect an index of a table.

#### Syntax

```
SELECT /*+ <Optimizer Hints> */ <Select List>...
```

```
INSERT /*+ <Optimizer Hints> */ INTO <Table>...
```

```
REPLACE /*+ <Optimizer Hints> */ INTO <Table>...
```

```
UPDATE /*+ <Optimizer Hints> */ <Table> SET...
```

```
DELETE /*+ <Optimizer Hints> */ FROM <Table>...
```

You can use the following optimizer hints in Aurora MySQL:

| Hint name                 | Description                                               | Applicable scopes  |
| ------------------------- | --------------------------------------------------------- | ------------------ |
| `BKA`, `NO_BKA`           | Turns on or off Batched Key Access join processing        | Query block, table |
| `BNL`, `NO_BNL`           | Turns on or off Block Nested-Loop join processing         | Query block, table |
| `MAX_EXECUTION_TIME`      | Limits statement run time                                 | Global             |
| `MRR`, `NO_MRR`           | Turns on or turns off multi-range read optimization       | Table, index       |
| `NO_ICP`                  | Turns off index condition push-down optimization          | Table, index       |
| `NO_RANGE_OPTIMIZATION`   | Turns off range optimization                              | Table, index       |
| `QB_NAME`                 | Assigns a logical name to a query block                   | Query block        |
| `SEMIJOIN`, `NO_SEMIJOIN` | Turns on or off semi-join strategies                      | Query block        |
| `SUBQUERY`                | Determines `MATERIALIZATION`, and `INTOEXISTS` processing | Query block        |

Query block names (using `QB_NAME`) are used to distinguish a block for limiting the scope of the table hint. Add `@` to indicate a hint scope for one or more named subqueries as shown in the following example.

```
SELECT /*+ SEMIJOIN(@SubQuery1 FIRSTMATCH, LOOSESCAN) */ *
FROM Table1
WHERE Col1 IN (SELECT /*+ QB_NAME(SubQuery1) */ Col1
FROM t3);
```

Values for `MAX_EXECUTION_TIME` are measured in seconds and are always global for the entire query.

###### Note

This option doesn’t exist in SQL Server where the run time limit is for the session scope.

For more information, see [Controlling the Query Optimizer](https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html "https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html"), [Optimizer Hints](https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html "https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html"), [Index Hints](https://dev.mysql.com/doc/refman/5.7/en/index-hints.html "https://dev.mysql.com/doc/refman/5.7/en/index-hints.html"), and [Optimizing Subqueries, Derived Tables, and View References](https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html "https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html") in the _MySQL documentation_.

### Migration Considerations

In general, the Aurora MySQL hint framework is relatively limited compared to the granular control provided by SQL Server. The specific optimizations used for SQL Server may be completely inapplicable to a new query optimizer. It is recommended to start migration testing with all hints removed. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed.

Aurora MySQL uses a list of indexes and hints, both allowed list or `USE` and disallowed list or `IGNORE`, as opposed to explicit index approach in SQL Server.

Index hints aren’t mandatory instructions. Aurora MySQL has some room to choose alternatives if it can’t use the hinted index. In SQL Server, forcing a non valid index or access method raises an error.

### Examples

Force an index access.

```
SELECT * FROM Table1 USE INDEX (Index1) ORDER BY Col1;
```

Specify multiple index hints.

```
SELECT * FROM Table1 USE INDEX (Index1) INNER JOIN Table2 IGNORE INDEX(Index2) ON
Table1.Col1 = Table2.Col1 ORDER BY Col1;
```

Specify optimizer hints.

```
SELECT /*+ NO_RANGE_OPTIMIZATION(Table1 PRIMARY, Index2) */ Col1 FROM Table1 WHERE
Col2 = 300;
```

```
SELECT /*+ BKA(t1) NO_BKA(t2) */ * FROM Table1 INNER JOIN Table2 ON ...;
```

```
SELECT /*+ NO_ICP(t1, t2) */ * FROM Table1 INNER JOIN Table2 ON ...;
```

## Summary

| Feature                                  | SQL Server               | Aurora MySQL                                           |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------ |
| Force a specific plan                    | Plan guides              | N/A                                                    |
| Apply hints to a query at runtime        | Plan guides              | N/A                                                    |
| Join hints                               | `LOOP`, `MERGE`, `HASH`  | `BNL`, `NO_BNL` (block-nested loops)                   |
| Locking hints                            | Supported                | N/A                                                    |
| Force seek or scan                       | `FORCESEEK`, `FORCESCAN` | `USE` with no index list forces a clustered index scan |
| Force an index                           | `INDEX=`                 | `USE`                                                  |
| Allowed list and disallowed list indexes | N/A                      | Supported with `USE` and `IGNORE`                      |
| Parameter value hints                    | `OPTIMIZE FOR`           | N/A                                                    |
| Compilation hints                        | `RECOMPILE`              | N/A                                                    |

For more information, see [Controlling the Query Optimizer](https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html "https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html"), [Optimizer Hints](https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html "https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html"), [Index Hints](https://dev.mysql.com/doc/refman/5.7/en/index-hints.html "https://dev.mysql.com/doc/refman/5.7/en/index-hints.html"), and [Optimizing Subqueries, Derived Tables, and View References](https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html "https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html") in the _MySQL documentation_.
