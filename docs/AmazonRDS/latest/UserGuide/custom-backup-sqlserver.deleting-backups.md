

# Deleting RDS Custom for SQL Server automated backups
<a name="custom-backup-sqlserver.deleting-backups"></a>

You can delete retained automated backups for RDS Custom for SQL Server when they are no longer needed. The procedure is the same as the procedure for deleting Amazon RDS backups.

## Console
<a name="USER_WorkingWithAutomatedBackups-sqlserver-Deleting.CON"></a>

**To delete a retained automated backup**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Automated backups**.

1. Choose **Retained**.

1. Choose the retained automated backup that you want to delete.

1. For **Actions**, choose **Delete**.

1. On the confirmation page, enter **delete me** and choose **Delete**. 

## AWS CLI
<a name="USER_WorkingWithAutomatedBackups-sqlserver-Deleting.CLI"></a>

You can delete a retained automated backup by using the AWS CLI command [delete-db-instance-automated-backup](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-instance-automated-backup.html).

The following option is used to delete a retained automated backup:
+ `--dbi-resource-id` – The resource identifier for the source RDS Custom DB instance.

  You can find the resource identifier for the source DB instance of a retained automated backup by using the AWS CLI command [describe-db-instance-automated-backups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instance-automated-backups.html).

The following example deletes the retained automated backup with source DB instance resource identifier `custom-db-123ABCEXAMPLE`.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds delete-db-instance-automated-backup \
2.     --dbi-resource-id {{custom-db-123ABCEXAMPLE}}
```
For Windows:  

```
1. aws rds delete-db-instance-automated-backup ^
2.     --dbi-resource-id {{custom-db-123ABCEXAMPLE}}
```