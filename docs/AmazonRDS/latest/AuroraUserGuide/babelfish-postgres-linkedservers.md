# Babelfish supports linked servers

Babelfish for Aurora PostgreSQL supports linked servers by using the PostgreSQL `tds_fdw`
extension in version 3.1.0. To work with linked servers, you must install the
`tds_fdw` extension. For more information about the `tds_fdw`
extension, see [Working with the supported foreign data wrappers for Amazon Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.md "Appendix.PostgreSQL.CommonDBATasks.Extensions.md").

## Installing the `tds_fdw` extension

You can install `tds_fdw` extension using the following methods.

###### Using CREATE EXTENSION from PostgreSQL endpoint

1. Connect to your PostgreSQL DB instance on the Babelfish database in the PostgreSQL port. Use an account that has the rds_superuser role.

```
psql --host=`your-DB-instance.aws-region.rds.amazonaws.com` --port=5432 --username=`test` --dbname=babelfish_db --`password`
```

2. Install the `tds_fdw` extension. This is a one-time installation process. You don't need to
   reinstall when the DB cluster restarts.

```

babelfish_db=> CREATE EXTENSION tds_fdw;
CREATE EXTENSION
```

###### Calling `sp_execute_postgresql` stored procedure from TDS endpoint

Babelfish supports installing `tds_fdw` extension by calling `sp_execute_postgresql` procedure from version 3.3.0. You can execute PostgreSQL statements from T-SQL endpoint without exiting the T-SQL port.
For more information, see [Working with Babelfish for Aurora PostgreSQL procedures](Appendix.Babelfish.md "Appendix.Babelfish.md")

1. Connect to your PostgreSQL DB instance on the Babelfish database in the T-SQL port.

```
sqlcmd -S `your-DB-instance.aws-region.rds.amazonaws.com` -U `test` -P `password`
```

2. Install the `tds_fdw` extension.

```
`1>`EXEC sp_execute_postgresql N'CREATE EXTENSION tds_fdw';
`2>go`
```

## Supported functionality

Babelfish supports adding remote RDS for SQL Server or Babelfish for Aurora PostgreSQL endpoints as the linked server.
You can also add other remote SQL Server instances as linked servers.
Then, use `OPENQUERY()` to retrieve data from these linked servers. Starting from Babelfish version 3.2.0,
four-part names are also supported.

The following stored procedures and catalog views are supported in order to use the linked servers.

Stored procedures

- sp_addlinkedserver – Babelfish doesn't support the `@provstr` parameter.
- sp_addlinkedsrvlogin
  - You must provide an explicit
    remote username and password to connect to the remote data source. You can't connect with the user's self credentials. Babelfish
    supports only `@useself = false`.
  - Babelfish doesn't support the `@locallogin` parameter since
    configuring remote server access specific to local login isn't supported.

- sp_linkedservers
- sp_helplinkedsrvlogin
- sp_dropserver
- sp_droplinkedsrvlogin – Babelfish doesn't
  support the `@locallogin` parameter since configuring remote server access
  specific to local login isn't supported.
- sp_serveroption – Babelfish supports the following server options:
  - query timeout (from Babelfish version 3.2.0)
  - connect timeout (from Babelfish version 3.3.0)

- sp_testlinkedserver (from Babelfish version 3.3.0)
- sp_enum_oledb_providers (from Babelfish version 3.3.0)

Catalog views

- sys.servers
- sys.linked_logins

## Using encryption in transit for the connection

The connection from the source Babelfish for Aurora PostgreSQL server to the target remote server uses
encryption in transit (TLS/SSL), depending on the remote server database configuration.
If the remote server isn't configured for encryption, the Babelfish server
making the request to the remote database falls back to unencrypted.

To enforce connection encryption

- If the target linked server is an RDS for SQL Server instance, set `rds.force_ssl = on` for the target SQL Server instance.
  For more information about SSL/TLS configuration for RDS for SQL Server, see [Using
  SSL with a Microsoft SQL Server DB instance](../UserGuide/SQLServer.Concepts.General.SSL.md "../UserGuide/SQLServer.Concepts.General.SSL.md")
- If the target linked server is a Babelfish for Aurora PostgreSQL cluster, set `babelfishpg_tds.tds_ssl_encrypt = on` and `ssl = on` for the target server.
  For more information about SSL/TLS, see [Babelfish SSL settings and client connections](babelfish-configuration.md#babelfish-ssl "babelfish-configuration.md#babelfish-ssl").

## Adding Babelfish as a linked server from SQL Server

Babelfish for Aurora PostgreSQL can be added as a linked server from a SQL Server. On a SQL Server database, you can add Babelfish as a linked server using Microsoft OLE DB provider for ODBC : MSDASQL.

There are two ways to configure Babelfish as a linked server from SQL Server using MSDASQL provider:

- Providing ODBC connection string as the provider string.
- Provide the System DSN of ODBC data source while adding the linked server.

## Limitations

- OPENQUERY() works only for SELECT and doesn't work for DML.
- Four-part object names work only for reading and doesn't work for modifying the remote table. An UPDATE can reference a remote table in the FROM clause without modifying it.
- Executing stored procedures against Babelfish linked servers isn't supported.
- Babelfish major version upgrade might not work if there are objects dependent on
  `OPENQUERY()` or objects referenced through four-part names. You must ensure that any objects referencing `OPENQUERY()` or four-part names are
  dropped before a major version upgrade.
- The following datatypes don't work as expected against remote Babelfish server: `nvarchar(max)`, `varchar(max)`, `varbinary(max)`, `binary(max)` and `time`.
  We recommend using the CAST function to convert these to the supported datatypes.

## Example

In the following example, a Babelfish for Aurora PostgreSQL instance is connecting to an instance of RDS for SQL Server in the cloud.

```

EXEC master.dbo.sp_addlinkedserver @server=N'rds_sqlserver', @srvproduct=N'', @provider=N'SQLNCLI', @datasrc=N'`myserver.CB2XKFSFFMY7.US-WEST-2.RDS.AMAZONAWS.COM`';
EXEC master.dbo.sp_addlinkedsrvlogin @rmtsrvname=N'rds_sqlserver',@useself=N'False',@locallogin=NULL,@rmtuser=N'`username`',@rmtpassword='`password`';

```

When the linked server is in place, you can then use T-SQL OPENQUERY() or standard four-part naming to reference a table, view,
or other supported objects, on the remote server:

```

SELECT * FROM OPENQUERY(rds_sqlserver, 'SELECT * FROM TestDB.dbo.t1');
SELECT * FROM rds_sqlserver.TestDB.dbo.t1;

```

To drop the linked server and all associated logins:

```

EXEC master.dbo.sp_dropserver @server=N'rds_sqlserver', @droplogins=N'droplogins';

```

## Troubleshooting

You can use the same security group for both source and remote servers to allow them to communicate with each other. Security group should allow
only inbound traffic on TDS port (1433 by default) and source IP in security group can be set as the security group ID itself. For more information
on how to set the rules for connecting to an instance from another instance with the same security group, see [Rules to connect to instances from an instance with the same security group](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances").

If access isn't configured correctly, an error message similar to the following example appears when you
try to query the remote server.

```
`TDS client library error: DB #: 20009, DB Msg: Unable to connect: server is unavailable or does not exist (mssql2019.aws-region.rds.amazonaws.com), OS #: 110, OS Msg: Connection timed out, Level: 9`
```
