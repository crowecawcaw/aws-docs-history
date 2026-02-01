Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_SYSTEM_PRIVILEGES

SVV_SYSTEM_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name      | Data type | Description                                                     |
| ---------------- | --------- | --------------------------------------------------------------- |
| system_privilege | text      | The name of the system permission.                              |
| identity_id      | integer   | The ID of the identity. Possible values are user ID or role ID. |
| identity_name    | text      | The name of the identity.                                       |
| identity_type    | text      | The type of the identity. Possible values are user or role.     |

## Sample query

The following example displays the result for the specified parameters.

```
SELECT system_privilege,identity_name,identity_type FROM svv_system_privileges
WHERE system_privilege = 'ALTER TABLE' AND identity_name = 'sys:superuser';

 system_privilege | identity_name | identity_type
------------------+---------------+---------------
   ALTER TABLE    | sys:superuser |     role
```
