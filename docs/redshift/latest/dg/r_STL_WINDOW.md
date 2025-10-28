Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_WINDOW

Analyzes query steps that perform window functions.

STL_WINDOW is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_WINDOW only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name  | Data type    | Description                                                                                                                                                                   |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---- | ------------ | ---------------------------------------------------------------- | --- | ---- | --- | ------------ | --- | ---- | --- | -------------- | --- | ---- | --- | ------------ | --- | --- | --- | --------------------- |
| userid       | integer      | ID of the user who generated the entry.                                                                                                                                       |
| query        | integer      | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice        | integer      | Number that identifies the slice where the query was running.                                                                                                                 |
| segment      | integer      | Number that identifies the query segment.                                                                                                                                     |
| step         | integer      | Query step that ran.                                                                                                                                                          |
| starttime    | timestamp    | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime      | timestamp    | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum      | integer      | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows         | bigint       | Total number of rows that were processed.                                                                                                                                     |
| is_diskbased | character(1) | If true (t), the query was performed as a disk-based operation. If false (f), the query was performed in memory.                                                              |
| workmem      | bigint       | Total number of bytes in working memory that were assigned to the step.                                                                                                       | ## Sample queries The following example returns window function results for slice 0 and segment 3. `select query, tasknum, rows, is_diskbased, workmem from stl_window where slice=0 and segment=3;` ``` query | tasknum | rows | is_diskbased | workmem -------+---------+------+--------------+---------- 86326 | 36  | 1857 | f   | 95256616 705 | 15  | 1857 | f   | 95256616 86399 | 27  | 1857 | f   | 95256616 649 | 10  | 0   | f   | 95256616 (4 rows) ``` |
