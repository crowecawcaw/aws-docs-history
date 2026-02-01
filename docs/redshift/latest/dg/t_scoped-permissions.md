Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Scoped permissions

Scoped permissions let you grant permissions to a user or role on
all objects of a type within a database or schema. Users and roles with scoped permissions have the specified
permissions on all current and future objects within the database or schema.

You can view the scope of database-level scoped permissions in [SVV_DATABASE_PRIVILEGES](r_SVV_DATABASE_PRIVILEGES.md "r_SVV_DATABASE_PRIVILEGES.md").
You can view the scope of schema-level scoped permissions in [SVV_SCHEMA_PRIVILEGES](r_SVV_SCHEMA_PRIVILEGES.md "r_SVV_SCHEMA_PRIVILEGES.md").

For more information on applying scoped permissions, see [GRANT](r_GRANT.md "r_GRANT.md")
and [REVOKE](r_REVOKE.md "r_REVOKE.md").
