# Oracle and PostgreSQL run plans

With AWS DMS, you can analyze and optimize database query performance by examining Oracle and PostgreSQL run plans. A run plan is the sequence of operations that the database engine performs to execute a SQL statement.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                      |
| ------------------------------ | ---------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | Syntax differences. Completely different optimizer with different operators and rules in PostgreSQL. |

## Oracle usage

Run plans represent the choices made by the query optimizer for accessing database data. The query optimizer generates run plans for `SELECT`, `INSERT`, `UPDATE` and `DELETE` statements. Users and database administrators can view run plans for specific queries and DML operations.

Run plans are especially useful for performance tuning of queries. For example, determining if new indexes should be created. Run plans can be affected by data volumes, data statistics, and instance parameters (global or session parameters).

Run plans are displayed as a structured tree with the following information:

- Tables access by the SQL statement and the referenced order for each table.
- Access method for each table in the statement (full table scan vs. index access).
- Algorithms used for join operations between tables (hash vs. nested loop joins).
- Operations performed on retrieved data as such as filtering, sorting, and aggregations.
- Information about rows being processed (cardinality) and the cost for each operation.
- Table partitions being accessed.
- Information about parallel runs.

Oracle 19 introduces SQL Quarantine: now queries that consume resources excessively can be automatically quarantined and prevented from being executed. These queries run plans are also quarantined.

**Examples**

Review the potential run plan for a query using the `EXPLAIN PLAN` statement.

```
SET AUTOTRACE TRACEONLY EXPLAIN
SELECT EMPLOYEE_ID, LAST_NAME, FIRST_NAME FROM EMPLOYEES
WHERE LAST_NAME='King' AND FIRST_NAME='Steven';

Run Plan
Plan hash value: 2077747057
Id  Operation                    Name         Rows  Bytes  Cost (%CPU)  Time
0   SELECT STATEMENT                          1     16     2 (0)        00:00:01
1   TABLE ACCESS BY INDEX ROWID  EMPLOYEES    1     16     2 (0)        00:00:01
2   INDEX RANGE SCAN             EMP_NAME_IX  1            1 (0)        00:00:01

Predicate Information (identified by operation id):
2 - access("LAST_NAME"='King' AND "FIRST_NAME"='Steven')
```

`SET AUTOTRACE TRACEONLY EXPLAIN` instructs SQL\*PLUS to show the run plan without actually running the query itself.

The `EMPLOYEES` table contains indexes for both the `LAST_NAME` and `FIRST_NAME` columns. Step 2 of the run plan indicates the optimizer is performing an `INDEX RANGE SCAN` in order to retrieve the filtered employee name.

View a different run plan displaying a `FULL TABLE SCAN`.

```
SET AUTOTRACE TRACEONLY EXPLAIN
SELECT EMPLOYEE_ID, LAST_NAME, FIRST_NAME FROM EMPLOYEES
WHERE SALARY > 10000;

Run Plan
Plan hash value: 1445457117
Id  Operation          Name         Rows  Bytes  Cost (%CPU)  Time
0   SELECT STATEMENT                72    1368   3 (0)        00:00:01
1   TABLE ACCESS FULL  EMPLOYEES    72    1368   3 (0)        00:00:01

Predicate Information (identified by operation id):
1 - filter("SALARY">10000)
```

