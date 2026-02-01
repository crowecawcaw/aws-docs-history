Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_DISKUSAGE

Amazon Redshift creates the SVV_DISKUSAGE system view by joining the STV_TBL_PERM and
STV_BLOCKLIST tables. The SVV_DISKUSAGE view contains information about data allocation
for the tables in a database.

Use aggregate queries with SVV_DISKUSAGE, as the following examples show, to determine
the number of disk blocks allocated per database, table, slice, or column. Each data
block uses 1 MB. You can also use [STV_PARTITIONS](r_STV_PARTITIONS.md "r_STV_PARTITIONS.md") to view summary information about disk
utilization.

SVV_DISKUSAGE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name      | Data type     | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db_id            | integer       | Database ID.                                                                                                                                                                                                                                                                                                                                                                                             |
| name             | character(72) | Table name.                                                                                                                                                                                                                                                                                                                                                                                              |
| slice            | integer       | Data slice allocated to the table.                                                                                                                                                                                                                                                                                                                                                                       |
| col              | integer       | Zero-based index for the column. Every table you<br>create has three hidden columns appended to it: INSERT_XID,<br>DELETE_XID, and ROW_ID (OID). A table with 3 user-defined columns<br>contains 6 actual columns, and the user-defined columns are<br>internally numbered as 0, 1, and 2. The INSERT_XID, DELETE_XID, and<br>ROW_ID columns are numbered 3, 4, and 5, respectively, in this<br>example. |
| tbl              | integer       | Table ID.                                                                                                                                                                                                                                                                                                                                                                                                |
| blocknum         | integer       | ID for the data block.                                                                                                                                                                                                                                                                                                                                                                                   |
| num_values       | integer       | Number of values contained on the block.                                                                                                                                                                                                                                                                                                                                                                 |
| minvalue         | bigint        | Minimum value contained on the block.                                                                                                                                                                                                                                                                                                                                                                    |
| maxvalue         | bigint        | Maximum value contained on the block.                                                                                                                                                                                                                                                                                                                                                                    |
| sb_pos           | integer       | Internal identifier for the position of the super<br>block on disk.                                                                                                                                                                                                                                                                                                                                      |
| pinned           | integer       | Whether or not the block is pinned into memory as<br>part of pre-load. 0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                            |
| on_disk          | integer       | Whether or not the block is automatically stored<br>on disk. 0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                      |
| modified         | integer       | Whether or not the block has been modified. 0 =<br>false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                                    |
| hdr_modified     | integer       | Whether or not the block header has been modified.<br>0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                             |
| unsorted         | integer       | Whether or not a block is unsorted. 0 = false; 1 =<br>true. Default is true.                                                                                                                                                                                                                                                                                                                             |
| tombstone        | integer       | For internal use.                                                                                                                                                                                                                                                                                                                                                                                        |
| preferred_diskno | integer       | Disk number that the block should be on, unless<br>the disk has failed. Once the disk has been fixed, the block will<br>move back to this disk.                                                                                                                                                                                                                                                          |
| temporary        | integer       | Whether or not the block contains temporary data,<br>such as from a temporary table or intermediate query results. 0 =<br>false; 1 = true. Default is false.                                                                                                                                                                                                                                             |
| newblock         | integer       | Indicates whether or not a block is new (true) or<br>was never committed to disk (false). 0 = false; 1 = true.                                                                                                                                                                                                                                                                                           |

## Sample queries

SVV_DISKUSAGE contains one row per allocated disk block, so a query that selects
all the rows potentially returns a very large number of rows. We recommend using
only aggregate queries with SVV_DISKUSAGE.

Return the highest number of blocks ever allocated to column 6 in the USERS table
(the EMAIL column):

```
select db_id, trim(name) as tablename, max(blocknum)
from svv_diskusage
where name='users' and col=6
group by db_id, name;

db_id  | tablename | max
--------+-----------+-----
175857 | users     |   2
(1 row)
```

The following query returns similar results for all of the columns in a large
10-column table called SALESNEW. (The last three rows, for columns 10 through 12,
are for the hidden metadata columns.)

```
select db_id, trim(name) as tablename, col, tbl, max(blocknum)
from svv_diskusage
where name='salesnew'
group by db_id, name, col, tbl
order by db_id, name, col, tbl;

db_id  | tablename  | col |  tbl   | max
--------+------------+-----+--------+-----
175857 | salesnew   |   0 | 187605 | 154
175857 | salesnew   |   1 | 187605 | 154
175857 | salesnew   |   2 | 187605 | 154
175857 | salesnew   |   3 | 187605 | 154
175857 | salesnew   |   4 | 187605 | 154
175857 | salesnew   |   5 | 187605 |  79
175857 | salesnew   |   6 | 187605 |  79
175857 | salesnew   |   7 | 187605 | 302
175857 | salesnew   |   8 | 187605 | 302
175857 | salesnew   |   9 | 187605 | 302
175857 | salesnew   |  10 | 187605 |   3
175857 | salesnew   |  11 | 187605 |   2
175857 | salesnew   |  12 | 187605 | 296
(13 rows)
```
