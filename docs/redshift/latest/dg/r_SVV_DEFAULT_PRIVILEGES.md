Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_DEFAULT_PRIVILEGES

Use SVV_DEFAULT_PRIVILEGES to view the default privileges that a user has access to in an Amazon Redshift cluster.

SVV_DEFAULT_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see default permissions granted to them.

## Table columns

| Column name    | Data type | Description                                                                                                                              |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| schema_name    | text      | The name of the schema.                                                                                                                  |
| object_type    | text      | The object type. Possible values are RELATION, FUNCTION, or PROCEDURE.                                                                   |
| owner_id       | integer   | The owner ID. Possible value is the user ID.                                                                                             |
| owner_name     | text      | The name of the owner.                                                                                                                   |
| owner_type     | text      | The owner type. Possible value is user.                                                                                                  |
| privilege_type | text      | The privilege type. Possible values are INSERT, SELECT, UPDATE, DELETE, RULE, REFERENCES<br>TRIGGER, DROP, and EXECUTE.                  |
| grantee_id     | integer   | The grantee ID. Possible values are user ID, role ID, and group ID.                                                                      |
| grantee_type   | text      | The grantee type. Possible values are user, role, and public.                                                                            |
| admin_option   | boolean   | The value that indicates whether the user can grant permissions to other users and roles.<br>It is always false for role and group type. |

## Sample query

The following example returns the output for SVV_DEFAULT_PRIVILEGES.

```
SELECT * from svv_default_privileges;

 schema_name |    object_type    | owner_id | owner_name | owner_type | privilege_type | grantee_id | grantee_name | grantee_type | admin_option
-------------+-------------------+--------- +------------+------------+----------------+------------+--------------+--------------+-------------+
   public    |     RELATION      |    106   |     u1     |    user    |     UPDATE     |     107    |      u2      |     user     |      f      |
   public    |     RELATION      |    106   |     u1     |    user    |     SELECT     |     107    |      u2      |     user     |      f      |

```
