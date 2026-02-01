Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# EXPLAIN

Displays the execution plan for a query statement without running the query. For
information about the query analysis workflow, see [Query analysis workflow](c-query-analysis-process.md "c-query-analysis-process.md").

## Syntax

```
EXPLAIN [ VERBOSE ] *query*

```

## Parameters

VERBOSE

Displays the full query plan instead of just a summary.

_query_

Query statement to explain. The query can be a SELECT, INSERT, CREATE TABLE
AS, UPDATE, or DELETE statement.

## Usage notes

EXPLAIN performance is sometimes influenced by the time it takes to create temporary
tables. For example, a query that uses the common subexpression optimization requires
temporary tables to be created and analyzed in order to return the EXPLAIN output. The
query plan depends on the schema and statistics of the temporary tables. Therefore, the
EXPLAIN command for this type of query might take longer to run than expected.

You can use EXPLAIN only for the following commands:

- SELECT
- SELECT INTO
- CREATE TABLE AS
- INSERT
- UPDATE
- DELETE

The EXPLAIN command will fail if you use it for other SQL commands, such as data
definition language (DDL) or database operations.

The EXPLAIN output relative unit costs are used by Amazon Redshift to choose a query plan. Amazon Redshift
compares the sizes of various resource estimates to determine the plan.

## Query planning and

execution steps

The execution plan for a specific Amazon Redshift query statement breaks down execution and
calculation of a query into a discrete sequence of steps and table operations that
eventually produce a final result set for the query. For information about query
planning, see [Query processing](c-query-processing.md "c-query-processing.md").

The following table provides a summary of steps that Amazon Redshift can use in developing
an execution plan for any query a user submits for execution.

