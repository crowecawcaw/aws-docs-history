# Change data capture (CDC) support with RDS Custom for SQL Server

## Overview

RDS Custom for SQL Server provides native support for Change data capture (CDC), enabling you to track and capture data
modifications in your SQL Server tables. CDC stores detailed metadata about these changes for subsequent retrieval and analysis.
For detailed information about CDC functionality, see
[Change data capture](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server#Capture "https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server#Capture") in the Microsoft documentation.

CDC operation in SQL Server requires matching values between the _local server_
(that has `server_id` = 0) in `sys.servers` and
`SERVERPROPERTY('ServerName')` identifiers. RDS Custom for SQL Server automatically maintains this
synchronization throughout the instance's lifecycle to ensuring continuous CDC functioning even if
hosts are replaced during maintenance or recovery operations.

###### Important

Following a Multi-AZ instance failover, the `SERVERPROPERTY('Servername')` function
automatically reflects changes in the network/computer name. However, the `@@SERVERNAME` function
retains the old server name until the `MSSQLSERVER` service is restarted.
Querying @@SERVERNAME returns the previous server name after a failover.
To obtain the accurate server name after a failover, use the following SQL query:

```
SELECT name FROM sys.servers WHERE server_id=0
```

This query provides the most up-to-date server name information without requiring a service restart.

## Region and version availability

CDC functionality is supported in all AWS Regions where RDS Custom for SQL Server is available, for all SQL Server versions supported by RDS Custom.
For more information about supported versions and Region availability of RDS Custom for SQL Server,
see [Supported Regions and DB engines for RDS Custom for SQL Server](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq").

## Requirements and limitations

When implementing CDC on RDS Custom for SQL Server, be aware the following key considerations:

- If you manually set `@@SERVERNAME` and/or _local server_ in `sys.servers`
  to use features like MS Replication, if the value of the local server (that has `server_id = 0`) in `sys.servers`
  is set to a format that matches `*.rds.amazonaws.com` or `*.awsrds.*.com`, RDS Custom for SQL Server does not attempt to modify it to match `SERVERPROPERTY('ServerName')`.
- RDS cannot modify the local server (that has `server_id = 0`) in `sys.servers` to a new
  hostname while remote logins or linked servers are actively using the old hostname. This limitation applies in two scenarios:
  - When a linked server establishes a connection to the local server using a remote login associated with the old hostname
  - When an RDS Custom for SQL Server instance acts as a publisher or distributor and has linked logins associated with the old hostname to its subscriber instances.

## Troubleshooting

To identify remote logins or linked logins associated with the old server name, use the following queries.
Validate the results and remove these logins to ensure proper CDC functionality.

```
SELECT * FROM sys.remote_logins WHERE server_id=0
```

or

```
select sss.srvname,ssp.name,srl.remote_name  from sys.server_principals ssp
inner join sys.remote_logins srl on srl.local_principal_id=ssp.principal_id
inner join sys.sysservers sss  on srl.server_id = sss.srvid
where sss.srvname = @@SERVERNAME
```
