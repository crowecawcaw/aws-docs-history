Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_MV_STATE

The STL_MV_STATE view contains a row for every state transition of a materialized
view.

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").

STL_MV_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_MV_STATE](SYS_MV_STATE.md "SYS_MV_STATE.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name       | Data type     | Description                                                                                                                                                                                                                                                                                                           |
| ----------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid            | bigint        | The ID of the user who created the event.                                                                                                                                                                                                                                                                             |
| starttime         | timestamp     | The start time of the event.                                                                                                                                                                                                                                                                                          |
| xid               | bigint        | The transaction id of the event.                                                                                                                                                                                                                                                                                      |
| event_desc        | char(500)     | The event that prompted the state change. Some example<br>values include the following:<br>• Column type was changed<br>• Column was dropped<br>• Column was renamed<br>• Schema name was changed<br>• Small table conversion<br>• TRUNCATE<br>• Vacuum<br>Note that there are other possible values for this column. |
| db_name           | char(128)     | The database that contains the materialized view.                                                                                                                                                                                                                                                                     |
| base_table_schema | char(128)     | The schema of the base table.                                                                                                                                                                                                                                                                                         |
| base_table_name   | char(128)     | The name of the base table.                                                                                                                                                                                                                                                                                           |
| mv_schema         | char(128)     | The schema of the materialized view.                                                                                                                                                                                                                                                                                  |
| mv_name           | char(128)     | The name of the materialized view.                                                                                                                                                                                                                                                                                    |
| state             | character(32) | The changed state of the materialized view as follows:<br>• Recompute<br>• Unrefreshable                                                                                                                                                                                                                              |

The following table shows example combinations of `event_desc` and `state`.

```

          event_desc     |     state
-------------------------+---------------
 TRUNCATE                | Recompute
 TRUNCATE                | Recompute
 Small table conversion  | Recompute
 Vacuum                  | Recompute
 Column was renamed      | Unrefreshable
 Column was dropped      | Unrefreshable
 Table was renamed       | Unrefreshable
 Column type was changed | Unrefreshable
 Schema name was changed | Unrefreshable

```

## Sample query

To view the log of state transitions of materialized views, run the following query.

```
select * from stl_mv_state;
```

This query returns the following sample output:

```

 userid |         starttime          | xid  |            event_desc       | db_name |  base_table_schema   |   base_table_name    |      mv_schema       | mv_name       |     state
--------+----------------------------+------+-----------------------------+---------+----------------------+----------------------+----------------------+---------------+---------------
    138 | 2020-02-14 02:21:25.578885 | 5180 | TRUNCATE                    | dev     | public               | mv_base_table        | public               | mv_test       | Recompute
    138 | 2020-02-14 02:21:56.846774 | 5275 | Column was dropped          | dev     |                      | mv_base_table        | public               | mv_test       | Unrefreshable
    100 | 2020-02-13 22:09:53.041228 | 1794 | Column was renamed          | dev     |                      | mv_base_table        | public               | mv_test       | Unrefreshable
      1 | 2020-02-13 22:10:23.630914 | 1893 | ALTER TABLE ALTER SORTKEY   | dev     | public               | mv_base_table_sorted | public               | mv_test       | Recompute
      1 | 2020-02-17 22:57:22.497989 | 8455 | ALTER TABLE ALTER DISTSTYLE | dev     | public               | mv_base_table        | public               | mv_test       | Recompute
    173 | 2020-02-17 22:57:23.591434 | 8504 | Table was renamed           | dev     |                      | mv_base_table        | public               | mv_test       | Unrefreshable
    173 | 2020-02-17 22:57:27.229423 | 8592 | Column type was changed     | dev     |                      | mv_base_table        | public               | mv_test       | Unrefreshable
    197 | 2020-02-17 22:59:06.212569 | 9668 | TRUNCATE                    | dev     | schemaf796e415850f4f | mv_base_table        | schemaf796e415850f4f | mv_test       | Recompute
    138 | 2020-02-14 02:21:55.705655 | 5226 | Column was renamed          | dev     |                      | mv_base_table        | public               | mv_test       | Unrefreshable
      1 | 2020-02-14 02:22:26.292434 | 5325 | ALTER TABLE ALTER SORTKEY   | dev     | public               | mv_base_table_sorted | public               | mv_test       | Recompute

```
