Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_PROCEDURE_MESSAGES

SYS_PROCEDURE_MESSAGES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type  | Description                                                                                            |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------- | --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------- | ----- | -------------------------- | ------ | ------------------------ | ------- | ----- | -------------------------- | --- | --------------------- | ------- | ----- | -------------------------- | ---- | ---------------------- | ------- | ----- | -------------------------- | ------- | ------------------------- | -------------- |
| transaction_id | bigint     | The transaction identifier.                                                                            |
| query_id       | integer    | The query identifier of the stored procedure call.                                                     |
| record_time    | timestamp  | The time in UTC when the message was generated.                                                        |
| log_level      | char(10)   | The log level of the generated message. Possible values are LOG, INFO, NOTICE, WARNING, and EXCEPTION. |
| message        | char(1024) | The text of the generated message.                                                                     |
| line_number    | integer    | The line number of the generated message.                                                              | ## Sample queries The following query shows sample output of SYS_PROCEDURE_MESSAGES. `select transaction_id, query_id, record_time, log_level, trim(message), line_number from sys_procedure_messages;` ``` transaction_id | query_id | record_time | log_level | btrim | line_number ---------------+----------+----------------------------+-----------+---------------------------+------------- 25267 | 80562 | 2023-07-17 14:38:31.910136 | NOTICE | test_notice_msg_b9f1e749 | 8 25267 | 80562 | 2023-07-17 14:38:31.910002 | LOG | test_log_msg_833c7420 | 6 25267 | 80562 | 2023-07-17 14:38:31.910111 | INFO | test_info_msg_651373d9 | 7 25267 | 80562 | 2023-07-17 14:38:31.910154 | WARNING | test_warning_msg_831c5747 | 9 (4 rows) ``` |
