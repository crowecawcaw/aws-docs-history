Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Superusers

Database superusers have the same permissions
as database owners for all databases.

The _admin_ user, which is the user you created when you launched the
cluster, is a superuser.

You must be a superuser to create a superuser.

Amazon Redshift system tables and system views are either visible only to superusers or visible
to all users. Only superusers can query system tables and system views that are designated
"visible to superusers." For information, see [SYS monitoring views](serverless_views-monitoring.md "serverless_views-monitoring.md").

Superusers can view all catalog tables. For information, see [System catalog tables](c_intro_catalog_views.md "c_intro_catalog_views.md").

A database superuser bypasses all permission checks. Superusers retain all permissions
regardless of GRANT and REVOKE commands. Be careful when using a superuser role. We
recommend that you do most of your work as a role that is not a superuser. You can create
an administrator role with more restrictive permissions. For more information about
creating roles, see [Role-based access control (RBAC)](t_Roles.md "t_Roles.md")

To create a new database superuser, log on to the database as a superuser and issue a
CREATE USER command or an ALTER USER command with the CREATEUSER permission.

```
CREATE USER adminuser CREATEUSER PASSWORD '1234Admin';
ALTER USER adminuser CREATEUSER;

```

To create, alter, or drop a superuser, use the same commands to manage users. For more information, see
[Creating, altering, and
deleting users](r_Users-creatingaltering-and-deleting-users.md "r_Users-creatingaltering-and-deleting-users.md").
