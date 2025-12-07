# Modifying tempdb database options

You can modify the database options on the `tempdb` database on your Amazon RDS DB
instances. For more information about which options can be modified, see [tempdb
database](https://msdn.microsoft.com/en-us/library/ms190768%28v=sql.120%29.aspx "https://msdn.microsoft.com/en-us/library/ms190768%28v=sql.120%29.aspx") in the Microsoft documentation.

Database options such as the maximum file size options are persistent after you restart your
DB instance. You can modify the database options to optimize performance when importing
data, and to prevent running out of storage.

## Optimizing performance when

importing data

To optimize performance when importing large amounts of data into your DB instance, set the
`SIZE` and `FILEGROWTH` properties of the tempdb database
to large numbers. For more information about how to optimize `tempdb`,
see [Optimizing tempdb performance](https://technet.microsoft.com/en-us/library/ms175527%28v=sql.120%29.aspx "https://technet.microsoft.com/en-us/library/ms175527%28v=sql.120%29.aspx") in the Microsoft documentation.

The following example demonstrates setting the size to 100 GB and file growth to
10 percent.

```
alter database[tempdb] modify file (NAME = N'`templog`', SIZE=`100GB`, FILEGROWTH = `10%`)
```

## Preventing storage

problems

To prevent the `tempdb` database from using all available disk space, set the
`MAXSIZE` property. The following example demonstrates setting the
property to 2048 MB.

```
alter database [tempdb] modify file (NAME = N'`templog`', MAXSIZE = `2048MB`)
```
