Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_LANGUAGE\_PRIVILEGES

Use SVV\_LANGUAGE\_PRIVILEGES to view the language permissions that are explicitly
granted to users, roles, and groups in the current database.

SVV\_LANGUAGE\_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name     | Data type | Description                                                                                                                                               |
| --------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| language\_name  | text      | The name of the language.                                                                                                                                 |
| privilege\_type | text      | The type of the permission. Possible value is<br>USAGE.                                                                                                   |
| identity\_id    | integer   | The ID of the identity. Possible values are user<br>ID, role ID, or group ID.                                                                             |
| identity\_name  | text      | The name of the identity.                                                                                                                                 |
| identity\_type  | text      | The type of the identity. Possible values are<br>user, role, group, or public.                                                                            |
| admin\_option   | boolean   | A value that indicates whether the user can grant<br>the permission to other users and roles. It is always false for the<br>role and group identity type. |

## Sample query

The following example displays the result of the SVV\_LANGUAGE\_PRIVILEGES.

```
SELECT language_name,privilege_type,identity_name,identity_type,admin_option FROM svv_language_privileges
WHERE identity_name IN ('role1', 'reguser');

 language_name | privilege_type | identity_name | identity_type | admin_option
---------------+----------------+---------------+---------------+---------------
   exfunc      |     USAGE      |    reguser    |     user      |    False
   exfunc      |     USAGE      |     role1     |     role      |    False
   plpythonu   |     USAGE      |    reguser    |     user      |    False
```
