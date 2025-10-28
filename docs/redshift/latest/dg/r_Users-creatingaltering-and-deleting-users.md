Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating, altering, and

deleting users

Database users are global across a data warehouse cluster (and not for each
individual database).

- To create a user, use the [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md") command.
- To create a superuser, use the [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md") command with the CREATEUSER option.
- To remove an existing user, use the [DROP USER](r_DROP_USER.md "r_DROP_USER.md") command.
- To change a user, for example changing a password, use the [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md") command.
- To view a list of users, query the PG_USER catalog table.

```
select * from pg_user;

  usename   | usesysid | usecreatedb | usesuper | usecatupd |  passwd  | valuntil | useconfig
------------+----------+-------------+----------+-----------+----------+----------+-----------
 rdsdb      |        1 | t           | t        | t         | ******** |          |
 masteruser |      100 | t           | t        | f         | ******** |          |
 dwuser     |      101 | f           | f        | f         | ******** |          |
 simpleuser |      102 | f           | f        | f         | ******** |          |
 poweruser  |      103 | f           | t        | f         | ******** |          |
 dbuser     |      104 | t           | f        | f         | ******** |          |
(6 rows)
```
