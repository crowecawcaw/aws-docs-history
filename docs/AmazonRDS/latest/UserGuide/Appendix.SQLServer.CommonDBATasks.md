# Changing the

`db_owner` to the `rdsa` account for your Amazon RDS for SQL Server database

When you create or restore a database in an RDS for SQL Server DB instance, Amazon RDS sets the owner of the database to `rdsa`. If you have a Multi-AZ deployment using SQL Server Database Mirroring (DBM)
or Always On Availability Groups (AGs), Amazon RDS sets the owner of the database on the secondary DB instance to `NT AUTHORITY\SYSTEM`.
The owner of the secondary database can't be changed until the secondary DB instance is promoted to the primary role.
In most cases, setting the owner of the database to `NT AUTHORITY\SYSTEM` isn't problematic when executing queries, however, can throw errors
when executing system stored procedures such as `sys.sp_updatestats` that require elevated permissions to execute.

You can use the following query to identify the owner of the databases owned by `NT AUTHORITY\SYSTEM`:

```
SELECT name FROM sys.databases WHERE SUSER_SNAME(owner_sid) = 'NT AUTHORITY\SYSTEM';

```

You can use the Amazon RDS stored procedure `rds_changedbowner_to_rdsa` to change the owner of the database to `rdsa`. The following databases are not allowed to be used
with `rds_changedbowner_to_rdsa`: `master, model, msdb, rdsadmin, rdsadmin_ReportServer, rdsadmin_ReportServerTempDB, SSISDB`.

To change the owner of the database to `rdsa`, call the `rds_changedbowner_to_rdsa` stored procedure and provide the name of the database.

###### Example usage:

```
exec msdb.dbo.rds_changedbowner_to_rdsa 'TestDB1';
```

The following parameter is required:

- `@db_name` – The name of the database to change the owner of the database to `rdsa`.

###### Important

You can't use `rds_changedbowner_to_rdsa` to change ownership of a database to a
login other than `rdsa`. For example, you can't change the ownership to
the login with which you created the database. To restore lost membership in the
`db_owner` role for your master user when no other database user can
be used to grant the membership, reset the master user password to obtain membership
in the `db_owner` role. For more information, see
[Resetting the db_owner role
membership for master user for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md").
