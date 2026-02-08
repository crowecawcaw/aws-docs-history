# Accessing Aurora DSQL with PostgreSQL-compatible clients

Aurora DSQL uses the [PostgreSQL
wire protocol](https://www.postgresql.org/docs/current/protocol.html "https://www.postgresql.org/docs/current/protocol.html"). You can connect to PostgreSQL using a variety of tools and clients, such as
AWS CloudShell, psql, DBeaver, and DataGrip. The following table summarizes how Aurora DSQL maps common
PostgreSQL connection parameters:

| PostgreSQL                                | Aurora DSQL                       | Notes                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role (also known as User or Group)        | Database Role                     | Aurora DSQL creates a role for you named `admin`. When you create custom database<br>roles, you must use the `admin` role to associate them with IAM roles for<br>authenticating when connecting to your cluster. For more information, see<br>[Using database roles and IAM authentication](using-database-and-iam-roles.md "using-database-and-iam-roles.md"). |
| Host (also known as hostname or hostspec) | Cluster Endpoint                  | Aurora DSQL single-Region clusters provide a single managed endpoint and automatically<br>redirect traffic if there is unavailability within the Region.                                                                                                                                                                                                         |
| Port                                      | N/A – use default `5432`          | This is the PostgreSQL default.                                                                                                                                                                                                                                                                                                                                  |
| Database (dbname)                         | use `postgres`                    | Aurora DSQL creates this database for you when you create the cluster.                                                                                                                                                                                                                                                                                           |
| SSL Mode                                  | SSL is always enabled server-side | In Aurora DSQL, Aurora DSQL supports the `require` SSL Mode. Connections without SSL<br>are rejected by Aurora DSQL.                                                                                                                                                                                                                                             |
| Password                                  | Authentication Token              | Aurora DSQL requires temporary authentication tokens instead of long-lived passwords. To<br>learn more, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").                                                                                                                       |

When connecting, Aurora DSQL requires a signed IAM [authentication
token](SECTION_authentication-token.md "SECTION_authentication-token.md") in place of a traditional password. These temporary tokens are generated using
AWS Signature Version 4 and are used only during connection establishment. Once connected, the
session remains active until it ends or the client disconnects.

If you attempt to open a new session with an expired token, the connection request fails and
a new token must be generated. For more information, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").

## Access Aurora DSQL using SQL clients

Aurora DSQL supports multiple PostgreSQL-compatible clients for connecting to your cluster. The
following sections describe how to connect using PostgreSQL with AWS CloudShell or your local command
line, as well as GUI-based tools like DBeaver and JetBrains DataGrip. Each client requires a
valid authentication token as described in the previous section.

###### Topics

- [Use DBeaver to access Aurora DSQL](accessing-dbeaver.md "accessing-dbeaver.md")
- [Use JetBrains DataGrip to access Aurora DSQL](accessing-datagrip.md "accessing-datagrip.md")
- [Use the PostgreSQL interactive terminal (psql) to access Aurora DSQL](accessing-psql.md "accessing-psql.md")
- [Use Aurora DSQL driver for SQLTools](accessing-vscode.md "accessing-vscode.md")
- [Troubleshooting](#accessing-troubleshooting "#accessing-troubleshooting")

## Troubleshooting

**Authentication credentials expiration for the SQL
Clients**

Established sessions remain authenticated for a maximum of 1 hour or until an explicit
disconnect or a client-side timeout takes place. If new connections need to be established, a
new authentication token must be generated and provided in the **Password** field of the connection. Trying to open a new session (for example, to list
new tables, or open a new SQL console) forces a new authentication attempt. If the authentication
token configured in the **Connection** settings is no longer valid,
that new session will fail and all previously opened sessions will become invalid. Keep this in
mind when choosing the duration of your IAM authentication token with the
`expires-in` option, which can be set to 15 minutes by default and can be set to a
maximum value of seven days.

Additionally, see the [Troubleshooting](troubleshooting.md "troubleshooting.md") section of the
Aurora DSQL documentation.
