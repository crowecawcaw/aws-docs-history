Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GRANT

Defines access permissions for a user or role.

Permissions include access options such as being able to read data in tables and views,
write data, create tables, and drop tables. Use this command to give specific permissions
for a table, database, schema, function, procedure, language, or column. To revoke
permissions from a database object, use the [REVOKE](r_REVOKE.md "r_REVOKE.md") command.

Permissions also include the following datashare producer access options:

- Granting datashare access to consumer namespaces and accounts.
- Granting permission to alter a datashare by adding or removing objects from the
  datashare.
- Granting permission to share a datashare by adding or removing consumer
  namespaces from the datashare.
  Datashare consumer access options are as follows:

- Granting users full access to databases created from a datashare or to external
  schemas that point to such databases.
- Granting users object-level permissions on databases created from a datashare like
  you can for local database objects. To grant this level of permission, you must use
  the WITH PERMISSIONS clause when creating a database from the datashare. For more
  information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").
  For more information about datashare permissions, see [Permissions you can grant to datashares](permissions-datashares.md "permissions-datashares.md").

Permissions also include the following Amazon Redshift Federated Permissions Catalog:

- Granting table-level permissions to users and roles.
- Granting fine-grained column-level permissions on tables, views and materialized views.
- Granting scoped permissions to users and roles.
- Granting database-level permissions on Amazon Redshift Federated Permissions Catalog.
  For more information about managing permissions on Amazon Redshift Federated Permissions Catalog,
  see [Managing access control on Amazon Redshift federated permissions catalog](federated-permissions-managing-access.md "federated-permissions-managing-access.md").
  For more information about Amazon Redshift Federated Permissions Catalog supported grant/revoke syntaxes, see
  [Grant/Revoke](federated-permissions-managing-access.md#federated-permissions-managing-access-grant-revoke "federated-permissions-managing-access.md#federated-permissions-managing-access-grant-revoke").

Permissions also include the CONNECT privilege for AWS IAM Identity Center federated users.
This privilege enables administrators to control user access through granular permissions at each Amazon Redshift workgroup(s) or cluster(s) where Amazon Redshift Federated Permissions are enabled.
Amazon Redshift administrator can specify which AWS IAM Identity Center federated user(s) or group(s)
have access to directly connect to the Amazon Redshift workgroup, providing
fine-grained control over the AWS IAM Identity Center user access at each workgroup or cluster.

You can also grant roles to manage database permissions and control what users can do
relative to your data. By defining roles and assigning roles to users, you can limit the
the actions those users can take, such as limiting users to only the CREATE TABLE and
INSERT commands. For more information about the CREATE ROLE command, see [CREATE ROLE](r_CREATE_ROLE.md "r_CREATE_ROLE.md"). Amazon Redshift has some system-defined roles that you can also use
to grant specific permissions to your users. For more information, see [Amazon Redshift system-defined roles](r_roles-default.md "r_roles-default.md").

You can only GRANT or REVOKE USAGE permissions on an external schema to database users
and user groups that use the ON SCHEMA syntax. When using ON EXTERNAL SCHEMA with AWS Lake Formation,
you can only GRANT and REVOKE permissions to an AWS Identity and Access Management (IAM) role. For the list of
permissions, see the syntax.

For stored procedures, the only permission that you can grant is EXECUTE.

You can't run GRANT (on an external resource) within a transaction block (BEGIN ...
END). For more information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

To see which permissions users have been granted for a database, use [HAS_DATABASE_PRIVILEGE](r_HAS_DATABASE_PRIVILEGE.md "r_HAS_DATABASE_PRIVILEGE.md"). To see
which permissions users have been granted for a schema, use [HAS_SCHEMA_PRIVILEGE](r_HAS_SCHEMA_PRIVILEGE.md "r_HAS_SCHEMA_PRIVILEGE.md"). To see which
permissions users have been granted for a table, use [HAS_TABLE_PRIVILEGE](r_HAS_TABLE_PRIVILEGE.md "r_HAS_TABLE_PRIVILEGE.md").

## Syntax

