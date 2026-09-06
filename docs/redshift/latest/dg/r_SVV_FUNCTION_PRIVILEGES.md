

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_FUNCTION\_PRIVILEGES
<a name="r_SVV_FUNCTION_PRIVILEGES"></a>

Use SVV\_FUNCTION\_PRIVILEGES to view the function permissions that are explicitly granted to users, roles, and groups in the current database.

SVV\_FUNCTION\_PRIVILEGES is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW GRANTS](r_SHOW_GRANTS.md) command for permission discovery. SHOW GRANTS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_FUNCTION_PRIVILEGES-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| namespace\_name | text | The name of the namespace where a specified function exists. | 
| function\_name | text | The name of the function. | 
| argument\_types | text | The string that represents the type of input argument for a function. | 
| privilege\_type | text | The type of the permission. Possible value is EXECUTE. | 
| identity\_id | integer | The ID of the identity. Possible values are user ID, role ID, or group ID. | 
| identity\_name | text | The name of the identity. | 
| identity\_type | text | The type of the identity. Possible values are user, role, group, or public. | 
| admin\_option | boolean | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | 

## Sample query
<a name="r_SVV_FUNCTION_PRIVILEGES-sample-query"></a>

The following example displays the result of the SVV\_FUNCTION\_PRIVILEGES.

```
SELECT namespace_name,function_name,argument_types,privilege_type,identity_name,identity_type,admin_option FROM svv_function_privileges
WHERE identity_name IN ('role1', 'reguser');

 namespace_name | function_name |       argument_types       | privilege_type |  identity_name | identity_type | admin_option
----------------+---------------+----------------------------+----------------+----------------+---------------+--------------
    public      | test_func1    | integer                    |    EXECUTE     |      role1     |     role      |  False
    public      | test_func2    | integer, character varying |    EXECUTE     |     reguser    |     user      |  False
```