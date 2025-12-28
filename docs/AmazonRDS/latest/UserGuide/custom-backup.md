# Deleting RDS Custom for Oracle automated backups

You can delete retained automated backups for RDS Custom for Oracle when they are no longer needed. The procedure is the
same as the procedure for deleting Amazon RDS backups.

###### To delete a retained automated backup

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated backups**.
3. Choose **Retained**.
4. Choose the retained automated backup that you want to delete.
5. For **Actions**, choose **Delete**.
6. On the confirmation page, enter `delete me` and choose
   **Delete**.
   You can delete a retained automated backup by using the AWS CLI command [delete-db-instance-automated-backup](../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md "../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md").

The following option is used to delete a retained automated backup:

- `--dbi-resource-id` – The resource identifier for the source RDS Custom DB instance.

You can find the resource identifier for the source DB instance of a retained automated backup by using the
AWS CLI command [describe-db-instance-automated-backups](../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md "../../../cli/latest/reference/rds/describe-db-instance-automated-backups.md").
The following example deletes the retained automated backup with source DB instance resource identifier
`custom-db-123ABCEXAMPLE`.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance-automated-backup \
    --dbi-resource-id `custom-db-123ABCEXAMPLE`
```

For Windows:

```
aws rds delete-db-instance-automated-backup ^
    --dbi-resource-id `custom-db-123ABCEXAMPLE`
```
