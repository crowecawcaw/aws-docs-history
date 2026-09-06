

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# EXPLAIN
<a name="r_EXPLAIN"></a>

Displays the execution plan for a query statement without running the query. For information about the query analysis workflow, see [Query analysis workflow](c-query-analysis-process.md).

## Syntax
<a name="r_EXPLAIN-synopsis"></a>

```
EXPLAIN [ VERBOSE ] query
```

## Parameters
<a name="r_EXPLAIN-parameters"></a>

VERBOSE   
Displays the full query plan instead of just a summary.

 *query*   
Query statement to explain. The query can be a SELECT, INSERT, CREATE TABLE AS, UPDATE, or DELETE statement.

## Usage notes
<a name="r_EXPLAIN-usage-notes"></a>

EXPLAIN performance is sometimes influenced by the time it takes to create temporary tables. For example, a query that uses the common subexpression optimization requires temporary tables to be created and analyzed in order to return the EXPLAIN output. The query plan depends on the schema and statistics of the temporary tables. Therefore, the EXPLAIN command for this type of query might take longer to run than expected.

You can use EXPLAIN only for the following commands:
+ SELECT
+ SELECT INTO
+ CREATE TABLE AS
+ INSERT
+ UPDATE
+ DELETE

The EXPLAIN command will fail if you use it for other SQL commands, such as data definition language (DDL) or database operations.

The EXPLAIN output relative unit costs are used by Amazon Redshift to choose a query plan. Amazon Redshift compares the sizes of various resource estimates to determine the plan.

## Query planning and execution steps
<a name="r_EXPLAIN-query-planning-and-execution-steps"></a>

The execution plan for a specific Amazon Redshift query statement breaks down execution and calculation of a query into a discrete sequence of steps and table operations that eventually produce a final result set for the query. For information about query planning, see [Query processing](c-query-processing.md).

The following table provides a summary of steps that Amazon Redshift can use in developing an execution plan for any query a user submits for execution.


