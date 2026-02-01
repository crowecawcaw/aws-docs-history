Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_STATISTIC_INDICATOR

Stores information about the number of rows inserted or deleted since the last
ANALYZE. The PG_STATISTIC_INDICATOR table is updated frequently following DML
operations, so statistics are approximate.

PG_STATISTIC_INDICATOR is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type | Description                                                  |
| ----------- | --------- | ------------------------------------------------------------ |
| stairelid   | oid       | Table ID                                                     |
| stairows    | float     | Total number of rows in the table.                           |
| staiins     | float     | Number of rows inserted since the last<br>ANALYZE.           |
| staidels    | float     | Number of rows deleted or updated since the last<br>ANALYZE. |

## Example

The following example returns information for table changes since the last
ANALYZE.

```
select * from pg_statistic_indicator;

stairelid | stairows | staiins | staidels
----------+----------+---------+---------
   108271 |       11 |       0 |        0
   108275 |      365 |       0 |        0
   108278 |     8798 |       0 |        0
   108280 |    91865 |       0 |   100632
   108267 |    89981 |   49990 |     9999
   108269 |      808 |     606 |      374
   108282 |   152220 |   76110 |   248566

```
