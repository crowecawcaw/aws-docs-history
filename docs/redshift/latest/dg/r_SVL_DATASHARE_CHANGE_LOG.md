Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_DATASHARE_CHANGE_LOG

Records the consolidated view for tracking changes to datashares on both producer and
consumer clusters.

SVL_DATASHARE_CHANGE_LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_DATASHARE_CHANGE_LOG](SYS_DATASHARE_CHANGE_LOG.md "SYS_DATASHARE_CHANGE_LOG.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name            | Data type    | Description                                                                                                                                                                                                                                                                                                |
| ---------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                 | integer      | The ID of the user taking the action.                                                                                                                                                                                                                                                                      |
| username               | varchar(128) | The name of the user taking the action.                                                                                                                                                                                                                                                                    |
| pid                    | integer      | The ID of the process.                                                                                                                                                                                                                                                                                     |
| xid                    | bigint       | The ID of the transaction.                                                                                                                                                                                                                                                                                 |
| share_id               | integer      | The ID of the datashare affected.                                                                                                                                                                                                                                                                          |
| share_name             | varchar(128) | The name of the datashare.                                                                                                                                                                                                                                                                                 |
| source_database_id     | integer      | The ID of the database to which the datashare<br>belongs.                                                                                                                                                                                                                                                  |
| source_database_name   | varchar(128) | The name of the database to which the datashare<br>belongs.                                                                                                                                                                                                                                                |
| consumer_database_id   | integer      | The ID of the database imported from the<br>datashare.                                                                                                                                                                                                                                                     |
| consumer_database_name | varchar(128) | The name of the database imported from the<br>datashare.                                                                                                                                                                                                                                                   |
| arn                    | varchar(192) | The ARN of the resource backing the imported database.                                                                                                                                                                                                                                                     |
| recordtime             | timestamp    | The timestamp of the action.                                                                                                                                                                                                                                                                               |
| action                 | varchar(128) | The action being run. Possible values are CREATE DATASHARE, DROP DATASHARE, GRANT ALTER, REVOKE ALTER, GRANT SHARE, REVOKE SHARE, ALTER ADD, ALTER REMOVE, ALTER SET, GRANT USAGE, REVOKE USAGE, CREATE DATABASE, GRANT or REVOKE USAGE on a shared database, DROP SHARED DATABASE, ALTER SHARED DATABASE. |
| status                 | integer      | The status of the action. Possible values are<br>SUCCESS and ERROR-ERROR CODE.                                                                                                                                                                                                                             |
| share_object_type      | varchar(64)  | The type of database object that was added to or<br>removed from the datashare. Possible values are schemas, tables,<br>columns, functions, and views. This is a field for the producer<br>cluster.                                                                                                        |
| share_object_id        | integer      | The ID of database object that was added to or<br>removed from the datashare. This is a field for the producer<br>cluster.                                                                                                                                                                                 |
| share_object_name      | varchar(128) | The name of database object that was added to or<br>removed from the datashare. This is a field for the producer<br>cluster.                                                                                                                                                                               |
| target_user_type       | varchar(16)  | The type of users or groups that a privilege was<br>granted to. This is a field for both the producer and consumer<br>cluster.                                                                                                                                                                             |
| target_userid          | integer      | The ID of users or groups that a privilege was<br>granted to. This is a field for both the producer and consumer<br>cluster.                                                                                                                                                                               |
| target_username        | varchar(128) | The name of users or groups that a privilege was<br>granted to. This is a field for both the producer and consumer<br>cluster.                                                                                                                                                                             |
| consumer_account       | varchar(16)  | The account ID of the data consumer. This is a<br>field for the producer cluster.                                                                                                                                                                                                                          |
| consumer_namespace     | varchar(64)  | The namespace of the data consumer account. This<br>is a field for the producer cluster.                                                                                                                                                                                                                   |
| producer_account       | varchar(16)  | The account ID of the producer account that the<br>datashare belongs to. This is a field for the consumer<br>cluster.                                                                                                                                                                                      |
| producer_namespace     | varchar(64)  | The namespace of the product account that the<br>datashare belongs to. This is a field for the consumer<br>cluster.                                                                                                                                                                                        |
| attribute_name         | varchar(64)  | The name of an attribute of the datashare or<br>shared database.                                                                                                                                                                                                                                           |
| attribute_value        | varchar(128) | The value of an attribute of the datashare or<br>shared database.                                                                                                                                                                                                                                          |
| message                | varchar(512) | The error message when an action fails.                                                                                                                                                                                                                                                                    |

## Sample queries

The following example shows a SVL_DATASHARE_CHANGE_LOG view.

```
SELECT DISTINCT action
FROM svl_datashare_change_log
WHERE share_object_name LIKE 'tickit%';

         action
 -----------------------
  "ALTER DATASHARE ADD"
```
