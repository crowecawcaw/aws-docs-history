# Working with SQL Server databases by using the tds_fdw extension

You can use the PostgreSQL `tds_fdw` extension to access databases that support
the tabular data stream (TDS) protocol, such as Sybase and Microsoft SQL Server databases. This
foreign data wrapper lets you connect from your
Aurora PostgreSQL DB cluster to databases that
use the TDS protocol, including Amazon RDS for Microsoft SQL Server. For more information, see
[tds-fdw/tds_fdw](https://github.com/tds-fdw/tds_fdw "https://github.com/tds-fdw/tds_fdw") documentation on GitHub.

The `tds_fdw` extension is supported on Amazon Aurora PostgreSQL version 13.6 and
higher releases.

## Setting up your Aurora PostgreSQL DB to use the tds_fdw extension

In the following procedures, you can find an example of setting up and using the `tds_fdw`
with an Aurora PostgreSQL DB cluster.
Before you can connect to a SQL Server database using `tds_fdw`,
you need to get the following details for the instance:

- Hostname or endpoint. For an RDS for SQL Server DB instance, you can find the endpoint by
  using the Console. Choose the Connectivity & security tab and look in the "Endpoint and port" section.
- Port number. The default port number for Microsoft SQL Server is 1433.
- Name of the database. The DB identifier.

You also need to provide access on the security group or the access control list (ACL) for the SQL Server port, 1433. Both
the Aurora PostgreSQL DB cluster
and the RDS for SQL Server DB instance need access to port 1433. If access isn't configured correctly,
when you try to query the Microsoft SQL Server you see the following error message:

```
ERROR: DB-Library error: DB #: 20009, DB Msg: Unable to connect:
Adaptive Server is unavailable or does not exist (`mssql2019`.`aws-region`.rds.amazonaws.com), OS #: 0, OS Msg: Success, Level: 9

```

###### To use tds_fdw to connect to a SQL Server database

1. Connect to your Aurora PostgreSQL DB cluster's primary
   instance using an account that has the `rds_superuser` role:

```
psql --host=`your-cluster-name-instance-1`.`aws-region`.rds.amazonaws.com --port=5432 --username=test –-password
```

2. Install the `tds_fdw` extension:

```
`test=>` `CREATE EXTENSION tds_fdw;`
`CREATE EXTENSION`
```

After the extension is installed on your Aurora PostgreSQL DB cluster
, you set up the foreign server.

###### To create the foreign server

Perform these tasks on the Aurora PostgreSQL DB cluster
using an account that has
`rds_superuser` privileges.

1. Create a foreign server in the Aurora PostgreSQL DB cluster:

```
`test=>` `CREATE SERVER `sqlserverdb` FOREIGN DATA WRAPPER tds_fdw OPTIONS (servername '`mssql2019`.`aws-region`.rds.amazonaws.com', port '1433', database '`tds_fdw_testing`');`
`CREATE SERVER`
```

To access non-ASCII data on the SQLServer side, create a server link with the character_set option in the Aurora PostgreSQL DB cluster:

```
`test=>` `CREATE SERVER `sqlserverdb` FOREIGN DATA WRAPPER tds_fdw OPTIONS (servername '`mssql2019`.`aws-region`.rds.amazonaws.com', port '1433', database '`tds_fdw_testing`', character_set `'UTF-8'`);`
`CREATE SERVER`
```

2. Grant permissions to a user who doesn't have `rds_superuser` role privileges, for example, `user1`:

```
`test=>` `GRANT USAGE ON FOREIGN SERVER `sqlserverdb` TO `user1`;`
```

3. Connect as user1 and create a mapping to a SQL Server user:

```
`test=>` `CREATE USER MAPPING FOR user1 SERVER `sqlserverdb` OPTIONS (username '`sqlserveruser`', password '`password`');`
`CREATE USER MAPPING`
```

4. Create a foreign table linked to a SQL Server table:

```
`test=>` `CREATE FOREIGN TABLE mytab (a int) SERVER `sqlserverdb` OPTIONS (table '`MYTABLE`');`
`CREATE FOREIGN TABLE`
```

5. Query the foreign table:

```
`test=>` `SELECT * FROM mytab;`
 `a
---
 1
(1 row)`
```

### Using encryption in transit for the connection

The connection from Aurora PostgreSQL
to SQL Server uses encryption in transit
(TLS/SSL) depending on the SQL Server database configuration. If the SQL
Server isn't configured for encryption, the RDS for PostgreSQL client
making the request to the SQL Server database falls back to unencrypted.

You can enforce encryption for the connection to RDS for SQL Server DB instances by
setting the `rds.force_ssl` parameter. To learn how,
see [Forcing
connections to your DB instance to use SSL](../UserGuide/SQLServer.Concepts.General.SSL.md#SQLServer.Concepts.General.SSL.Forcing "../UserGuide/SQLServer.Concepts.General.SSL.md#SQLServer.Concepts.General.SSL.Forcing"). For more information about SSL/TLS
configuration for RDS for SQL Server, see [Using
SSL with a Microsoft SQL Server DB instance](../UserGuide/SQLServer.Concepts.General.SSL.md "../UserGuide/SQLServer.Concepts.General.SSL.md").
