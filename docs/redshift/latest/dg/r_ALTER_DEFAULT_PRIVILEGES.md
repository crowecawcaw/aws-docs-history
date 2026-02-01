Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER DEFAULT PRIVILEGES

Defines the default set of access permissions to be applied to objects that are created
in the future by the specified user. By default, users can change only their own default
access permissions. Only a superuser can specify default permissions for other
users.

You can apply default privileges to roles, users, or user groups. You can set default
permissions globally for all objects created in the current database, or for objects
created only in the specified schemas.

Default permissions apply only to new objects. Running ALTER DEFAULT PRIVILEGES doesn’t
change permissions on existing objects. To grant permissions on all current and future
objects created by any user within a database or schema, see [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").

To view information about the default privileges for database users, query the [PG_DEFAULT_ACL](r_PG_DEFAULT_ACL.md "r_PG_DEFAULT_ACL.md") system catalog table.

For more information about privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

## Required privileges

Following are required privileges for ALTER DEFAULT PRIVILEGES:

- Superuser
- Users with the ALTER DEFAULT PRIVILEGES privilege
- Users changing their own default access privileges
- Users setting privileges for schemas that they have access privileges to

## Syntax

```
ALTER DEFAULT PRIVILEGES
    [ FOR USER *target\_user* [, ...] ]
    [ IN SCHEMA *schema\_name* [, ...] ]
    *grant\_or\_revoke\_clause*

where *grant\_or\_revoke\_clause* is one of:

GRANT { { SELECT | INSERT | UPDATE | DELETE | DROP | REFERENCES | TRUNCATE } [,...] | ALL [ PRIVILEGES ] }
	ON TABLES
	TO { *user\_name* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
	ON FUNCTIONS
	TO { *user\_name* [ WITH GRANT OPTION ] |  ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
	ON PROCEDURES
	TO { *user\_name* [ WITH GRANT OPTION ] |  ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

REVOKE [ GRANT OPTION FOR ] { { SELECT | INSERT | UPDATE | DELETE | REFERENCES | TRUNCATE } [,...] | ALL [ PRIVILEGES ] }
	ON TABLES
	FROM *user\_name* [, ...] [ RESTRICT ]

REVOKE  { { SELECT | INSERT | UPDATE | DELETE | REFERENCES | TRUNCATE } [,...] | ALL [ PRIVILEGES ] }
	ON TABLES
	FROM { ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...] [ RESTRICT ]

REVOKE [ GRANT OPTION FOR ] { EXECUTE | ALL [ PRIVILEGES ] }
	ON FUNCTIONS
	FROM *user\_name* [, ...] [ RESTRICT ]

REVOKE { EXECUTE | ALL [ PRIVILEGES ] }
	ON FUNCTIONS
	FROM { ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...] [ RESTRICT ]

REVOKE [ GRANT OPTION FOR ] { EXECUTE | ALL [ PRIVILEGES ] }
	ON PROCEDURES
	FROM *user\_name* [, ...] [ RESTRICT ]

REVOKE { EXECUTE | ALL [ PRIVILEGES ] }
	ON PROCEDURES
	FROM { ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...] [ RESTRICT ]
```

## Parameters

FOR USER _target_user_

Optional. The name of the user for which default privileges are defined.
Only a superuser can specify default privileges for other users. The default
value is the current user.

IN SCHEMA _schema_name_

Optional. If an IN SCHEMA clause appears, the specified default privileges
are applied to new objects created in the specified
_schema_name_. In this case, the user or user group that
is the target of ALTER DEFAULT PRIVILEGES must have CREATE privilege for the
specified schema. Default privileges that are specific to a schema are added to
existing global default privileges. By default, default privileges are applied
globally to the entire database.

GRANT

The set of privileges to grant to the specified users or groups for all new
tables and views, functions, or stored procedures created by the specified
user. You can set the same privileges and options with the GRANT clause that
you can with the [GRANT](r_GRANT.md "r_GRANT.md") command.

WITH GRANT OPTION

A clause that indicates that the user receiving the privileges can in turn
grant the same privileges to others. You can't grant WITH GRANT OPTION to
a group or to PUBLIC.

TO _user_name_ | ROLE _role_name_ | GROUP
_group_name_

The name of the user, role, or user group to which the specified default
privileges are applied.

REVOKE

The set of privileges to revoke from the specified users or groups for all
new tables, functions, or stored procedures created by the specified user. You
can set the same privileges and options with the REVOKE clause that you can
with the [REVOKE](r_REVOKE.md "r_REVOKE.md") command.

GRANT OPTION FOR

A clause that revokes only the option to grant a specified privilege to
other users and doesn't revoke the privilege itself. You can't revoke
GRANT OPTION from a group or from PUBLIC.

FROM _user_name_ | ROLE _role_name_ |
GROUP _group_name_

The name of the user, role, or user group from which the specified
privileges are revoked by default.

RESTRICT

The RESTRICT option revokes only those privileges that the user directly
granted. This is the default.

## Examples

Suppose that you want to allow any user in the user group `report_readers`
to view all tables and views created by the user `report_admin`. In this
case, run the following command as a superuser.

```
alter default privileges for user report_admin grant select on tables to group report_readers;
```

In the following example, the first command grants SELECT privileges on all new
tables that you create. Anytime you create a new view, you must explicitly grant
privileges to the view or re-run the `alter default privileges` command
again.

```
alter default privileges grant select on tables to public;
```

The following example grants INSERT privilege to the `sales_admin` user
group for all new tables and views that you create in the `sales` schema.

```
alter default privileges in schema sales grant insert on tables to group sales_admin;
```

The following example reverses the ALTER DEFAULT PRIVILEGES command in the preceding
example.

```
alter default privileges in schema sales revoke insert on tables from group sales_admin;
```

By default, the PUBLIC user group has execute permission for all new user-defined
functions. To revoke `public` execute permissions for your new functions and
then grant execute permission only to the `dev_test` user group, run the
following commands.

```
alter default privileges revoke execute on functions from public;
alter default privileges grant execute on functions to group dev_test;
```
