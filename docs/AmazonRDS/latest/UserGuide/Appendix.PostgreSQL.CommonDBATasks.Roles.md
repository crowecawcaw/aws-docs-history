# Understanding the

rds_superuser role

In PostgreSQL, a _role_ can define a user, a group, or a set of
specific permissions granted to a group or user for various objects in the database.
PostgreSQL commands to `CREATE USER` and `CREATE GROUP` have been
replaced by the more general, `CREATE ROLE` with specific properties to distinguish
database users. A database user can be thought of as a role with the LOGIN privilege.

###### Note

The `CREATE USER` and `CREATE GROUP` commands can still be used.
For more information, see [Database Roles](https://www.postgresql.org/docs/current/user-manag.html "https://www.postgresql.org/docs/current/user-manag.html") in
the PostgreSQL documentation.

The `postgres` user is the most highly privileged database user on your RDS for PostgreSQL DB instance. It has the characteristics defined by the following
`CREATE ROLE` statement.

```
CREATE ROLE postgres WITH LOGIN NOSUPERUSER INHERIT CREATEDB CREATEROLE NOREPLICATION VALID UNTIL 'infinity'
```

The properties `NOSUPERUSER`, `NOREPLICATION`, `INHERIT`,
and `VALID UNTIL 'infinity'` are the default options for CREATE ROLE, unless
otherwise specified.

By default, `postgres` has privileges granted to the `rds_superuser`
role, and permissions to create roles and databases. The `rds_superuser` role
allows the `postgres` user to do the following:

- Add extensions that are available for use with Amazon RDS.
  For more information, see [Working with PostgreSQL
  features supported by Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- Create roles for users and grant privileges to users. For more information, see [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html "https://www.postgresql.org/docs/current/sql-createrole.html")
  and [GRANT](https://www.postgresql.org/docs/14/sql-grant.html "https://www.postgresql.org/docs/14/sql-grant.html") in the
  PostgreSQL documentation.
- Create databases. For more information, see [CREATE DATABASE](https://www.postgresql.org/docs/14/sql-createdatabase.html "https://www.postgresql.org/docs/14/sql-createdatabase.html")
  in the PostgreSQL documentation.
- Grant `rds_superuser` privileges to user roles that don't have these
  privileges, and revoke privileges as needed. We recommend that you grant this role only to
  those users who perform superuser tasks. In other words, you can grant this role to
  database administrators (DBAs) or system administrators.
- Grant (and revoke) the `rds_replication` role to database users that
  don't have the `rds_superuser` role.
- Grant (and revoke) the `rds_password` role to database users that
  don't have the `rds_superuser` role.
- Obtain status information about all database connections by using the
  `pg_stat_activity` view. When needed, `rds_superuser` can stop any
  connections by using `pg_terminate_backend` or `pg_cancel_backend`.
  In the `CREATE ROLE postgres...` statement, you can see that the
  `postgres` user role specifically disallows PostgreSQL `superuser`
  permissions. RDS for PostgreSQL is a managed service, so you can't access the host OS, and you
  can't connect using the PostgreSQL `superuser` account. Many of the tasks that
  require `superuser` access on a stand-alone PostgreSQL are managed automatically by
  Amazon RDS.

For more information about granting privileges, see [GRANT](http://www.postgresql.org/docs/current/sql-grant.html "http://www.postgresql.org/docs/current/sql-grant.html") in the PostgreSQL
documentation.

The `rds_superuser` role is one of several _predefined_
roles in an
RDS for PostgreSQL DB instance.

###### Note

In PostgreSQL 13 and earlier releases, _predefined_ roles are known
as _default_ roles.

In the following list, you find some of the other predefined roles that are created
automatically for a new
RDS for PostgreSQL DB instance. Predefined roles and their
privileges can't be changed. You can't drop, rename, or modify privileges for these
predefined roles. Attempting to do so results in an error.

- rds_password – A role that can change passwords
  and set up password constraints for database users. The `rds_superuser` role is
  granted with this role by default, and can grant the role to database users. For more
  information, see [Controlling user access to the
  PostgreSQL database](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").
  - For RDS for PostgreSQL versions older than 14, `rds_password` role can
    change passwords and set up password constraints for database users and users with
    `rds_superuser` role. From RDS for PostgreSQL version 14 and later,
    `rds_password` role can change passwords and set up password constraints
    only for database users. Only users with `rds_superuser` role can perform
    these actions on other users with `rds_superuser` role.

- rdsadmin – A role that's created to handle
  many of the management tasks that the administrator with `superuser` privileges
  would perform on a standalone PostgreSQL database. This role is used internally by RDS for PostgreSQL for many management tasks.
- rdstopmgr – A role that's used internally
  by Amazon RDS to support Multi-AZ deployments.
- rds_reserved – A role that's used
  internally by Amazon RDS to reserve database connections.
