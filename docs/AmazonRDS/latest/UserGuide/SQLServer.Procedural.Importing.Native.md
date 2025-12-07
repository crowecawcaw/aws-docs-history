# Compressing backup

files

To save space in your Amazon S3 bucket, you can compress your backup files. For more
information about compressing backup files, see [Backup compression](https://msdn.microsoft.com/en-us/library/bb964719.aspx "https://msdn.microsoft.com/en-us/library/bb964719.aspx")
in the Microsoft documentation.

Compressing your backup files is supported for the following database editions:

- Microsoft SQL Server Enterprise Edition
- Microsoft SQL Server Standard Edition
  To verify the compression option for your backup files, run the following code:

```
exec rdsadmin.dbo.rds_show_configuration 'S3 backup compression';
```

To turn on compression for your backup files, run the following code:

```
exec rdsadmin.dbo.rds_set_configuration 'S3 backup compression', 'true';
```

To turn off compression for your backup files, run the following code:

```
exec rdsadmin.dbo.rds_set_configuration 'S3 backup compression', 'false';
```
