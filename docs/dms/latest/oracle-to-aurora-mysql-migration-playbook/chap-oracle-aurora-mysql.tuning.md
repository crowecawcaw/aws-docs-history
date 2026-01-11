# Database hints

With AWS DMS, you can configure Oracle session parameters and MySQL session variables to optimize performance, control resource usage, and customize database behavior during migration tasks. Oracle session parameters and MySQL session variables are special configuration settings that influence how the database engine operates and processes data. These settings can be crucial for ensuring efficient data transfer, minimizing resource contention, and adhering to organizational policies or regulatory requirements.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                          |
| ------------------------------ | ---------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | Very limited set of hints in MySQL. Use index hints and optimizer hints as comments. Syntax differences. |

## Oracle usage

Oracle provides users with the ability to influence how the query optimizer behaves and the decisions made to generate query run plans. Controlling the behavior of the database optimizer is performed using database hints. They can be defined as a directive operation to the optimizer and alter the decisions of how run plans are generated.

Oracle supports over 60 different database hints, and each database hint can have 0 or more arguments. Database hints are divided into different categories such as optimizer hints, join order hints, and parallel run hints.

Database hints are embedded directly into the SQL queries immediately following the `SELECT` keyword using the following format: `/* <DB_HINT> */`.

### Examples

Force the query optimizer to use a specific index for data access.

```
SELECT /* INDEX(EMP, IDX_EMP_HIRE_DATE)*/ * FROM EMPLOYEES EMP
WHERE HIRE_DATE >= '01-JAN-2010';

Run Plan
Plan hash value: 3035503638
| Id | Operation                   | Name          | Rows | Bytes | Cost (%CPU) | Time
| 0  | SELECT STATEMENT            |               | 1    | 62    | 2 (0)       | 00:00:01
| 1  | TABLE ACCESS BY INDEX ROWID | EMPLOYEES     | 1    | 62    | 2 (0)       | 00:00:01
|* 2 | INDEX RANGE SCAN            | IDX_HIRE_DATE | 1    |       | 1 (0)       | 00:00:01

Predicate Information (identified by operation id):
2 - access("HIRE_DATE">=TO_DATE(' 2010-01-01 00:00:00', 'syyyy-mm-dd hh24:mi:ss'))
```

