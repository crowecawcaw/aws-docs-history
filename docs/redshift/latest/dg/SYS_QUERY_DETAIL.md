Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_QUERY_DETAIL

Use SYS_QUERY_DETAIL to view details for queries at various metric levels, with each
row representing details about a particular WLM query at a given metric level. This view contains many types of
queries such as DDL, DML, and utility commands (for example, copy and unload). Some
columns might not be relevant depending on the query type. For example,
external_scanned_bytes is not relevant to internal tables.

SYS_QUERY_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

To verify whether a transaction containing the executed query was successfully
committed, you need to perform a join operation between system tables and the
`sys_transaction_history` table. For example:

```
SELECT
    th.transaction_id,
    qd.query_id,
    th.status AS transaction_status
FROM
    sys_query_detail qd
LEFT JOIN sys_query_history qh ON qd.query_id = qh.query_id
LEFT JOIN sys_transaction_history th on qh.transaction_id = th.transaction_id;
```

## Table columns

| Column name               | Data type      | Description                                                                                                                                                                                                                                                        |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| user_id                   | integer        | The identifier of the user who submitted the<br>query.                                                                                                                                                                                                             |
| query_id                  | bigint         | The query identifier.                                                                                                                                                                                                                                              |
| child_query_sequence      | integer        | The sequence of the rewritten user query, starting<br>with 1.                                                                                                                                                                                                      |
| stream_id                 | integer        | The stream identifier of the query stream.                                                                                                                                                                                                                         |
| segment_id                | integer        | The segment identifier of the query running<br>segment.                                                                                                                                                                                                            |
| step_id                   | integer        | The step identifier in a segment.                                                                                                                                                                                                                                  |
| step_name                 | text           | The step name in a segment. Possible values are<br>`aggregate`, `broadcast`,<br>`delete`, `distribute`, `hash`,<br>`hashjoin`, `insert`, `limit`,<br>`merge`, `nestloop`, `parse`,<br>`return`, `save`, `scan`,<br>`sort`, `sortlimit`, `unique`,<br>and `window`. |
| table_id                  | integer        | The table identifier for permanent table<br>scans.                                                                                                                                                                                                                 |
| table_name                | character(136) | The table name of the step that is being<br>operated.                                                                                                                                                                                                              |
| is_rrscan                 | character      | A value that indicates whether a step is a scan<br>step. True (t) indicates that a range-restricted scan was<br>used.                                                                                                                                              |
| start_time                | timestamp      | The time when the query step began.<br>This field is recorded at the segment level,<br>regardless of the value in the `metrics_level` column.                                                                                                                      |
| end_time                  | timestamp      | The time when the query step completed.<br>This field is recorded at the segment level,<br>regardless of the value in the `metrics_level` column.                                                                                                                  |
| duration                  | bigint         | The amount of time (microseconds) spent on the<br>step. This field is recorded at the segment level,<br>regardless of the value in the `metrics_level` column.                                                                                                     |
| alert                     | text           | The description of the alert event.                                                                                                                                                                                                                                |
| input_bytes               | bigint         | The input bytes for the current step.                                                                                                                                                                                                                              |
| input_rows                | bigint         | The input rows for the current step.                                                                                                                                                                                                                               |
| output_bytes              | bigint         | The output bytes for the current step.                                                                                                                                                                                                                             |
| output_rows               | bigint         | The output rows for the current step.                                                                                                                                                                                                                              |
| blocks_read               | bigint         | The number of blocks the step read.                                                                                                                                                                                                                                |
| blocks_write              | bigint         | The number of blocks the step wrote.                                                                                                                                                                                                                               |
| local_read_IO             | bigint         | The number of blocks read from local disk<br>cache.                                                                                                                                                                                                                |
| remote_read_IO            | bigint         | The number of blocks read from remote.                                                                                                                                                                                                                             |
| source                    | text           | The type of database object that was scanned. This<br>column only has a value when the row's<br>\*step_name<br>• value is<br>`scan`.                                                                                                                               |
| data_skewness             | integer        | The skewness of output rows distribution among all<br>steps. It is a number in the range of 0% to 100%. The larger the<br>number, the more unbalanced is the distribution.                                                                                         |
| time_skewness             | integer        | The skewness of execution time distribution among<br>all steps. It is a number in the range of 0% to 100%. The larger the<br>number, the more unbalanced is the distribution.                                                                                      |
| is_active                 | character      | The state of the query at the step level. Possible<br>values are ‘t’ that shows the step is actively running or ‘f’ that<br>indicates the step completes running.                                                                                                  |
| spilled_block_local_disk  | bigint         | The number of blocks spilled to local<br>disk.                                                                                                                                                                                                                     |
| spilled_block_remote_disk | bigint         | The number of blocks spilled to Amazon Simple Storage Service.                                                                                                                                                                                                     |
| step_attribute            | character(64)  | Contains information about the associated step.<br>Possible values for scan steps:<br>`multi-dimensional`.                                                                                                                                                         |
| metrics_level             | character(64)  | The metric level of the query. Possible values are as follows:<br>• Child query<br>• Stream<br>• Segment<br>• Step                                                                                                                                                 |
| plan_parent_id            | integer        | The identifier of the plan node's parent node.<br>A parent node can have multiple child nodes. For example,<br>a merge join is the parent node of the scans on the joined tables.                                                                                  |
| plan_node_id              | integer        | The identifier of a plan node<br>that maps to one or more steps in the query.                                                                                                                                                                                      |

