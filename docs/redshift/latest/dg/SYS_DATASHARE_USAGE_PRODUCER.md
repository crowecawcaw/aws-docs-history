Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_DATASHARE_USAGE_PRODUCER

Records the activity and usage of datashares. This view is only relevant on the
producer cluster.

SYS_DATASHARE_USAGE_PRODUCER is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type    | Description                                                                                                                 |
| ------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| share_id                 | integer      | The object ID (OID) of the datashare.                                                                                       |
| share_name               | varchar(128) | The name of the datashare.                                                                                                  |
| request_id               | varchar(50)  | The unique ID of the requested API call.                                                                                    |
| request_type             | varchar(25)  | The type of the request made to the producer cluster.                                                                       |
| object_type              | varchar(64)  | The type of the object being shared from the datashare. Possible values are schemas, tables, columns, functions, and views. |
| object_oid               | integer      | The ID of the object being shared from the datashare.                                                                       |
| object_name              | varchar(128) | The name of the object being shared from the datashare.                                                                     |
| consumer_account         | varchar(16)  | The account of the consumer account that the datashare is shared to.                                                        |
| consumer_namespace       | varchar(64)  | The namespace of the consumer account that the datashare is shared to.                                                      |
| consumer_transaction_uid | varchar(50)  | The unique transaction ID of the statement on the consumer cluster.                                                         |
| record_time              | timestamp    | The time when the action is recorded.                                                                                       |
| status                   | integer      | The status of the datashare.                                                                                                |
| error_message            | varchar(512) | The message for an error.                                                                                                   |
| consumer_region          | char(64)     | The Region that the consumer cluster is in.                                                                                 | ## Sample queries The following example shows the SYS_DATASHARE_USAGE_PRODUCER view. `SELECT DISTINCT FROM sys_datashare_usage_producer WHERE object_name LIKE 'tickit%'; request_type ------------------ "GET RELATION"` |
