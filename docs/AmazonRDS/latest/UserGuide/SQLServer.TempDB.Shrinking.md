

# Shrinking the tempdb database
<a name="SQLServer.TempDB.Shrinking"></a>

There are two ways to shrink the `tempdb` database on your Amazon RDS DB instance. You can use the `rds_shrink_tempdbfile` procedure, or you can set the `SIZE` property, 

## Using the rds\_shrink\_tempdbfile procedure
<a name="SQLServer.TempDB.Shrinking.Proc"></a>

You can use the Amazon RDS procedure `msdb.dbo.rds_shrink_tempdbfile` to shrink the `tempdb` database. You can only call `rds_shrink_tempdbfile` if you have `CONTROL` access to `tempdb`. When you call `rds_shrink_tempdbfile`, there is no downtime for your DB instance. 

The `rds_shrink_tempdbfile` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `@temp_filename` | SYSNAME | — | required | The logical name of the file to shrink. | 
| `@target_size` | int | null | optional | The new size for the file, in megabytes. | 

The following example gets the names of the files for the `tempdb` database.

```
1. use tempdb;
2. GO
3. 
4. select name, * from sys.sysfiles;
5. GO
```

The following example shrinks a `tempdb` database file named `test_file`, and requests a new size of `10` megabytes: 

```
1. exec msdb.dbo.rds_shrink_tempdbfile @temp_filename = N'{{test_file}}', @target_size = {{10}};
```

## Setting the SIZE property
<a name="SQLServer.TempDB.Shrinking.Size"></a>

You can also shrink the `tempdb` database by setting the `SIZE` property and then restarting your DB instance. For more information about restarting your DB instance, see [Rebooting a DB instance](USER_RebootInstance.md).

The following example demonstrates setting the `SIZE` property to 1024 MB. 

```
1. alter database [tempdb] modify file (NAME = N'{{templog}}', SIZE = {{1024MB}})
```