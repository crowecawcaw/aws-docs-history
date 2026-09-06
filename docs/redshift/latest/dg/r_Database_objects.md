

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Database security
<a name="r_Database_objects"></a>

You manage database security by controlling which users have access to which database objects. Users can be assigned roles or groups, and the permissions you grant to users, roles, or groups decides which database objects they can access.

**Topics**
+ [Amazon Redshift security overview](c_security-overview.md)
+ [Default database user permissions](r_Privileges.md)
+ [superuser](r_superusers.md)
+ [Users](r_Users.md)
+ [Groups](r_Groups.md)
+ [Schemas](r_Schemas_and_tables.md)
+ [Role-based access control (RBAC)](t_Roles.md)
+ [Row-level security](t_rls.md)
+ [Metadata security](t_metadata_security.md)
+ [Dynamic data masking](t_ddm.md)
+ [Scoped permissions](t_scoped-permissions.md)

Access to database objects depends on the permissions that you grant to users or roles. The following guidelines summarize how database security works:
+ By default, permissions are granted only to the object owner.
+ Amazon Redshift database users are named users that can connect to a database. A user is granted permissions in two ways: explicitly, by having those permissions assigned directly to the account, or implicitly, by being a member of a group that is granted permissions.
+ Groups are collections of users that can be collectively assigned permissions for streamlined security maintenance.
+ Schemas are collections of database tables and other database objects. Schemas are similar to file system directories, except that schemas cannot be nested. Users can be granted access to a single schema or to multiple schemas.

Additionally, Amazon Redshift employs the following features to give you finer control over which users have access to which database objects:
+  With role-based access control (RBAC), you can assign permissions to roles which you can then apply to users, letting you control permissions for large groups of users. Unlike groups, roles can inherit permissions from other roles. 

  With row-level security (RLS), you can define policies that restrict access to rows of your choosing, then apply those policies to users or groups. 

   Dynamic data masking (DDM) further protects your data by transforming it at query runtime so that you can allow users access to data without exposing sensitive details. 

For examples of security implementation, see [Example for controlling user and group access](t_user_group_examples.md).

For more information about protecting your data, see [Security in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/iam-redshift-user-mgmt.html) in the *Amazon Redshift Management Guide*. 