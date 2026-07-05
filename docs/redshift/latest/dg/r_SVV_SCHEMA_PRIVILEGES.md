Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_SCHEMA\_PRIVILEGES

Use SVV\_SCHEMA\_PRIVILEGES to view the schema permissions that are explicitly granted
to users, roles, and groups in the current database.

SVV\_SCHEMA\_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW GRANTS](r_SHOW_GRANTS.md "r_SHOW_GRANTS.md") command for permission discovery. SHOW GRANTS works consistently
across local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name      | Data type | Description                                                                                                                                                                                                                                                           |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namespace\_name  | text      | The name of the namespace where a specified schema<br>exists.                                                                                                                                                                                                         |
| privilege\_type  | text      | The type of the permission. For permissions with a privilege\_scope<br>of schema, possible values are CREATE, USAGE, and ALTER. For privilege\_scope values<br>other than schema, possible values include any permission type available on the permission's<br>scope. |
| identity\_id     | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID.                                                                                                                                                                                            |
| identity\_name   | text      | The name of the identity.                                                                                                                                                                                                                                             |
| identity\_type   | text      | The type of the identity. Possible values are user, role, group, or public.                                                                                                                                                                                           |
| admin\_option    | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type.                                                                                                             |
| privilege\_scope | text      | The scope of the permission specified<br>in privilege\_type. Possible values are as follows:<br>• SCHEMA<br>• TABLES<br>• FUNCTIONS<br>For information on scoped permissions, go to [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").          |

## Sample query

The following example displays the result of the SVV\_SCHEMA\_PRIVILEGES.

```
SELECT namespace_name,privilege_type,identity_name,identity_type,admin_option FROM svv_schema_privileges
WHERE namespace_name = 'test_schema1';

 namespace_name | privilege_type |  identity_name | identity_type | admin_option
----------------+----------------+----------------+---------------+--------------
 test_schema1   |    USAGE       |     reguser    |     user      |   False
 test_schema1   |    USAGE       |     role1      |     role      |   False
```
