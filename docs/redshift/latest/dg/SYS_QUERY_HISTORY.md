Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_QUERY_HISTORY

Use SYS_QUERY_HISTORY to view details of user queries. Each row represents a user
query with accumulated statistics for some of the fields. This view contains many types
of queries, such as data definition language (DDL), data manipulation language (DML),
copy, unload, and Amazon Redshift Spectrum. It contains both running and finished queries.

SYS_QUERY_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

To verify whether a transaction containing the executed query was successfully
committed, you need to perform a join operation between system tables and the
`sys_transaction_history` table. For example:

```
SELECT
    qh.transaction_id,
    qh.query_id,
    qh.status AS query_status,
    qh.query_type,
    TRIM(qh.query_text) AS query_text,
    th.status AS transaction_status
FROM
    sys_query_history qh
LEFT JOIN
    sys_transaction_history th ON qh.transaction_id = th.transaction_id;
```

## Table columns

| Column name             | Data type       | Description                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id                 | integer         | The identifier of the user who submitted the<br>query.                                                                                                                                                                                                                                                                                                              |
| query_id                | bigint          | The query identifier.                                                                                                                                                                                                                                                                                                                                               |
| query_label             | character(320)  | The short name for the query.                                                                                                                                                                                                                                                                                                                                       |
| transaction_id          | bigint          | The transaction identifier.                                                                                                                                                                                                                                                                                                                                         |
| session_id              | integer         | The process identifier of the process running the<br>query.                                                                                                                                                                                                                                                                                                         |
| database_name           | character(128)  | The name of the database the user was connected to<br>when the query was issued.                                                                                                                                                                                                                                                                                    |
| query_type              | character(32)   | The type of query, such as, SELECT, INSERT,<br>UPDATE, UNLOAD, COPY, COMMAND, DDL, UTILITY, CTAS, and<br>OTHER.                                                                                                                                                                                                                                                     |
| status                  | character(10)   | The status of the query. Valid values: planning,<br>queued, running, returning, failed, canceled, and success.                                                                                                                                                                                                                                                      |
| result_cache_hit        | Boolean         | Indicates whether the query matches the result<br>cache.                                                                                                                                                                                                                                                                                                            |
| start_time              | timestamp       | The time when the query began.                                                                                                                                                                                                                                                                                                                                      |
| end_time                | timestamp       | The time when the query completed.                                                                                                                                                                                                                                                                                                                                  |
| elapsed_time            | bigint          | The total amount of time (microseconds) spent on<br>the query.                                                                                                                                                                                                                                                                                                      |
| queue_time              | bigint          | The total time (microseconds) spent on the service<br>class query queue.                                                                                                                                                                                                                                                                                            |
| execution_time          | bigint          | The total time (microseconds) running in the<br>service class.                                                                                                                                                                                                                                                                                                      |
| error_message           | character(512)  | The reason a query failed.                                                                                                                                                                                                                                                                                                                                          |
| returned_rows           | bigint          | The number of rows returned to the client.                                                                                                                                                                                                                                                                                                                          |
| returned_bytes          | bigint          | The number of bytes returned to the client.                                                                                                                                                                                                                                                                                                                         |
| query_text              | character(4000) | The query string. This string might be truncated.                                                                                                                                                                                                                                                                                                                   |
| redshift_version        | character(256)  | The Amazon Redshift version when the query ran.                                                                                                                                                                                                                                                                                                                     |
| usage_limit             | character(150)  | List of usage limit IDs reached by the<br>query.                                                                                                                                                                                                                                                                                                                    |
| compute_type            | varchar(32)     | Indicates whether the query runs on the main<br>cluster or concurrency scaling cluster. Possible values are<br>`primary` (query runs on the main cluster),<br>`secondary` (query runs on the secondary cluster), or<br>`primary-scale` (query runs on the concurrency<br>cluster). This is only applicable to provisioned cluster.                                  |
| compile_time            | bigint          | The total time (microseconds) spent on compilation<br>of the query.                                                                                                                                                                                                                                                                                                 |
| planning_time           | bigint          | The total time (microseconds) spent on planning of<br>the query.                                                                                                                                                                                                                                                                                                    |
| lock_wait_time          | bigint          | The total time (microseconds) spent on waiting for<br>relation lock.                                                                                                                                                                                                                                                                                                |
| service_class_id        | integer         | The service class's ID. For a list of<br>service class IDs, go to [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").<br>This column is only used for queries run on provisioned<br>clusters. For queries run on Redshift Serverless, this column contains<br>-1.       |
| service_class_name      | character(64)   | The service class name.<br>This column is only used for queries run on provisioned<br>clusters. For queries run on Amazon Redshift Redshift Serverless, this column<br>is empty.                                                                                                                                                                                    |
| query_priority          | character(20)   | The priority of the queue in which the query<br>ran. Possible values are as follows:<br>• NULL<br>• lowest<br>• low<br>• normal<br>• high<br>• highest<br>NULL means that query priority isn't supported for the<br>query.<br>This column is only used for queries run on provisioned<br>clusters. For queries run on Redshift Serverless, this column is<br>empty. |
| short_query_accelerated | character(10)   | Whether the query was accelerated using<br>short query acceleration (SQA). Possible values are as<br>follows:<br>• true<br>• false<br>• NULL<br>This column is only used for queries run on provisioned<br>clusters. For queries run on Redshift Serverless, this column is<br>empty.                                                                               |
| user_query_hash         | character(40)   | The query hash generated from the query,<br>including its query literals. Repeated queries with the same query<br>text will have the same user_query_hash values.                                                                                                                                                                                                   |
| generic_query_hash      | character(40)   | The query hash generated from the query,<br>excluding its query literals. Repeated queries with the same query<br>text, but different query literals, will have the same<br>generic_query_hash values.                                                                                                                                                              |
| query_hash_version      | integer         | The version number for the<br>query hash generated from the query.                                                                                                                                                                                                                                                                                                  |
| result_cache_query_id   | integer         | If the query used result caching,<br>this field value is the query ID of the query that was the<br>source of the cached results. If result caching was not used,<br>this field value is `0`.                                                                                                                                                                        |
| username                | character(128)  | The username of the user who submitted the query.                                                                                                                                                                                                                                                                                                                   |