For more information, see [Explaining and Displaying Execution Plans](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/generating-and-displaying-execution-plans.html#GUID-60E30B1C-342B-4D71-B154-C26623D6A3B1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/generating-and-displaying-execution-plans.html#GUID-60E30B1C-342B-4D71-B154-C26623D6A3B1") in the _Oracle documentation_.

## PostgreSQL usage

The PostgreSQL equivalent to Oracle `EXPLAIN PLAN` is the `EXPLAIN` keyword. The `EXPLAIN` keyword is used to display the run plan for a supplied SQL statement.

Similar to Oracle, the query planner in PostgreSQL will generate the estimated run plan for actions such as: `SELECT`, `INSERT`, `UPDATE` and `DELETE`. It builds a structured tree of plan nodes representing the different actions taken (the sign `→` represents a root line in the PostgreSQL run plan).

In addition, the `EXPLAIN` statement provides statistical information regarding each action such as: cost, rows, time and loops.

When you use the `EXPLAIN` command as part of a SQL statement, the statement will not run, and the run plan will be an estimation. By using the `EXPLAIN ANALYZE` command, the statement will run in addition to displaying the run plan.

### PostgreSQL EXPLAIN synopsis

```
EXPLAIN [ ( option value[, ...] ) ] statement
EXPLAIN [ ANALYZE ] [ VERBOSE ] statement

where option and values can be one of:

  ANALYZE [ boolean ]
  VERBOSE [ boolean ]
  COSTS [ boolean ]
  BUFFERS [ boolean ]
  TIMING [ boolean ]
  SUMMARY [ boolean ] (since PostgreSQL 10)
  FORMAT { TEXT | XML | JSON | YAML }
```

By default, planning and running time are displayed when you use `EXPLAIN ANALYZE`, but not in other cases. A new `SUMMARY` option provides explicit control of this information. Use `SUMMARY` to include planning and run time metrics in your output.

PostgreSQL provides configurations options that will cancel SQL statements running longer than provided time limit. To use this option, you can set the `statement_timeout` instance-level parameter.

If the value is specified without units, it is taken as milliseconds. A value of zero (the default) disables the timeout.

Third-party connection pooler solutions such as `Pgbouncer` and `PgPool` build on that and allow more flexibility in controlling how long connection to DB can run, be in idle state and so on.

### Aurora PostgreSQL Query Plan Management

The Aurora PostgreSQL Query Plan Management (QPM) feature solves the problem of plan instability by allowing database users to maintain stable, yet optimal, performance for a set of managed SQL statements. QPM primarily serves two main objectives:

- **Plan stability**. QPM prevents plan regression and improves plan stability when any of the above changes occur in the system.
- **Plan adaptability**. QPM automatically detects new minimum-cost plans and controls when new plans may be used and adapts to the changes.

The quality and consistency of query optimization have a major impact on the performance and stability of any relational database management system (RDBMS). Query optimizers create a query execution plan for a SQL statement at a specific point in time. After conditions change, the optimizer might pick a different plan that makes performance better or worse.

In some cases, a number of changes can all cause the query optimizer to choose a different plan and lead to performance regression. These changes include changes in statistics, constraints, environment settings, query parameter bindings, and software upgrades. Regression is a major concern for high-performance applications.

With query plan management, you can control execution plans for a set of statements that you want to manage.

You can do the following:

- Improve plan stability by forcing the optimizer to choose from a small number of known, good plans.
- Optimize plans centrally and then distribute the best plans globally.
- Identify indexes that aren’t used and assess the impact of creating or dropping an index.
- Automatically detect a new minimum-cost plan discovered by the optimizer.
- Try new optimizer features with less risk, because you can choose to approve only the plan changes that improve performance.

**Examples**

View the run plan of a SQL statement using the `EXPLAIN` command.

```
EXPLAIN
  SELECT EMPLOYEE_ID, LAST_NAME, FIRST_NAME FROM EMPLOYEES
  WHERE LAST_NAME='King' AND FIRST_NAME='Steven';

Index Scan using idx_emp_name on employees (cost=0.14..8.16 rows=1 width=18)
Index Cond: (((last_name)::text = 'King'::text) AND ((first_name)::text = 'Steven'::text))
(2 rows)
```

Run the same statement with the `ANALYZE` keyword.

```
EXPLAIN ANALYZE
  SELECT EMPLOYEE_ID, LAST_NAME, FIRST_NAME FROM EMPLOYEES
  WHERE LAST_NAME='King' AND FIRST_NAME='Steven';

Seq Scan on employees (cost=0.00..3.60 rows=1 width=18) (actual time=0.012..0.024 rows=1 loops=1)
Filter: (((last_name)::text = 'King'::text) AND ((first_name)::text = 'Steven'::text))
Rows Removed by Filter: 106
Planning time: 0.073 ms
Execution time: 0.037 ms
(5 rows)
```

By adding the ANALYZE keyword and executing the statement, we get additional information in addition to the execution plan.

View a PostgreSQL run plan showing a `FULL TABLE SCAN`.

```
EXPLAIN ANALYZE
  SELECT EMPLOYEE_ID, LAST_NAME, FIRST_NAME FROM EMPLOYEES
  WHERE SALARY > 10000;

Seq Scan on employees (cost=0.00..3.34 rows=15 width=18) (actual time=0.012..0.036 rows=15 loops=1)
Filter: (salary > '10000'::numeric)
Rows Removed by Filter: 92
Planning time: 0.069 ms
Execution time: 0.052 ms
(5 rows)
```

PostgreSQL can perform several scan types for processing and retrieving data from tables including sequential scans, index scans, and bitmap index scans. The sequential scan (`Seq Scan`) is PostgreSQL equivalent for Oracle `Table access full` (full table scan).

For more information, see [EXPLAIN](https://www.postgresql.org/docs/13/sql-explain.html "https://www.postgresql.org/docs/13/sql-explain.html") in the _PostgreSQL documentation_.
