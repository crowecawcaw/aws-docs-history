Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# REVOKE

Removes access permissions, such as permissions to create, drop, or update tables, from
a user or role.

You can only GRANT or REVOKE USAGE permissions on an external schema to database users
and roles using the ON SCHEMA syntax. When using ON EXTERNAL SCHEMA with AWS Lake Formation, you can
only GRANT and REVOKE permissions to an AWS Identity and Access Management (IAM) role. For the list of permissions,
see the syntax.

For stored procedures, USAGE ON LANGUAGE `plpgsql` permissions are granted to
PUBLIC by default. EXECUTE ON PROCEDURE permission is granted only to the owner and
superusers by default.

Specify in the REVOKE command the permissions that you want to remove. To give
permissions, use the [GRANT](r_GRANT.md "r_GRANT.md") command.

## Syntax

```
REVOKE [ GRANT OPTION FOR ]
{ { SELECT | INSERT | UPDATE | DELETE | DROP | REFERENCES | ALTER | TRUNCATE } [,...] | ALL [ PRIVILEGES ] }
ON { [ TABLE ] *table\_name* [, ...] | ALL TABLES IN SCHEMA *schema\_name* [, ...] }
FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
{ { CREATE | TEMPORARY | TEMP | ALTER } [,...] | ALL [ PRIVILEGES ] }
ON DATABASE *db\_name* [, ...]
FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
{ { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
ON SCHEMA *schema\_name* [, ...]
FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
EXECUTE
    ON FUNCTION *function\_name* ( [ [ *argname* ] *argtype* [, ...] ] ) [, ...]
    FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
{ { EXECUTE } [,...] | ALL [ PRIVILEGES ] }
    ON PROCEDURE *procedure\_name* ( [ [ *argname* ] *argtype* [, ...] ] ) [, ...]
    FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
USAGE
    ON LANGUAGE *language\_name* [, ...]
    FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
[ RESTRICT ]

REVOKE [GRANT OPTION FOR]
{ { ALTER | DROP} [,...] | ALL [ PRIVILEGES ] }
    ON COPY JOB *job\_name* [,...]
    FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

```

The following is the syntax for column-level permissions on Amazon Redshift tables and
views.

```
REVOKE { { SELECT | UPDATE } ( *column\_name* [, ...] ) [, ...] | ALL [ PRIVILEGES ] ( *column\_name* [,...] ) }
     ON { [ TABLE ] *table\_name* [, ...] }
     FROM { *username* | ROLE *role\_name* | GROUP group_name | PUBLIC } [, ...]
     [ RESTRICT ]
```

The following is the syntax to revoke the ASSUMEROLE permission from users and
groups with a specified role.

```
REVOKE ASSUMEROLE
    ON { 'iam_role' [, ...]  | default | ALL }
    FROM { *user\_name* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
    FOR { ALL | COPY | UNLOAD | EXTERNAL FUNCTION | CREATE MODEL }

```

The following is the syntax for Redshift Spectrum integration with Lake Formation.

```
REVOKE [ GRANT OPTION FOR ]
{ SELECT | ALL [ PRIVILEGES ] } ( *column\_list* )
    ON EXTERNAL TABLE *schema\_name.table\_name*
    FROM { IAM_ROLE *iam\_role* } [, ...]

REVOKE [ GRANT OPTION FOR ]
{ { SELECT | ALTER | DROP | DELETE | INSERT }  [, ...] | ALL [ PRIVILEGES ] }
    ON EXTERNAL TABLE *schema\_name.table\_name* [, ...]
    FROM { { IAM_ROLE *iam\_role* } [, ...] | PUBLIC }

REVOKE [ GRANT OPTION FOR ]
{ { CREATE | ALTER | DROP }  [, ...] | ALL [ PRIVILEGES ] }
    ON EXTERNAL SCHEMA *schema\_name* [, ...]
    FROM { IAM_ROLE *iam\_role* } [, ...]
```

###### Producer-side datashare permissions

The following is the syntax for using REVOKE to remove ALTER or SHARE
permissions from a user or role. The user whose permissions have been revoked
can no longer alter the datashare, or grant usage to a consumer.

```
REVOKE { ALTER | SHARE } ON DATASHARE *datashare\_name*
 FROM { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP `group_name` | PUBLIC } [, ...]
```

