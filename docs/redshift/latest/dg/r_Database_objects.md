Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Database security

You manage database security by controlling which users have access to which database
objects. Users can be assigned roles or groups, and the permissions you grant to
users, roles, or groups decides which database objects they can access.

###### Topics

- [Amazon Redshift security overview](c_security-overview.md "c_security-overview.md")
- [Default database user permissions](r_Privileges.md "r_Privileges.md")
- [Superusers](r_superusers.md "r_superusers.md")
- [Users](r_Users.md "r_Users.md")
- [Groups](r_Groups.md "r_Groups.md")
- [Schemas](r_Schemas_and_tables.md "r_Schemas_and_tables.md")
- [Role-based access control (RBAC)](t_Roles.md "t_Roles.md")
- [Row-level security](t_rls.md "t_rls.md")
- [Metadata security](t_metadata_security.md "t_metadata_security.md")
- [Dynamic data masking](t_ddm.md "t_ddm.md")
- [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md")
  Access to database objects depends on the permissions that you grant to users or
  roles. The following guidelines summarize how database security works:

- By default, permissions are granted only to the object owner.
- Amazon Redshift database users are named users that can connect to a database. A
  user is granted permissions in two ways: explicitly, by having those permissions
  assigned directly to the account, or implicitly, by being a member of a group that is
  granted permissions.
- Groups are collections of users that can be collectively assigned permissions for
  streamlined security maintenance.
- Schemas are collections of database tables and other database objects. Schemas are
  similar to file system directories, except that schemas cannot be nested. Users can
  be granted access to a single schema or to multiple schemas.
  Additionally, Amazon Redshift employs the following features to give you finer control over
  which users have access to which database objects:

- Role-based access control (RBAC) lets you assign permissions to roles which you can then
  apply to users, letting you control permissions for large groups of users. Unlike groups,
  roles can inherit permissions from other roles.

Row-level security (RLS) lets you define policies that restrict access to rows of your choosing,
then apply those policies to users or groups.

Dynamic data masking (DDM) further protects your data by transforming it at query runtime so that
you can allow users access to data without exposing sensitive details.
For examples of security implementation, see [Example for controlling user and group
access](t_user_group_examples.md "t_user_group_examples.md").

For more information about protecting your data, see
[Security in Amazon Redshift](../mgmt/iam-redshift-user-mgmt.md "../mgmt/iam-redshift-user-mgmt.md") in
the _Amazon Redshift Management Guide_.
