

# Associating a DB parameter group with a DB instance in Amazon RDS
<a name="USER_WorkingWithParamGroups.Associating"></a>

You can create your own DB parameter groups with customized settings. You can associate a DB parameter group with a DB instance using the AWS Management Console, the AWS CLI, or the RDS API. You can do so when you create or modify a DB instance.

For information about creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Creating.md). For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).  For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

**Note**  
When you associate a new DB parameter group with a DB instance, the modified static and dynamic parameters are applied only after the DB instance is rebooted. However, if you modify dynamic parameters in the DB parameter group after you associate it with the DB instance, these changes are applied immediately without a reboot.

## Console
<a name="USER_WorkingWithParamGroups.Associating.CON"></a>

**To associate a DB parameter group with a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify. 

1. Choose **Modify**. The **Modify DB instance** page appears.

1. Change the **DB parameter group** setting. 

1. Choose **Continue** and check the summary of modifications. 

1. (Optional) Choose **Apply immediately** to apply the changes immediately. Choosing this option can cause an outage in some cases. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).

1. On the confirmation page, review your changes. If they are correct, choose **Modify DB instance** to save your changes. 

   Or choose **Back** to edit your changes or **Cancel** to cancel your changes. 

## AWS CLI
<a name="USER_WorkingWithParamGroups.Associating.CLI"></a>

To associate a DB parameter group with a DB instance, use the AWS CLI [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command with the following options:
+ `--db-instance-identifier`
+ `--db-parameter-group-name`

The following example associates the `mydbpg` DB parameter group with the `database-1` DB instance. The changes are applied immediately by using `--apply-immediately`. Use `--no-apply-immediately` to apply the changes during the next maintenance window. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{database-1}} \
    --db-parameter-group-name {{mydbpg}} \
    {{--apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{database-1}} ^
    --db-parameter-group-name {{mydbpg}} ^
    {{--apply-immediately}}
```

## RDS API
<a name="USER_WorkingWithParamGroups.Associating.API"></a>

To associate a DB parameter group with a DB instance, use the RDS API [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation with the following parameters:
+ `DBInstanceName`
+ `DBParameterGroupName`