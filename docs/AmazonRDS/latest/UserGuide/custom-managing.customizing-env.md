

# Customizing your RDS Custom environment
<a name="custom-managing.customizing-env"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

RDS Custom for Oracle includes built-in features that allow you to customize your DB instance environment without pausing automation. For example, you can use RDS APIs to customize your environment as follows:
+ Create and restore DB snapshots to create a clone environment.
+ Create read replicas.
+ Modify storage settings.
+ Change the CEV to apply release updates

For some customizations, such as changing the character set, you can't use the RDS APIs. In these cases, you need to change the environment manually by accessing your Amazon EC2 instance as the root user or logging in to your Oracle database as `SYSDBA`. 

To customize your instance manually, you must pause and resume RDS Custom automation. This pause ensures that your customizations don't interfere with RDS Custom automation. In this way, you avoid breaking the support perimeter, which places the instance in the `unsupported-configuration` state until you fix the underlying issues. Pausing and resuming are the only supported automation tasks when you modify an RDS Custom for Oracle DB instance.

## General steps for customizing your RDS Custom environment
<a name="custom-managing.pausing.general-steps"></a>

To customize your RDS Custom DB instance, complete the following steps:

1. Pause RDS Custom automation for a specified period using the console or CLI. 

1. Identify your underlying Amazon EC2 instance.

1. Connect to your underlying Amazon EC2 instance using SSH keys or AWS Systems Manager.

1. Verify your current configuration settings at the database or operating system layer.

   You can validate your changes by comparing the initial configuration to the changed configuration. Depending on the type of customization, use OS tools or database queries.

1. Customize your RDS Custom for Oracle DB instance as needed.

1. Reboot your instance or database, if required.
**Note**  
In an on-premises Oracle CDB, you can preserve a specified open mode for PDBs using a built-in command or after a startup trigger. This mechanism brings PDBs to a specified state when the CDB restarts. When opening your CDB, RDS Custom automation discards any user-specified preserved states and attempts to open all PDBs. If RDS Custom can't open all PDBs, the following event is issued: `The following PDBs failed to open: {{list-of-PDBs}}`.

1. Verify your new configuration settings by comparing them with the previous settings.

1. Resume RDS Custom automation in either of the following ways:
   + Resume automation manually.
   + Wait for the pause period to end. In this case, RDS Custom resumes monitoring and instance recovery automatically.

1. Verify the RDS Custom automation framework

   If you followed the preceding steps correctly, RDS Custom starts an automated backup. The status of the instance in the console shows **Available**.

For best practices and step-by-step instructions, see the AWS blog posts [Make configuration changes to an Amazon RDS Custom for Oracle instance: Part 1](https://aws.amazon.com/blogs/database/part-1-make-configuration-changes-to-an-amazon-rds-custom-for-oracle-instance/) and [Recreate an Amazon RDS Custom for Oracle database: Part 2](https://aws.amazon.com/blogs/database/part-2-recreate-an-amazon-rds-custom-for-oracle-database/).

## Pausing and resuming your RDS Custom DB instance
<a name="custom-managing.pausing"></a>

You can pause and resume automation for your DB instance using the console or CLI. 

### Console
<a name="custom-managing.pausing.console"></a>

**To pause or resume RDS Custom automation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB instance that you want to modify.

1. Choose **Modify**. The **Modify DB instance** page appears.

1. For **RDS Custom automation mode**, choose one of the following options:
   + **Paused** pauses the monitoring and instance recovery for the RDS Custom DB instance. Enter the pause duration that you want (in minutes) for **Automation mode duration**. The minimum value is 60 minutes (default). The maximum value is 1,440 minutes.
   + **Full automation** resumes automation.

1. Choose **Continue** to check the summary of modifications.

   A message indicates that RDS Custom will apply the changes immediately.

1. If your changes are correct, choose **Modify DB instance**. Or choose **Back** to edit your changes or **Cancel** to cancel your changes.

   On the RDS console, the details for the modification appear. If you paused automation, the **Status** of your RDS Custom DB instance indicates **Automation paused**.

1. (Optional) In the navigation pane, choose **Databases**, and then your RDS Custom DB instance.

   In the **Summary** pane, **RDS Custom automation mode** indicates the automation status. If automation is paused, the value is **Paused. Automation resumes in {{num}} minutes**.

### AWS CLI
<a name="custom-managing.pausing.CLI"></a>

To pause or resume RDS Custom automation, use the `modify-db-instance` AWS CLI command. Identify the DB instance using the required parameter `--db-instance-identifier`. Control the automation mode with the following parameters:
+ `--automation-mode` specifies the pause state of the DB instance. Valid values are `all-paused`, which pauses automation, and `full`, which resumes it.
+ `--resume-full-automation-mode-minutes` specifies the duration of the pause. The default value is 60 minutes.

**Note**  
Regardless of whether you specify `--no-apply-immediately` or `--apply-immediately`, RDS Custom applies modifications asynchronously as soon as possible.

In the command response, `ResumeFullAutomationModeTime` indicates the resume time as a UTC timestamp. When the automation mode is `all-paused`, you can use `modify-db-instance` to resume automation mode or extend the pause period. No other `modify-db-instance` options are supported.

The following example pauses automation for `my-custom-instance` for 90 minutes.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-custom-instance}} \
    --automation-mode all-paused \
    --resume-full-automation-mode-minutes 90
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-custom-instance}} ^
    --automation-mode all-paused ^
    --resume-full-automation-mode-minutes 90
