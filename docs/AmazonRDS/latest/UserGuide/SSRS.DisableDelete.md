# Disabling and deleting SSRS databases

Use the following procedures to disable SSRS and delete SSRS databases:

###### Topics

- [Turning off SSRS](#SSRS.Disable "#SSRS.Disable")
- [Deleting the SSRS databases](#SSRS.Drop "#SSRS.Drop")

## Turning off SSRS

To turn off SSRS, remove the `SSRS` option from its option group. Removing the option doesn't delete the SSRS
databases. For more information, see [Deleting the SSRS databases](#SSRS.Drop "#SSRS.Drop").

You can turn SSRS on again by adding back the `SSRS` option. If you have also
deleted the SSRS databases, readding the option on the same DB instance creates new
report server databases.

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

## Deleting the SSRS databases

Removing the `SSRS` option doesn't delete the report server databases. To
delete them, use the following stored procedure.

To delete the report server databases, be sure to remove the `SSRS` option
first.

###### To delete the SSRS databases

- Use the following stored procedure.

```
exec msdb.dbo.rds_drop_ssrs_databases
```
