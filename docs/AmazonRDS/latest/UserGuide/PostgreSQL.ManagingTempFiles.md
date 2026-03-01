# Viewing temporary file usage with Performance Insights

You can use Performance Insights to view temporary file usage by turning on the metrics
**temp_bytes** and **temp_files**. The view in
Performance Insights doesn't show the specific queries that generate temporary files, however, when
you combine Performance Insights with the query shown for `pg_ls_tmpdir`, you can
troubleshoot, analyze, and determine the changes in your query workload.

1. In the Performance Insights dashboard, choose **Manage
   Metrics**.
2. Choose **Database metrics**, and select the
   **temp_bytes** and **temp_files** metrics
   as shown in the following image.

![Metrics displayed in the graph.](images/rpg_mantempfiles_metrics.png) 3. In the **Top SQL** tab, choose the
**Preferences** icon. 4. In the **Preferences** window, turn on the following
statistics to appear in the **Top SQL**tab and choose
**Continue**.

    * Temp writes/sec
    * Temp reads/sec
    * Tmp blk write/call
    * Tmp blk read/call

5. The temporary file is broken out when combined with the query shown for
   `pg_ls_tmpdir`, as shown in the following example.

![Query that displays the temporary file usage.](images/rpg_mantempfiles_query.png)
The `IO:BufFileRead` and `IO:BufFileWrite` events occur when the
top queries in your workload often create temporary files. You can use Performance
Insights to identify top queries waiting on `IO:BufFileRead` and
`IO:BufFileWrite` by reviewing Average Active Session (AAS) in Database
Load and Top SQL sections.

![IO:BufFileRead and IO:BufFileWrite in the graph.](images/perfinsights_IOBufFile.png)
For more information on how to analyze top queries and load by wait event with
Performance Insights, see [Overview of the Top SQL tab](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md#USER_PerfInsights.UsingDashboard.Components.AvgActiveSessions.TopLoadItemsTable.TopSQL "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md#USER_PerfInsights.UsingDashboard.Components.AvgActiveSessions.TopLoadItemsTable.TopSQL"). You should identify and tune the queries that cause increase in temporary file usage
and related wait events. For more information on these wait events and remediation, see
[IO:BufFileRead and
IO:BufFileWrite](wait-event.md "wait-event.md").

###### Note

The [`work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM") parameter controls when the sort operation
runs out of memory and results are written into temporary files. We recommend that
you don't change the setting of this parameter higher than the default value because
it would permit every database session to consume more memory. Also, a single
session that performs complex joins and sorts can perform parallel operations in
which each operation consumes memory.

As a best practice, when you have a large report with multiple joins and sorts,
set this parameter at the session level by using the `SET work_mem`
command. Then the change is only applied to the current session and doesn't
change the value globally.