## Sample queries

The following query returns running and queued queries.

```
SELECT user_id,
       query_id,
       transaction_id,
       session_id,
       status,
       trim(database_name) AS database_name,
       start_time,
       end_time,
       result_cache_hit,
       elapsed_time,
       queue_time,
       execution_time
FROM sys_query_history
WHERE status IN ('running','queued')
ORDER BY start_time;
```

Sample output.

```
 user_id | query_id | transaction_id | session_id | status  | database_name |        start_time         |          end_time          | result_cache_hit | elapsed_time | queue_time | execution_time
---------+----------+----------------+------------+---------+---------------+---------------------------+----------------------------+------------------+--------------+------------+----------------
     101 |   760705 |         852337 | 1073832321 | running | tpcds_1t      | 2022-02-15 19:03:19.67849 | 2022-02-15 19:03:19.739811 | f                |        61321 |          0 |              0
```

The following query returns the query start time, end time, queue time, elapsed
time, planning time, and other metadata for a specific query.

```
SELECT user_id,
       query_id,
       transaction_id,
       session_id,
       status,
       trim(database_name) AS database_name,
       start_time,
       end_time,
       result_cache_hit,
       elapsed_time,
       queue_time,
       execution_time,
       planning_time,
       trim(query_text) as query_text
FROM sys_query_history
WHERE query_id = 3093;
```

Sample output.

```
user_id | query_id | transaction_id | session_id |   status   | database_name |         start_time         |          end_time          | result_cache_hit | elapsed_time | queue_time | execution_time | planning_time | query_text
--------+----------+----------------+------------+------------+---------------+----------------------------+----------------------------+------------------+--------------+------------+----------------+---------------+-------------------------------------
    106 |     3093 |          11759 | 1073750146 | success    | dev           | 2023-03-16 16:53:17.840214 | 2023-03-16 16:53:18.106588 | f                |       266374 |          0 |         105725 |        136589 | select count(*) from item;
```

