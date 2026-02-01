Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ROLES

Use SVV_ROLES to view role information.

This table is visible to all users.

## Table columns

| Column name | Data type | Description                                                             |
| ----------- | --------- | ----------------------------------------------------------------------- |
| role_id     | integer   | The role ID.                                                            |
| role_name   | text      | The name of the role.                                                   |
| role_owner  | text      | The name of the role owner.                                             |
| external_id | text      | The unique identifier of the role in the third-party identity provider. |

## Sample query

The following example returns the output of SVV_ROLES.

```
SELECT role_name,role_owner FROM svv_roles WHERE role_name IN ('role1', 'role2');

 role_name | role_owner
-----------+------------
   role1   | superuser
   role2   | superuser
```
