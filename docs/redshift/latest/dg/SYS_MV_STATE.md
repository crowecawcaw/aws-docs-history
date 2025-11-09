Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_MV_STATE

The results include information about the state of all materialized views. It includes
base table information, schema properties, and information about recent events, like
dropping a column.

SYS_MV_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type     | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id                  | bigint        | The ID of the user who created the event.                                                                                                                                                                                                                                                                           |
| transaction_id           | bigint        | The transaction ID of the event.                                                                                                                                                                                                                                                                                    |
| database_name            | char(128)     | The database that contains the materialized<br>view.                                                                                                                                                                                                                                                                |
| event_desc               | char(500)     | The event that prompted the state change. Example<br>values include the following:<br>• Column type was changed<br>• Column was dropped<br>• Column was renamed<br>• Schema name was changed<br>• Small-table conversion<br>• TRUNCATE<br>• Vacuum<br>Note that there are other possible values for this<br>column. |
| start_time               | timestamp     | The start time of the event.                                                                                                                                                                                                                                                                                        |
| base_table_database_name | char(128)     | The database name for the base table.                                                                                                                                                                                                                                                                               |
| base_table_schema        | char(128)     | The schema of the base table.                                                                                                                                                                                                                                                                                       |
| base_table_name          | char(128)     | The name of the base table.                                                                                                                                                                                                                                                                                         |
| mv_schema                | char(128)     | The schema of the materialized view.                                                                                                                                                                                                                                                                                |
| mv_name                  | char(128)     | The name of the materialized view.                                                                                                                                                                                                                                                                                  |
| state                    | character(32) | The changed state of the materialized view, which<br>are as follows:<br>• Recompute<br>• Unrefreshable                                                                                                                                                                                                              |

## Sample queries

The following query shows the materialized view state.

```
select * from sys_mv_state;
```

The query returns the following sample output:

```
 user_id | transaction_id | database_name | event_desc                  | start_time                 | base_table_database_name | base_table_schema | base_table_name     |  mv_schema  | mv_name                    | state
---------+----------------+---------------+-----------------------------+----------------------------+--------------------------+-------------------+---------------------+-------------+----------------------------+--------------
 106     | 12720          | tickit_db     | TRUNCATE                    | 2023-07-26 14:59:12.788268 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_a1f3f862 | Recompute
 106     | 12724          | tickit_db     | ALTER TABLE ALTER DISTSTYLE | 2023-07-26 14:59:51.409014 | tickit_db                | mv_schema         | test_table_58102435 | mv_schema   | materialized_view_ca746631 | Recompute
 106     | 12720          | tickit_db     | Column was renamed          | 2023-07-26 14:59:12.822928 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5750a8d4 | Unrefreshable
 106     | 12727          | tickit_db     | Table was renamed           | 2023-07-26 15:00:08.051244 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5750a8d4 | Unrefreshable
 106     | 12720          | tickit_db     | Column was renamed          | 2023-07-26 14:59:12.857755 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5750a8d4 | Unrefreshable
 106     | 12727          | tickit_db     | Table was renamed           | 2023-07-26 15:00:08.051358 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5ef0d754 | Unrefreshable
 106     | 12720          | tickit_db     | TRUNCATE                    | 2023-07-26 14:59:12.788159 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5750a8d4 | Recompute
 106     | 12720          | tickit_db     | Column was renamed          | 2023-07-26 14:59:12.857799 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_a1f3f862 | Unrefreshable
 106     | 12720          | tickit_db     | TRUNCATE                    | 2023-07-26 14:59:12.788327 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_5ef0d754 | Recompute
 106     | 12727          | tickit_db     | ALTER TABLE ALTER SORTKEY   | 2023-07-26 15:00:08.006235 | tickit_db                | mv_schema         | test_table_58102435 | mv_schema   | materialized_view_ca746631 | Recompute
 106     | 12720          | tickit_db     | Column was renamed          | 2023-07-26 14:59:12.82297  | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_a1f3f862 | Unrefreshable
 106     | 12727          | tickit_db     | Table was renamed           | 2023-07-26 15:00:08.051321 | tickit_db                | mv_schema         | test_table_95d6d861 | mv_schema   | materialized_view_a1f3f862 | Unrefreshable
```