The following query lists the 10 most recent SELECT queries.

```
SELECT query_id,
       transaction_id,
       session_id,
       start_time,
       elapsed_time,
       queue_time,
       execution_time,
       returned_rows,
       returned_bytes
FROM sys_query_history
WHERE query_type = 'SELECT'
ORDER BY start_time DESC limit 10;
```

Sample output.

```

 query_id | transaction_id | session_id |         start_time         | elapsed_time | queue_time | execution_time | returned_rows | returned_bytes
----------+----------------+------------+----------------------------+--------------+------------+----------------+---------------+----------------
   526532 |          61093 | 1073840313 | 2022-02-09 04:43:24.149603 |       520571 |          0 |         481293 |             1 |           3794
   526520 |          60850 | 1073840313 | 2022-02-09 04:38:27.24875  |       635957 |          0 |         596601 |             1 |           3679
   526508 |          60803 | 1073840313 | 2022-02-09 04:37:51.118835 |       563882 |          0 |         503135 |             5 |          17216
   526505 |          60763 | 1073840313 | 2022-02-09 04:36:48.636224 |       649337 |          0 |         589823 |             1 |            652
   526478 |          60730 | 1073840313 | 2022-02-09 04:36:11.741471 |     14611321 |          0 |       14544058 |             0 |              0
   526467 |          60636 | 1073840313 | 2022-02-09 04:34:11.91463  |     16711367 |          0 |       16633767 |             1 |            575
   511617 |         617946 | 1074009948 | 2022-01-20 06:21:54.44481  |      9937090 |          0 |        9899271 |           100 |          12500
   511603 |         617941 | 1074259415 | 2022-01-20 06:21:45.71744  |      8065081 |          0 |        7582500 |           100 |           8889
   511595 |         617935 | 1074128320 | 2022-01-20 06:21:44.030876 |      1051270 |          0 |        1014879 |             1 |             72
   511584 |         617931 | 1074030019 | 2022-01-20 06:21:42.764088 |       609033 |          0 |         485887 |           100 |           8438
```

The following query shows the daily select query count and average query elapsed
time.

```
SELECT date_trunc('day',start_time) AS exec_day,
       status,
       COUNT(*) AS query_cnt,
       AVG(datediff (microsecond,start_time,end_time)) AS elapsed_avg
FROM sys_query_history
WHERE query_type = 'SELECT'
AND start_time >= '2022-01-14'
AND start_time <= '2022-01-18'
GROUP BY exec_day,
         status
ORDER BY exec_day,
         status;
```

Sample output.

```
      exec_day       | status  | query_cnt | elapsed_avg
---------------------+---------+-----------+------------
 2022-01-14 00:00:00 | success |      5253 |  56608048
 2022-01-15 00:00:00 | success |      7004 |  56995017
 2022-01-16 00:00:00 | success |      5253 |  57016363
 2022-01-17 00:00:00 | success |      5309 |  55236784
 2022-01-18 00:00:00 | success |      8092 |  54355124
```

The following query shows the daily query elapsed time performance.

```
SELECT distinct date_trunc('day',start_time) AS exec_day,
       query_count.cnt AS query_count,
       Percentile_cont(0.5) within group(ORDER BY elapsed_time) OVER (PARTITION BY exec_day) AS P50_runtime,
       Percentile_cont(0.8) within group(ORDER BY elapsed_time) OVER (PARTITION BY exec_day) AS P80_runtime,
       Percentile_cont(0.9) within group(ORDER BY elapsed_time) OVER (PARTITION BY exec_day) AS P90_runtime,
       Percentile_cont(0.99) within group(ORDER BY elapsed_time) OVER (PARTITION BY exec_day) AS P99_runtime,
       Percentile_cont(1.0) within group(ORDER BY elapsed_time) OVER (PARTITION BY exec_day) AS max_runtime
FROM sys_query_history
LEFT JOIN (SELECT  date_trunc('day',start_time) AS day, count(*) cnt
           FROM sys_query_history
           WHERE query_type = 'SELECT'
           GROUP by 1) query_count
ON date_trunc('day',start_time) = query_count.day
WHERE query_type = 'SELECT'
ORDER BY exec_day;
```

