Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for using scoped permissions

When using scoped permissions, consider the following:

- You can use scoped permissions to grant or revoke permissions
  on a database or schema scope to or from a specified user or role.
- You can't grant scoped permissions to user groups.
- Granting or revoking scoped permissions changes permissions for
  all current and future objects in the scope.
- Scoped permissions and object-level permissions operate independently of each other.
  For example, a user will maintain permissions on a table in both of the following cases.
  - The user is granted SELECT on the table schema1.table1 and SELECT scoped permission on schema1.
    The user then has SELECT revoked for all tables in schema schema1.
    The user retains SELECT on schema1.table1.
  - The user is granted SELECT on the table schema1.table1 and SELECT scoped permission on schema1.
    The user then has SELECT revoked for schema1.table1.
    The user retains SELECT on schema1.table1.

- To grant or revoke scoped permissions, you must meet one of the following criteria:
  - Superusers.
  - Users with the grant option for that permission.
    For more information on grant options, go to the
    WITH GRANT OPTION parameter in [GRANT](r_GRANT.md "r_GRANT.md").

- Scoped permissions can only be granted to or revoked from objects for
  the connected database, or from databases imported from a datashare.
- You can use scoped permissions to set the default permissions on a database created from a datashare.
  A consumer-side datashare user who is granted scoped permissions on a shared database will
  automatically gain those permissions for any new object added to the datashare on
  the producer side.
- Producers can grant scoped permissions on objects within a schema to a datashare. (preview)
