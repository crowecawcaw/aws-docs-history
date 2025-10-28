# Database authentication with

Babelfish for Aurora PostgreSQL

Babelfish for Aurora PostgreSQL supports two ways to authenticate database users. Password
authentication is available by default for all Babelfish DB clusters. You can
also add Kerberos authentication for the same DB cluster.

###### Topics

- [Password authentication with
  Babelfish](#babelfish-authentication "#babelfish-authentication")
- [Kerberos authentication with Babelfish](babelfish-active-directory.md "babelfish-active-directory.md")
- [Setting up Kerberos authentication using
  Active Directory security groups for Babelfish](babelfish-kerberos-securityad.md "babelfish-kerberos-securityad.md")

## Password authentication with

Babelfish

Babelfish for Aurora PostgreSQL supports password authentication. Passwords are stored in
encrypted form on disk. For more information about authentication on an
Aurora PostgreSQL cluster, see [Security with Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

You might be prompted for credentials each time you connect to Babelfish.
Any user migrated to or created on Aurora PostgreSQL can use the same credentials on
both the SQL Server port and the PostgreSQL port. Babelfish doesn't
enforce password policies, but we recommend that you do the following:

- Require a complex password that's at least eight (8) characters
  long.
- Enforce a password expiration policy.

To review a complete list of database users, use the command `SELECT * FROM
 pg_user;`.
