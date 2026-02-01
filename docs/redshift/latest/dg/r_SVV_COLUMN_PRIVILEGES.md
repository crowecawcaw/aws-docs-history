Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_COLUMN_PRIVILEGES

Use SVV_COLUMN_PRIVILEGES to view the column permissions that are explicitly granted
to users, roles, and groups in the current database.

SVV_COLUMN_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name    | Data type | Description                                                                |
| -------------- | --------- | -------------------------------------------------------------------------- |
| namespace_name | text      | The name of the namespace where a specified relation exists.               |
| relation_name  | text      | The name of the relation.                                                  |
| column_name    | text      | The name of the column.                                                    |
| privilege_type | text      | The type of the permission. Possible values are<br>SELECT or UPDATE.       |
| identity_id    | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID. |
| identity_name  | text      | The name of the identity.                                                  |
| identity_type  | text      | The type of the identity. Possible values are user, role, group or public. |

## Sample query

The following example displays the result of the SVV_COLUMN_PRIVILEGES.

```
SELECT namespace_name,relation_name,COLUMN_NAME,privilege_type,identity_name,identity_type
FROM svv_column_privileges WHERE relation_name = 'lineitem';

 namespace_name | relation_name | column_name | privilege_type | identity_name | identity_type
----------------+---------------+-------------+----------------+---------------+----------------
    public      |   lineitem    | l_orderkey  |     SELECT     |    reguser    |     user
    public      |   lineitem    | l_orderkey  |     SELECT     |     role1     |     role
    public      |   lineitem    | l_partkey   |     SELECT     |    reguser    |     user
    public      |   lineitem    | l_partkey   |     SELECT     |     role1     |     role
```
