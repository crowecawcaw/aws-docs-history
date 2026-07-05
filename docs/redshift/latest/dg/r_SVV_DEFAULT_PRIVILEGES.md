Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_DEFAULT\_PRIVILEGES

Use SVV\_DEFAULT\_PRIVILEGES to view the default privileges that a user has access to in an Amazon Redshift cluster.

SVV\_DEFAULT\_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see default permissions granted to them.

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW GRANTS](r_SHOW_GRANTS.md "r_SHOW_GRANTS.md") command for permission discovery. SHOW GRANTS works consistently
across local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name     | Data type | Description                                                                                                                              |
| --------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| schema\_name    | text      | The name of the schema.                                                                                                                  |
| object\_type    | text      | The object type. Possible values are RELATION, FUNCTION, or PROCEDURE.                                                                   |
| owner\_id       | integer   | The owner ID. Possible value is the user ID.                                                                                             |
| owner\_name     | text      | The name of the owner.                                                                                                                   |
| owner\_type     | text      | The owner type. Possible value is user.                                                                                                  |
| privilege\_type | text      | The privilege type. Possible values are INSERT, SELECT, UPDATE, DELETE, RULE, REFERENCES<br>TRIGGER, DROP, and EXECUTE.                  |
| grantee\_id     | integer   | The grantee ID. Possible values are user ID, role ID, and group ID.                                                                      |
| grantee\_type   | text      | The grantee type. Possible values are user, role, and public.                                                                            |
| admin\_option   | boolean   | The value that indicates whether the user can grant permissions to other users and roles.<br>It is always false for role and group type. |

## Sample query

The following example returns the output for SVV\_DEFAULT\_PRIVILEGES.

```
SELECT * from svv_default_privileges;

 schema_name |    object_type    | owner_id | owner_name | owner_type | privilege_type | grantee_id | grantee_name | grantee_type | admin_option
-------------+-------------------+--------- +------------+------------+----------------+------------+--------------+--------------+-------------+
   public    |     RELATION      |    106   |     u1     |    user    |     UPDATE     |     107    |      u2      |     user     |      f      |
   public    |     RELATION      |    106   |     u1     |    user    |     SELECT     |     107    |      u2      |     user     |      f      |

```
