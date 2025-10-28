Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query performance improvement

Following are some common issues that affect Amazon Redshift query performance, with instructions on
ways to diagnose and resolve them.

###### Topics

- [Table statistics missing or out of
  date](#table-statistics-missing-or-out-of-date "#table-statistics-missing-or-out-of-date")
- [Nested loop](#nested-loop "#nested-loop")
- [Hash join](#hash-join "#hash-join")
- [Ghost rows or uncommitted rows](#ghost-rows-or-uncommitted-rows "#ghost-rows-or-uncommitted-rows")
- [Unsorted or missorted rows](#unsorted-or-mis-sorted-rows "#unsorted-or-mis-sorted-rows")
- [Suboptimal data distribution](#suboptimal-data-distribution "#suboptimal-data-distribution")
- [Insufficient memory allocated to the
  query](#insufficient-memory-allocated-to-the-query "#insufficient-memory-allocated-to-the-query")
- [Suboptimal WHERE clause](#suboptimal-WHERE-clause "#suboptimal-WHERE-clause")
- [Insufficiently restrictive predicate](#insufficiently-restrictive-predicate "#insufficiently-restrictive-predicate")
- [Very large result set](#very-large-result-set "#very-large-result-set")
- [Large SELECT list](#large-SELECT-list "#large-SELECT-list")

## Table statistics missing or out of

date

If table statistics are missing or out of date, you might see the
following:

- A warning message in EXPLAIN command results.
- A missing statistics alert event in STL_ALERT_EVENT_LOG. For more
  information, see [Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md").

To fix this issue, run [ANALYZE](r_ANALYZE.md "r_ANALYZE.md").

## Nested loop

If a nested loop is present, you might see a nested loop alert event in
STL_ALERT_EVENT_LOG. You can also identify this type of event by running the query at
[Identifying queries with nested loops](identify-queries-with-nested-loops.md "identify-queries-with-nested-loops.md"). For more information, see
[Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md").

To fix this, review your query for cross-joins and remove them if possible.
Cross-joins are joins without a join condition that result in the Cartesian product
of two tables. They are typically run as nested loop joins, which are the
slowest of the possible join types.

## Hash join

If a hash join is present, you might see the following:

- Hash and hash join operations in the query plan. For more information, see
  [Analyzing the query plan](c-analyzing-the-query-plan.md "c-analyzing-the-query-plan.md").
- An HJOIN step in the segment with the highest maxtime value in
  SVL_QUERY_SUMMARY. For more information, see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

To fix this issue, you can take a couple of approaches:

- Rewrite the query to use a merge join if possible. You can do this by
  specifying join columns that are both distribution keys and sort keys.
- If the HJOIN step in SVL_QUERY_SUMMARY has a very high value in the rows
  field compared to the rows value in the final RETURN step in the query, check
  whether you can rewrite the query to join on a unique column. When a query does
  not join on a unique column, such as a primary key, that increases the number
  of rows involved in the join.

## Ghost rows or uncommitted rows

If ghost rows or uncommitted rows are present, you might see an alert event in
STL_ALERT_EVENT_LOG that indicates excessive ghost rows. For more information, see
[Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md").

To fix this issue, you can take a couple of approaches:

- Check the **Loads** tab of your Amazon Redshift console for active
  load operations on any of the query tables. If you see active load operations,
  wait for those to complete before taking action.
- If there are no active load operations, run [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md") on the query tables to remove deleted
  rows.

## Unsorted or missorted rows

If unsorted or missorted rows are present, you might see a very selective filter
alert event in STL_ALERT_EVENT_LOG. For more information, see [Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md").

You can also check to see if any of the tables in your query have large unsorted
areas by running the query in [Identifying tables with data skew
or unsorted rows](identify-tables-with-data-skew-or-unsorted-rows.md "identify-tables-with-data-skew-or-unsorted-rows.md").

To fix this issue, you can take a couple of approaches:

- Run [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md") on
  the query tables to re-sort the rows.
- Review the sort keys on the query tables to see if any improvements can be
  made. Remember to weigh the performance of this query against the performance
  of other important queries and the system overall before making any changes.
  For more information, see [Sort keys](t_Sorting_data.md "t_Sorting_data.md").

## Suboptimal data distribution

If data distribution is suboptimal, you might see the following:

- A serial execution, large broadcast, or large distribution alert event
  appears in STL_ALERT_EVENT_LOG. For more information, see [Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md").
- Slices are not processing approximately the same number of rows for a given
  step. For more information, see [Using the SVL_QUERY_REPORT view](using-SVL-Query-Report.md "using-SVL-Query-Report.md").
- Slices are not taking approximately the same amount of time for a given
  step. For more information, see [Using the SVL_QUERY_REPORT view](using-SVL-Query-Report.md "using-SVL-Query-Report.md").

If none of the preceding is true, you can also see if any of the tables in your
query have data skew by running the query in [Identifying tables with data skew
or unsorted rows](identify-tables-with-data-skew-or-unsorted-rows.md "identify-tables-with-data-skew-or-unsorted-rows.md").

To fix this issue, review the distribution styles for the tables in the query and see if any improvements can
be made. Remember to weigh the performance of this query against the performance of
other important queries and the system overall before making any changes. For more
information, see [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md").

## Insufficient memory allocated to the

query

If insufficient memory is allocated to your query, you might see a step in
SVL_QUERY_SUMMARY that has an `is_diskbased` value of true. For more
information, see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

To fix this issue, allocate more memory to the query by temporarily increasing the
number of query slots it uses. Workload Management (WLM) reserves slots in a query
queue equivalent to the concurrency level set for the queue. For example, a queue
with a concurrency level of 5 has 5 slots. Memory assigned to the queue is allocated
equally to each slot. Assigning several slots to one query gives that query access to
the memory for all of those slots. For more information on how to temporarily
increase the slots for a query, see [wlm_query_slot_count](r_wlm_query_slot_count.md "r_wlm_query_slot_count.md").

## Suboptimal WHERE clause

If your WHERE clause causes excessive table scans, you might see a SCAN step in
the segment with the highest `maxtime` value in SVL_QUERY_SUMMARY. For
more information, see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

To fix this issue, add a WHERE clause to the query based on the primary sort
column of the largest table. This approach helps minimize scanning time. For more
information, see [Amazon Redshift best practices for designing
tables](c_designing-tables-best-practices.md "c_designing-tables-best-practices.md").

## Insufficiently restrictive predicate

If your query has an insufficiently restrictive predicate, you might see a SCAN
step in the segment with the highest `maxtime` value in SVL_QUERY_SUMMARY
that has a very high `rows` value compared to the `rows` value
in the final RETURN step in the query. For more information, see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

To fix this issue, try adding a predicate to the query or making the existing
predicate more restrictive to narrow the output.

## Very large result set

If your query returns a very large result set, consider rewriting the query to use
[UNLOAD](r_UNLOAD.md "r_UNLOAD.md") to write the results to Amazon S3.
This approach improves the performance of the RETURN step by taking advantage of
parallel processing. For more information on checking for a very large result set,
see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

## Large SELECT list

If your query has an unusually large SELECT list, you might see a
`bytes` value that is high relative to the `rows` value for
any step (in comparison to other steps) in SVL_QUERY_SUMMARY. This high
`bytes` value can be an indicator that you are selecting a lot of
columns. For more information, see [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md").

To fix this issue, review the columns you are selecting and see if any can be
removed.
