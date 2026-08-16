Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_DATASHARE\_CROSS\_REGION\_USAGE

Use the SYS\_DATASHARE\_CROSS\_REGION\_USAGE view to get a summary of cross-Region data
transferred usage caused by cross-Region datasharing query.
SYS\_DATASHARE\_CROSS\_REGION\_USAGE aggregates details at the segment level.

SYS\_DATASHARE\_CROSS\_REGION\_USAGE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type     | Description                                                                                                             |
| ---------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------- |
| query\_id              | integer       | The ID of the query. Use this value to join other<br>system tables and views.                                           |
| child\_query\_sequence | integer       | The sequence of the rewritten user query, starting<br>with 1.                                                           |
| segment\_id            | bigint        | The number of the segment. A query consists of<br>multiple segments, and each segment consists of one or more<br>steps. |
| start\_time            | time          | The time in UTC that the data transfer<br>began.                                                                        |
| end\_time              | time          | The time in UTC that the data transfer<br>ended.                                                                        |
| transferred\_data      | bigint        | The number of bytes of data transferred from a<br>producer Region to a consumer Region.                                 |
| source\_region         | char(25)      | The producer Region that the query transferred<br>data from.                                                            |
| query\_uuid            | character(36) | A globally unique identifier (UUID) of the query.                                                                       |

## Sample queries

The following example shows a SYS\_DATASHARE\_CROSS\_REGION\_USAGE view.

```
SELECT query_id, segment_id, transferred_data, source_region
from sys_datashare_cross_region_usage
where query_id = pg_last_query_id()
order by query_id, segment_id;

  query_id | segment_id | transferred_data | source_region
-----------+------------+------------------+---------------
    200048 |          2 |          4194304 |    us-west-1
    200048 |          2 |          4194304 |    us-east-2
```
