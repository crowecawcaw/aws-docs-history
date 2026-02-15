# Associating a DB parameter group with a

DB instance in Amazon Aurora

You can create your own DB parameter groups with customized settings. You can associate a DB parameter group
with a DB instance using the AWS Management Console, the AWS CLI, or the RDS API. You can do so when you
create or modify a DB instance.

For information about creating a DB parameter group, see [Creating a DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). For information about modifying a DB instance, see [Modifying a DB instance in a DB cluster](Aurora.md#Aurora.Modifying.Instance "Aurora.md#Aurora.Modifying.Instance").

###### Note

When you associate a new DB parameter group with a DB instance, the modified static and dynamic
parameters are applied only after the DB instance is rebooted. However, if you modify
dynamic parameters in the DB parameter group after you associate it with the DB instance, these changes
are applied immediately without a reboot.

###### To associate a DB parameter group with a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB instance that you want to modify.
3. Choose **Modify**. The **Modify
   DB instance** page appears.
4. Change the **DB parameter group** setting.
5. Choose **Continue** and check the summary of
   modifications.
6. (Optional) Choose **Apply immediately** to apply the
   changes immediately. Choosing this option can cause an outage in some
   cases.
7. On the confirmation page, review your changes. If they are correct,
   choose **Modify DB instance** to save your changes.

Or choose **Back** to edit your changes or
**Cancel** to cancel your changes.
To associate a DB parameter group with a DB instance, use the AWS CLI [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the following
options:

- `--db-instance-identifier`
- `--db-parameter-group-name`
  The following example associates the `mydbpg` DB parameter group with the
  `database-1` DB instance. The changes are applied immediately by using
  `--apply-immediately`. Use `--no-apply-immediately` to
  apply the changes during the next maintenance window.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `database-1` \
    --db-parameter-group-name `mydbpg` \
    `--apply-immediately`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `database-1` ^
    --db-parameter-group-name `mydbpg` ^
    `--apply-immediately`
```

To associate a DB parameter group with a DB instance, use the RDS API [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") operation with the following
parameters:

- `DBInstanceName`
- `DBParameterGroupName`
