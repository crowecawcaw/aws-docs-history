

# Modifying an Amazon RDS DB instance
<a name="Overview.DBInstance.Modifying"></a>

You can change the settings of a DB instance to accomplish tasks such as adding additional storage or changing the DB instance class. In this topic, you can find out how to modify an Amazon RDS DB instance and learn about the settings for DB instances. 

We recommend that you test any changes on a test instance before modifying a production instance. Doing this helps you to fully understand the impact of each change. Testing is especially important when upgrading database versions. 

Most modifications to a DB instance you can either apply immediately or defer until the next maintenance window. Some modifications, such as parameter group changes, require that you manually reboot your DB instance for the change to take effect. 

**Important**  
Some modifications result in downtime because Amazon RDS must reboot your DB instance for the change to take effect. Review the impact to your database and applications before modifying your DB instance settings. 

## Console
<a name="USER_ModifyInstance.Console"></a>

**To modify a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify. 

1. Choose **Modify**. The **Modify DB instance** page appears.

1. Change any of the settings that you want. For information about each setting, see [Settings for DB instances](USER_ModifyInstance.Settings.md). 

1. When all the changes are as you want them, choose **Continue** and check the summary of modifications. 

1. (Optional) Choose **Apply immediately** to apply the changes immediately. Choosing this option can cause downtime in some cases. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md). 

1. On the confirmation page, review your changes. If they are correct, choose **Modify DB instance** to save your changes. 

   Or choose **Back** to edit your changes or **Cancel** to cancel your changes. 

## AWS CLI
<a name="USER_ModifyInstance.CLI"></a>

To modify a DB instance by using the AWS CLI, call the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command. Specify the DB instance identifier and the values for the options that you want to modify. For information about each option, see [Settings for DB instances](USER_ModifyInstance.Settings.md). 

**Example**  
The following code modifies `mydbinstance` by setting the backup retention period to 1 week (7 days). The code enables deletion protection by using `--deletion-protection`. To disable deletion protection, use `--no-deletion-protection`. The changes are applied during the next maintenance window by using `--no-apply-immediately`. Use `--apply-immediately` to apply the changes immediately. For more information, see [Using the schedule modifications setting](USER_ModifyInstance.ApplyImmediately.md).   
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{mydbinstance}} \
    --backup-retention-period {{7}} \
    {{--deletion-protection}} \
    {{--no-apply-immediately}}
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{mydbinstance}} ^
    --backup-retention-period {{7}} ^
    {{--deletion-protection}} ^
    {{--no-apply-immediately}}
```

**Example**  
The following example adds a storage volume to an RDS for Oracle DB instance. The additional volume uses gp3 storage with 5000 GiB of allocated storage and 12000 IOPS.  

```
aws rds modify-db-instance \
     --db-instance-identifier my-oracle-instance \
     --additional-storage-volumes '[{ \
             "VolumeName": "rdsdbdata2", \
             "StorageType": "gp3",
             "AllocatedStorage": 5000, \
             "IOPS": 12000 \
         }]'
```

## RDS API
<a name="USER_ModifyInstance.API"></a>

To modify a DB instance by using the Amazon RDS API, call the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation. Specify the DB instance identifier, and the parameters for the settings that you want to modify. For information about each parameter, see [Settings for DB instances](USER_ModifyInstance.Settings.md). 