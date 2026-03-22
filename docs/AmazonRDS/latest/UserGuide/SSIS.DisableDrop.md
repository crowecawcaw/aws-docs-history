# Disable and drop SSIS database

Use the following steps to disable or drop SSIS databases:

###### Topics

- [Disabling SSIS](#SSIS.Disable "#SSIS.Disable")
- [Dropping the SSISDB database](#SSIS.Drop "#SSIS.Drop")

## Disabling SSIS

To disable SSIS, remove the `SSIS` option from its option group.

###### Important

Removing the option doesn't delete the SSISDB database, so you can safely remove the
option without losing the SSIS projects.

You can re-enable the `SSIS` option after removal to reuse the SSIS
projects that were previously deployed to the SSIS catalog.

The following procedure removes the `SSIS` option.

###### To remove the SSIS option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `SSIS` option (`ssis-se-2016` in
   the previous examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **SSIS** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it at
   the next maintenance window.
7. Choose **Delete**.
   The following procedure removes the `SSIS` option.

###### To remove the SSIS option from its option group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `ssis-se-2016` \
    --options SSIS \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `ssis-se-2016` ^
    --options SSIS ^
    --apply-immediately
```

## Dropping the SSISDB database

After removing the SSIS option, the SSISDB database isn't deleted. To drop the SSISDB
database, use the `rds_drop_ssis_database` stored procedure after removing
the SSIS option.

###### To drop the SSIS database

- Use the following stored procedure.

```
USE [msdb]
GO
EXEC dbo.rds_drop_ssis_database
GO
```

After dropping the SSISDB database, if you re-enable the SSIS option you get a fresh SSISDB catalog.
