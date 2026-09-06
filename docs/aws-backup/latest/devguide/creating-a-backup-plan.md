

# Create a backup plan
<a name="creating-a-backup-plan"></a>

You can create a backup plan using the AWS Backup console, API, CLI, SDK, or an AWS CloudFormation template.

**Topics**
+ [Create backup plans using the AWS Backup console](#create-backup-plan-console)
+ [Create backup plans using the AWS CLI](#create-backup-plan-cli)
+ [Backup plan options and configuration](plan-options-and-configuration.md)
+ [CloudFormation templates for backup plans](plan-cfn.md)
+ [Delete a backup plan](deleting-a-backup-plan.md)
+ [Update a backup plan](updating-a-backup-plan.md)

## Create backup plans using the AWS Backup console
<a name="create-backup-plan-console"></a>

Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup). From the dashboard, choose **Manage Backup** plans. Or, using the navigation pane, choose **Backup plans** and choose **Create Backup** plan.

**Start options**

You have three choices for your new backup plan:
+ Create a backup plan based on an existing plan
+ Build a new plan
+ [Create a backup plan using the AWS CLI](#create-backup-plan-cli)

In this procedure, we build a new plan. Each part of the configuration has a link to an expanded section further on the page to where you can navigate for more detail.

1. Enter a plan name in **[Backup plan name](plan-options-and-configuration.md#plan-name)**.

   If you try to create a backup plan that is identical to an existing plan, you receive an `AlreadyExistsException` error.

1. Optionally, you can add tags to your backup plan.

1. **Backup rule configuration:** In the backup rule configuration section, you will set the backup schedule, window, and lifecycle.

1. **Schedule:**

   1. Enter a **backup rule name** in the text field.

   1. In the backup vault menu, choose **Default** or choose **Create new Backup vault** to create a vault.

   1. In the backup frequency menu, choose how often you want this plan to create a backup.

1. **Backup window:**

   1. **Start time** defaults to 12:30 AM (00:30 in 24hr time) in your system’s local timezone.

   1. **Start within** defaults to 8 hours. You can change this to specify a window of time for the backup to start.

   1. **Complete within** defaults to 7 days. Ensure that there is enough time for the backup up to complete even if the job starts at the end of the start window.

1. **[Continuous backups and point-in-time recovery (PITR)](point-in-time-recovery.md):** You can select **Enable continuous backups for point-in-time recovery (PITR)**. To verify which resources are supported for this type of backup, see the [Feature availability by resource](backup-feature-availability.md#features-by-resource) matrix.

1. **Lifecycle**

   1. **Cold storage:** Select this box to let eligible resource types transition to cold storage in accordance with the timetable you specify in the total retention period. To use cold storage, you must have a total retention period of 90 days or greater. However please note the following. Some services support incremental backups. For incremental backups, you must have at least one warm full backup. AWS Backup recommends that you set your lifecycle settings to not move your backup to cold storage until after at least 8 days. If the full backup is transitioned to cold storage too soon (for example, a transition to cold storage after 1 day), AWS Backup will create another warm full backup.

   1. **Cold storage for Amazon EBS** is [Amazon EBS Snapshots Archive](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html). Snapshots transitioned to archive storage tier will display in the console as cold tier. If cold storage is enabled, and if your backup frequency is monthly or less often, you can have your backup plan transition EBS snapshots.

   1. The **total retention period** is the number of days that you store your resource in AWS Backup. It is the total number of days of warm storage plus cold storage.

1. (*Optional*) You can opt in to have a backup index created with each periodic backup of a supported resource type (continuous backups will have daily indexes created). Only recovery points (backups) that have an associated index can be included in a [backup search](backup-search.md).

   For example, each time your backup plan creates an S3 backup, you can have a backup index for that backup created, also. This will allow that particular backup to be included in a future search.

   Place a check next to the resource type(s) for which you want to have indexes created.

1. (*Optional*) Enable malware scanning to automatically scan backups after they are created. When configuring malware protection, specify which resource types to scan (Amazon EC2, Amazon EBS, Amazon S3, or all supported resources) and the scanning types (full or incremental). Malware scanning applies only to your selected resource types. For example, if your backup plan includes both Amazon S3 and Amazon EC2 resources, but you enable malware scanning only for Amazon EC2, the service will scan only your EC2 backups. For each backup rule, you can configure which scanning type to use. The schedule of the backup rule will determine how frequently the scanning type takes place.
**Important**  
Before enabling malware protection, ensure your backup role and scanner role have the required permissions. For more information, see [the permissions documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/malware-protection.html#malware-access). 

1. (*Optional*) Use **Copy to destination** to create a cross-Region copy of eligible resources if you want to store a copy of a backup in a different AWS Region.

1. (*Optional*) Tags added to recovery points.

1. When all sections are set to your specifications, choose **Save Backup rule**.

## Create backup plans using the AWS CLI
<a name="create-backup-plan-cli"></a>

You can also define your backup plan in a JSON document and provide it using the AWS Backup console or AWS CLI. The following JSON document contains a sample backup plan that creates a daily backup at 1:00 Pacific time (the local time adjusts to daylight, standard, or summer time conditions if applicable). It automatically deletes a backup after one year.

```
{
  "BackupPlan":{
    "BackupPlanName":"{{test-plan}}",
    "Rules":[
      {
        "RuleName":"{{test-rule}}",
        "TargetBackupVaultName":"{{test-vault}}",
        "ScheduleExpression":"cron(0 1 ? * * *)",
        "ScheduleExpressionTimezone":"America/Los_Angeles",
        "StartWindowMinutes":{{integer}}, // Value is in minutes
        "CompletionWindowMinutes":{{integer}}, // Value is in minutes
        "IndexActions": [ 
               { 
                  "ResourceTypes": [ "{{string}}" ]
               }
            ],
        "Lifecycle":{
          "DeleteAfterDays":{{integer}}, // Value is in days
        }
      }
    ]
  }
}
```

You can store your JSON document with a name you choose. The following CLI command shows [`create-backup-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html) with a JSON named `test-backup-plan.json`:

```
aws backup create-backup-plan --cli-input-json file://{{PATH-TO-FILE}}/{{test-backup-plan}}.json
```

Note that while some systems number the days of the week from 0 to 6, we number them from 1 to 7. For more information, see [Cron and rate expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html). For more information about timezones, see [TimeZone](https://docs.aws.amazon.com/location/latest/APIReference/API_TimeZone.html) in the *Amazon Location Service API reference*.