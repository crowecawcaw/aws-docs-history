# Delegating and

controlling user password management

As a DBA, you might want to delegate the management of user passwords. Or, you might want
to prevent database users from changing their passwords or reconfiguring password constraints,
such as password lifetime. To ensure that only the database users that you choose can change
password settings, you can turn on the restricted password management feature. When you
activate this feature, only those database users that have been granted the
`rds_password` role can manage passwords.

###### Note

To use restricted password management, your
Aurora PostgreSQL DB cluster must be running Amazon Aurora
PostgreSQL 10.6 or higher.

By default, this feature is `off`, as shown in the following:

```
`postgres=>` `SHOW rds.restrict_password_commands;`
 `rds.restrict_password_commands
--------------------------------
 off
(1 row)`
```

To turn on this feature, you use a custom parameter group and change the setting for
`rds.restrict_password_commands` to 1. Be sure to reboot your Aurora PostgreSQL's primary DB instance
so that the setting takes
effect.

With this feature active, `rds_password` privileges are needed for the
following SQL commands:

```
CREATE ROLE myrole WITH PASSWORD 'mypassword';
CREATE ROLE myrole WITH PASSWORD 'mypassword' VALID UNTIL '2023-01-01';
ALTER ROLE myrole WITH PASSWORD 'mypassword' VALID UNTIL '2023-01-01';
ALTER ROLE myrole WITH PASSWORD 'mypassword';
ALTER ROLE myrole VALID UNTIL '2023-01-01';
ALTER ROLE myrole RENAME TO myrole2;
```

Renaming a role (`ALTER ROLE myrole RENAME TO newname`) is also restricted if
the password uses the MD5 hashing algorithm.

With this feature active, attempting any of these SQL commands without the
`rds_password` role permissions generates the following error:

```
ERROR: must be a member of rds_password to alter passwords
```

We recommend that you grant the `rds_password` to only a few roles that you use
solely for password management. If you grant `rds_password` privileges to database
users that don't have `rds_superuser` privileges, you need to also grant them
the `CREATEROLE` attribute.

Make sure that you verify password requirements such as expiration and needed complexity
on the client side. If you use your own client-side utility for password related changes, the
utility needs to be a member of `rds_password` and have `CREATE ROLE`
privileges.
