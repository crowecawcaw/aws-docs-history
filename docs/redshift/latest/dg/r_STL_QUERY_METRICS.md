Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_QUERY_METRICS

Contains metrics information, such as the number of rows processed, CPU usage,
input/output, and disk use, for queries that have completed running in user-defined
query queues (service classes). To view metrics for active queries that are currently
running, see the [STV_QUERY_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md") system view.

Query metrics are sampled at one second intervals. As a result, different runs of the
same query might return slightly different times. Also, query segments that run in less
than one second might not be recorded.

STL_QUERY_METRICS tracks and aggregates metrics at the query, segment, and step level.
For information about query segments and steps, see [Query planning and execution workflow](c-query-planning.md "c-query-planning.md"). Many metrics (such as `max_rows`,
`cpu_time`, and so on) are summed across node slices. For more
information about node slices, see [Data warehouse system
architecture](c_high_level_system_architecture.md "c_high_level_system_architecture.md").

To determine the level at which the row reports metrics, examine the
`segment` and `step_type` columns.

- If both `segment` and `step_type` are `-1`,
  then the row reports metrics at the query level.
- If `segment` is not `-1` and `step_type` is
  `-1`, then the row reports metrics at the segment level.
- If both `segment` and `step_type` are not
  `-1`, then the row reports metrics at the step level.
  The [SVL_QUERY_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md") view and
  the [SVL_QUERY_METRICS_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md") view aggregate the data in this view
  and present the information in a more accessible form.

STL_QUERY_METRICS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name         | Data type     | Description                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| userid              | integer       | ID of the user that ran the query that generated<br>the entry.                                                                                                                                                                                                                                                                             |
| service_class       | integer       | ID for the service class. Query<br>queues are defined in the WLM configuration. Metrics are reported<br>only for user-defined queues.                                                                                                                                                                                                      |
| query               | integer       | Query ID. The query column can be used to join<br>other system tables and views.                                                                                                                                                                                                                                                           |
| segment             | integer       | Segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps. Query<br>segments can run in parallel. Each segment runs in a single process.<br>If the segment value is -1, metrics segment values are rolled up to<br>the query level.                                                         |
| step_type           | integer       | Type of step that ran. For a description of<br>step types, see [Step types](r_STV_QUERY_METRICS.md#r_STV_QUERY_METRICS-step-type "r_STV_QUERY_METRICS.md#r_STV_QUERY_METRICS-step-type").                                                                                                                                                  |
| starttime           | timestamp     | Time in UTC that the query started executing, with<br>6 digits of precision for fractional seconds. For example:<br>`2009-06-12 11:29:19.131358`.                                                                                                                                                                                          |
| slices              | integer       | Number of slices for the cluster.                                                                                                                                                                                                                                                                                                          |
| max_rows            | bigint        | Maximum number of rows output for a step,<br>aggregated across all slices.                                                                                                                                                                                                                                                                 |
| rows                | bigint        | Number of rows processed by a step.                                                                                                                                                                                                                                                                                                        |
| max_cpu_time        | bigint        | Maximum CPU time used, in microseconds. At the<br>segment level, the maximum CPU time used by the segment across all<br>slices. At the query level, the maximum CPU time used by any query<br>segment.                                                                                                                                     |
| cpu_time            | bigint        | CPU time used, in microseconds. At the segment<br>level, the total CPU time for the segment across all slices. At the<br>query level, the sum of CPU time for the query across all slices and<br>segments.                                                                                                                                 |
| max_blocks_read     | integer       | Maximum number of 1 MB blocks read by the segment,<br>aggregated across all slices. At the segment level, the maximum<br>number of 1 MB blocks read for the segment across all slices. At the<br>query level, the maximum number of 1 MB blocks read by any query<br>segment.                                                              |
| blocks_read         | bigint        | Number of 1 MB blocks read by the query or<br>segment.                                                                                                                                                                                                                                                                                     |
| max_run_time        | bigint        | The maximum elapsed time for a segment, in<br>microseconds. At the segment level, the maximum run time for the<br>segment across all slices. At the query level, the maximum run time<br>for any query segment.                                                                                                                            |
| run_time            | bigint        | Total run time, summed across slices. Run time doesn't include<br>wait time.<br>At the segment level, the run time for the segment, summed<br>across all slices. At the query level, the run time for the<br>query summed across all slices and segments. Because this value<br>is a sum, run time is not related to query execution time. |
| max_blocks_to_disk  | bigint        | The maximum amount of disk space used to write<br>intermediate results, in MB blocks. At the segment level, the<br>maximum amount of disk space used by the segment across all slices.<br>At the query level, the maximum amount of disk space used by any<br>query segment.                                                               |
| blocks_to_disk      | bigint        | The amount of disk space used by a query or<br>segment to write intermediate results, in MB blocks.                                                                                                                                                                                                                                        |
| step                | integer       | Query step that ran.                                                                                                                                                                                                                                                                                                                       |
| max_query_scan_size | bigint        | The maximum size of data scanned by a query, in<br>MB. At the segment level, the maximum size of data scanned by the<br>segment across all slices. At the query level, the maximum size of<br>data scanned by any query segment.                                                                                                           |
| query_scan_size     | bigint        | The size of data scanned by a query, in MB.                                                                                                                                                                                                                                                                                                |
| query_priority      | integer       | The priority of the query. Possible values are<br>`-1`, `0`, `1`, `2`,<br>`3`, and `4`, where `-1` means<br>that query priority isn't supported.                                                                                                                                                                                           |
| query_queue_time    | bigint        | The amount of time in microseconds that the query was queued.                                                                                                                                                                                                                                                                              |
| service_class_name  | character(64) | The name of the service class.                                                                                                                                                                                                                                                                                                             |

## Sample query

To find queries with high CPU time (more the 1,000 seconds), run the following
query.

```
Select query, cpu_time / 1000000 as cpu_seconds
from stl_query_metrics where segment = -1 and cpu_time > 1000000000
order by cpu_time;

query | cpu_seconds
------+------------
25775 |        9540
```

To find active queries with a nested loop join that returned more than one million
rows, run the following query.

```
select query, rows
from stl_query_metrics
where step_type = 15 and rows > 1000000
order by rows;

query | rows
------+-----------
25775 | 2621562702
```

To find active queries that have run for more than 60 seconds and have used less
than 10 seconds of CPU time, run the following query.

```
select query, run_time/1000000 as run_time_seconds
from stl_query_metrics
where segment = -1 and run_time > 60000000 and cpu_time < 10000000;

query | run_time_seconds
------+-----------------
25775 |              114
```