```
GRANT { { SELECT | INSERT | UPDATE | DELETE | DROP | REFERENCES | ALTER | TRUNCATE } [,...] | ALL [ PRIVILEGES ] }
    ON { [ TABLE ] *table\_name* [, ...] | ALL TABLES IN SCHEMA *schema\_name* [, ...] }
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { { CREATE | USAGE | TEMPORARY | TEMP | ALTER } [,...] | ALL [ PRIVILEGES ] }
    ON DATABASE *db\_name* [, ...]
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
    ON SCHEMA *schema\_name* [, ...]
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
    ON { FUNCTION *function\_name* ( [ [ *argname* ] *argtype* [, ...] ] ) [, ...] | ALL FUNCTIONS IN SCHEMA *schema\_name* [, ...] }
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
    ON { PROCEDURE *procedure\_name* ( [ [ *argname* ] *argtype* [, ...] ] ) [, ...] | ALL PROCEDURES IN SCHEMA *schema\_name* [, ...] }
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT USAGE
    ON LANGUAGE *language\_name* [, ...]
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { { ALTER | DROP} [,...] | ALL [ PRIVILEGES ] }
    ON COPY JOB *job\_name* [,...]
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

```

The following is the syntax for column-level permissions on Amazon Redshift tables and
views.

```
GRANT { { SELECT | UPDATE } ( *column\_name* [, ...] ) [, ...] | ALL [ PRIVILEGES ] ( *column\_name* [,...] ) }
     ON { [ TABLE ] *table\_name* [, ...] }

     TO { *username* | ROLE *role\_name* | GROUP group_name | PUBLIC } [, ...]
```