The following is the syntax for using REVOKE to remove a consumer’s access to a
datashare.

```
REVOKE USAGE
 ON DATASHARE *datashare\_name*
 FROM NAMESPACE *'namespaceGUID'* [, ...] | ACCOUNT *'accountnumber'* [ VIA DATA CATALOG ] [, ...]
```

The following is an example of revoking usage of a datashare from a Lake Formation
account.

```
REVOKE USAGE ON DATASHARE salesshare FROM ACCOUNT '123456789012' VIA DATA CATALOG;
```

###### Consumer-side datashare permissions

The following is the REVOKE syntax for data-sharing usage permissions on a
specific database or schema created from a datashare.
Revoking usage permission from a database created with the
WITH PERMISSIONS clause doesn't revoke any additional permissions you granted a
user or role, including object-level permissions granted for underlying
objects. If you re-grant usage permission to that user or role, they will
retain all additional permissions that they had before you revoked
usage.

```
REVOKE USAGE ON { DATABASE *shared\_database\_name* [, ...] | SCHEMA *shared\_schema*}
 FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
```

Scoped permissions let you grant permissions to a user or role on
all objects of a type within a database or schema. Users and roles with scoped permissions have the specified
permissions on all current and future objects within the database or schema.

You can view the scope of database-level scoped permissions in [SVV_DATABASE_PRIVILEGES](r_SVV_DATABASE_PRIVILEGES.md "r_SVV_DATABASE_PRIVILEGES.md").
You can view the scope of schema-level scoped permissions in [SVV_SCHEMA_PRIVILEGES](r_SVV_SCHEMA_PRIVILEGES.md "r_SVV_SCHEMA_PRIVILEGES.md").

