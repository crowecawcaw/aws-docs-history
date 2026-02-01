# Pausing and resuming RDS Custom automation

RDS Custom automatically provides monitoring and instance recovery for an RDS Custom for SQL Server DB instance. If you need to
customize the instance, do the following:

1. Pause RDS Custom automation for a specified period. The pause ensures that your customizations don't interfere with RDS Custom
   automation.
2. Customize the RDS Custom for SQL Server DB instance as needed.
3. Do either of the following:
   - Resume automation manually.
   - Wait for the pause period to end. In this case, RDS Custom resumes monitoring and instance
     recovery automatically.

###### Important

Pausing and resuming automation are the only supported automation tasks when modifying an RDS Custom for SQL Server DB instance.

###### To pause or resume RDS Custom automation

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB instance that you
   want to modify.
3. Choose **Modify**. The **Modify DB instance** page appears.
4. For **RDS Custom automation mode**, choose one of the following options:
   - **Paused** pauses the monitoring and instance
     recovery for the RDS Custom DB instance. Enter the pause duration
     that you want (in minutes) for **Automation mode
     duration**. The minimum value is 60 minutes
     (default). The maximum value is 1,440 minutes.
   - **Full automation** resumes automation.

5. Choose **Continue** to check the summary of modifications.

A message indicates that RDS Custom will apply the changes immediately. 6. If your changes are correct, choose **Modify DB instance**. Or choose
**Back** to edit your changes or **Cancel** to cancel your
changes.

On the RDS console, the details for the modification appear. If you paused automation, the
**Status** of your RDS Custom DB instance indicates **Automation
paused**. 7. (Optional) In the navigation pane, choose **Databases**, and then your
RDS Custom DB instance.

In the **Summary** pane, **RDS Custom automation mode**
indicates the automation status. If automation is paused, the value is **Paused.
Automation resumes in `num` minutes**.
To pause or resume RDS Custom automation, use the `modify-db-instance` AWS CLI command. Identify the DB
instance using the required parameter `--db-instance-identifier`. Control the automation mode with the
following parameters:

- `--automation-mode` specifies the pause state of the DB instance. Valid values are
  `all-paused`, which pauses automation, and `full`, which resumes
  it.
- `--resume-full-automation-mode-minutes` specifies the duration of the pause. The
  default value is 60 minutes.

###### Note

Regardless of whether you specify `--no-apply-immediately` or `--apply-immediately`, RDS Custom
applies modifications asynchronously as soon as possible.

In the command response, `ResumeFullAutomationModeTime` indicates the resume time as a UTC timestamp. When
the automation mode is `all-paused`, you can use `modify-db-instance` to resume automation mode or
extend the pause period. No other `modify-db-instance` options are supported.

The following example pauses automation for `my-custom-instance` for 90 minutes.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --automation-mode all-paused \
    --resume-full-automation-mode-minutes 90
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --automation-mode all-paused ^
    --resume-full-automation-mode-minutes 90
```

The following example extends the pause duration for an extra 30 minutes. The 30 minutes is added to
the original time shown in `ResumeFullAutomationModeTime`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --automation-mode all-paused \
    --resume-full-automation-mode-minutes 30
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --automation-mode all-paused ^
    --resume-full-automation-mode-minutes 30
```

The following example resumes full automation for `my-custom-instance`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --automation-mode full \
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --automation-mode full
```

In the following partial sample output, the pending `AutomationMode` value is
`full`.

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