For more information, see [Additional Hints](https://docs.oracle.com/cd/E25178_01/server.1111/e16638/hintsref.htm#CHDIDIDI "https://docs.oracle.com/cd/E25178_01/server.1111/e16638/hintsref.htm#CHDIDIDI") and [Influencing the Optimizer](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/influencing-the-optimizer.html#GUID-8758EF88-1CC6-41BD-8581-246702414D1D "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/influencing-the-optimizer.html#GUID-8758EF88-1CC6-41BD-8581-246702414D1D") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL supports two types of hints: optimizer hints and index hints.

### Index hints

The `USE INDEX` hint limits the optimizer’s choice to one of the indexes listed in the <Index List> white list. Alternatively, indexes can be black listed using the `IGNORE` keyword.

The `FORCE INDEX` hint is similar to `USE INDEX (index_list)`, but with strong favor towards seek against scan. The hints use the actual index names, not column names. You can refer to primary keys using the keyword `PRIMARY`.

**Syntax**

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

###### Note

In Aurora MySQL, the primary key is the clustered index.

The syntax for index hints has the following characteristics: \* You can omit `<Index List>` for `USE INDEX` only. It translates to _don’t use any indexes_, which is equivalent to a clustered index scan. \* Index hints can be further scoped down using the `FOR` clause. Use `FOR JOIN`, `FOR ORDER BY`, or `FOR GROUP BY` to limit the hint applicability to that specific query processing phase. \* Multiple index hints can be specified for the same or different scope.

### Optimizer hints

Optimizer hints give developers or administrators control over some of the optimizer decision tree. They are specified within the statement text as a comment with the prefix `+`.

Optimizer hints may pertain to different scopes and are valid in only one or two scopes. The available scopes for optimizer hints in descending scope width order are:

- **Global** hints affect the entire statement. Only `MAX_EXECUTION TIME` is a global optimizer hint.
- **Query-level** hints affect a query block within a composed statement such as UNION or a subquery.
- **Table-level** hints affect a table within a query block.
- **Index-level** hints affect an index of a table.

**Syntax**

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

The following optimizer hints are available in Aurora MySQL.

| Hint Name                 | Description                                               | Applicable Scopes  |
| ------------------------- | --------------------------------------------------------- | ------------------ |
| `BKA`, `NO_BKA`           | Turns on or turns off batched key access join processing  | Query block, table |
| `BNL`, `NO_BNL`           | Turns on or turns off block nested loop join processing   | Query block, table |
| `MAX_EXECUTION_TIME`      | Limits statement run time                                 | Global             |
| `MRR`, `NO_MRR`           | Turns on or turns off multi-range read optimization       | Table, index       |
| `NO_ICP`                  | Turns off index condition push-down optimization          | Table, index       |
| `NO_RANGE_OPTIMIZATION`   | Turns off range optimization                              | Table, index       |
| `QB_NAME`                 | Assigns a logical name to a query block                   | Query block        |
| `SEMIJOIN`, `NO_SEMIJOIN` | Turns on or turns off semi-join strategies                | Query block        |
| `SUBQUERY`                | Determines `MATERIALIZATION`, and `INTOEXISTS` processing | Query block        |

You can use query block names with `QB_NAME` to distinguish a block for limiting the scope of the table hint. Add `@` to indicate a hint scope for one or more named subqueries. Consider the following example:

```
SELECT /*+ SEMIJOIN(@SubQuery1 FIRSTMATCH, LOOSESCAN) */ *
FROM Table1
WHERE Col1 IN (SELECT /*+ QB_NAME(SubQuery1) */ Col1
    FROM t3);
```

Values for `MAX_EXECUTION_TIME` are measured in seconds and are always global for the entire query.

###### Note

This option doesn’t exist in Oracle, where the run time limit pertains to the session scope.

### Migration considerations

In general, the Aurora MySQL hint framework is relatively limited compared to the granular control provided by Oracle. It is recommended to start migration testing with all hints removed. Then, selectively apply hints as a last resort if other means such as schema, index, and query optimizations have failed.

Aurora MySQL uses a list of indexes and hints, both white list (USE) and black list (IGNORE), as opposed to Oracle’s explicit index approach.

Index hints are not mandatory instructions. Aurora MySQL may choose alternatives if it cannot use the hinted index.

### Examples

Force an index access.

```
SELECT * FROM Table1 USE INDEX (Index1) ORDER BY Col1;
```

Specify multiple index hints.

```
SELECT * FROM Table1
    USE INDEX (Index1)
    INNER JOIN Table2
        IGNORE INDEX(Index2)
        ON Table1.Col1 = Table2.Col1
    ORDER BY Col1;
```

Specify optimizer hints.

```
SELECT /*+ NO_RANGE_OPTIMIZATION(Table1 PRIMARY, Index2) */
Col1 FROM Table1 WHERE Col2 = 300;
```

```
SELECT /*+ BKA(t1) NO_BKA(t2) */ * FROM Table1 INNER JOIN Table2 ON ...;
```

```
SELECT /*+ NO_ICP(t1, t2) */ * FROM Table1 INNER JOIN Table2 ON ...;
```

## Summary

| Feature                          | Oracle                                                                                             | Aurora MySQL                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Force a specific plan            | `DBMS_SPM`                                                                                         | N/A                                                    |
| Join hints                       | `USE_NL`, `NO_USE_NL`, `USE_NL_WITH_INDEX`, `USE_MERGE`, `NO_USE_MERGE`, `USE_HASH`, `NO_USE_HASH` | `BNL`, `NO_BNL` (Block Nested Loops)                   |
| Force scan                       | `FULL`                                                                                             | `USE` with no index list forces a clustered index scan |
| Force an index                   | `INDEX`                                                                                            | `USE`                                                  |
| Allow list and deny list indexes | `NO_INDEX`                                                                                         | Supported with `USE` and `IGNORE`                      |
| Parameter value hints            | `opt_param`                                                                                        | N/A                                                    |

For more information, see [Controlling the Query Optimizer](https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html "https://dev.mysql.com/doc/refman/5.7/en/controlling-optimizer.html"), [Optimizer Hints](https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html "https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html"), [Index Hints](https://dev.mysql.com/doc/refman/5.7/en/index-hints.html "https://dev.mysql.com/doc/refman/5.7/en/index-hints.html"), and [Optimizing Subqueries, Derived Tables, and View References](https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html "https://dev.mysql.com/doc/refman/5.7/en/subquery-optimization.html") in the _MySQL documentation_.
