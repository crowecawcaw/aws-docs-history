

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_USER\_INFO
<a name="r_SVV_USER_INFO"></a>

You can retrieve data about Amazon Redshift database users with the SVV\_USER\_INFO view.

SVV\_USER\_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SVV_USER_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_name  | text  | The user name for the role.  | 
| user\_id | integer | The user ID for the user. | 
| createdb | boolean | A value that indicates whether the user has permissions to create databases.  | 
| superuser | boolean | A value that indicates whether the user is a superuser. | 
| catalog\_update | boolean | A value that indicates whether the user can update system catalogs.  | 
| connection\_limit | text  | The number of connections that the user can open. | 
| syslog\_access  | text  | A value that indicates whether the user has access to the system logs. The two possible values are RESTRICTED and UNRESTRICTED. RESTRICTED means that users that are not superusers can see their own records. UNRESTRICTED means that user that are not superusers can see all records in the system views and tables to which they have SELECT privileges.  | 
| last\_ddl\_timestamp | timestamp | The timestamp for the last data definition language (DDL) create statement run by the user.  | 
| session\_timeout | integer | The maximum time in seconds that a session remains inactive or idle before timing out. 0 indicates that no timeout is set. For information about the cluster's idle or inactive timeout setting, see [ Quotas and limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the Amazon Redshift Management Guide. | 
| external\_user\_id | text | Unique identifier of the user in the third-party identity provider. | 

## Sample queries
<a name="SVV_USER_INFO-sample-queries"></a>

The following command retrieves user information from SVV\_USER\_INFO.

```
SELECT * FROM SVV_USER_INFO;
```