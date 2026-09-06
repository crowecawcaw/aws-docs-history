

# Modifying an RDS Custom for SQL Server Multi-AZ deployment to a Single-AZ deployment
<a name="custom-sqlserver-multiaz.modify-maztosaz"></a>

You can modify an existing RDS Custom for SQL Server DB instance from a Multi-AZ to a Single-AZ deployment. 

## Console
<a name="custom-sqlserver-multiaz.modify-maztosaz.Console"></a>

**To modify an RDS Custom for SQL Server DB instance from a Multi-AZ to Single-AZ deployment.**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose **Databases**.

   The **Databases** pane appears.

1. Choose the RDS Custom for SQL Server DB instance that you want to modify.

1. For **Multi-AZ deployment**, choose **No**.

1. On the **Confirmation** page, choose **Apply immediately** to apply the changes immediately. Choosing this option doesn't cause downtime, but there is a possible performance impact. Alternatively, you can choose to apply the update during the next maintenance window. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).

1. On the **Confirmation** page, choose **Modify DB Instance**.

## AWS CLI
<a name="custom-sqlserver-multiaz.modify-maztosaz.CLI"></a>

To modify a Multi-AZ deployment to a Single-AZ deployment by using the AWS CLI, call the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command and include the `--no-multi-az` option. Specify the DB instance identifier and the values for other options that you want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.Settings.md). 

**Example**  
The following code modifies `mycustomdbinstance` by including the `--no-multi-az` option. The changes are applied during the next maintenance window by using `--no-apply-immediately`. Use `--apply-immediately` to apply the changes immediately. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mycustomdbinstance}} \
    --no-multi-az  \
    {{--no-apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mycustomdbinstance}} ^
    --no-multi-az \ ^
    {{--no-apply-immediately}}
```

## RDS API
<a name="custom-sqlserver-multiaz.modify-maztosaz.API"></a>

To modify a Multi-AZ deployment to a Single-AZ deployment by using the RDS API, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation and set the `MultiAZ` parameter to `false`.