Sample output.

```

      exec_day       | query_count | p50_runtime | p80_runtime | p90_runtime | p99_runtime  | max_runtime
---------------------+-------------+-------------+-------------+-------------+--------------+--------------
 2022-01-14 00:00:00 |        5253 |  16816922.0 |  69525096.0 | 158524917.8 | 486322477.52 | 1582078873.0
 2022-01-15 00:00:00 |        7004 |  15896130.5 |  71058707.0 | 164314568.9 | 500331542.07 | 1696344792.0
 2022-01-16 00:00:00 |        5253 |  15750451.0 |  72037082.2 | 159513733.4 | 480372059.24 | 1594793766.0
 2022-01-17 00:00:00 |        5309 |  15394513.0 |  68881393.2 | 160254700.0 | 493372245.84 | 1521758640.0
 2022-01-18 00:00:00 |        8092 |  15575286.5 |  68485955.4 | 154559572.5 | 463552685.39 | 1542783444.0
 2022-01-19 00:00:00 |        5860 |  16648747.0 |  72470482.6 | 166485138.2 | 492038228.67 | 1693483241.0
 2022-01-20 00:00:00 |        1751 |  15422072.0 |  69686381.0 | 162315385.0 | 497066615.00 | 1439319739.0
 2022-02-09 00:00:00 |          13 |   6382812.0 |  17616161.6 |  21197988.4 |  23021343.84 |   23168439.0
```

The following query shows the query type distribution.

```
SELECT query_type,
       COUNT(*) AS query_count
FROM sys_query_history
GROUP BY query_type
ORDER BY query_count DESC;
```

Sample output.

```
 query_type | query_count
------------+-------------
 UTILITY    |      134486
 SELECT     |       38537
 DDL        |        4832
 OTHER      |         768
 LOAD       |         768
 CTAS       |         748
 COMMAND    |          92
```

The following example shows the difference in
query hash results between several queries.
Observe the following queries:

```
CREATE TABLE test_table (col1 INT);

INSERT INTO test_table VALUES (1),(2);

SELECT * FROM test_table;

SELECT * FROM test_table;

SELECT col1 FROM test_table;

SELECT * FROM test_table WHERE col1=1;

SELECT * FROM test_table WHERE col1=2;

SELECT query_id, TRIM(user_query_hash) AS user_query_hash, TRIM(generic_query_hash) AS generic_query_hash, TRIM(query_text) AS text FROM sys_query_history ORDER BY start_time
DESC LIMIT 10;
```

Following is a sample output:

```
query_id | user_query_hash | generic_query_hash | text
---------+-----------------+--------------------+----------
24723049 | oPuFtjEPLTs=    | oPuFtjEPLTs=       | select query_id, trim(user_query_hash) as user_query_hash, trim(generic_query_hash) as generic_query_hash, query_hash_version, trim(query_text) as text from sys_query_history order by start_time\r\ndesc limit 20
24723045 | Gw2Kwdd8m2I=    | IwfRu8/XAKI=       | select * from test_table where col1=2 limit 100
24723041 | LNw2vx0GDXo=    | IwfRu8/XAKI=       | select * from test_table where col1=1 limit 100
24723036 | H+qep/c82Y8=    | H+qep/c82Y8=       | select col1 from test_table limit 100
24723033 | H+qep/c82Y8=    | H+qep/c82Y8=       | select * from test_table limit 100
24723029 | H+qep/c82Y8=    | H+qep/c82Y8=       | select * from test_table limit 100
24723023 | 50sirx9E1hU=    | uO36Z1a/QYs=       | insert into test_table values (1),(2)
24723021 | YSVnlivZHeo=    | YSVnlivZHeo=       | create table test_table (col1 int)
```

`SELECT * FROM test_table;` and `SELECT col1 FROM test_table;` have
the same user_query_hash value, since test_table has only one column.
`SELECT * FROM test_table WHERE col1=1;` and
`SELECT * FROM test_table WHERE col1=2;` have different user_query_hash values,
but identical generic_query_hash values, since the two queries are
identical outside of the query literals 1 and 2.
