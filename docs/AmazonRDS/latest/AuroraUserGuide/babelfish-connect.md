# Connecting to a Babelfish DB cluster

To connect to Babelfish, you connect to the endpoint of the Aurora PostgreSQL
cluster running Babelfish. Your client can use one of the following client
drivers compliant with TDS version 7.1 through 7.4:

- Open Database Connectivity (ODBC)
- OLE DB Driver/MSOLEDBSQL
- Java Database Connectivity (JDBC) version 8.2.2 (mssql-jdbc-8.2.2) and
  higher
- Microsoft SqlClient Data Provider for SQL Server
- .NET Data Provider for SQL Server
- SQL Server Native Client 11.0 (deprecated)
- OLE DB Provider/SQLOLEDB (deprecated)
  With Babelfish, you run the following:

- SQL Server tools, applications, and syntax on the TDS port, by default port

1433.

- PostgreSQL tools, applications, and syntax on the PostgreSQL port, by default
  port 5432.
  To learn more about connecting to Aurora PostgreSQL in general, see [Connecting to an Amazon Aurora PostgreSQL
  DB cluster](Aurora.md#Aurora.Connecting.AuroraPostgreSQL "Aurora.md#Aurora.Connecting.AuroraPostgreSQL").

###### Note

Third-party developer tools using the SQL Server OLEDB provider to access metadata
aren't supported. We recommend you to use SQL Server JDBC, ODBC, or SQL Native
client connections for these tools.

Starting with Babelfish version 5.1.0, end-to-end connection encryption is
enforced by default. To ensure continued connectivity:

- Configure SSL/TLS encryption for your connections. For more information, see
  [Using SSL/TLS to encrypt a connection to a DB
  cluster](UsingWithRDS.md "UsingWithRDS.md").
- Import the required certificates on your client computers. For more
  information, see [Using SSL with a Microsoft SQL Server DB instance](../UserGuide/SQLServer.Concepts.General.SSL.md "../UserGuide/SQLServer.Concepts.General.SSL.md").
  If you want to continue using the encryption settings from a previous version of
  Babelfish (prior to version 5.1.0), you can set the `rds.force_ssl`
  parameter to `0` in your DB cluster parameter group.

###### Topics

- [Finding the writer endpoint and port
  number](#babelfish-connect-endpoint "#babelfish-connect-endpoint")
- [Creating C# or JDBC client connections
  to Babelfish](babelfish-connect-configure.md "babelfish-connect-configure.md")
- [Using a SQL Server client to connect
  to your DB cluster](babelfish-connect-sqlserver.md "babelfish-connect-sqlserver.md")
- [Using a PostgreSQL client to connect to
  your DB cluster](babelfish-connect-PostgreSQL.md "babelfish-connect-PostgreSQL.md")

## Finding the writer endpoint and port

number

To connect to your Babelfish DB cluster, you use the endpoint associated
with the DB cluster's writer (primary) instance. The instance must have a
status of **Available**. It can take up to 20 minutes for the
instances to be available after creating the Babelfish for Aurora PostgreSQL DB cluster.

###### To find your database endpoint

1. Open the console for Babelfish.
2. Choose **Databases** from the navigation pane.
3. Choose your Babelfish for Aurora PostgreSQL DB cluster from those listed to see its
   details.
4. On the **Connectivity & security** tab, note the
   available cluster **Endpoints** values. Use the cluster
   endpoint for the writer instance in your connection strings for any
   applications that perform database write or read operations.

![Finding a Babelfish endpoint and port.](images/Babelfish-database-endpoint.png)

For more information about Aurora DB cluster details, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

###### Important

Ensure the certificate matches the Certificate Authority shown in your DB cluster
configuration on the AWS Management Console.
