# Connecting to a database through RDS Proxy

The way to connect to an RDS DB instance through a proxy or by connecting to the database is generally the same.
For more information, see [Overview of proxy endpoints](rds-proxy-endpoints.md#rds-proxy-endpoints-overview "rds-proxy-endpoints.md#rds-proxy-endpoints-overview").

###### Topics

- [Connecting to a database using database credentials](#rds-proxy-connecting-native "#rds-proxy-connecting-native")
- [Connecting to a database using IAM authentication](#rds-proxy-connecting-iam "#rds-proxy-connecting-iam")
- [Considerations for connecting to Microsoft SQL Server](#rds-proxy-connecting-sqlserver "#rds-proxy-connecting-sqlserver")
- [Considerations for connecting to PostgreSQL](#rds-proxy-connecting-postgresql "#rds-proxy-connecting-postgresql")

## Connecting to a database using database credentials

Use the following steps to connect to a proxy using database credentials:

1. Find the proxy endpoint. In the AWS Management Console, you can find the endpoint on the details page for the
   corresponding proxy. With the AWS CLI, you can use the
   [describe-db-proxies](../../../cli/latest/reference/rds/describe-db-proxies.md "../../../cli/latest/reference/rds/describe-db-proxies.md") command. The
   following example shows how.

```
# Add --output text to get output as a simple tab-separated list.
$ aws rds describe-db-proxies --query '*[*].{DBProxyName:DBProxyName,Endpoint:Endpoint}'
[
    [
        {
            "Endpoint": "**the-proxy.proxy-demo.us-east-1.rds.amazonaws.com**",
            "DBProxyName": "the-proxy"
        },
        {
            "Endpoint": "**the-proxy-other-secret.proxy-demo.us-east-1.rds.amazonaws.com**",
            "DBProxyName": "the-proxy-other-secret"
        },
        {
            "Endpoint": "**the-proxy-rds-secret.proxy-demo.us-east-1.rds.amazonaws.com**",
            "DBProxyName": "the-proxy-rds-secret"
        },
        {
            "Endpoint": "**the-proxy-t3.proxy-demo.us-east-1.rds.amazonaws.com**",
            "DBProxyName": "the-proxy-t3"
        }
    ]
]
```

2. Specify the endpoint as the host parameter in the connection string for your client application. For
   example, specify the proxy endpoint as the value for the `mysql -h` option or `psql
-h` option.
3. Supply the same database user name and password as you usually do.

## Connecting to a database using IAM authentication

When you use IAM authentication with RDS Proxy, you have two options for authentication between your client and proxy:

- Set up your database users to authenticate with regular
  user names and passwords. RDS Proxy retrieves the user name and
  password credentials from Secrets Manager. The connection from RDS Proxy to the underlying database doesn't
  go through IAM.
- You can also use end-to-end IAM authentication, which connects to your database through
  the proxy using IAM without requiring database credentials.

To connect to RDS Proxy using IAM authentication, use the same general connection
procedure as for IAM authentication with an
RDS DB instance.
For general information about using IAM, see [Security in Amazon RDS](UsingWithRDS.md "UsingWithRDS.md").
If you are using end-to-end IAM authentication, provide the IAM authentication plugin to your DB user.
See [Creating a database account using
IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").

The major differences in IAM usage for RDS Proxy include the following:

- With standard IAM authentication, database users have regular credentials
  within the database. You set up Secrets Manager secrets containing
  these user names and passwords, and authorize RDS Proxy to retrieve the credentials from Secrets Manager.
  The IAM authentication applies to the connection between your client program and the proxy. The proxy
  then authenticates to the database using the user name and password credentials retrieved from Secrets Manager.
- With end-to-end IAM authentication, you don't need to configure Secrets Manager secrets for database credentials.
  The IAM authentication applies to the connection between the client to the proxy and proxy to the database.
- Instead of the instance, cluster, or reader endpoint, you specify the proxy endpoint. For details about
  the proxy endpoint, see [Connecting to your DB instance using IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").
- Make sure that you use Transport Layer Security (TLS)/Secure Sockets Layer (SSL) when connecting to a proxy using IAM authentication.

You can grant a specific user access to the proxy by modifying the IAM policy. An example follows.

```
"Resource": "arn:aws:rds-db:us-east-2:1234567890:dbuser:prx-ABCDEFGHIJKL01234/db_user"
```

###### Tip

When configuring IAM authentication for RDS Proxy connections, follow these important guidelines to avoid connection issues:

- Do not grant the `rds_iam` role while maintaining general
  password authentication for the same database user or role.
- Remember that while clients connect to RDS Proxy using IAM authentication, RDS Proxy
  always connects to the database using password authentication through Secrets Manager.
- If you experience frequent connection terminations and reconnections, remove any
  existing `rds_iam` grants from the user or role and use only password authentication.
- Ensure your password policy satisfies SCRAM-SHA-256 safe character requirements.
  Mixing IAM and password authentication methods for the same database user can cause connection instability.

## Considerations for connecting to Microsoft SQL Server

For connecting to a proxy using IAM authentication, you don't use the
password
field. Instead, you provide the appropriate token property for each type of database
driver in the token field. For example, use the `accessToken` property for
JDBC, or the `sql_copt_ss_access_token` property for ODBC. Or use the
`AccessToken` property for the .NET SqlClient driver. You can't use IAM
authentication with clients that don't support token properties.

Under some conditions, a proxy can't share a database connection and instead pins the connection from your client application to the proxy to a dedicated database connection.
For more information about these conditions, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md "rds-proxy-pinning.md").

## Considerations for connecting to PostgreSQL

If you create a new PostgreSQL database user for connecting to RDS Proxy, make sure that
you grant the user `CONNECT` privilege on the database. Without this, the user
can't establish a connection. For more information, see [Adding a new database user to a PostgreSQL database when using RDS Proxy](rds-proxy-new-db-user.md#rds-proxy-new-db-user-pg "rds-proxy-new-db-user.md#rds-proxy-new-db-user-pg").

When a client starts a connection to a PostgreSQL database, it sends a startup
message. This message includes pairs of parameter name and value strings. For details, see
the `StartupMessage` in [PostgreSQL
message formats](https://www.postgresql.org/docs/current/protocol-message-formats.html "https://www.postgresql.org/docs/current/protocol-message-formats.html") in the PostgreSQL documentation.

When you connect through an RDS proxy, the startup message can include the following
currently recognized parameters:

- `user`
- `database`

The startup message can also include the following additional runtime parameters:

- `application_name`
- `client_encoding`
- `DateStyle`
- `TimeZone`
- `extra_float_digits`
- `search_path`

For more information about PostgreSQL messaging, see the [Frontend/Backend
protocol](https://www.postgresql.org/docs/current/protocol.html "https://www.postgresql.org/docs/current/protocol.html") in the PostgreSQL documentation.

For PostgreSQL, if you use JDBC, we recommend the following to avoid pinning:

- Set the JDBC connection parameter `assumeMinServerVersion` to at least
  `9.0` to avoid pinning. This prevents the JDBC driver from performing
  an extra round trip during connection startup when it runs `SET extra_float_digits
= 3`.
- Set the JDBC connection parameter `ApplicationName` to
  `any/your-application-name` to avoid pinning.
  Doing this prevents the JDBC driver from performing an extra round trip during
  connection startup when it runs `SET application_name = "PostgreSQL JDBC
Driver"`. Note the JDBC parameter is `ApplicationName` but the
  PostgreSQL `StartupMessage` parameter is
  `application_name`.

For more information, see [Avoiding pinning an RDS Proxy](rds-proxy-pinning.md "rds-proxy-pinning.md"). For more information about connecting using JDBC, see
[Connecting to the
database](https://jdbc.postgresql.org/documentation/setup/ "https://jdbc.postgresql.org/documentation/setup/") in the PostgreSQL documentation.
