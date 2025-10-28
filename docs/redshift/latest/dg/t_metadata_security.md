Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Metadata security

Like Amazon Redshift’s row-level security, metadata security gives you more granular control
over your metadata. If metadata security is enabled for your provisioned cluster or
serverless workgroup, users can see metadata for the objects for which they have viewing
access. Metadata security lets you separate visibility based on your needs. For example,
you can use a single data warehouse to centralize all of your data storage. However, if you
store data for multiple sectors, managing security can become troublesome. With metadata
security enabled, you can configure your visibility. Users of one sector can have more
visibility over their objects, while you restrict viewing access to users of another
sector. Metadata security supports all object types, such as schemas, tables, views,
materialized views, stored procedures, user-defined functions, and machine learning
models.

Users can see metadata of objects under the following circumstances:

- If object access is granted to the user.
- If object access is granted to a group or a role that the user is a part
  of.
- The object is public.
- The user is the owner of the database object.
  To enable metadata security, use the [ALTER SYSTEM](r_ALTER_SYSTEM.md "r_ALTER_SYSTEM.md") command. The following
  is the syntax of how to use the ALTER SYSTEM command with metadata security.

```
ALTER SYSTEM SET metadata_security=[true|t|on|false|f|off];
```

When you enable metadata security, all users who have the necessary permissions can see
the relevant metadata of objects that they have access to. If you want only certain users
to be able to see metadata security, grant the `ACCESS CATALOG` permission to a
role, and then assign the role to the user. For more information about using roles to
better control security, see [Role-based access control](t_Roles.md "t_Roles.md").

The following example demonstrates how to grant the
`ACCESS CATALOG` permission to a role,
and then assigns the role to a user. For more information about granting permissions,
see the [GRANT](r_GRANT.md "r_GRANT.md")
command.

```
CREATE ROLE sample_metadata_viewer;

GRANT ACCESS CATALOG TO ROLE sample_metadata_viewer;

GRANT ROLE sample_metadata_viewer to salesadmin;
```

If you prefer to use already defined roles, the [system-defined roles](r_roles-default.md "r_roles-default.md")
`operator`, `secadmin`, `dba`, and `superuser`
all have the necessary permissions to view object metadata. By default, superusers can see
the complete catalog.

```
GRANT ROLE operator to sample_user;
```

If you’re using roles to control metadata security, you have access to all of the system
views and functions that come with role-based access control. For example, you can
query the [SVV_ROLES](r_SVV_ROLES.md "r_SVV_ROLES.md") view to see all roles.
To see if a user is a member of a role or group, use the
[USER_IS_MEMBER_OF](r_USER_IS_MEMBER_OF.md "r_USER_IS_MEMBER_OF.md") function. For a full list of SVV views, see [SVV metadata views](svv_views.md "svv_views.md"). For a list of system information functions,
see [System information functions](r_System_information_functions.md "r_System_information_functions.md").
