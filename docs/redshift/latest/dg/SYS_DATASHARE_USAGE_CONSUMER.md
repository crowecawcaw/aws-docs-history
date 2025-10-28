Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_DATASHARE_USAGE_CONSUMER

Records the activity and usage of datashares. This view is only relevant on the
consumer cluster.

SYS_DATASHARE_USAGE_CONSUMER is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type    | Description                                           |
| --------------- | ------------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------- | --- | --- |
| user_id         | integer      | The ID of the user issuing the request.               |
| session_id      | integer      | The ID of the leader process running the query.       |
| transaction_id  | bigint       | The context of the current transaction.               |
| request_id      | varchar(50)  | The unique ID of the requested API call.              |
| request_type    | varchar(25)  | The type of the request made to the producer cluster. |
| transaction_uid | varchar(50)  | The unique ID of the transaction.                     |
| record_time     | timestamp    | The time when the action is recorded.                 |
| status          | integer      | The status of the requested API call.                 |
| error_message   | varchar(512) | The message for an error.                             | ## Sample queries The following example shows the SYS_DATASHARE_USAGE_CONSUMER view. ``` SELECT request_type, status, trim(error) AS error FROM sys_datashare_usage_consumer request_type | status | error_message ----------------+--------+--------------- "GET RELATION" | 0   | ``` |
