

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Reviewing query alerts
<a name="c-reviewing-query-alerts"></a>

To use the [STL\_ALERT\_EVENT\_LOG](r_STL_ALERT_EVENT_LOG.md) system table to identify and correct potential performance issues with your query, follow these steps:

1. Run the following to determine your query ID:

   ```
   select query, elapsed, substring
   from svl_qlog
   order by query
   desc limit 5;
   ```

   Examine the truncated query text in the `substring` field to determine which `query` value to select. If you have run the query more than once, use the `query` value from the row with the lower `elapsed` value. That is the row for the compiled version. If you have been running many queries, you can raise the value used by the LIMIT clause used to make sure that your query is included.

1. Select rows from STL\_ALERT\_EVENT\_LOG for your query:

   ```
   Select * from stl_alert_event_log where query = MyQueryID;               
   ```  
![A sample query result from STL_ALERT_EVENT_LOG.](https://docs.aws.amazon.com/redshift/latest/dg/images/stl_alert_event_log_results.png)

1. Evaluate the results for your query. Use the following table to locate potential solutions for any issues that you have identified.
**Note**  
Not all queries have rows in STL\_ALERT\_EVENT\_LOG, only those with identified issues.


<table>
<thead>
  <tr><th>Issue</th><th>Event value</th><th>Solution value</th><th>Recommended solution</th></tr>
</thead>
<tbody>
  <tr><td>Statistics for the tables in the query are missing or out of date.</td><td>Missing query planner statistics</td><td>Run the ANALYZE command </td><td>See <a href="query-performance-improvement-opportunities.md#table-statistics-missing-or-out-of-date">Table statistics missing or out of date</a>.</td></tr>
  <tr><td>There is a nested loop join (the least optimal join) in the query plan.</td><td>Nested Loop Join in the query plan</td><td>Review the join predicates to avoid Cartesian products </td><td>See <a href="query-performance-improvement-opportunities.md#nested-loop">Nested loop</a>.</td></tr>
  <tr><td>The scan skipped a relatively large number of rows that are marked as deleted but not vacuumed, or rows that have been inserted but not committed. </td><td>Scanned a large number of deleted rows</td><td>Run the VACUUM command to reclaim deleted space </td><td> See <a href="query-performance-improvement-opportunities.md#ghost-rows-or-uncommitted-rows">Ghost rows or uncommitted rows</a>. </td></tr>
  <tr><td>More than 1,000,000 rows were redistributed for a hash join or aggregation. </td><td>Distributed a large number of rows across the network:RowCount rows were distributed in order to process the aggregation</td><td>Review the choice of distribution key to collocate the join or aggregation </td><td> See <a href="query-performance-improvement-opportunities.md#suboptimal-data-distribution">Suboptimal data distribution</a>. </td></tr>
  <tr><td>More than 1,000,000 rows were broadcast for a hash join. </td><td>Broadcasted a large number of rows across the network</td><td>Review the choice of distribution key to collocate the join and consider using distributed tables </td><td> See <a href="query-performance-improvement-opportunities.md#suboptimal-data-distribution">Suboptimal data distribution</a>. </td></tr>
  <tr><td>A DS_DIST_ALL_INNER redistribution style was indicated in the query plan, which forces serial execution because the entire inner table was redistributed to a single node.</td><td>DS_DIST_ALL_INNER for Hash Join in the query plan</td><td>Review the choice of distribution strategy to distribute the inner, rather than outer, table </td><td> See <a href="query-performance-improvement-opportunities.md#suboptimal-data-distribution">Suboptimal data distribution</a>. </td></tr>
</tbody>
</table>