## Usage notes

SYS_QUERY_DETAIL can contain metrics at the step, steam, segment, and child query level.
In addition to referencing the metrics_level column, you can see which metric level a given
row is showing by referencing the step_id, segment_id, and stream_id fields according to
the following table.

| Metric level | stream_id value    | segment_id value   | step_id value      |
| ------------ | ------------------ | ------------------ | ------------------ |
| child query  | -1                 | -1                 | -1                 |
| stream       | A valid step value | -1                 | -1                 |
| segment      | A valid step value | A valid step value | -1                 |
| step         | A valid step value | A valid step value | A valid step value |

## Sample queries

The following example returns the output of SYS_QUERY_DETAIL.

The following query shows the query metadata detail at step level, including step
name, input_bytes, output_bytes, input_rows, output_rows.

```
SELECT query_id,
       child_query_sequence,
       stream_id,
       segment_id,
       step_id,
       trim(step_name) AS step_name,
       duration,
       input_bytes,
       output_bytes,
       input_rows,
       output_rows
FROM sys_query_detail
WHERE query_id IN (193929)
ORDER BY query_id,
         stream_id,
         segment_id,
         step_id DESC;
```

Sample output.

```
 query_id | child_query_sequence | stream_id | segment_id | step_id | step_name  |    duration     | input_bytes | output_bytes | input_rows | output_rows
----------+----------------------+-----------+------------+---------+------------+-----------------+-------------+--------------+------------+-------------
   193929 |                    2 |         0 |          0 |       3 | hash       |           37144 |           0 |      9350272 |          0 |      292196
   193929 |                    5 |         0 |          0 |       3 | hash       |            9492 |           0 |        23360 |          0 |        1460
   193929 |                    1 |         0 |          0 |       3 | hash       |           46809 |           0 |      9350272 |          0 |      292196
   193929 |                    4 |         0 |          0 |       2 | return     |            7685 |           0 |          896 |          0 |         112
   193929 |                    1 |         0 |          0 |       2 | project    |           46809 |           0 |            0 |          0 |      292196
   193929 |                    2 |         0 |          0 |       2 | project    |           37144 |           0 |            0 |          0 |      292196
   193929 |                    5 |         0 |          0 |       2 | project    |            9492 |           0 |            0 |          0 |        1460
   193929 |                    3 |         0 |          0 |       2 | return     |           11033 |           0 |        14336 |          0 |         112
   193929 |                    2 |         0 |          0 |       1 | project    |           37144 |           0 |            0 |          0 |      292196
   193929 |                    1 |         0 |          0 |       1 | project    |           46809 |           0 |            0 |          0 |      292196
   193929 |                    5 |         0 |          0 |       1 | project    |            9492 |           0 |            0 |          0 |        1460
   193929 |                    3 |         0 |          0 |       1 | aggregate  |           11033 |           0 |       201488 |          0 |          14
   193929 |                    4 |         0 |          0 |       1 | aggregate  |            7685 |           0 |        28784 |          0 |          14
   193929 |                    5 |         0 |          0 |       0 | scan       |            9492 |           0 |        23360 |     292196 |        1460
   193929 |                    4 |         0 |          0 |       0 | scan       |            7685 |           0 |         1344 |        112 |         112
   193929 |                    2 |         0 |          0 |       0 | scan       |           37144 |           0 |      7304900 |     292196 |      292196
   193929 |                    3 |         0 |          0 |       0 | scan       |           11033 |           0 |        13440 |        112 |         112
   193929 |                    1 |         0 |          0 |       0 | scan       |           46809 |           0 |      7304900 |     292196 |      292196
   193929 |                    5 |         0 |          0 |      -1 |            |            9492 |       12288 |            0 |          0 |           0
   193929 |                    1 |         0 |          0 |      -1 |            |           46809 |       16384 |            0 |          0 |           0
   193929 |                    2 |         0 |          0 |      -1 |            |           37144 |       16384 |            0 |          0 |           0
   193929 |                    4 |         0 |          0 |      -1 |            |            7685 |       28672 |            0 |          0 |           0
   193929 |                    3 |         0 |          0 |      -1 |            |           11033 |      114688 |            0 |          0 |           0
```

