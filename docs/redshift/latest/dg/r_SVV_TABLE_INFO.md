Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_TABLE_INFO

Shows summary information for tables and materialized views in the
currently connected database. The view filters out system tables,
and shows only user-defined tables and materialized views
that contain at least 1 row of data.

You can use the SVV_TABLE_INFO view to diagnose and address table design issues that
can influence query performance. This includes issues with compression encoding,
distribution keys, sort style, data distribution skew, table size, and statistics. The
SVV_TABLE_INFO view doesn't return any information for empty tables.

The SVV_TABLE_INFO view summarizes information from the following
system tables and catalog tables:

- [STV_NODE_STORAGE_CAPACITY](r_STV_NODE_STORAGE_CAPACITY.md "r_STV_NODE_STORAGE_CAPACITY.md")
- [STV_SLICES](r_STV_SLICES.md "r_STV_SLICES.md")
- [STV_TBL_PERM](r_STV_TBL_PERM.md "r_STV_TBL_PERM.md")
- [PG_ATTRIBUTE](https://www.postgresql.org/docs/8.0/static/catalog-pg-attribute.html "https://www.postgresql.org/docs/8.0/static/catalog-pg-attribute.html")
- [PG_CLASS](https://www.postgresql.org/docs/8.0/static/catalog-pg-class.html "https://www.postgresql.org/docs/8.0/static/catalog-pg-class.html")
- [PG_DATABASE](https://www.postgresql.org/docs/8.0/static/catalog-pg-database.html "https://www.postgresql.org/docs/8.0/static/catalog-pg-database.html")
- [PG_NAMESPACE](https://www.postgresql.org/docs/8.0/static/catalog-pg-namespace.html "https://www.postgresql.org/docs/8.0/static/catalog-pg-namespace.html")
- [PG_STATISTIC_INDICATOR](r_PG_STATISTIC_INDICATOR.md "r_PG_STATISTIC_INDICATOR.md")
  SVV_TABLE_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and
  views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data"). To permit a user to query the view, grant SELECT
  permission on SVV_TABLE_INFO to the user.

## Table columns

| Column name            | Data type                   | Description                                                                                                                                                                                                       |
| ---------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------------------------- |
| database               | text                        | Database name.                                                                                                                                                                                                    |
| schema                 | text                        | Schema name.                                                                                                                                                                                                      |
| table_id               | oid                         | Table ID.                                                                                                                                                                                                         |
| table                  | text                        | Table name.                                                                                                                                                                                                       |
| encoded                | text                        | Value that indicates whether any column has<br>compression encoding defined.                                                                                                                                      |
| diststyle              | text                        | Distribution style or distribution key column, if<br>key distribution is defined. Possible values include<br>`EVEN`,<br>`KEY(*column*)`,<br>`ALL`,<br>`AUTO(ALL)`,<br>`AUTO(EVEN)`, and<br>`AUTO(KEY(*column*))`. |
| sortkey1               | text                        | First column in the sort key, if a sort key is<br>defined. Possible values include<br>`*column*`,<br>`AUTO(SORTKEY)`, and<br>`AUTO(SORTKEY(*column*))`.                                                           |
| max_varchar            | integer                     | Size of the largest column that uses a VARCHAR<br>data type.                                                                                                                                                      |
| sortkey1_enc           | character(32)               | Compression encoding of the first column in the<br>sort key, if a sort key is defined.                                                                                                                            |
| sortkey_num            | integer                     | Number of columns defined as sort keys.                                                                                                                                                                           |
| size                   | bigint                      | Size of the table, in 1-MB data blocks.                                                                                                                                                                           |
| pct_used               | numeric(10,4)               | Percent of available space that is used by the<br>table.                                                                                                                                                          |
| empty                  | bigint                      | For internal use. This column is no longer used<br>and will be removed in a future release.                                                                                                                       |
| unsorted               | numeric(5,2)                | Percent of unsorted rows in the table.                                                                                                                                                                            |
| stats_off              | numeric(5,2)                | Number that indicates how stale the table's<br>statistics are; 0 is current, 100 is out of date.                                                                                                                  |
| tbl_rows               | numeric(38,0)               | Total number of rows in the table. This value<br>includes rows marked for deletion, but not yet vacuumed.                                                                                                         |
| skew_sortkey1          | numeric(19,2)               | Ratio of the size of the largest non-sort key<br>column to the size of the first column of the sort key, if a sort<br>key is defined. Use this value to evaluate the effectiveness of the<br>sort key.            |
| skew_rows              | numeric(19,2)               | Ratio of the number of rows in the slice with the<br>most rows to the number of rows in the slice with the fewest rows.                                                                                           |
| estimated_visible_rows | numeric(38,0)               | The estimated rows in the table. This value does not include rows marked for deletion.                                                                                                                            |
| risk_event             | text                        | Risk information about a table. The field is separated into parts:<br>```<br>`risk_type`                                                                                                                          | `xid` | `timestamp`<br>``<br>• The `risk_type`, where `1` indicates that a `COPY command with the EXPLICIT_IDS option` ran.<br>Amazon Redshift no longer checks the uniqueness of IDENTITY columns in the table.<br>For more information,<br>see [EXPLICIT\_IDS](copy-parameters-data-conversion.md#copy-explicit-ids "copy-parameters-data-conversion.md#copy-explicit-ids").<br>• The transaction ID, `xid`, that introduced the risk.<br>• The `timestamp` when the COPY command ran.<br>The following example shows the values in the field.<br>``<br>1 | 1107 | 2019-06-22 07:16:11.292952<br>``` |
| vacuum_sort_benefit    | numeric(12,2)               | The estimated maximum percentage improvement of scan query performance when you run vacuum sort.                                                                                                                  |
| create_time            | timestamp without time zone | The timestamp for when the table was created.                                                                                                                                                                     |

## Sample queries

The following example shows encoding, distribution style, sorting, and data skew
for all user-defined tables in the database. Here, "table" must be enclosed in
double quotation marks because it is a reserved word.

```
select "table", encoded, diststyle, sortkey1, skew_sortkey1, skew_rows
from svv_table_info
order by 1;

table          | encoded | diststyle       | sortkey1     | skew_sortkey1 | skew_rows
---------------+---------+-----------------+--------------+---------------+----------
category       | N       | EVEN            |              |               |
date           | N       | ALL             | dateid       |          1.00 |
event          | Y       | KEY(eventid)    | dateid       |          1.00 |      1.02
listing        | Y       | KEY(listid)     | dateid       |          1.00 |      1.01
sales          | Y       | KEY(listid)     | dateid       |          1.00 |      1.02
users          | Y       | KEY(userid)     | userid       |          1.00 |      1.01
venue          | N       | ALL             | venueid      |          1.00 |
(7 rows)
```
