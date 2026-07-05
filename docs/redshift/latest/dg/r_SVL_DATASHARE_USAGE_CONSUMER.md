Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVL\_DATASHARE\_USAGE\_CONSUMER

Records the activity and usage of datashares. This view is only relevant on the consumer cluster.

SVL\_DATASHARE\_USAGE\_CONSUMER is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_DATASHARE\_USAGE\_CONSUMER](SYS_DATASHARE_USAGE_CONSUMER.md "SYS_DATASHARE_USAGE_CONSUMER.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name      | Data type    | Description                                              |
| ---------------- | ------------ | -------------------------------------------------------- |
| userid           | integer      | The ID of the user issuing the request.                  |
| pid              | integer      | The ID of the leader process running the query.          |
| xid              | bigint       | The context of the current transaction.                  |
| request\_id      | varchar(50)  | The unique ID of the requested API call.                 |
| request\_type    | varchar(25)  | The type of the request made to the producer<br>cluster. |
| transaction\_uid | varchar(50)  | The unique ID of the transaction.                        |
| recordtime       | timestamp    | The time when the action is recorded.                    |
| status           | integer      | The status of the requested API call.                    |
| error            | varchar(512) | The message for an error.                                |

## Sample queries

The following example shows a SVL\_DATASHARE\_USAGE\_CONSUMER view.

```
SELECT request_type, status, trim(error) AS error
FROM svl_datashare_usage_consumer

  request_type  | status | error
----------------+--------+--------
 "GET RELATION" |   0    |
```
