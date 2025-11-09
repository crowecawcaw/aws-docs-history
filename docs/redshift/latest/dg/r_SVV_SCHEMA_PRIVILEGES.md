Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_SCHEMA_PRIVILEGES

Use SVV_SCHEMA_PRIVILEGES to view the schema permissions that are explicitly granted
to users, roles, and groups in the current database.

SVV_SCHEMA_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name     | Data type | Description                                                                                                                                                                                                                                                         |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namespace_name  | text      | The name of the namespace where a specified schema<br>exists.                                                                                                                                                                                                       |
| privilege_type  | text      | The type of the permission. For permissions with a privilege_scope<br>of schema, possible values are CREATE, USAGE, and ALTER. For privilege_scope values<br>other than schema, possible values include any permission type available on the permission's<br>scope. |
| identity_id     | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID.                                                                                                                                                                                          |
| identity_name   | text      | The name of the identity.                                                                                                                                                                                                                                           |
| identity_type   | text      | The type of the identity. Possible values are user, role, group, or public.                                                                                                                                                                                         |
| admin_option    | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type.                                                                                                           |
| privilege_scope | text      | The scope of the permission specified<br>in privilege_type. Possible values are as follows:<br>• SCHEMA<br>• TABLES<br>• FUNCTIONS<br>For information on scoped permissions, go to [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").         |

## Sample query

The following example displays the result of the SVV_SCHEMA_PRIVILEGES.

```
SELECT namespace_name,privilege_type,identity_name,identity_type,admin_option FROM svv_schema_privileges
WHERE namespace_name = 'test_schema1';

 namespace_name | privilege_type |  identity_name | identity_type | admin_option
----------------+----------------+----------------+---------------+--------------
 test_schema1   |    USAGE       |     reguser    |     user      |   False
 test_schema1   |    USAGE       |     role1      |     role      |   False
```