To view the tables in your database in order from most used to least used, use the
following example. Replace `sample_data_dev` with your own
database. Note that this query will count queries starting when your cluster is
created, but your system view data is not saved when your data warehouse is lacking
space.

```
`SELECT table_name, COUNT (DISTINCT query_id)
FROM SYS_QUERY_DETAIL
WHERE table_name LIKE 'sample_data_dev%'
GROUP BY table_name
ORDER BY COUNT(*) DESC;`

`+---------------------------------+-------+
| table_name | count |
+---------------------------------+-------+
| sample_data_dev.tickit.venue | 4 |
| sample_data_dev.myunload1.venue | 3 |
| sample_data_dev.tickit.listing | 1 |
| sample_data_dev.tickit.category | 1 |
| sample_data_dev.tickit.users | 1 |
| sample_data_dev.tickit.date | 1 |
| sample_data_dev.tickit.sales | 1 |
| sample_data_dev.tickit.event | 1 |
+---------------------------------+-------+`
```

The following example shows the various metric levels for a single WLM query.

```
SELECT query_id, child_query_sequence, stream_id, segment_id, step_id, step_name, start_time, end_time, metrics_level
FROM sys_query_detail
WHERE query_id = 1553 AND step_id = -1
ORDER BY stream_id, segment_id, step_id;

 query_id | child_query_sequence | stream_id | segment_id | step_id | step_name |         start_time         |          end_time          | metrics_level
----------+----------------------+-----------+------------+---------+-----------+----------------------------+----------------------------+---------------
     1553 |                    1 |        -1 |         -1 |      -1 |           | 2024-10-17 02:28:49.814721 | 2024-10-17 02:28:49.847838 | child query
     1553 |                    1 |         0 |         -1 |      -1 |           | 2024-10-17 02:28:49.814721 | 2024-10-17 02:28:49.835609 | stream
     1553 |                    1 |         0 |          0 |      -1 |           | 2024-10-17 02:28:49.824677 | 2024-10-17 02:28:49.830372 | segment
     1553 |                    1 |         1 |         -1 |      -1 |           | 2024-10-17 02:28:49.835624 | 2024-10-17 02:28:49.845773 | stream
     1553 |                    1 |         1 |          1 |      -1 |           | 2024-10-17 02:28:49.84088  | 2024-10-17 02:28:49.842388 | segment
     1553 |                    1 |         1 |          2 |      -1 |           | 2024-10-17 02:28:49.835926 | 2024-10-17 02:28:49.844396 | segment
     1553 |                    1 |         2 |         -1 |      -1 |           | 2024-10-17 02:28:49.846949 | 2024-10-17 02:28:49.847838 | stream
     1553 |                    1 |         2 |          3 |      -1 |           | 2024-10-17 02:28:49.847013 | 2024-10-17 02:28:49.847485 | segment
(8 rows)
```