| EXPLAIN operators                                                                                                                                                                                                                                                                                         | Query execution steps | Description                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **SCAN:**                                                                                                                                                                                                                                                                                                 |
| Sequential Scan                                                                                                                                                                                                                                                                                           | scan                  | Amazon Redshift relation scan or table scan operator or step.<br>Scans whole table sequentially from beginning to end; also evaluates query<br>constraints for every row (Filter) if specified with WHERE clause. Also used<br>to run INSERT, UPDATE, and DELETE statements.                                   |
| \*_JOINS:_<br>• Amazon Redshift uses different join operators based on the<br>physical design of the tables being joined, the location of the data<br>required for the join, and specific attributes of the query itself. Subquery<br>Scan -<br>• Subquery scan and append are used to run UNION queries. |
| Nested Loop                                                                                                                                                                                                                                                                                               | nloop                 | Least optimal join; mainly used for cross-joins<br>(Cartesian products; without a join condition) and some inequality joins.                                                                                                                                                                                   |
| Hash Join                                                                                                                                                                                                                                                                                                 | hjoin                 | Also used for inner joins and left and right outer joins<br>and typically faster than a nested loop join. Hash Join reads the outer<br>table, hashes the joining column, and finds matches in the inner hash table.<br>Step can spill to disk. (Inner input of hjoin is hash step which can be<br>disk-based.) |
| Merge Join                                                                                                                                                                                                                                                                                                | mjoin                 | Also used for inner joins and outer joins<br>(for join tables that are both distributed and sorted on the joining<br>columns). Typically the fastest Amazon Redshift join algorithm, not including other<br>cost considerations.                                                                               |
| \*_AGGREGATION:_<br>• Operators and steps used for queries that<br>involve aggregate functions and GROUP BY operations.                                                                                                                                                                                   |
| Aggregate                                                                                                                                                                                                                                                                                                 | aggr                  | Operator/step for scalar aggregate functions.                                                                                                                                                                                                                                                                  |
| HashAggregate                                                                                                                                                                                                                                                                                             | aggr                  | Operator/step for grouped aggregate functions. Can<br>operate from disk by virtue of hash table spilling to disk.                                                                                                                                                                                              |
| GroupAggregate                                                                                                                                                                                                                                                                                            | aggr                  | Operator sometimes chosen for grouped aggregate queries<br>if the Amazon Redshift configuration setting for force_hash_grouping setting is<br>off.                                                                                                                                                             |
| \*_SORT:_<br>• Operators and steps used when queries have to sort or<br>merge result sets.                                                                                                                                                                                                                |
| Sort                                                                                                                                                                                                                                                                                                      | sort                  | Sort performs the sorting specified by the ORDER BY<br>clause as well as other operations such as UNIONs and joins. Can operate<br>from disk.                                                                                                                                                                  |
| Merge                                                                                                                                                                                                                                                                                                     | merge                 | Produces final sorted results of a query based on<br>intermediate sorted results derived from operations performed in parallel.                                                                                                                                                                                |
| **EXCEPT,<br>INTERSECT, and UNION operations:**                                                                                                                                                                                                                                                           |
| SetOp Except [Distinct]                                                                                                                                                                                                                                                                                   | hjoin                 | Used for EXCEPT queries. Can operate from disk based on<br>virtue of fact that input hash can be disk-based.                                                                                                                                                                                                   |
| Hash Intersect [Distinct]                                                                                                                                                                                                                                                                                 | hjoin                 | Used for INTERSECT queries. Can operate from disk based<br>on virtue of fact that input hash can be disk-based.                                                                                                                                                                                                |
| Append [All                                                                                                                                                                                                                                                                                               | Distinct]             | save                                                                                                                                                                                                                                                                                                           | Append used with Subquery Scan to implement UNION and<br>UNION ALL queries. Can operate from disk based on virtue of "save". |
| **Miscellaneous/Other:**                                                                                                                                                                                                                                                                                  |
| Hash                                                                                                                                                                                                                                                                                                      | hash                  | Used for inner joins and left and right outer joins<br>(provides input to a hash join). The Hash operator creates the hash table<br>for the inner table of a join. (The inner table is the table that is checked<br>for matches and, in a join of two tables, is usually the smaller of the<br>two.)           |
| Limit                                                                                                                                                                                                                                                                                                     | limit                 | Evaluates the LIMIT clause.                                                                                                                                                                                                                                                                                    |
| Materialize                                                                                                                                                                                                                                                                                               | save                  | Materialize rows for input to nested loop joins and some<br>merge joins. Can operate from disk.                                                                                                                                                                                                                |
| --                                                                                                                                                                                                                                                                                                        | parse                 | Used to parse textual input data during a load.                                                                                                                                                                                                                                                                |
| --                                                                                                                                                                                                                                                                                                        | project               | Used to rearrange columns and compute expressions, that<br>is, project data.                                                                                                                                                                                                                                   |
| Result                                                                                                                                                                                                                                                                                                    | --                    | Run scalar functions that don't involve any table<br>access.                                                                                                                                                                                                                                                   |
| --                                                                                                                                                                                                                                                                                                        | return                | Return rows to the leader or client.                                                                                                                                                                                                                                                                           |
| Subplan                                                                                                                                                                                                                                                                                                   | --                    | Used for certain subqueries.                                                                                                                                                                                                                                                                                   |
| Unique                                                                                                                                                                                                                                                                                                    | unique                | Eliminates duplicates from SELECT DISTINCT and UNION<br>queries.                                                                                                                                                                                                                                               |
| Window                                                                                                                                                                                                                                                                                                    | window                | Compute aggregate and ranking window functions. Can<br>operate from disk.                                                                                                                                                                                                                                      |
| **Network<br>Operations:**                                                                                                                                                                                                                                                                                |
| Network (Broadcast)                                                                                                                                                                                                                                                                                       | bcast                 | Broadcast is also an attribute of Join Explain operators<br>and steps.                                                                                                                                                                                                                                         |
| Network (Distribute)                                                                                                                                                                                                                                                                                      | dist                  | Distribute rows to compute nodes for parallel processing<br>by data warehouse cluster.                                                                                                                                                                                                                         |
| Network (Send to Leader)                                                                                                                                                                                                                                                                                  | return                | Sends results back to the leader for further processing.                                                                                                                                                                                                                                                       |
| **DML<br>Operations (operators that modify data):**                                                                                                                                                                                                                                                       |
| Insert (using Result)                                                                                                                                                                                                                                                                                     | insert                | Inserts data.                                                                                                                                                                                                                                                                                                  |
| Delete (Scan + Filter)                                                                                                                                                                                                                                                                                    | delete                | Deletes data. Can operate from disk.                                                                                                                                                                                                                                                                           |
| Update (Scan + Filter)                                                                                                                                                                                                                                                                                    | delete, insert        | Implemented as delete and Insert.                                                                                                                                                                                                                                                                              |

## Using EXPLAIN for RLS

If a query contains a table that is subject to row-level security (RLS) policies,
EXPLAIN displays a special RLS SecureScan node. Amazon Redshift also logs the same node type to
the STL_EXPLAIN system table. EXPLAIN doesn't reveal the RLS predicate that applies
to dim_tbl. The RLS SecureScan node type serves as an indicator that the execution plan
contains additional operations that are invisible to the current user.

The following example illustrates an RLS SecureScan node.

