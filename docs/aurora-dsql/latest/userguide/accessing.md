# Accessing Aurora DSQL with PostgreSQL-compatible clients

Aurora DSQL uses the [PostgreSQL
wire protocol](https://www.postgresql.org/docs/current/protocol.html "https://www.postgresql.org/docs/current/protocol.html"). You can connect to PostgreSQL using a variety of tools and clients, such as
AWS CloudShell, psql, DBeaver, and DataGrip. The following table summarizes how Aurora DSQL maps common
PostgreSQL connection parameters:

| PostgreSQL                                | Aurora DSQL                       | Notes                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role (also known as User or Group)        | Database Role                     | Aurora DSQL creates a role for you named `admin`. When you create custom database<br>roles, you must use the `admin` role to associate them with IAM roles for<br>authenticating when connecting to your cluster. For more information, see [Configure custom database roles](using-database-and-iam-roles.md "using-database-and-iam-roles.md"). |
| Host (also known as hostname or hostspec) | Cluster Endpoint                  | Aurora DSQL single-Region clusters provide a single managed endpoint and automatically<br>redirect traffic if there is unavailability within the Region.                                                                                                                                                                                          |
| Port                                      | N/A – use default `5432`          | This is the PostgreSQL default.                                                                                                                                                                                                                                                                                                                   |
| Database (dbname)                         | use `postgres`                    | Aurora DSQL creates this database for you when you create the cluster.                                                                                                                                                                                                                                                                            |
| SSL Mode                                  | SSL is always enabled server-side | In Aurora DSQL, Aurora DSQL supports the `require` SSL Mode. Connections without SSL<br>are rejected by Aurora DSQL.                                                                                                                                                                                                                              |
| Password                                  | Authentication Token              | Aurora DSQL requires temporary authentication tokens instead of long-lived passwords. To<br>learn more, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").                                                                                                        |

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

- [Use AWS CloudShell to access Aurora DSQL with the PostgreSQL
  interactive terminal (psql)](#accessing-sql-clients-psql "#accessing-sql-clients-psql")
- [Use the local CLI to access Aurora DSQL with the
  PostgreSQL interactive terminal (psql)](#accessing-sql-clients-psql-local "#accessing-sql-clients-psql-local")
- [Use DBeaver to access Aurora DSQL](#accessing-sql-clients-dbeaver "#accessing-sql-clients-dbeaver")
- [Use JetBrains
  DataGrip to access Aurora DSQL](#accessing-sql-clients-datagrip "#accessing-sql-clients-datagrip")
- [Troubleshooting](#accessing-troubleshooting "#accessing-troubleshooting")

## Use AWS CloudShell to access Aurora DSQL with the PostgreSQL

interactive terminal (psql)

Use the following procedure to access Aurora DSQL with the PostgreSQL interactive terminal from
AWS CloudShell. For more information, see [What is AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md").

###### To connect using AWS CloudShell

1. Sign in to the [Aurora DSQL
   console](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. Choose the cluster for which you would like to open in CloudShell. If you haven't yet
   created a cluster, follow the steps in [Step 1: Create an Aurora DSQL single-Region
   cluster](getting-started.md#getting-started-create-cluster "getting-started.md#getting-started-create-cluster") or [Create a multi-Region
   cluster](getting-started.md#getting-started-multi-region "getting-started.md#getting-started-multi-region").
3. Choose **Connect with Query Editor** and then choose **Connect
   with CloudShell**.
4. Choose whether you want to connect as an admin or with a [custom database role](authentication-authorization.md#authentication-authorization-iam-role-connect "authentication-authorization.md#authentication-authorization-iam-role-connect").
5. Choose **Launch in CloudShell** and choose **Run**
   in the following CloudShell dialog.

## Use the local CLI to access Aurora DSQL with the

PostgreSQL interactive terminal (psql)

Use `psql`, a terminal-based front-end to PostgreSQL utility, to interactively enter in queries, issue them to PostgreSQL, and view the query results.

###### Note

To improve query response times, use the PostgreSQL version 17 client. If you use the CLI in a
different environment, make sure you manually set up Python version 3.8+ and psql version
14+.

Download your operating system's installer from the [PostgreSQL Downloads](https://www.postgresql.org/download/ "https://www.postgresql.org/download/") page. For more information
about `psql`, see [PostgreSQL Client Applications](https://www.postgresql.org/docs/current/app-psql.htm "https://www.postgresql.org/docs/current/app-psql.htm") on the _PostgreSQL_ website.

If you already have the AWS CLI installed, use the following example to connect to your
cluster.

```
# Aurora DSQL requires a valid IAM token as the password when connecting.
# Aurora DSQL provides tools for this and here we're using Python.
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token \
  --region `us-east-1` \
  --expires-in 3600 \
  --hostname `your_cluster_endpoint`)

# Aurora DSQL requires SSL and will reject your connection without it.
export PGSSLMODE=require

# Connect with psql, which automatically uses the values set in PGPASSWORD and PGSSLMODE.
# Quiet mode suppresses unnecessary warnings and chatty responses but still outputs errors.
psql --quiet \
  --username admin \
  --dbname postgres \
  --host `your_cluster_endpoint`
```

## Use DBeaver to access Aurora DSQL

DBeaver is an open-source, GUI-based database tool. You can use it to connect to and manage
your database. To download DBeaver, see the [download
page](https://dbeaver.io/download/ "https://dbeaver.io/download/") on the _DBeaver Community_ website.

Use the following procedure to connect to your cluster using DBeaver.

###### To set up a new Aurora DSQL connection in DBeaver

1. Choose **New Database Connection**.
2. In the **New Database Connection** window, choose PostgreSQL.
3. In the **Connection settings/Main** tab, choose **Connect by:
   Host** and enter the following information:
   1. **Host** – Use your cluster endpoint.

   **Database** – Enter `postgres`

   **Authentication** – Choose `Database
 Native`

   **Username** – Enter `admin`

   **Password** – Generate an [authentication
   token](SECTION_authentication-token.md "SECTION_authentication-token.md"). Copy the generated token and use it as your password.

4. Ignore any warnings and paste your authentication token into the **DBeaver
   Password** field.

###### Note

You must set SSL mode in the client connections. Aurora DSQL supports `PGSSLMODE=require
 and PGSSLMODE=verify-full`. Aurora DSQL enforces SSL communication on the server side and
rejects non-SSL connections. For the `verify-full` option you will need to install
the SSL certificates locally. For more information see [SSL/TLS
certificates](configure-root-certificates.md "configure-root-certificates.md"). 5. You should be connected to your cluster and can begin running SQL statements.

###### Important

The administrative features provided by DBeaver for the PostgreSQL databases (such as
**Session Manager** and **Lock
Manager**) don't apply to a database, due to its unique architecture. While
accessible, these screens don't provide reliable information on the database health or
status.

## Use JetBrains

DataGrip to access Aurora DSQL

JetBrains DataGrip is a cross-platform IDE for working with SQL and databases, including
PostgreSQL. DataGrip includes a robust GUI with an intelligent SQL editor. To download DataGrip, go
to the [download page](https://www.jetbrains.com/datagrip/download "https://www.jetbrains.com/datagrip/download") on the
_JetBrains_ website.

###### To set up a new Aurora DSQL connection in JetBrains DataGrip

1. Choose **New Data Source** and choose PostgreSQL.
2. In the **Data Sources/General** tab, enter the following
   information:
   1. **Host** – Use your cluster endpoint.

   **Port** – Aurora DSQL uses the PostgreSQL default:
   `5432`

   **Database** – Aurora DSQL uses the PostgreSQL default of
   `postgres`

   **Authentication** – Choose `User &
 Password` .

   **Username** – Enter `admin`.

   **Password** – [Generate a
   token](SECTION_authentication-token.md "SECTION_authentication-token.md") and paste it into this field.

   **URL** – Don't modify this field. It will be
   auto-populated based on the other fields.

3. **Password** – Provide this by generating an
   authentication token. Copy the resulting output of the token generator and paste it into the
   password field.

###### Note

You must set SSL mode in the client connections. Aurora DSQL supports `PGSSLMODE=require
 and PGSSLMODE=verify-full`. Aurora DSQL enforces SSL communication on the server side and
rejects non-SSL connections. For the `verify-full` option you will need to install
the SSL certificates locally. For more information see [SSL/TLS
certificates](configure-root-certificates.md "configure-root-certificates.md"). 4. You should be connected to your cluster and can start running SQL statements:

###### Important

Some views provided by DataGrip for the PostgreSQL databases (such as Sessions) don't apply to
a database because of its unique architecture. While accessible, these screens don't provide
reliable information on the actual sessions connected to the database.

## Troubleshooting

**Authentication credentials expiration for the SQL
Clients**

Established sessions remain authenticated for a maximum of 1 hour or until an explicit
disconnect or a client-side timeout takes place. If new connections need to be established, a
new authentication token must be generated and provided in the **Password** field of connection. Trying to open a new session (for example, to list
new tables, or a new SQL console) forces a new authentication attempt. If the authentication
token configured in the **Connection** settings is no longer valid,
that new session will fail and all previously opened sessions will become invalid. Keep this in
mind when choosing the duration of your IAM authentication token with the
`expires-in` option which can be set to 15 minutes by default and can be set to a
maximum value of seven days.

Additionally, see the [Troubleshooting](troubleshooting.md "troubleshooting.md") section of the
Aurora DSQL documentation.
