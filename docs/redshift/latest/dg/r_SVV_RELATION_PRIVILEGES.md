Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_RELATION\_PRIVILEGES

Use SVV\_RELATION\_PRIVILEGES to view the relation (tables and views) permissions that
are explicitly granted to users, roles, and groups in the current database.

SVV\_RELATION\_PRIVILEGES is visible to the following users:

- Superusers
- Users with the SYSLOG ACCESS UNRESTRICTED permission
  Other users can only see identities they have access to or own. For more information about data visibility,
  see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW GRANTS](r_SHOW_GRANTS.md "r_SHOW_GRANTS.md") command for permission discovery. SHOW GRANTS works consistently
across local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name     | Data type | Description                                                                                                                                               |
| --------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namespace\_name | text      | The name of the namespace where a specified<br>relation exists.                                                                                           |
| relation\_name  | text      | The name of the relation.                                                                                                                                 |
| privilege\_type | text      | The type of the permission. Possible values are<br>INSERT, SELECT, UPDATE, DELETE, REFERENCES, or DROP.                                                   |
| identity\_id    | integer   | The ID of the identity. Possible values are user<br>ID, role ID, or group ID.                                                                             |
| identity\_name  | text      | The name of the identity.                                                                                                                                 |
| identity\_type  | text      | The type of the identity. Possible values are<br>user, role, group, or public.                                                                            |
| admin\_option   | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type. |

## Sample query

The following example displays the result of the SVV\_RELATION\_PRIVILEGES.

```
SELECT namespace_name,relation_name,privilege_type,identity_name,identity_type,admin_option FROM svv_relation_privileges
WHERE relation_name = 'orders' AND privilege_type = 'SELECT';

 namespace_name | relation_name | privilege_type |  identity_name | identity_type | admin_option
----------------+---------------+----------------+----------------+---------------+--------------
     public     |    orders     |     SELECT     |    reguser     |     user      |    False
     public     |    orders     |     SELECT     |     role1      |     role      |    False
```
