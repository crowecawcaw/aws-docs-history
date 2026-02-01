Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_BLOCKLIST

STV_BLOCKLIST contains the number of 1 MB disk blocks that are used by each slice,
table, or column in a database.

Use aggregate queries with STV_BLOCKLIST, as the following examples show, to determine
the number of 1 MB disk blocks allocated per database, table, slice, or column. You can
also use [STV_PARTITIONS](r_STV_PARTITIONS.md "r_STV_PARTITIONS.md") to view
summary information about disk utilization.

STV_BLOCKLIST is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STV_BLOCKLIST only records blocks owned by the provisioned cluster or serverless namespace.
If the database includes blocks shared from a datashare producer, those blocks aren’t
included in STV_BLOCKLIST. For more information about datashares, go to
[Data sharing in Amazon Redshift](datashare-overview.md "datashare-overview.md").

## Table columns

| Column name      | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| slice            | integer   | Node slice.                                                                                                                                                                                                                                                                                                                                                                                              |
| col              | integer   | Zero-based index for the column. Every table you<br>create has three hidden columns appended to it: INSERT_XID,<br>DELETE_XID, and ROW_ID (OID). A table with 3 user-defined columns<br>contains 6 actual columns, and the user-defined columns are<br>internally numbered as 0, 1, and 2. The INSERT_XID, DELETE_XID, and<br>ROW_ID columns are numbered 3, 4, and 5, respectively, in this<br>example. |
| tbl              | integer   | Table ID for the database table.                                                                                                                                                                                                                                                                                                                                                                         |
| blocknum         | integer   | ID for the data block.                                                                                                                                                                                                                                                                                                                                                                                   |
| num_values       | integer   | Number of values contained on the block.                                                                                                                                                                                                                                                                                                                                                                 |
| extended_limits  | integer   | For internal use.                                                                                                                                                                                                                                                                                                                                                                                        |
| minvalue         | bigint    | Minimum data value of the block. Stores first<br>eight characters as 64-bit integer for non-numeric data. Used for<br>disk scanning.                                                                                                                                                                                                                                                                     |
| maxvalue         | bigint    | Maximum data value of the block. Stores first<br>eight characters as 64-bit integer for non-numeric data. Used for<br>disk scanning.                                                                                                                                                                                                                                                                     |
| sb_pos           | integer   | Internal Amazon Redshift identifier for super block<br>position on the disk.                                                                                                                                                                                                                                                                                                                             |
| pinned           | integer   | Whether or not the block is pinned into memory as<br>part of pre-load. 0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                            |
| on_disk          | integer   | Whether or not the block is automatically stored<br>on disk. 0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                      |
| modified         | integer   | Whether or not the block has been modified. 0 =<br>false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                                    |
| hdr_modified     | integer   | Whether or not the block header has been modified.<br>0 = false; 1 = true. Default is false.                                                                                                                                                                                                                                                                                                             |
| unsorted         | integer   | Whether or not a block is unsorted. 0 = false; 1 =<br>true. Default is true.                                                                                                                                                                                                                                                                                                                             |
| tombstone        | integer   | For internal use.                                                                                                                                                                                                                                                                                                                                                                                        |
| preferred_diskno | integer   | Disk number that the block should be on, unless<br>the disk has failed. Once the disk has been fixed, the block will<br>move back to this disk.                                                                                                                                                                                                                                                          |
| temporary        | integer   | Whether or not the block contains temporary data,<br>such as from a temporary table or intermediate query results. 0 =<br>false; 1 = true. Default is false.                                                                                                                                                                                                                                             |
| newblock         | integer   | Indicates whether or not a block is new (true) or<br>was never committed to disk (false). 0 = false; 1 = true.                                                                                                                                                                                                                                                                                           |
| num_readers      | integer   | Number of references on each block.                                                                                                                                                                                                                                                                                                                                                                      |
| flags            | integer   | Internal Amazon Redshift flags for the block header.                                                                                                                                                                                                                                                                                                                                                     |

## Sample queries

STV_BLOCKLIST contains one row per allocated disk block, so a query that selects
all the rows potentially returns a very large number of rows. We recommend using
only aggregate queries with STV_BLOCKLIST.

The [SVV_DISKUSAGE](r_SVV_DISKUSAGE.md "r_SVV_DISKUSAGE.md") view
provides similar information in a more user-friendly format; however, the following
example demonstrates one use of the STV_BLOCKLIST table.

To determine the number of 1 MB blocks used by each column in the VENUE table,
type the following query:

```
select col, count(*)
from stv_blocklist, stv_tbl_perm
where stv_blocklist.tbl = stv_tbl_perm.id
and stv_blocklist.slice = stv_tbl_perm.slice
and stv_tbl_perm.name = 'venue'
group by col
order by col;
```

This query returns the number of 1 MB blocks allocated to each column in the VENUE
table, shown by the following sample data:

```
 col | count
-----+-------
   0 |  4
   1 |  4
   2 |  4
   3 |  4
   4 |  4
   5 |  4
   7 |  4
   8 |  4
(8 rows)

```

The following query shows whether or not table data is actually distributed over
all slices:

```
select trim(name) as table, stv_blocklist.slice, stv_tbl_perm.rows
from stv_blocklist,stv_tbl_perm
where stv_blocklist.tbl=stv_tbl_perm.id
and stv_tbl_perm.slice=stv_blocklist.slice
and stv_blocklist.id > 10000 and name not like '%#m%'
and name not like 'systable%'
group by name, stv_blocklist.slice, stv_tbl_perm.rows
order by 3 desc;
```

This query produces the following sample output, showing the even data
distribution for the table with the most rows:

```

table   | slice | rows
----------+-------+-------
listing  |    13 | 10527
listing  |    14 | 10526
listing  |     8 | 10526
listing  |     9 | 10526
listing  |     7 | 10525
listing  |     4 | 10525
listing  |    17 | 10525
listing  |    11 | 10525
listing  |     5 | 10525
listing  |    18 | 10525
listing  |    12 | 10525
listing  |     3 | 10525
listing  |    10 | 10525
listing  |     2 | 10524
listing  |    15 | 10524
listing  |    16 | 10524
listing  |     6 | 10524
listing  |    19 | 10524
listing  |     1 | 10523
listing  |     0 | 10521
...
(180 rows)

```

The following query determines whether any tombstoned blocks were committed to
disk:

```
select slice, col, tbl, blocknum, newblock
from stv_blocklist
where  tombstone > 0;

slice | col |   tbl  | blocknum | newblock
-------+-----+--------+----------+----------
4     |  0  | 101285 |    0     |   1
4     |  2  | 101285 |    0     |   1
4     |  4  | 101285 |    1     |   1
5     |  2  | 101285 |    0     |   1
5     |  0  | 101285 |    0     |   1
5     |  1  | 101285 |    0     |   1
5     |  4  | 101285 |    1     |   1
...
(24 rows)
```
