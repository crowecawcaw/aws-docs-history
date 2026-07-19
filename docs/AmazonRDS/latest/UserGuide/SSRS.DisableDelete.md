# Disabling and deleting SSRS or PBIRS databases

Use the following procedures to disable SSRS or PBIRS and delete their databases:

###### Topics

- [Turning off SSRS or PBIRS](#SSRS.Disable "#SSRS.Disable")
- [Deleting the SSRS or PBIRS databases](#SSRS.Drop "#SSRS.Drop")

## Turning off SSRS or PBIRS

To turn off SSRS, remove the `SSRS` option from its option group. To turn off PBIRS,
remove the `PBIRS` option from its option group. Removing the option doesn't
delete the report server databases. For more information, see [Deleting the SSRS or PBIRS databases](#SSRS.Drop "#SSRS.Drop").

You can turn SSRS on again by adding back the `SSRS` option, or PBIRS by adding back
the `PBIRS` option. If you have also deleted the report server databases, adding back
the option on the same DB instance creates new report server databases.

###### To remove the SSRS option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `SSRS` option (`ssrs-se-2017` in
   the previous examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **SSRS** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it at
   the next maintenance window.
7. Choose **Delete**.

###### To remove the PBIRS option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `PBIRS` option (`pbirs-se-2025` in
   the previous examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **PBIRS** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it at
   the next maintenance window.
7. Choose **Delete**.

###### To remove the SSRS option from its option group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `ssrs-se-2017` \
    --options SSRS \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `ssrs-se-2017` ^
    --options SSRS ^
    --apply-immediately
```

###### To remove the PBIRS option from its option group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `pbirs-se-2025` \
    --options PBIRS \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `pbirs-se-2025` ^
    --options PBIRS ^
    --apply-immediately
```

## Deleting the SSRS or PBIRS databases

Removing the `SSRS` or `PBIRS` option doesn't delete the report
server databases. To delete them, use the following stored procedures.

To delete the report server databases, be sure to remove the `SSRS` or
`PBIRS` option first.

###### To delete the SSRS databases

- Use the following stored procedure.

```
exec msdb.dbo.rds_drop_ssrs_databases
```

###### To delete the PBIRS databases (SQL Server 2025 and higher)

- Use the following stored procedure.

```
exec msdb.dbo.rds_drop_pbirs_databases
```
