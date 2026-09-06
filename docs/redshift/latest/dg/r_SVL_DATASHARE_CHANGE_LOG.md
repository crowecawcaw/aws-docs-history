

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_DATASHARE\_CHANGE\_LOG
<a name="r_SVL_DATASHARE_CHANGE_LOG"></a>

Records the consolidated view for tracking changes to datashares on both producer and consumer clusters.

SVL\_DATASHARE\_CHANGE\_LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_DATASHARE\_CHANGE\_LOG](SYS_DATASHARE_CHANGE_LOG.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_SVL_DATASHARE_CHANGE_LOG-table-rows"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | The ID of the user taking the action. | 
| username | varchar(128) | The name of the user taking the action. | 
| pid | integer | The ID of the process. | 
| xid | bigint | The ID of the transaction. | 
| share\_id | integer | The ID of the datashare affected. | 
| share\_name | varchar(128) | The name of the datashare. | 
| source\_database\_id | integer | The ID of the database to which the datashare belongs. | 
| source\_database\_name | varchar(128) | The name of the database to which the datashare belongs. | 
| consumer\_database\_id | integer | The ID of the database imported from the datashare. | 
| consumer\_database\_name | varchar(128) | The name of the database imported from the datashare. | 
| arn | varchar(192) | The ARN of the resource backing the imported database. | 
| recordtime | timestamp | The timestamp of the action. | 
| action | varchar(128) | The action being run. Possible values are CREATE DATASHARE, DROP DATASHARE, GRANT ALTER, REVOKE ALTER, GRANT SHARE, REVOKE SHARE, ALTER ADD, ALTER REMOVE, ALTER SET, GRANT USAGE, REVOKE USAGE, CREATE DATABASE, GRANT or REVOKE USAGE on a shared database, DROP SHARED DATABASE, ALTER SHARED DATABASE.  | 
| status | integer | The status of the action. Possible values are SUCCESS and ERROR-ERROR CODE. | 
| share\_object\_type | varchar(64) | The type of database object that was added to or removed from the datashare. Possible values are schemas, tables, columns, functions, and views. This is a field for the producer cluster. | 
| share\_object\_id | integer | The ID of database object that was added to or removed from the datashare. This is a field for the producer cluster. | 
| share\_object\_name | varchar(128) | The name of database object that was added to or removed from the datashare. This is a field for the producer cluster. | 
| target\_user\_type | varchar(16) | The type of users or groups that a privilege was granted to. This is a field for both the producer and consumer cluster. | 
| target\_userid  | integer | The ID of users or groups that a privilege was granted to. This is a field for both the producer and consumer cluster. | 
| target\_username | varchar(128) | The name of users or groups that a privilege was granted to. This is a field for both the producer and consumer cluster. | 
| consumer\_account | varchar(16) | The account ID of the data consumer. This is a field for the producer cluster. | 
| consumer\_namespace | varchar(64) | The namespace of the data consumer account. This is a field for the producer cluster. | 
| producer\_account | varchar(16) | The account ID of the producer account that the datashare belongs to. This is a field for the consumer cluster. | 
| producer\_namespace  | varchar(64) | The namespace of the product account that the datashare belongs to. This is a field for the consumer cluster. | 
| attribute\_name | varchar(64) | The name of an attribute of the datashare or shared database. | 
| attribute\_value | varchar(128) | The value of an attribute of the datashare or shared database. | 
| message | varchar(512) | The error message when an action fails. | 

## Sample queries
<a name="r_SVL_DATASHARE_CHANGE_LOG-sample-queries"></a>

The following example shows a SVL\_DATASHARE\_CHANGE\_LOG view.

```
SELECT DISTINCT action
FROM svl_datashare_change_log
WHERE share_object_name LIKE 'tickit%';

         action
 -----------------------
  "ALTER DATASHARE ADD"
```