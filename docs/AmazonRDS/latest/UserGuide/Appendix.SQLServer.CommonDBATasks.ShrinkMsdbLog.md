

# Shrinking the msdb transaction log file for Amazon RDS for SQL Server
<a name="Appendix.SQLServer.CommonDBATasks.ShrinkMsdbLog"></a>

If the transaction log file of the `msdb` system database has grown larger than you need, you can shrink it by using the `rds_shrink_msdb_log_file` stored procedure. The target size must be smaller than the current size of the log file. There is no downtime for your DB instance when you run the procedure.

The `rds_shrink_msdb_log_file` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `@log_file_name` | SYSNAME | NULL | required | The logical name of the `msdb` transaction log file to shrink. | 
| `@TargetSizeMB` | int | NULL | required | The new size for the log file, in megabytes. The value must be greater than 0 and smaller than the current size of the log file. | 

The following example gets the logical name and current size of the `msdb` transaction log file.

```
USE msdb;
GO

SELECT name, size * 8 / 1024 AS size_mb FROM sys.database_files WHERE type_desc = 'LOG';
GO
```

The following example shrinks the `msdb` transaction log file to 30 MB. In the example, replace the `@log_file_name` value {{MSDBLog}} with the logical name of your log file and the `@TargetSizeMB` value {{30}} with the target size in MB.

```
EXEC msdb.dbo.rds_shrink_msdb_log_file @log_file_name = N'{{MSDBLog}}', @TargetSizeMB = {{30}};
```

The procedure returns a result set with the logical file name and the size of the file in megabytes before and after the shrink operation.