```
EXPLAIN
SELECT D.cint
FROM fact_tbl F INNER JOIN dim_tbl D ON F.k_dim = D.k
WHERE F.k_dim / 10 > 0;
                               QUERY PLAN
------------------------------------------------------------------------
 XN Hash Join DS_DIST_ALL_NONE  (cost=0.08..0.25 rows=1 width=4)
   Hash Cond: ("outer".k_dim = "inner"."k")
   ->  *XN* *RLS SecureScan f  (cost=0.00..0.14 rows=2 width=4)*
         Filter: ((k_dim / 10) > 0)
   ->  XN Hash  (cost=0.07..0.07 rows=2 width=8)
         ->  XN Seq Scan on dim_tbl d  (cost=0.00..0.07 rows=2 width=8)
               Filter: (("k" / 10) > 0)
```

To enable full investigation of query plans that are subject to RLS, Amazon Redshift offers
the EXPLAIN RLS system permissions. Users that have been granted this permission can
inspect complete query plans that also include RLS predicates.

The following example illustrates an additional Seq Scan below the RLS SecureScan
node also includes the RLS policy predicate (k_dim > 1).

```
EXPLAIN SELECT D.cint
FROM fact_tbl F INNER JOIN dim_tbl D ON F.k_dim = D.k
WHERE F.k_dim / 10 > 0;
                                   QUERY PLAN
---------------------------------------------------------------------------------
 XN Hash Join DS_DIST_ALL_NONE  (cost=0.08..0.25 rows=1 width=4)
   Hash Cond: ("outer".k_dim = "inner"."k")
   *->  XN RLS SecureScan f  (cost=0.00..0.14 rows=2 width=4)
         Filter: ((k_dim / 10) > 0)*
         ->  *XN* *Seq Scan on fact_tbl rls_table  (cost=0.00..0.06 rows=5 width=8)
               Filter: (k_dim > 1)*
   ->  XN Hash  (cost=0.07..0.07 rows=2 width=8)
         ->  XN Seq Scan on dim_tbl d  (cost=0.00..0.07 rows=2 width=8)
               Filter: (("k" / 10) > 0)
```

While the EXPLAIN RLS permission is granted to a user, Amazon Redshift logs the full query
plan including RLS predicates in the STL_EXPLAIN system table. Queries that are run
while this permission is not granted will be logged without RLS internals. Granting or
removing the EXPLAIN RLS permission won't change what Amazon Redshift has logged to
STL_EXPLAIN for previous queries.

### AWS Lake Formation-RLS protected Redshift relations

The following example illustrates an LF SecureScan node, which you can use to view
Lake Formation-RLS relations.

```
EXPLAIN
SELECT *
FROM lf_db.public.t_share
WHERE a > 1;
QUERY PLAN
---------------------------------------------------------------
XN LF SecureScan t_share  (cost=0.00..0.02 rows=2 width=11)
(2 rows)
```

## Examples

###### Note

For these examples, the sample output might vary depending on Amazon Redshift
configuration.

The following example returns the query plan for a query that selects the EVENTID,
EVENTNAME, VENUEID, and VENUENAME from the EVENT and VENUE tables:

```
explain
select eventid, eventname, event.venueid, venuename
from event, venue
where event.venueid = venue.venueid;
```

```
                                QUERY PLAN
--------------------------------------------------------------------------
XN Hash Join DS_DIST_OUTER  (cost=2.52..58653620.93 rows=8712 width=43)
Hash Cond: ("outer".venueid = "inner".venueid)
->  XN Seq Scan on event  (cost=0.00..87.98 rows=8798 width=23)
->  XN Hash  (cost=2.02..2.02 rows=202 width=22)
->  XN Seq Scan on venue  (cost=0.00..2.02 rows=202 width=22)
(5 rows)
```

The following example returns the query plan for the same query with verbose
output:

```
explain verbose
select eventid, eventname, event.venueid, venuename
from event, venue
where event.venueid = venue.venueid;
```

```
                                QUERY PLAN
--------------------------------------------------------------------------
{HASHJOIN
:startup_cost 2.52
:total_cost 58653620.93
:plan_rows 8712
:plan_width 43
:best_pathkeys <>
:dist_info DS_DIST_OUTER
:dist_info.dist_keys (
TARGETENTRY
{
VAR
:varno 2
:varattno 1
...

XN Hash Join DS_DIST_OUTER  (cost=2.52..58653620.93 rows=8712 width=43)
Hash Cond: ("outer".venueid = "inner".venueid)
->  XN Seq Scan on event  (cost=0.00..87.98 rows=8798 width=23)
->  XN Hash  (cost=2.02..2.02 rows=202 width=22)
->  XN Seq Scan on venue  (cost=0.00..2.02 rows=202 width=22)
(519 rows)
```

The following example returns the query plan for a CREATE TABLE AS (CTAS) statement:

```
explain create table venue_nonulls as
select * from venue
where venueseats is not null;

QUERY PLAN
-----------------------------------------------------------
XN Seq Scan on venue  (cost=0.00..2.02 rows=187 width=45)
Filter: (venueseats IS NOT NULL)
(2 rows)
```
