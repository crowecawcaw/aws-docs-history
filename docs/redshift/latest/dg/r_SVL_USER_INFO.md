

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_USER\_INFO
<a name="r_SVL_USER_INFO"></a>

You can retrieve data about Amazon Redshift database users with the SVL\_USER\_INFO view.

SVL\_USER\_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SVL_USER_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| usename  | text  | The user name for the role.  | 
| usesysid | integer | The user ID for the user. | 
| usecreatedb | boolean | A value that indicates whether the user has permissions to create databases.  | 
| usesuper | boolean | A value that indicates whether the user is a superuser. | 
| usecatupd | boolean | A value that indicates whether the user can update system catalogs.  | 
| useconnlimit  | text  | The number of connections that the user can open. | 
| syslogaccess  | text  | A value that indicates whether the user has access to the system logs. The two possible values are RESTRICTED and UNRESTRICTED. RESTRICTED means that users that are not superusers can see their own records. UNRESTRICTED means that user that are not superusers can see all records in the system views and tables to which they have SELECT privileges.  | 
| last\_ddl\_ts | timestamp | The timestamp for the last data definition language (DDL) create statement run by the user.  | 
| sessiontimeout | integer | The maximum time in seconds that a session remains inactive or idle before timing out. 0 indicates that no timeout is set. For information about the cluster's idle or inactive timeout setting, see [ Quotas and limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the Amazon Redshift Management Guide. | 
| external\_id | text | Unique identifier of the user in the third-party identity provider. | 

## Sample queries
<a name="SVL_USER_INFO-sample-queries"></a>

The following command retrieves user information from SVL\_USER\_INFO.

```
SELECT * FROM SVL_USER_INFO;
```