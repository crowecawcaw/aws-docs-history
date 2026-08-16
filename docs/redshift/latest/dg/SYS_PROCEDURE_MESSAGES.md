Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_PROCEDURE\_MESSAGES

SYS\_PROCEDURE\_MESSAGES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type     | Description                                                                                               |
| --------------- | ------------- | --------------------------------------------------------------------------------------------------------- |
| transaction\_id | bigint        | The transaction identifier.                                                                               |
| query\_id       | integer       | The query identifier of the stored procedure<br>call.                                                     |
| record\_time    | timestamp     | The time in UTC when the message was<br>generated.                                                        |
| log\_level      | char(10)      | The log level of the generated message. Possible<br>values are LOG, INFO, NOTICE, WARNING, and EXCEPTION. |
| message         | char(1024)    | The text of the generated message.                                                                        |
| line\_number    | integer       | The line number of the generated message.                                                                 |
| query\_uuid     | character(36) | A globally unique identifier (UUID) of the query.                                                         |

## Sample queries

The following query shows sample output of SYS\_PROCEDURE\_MESSAGES.

```
select transaction_id, query_id, record_time, log_level, trim(message), line_number from sys_procedure_messages;
```

```
transaction_id | query_id |        record_time         | log_level |           btrim           | line_number
---------------+----------+----------------------------+-----------+---------------------------+-------------
     25267     |   80562  | 2023-07-17 14:38:31.910136 |   NOTICE  | test_notice_msg_b9f1e749  |     8
     25267     |   80562  | 2023-07-17 14:38:31.910002 |    LOG    |  test_log_msg_833c7420    |     6
     25267     |   80562  | 2023-07-17 14:38:31.910111 |    INFO   |  test_info_msg_651373d9   |     7
     25267     |   80562  | 2023-07-17 14:38:31.910154 |   WARNING | test_warning_msg_831c5747 |     9
(4 rows)
```
