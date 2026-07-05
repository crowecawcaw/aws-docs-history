Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_DATABASE\_PRIVILEGES

Use SVV\_DATABASE\_PRIVILEGES to view the database permissions that are explicitly
granted to users, roles, and groups in your Amazon Redshift cluster.

SVV\_DATABASE\_PRIVILEGES is visible to the following users:

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

| Column name      | Data type | Description                                                                                                                                                                                                                                                                                   |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| database\_name   | text      | The name of the database.                                                                                                                                                                                                                                                                     |
| privilege\_type  | text      | The type of the permission. For permissions with a privilege\_scope<br>of database, possible values are USAGE, CREATE, TEMPORARY,<br>TEMP, and ALTER. For privilege\_scope values<br>other than database, possible values include any permission type available on the permission's<br>scope. |
| identity\_id     | integer   | The ID of the identity. Possible values are user<br>ID, role ID, or group ID.                                                                                                                                                                                                                 |
| identity\_name   | text      | The name of the identity.                                                                                                                                                                                                                                                                     |
| identity\_type   | text      | The type of the identity. Possible values are<br>user, role, group, or public.                                                                                                                                                                                                                |
| admin\_option    | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type.                                                                                                                                     |
| privilege\_scope | text      | The scope of the permission specified<br>in privilege\_type. Possible values are as follows:<br>• DATABASE<br>• SCHEMAS<br>• TABLES<br>• FUNCTIONS<br>• LANGUAGES<br>For information on scoped permissions, go to [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").    |

## Sample query

The following example displays the result of the SVV\_DATABASE\_PRIVILEGES.

```
SELECT database_name,privilege_type,identity_name,identity_type,admin_option FROM svv_database_privileges
WHERE database_name = 'test_db';

 database_name | privilege_type | identity_name | identity_type | admin_option
---------------+----------------+---------------+---------------+--------------
     test_db   |     CREATE     |     reguser   |      user     |     False
     test_db   |     CREATE     |      role1    |      role     |     False
     test_db   |     TEMP       |      public   |      public   |     False
     test_db   |     TEMP       |      role1    |      role     |     False
```
