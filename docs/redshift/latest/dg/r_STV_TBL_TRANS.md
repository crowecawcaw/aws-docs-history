Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_TBL_TRANS

Use the STV_TBL_TRANS table to find out information about the transient database
tables that are currently in memory.

Transient tables are typically temporary row sets that are used as intermediate
results while a query runs. STV_TBL_TRANS differs from [STV_TBL_PERM](r_STV_TBL_PERM.md "r_STV_TBL_PERM.md") in that STV_TBL_PERM contains information about
permanent database tables.

STV_TBL_TRANS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type | Description                                                                                                                                    |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| slice          | integer   | Node slice allocated to the table.                                                                                                             |
| id             | integer   | Table ID.                                                                                                                                      |
| rows           | bigint    | Number of data rows in the table.                                                                                                              |
| size           | bigint    | Number of bytes allocated to the table.                                                                                                        |
| query_id       | bigint    | Query ID.                                                                                                                                      |
| ref_cnt        | integer   | Number of references.                                                                                                                          |
| from_suspended | integer   | Whether or not this table was created during a<br>query that is now suspended.                                                                 |
| prep_swap      | integer   | Whether or not this transient table is prepared to<br>swap to disk if needed. (The swap will only occur in situations<br>where memory is low.) |

## Sample queries

To view transient table information for a query with a query ID of 90, type the
following command:

```
select slice, id, rows, size, query_id, ref_cnt
from stv_tbl_trans
where query_id = 90;
```

This query returns the transient table information for query 90, as shown in the
following sample output:

```

slice | id | rows | size | query_ | ref_ | from_     | prep_
      |    |      |      | id     | cnt  | suspended | swap
------+----+------+------+--------+------+-----------+-------
 1013 | 95 |    0 |    0 |     90 |    4 |         0 |   0
    7 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   10 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   17 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   14 | 96 |    0 |    0 |     90 |    4 |         0 |   0
    3 | 96 |    0 |    0 |     90 |    4 |         0 |   0
 1013 | 99 |    0 |    0 |     90 |    4 |         0 |   0
    9 | 96 |    0 |    0 |     90 |    4 |         0 |   0
    5 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   19 | 96 |    0 |    0 |     90 |    4 |         0 |   0
    2 | 96 |    0 |    0 |     90 |    4 |         0 |   0
 1013 | 98 |    0 |    0 |     90 |    4 |         0 |   0
   13 | 96 |    0 |    0 |     90 |    4 |         0 |   0
    1 | 96 |    0 |    0 |     90 |    4 |         0 |   0
 1013 | 96 |    0 |    0 |     90 |    4 |         0 |   0
    6 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   11 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   15 | 96 |    0 |    0 |     90 |    4 |         0 |   0
   18 | 96 |    0 |    0 |     90 |    4 |         0 |   0

```

In this example, you can see that the query data involves tables 95, 96, and 98.
Because zero bytes are allocated to this table, this query can run in memory.
