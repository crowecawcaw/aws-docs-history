# Handling DDL Statement behavior

based on default or explicit schema

When using an AD authenticated session, the default schema for the current session is
determined by the following conditions:

- If an individual database user exists, the user's default schema is considered
  as current session’s default schema.
- If the default schema for a group database user exists, the group database
  user's default schema is considered as current session’s default schema with the
  smallest principal id.

## Understanding CREATE DDL

statement behavior

If there is no explicit schema specified in the CREATE DDL statement then object
creation will take place in the default schema of current session. If the schema
can't be determined whether default or explicit, then the DDL statement will throw
following error:

```

`"Babelfish Unsupported Command : Schema required for CREATE DDLs when connecting with Active Directory Group authentication. Assign default schema to group user or specify schema in command."`

```

###### Example: Default schema doesn’t exist for Windows group user

Windows group user [corp\accounts-group] have NULL default schema and AD user
user1 is trying to perform the DDL without specifying the schema explicitly.
Since individual windows login and user doesn’t exist for user1, it will get the
database level privileges of Windows group user [corp\accounts-group]
only.

```

`1>` create TABLE t2(a int);
`2>` GO
`Msg 33557097, Level 16, State 1, Server db-inst, Line 1
Babelfish Unsupported Command : Schema required for CREATE DDLs when connecting with Active Directory Group authentication. Assign default schema to group user or specify schema in command.`

```

###### Note

Individual windows login and user doesn’t exist for AD user user1

###### Example: Default schema exists for Windows group users

Create Windows group user for [corp\accounts-group] login with default schema
using sysadmin.

```

`1>` CREATE USER [corp\accounts-group] FOR LOGIN [corp\accounts-group] WITH DEFAULT_SCHEMA = sch_acc;
`2>` GO
`1>` CREATE SCHEMA sch_acc AUTHORIZATION [gad\accounts-group];
`2>` GO
`1>` SELECT name, principal_id, default_schema_name FROM sys.database_principals WHERE name = 'corp\accounts-group';
`2>` GO
 `name principal_id default_schema_name
------------------ ------------ -------------------
corp\accounts-group 24162 sch_acc

(1 rows affected)`

```

Try creating object without specifying schema explicitly using AD user user1.
Table t2 will be created in default schema of [corp\accounts-group] Windows
group user Owner of this object will be same as owner of schema sch_acc.

```

`1>` CREATE TABLE t_group(a int);
`2>` GO
`1>` SELECT name, schema_name(schema_id) FROM sys.objects WHERE name like 't_group';
`2>` GO
`name schema_name
------- -----------
t_group sch_acc

(1 rows affected)`

```

###### Note

Individual windows login and user doesn’t exist for AD user user1

###### Example: Individual database user also exists for an AD user

If an individual database user also exists for an AD user then the objects
will always be created in the schema associated with individual database user.
If the schema doesn’t exist for the database user then dbo schema will be used.
Create individual windows login and database user for AD user user1. Connect
through TDS endpoint using a sysadmin login

```

`1>` CREATE LOGIN [corp\user1] FROM WINDOWS;
`2>` GO
`1>` CREATE USER [corp\user1] FOR LOGIN [corp\user1] WITH DEFAULT_SCHEMA = sch1;
`2>` GO
`1>` CREATE SCHEMA sch1 AUTHORIZATION [corp\user1];
`2>` GO
`1>` SELECT name, default_schema_name FROM sys.database_principals WHERE name = 'corp\user1';
`2>` GO
`name default_schema_name
--------- -------------------
corp\user1 sch1

(1 rows affected)`

```

Connect using AD user user1 and try creating object without specifying schema
explicitly. Table t2 will be created in schema sch1. Also note that owner of
this object will be same as owner of schema sch1.

```

`1>` CREATE TABLE t2(a int);
`2>` GO
`1>` SELECT name, schema_name(schema_id) FROM sys.objects WHERE name like 't2';
`2>` GO
 `name schema_name
---- -----------
t2 sch1

(1 rows affected)`

```
