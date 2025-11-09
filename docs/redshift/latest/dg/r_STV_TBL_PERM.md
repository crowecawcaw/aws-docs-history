Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_TBL_PERM

The STV_TBL_PERM table contains information about the permanent tables in Amazon Redshift,
including temporary tables created by a user for the current session. STV_TBL_PERM
contains information for all tables in all databases.

This table differs from [STV_TBL_TRANS](r_STV_TBL_TRANS.md "r_STV_TBL_TRANS.md"), which contains information about transient
database tables that the system creates during query processing.

STV_TBL_PERM is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type     | Description                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| slice           | integer       | Node slice allocated to the table.                                                                                                                                                                                                                                                                                     |
| id              | integer       | Table ID.                                                                                                                                                                                                                                                                                                              |
| name            | character(72) | Table name.                                                                                                                                                                                                                                                                                                            |
| rows            | bigint        | Number of data rows in the slice.                                                                                                                                                                                                                                                                                      |
| sorted_rows     | bigint        | Number of rows in the slice that are already<br>sorted on disk. If this number does not match the ROWS number,<br>vacuum the table to resort the rows.                                                                                                                                                                 |
| temp            | integer       | Whether or not the table is a temporary table. 0 =<br>false; 1 = true.                                                                                                                                                                                                                                                 |
| db_id           | integer       | ID of the database where the table was created.                                                                                                                                                                                                                                                                        |
| insert_pristine | integer       | For internal use.                                                                                                                                                                                                                                                                                                      |
| delete_pristine | integer       | For internal use.                                                                                                                                                                                                                                                                                                      |
| backup          | integer       | Value that indicates whether the table is included<br>in cluster snapshots. 0 = no; 1 = yes. For more information, see the<br>[BACKUP](r_CREATE_TABLE_NEW.md#create-table-backup "r_CREATE_TABLE_NEW.md#create-table-backup") parameter for the CREATE<br>TABLE command.                                               |
| dist_style      | integer       | Distribution style of the table that the slice<br>belongs to. For information on the values, see [Viewing distribution styles](viewing-distribution-styles.md "viewing-distribution-styles.md"). For information on distribution styles, see [Distribution styles](c_choosing_dist_sort.md "c_choosing_dist_sort.md"). |
| block_count     | integer       | Number of blocks used by the slice. The value is -1 when the block count can't be calculated.                                                                                                                                                                                                                          |

## Sample queries

The following query returns a list of distinct table IDs and names:

```
select distinct id, name
from stv_tbl_perm order by name;

   id   |          name
--------+-------------------------
 100571 | category
 100575 | date
 100580 | event
 100596 | listing
 100003 | padb_config_harvest
 100612 | sales
...
```

Other system tables use table IDs, so knowing which table ID corresponds to a
certain table can be very useful. In this example, SELECT DISTINCT is used to remove
the duplicates (tables are distributed across multiple slices).

To determine the number of blocks used by each column in the VENUE table, type the
following query:

```
select col, count(*)
from stv_blocklist, stv_tbl_perm
where stv_blocklist.tbl = stv_tbl_perm.id
and stv_blocklist.slice = stv_tbl_perm.slice
and stv_tbl_perm.name = 'venue'
group by col
order by col;

 col | count
-----+-------
   0 |     8
   1 |     8
   2 |     8
   3 |     8
   4 |     8
   5 |     8
   6 |     8
   7 |     8
(8 rows)
```

## Usage notes

The ROWS column includes counts of deleted rows that have not been vacuumed (or
have been vacuumed but with the SORT ONLY option). Therefore, the SUM of the ROWS
column in the STV_TBL_PERM table might not match the COUNT(\*) result when you query
a given table directly. For example, if 2 rows are deleted from VENUE, the COUNT(\*)
result is 200 but the SUM(ROWS) result is still 202:

```
delete from venue
where venueid in (1,2);

select count(*) from venue;
count
-------
200
(1 row)

select trim(name) tablename, sum(rows)
from stv_tbl_perm where name='venue' group by name;

tablename | sum
-----------+-----
venue     | 202
(1 row)
```

To synchronize the data in STV_TBL_PERM, run a full vacuum the VENUE table.

```
vacuum venue;

select trim(name) tablename, sum(rows)
from stv_tbl_perm
where name='venue'
group by name;

tablename | sum
-----------+-----
venue     | 200
(1 row)
```
