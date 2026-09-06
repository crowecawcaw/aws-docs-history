

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_SYSTEM\_PRIVILEGES
<a name="r_SVV_SYSTEM_PRIVILEGES"></a>

SVV\_SYSTEM\_PRIVILEGES is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW GRANTS](r_SHOW_GRANTS.md) command for permission discovery. SHOW GRANTS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_SYSTEM_PRIVILEGES-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| system\_privilege | text | The name of the system permission. | 
| identity\_id | integer | The ID of the identity. Possible values are user ID or role ID. | 
| identity\_name | text | The name of the identity. | 
| identity\_type | text | The type of the identity. Possible values are user or role. | 

## Sample query
<a name="r_SVV_SYSTEM_PRIVILEGES-sample-query"></a>

The following example displays the result for the specified parameters.

```
SELECT system_privilege,identity_name,identity_type FROM svv_system_privileges
WHERE system_privilege = 'ALTER TABLE' AND identity_name = 'sys:superuser';

 system_privilege | identity_name | identity_type
------------------+---------------+---------------
   ALTER TABLE    | sys:superuser |     role
```