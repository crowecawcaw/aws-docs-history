# Connecting to Babelfish

via TDS endpoint

In the following example, user1 is member of accounts-group and sales-group, user2 is
member of accounts-group and dev-group.

| Username | AD Security Groups membership |
| -------- | ----------------------------- |
| user1    | accounts-group, sales-group   |
| user2    | accounts-group, dev-group     |

Connect to Babelfish database server using sqlcmd utility. You can verify if
an user (user1 in this example) was authenticated using Kerberos by following the
example below:

```
`1>` select principal, gss_authenticated from pg_stat_gssapi where pid = pg_backend_pid();
`2>`  GO
principal               gss_authenticated
----------------------  -----------------
user1@CORP.EXAMPLE.COM  1

((1 rows affected))
`1>` select suser_name();
`2>`  GO
suser_name
----------
corp\user1

(1 rows affected)
```

In this example, user1 will inherit the privileges of accounts-group and sales-group.
You can verify the group membership using `sys.login_token` system view.

```
`1>` SELECT name, type FROM sys.login_token;
`2>`  GO
name                type
------------------- ----
corp\accounts-group WINDOWS GROUP
corp\sales-group    WINDOWS GROUP

(2 rows affected)
```
