

# Converting a Multi-AZ deployment to a Single-AZ deployment in RDS Custom for Oracle
<a name="custom-oracle-multiaz-modify-multi-to-single"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can modify an existing RDS Custom for Oracle DB instance from a Multi-AZ to a Single-AZ deployment.

## Console
<a name="custom-oracle-multiaz-multi-to-single-console"></a>

**To modify an RDS Custom for Oracle DB instance from a Multi-AZ to Single-AZ deployment**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose **Databases**. The **Databases** pane appears.

1. Choose the RDS Custom for Oracle DB instance that you want to modify.

1. For **Multi-AZ deployment**, choose **No**.

1. On the **Confirmation** page, choose **Apply immediately** to apply the changes immediately. Choosing this option doesn't cause downtime, but there is a possible performance impact. Alternatively, you can choose to apply the update during the next maintenance window. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).

1. On the **Confirmation** page, choose **Modify DB Instance**.

## AWS CLI
<a name="custom-oracle-multiaz-multi-to-single-cli"></a>

To modify a Multi-AZ deployment to a Single-AZ deployment by using the AWS CLI, call the [modify-db-instance](https://docs.aws.amazon.com//cli/latest/reference/rds/modify-db-instance.html) command and include the `--no-multi-az` option. Specify the DB instance identifier and the values for other options that you want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.Settings.md).

**Example**  
The following code modifies `mycustomdbinstance` by including the `--no-multi-az` option. The changes are applied during the next maintenance window by using `--no-apply-immediately`. Use `--apply-immediately` to apply the changes immediately. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mycustomdbinstance}} \
    --no-multi-az \
    [--no-apply-immediately | --apply-immediately]
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mycustomdbinstance}} ^
    --no-multi-az ^
    [--no-apply-immediately | --apply-immediately]
```

## RDS API
<a name="custom-oracle-multiaz-multi-to-single-api"></a>

To modify a Multi-AZ deployment to a Single-AZ deployment by using the Amazon RDS API, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation and set the `MultiAZ` parameter to `false`.