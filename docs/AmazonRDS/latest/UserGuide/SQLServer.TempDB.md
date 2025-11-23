# Shrinking the tempdb database

There are two ways to shrink the `tempdb` database on your Amazon RDS DB instance. You
can use the `rds_shrink_tempdbfile` procedure, or you can set the
`SIZE` property,

## Using the rds_shrink_tempdbfile

procedure

You can use the Amazon RDS procedure `msdb.dbo.rds_shrink_tempdbfile` to shrink the
`tempdb` database. You can only call
`rds_shrink_tempdbfile` if you have `CONTROL` access to
`tempdb`. When you call `rds_shrink_tempdbfile`, there is
no downtime for your DB instance.

The `rds_shrink_tempdbfile` procedure has the following parameters.

| Parameter name   | Data type | Default | Required | Description                              |
| ---------------- | --------- | ------- | -------- | ---------------------------------------- |
| `@temp_filename` | SYSNAME   | —       | required | The logical name of the file to shrink.  |
| `@target_size`   | int       | null    | optional | The new size for the file, in megabytes. |

The following example gets the names of the files for the `tempdb`
database.

```
use tempdb;
GO

select name, * from sys.sysfiles;
GO
```

The following example shrinks a `tempdb` database file named
`test_file`, and requests a new size of `10` megabytes:

```
exec msdb.dbo.rds_shrink_tempdbfile @temp_filename = N'`test_file`', @target_size = `10`;
```

## Setting the SIZE property

You can also shrink the `tempdb` database by setting the `SIZE`
property and then restarting your DB instance. For more information about restarting
your DB instance, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

The following example demonstrates setting the `SIZE` property to 1024
MB.

```
alter database [tempdb] modify file (NAME = N'`templog`', SIZE = `1024MB`)
```
