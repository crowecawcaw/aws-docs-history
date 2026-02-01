Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_DISK_FULL_DIAG

Logs information about errors recorded when the disk is full.

STL_DISK_FULL_DIAG is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type | Description                                                                     |
| ----------- | --------- | ------------------------------------------------------------------------------- |
| currenttime | bigint    | The day and time the error was generated in microseconds since January 1, 2000. |
| node_num    | bigint    | The identifier for the node.                                                    |
| query_id    | bigint    | The identifier for the query that caused the<br>error.                          |
| temp_blocks | bigint    | The number of temporary blocks created by the<br>query.                         |

## Sample queries

The following example returns details about the data stored when there is a
disk-full error.

```
select * from stl_disk_full_diag
```

The following example converts the `currenttime` to a timestamp.

```
select '2000-01-01'::timestamp + (currenttime/1000000.0)* interval '1 second' as currenttime,node_num,query_id,temp_blocks from pg_catalog.stl_disk_full_diag;
```

```

        currenttime         | node_num | query_id | temp_blocks
----------------------------+----------+----------+-------------
 2019-05-18 19:19:18.609338 |        0 |   569399 |       70982
 2019-05-18 19:37:44.755548 |        0 |   569580 |       70982
 2019-05-20 13:37:20.566916 |        0 |   597424 |       70869

```
