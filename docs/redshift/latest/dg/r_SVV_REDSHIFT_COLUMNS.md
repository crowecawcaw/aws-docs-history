Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_REDSHIFT\_COLUMNS

Use SVV\_REDSHIFT\_COLUMNS to view a list of all columns that a user has access to. This
set of columns includes the columns on the cluster and the columns from datashares
provided by remote clusters.

SVV\_REDSHIFT\_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW COLUMNS](r_SHOW_COLUMNS.md "r_SHOW_COLUMNS.md") command for column discovery. SHOW COLUMNS works consistently across
local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name       | Data type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| database\_name    | varchar(128)  | The name of the database where the table<br>containing the columns exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| schema\_name      | varchar(128)  | The name of the schema for the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| table\_name       | varchar(128)  | The name of the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| column\_name      | varchar(128)  | The name of a column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ordinal\_position | integer       | The position of the column in the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| data\_type        | varchar(32)   | The data type of the column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| column\_default   | varchar(4000) | The default value of the column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| is\_nullable      | varchar(3)    | A value that defines whether a column is nullable. Possible<br>values are `yes`, `no`, and " " (an empty<br>string that represents no information).                                                                                                                                                                                                                                                                                                                                                                                                        |
| encoding          | varchar(128)  | The encoding type of the column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| distkey           | boolean       | A value that is true if this column is the<br>distribution key for the table, and false otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| sortkey           | integer       | A value that specifies the order of the column in the sort<br>key.<br>If the table uses a compound sort key, then all columns that<br>are part of the sort key have a positive value that indicates<br>the position of the column in the sort key.<br>If the table uses an interleaved sort key, then each column<br>that is part of the sort key has a value that is alternately<br>positive or negative. Here, the absolute value indicates the<br>position of the column in the sort key.<br>If `sortkey` is 0, the column isn't part of a<br>sort key. |
| column\_acl       | varchar(128)  | A string that defines the permissions for the<br>specified user or user group for the column.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| remarks           | varchar(256)  | Remarks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Sample query

The following example returns the output of SVV\_REDSHIFT\_COLUMNS.

```
SELECT *
FROM svv_redshift_columns
WHERE database_name = 'tickit_db'
    AND TABLE_NAME = 'tickit_sales_redshift'
ORDER BY COLUMN_NAME,
    TABLE_NAME,
    database_name
LIMIT 5;

database_name | schema_name |       table_name      | column_name | ordinal_position | data_type | column_default | is_nullable | encoding | distkey | sortkey | column_acl  | remarks
--------------+-------------+-----------------------+-------------+------------------+-----------+----------------+-------------+----------+---------+---------+-------------+--------
   tickit_db  |   public    | tickit_sales_redshift |   buyerid   |        4         |  integer  |                |      NO     |   az64   |  False  |    0    |             |
   tickit_db  |   public    | tickit_sales_redshift |  commission |        9         |  numeric  |      (8,2)     |     YES     |   az64   |  False  |    0    |             |
   tickit_db  |   public    | tickit_sales_redshift |    dateid   |        6         |  smallint |                |      NO     |   none   |  False  |    1    |             |
   tickit_db  |   public    | tickit_sales_redshift |   eventid   |        5         |  integer  |                |      NO     |   az64   |  False  |    0    |	      |
   tickit_db  |   public    | tickit_sales_redshift |   listid    |        2         |  integer  |                |      NO     |   az64   |  True   |    0    |             |
```
