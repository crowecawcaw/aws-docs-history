Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_ANALYZE_HISTORY

Logs details for [ANALYZE](r_ANALYZE.md "r_ANALYZE.md") operations.

SYS_ANALYZE_HISTORY is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name               | Data type | Description                                                                                                                                                              |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| user_id                   | integer   | The ID of the user who generated the<br>entry.                                                                                                                           |
| transaction_id            | long      | The transaction ID.                                                                                                                                                      |
| database_name             | char(30)  | The name of the database.                                                                                                                                                |
| table_name                | char(30)  | The name of the table.                                                                                                                                                   |
| table_id                  | integer   | The ID of the table.                                                                                                                                                     |
| is_automatic              | char(1)   | The value is true (t) if the operation included an<br>Amazon Redshift ANALYZE operation by default. The value is false (f) if the<br>ANALYZE command was run explicitly. |
| status                    | char(15)  | The result of the analyze command. Possible values<br>are Full, Skipped, and PredicateColumn.                                                                            |
| start_time                | timestamp | The time in UTC of when the ANALYZE operation<br>started running.                                                                                                        |
| end_time                  | timestamp | The time in UTC of when the ANALYZE operation<br>finished running.                                                                                                       |
| rows                      | double    | The total number of rows in the table                                                                                                                                    |
| modified_rows             | double    | The total number of rows that were modified since<br>the last ANALYZE operation.                                                                                         |
| analyze_threshold_percent | integer   | The value of the analyze_threshold_percent<br>parameter.                                                                                                                 |
| last_analyze_time         | timestamp | The time in UTC of when the table was previously<br>analyzed.                                                                                                            |

## Sample queries

```

 user_id | transaction_id | database_name | schema_name |      table_name     | table_id | is_automatic | Status |         start_time         |          end_time          | rows | modified_rows | analyze_threshold_percent |  last_analyze_time
---------+----------------+---------------+-------------+---------------------+----------+--------------+--------+----------------------------+----------+-----------------+------+---------------+---------------------------+---------------------
     101 |           8006 |           dev |      public | test_table_562bf8dc |   110427 |            f |   Full | 2023-09-21 18:33:08.504646 | 2023-09-21 18:33:24.296498 |    5 |             5 |                         0 | 2000-01-01 00:00:00

```
