# Converting a Multi-AZ deployment to a Single-AZ deployment in RDS Custom for Oracle

You can modify an existing RDS Custom for Oracle DB instance from a Multi-AZ to a Single-AZ
deployment.

## Console

###### To modify an RDS Custom for Oracle DB instance from a Multi-AZ to Single-AZ deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the Amazon RDS console, choose **Databases**. The
   **Databases** pane appears.
3. Choose the RDS Custom for Oracle DB instance that you want to modify.
4. For **Multi-AZ deployment**, choose
   **No**.
5. On the **Confirmation** page, choose **Apply
   immediately** to apply the changes immediately. Choosing this
   option doesn't cause downtime, but there is a possible performance impact.
   Alternatively, you can choose to apply the update during the next
   maintenance window. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.md "USER_ModifyInstance.md").
6. On the **Confirmation** page, choose **Modify DB
   Instance**.

## AWS CLI

To modify a Multi-AZ deployment to a Single-AZ deployment by using the AWS CLI, call
the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command and include the `--no-multi-az`
option. Specify the DB instance identifier and the values for other options that you
want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md").

###### Example

The following code modifies `mycustomdbinstance` by including the
`--no-multi-az` option. The changes are applied during the next
maintenance window by using `--no-apply-immediately`. Use
`--apply-immediately` to apply the changes immediately. For more
information, see [Using the schedule modifications setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mycustomdbinstance` \
    --no-multi-az \
    [--no-apply-immediately | --apply-immediately]
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mycustomdbinstance` ^
    --no-multi-az ^
    [--no-apply-immediately | --apply-immediately]
```

## RDS API

To modify a Multi-AZ deployment to a Single-AZ deployment by using the Amazon RDS API,
call the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") operation and set the `MultiAZ` parameter to
`false`.
