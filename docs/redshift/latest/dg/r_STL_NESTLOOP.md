Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_NESTLOOP

Analyzes nested-loop join execution steps for queries.

STL_NESTLOOP is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_NESTLOOP only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type | Description                                                                                                                                                                   |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | --- | ---- | -------- | ------- | ---- | ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | ----- | ------- |
| userid      | integer   | ID of the user who generated the entry.                                                                                                                                       |
| query       | integer   | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice       | integer   | Number that identifies the slice where the query was running.                                                                                                                 |
| segment     | integer   | Number that identifies the query segment.                                                                                                                                     |
| step        | integer   | Query step that ran.                                                                                                                                                          |
| starttime   | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime     | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum     | integer   | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows        | bigint    | Total number of rows that were processed.                                                                                                                                     |
| tbl         | integer   | Table ID.                                                                                                                                                                     |
| checksum    | bigint    | This information is for internal use only.                                                                                                                                    | ## Sample queries Because the following query neglects to join the CATEGORY table, it produces a partial Cartesian product, which is not recommended. It is shown here to illustrate a nested loop. `select count(event.eventname), event.eventname, category.catname, date.caldate from event, category, date where event.dateid = date.dateid group by event.eventname, category.catname, date.caldate;` The following query shows the results from the previous query in the STL_NESTLOOP view. `select query, slice, segment as seg, step, datediff(msec, starttime, endtime) as duration, tasknum, rows, tbl from stl_nestloop where query = pg_last_query_id();` ``` query | slice | seg | step | duration | tasknum | rows | tbl -------+-------+-----+------+----------+---------+-------+----- 6028 | 0   | 4   | 5   | 41  | 22  | 24277 | 240 6028 | 1   | 4   | 5   | 26  | 23  | 24189 | 240 6028 | 3   | 4   | 5   | 25  | 23  | 24376 | 240 6028 | 2   | 4   | 5   | 54  | 22  | 23936 | 240 ``` |
