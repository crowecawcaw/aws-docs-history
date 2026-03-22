# Deactivating servers linked to Teradata

To deactivate linked servers to Teradata, remove the `ODBC_TERADATA` option from its option group.

###### Important

Deleting the option doesn't delete the linked server configurations on the DB instance. You must manually drop them to remove them from the DB instance.

You can reactivate the `ODBC_TERADATA` after removal to reuse the linked server configurations
that were previously configured on the DB instance.

To remove the `ODBC_TERADATA` option from the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `ODBC_TERADATA` option.
4. Choose **Delete**.
5. Under **Deletion options**, choose `ODBC_TERADATA` under **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it during the next maintenance window.
7. Choose **Delete**.
   The following commands removes the `ODBC_TERADATA` option.

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `teradata-odbc-se-2019` \
    --options ODBC_TERADATA \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `teradata-odbc-se-2019` ^
    --options ODBC_TERADATA ^
    --apply-immediately
```
