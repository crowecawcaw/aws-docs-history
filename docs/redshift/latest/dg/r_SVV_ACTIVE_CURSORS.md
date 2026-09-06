

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ACTIVE\_CURSORS
<a name="r_SVV_ACTIVE_CURSORS"></a>

SVV\_ACTIVE\_CURSORS displays details for currently open cursors. For more information, see [DECLARE](declare.md). 

SVV\_ACTIVE\_CURSORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data). A user can only view cursors opened by that user. A superuser can view all cursors.

## Table columns
<a name="r_SVV_ACTIVE_CURSORS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The ID of the user who created the cursor. | 
| cursor\_name | varchar(128) | The name of the cursor. | 
| transaction\_id | bigint(128) | The ID of the transaction. | 
| session\_id | integer | The ID of the process with the active cursor. | 
| declare\_time | timestamp | The time the cursor was declared. | 
| total\_bytes | bigint | The size of the cursor result set, in bytes. | 
| total\_rows | bigint | The number of rows in the cursor result set. | 
| fetched\_rows | bigint | The number of rows currently fetched from the cursor result set. | 
| cursor\_storage\_limit\_used\_percent | integer | The percentage of disk space currently used by the cursor. | 