For more information about scoped permissions, see [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").

The following is the syntax for revoking scoped permissions from users and
roles.

```
REVOKE [ GRANT OPTION ]
{ CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
FOR SCHEMAS IN
DATABASE db_name
FROM { username | ROLE role_name } [, ...]

REVOKE [ GRANT OPTION ]
{ { SELECT | INSERT | UPDATE | DELETE | DROP | ALTER | TRUNCATE | REFERENCES } [, ...] } | ALL [PRIVILEGES] } }
FOR TABLES IN
{ SCHEMA schema_name [ DATABASE db_name ] | DATABASE db_name }
FROM { username | ROLE role_name } [, ...]

REVOKE [ GRANT OPTION ] { EXECUTE | ALL [ PRIVILEGES ] }
FOR FUNCTIONS IN
{ SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
FROM { username | ROLE role_name } [, ...]

REVOKE [ GRANT OPTION ] { EXECUTE | ALL [ PRIVILEGES ] }
FOR PROCEDURES IN
{ SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
FROM { username | ROLE role_name } [, ...]

REVOKE [ GRANT OPTION ] USAGE
FOR LANGUAGES IN
DATABASE db_name
FROM { username | ROLE role_name } [, ...]

REVOKE [GRANT_OPTION]
{ { CREATE | ALTER | DROP} [,...] | ALL [ PRIVILEGES ] }
FOR COPY JOBS
IN DATABASE *db\_name*
FROM { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* } [, ...]

```

Note that scoped permissions don’t distinguish between permissions for
functions and for procedures. For example, the following statement revokes
`EXECUTE` permissions for both functions and procedures from
`bob` in the schema `Sales_schema`.

```
REVOKE EXECUTE FOR FUNCTIONS IN SCHEMA Sales_schema FROM bob;
```

The following is the syntax for machine learning model permissions on
Amazon Redshift.

```
REVOKE [ GRANT OPTION FOR ]
    CREATE MODEL FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
    [ RESTRICT ]

REVOKE [ GRANT OPTION FOR ]
    { EXECUTE | ALL [ PRIVILEGES ] }
    ON MODEL *model\_name* [, ...]

    FROM { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
    [ RESTRICT ]
```

The following is the syntax for revoking role permissions on Amazon Redshift.

```
REVOKE [ ADMIN OPTION FOR ] { ROLE *role\_name* } [, ...] FROM { *user\_name* } [, ...]
```

```
REVOKE { ROLE *role\_name* } [, ...] FROM { ROLE *role\_name* } [, ...]
```

The following is the syntax for revoking system permissions to roles on
Amazon Redshift.

```
REVOKE
  {
    { CREATE USER | DROP USER | ALTER USER |
    CREATE SCHEMA | DROP SCHEMA |
    ALTER DEFAULT PRIVILEGES |
    ACCESS CATALOG |
    CREATE TABLE | DROP TABLE | ALTER TABLE |
    CREATE OR REPLACE FUNCTION | CREATE OR REPLACE EXTERNAL FUNCTION |
    DROP FUNCTION |
    CREATE OR REPLACE PROCEDURE | DROP PROCEDURE |
    CREATE OR REPLACE VIEW | DROP VIEW |
    CREATE MODEL | DROP MODEL |
    CREATE DATASHARE | ALTER DATASHARE | DROP DATASHARE |
    CREATE LIBRARY | DROP LIBRARY |
    CREATE ROLE | DROP ROLE
    TRUNCATE TABLE
    VACUUM | ANALYZE | CANCEL }[, ...]
  }
  | { ALL [ PRIVILEGES ] }
FROM { ROLE *role\_name* } [, ...]
```

The following is the syntax for revoking permissions to explain the
security policy filters of a query in the EXPLAIN plan. Possible security policies include row-level security policies
and dynamic data masking policies.

```
REVOKE EXPLAIN { RLS | MASKING } FROM ROLE *rolename*
```

The following is the syntax for revoking permissions to bypass row-level
security policies for a query.

```
REVOKE IGNORE RLS FROM ROLE *rolename*
```

The following is the syntax for revoking SELECT permissions from the specified
security policy. Possible security policies include row-level security policies
and dynamic data masking policies.

```
REVOKE SELECT ON [ TABLE ] *table\_name* [, ...]
            FROM { RLS | MASKING } POLICY *policy\_name* [, ...]
```

## Parameters

GRANT OPTION FOR

Revokes only the option to grant a specified permission to other users and
doesn't revoke the permission itself. You can't revoke GRANT OPTION
from a group or from PUBLIC.

SELECT

Revokes the permission to select data from a table or a view using a SELECT
statement.

INSERT

Revokes the permission to load data into a table using an INSERT statement
or a COPY statement.

UPDATE

Revokes the permission to update a table column using an UPDATE statement.

DELETE

Revokes the permission to delete a data row from a table.

REFERENCES

Revokes the permission to create a foreign key constraint. You should revoke
this permission on both the referenced table and the referencing table.

TRUNCATE

Revokes the permission to truncate a table. Without this permission, only
the owner of a table or a superuser can truncate a table. For more information
about the TRUNCATE command, see [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md").

ALL [ PRIVILEGES ]

Revokes all available permissions at once from the specified user or group.
The PRIVILEGES keyword is optional.

###### Note

Amazon Redshift doesn't support the RULE and TRIGGER permissions. For more
information, go to [Unsupported PostgreSQL
features](c_unsupported-postgresql-features.md "c_unsupported-postgresql-features.md").

ALTER

Depending on the database object, revokes the following permissions from the
user or user group:

- For tables, ALTER revokes permission to alter a table or view. For
  more information, see [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").
- For databases, ALTER revokes permission to alter a database. For more
  information, see [ALTER DATABASE](r_ALTER_DATABASE.md "r_ALTER_DATABASE.md").
- For schemas, ALTER grants revokes to alter a schema. For more
  information, see [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md").
- For external tables, ALTER revokes permission to alter a table in an
  AWS Glue Data Catalog that is enabled for Lake Formation. This permission only applies when
  using Lake Formation.

DROP

Depending on the database object, revokes the following permissions from the
user or role:

- For tables, DROP revokes permission to drop a table or view. For more
  information, see [DROP TABLE](r_DROP_TABLE.md "r_DROP_TABLE.md").
- For databases, DROP revokes permission to drop a database. For more
  information, see [DROP DATABASE](r_DROP_DATABASE.md "r_DROP_DATABASE.md").
- For schemas, DROP revokes permission to drop a schema. For more
  information, see [DROP SCHEMA](r_DROP_SCHEMA.md "r_DROP_SCHEMA.md").

ASSUMEROLE

Revokes the permission to run COPY, UNLOAD, EXTERNAL FUNCTION, or CREATE
MODEL commands from users, roles, or groups with a specified role.

ON [ TABLE ] _table_name_

Revokes the specified permissions on a table or a view. The TABLE keyword is
optional.

ON ALL TABLES IN SCHEMA _schema_name_

Revokes the specified permissions on all tables in the referenced
schema.

( _column_name_ [,...] ) ON TABLE
_table_name_

Revokes the specified permissions from users, groups, or PUBLIC on the
specified columns of the Amazon Redshift table or view.

( _column_list_ ) ON EXTERNAL TABLE
_schema_name.table_name_

Revokes the specified permissions from an IAM role on the specified columns
of the Lake Formation table in the referenced schema.

ON EXTERNAL TABLE _schema_name.table_name_

Revokes the specified permissions from an IAM role on the specified Lake Formation
tables in the referenced schema.

ON EXTERNAL SCHEMA _schema_name_

Revokes the specified permissions from an IAM role on the referenced
schema.

FROM IAM_ROLE _iam_role_

Indicates the IAM role losing the permissions.

ROLE _role_name_

Revokes the permissions from the specified role.

GROUP _group_name_

Revokes the permissions from the specified user group.

PUBLIC

Revokes the specified permissions from all users. PUBLIC represents a group
that always includes all users. An individual user's permissions consist
of the sum of permissions granted to PUBLIC, permissions granted to any groups
that the user belongs to, and any permissions granted to the user
individually.

Revoking PUBLIC from a Lake Formation external table results in revoking the
permission from the Lake Formation _everyone_ group.

CREATE

Depending on the database object, revokes the following permissions from the
user or group:

- For databases, using the CREATE clause for REVOKE prevents users from
  creating schemas within the database.
- For schemas, using the CREATE clause for REVOKE prevents users from
  creating objects within a schema. To rename an object, the user must have
  the CREATE permission and own the object to be renamed.

###### Note

By default, all users have CREATE and USAGE permissions on the PUBLIC
schema.

TEMPORARY | TEMP

Revokes the permission to create temporary tables in the specified
database.

###### Note

By default, users are granted permission to create temporary tables by
their automatic membership in the PUBLIC group. To remove the permission for
any users to create temporary tables, revoke the TEMP permission from the
PUBLIC group and then explicitly grant the permission to create temporary
tables to specific users or groups of users.

ON DATABASE _db_name_

Revokes the permissions on the specified database.

USAGE

Revokes USAGE permissions on objects within a specific schema, which makes
these objects inaccessible to users. Specific actions on these objects must be
revoked separately (such as the EXECUTE permission on functions).

###### Note

By default, all users have CREATE and USAGE permissions on the PUBLIC
schema.

ON SCHEMA _schema_name_

Revokes the permissions on the specified schema. You can use schema
permissions to control the creation of tables; the CREATE permission for a
database only controls the creation of schemas.

RESTRICT

Revokes only those permissions that the user directly granted. This behavior
is the default.

EXECUTE ON PROCEDURE _procedure_name_

Revokes the EXECUTE permission on a specific stored procedure. Because
stored procedure names can be overloaded, you must include the argument list
for the procedure. For more information, see [Naming stored procedures](stored-procedure-naming.md "stored-procedure-naming.md").

EXECUTE ON ALL PROCEDURES IN SCHEMA _procedure_name_

Revokes the specified permissions on all procedures in the referenced
schema.

USAGE ON LANGUAGE _language_name_

Revokes the USAGE permission on a language. For Python user-defined
functions (UDFs), use `plpythonu`. For SQL UDFs, use
`sql`. For stored procedures, use `plpgsql`.

To create a UDF, you must have permission for usage on language for SQL or
`plpythonu` (Python). By default, USAGE ON LANGUAGE SQL is
granted to PUBLIC. However, you must explicitly grant USAGE ON LANGUAGE
PLPYTHONU to specific users or groups.

To revoke usage for SQL, first revoke usage from PUBLIC. Then grant usage on
SQL only to the specific users or groups permitted to create SQL UDFs. The
following example revokes usage on SQL from PUBLIC then grants usage to the
user group `udf_devs`.

```
revoke usage on language sql from PUBLIC;
grant usage on language sql to group udf_devs;
```

For more information, see [UDF security and permissions](udf-security-and-privileges.md "udf-security-and-privileges.md").

To revoke usage for stored procedures, first revoke usage from PUBLIC. Then
grant usage on `plpgsql` only to the specific users or groups
permitted to create stored procedures. For more information, see [Security and privileges for
stored procedures](stored-procedure-security-and-privileges.md "stored-procedure-security-and-privileges.md") .

ON COPY JOB _job_name_

Revokes the specified permissions on a copy job.

FOR { ALL | COPY | UNLOAD | EXTERNAL FUNCTION | CREATE MODEL } [, ...]

Specifes the SQL command for which the permission is revoked. You can
specify ALL to revoke the permission on the COPY, UNLOAD, EXTERNAL FUNCTION,
and CREATE MODEL statements. This clause applies only to revoking the
ASSUMEROLE permission.

ALTER

Revokes the ALTER permission for users or user groups that allows those that
don't own a datashare to alter the datashare. This permission is required to
add or remove objects from a datashare, or to set the property
PUBLICACCESSIBLE. For more information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

SHARE

Revokes permissions for users and user groups to add consumers to a
datashare. Revoking this permissionis required to stop the particular consumer
from accessing the datashare from its clusters.

ON DATASHARE _datashare_name_

Grants the specified permissions on the referenced datashare.

FROM username

Indicates the user losing the permissions.

FROM GROUP _group_name_

Indicates the user group losing the permissions.

WITH GRANT OPTION

Indicates that the user losing the permissions can in turn revoke the same
permissions for others. You can't revoke WITH GRANT OPTION for a group or
for PUBLIC.

USAGE

When USAGE is revoked for a consumer account or namespace within the same
account, the specified consumer account or namespace within an account
can't access the datashare and the objects of the datashare in read-only
fashion.

Revoking the USAGE permission revokes the access to a datashare from
consumers.

FROM NAMESPACE 'clusternamespace GUID'

Indicates the namespace in the same account that has consumers losing the
permissions to the datashare. Namespaces use a 128-bit alphanumeric globally
unique identifier (GUID).

FROM ACCOUNT 'accountnumber' [ VIA DATA CATALOG ]

Indicates the account number of another account that has the consumers
losing the permissions to the datashare. Specifying ‘VIA DATA CATALOG’
indicates that you are revoking usage of the datashare from a Lake Formation account.
Omitting the account number means that you're revoking from the account
that owns the cluster.

ON DATABASE _shared_database_name> [, ...]_

Revokes the specified usage permissions on the specified database that was
created in the specified datashare.

ON SCHEMA _shared_schema_

Revokes the specified permissions on the specified schema that was created
in the specified datashare.

FOR { SCHEMAS | TABLES | FUNCTIONS | PROCEDURES | LANGUAGES | COPY JOBS} IN

Specifies the database objects to revoke permission from. The parameters
following IN define the scope of the revoked permission.

CREATE MODEL

Revokes the CREATE MODEL permission to create machine learning models in the
specified database.

ON MODEL _model_name_

Revokes the EXECUTE permission for a specific model.

ACCESS CATALOG

Revokes the permission to view relevant metadata of objects that the role
has access to.

[ ADMIN OPTION FOR ] { role } [, ...]

The role that you revoke from a specified user that has the WITH ADMIN
OPTION.

FROM { role } [, ...]

The role that you revoke the specified role from.

EXPLAIN { RLS | MASKING } FROM ROLE _rolename_

Revokes the permission to explain the security policy filters of a
query in the EXPLAIN plan from a role. RLS revokes permission to explain row-level security policy filters.
MASKING revokes permission to explain dynamic data masking policy filters.

IGNORE RLS FROM ROLE _rolename_

Revokes the permission to bypass row-level security policies for a query from a
role.

FROM { RLS | MASKING } POLICY _policy_name_
Indicates the security policy losing the permissions.
TO RLS POLICY indicates a row-level security policy. TO MASKING POLICY indicates
a dynamic data masking policy.

## Usage notes

To learn more about the usage notes for REVOKE, see [Usage notes](r_REVOKE-usage-notes.md "r_REVOKE-usage-notes.md").

## Examples

For examples of how to use REVOKE, see [Examples](r_REVOKE-examples.md "r_REVOKE-examples.md").
