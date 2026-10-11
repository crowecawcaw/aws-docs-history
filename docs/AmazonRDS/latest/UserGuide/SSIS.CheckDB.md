

# Checking the integrity of the SSISDB database
<a name="SSIS.CheckDB"></a>

To check the logical and physical integrity of the SSISDB database, use the `rds_dbcc_checkdb` stored procedure. The procedure runs `DBCC CHECKDB` on the database that you specify with the `ALL_ERRORMSGS`, `NO_INFOMSGS`, and `TABLERESULTS` options. The procedure supports only the SSISDB database, and the database must be online.

The `rds_dbcc_checkdb` procedure has the following parameter.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `@database_name` | SYSNAME | None | required | The name of the database to check. Only `SSISDB` is supported. | 

The following example checks the integrity of the SSISDB database.

```
EXEC msdb.dbo.rds_dbcc_checkdb @database_name = N'SSISDB';
```

The procedure returns any errors that `DBCC CHECKDB` finds as a result set. If the check finds no errors, the result set is empty. For more information about the output, see [DBCC CHECKDB](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql) on the Microsoft Learn website.