The following is the syntax for the ASSUMEROLE permissions granted to users and
groups with a specified role. To begin using the ASSUMEROLE privilege, see [Usage notes for granting the
ASSUMEROLE permission](r_GRANT-usage-notes.md#r_GRANT-usage-notes-assumerole "r_GRANT-usage-notes.md#r_GRANT-usage-notes-assumerole").

```
GRANT ASSUMEROLE
       ON { 'iam_role' [, ...] | default | ALL }
       TO { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
       FOR { ALL | COPY | UNLOAD | EXTERNAL FUNCTION | CREATE MODEL } [, ...]
```

The following is the syntax for Redshift Spectrum integration with Lake Formation.

```
GRANT { SELECT | ALL [ PRIVILEGES ] } ( *column\_list* )
    ON EXTERNAL TABLE *schema\_name.table\_name*
    TO { IAM_ROLE *iam\_role* } [, ...] [ WITH GRANT OPTION ]

GRANT { { SELECT | ALTER | DROP | DELETE | INSERT }  [, ...] | ALL [ PRIVILEGES ] }
    ON EXTERNAL TABLE *schema\_name.table\_name* [, ...]
    TO { { IAM_ROLE *iam\_role* } [, ...] | PUBLIC } [ WITH GRANT OPTION ]

GRANT { { CREATE | ALTER | DROP }  [, ...] | ALL [ PRIVILEGES ] }
    ON EXTERNAL SCHEMA *schema\_name* [, ...]
    TO { IAM_ROLE *iam\_role* } [, ...] [ WITH GRANT OPTION ]
```

###### Producer-side datashare permissions

The following is the syntax for using GRANT to grant ALTER or SHARE
permissions to a user or role. The user can alter the datashare with the ALTER
permission, or grant usage to a consumer with the SHARE permission. ALTER and
SHARE are the only permissions that you can grant on a datashare to users and
roles.

```
GRANT { ALTER | SHARE } ON DATASHARE *datashare\_name*
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP `group_name` | PUBLIC } [, ...]
```

The following is the syntax for using GRANT for datashare usage permissions on
Amazon Redshift. You grant access to a datashare to a consumer using the USAGE permission.
You can't grant this permission to users or user groups. This permission also
doesn't support the WITH GRANT OPTION for the GRANT statement. Only users or user
groups with the SHARE permission previously granted to them FOR the datashare can
run this type of GRANT statement.

```
GRANT USAGE
    ON DATASHARE *datashare\_name*
    TO NAMESPACE *'namespaceGUID'* | ACCOUNT *'accountnumber'* [ VIA DATA CATALOG ]
```

The following is an example of how to grant usage of a datashare to a Lake Formation
account.

```
GRANT USAGE ON DATASHARE salesshare TO ACCOUNT '123456789012' VIA DATA CATALOG;
```

###### Consumer-side datashare permissions

The following is the syntax for GRANT data-sharing usage permissions on a
specific database or schema created from a datashare.

Further permissions required for consumers to access a database created from a
datashare vary depending on whether or not the CREATE DATABASE command used to
create the database from the datashare used the WITH PERMISSIONS clause. For more
information about the CREATE DATABASE command and WITH PERMISSIONS clause, see
[CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

###### Databases created without using the WITH PERMISSIONS clause

When you grant USAGE on a database created from a datashare without the WITH
PERMISSIONS clause, you don't need to grant permissions separately on the
objects in the shared database. Entities granted usage on databases created
from datashares without the WITH PERMISSIONS clause automatically have access
to all objects in the database.

###### Databases created using the WITH PERMISSIONS clause

When you grant USAGE on a database where the shared database was created
from a datashare with the WITH PERMISSIONS clause, consumer-side identities
must still be granted the relevant permissions for database objects in the
shared database in order to access them, just as you would grant permissions
for local database objects. To grant permissions to objects in a database
created from a datashare, use the three-part syntax
`database_name.schema_name.object_name`. To grant permissions to
objects in an external schema pointing to a shared schema within the shared
database, use the two-part syntax `schema_name.object_name`.

```
GRANT USAGE ON { DATABASE *shared\_database\_name* [, ...] | SCHEMA *shared\_schema*}
    TO { *username* | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]
```

Scoped permissions let you grant permissions to a user or role on
all objects of a type within a database or schema. Users and roles with scoped permissions have the specified
permissions on all current and future objects within the database or schema.

You can view the scope of database-level scoped permissions in [SVV_DATABASE_PRIVILEGES](r_SVV_DATABASE_PRIVILEGES.md "r_SVV_DATABASE_PRIVILEGES.md").
You can view the scope of schema-level scoped permissions in [SVV_SCHEMA_PRIVILEGES](r_SVV_SCHEMA_PRIVILEGES.md "r_SVV_SCHEMA_PRIVILEGES.md").

For more information about scoped permissions, see [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").

The following is the syntax for granting scoped permissions to users and
roles.

```
GRANT { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
FOR SCHEMAS IN
DATABASE db_name
TO { username [ WITH GRANT OPTION ] | ROLE role_name } [, ...]

GRANT
{ { SELECT | INSERT | UPDATE | DELETE | DROP | ALTER | TRUNCATE | REFERENCES } [, ...] } | ALL [PRIVILEGES] } }
FOR TABLES IN
{SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
TO { username [ WITH GRANT OPTION ] | ROLE role_name} [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
FOR FUNCTIONS IN
{SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
TO { username [ WITH GRANT OPTION ] | ROLE role_name | } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
FOR PROCEDURES IN
{SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
TO { username [ WITH GRANT OPTION ] | ROLE role_name | } [, ...]

GRANT USAGE
FOR LANGUAGES IN
{DATABASE db_name}
TO { username [ WITH GRANT OPTION ] | ROLE role_name } [, ...]

GRANT { { CREATE | ALTER | DROP} [,...] | ALL [ PRIVILEGES ] }
FOR COPY JOBS
IN DATABASE *db\_name*
TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* } [, ...]

```

Note that scoped permissions don’t distinguish between permissions for
functions and for procedures. For example, the following statement grants
`bob` the `EXECUTE` permission for both functions and
procedures in the schema `Sales_schema`.

```
GRANT EXECUTE FOR FUNCTIONS IN SCHEMA Sales_schema TO bob;
```

The following is the syntax for machine learning model permissions on
Amazon Redshift.

```
GRANT CREATE MODEL
    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP *group\_name* | PUBLIC } [, ...]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
    ON MODEL *model\_name* [, ...]

    TO { *username* [ WITH GRANT OPTION ] | ROLE *role\_name* | GROUP group_name | PUBLIC } [, ...]
```

The following is the syntax for granting roles on Amazon Redshift.

```
GRANT { ROLE *role\_name* } [, ...] TO { { *user\_name* [ WITH ADMIN OPTION ] } | ROLE *role\_name* }[, ...]
```

The following is the syntax for granting system permissions to roles on Amazon Redshift.
Note that you can only grant permissions to roles, not users.

```
GRANT
  {
    { CREATE USER | DROP USER | ALTER USER |
    CREATE SCHEMA | DROP SCHEMA |
    ALTER DEFAULT PRIVILEGES |
    ACCESS CATALOG | ACCESS SYSTEM TABLE
    CREATE TABLE | DROP TABLE | ALTER TABLE |
    CREATE OR REPLACE FUNCTION | CREATE OR REPLACE EXTERNAL FUNCTION |
    DROP FUNCTION |
    CREATE OR REPLACE PROCEDURE | DROP PROCEDURE |
    CREATE OR REPLACE VIEW | DROP VIEW |
    CREATE MODEL | DROP MODEL |
    CREATE DATASHARE | ALTER DATASHARE | DROP DATASHARE |
    CREATE LIBRARY | DROP LIBRARY |
    CREATE ROLE | DROP ROLE |
    TRUNCATE TABLE
    VACUUM | ANALYZE | CANCEL |
    IGNORE RLS | EXPLAIN RLS |
    EXPLAIN MASKING }[, ...]
  }
  | { ALL [ PRIVILEGES ] }
TO ROLE *role\_name* [, ...]
```

The following is the syntax for granting permissions to explain the
security policy filters of a query in the EXPLAIN plan.
Possible security policies include row-level security policies
and dynamic data masking policies.

```
GRANT EXPLAIN { RLS | MASKING } TO ROLE *rolename*
```

The following is the syntax for granting permissions to bypass row-level
security policies for a query. This syntax doesn't apply to dynamic data masking policies.

```
GRANT IGNORE RLS TO ROLE *rolename*
```

The following is the syntax for granting lookup table permissions to the specified
security policy. Possible security policies include row-level security policies
and dynamic data masking policies.

```
GRANT SELECT ON [ TABLE ] *table\_name* [, ...]
TO { RLS | MASKING } POLICY *policy\_name* [, ...]
```

The following is the syntax for granting permissions for AWS IAM Identity Center federated users (or groups) to connect to a workgroup/cluster:

```
GRANT CONNECT [ON WORKGROUP]
TO [USER] *<prefix>:<username>* | ROLE *<prefix>:<rolename>* | PUBLIC;
```

## Parameters

SELECT

Grants permission to select data from a table or view using a SELECT
statement. The SELECT permission is also required to reference existing column
values for UPDATE or DELETE operations.

INSERT

Grants permission to load data into a table using an INSERT statement or a
COPY statement.

UPDATE

Grants permission to update a table column using an UPDATE statement. UPDATE
operations also require the SELECT permission, because they must reference
table columns to determine which rows to update, or to compute new values for
columns.

DELETE

Grants permission to delete a data row from a table. DELETE operations also
require the SELECT permission, because they must reference table columns to
determine which rows to delete.

DROP

Depending on the database object, grants the following permissions to the
user or role:

- For tables, DROP grants permission to drop a table or view. For more
  information, see [DROP TABLE](r_DROP_TABLE.md "r_DROP_TABLE.md").
- For databases, DROP grants permission to drop a database. For more
  information, see [DROP DATABASE](r_DROP_DATABASE.md "r_DROP_DATABASE.md").
- For schemas, DROP grants permission to drop a schema. For more
  information, see [DROP SCHEMA](r_DROP_SCHEMA.md "r_DROP_SCHEMA.md").

REFERENCES

Grants permission to create a foreign key constraint. You need to grant this
permission on both the referenced table and the referencing table; otherwise,
the user can't create the constraint.

ALTER

Depending on the database object, grants the following permissions to the
user or user group:

- For tables, ALTER grants permission to alter a table or view. For more
  information, see [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").
- For databases, ALTER grants permission to alter a database. For more
  information, see [ALTER DATABASE](r_ALTER_DATABASE.md "r_ALTER_DATABASE.md").
- For schemas, ALTER grants permission to alter a schema. For more
  information, see [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md").
- For external tables, ALTER grants permission to alter a table in an
  AWS Glue Data Catalog that is enabled for Lake Formation. This permission only applies when
  using Lake Formation.

TRUNCATE

Grants permission to truncate a table. Without this permission, only the
owner of a table or a superuser can truncate a table. For more information
about the TRUNCATE command, see [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md").

ALL [ PRIVILEGES ]

Grants all available permissions at once to the specified user or role. The
PRIVILEGES keyword is optional.

GRANT ALL ON SCHEMA doesn't grant CREATE permissions for external
schemas.

You can grant the ALL permission to a table in an AWS Glue Data Catalog that is
enabled for Lake Formation. In this case, individual permissions (such as SELECT, ALTER,
and so on) are recorded in the Data Catalog.

###### Note

Amazon Redshift doesn't support the RULE and TRIGGER permissions. For more
information, go to [Unsupported PostgreSQL
features](c_unsupported-postgresql-features.md "c_unsupported-postgresql-features.md").

ASSUMEROLE

Grants permission to run COPY, UNLOAD, EXTERNAL FUNCTION, and CREATE MODEL
commands to users, roles, or groups with a specified role. The user, role, or
group assumes that role when running the specified command. To begin using the
ASSUMEROLE permission, see [Usage notes for granting the
ASSUMEROLE permission](r_GRANT-usage-notes.md#r_GRANT-usage-notes-assumerole "r_GRANT-usage-notes.md#r_GRANT-usage-notes-assumerole").

ON [ TABLE ] _table_name_

Grants the specified permissions on a table or a view. The TABLE keyword is
optional. You can list multiple tables and views in one statement.

ON ALL TABLES IN SCHEMA _schema_name_

Grants the specified permissions on all tables and views in the referenced
schema.

( _column_name_ [,...] ) ON TABLE
_table_name_

Grants the specified permissions to users, groups, or PUBLIC on the
specified columns of the Amazon Redshift table or view.

( _column_list_ ) ON EXTERNAL TABLE
_schema_name.table_name_

Grants the specified permissions to an IAM role on the specified columns of
the Lake Formation table in the referenced schema.

ON EXTERNAL TABLE _schema_name.table_name_

Grants the specified permissions to an IAM role on the specified Lake Formation tables
in the referenced schema.

ON EXTERNAL SCHEMA _schema_name_

Grants the specified permissions to an IAM role on the referenced
schema.

ON _iam_role_

Grants the specified permissions to an IAM role.

TO _username_

Indicates the user receiving the permissions.

TO IAM_ROLE _iam_role_

Indicates the IAM role receiving the permissions.

WITH GRANT OPTION

Indicates that the user receiving the permissions can in turn grant the same
permissions to others. WITH GRANT OPTION can't be granted to a group or to
PUBLIC.

ROLE _role_name_

Grants the permissions to a role.

GROUP _group_name_

Grants the permissions to a user group. Can be a comma-separated list to
specify multiple user groups.

PUBLIC

Grants the specified permissions to all users, including users created
later. PUBLIC represents a group that always includes all users. An individual
user's permissions consist of the sum of permissions granted to PUBLIC,
permissions granted to any groups that the user belongs to, and any permissions
granted to the user individually.

Granting PUBLIC to a Lake Formation EXTERNAL TABLE results in granting the permission
to the Lake Formation _everyone_ group.

CONNECT [ON WORKGROUP] TO { [USER] <prefix>:<username> | ROLE <prefix>:<rolename> | PUBLIC }

Grants the permission to connect to a workgroup or cluster to AWS IAM Identity Center federated
users or groups. The prefix identifies the identity provider. When granted to PUBLIC, the
permission applies to all AWS IAM Identity Center federated users, including users created later.
This permission is applicable only when Amazon Redshift Federated Permissions are enabled on
the workgroup or cluster.

CREATE

Depending on the database object, grants the following permissions to the
user or user group:

- For databases, CREATE allows users to create schemas within the
  database.
- For schemas, CREATE allows users to create objects within a schema. To
  rename an object, the user must have the CREATE permission and own the
  object to be renamed.
- CREATE ON SCHEMA isn't supported for Amazon Redshift Spectrum external
  schemas. To grant usage of external tables in an external schema, grant
  USAGE ON SCHEMA to the users that need access. Only the owner of an
  external schema or a superuser is permitted to create external tables in
  the external schema. To transfer ownership of an external schema, use
  [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md") to
  change the owner.

TEMPORARY | TEMP

Grants the permission to create temporary tables in the specified database.
To run Amazon Redshift Spectrum queries, the database user must have permission to create
temporary tables in the database.

###### Note

By default, users are granted permission to create temporary tables by
their automatic membership in the PUBLIC group. To remove the permission for
any users to create temporary tables, revoke the TEMP permission from the
PUBLIC group. Then explicitly grant the permission to create temporary
tables to specific users or groups of users.

ON DATABASE _db_name_

Grants the specified permissions on a database.

USAGE

Grants USAGE permission on a specific schema, which makes objects in that
schema accessible to users. Specific actions on these objects must be granted
separately (for example, SELECT or UPDATE permission on tables) for local
Amazon Redshift schemas. By default, all users have CREATE and USAGE permission on the
PUBLIC schema.

When you grant USAGE to external schemas using ON SCHEMA syntax, you don't
need to grant actions separately on the objects in the external schema. The
corresponding catalog permissions control granular permissions on the external
schema objects.

ON SCHEMA _schema_name_

Grants the specified permissions on a schema.

GRANT CREATE ON SCHEMA and the CREATE permission in GRANT ALL ON SCHEMA
aren't supported for Amazon Redshift Spectrum external schemas. To grant usage of
external tables in an external schema, grant USAGE ON SCHEMA to the users that
need access. Only the owner of an external schema or a superuser is permitted
to create external tables in the external schema. To transfer ownership of an
external schema, use [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md") to change the owner.

EXECUTE ON ALL FUNCTIONS IN SCHEMA _schema_name_

Grants the specified permissions on all functions in the referenced
schema.

Amazon Redshift doesn't support GRANT or REVOKE statements for pg_proc builtin
entries defined in pg_catalog namespace.

EXECUTE ON PROCEDURE _procedure_name_

Grants the EXECUTE permission on a specific stored procedure. Because stored
procedure names can be overloaded, you must include the argument list for the
procedure. For more information, see [Naming stored procedures](stored-procedure-naming.md "stored-procedure-naming.md").

EXECUTE ON ALL PROCEDURES IN SCHEMA _schema_name_

Grants the specified permissions on all stored procedures in the referenced
schema.

USAGE ON LANGUAGE _language_name_

Grants the USAGE permission on a language.

###### Note

Starting November 1, 2025,
Amazon Redshift will no longer support the creation of new Python UDFs.
Existing Python UDFs will continue to function until June 30, 2026.
Starting July 1, 2026, Amazon Redshift will no longer support Python
UDFs. We recommend that you migrate your existing Python UDFs to Lambda UDFs before November 1, 2025.
For information on creating and using Lambda UDFs, see [Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md").
For information on converting existing Python UDFs to
Lambda UDFs, see the [blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

The USAGE ON LANGUAGE permission is required to create user-defined
functions (UDFs) by running the [CREATE FUNCTION](r_CREATE_FUNCTION.md "r_CREATE_FUNCTION.md") command. For more information, see [UDF security and permissions](udf-security-and-privileges.md "udf-security-and-privileges.md").

The USAGE ON LANGUAGE permission is required to create stored procedures by
running the [CREATE PROCEDURE](r_CREATE_PROCEDURE.md "r_CREATE_PROCEDURE.md") command. For more information, see
[Security and privileges for
stored procedures](stored-procedure-security-and-privileges.md "stored-procedure-security-and-privileges.md") .

For Python UDFs, use `plpythonu`. For SQL UDFs, use
`sql`. For stored procedures, use `plpgsql`.

ON COPY JOB _job_name_

Grants the specified permissions on a copy job.

FOR { ALL | COPY | UNLOAD | EXTERNAL FUNCTION | CREATE MODEL } [, ...]

Specifies the SQL command for which the permission is granted. You can
specify ALL to grant the permission on the COPY, UNLOAD, EXTERNAL FUNCTION, and
CREATE MODEL statements. This clause applies only to granting the ASSUMEROLE
permission.

ALTER

Grants the ALTER permission to users to add or remove objects from a
datashare, or to set the property PUBLICACCESSIBLE. For more information, see
[ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

SHARE

Grants pemrissions to users and user groups to add data consumers to a
datashare. This permission is required to enable the particular consumer
(account or namespace) to access the datashare from their clusters. The
consumer can be the same or a different AWS account, with the same or a
different cluster namespace as specified by a globally unique identifier
(GUID).

ON DATASHARE _datashare_name_

Grants the specified permissions on the referenced datashare. For
information about consumer access control granularity, see [Data sharing at different levels in Amazon Redshift](datashare-overview.md#granularity "datashare-overview.md#granularity").

USAGE

When USAGE is granted to a consumer account or namespace within the same
account, the specific consumer account or namespace within the account can
access the datashare and the objects of the datashare in read-only fashion.

TO NAMESPACE 'clusternamespace GUID'

Indicates a namespace in the same account where consumers can receive the
specified permissions to the datashare. Namespaces use a 128-bit alphanumeric
GUID.

TO ACCOUNT 'accountnumber' [ VIA DATA CATALOG ]

Indicates the number of another account whose consumers can receive the
specified permissions to the datashare. Specifying ‘VIA DATA CATALOG’ indicates
that you are granting usage of the datashare to a Lake Formation account. Omitting this
parameter means you're granting usage to an account that owns the
cluster.

ON DATABASE _shared_database_name> [, ...]_

Grants the specified usage permissions on the specified database that is
created in the specified datashare.

ON SCHEMA _shared_schema_

Grants the specified permissions on the specified schema that is created in
the specified datashare.

FOR { SCHEMAS | TABLES | FUNCTIONS | PROCEDURES | LANGUAGES | COPY JOBS} IN

Specifies the database objects to grant permission to. The parameters
following IN define the scope of the granted permission.

CREATE MODEL

Grants the CREATE MODEL permission to specific users or user groups.

ON MODEL _model_name_

Grants the EXECUTE permission on a specific model.

ACCESS CATALOG

Grants the permission to view relevant metadata of objects that the role has
access to.

{ role } [, ...]

The role to be granted to another role, a user, or PUBLIC.

PUBLIC represents a group that always includes all users. An individual
user's permissions consist of the sum of permissions granted to PUBLIC,
permissions granted to any groups that the user belongs to, and any permissions
granted to the user individually.

TO { { _user_name_ [ WITH ADMIN OPTION ] } | role }[,
...]

Grants the specified role to a specified user with the WITH ADMIN OPTION,
another role, or PUBLIC.

The WITH ADMIN OPTION clause provides the administration options for all the
granted roles to all the grantees.

EXPLAIN { RLS | MASKING } TO ROLE _rolename_

Grants the permission to explain the security policy filters of a
query in the EXPLAIN plan to a role. RLS grants permission to explain row-level security policy filters.
MASKING grants permission to explain dynamic data masking policy filters.

IGNORE RLS TO ROLE _rolename_

Grants the permission to bypass row-level security policies for a query to a
role.

TO { RLS | MASKING } POLICY _policy_name_
Indicates the security policy receiving the permissions.
TO RLS POLICY indicates a row-level security policy. TO MASKING POLICY indicates
a dynamic data masking policy.

## Usage notes

To learn more about the usage notes for GRANT, see [Usage notes](r_GRANT-usage-notes.md "r_GRANT-usage-notes.md").

## Examples

For examples of how to use GRANT, see [Examples](r_GRANT-examples.md "r_GRANT-examples.md").
