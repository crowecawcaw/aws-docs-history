Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_HASH

Analyzes hash execution steps for queries.

STL_HASH is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_HASH only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name             | Data type    | Description                                                                                                                                                                   |
| ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | ----- | -------- | ------- | --------- | -------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------- | --- | ------ | --- | -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | ----------------- |
| userid                  | integer      | ID of the user who generated the entry.                                                                                                                                       |
| query                   | integer      | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice                   | integer      | Number that identifies the slice where the query was running.                                                                                                                 |
| segment                 | integer      | Number that identifies the query segment.                                                                                                                                     |
| step                    | integer      | Query step that ran.                                                                                                                                                          |
| starttime               | timestamp    | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime                 | timestamp    | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum                 | integer      | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows                    | bigint       | Total number of rows that were processed.                                                                                                                                     |
| bytes                   | bigint       | Size, in bytes, of all the output rows for the step.                                                                                                                          |
| slots                   | integer      | Total number of hash buckets.                                                                                                                                                 |
| occupied                | integer      | Total number of slots that contain records.                                                                                                                                   |
| maxlength               | integer      | Size of the largest slot.                                                                                                                                                     |
| tbl                     | integer      | Table ID.                                                                                                                                                                     |
| is_diskbased            | character(1) | If true (t), the query was performed as a disk-based operation. If false (f), the query was performed in memory.                                                              |
| workmem                 | bigint       | Total number of bytes of working memory assigned to the step.                                                                                                                 |
| num_parts               | integer      | Total number of partitions that a hash table was divided into during a hash step.                                                                                             |
| est_rows                | bigint       | Estimated number of rows to be hashed.                                                                                                                                        |
| num_blocks_permitted    | integer      | This information is for internal use only.                                                                                                                                    |
| resizes                 | integer      | This information is for internal use only.                                                                                                                                    |
| checksum                | bigint       | This information is for internal use only.                                                                                                                                    |
| runtime_filter_size     | integer      | Size of the runtime filter in bytes.                                                                                                                                          |
| max_runtime_filter_size | integer      | Maximum size of the runtime filter in bytes.                                                                                                                                  | ## Sample queries The following example returns information about the number of partitions that were used in a hash for query 720, and indicates that none of the steps ran on disk. `select slice, rows, bytes, occupied, workmem, num_parts, est_rows, num_blocks_permitted, is_diskbased from stl_hash where query=720 and segment=5 order by slice;` ``` slice | rows | bytes | occupied | workmem | num_parts | est_rows | num_blocks_permitted | is_diskbased -------+------+--------+----------+----------+-----------+----------+----------------------+-------------- 0 | 145 | 585800 | 1   | 88866816 | 16  | 1   | 52 f 1 | 0   | 0   | 0   | 0   | 16  | 1   | 52 f (2 rows) ``` |
