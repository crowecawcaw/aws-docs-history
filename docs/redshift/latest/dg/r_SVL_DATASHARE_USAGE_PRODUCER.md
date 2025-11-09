Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_DATASHARE_USAGE_PRODUCER

Records the activity and usage of datashares. This view is only relevant on the
producer cluster.

SVL_DATASHARE_USAGE_PRODUCER is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_DATASHARE_USAGE_PRODUCER](SYS_DATASHARE_USAGE_PRODUCER.md "SYS_DATASHARE_USAGE_PRODUCER.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name              | Data type    | Description                                                                                                                       |
| ------------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| share_id                 | integer      | The object ID (OID) of the datashare.                                                                                             |
| share_name               | varchar(128) | The name of the datashare.                                                                                                        |
| request_id               | varchar(50)  | The unique ID of the requested API call.                                                                                          |
| request_type             | varchar(25)  | The type of the request made to the producer cluster.                                                                             |
| object_type              | varchar(64)  | The type of the object being shared from the<br>datashare. Possible values are schemas, tables, columns, functions,<br>and views. |
| object_oid               | integer      | The ID of the object being shared from the<br>datashare.                                                                          |
| object_name              | varchar(128) | The name of the object being shared from the<br>datashare.                                                                        |
| consumer_account         | varchar(16)  | The account of the consumer account that the<br>datashare is shared to.                                                           |
| consumer_namespace       | varchar(64)  | The namespace of the consumer account that the<br>datashare is shared to.                                                         |
| consumer_transaction_uid | varchar(50)  | The unique transaction ID of the statement on the consumer cluster.                                                               |
| recordtime               | timestamp    | The time when the action is recorded.                                                                                             |
| status                   | integer      | The status of the datashare.                                                                                                      |
| error                    | varchar(512) | The message for an error.                                                                                                         |
| consumer_region          | char(64)     | The Region that the consumer cluster is in.                                                                                       |

## Sample queries

The following example shows a SVL_DATASHARE_USAGE_PRODUCER view.

```
SELECT DISTINCT request_type
FROM svl_datashare_usage_producer
WHERE object_name LIKE 'tickit%';

   request_type
 ------------------
   "GET RELATION"
```