<table>
<thead>
  <tr><th>EXPLAIN operators </th><th>Query execution steps </th><th>Description </th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>SCAN:</b> </td></tr>
  <tr><td> Sequential Scan </td><td>scan </td><td>Amazon Redshift relation scan or table scan operator or step. Scans whole table sequentially from beginning to end; also evaluates query constraints for every row (Filter) if specified with WHERE clause. Also used to run INSERT, UPDATE, and DELETE statements. </td></tr>
  <tr><td colspan="3"><b>JOINS:</b> Amazon Redshift uses different join operators based on the physical design of the tables being joined, the location of the data required for the join, and specific attributes of the query itself. Subquery Scan -- Subquery scan and append are used to run UNION queries. </td></tr>
  <tr><td>Nested Loop </td><td>nloop </td><td>Least optimal join; mainly used for cross-joins (Cartesian products; without a join condition) and some inequality joins. </td></tr>
  <tr><td>Hash Join </td><td>hjoin </td><td>Also used for inner joins and left and right outer joins and typically faster than a nested loop join. Hash Join reads the outer table, hashes the joining column, and finds matches in the inner hash table. Step can spill to disk. (Inner input of hjoin is hash step which can be disk-based.) </td></tr>
  <tr><td>Merge Join </td><td>mjoin </td><td>Also used for inner joins and outer joins (for join tables that are both distributed and sorted on the joining columns). Typically the fastest Amazon Redshift join algorithm, not including other cost considerations. </td></tr>
  <tr><td colspan="3"><b>AGGREGATION:</b> Operators and steps used for queries that involve aggregate functions and GROUP BY operations. </td></tr>
  <tr><td>Aggregate </td><td>aggr </td><td>Operator/step for scalar aggregate functions. </td></tr>
  <tr><td>HashAggregate </td><td>aggr </td><td>Operator/step for grouped aggregate functions. Can operate from disk by virtue of hash table spilling to disk. </td></tr>
  <tr><td>GroupAggregate </td><td>aggr </td><td>Operator sometimes chosen for grouped aggregate queries if the Amazon Redshift configuration setting for force_hash_grouping setting is off. </td></tr>
  <tr><td colspan="3"><b>SORT:</b> Operators and steps used when queries have to sort or merge result sets. </td></tr>
  <tr><td>Sort </td><td>sort </td><td>Sort performs the sorting specified by the ORDER BY clause as well as other operations such as UNIONs and joins. Can operate from disk. </td></tr>
  <tr><td>Merge </td><td>merge </td><td>Produces final sorted results of a query based on intermediate sorted results derived from operations performed in parallel. </td></tr>
  <tr><td colspan="3"><b>EXCEPT, INTERSECT, and UNION operations:</b> </td></tr>
  <tr><td>SetOp Except [Distinct] </td><td>hjoin </td><td>Used for EXCEPT queries. Can operate from disk based on virtue of fact that input hash can be disk-based. </td></tr>
  <tr><td>Hash Intersect [Distinct] </td><td>hjoin </td><td>Used for INTERSECT queries. Can operate from disk based on virtue of fact that input hash can be disk-based. </td></tr>
  <tr><td>Append [All |Distinct] </td><td>save </td><td>Append used with Subquery Scan to implement UNION and UNION ALL queries. Can operate from disk based on virtue of "save". </td></tr>
  <tr><td colspan="3"><b>Miscellaneous/Other:</b> </td></tr>
  <tr><td>Hash </td><td>hash </td><td>Used for inner joins and left and right outer joins (provides input to a hash join). The Hash operator creates the hash table for the inner table of a join. (The inner table is the table that is checked for matches and, in a join of two tables, is usually the smaller of the two.) </td></tr>
  <tr><td>Limit </td><td>limit </td><td>Evaluates the LIMIT clause. </td></tr>
  <tr><td>Materialize </td><td>save </td><td>Materialize rows for input to nested loop joins and some merge joins. Can operate from disk. </td></tr>
  <tr><td>-- </td><td>parse </td><td>Used to parse textual input data during a load. </td></tr>
  <tr><td>-- </td><td>project </td><td>Used to rearrange columns and compute expressions, that is, project data. </td></tr>
  <tr><td>Result </td><td>-- </td><td>Run scalar functions that don't involve any table access. </td></tr>
  <tr><td>-- </td><td>return </td><td>Return rows to the leader or client. </td></tr>
  <tr><td>Subplan </td><td>-- </td><td>Used for certain subqueries. </td></tr>
  <tr><td>Unique </td><td>unique </td><td>Eliminates duplicates from SELECT DISTINCT and UNION queries. </td></tr>
  <tr><td>Window </td><td>window </td><td>Compute aggregate and ranking window functions. Can operate from disk. </td></tr>
  <tr><td colspan="3"><b>Network Operations:</b> </td></tr>
  <tr><td>Network (Broadcast) </td><td>bcast </td><td>Broadcast is also an attribute of Join Explain operators and steps. </td></tr>
  <tr><td>Network (Distribute) </td><td>dist </td><td>Distribute rows to compute nodes for parallel processing by data warehouse cluster. </td></tr>
  <tr><td>Network (Send to Leader) </td><td>return </td><td>Sends results back to the leader for further processing. </td></tr>
  <tr><td colspan="3"><b>DML Operations (operators that modify data):</b> </td></tr>
  <tr><td>Insert (using Result) </td><td>insert </td><td>Inserts data. </td></tr>
  <tr><td>Delete (Scan + Filter) </td><td>delete </td><td>Deletes data. Can operate from disk. </td></tr>
  <tr><td>Update (Scan + Filter) </td><td>delete, insert </td><td>Implemented as delete and Insert. </td></tr>
</tbody>
</table>


## Using EXPLAIN for RLS
<a name="r_EXPLAIN-RLS"></a>

If a query contains a table that is subject to row-level security (RLS) policies, EXPLAIN displays a special RLS SecureScan node. Amazon Redshift also logs the same node type to the STL\_EXPLAIN system table. EXPLAIN doesn't reveal the RLS predicate that applies to dim\_tbl. The RLS SecureScan node type serves as an indicator that the execution plan contains additional operations that are invisible to the current user.

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

To enable full investigation of query plans that are subject to RLS, Amazon Redshift offers the EXPLAIN RLS system permissions. Users that have been granted this permission can inspect complete query plans that also include RLS predicates. 

The following example illustrates an additional Seq Scan below the RLS SecureScan node also includes the RLS policy predicate (k\_dim > 1).

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

While the EXPLAIN RLS permission is granted to a user, Amazon Redshift logs the full query plan including RLS predicates in the STL\_EXPLAIN system table. Queries that are run while this permission is not granted will be logged without RLS internals. Granting or removing the EXPLAIN RLS permission won't change what Amazon Redshift has logged to STL\_EXPLAIN for previous queries.

### AWS Lake Formation-RLS protected Redshift relations
<a name="r_EXPLAIN_RLS-LF"></a>

The following example illustrates an LF SecureScan node, which you can use to view Lake Formation-RLS relations.

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
<a name="r_EXPLAIN-examples"></a>

**Note**  
For these examples, the sample output might vary depending on Amazon Redshift configuration.

The following example returns the query plan for a query that selects the EVENTID, EVENTNAME, VENUEID, and VENUENAME from the EVENT and VENUE tables:

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

The following example returns the query plan for the same query with verbose output:

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