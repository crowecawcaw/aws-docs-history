# Utilizing privileges of AD security group membership

## Inheriting server-level privileges

AD users that are members of given AD security group will inherit server-level
privileges granted to the mapped Windows group login. For example, consider the
`accounts-group` AD security group, that is granted membership to the
`sysadmin` server role on the Babelfish. You can inherit the
server-level privileges using the following command:

```

`1>` ALTER SERVER ROLE sysadmin ADD MEMBER [corp\accounts-group];

```

Consequently, any Active Directory user who is a member of the
`accounts-group` AD security group will inherit the server-level
privileges associated with the `sysadmin` role. This means that a user
like `corp\user1`, being a member of `accounts-group`, will
now have the ability to perform server-level operations within
Babelfish.

###### Note

To perform server-level DDLs, Windows login for individual AD user must
exist. For more information, see [Limitations](babelfish-kerberos-securityad-limitations.md "babelfish-kerberos-securityad-limitations.md").

## Inheriting database-level privileges

To grant the database level privileges, a database user has to be created and
mapped with Windows group login. AD users which are members of given AD security
group will inherit database-level privileges granted to that database user. In the
following example, you can see how database level privileges for Windows group
[corp\accounts-group] are assigned.

```

`1>` CREATE DATABASE db1;
`2>` GO
`1>` USE db1;
`2>` GO
Changed database context to 'db1'.
`1>` CREATE TABLE dbo.t1(a int);
`2>` GO

```

Create a database user [corp\sales-group] for Windows group login
[corp\accounts-group]. To perform this step, connect through TDS endpoint using
login who is a member of sysadmin.

```

`1>` CREATE USER [corp\accounts-group] FOR LOGIN [corp\accounts-group];
`2>` GO

```

Now, connect as AD user user1 to check access of table t1. Since we have not yet
granted the database level privileges, it will result in permission denied error.

```

`1>` SELECT * FROM dbo.t1;
`2>` GO
Msg 33557097, Level 16, State 1, Server db-inst, Line 1
permission denied for table t1

```

Grant SELECT on table t1 to database user [corp\accounts-group]. To perform this
step, connect through TDS endpoint using login who is member of sysadmin.

```

`1>` GRANT SELECT ON dbo.t1 TO [corp\accounts-group];
`2>` GO

```

Connect as AD user user1 to validate the access.

```

`1>` SELECT * FROM dbo.t1;
`2>` GO
a
-----------

(0 rows affected)

```
