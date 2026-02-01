Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_DATASHARE_CROSS_REGION_USAGE

Use the SVL_DATASHARE_CROSS_REGION_USAGE view to get a summary of cross-Region data
transferred usage caused by cross-Region datasharing query.
SVL_DATASHARE_CROSS_REGION_USAGE aggregates details at the segment level.

SVL_DATASHARE_CROSS_REGION_USAGE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_DATASHARE_CROSS_REGION_USAGE](r_SYS_DATASHARE_CROSS_REGION_USAGE.md "r_SYS_DATASHARE_CROSS_REGION_USAGE.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name      | Data type | Description                                                                                                       |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------- |
| query            | integer   | The ID of the query. Use this value to join other system tables and views.                                        |
| segment          | bigint    | The number of the segment. A query consists of multiple segments, and each segment consists of one or more steps. |
| start_time       | time      | The time in UTC that the data transfer<br>began.                                                                  |
| end_time         | time      | The time in UTC that the data transfer<br>ended.                                                                  |
| transferred_data | bigint    | The number of bytes of data transferred from a producer Region to a consumer Region.                              |
| source_region    | char(25)  | The producer Region that the query transferred data from.                                                         |
| recordtime       | timestamp | The time when the action is recorded.                                                                             |

## Sample queries

The following example shows a SVL_DATASHARE_CROSS_REGION_USAGE view.

```
SELECT query, segment, transferred_data, source_region
from svl_datashare_cross_region_usage
where query = pg_last_query_id()
order by query,segment;

  query | segment | transferred_data | source_region
--------+---------+------------------+---------------
 200048 |       2 |          4194304 |    us-west-1
 200048 |       2 |          4194304 |    us-east-2
```
