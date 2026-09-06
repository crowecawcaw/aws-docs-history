

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_INTERLEAVED\_COLUMNS
<a name="r_SVV_INTERLEAVED_COLUMNS"></a>

Use the SVV\_INTERLEAVED\_COLUMNS view to help determine whether a table that uses interleaved sort keys should be reindexed using [VACUUM REINDEX](r_VACUUM_command.md#vacuum-reindex). For more information about how to determine how often to run VACUUM and when to run a VACUUM REINDEX, see [Minimizing vacuum times](vacuum-managing-vacuum-times.md).

SVV\_INTERLEAVED\_COLUMNS is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SVV_INTERLEAVED_COLUMNS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| tbl | integer  | Table ID. | 
| col | integer | Zero-based index for the column. | 
| interleaved\_skew | numeric(19,2) | Ratio that indicates of the amount of skew present in the interleaved sort key columns for a table. A value of 1.00 indicates no skew, and larger values indicate more skew. Tables with a large skew should be reindexed with the VACUUM REINDEX command.  | 
| last\_reindex | timestamp | Time when the last VACUUM REINDEX was run for the specified table. This value is NULL if a table has never been reindexed or if the underlying system log table, STL\_VACUUM, has been rotated since the last reindex. | 

## Sample queries
<a name="SVV_INTERLEAVED_COLUMNS-sample-queries"></a>

To identify tables that might need to be reindexed, run the following query.

```
select tbl as tbl_id, stv_tbl_perm.name as table_name, 
col, interleaved_skew, last_reindex
from svv_interleaved_columns, stv_tbl_perm
where svv_interleaved_columns.tbl = stv_tbl_perm.id
and interleaved_skew is not null;

 tbl_id | table_name | col | interleaved_skew | last_reindex
--------+------------+-----+------------------+--------------------
 100068 | lineorder  |   0 |             3.65 | 2015-04-22 22:05:45
 100068 | lineorder  |   1 |             2.65 | 2015-04-22 22:05:45
 100072 | customer   |   0 |             1.65 | 2015-04-22 22:05:45
 100072 | lineorder  |   1 |             1.00 | 2015-04-22 22:05:45
(4 rows)
```