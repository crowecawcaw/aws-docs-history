Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_DATASHARE\_USAGE\_CONSUMER

Records the activity and usage of datashares. This view is only relevant on the
consumer cluster.

SYS\_DATASHARE\_USAGE\_CONSUMER is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name      | Data type    | Description                                              |
| ---------------- | ------------ | -------------------------------------------------------- |
| user\_id         | integer      | The ID of the user issuing the request.                  |
| session\_id      | integer      | The ID of the leader process running the query.          |
| transaction\_id  | bigint       | The context of the current transaction.                  |
| request\_id      | varchar(50)  | The unique ID of the requested API call.                 |
| request\_type    | varchar(25)  | The type of the request made to the producer<br>cluster. |
| transaction\_uid | varchar(50)  | The unique ID of the transaction.                        |
| record\_time     | timestamp    | The time when the action is recorded.                    |
| status           | integer      | The status of the requested API call.                    |
| error            | varchar(512) | The message for an error.                                |

## Sample queries

The following example shows the SYS\_DATASHARE\_USAGE\_CONSUMER view.

```
SELECT request_type, status, trim(error) AS error
FROM sys_datashare_usage_consumer

  request_type  | status | error_message
----------------+--------+---------------
 "GET RELATION" |   0    |
```
