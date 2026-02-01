Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_FUNCTION_PRIVILEGES

Use SVV_FUNCTION_PRIVILEGES to view the function permissions that are explicitly
granted to users, roles, and groups in the current database.

SVV_FUNCTION_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name    | Data type | Description                                                                                                                                               |
| -------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namespace_name | text      | The name of the namespace where a specified<br>function exists.                                                                                           |
| function_name  | text      | The name of the function.                                                                                                                                 |
| argument_types | text      | The string that represents the type of input<br>argument for a function.                                                                                  |
| privilege_type | text      | The type of the permission. Possible value is<br>EXECUTE.                                                                                                 |
| identity_id    | integer   | The ID of the identity. Possible values are user<br>ID, role ID, or group ID.                                                                             |
| identity_name  | text      | The name of the identity.                                                                                                                                 |
| identity_type  | text      | The type of the identity. Possible values are<br>user, role, group, or public.                                                                            |
| admin_option   | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type. |

## Sample query

The following example displays the result of the SVV_FUNCTION_PRIVILEGES.

```
SELECT namespace_name,function_name,argument_types,privilege_type,identity_name,identity_type,admin_option FROM svv_function_privileges
WHERE identity_name IN ('role1', 'reguser');

 namespace_name | function_name |       argument_types       | privilege_type |  identity_name | identity_type | admin_option
----------------+---------------+----------------------------+----------------+----------------+---------------+--------------
    public      | test_func1    | integer                    |    EXECUTE     |      role1     |     role      |  False
    public      | test_func2    | integer, character varying |    EXECUTE     |     reguser    |     user      |  False
```