```

The following example extends the pause duration for an extra 30 minutes. The 30 minutes is added to the original time shown in `ResumeFullAutomationModeTime`.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-custom-instance}} \
    --automation-mode all-paused \
    --resume-full-automation-mode-minutes 30
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-custom-instance}} ^
    --automation-mode all-paused ^
    --resume-full-automation-mode-minutes 30
```

The following example resumes full automation for `my-custom-instance`.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-custom-instance}} \
    --automation-mode full \
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my-custom-instance}} ^
    --automation-mode full
```
In the following partial sample output, the pending `AutomationMode` value is `full`.  

```
{
    "DBInstance": {
        "PubliclyAccessible": true,
        "MasterUsername": "admin",
        "MonitoringInterval": 0,
        "LicenseModel": "bring-your-own-license",
        "VpcSecurityGroups": [
            {
                "Status": "active",
                "VpcSecurityGroupId": "0123456789abcdefg"
            }
        ],
        "InstanceCreateTime": "2020-11-07T19:50:06.193Z",
        "CopyTagsToSnapshot": false,
        "OptionGroupMemberships": [
            {
                "Status": "in-sync",
                "OptionGroupName": "default:custom-oracle-ee-19"
            }
        ],
        "PendingModifiedValues": {
            "AutomationMode": "full"
        },
        "Engine": "custom-oracle-ee",
        "MultiAZ": false,
        "DBSecurityGroups": [],
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.custom-oracle-ee-19",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        ...
        "ReadReplicaDBInstanceIdentifiers": [],
        "AllocatedStorage": 250,
        "DBInstanceArn": "arn:aws:rds:us-west-2:012345678912:db:my-custom-instance",
        "BackupRetentionPeriod": 3,
        "DBName": "ORCL",
        "PreferredMaintenanceWindow": "fri:10:56-fri:11:26",
        "Endpoint": {
            "HostedZoneId": "ABCDEFGHIJKLMNO",
            "Port": 8200,
            "Address": "my-custom-instance.abcdefghijk.us-west-2.rds.amazonaws.com"
        },
        "DBInstanceStatus": "automation-paused",
        "IAMDatabaseAuthenticationEnabled": false,
        "AutomationMode": "all-paused",
        "EngineVersion": "19.my_cev1",
        "DeletionProtection": false,
        "AvailabilityZone": "us-west-2a",
        "DomainMemberships": [],
        "StorageType": "gp2",
        "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVW",
        "ResumeFullAutomationModeTime": "2020-11-07T20:56:50.565Z",
        "KmsKeyId": "arn:aws:kms:us-west-2:012345678912:key/aa111a11-111a-11a1-1a11-1111a11a1a1a",
        "StorageEncrypted": false,
        "AssociatedRoles": [],
        "DBInstanceClass": "db.m5.xlarge",
        "DbInstancePort": 0,
        "DBInstanceIdentifier": "my-custom-instance",
        "TagList": []
    }
```