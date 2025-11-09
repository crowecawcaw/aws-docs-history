# How continuity management works

AMS uses [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") for continuity management.

When starting to work with AWS Backup in AMS:

1. Run an on-demand backup
2. Create a backup plan (optional, AMS provides default backup plans)
3. Use the default AMS a backup vaults (optional)
4. Manage (run, refine, delete, and so forth) your backup plans and recovery points

## AMS backup plans

A backup plan is a policy expression that defines when and how you want to back up supported AWS resources, such as
RDS databases, EBS volumes, DynamoDB tables, and EFS file systems. Scheduling and retention policies are managed via
custom backup plans, which you can create using a change type (CT) with AMS Advanced or using AWS Backup with AMS Accelerate.
Assign resources to your backup plans using tags and AWS Backup automatically backs up and retains backups for assigned resources
according to the defined backup plan. You can create multiple backup plans if you have workloads with different backup
requirements.

A backup plan can have up to six backup rules that define a schedule and a retention period, among other details.
The backup schedule determines when AWS Backup initiates a backup job and how often a backup is created. You can choose a
frequency of hourly, daily, weekly, or monthly. The deletion days setting determines how many days the snapshot is
stored before being automatically deleted.

###### Note

AMS Advanced: If you are migrated from the legacy AMS backup system, AMS
creates a default backup plan for backwards compatibility. The **key:value** pair in this scenario is
**Backup:True**. To support backwards compatibility, the value here is case insensitive,
so **Backup:True** or **Backup:TRUE** are all valid tags.
All other key:value pairs are case sensitive.

AWS Backup can operate at the EBS volume level or at the Amazon EC2 instance level, but do not do both
at the same time, as this can lead to a race condition where the backups may clash.

### Default backup plans, multi-account landing zone

During the new **Account creation** RFC, AMS ensures that there is an overarching default backup
plan at the account level to safeguard your workloads. The values for mandatory fields are set by
default, as shown in the following section:

#### Default AMS backup plan

**default-backup-plan**

TAG key: `Backup`

TAG value: `True`

```
RuleForDailyBackups schedule expression: cron(30 23 ? * *) (a daily backup for 23:30 UTC time)
RuleForDailyBackups delete after days: 31 days
RuleForWeeklyBackups schedule expression: cron(30 23 ? * 7 *) (a weekly backup for 23:30 UTC time only on Saturday)
RuleForWeeklyBackups delete after weeks: 6 weeks
RuleForMonthlyBackups schedule expression: cron(30 23 * ? *) (a monthly backup for 23:30 UTC time on day 1 of the month)
RuleForMonthlyBackups delete after weeks: 26 weeks
RuleForYearlyBackups schedule expression: cron(30 23 1 1 ? *) (a yearly backup for 23:30 UTC time on day 1 of the month, only in January)
RuleForYearlyBackups delete after years: 2 years
```

| Default AMS backup plan | Start Time                                  | Retention |
| ----------------------- | ------------------------------------------- | --------- |
| hourly backup           | N/A                                         | N/A       |
| daily backup            | daily 11:30PM UTC                           | 7 days    |
| weekly backup           | weekly 11:30PM UTC, only on Saturday        | 4 weeks   |
| monthly backup          | monthly 11:30 PM UTC, on day 1 of the month | 26 weeks  |
| yearly backup           | 11:30 PM UTC, on day 1 of the month         | 2 years   |

#### Enhanced default AMS backup plan

This plan is a blueprint for AWS Backup best practices to protect against ransomware attacks. It implements a daily, weekly, monthly, and yearly backup
strategy. AWS Backup [continuous backup](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") is enabled with maximum
retention (31 days) on [supported resources](../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services "../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services").

**ams-enhanced-default-backup-plan**

TAG key: `backup-orchestrator-enhanced`

TAG value: `true`

```
RuleForDailyBackups schedule expression: cron(0 0 4 ? * * ) (a daily backup for 04:00 UTC time)
RuleForDailyBackups delete after days: 31 days
RuleForDailyBackups continuous backup: true
RuleForWeeklyBackups schedule expression: cron(0 0 2 ? * 7) (a weekly backup for 02:00 UTC time only on Saturday)
RuleForWeeklyBackups delete after weeks: 6 weeks
RuleForMonthlyBackups schedule expression: cron(0 2 1 * ? *) (a monthly backup for 02:00 UTC time on day 1 of the month)
RuleForMonthlyBackups delete after weeks: 26 weeks
RuleForYearlyBackups schedule expression: cron(0 2 1 1 ? *) (a yearly backup for 02:00 UTC time on day 1 of the month, only in January)
RuleForYearlyBackups delete after years: 2 years
```

| Enhanced AMS backup plan | Start Time                 | Retention |
| ------------------------ | -------------------------- | --------- |
| hourly backup            | N/A                        | N/A       |
| daily backup             | daily 4:00 UTC             | 31 days   |
| weekly backup            | Saturday, 2:00 UTC         | 6 weeks   |
| monthly backup           | 1st of the month, 2:00 UTC | 26 weeks  |
| yearly backup            | Jan 1st, 2:00 UTC          | 2 years   |

#### Data sensitive AMS backup plan

This plan is a blueprint for AWS Backup best practices to protect against ransomware attacks for data-sensitive applications. It implements an hourly, daily, weekly,
monthly, and yearly backup strategy. AWS Backup [continuous backup](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") is
enabled with maximum retention (31 days) on
[supported resources](../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services "../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services").

**ams-data-sensitive-backup-plan**

TAG key: `backup-orchestrator-data-sensitive`

TAG value: `true`

```
RuleForHourlyBackups schedule expression: cron(0 * ? * * *) (an hourly backup at the hour mark)
RuleForHourlyBackups delete after days: 7 days
RuleForDailyBackups schedule expression: cron(0 0 4 ? * * ) (a daily backup for 04:00 UTC time)
RuleForDailyBackups delete after days: 31 days
RuleForWeeklyBackups schedule expression: cron(0 0 2 ? * 7) (a weekly backup for 02:00 UTC time only on Saturday)
RuleForWeeklyBackups delete after weeks: 6 weeks
RuleForMonthlyBackups schedule expression: cron(0 2 1 * ? *) (a monthly backup for 02:00 UTC time on day 1 of the month)
RuleForMonthlyBackups delete after weeks: 26 weeks
RuleForYearlyBackups schedule expression: cron(0 2 1 1 ? *) (a yearly backup for 02:00 UTC time on day 1 of the month, only in January)
RuleForYearlyBackups delete after years: 2 years
```

| Data Sensitive AMS backup plan | Start Time                 | Retention |
| ------------------------------ | -------------------------- | --------- |
| hourly backup                  | at the hour mark           | 7 days    |
| daily backup                   | daily 4:00 UTC             | 31 days   |
| weekly backup                  | Saturday, 2:00 UTC         | 6 weeks   |
| monthly backup                 | 1st of the month, 2:00 UTC | 26 weeks  |
| yearly backup                  | Jan 1st, 2:00 UTC          | 2 years   |

## AMS backup vaults

AWS Backup organizes snapshots into logical storage units called vaults.

You can control backup vault notifications at individual vault-level using tags. You can opt out of notifications for a specific vault by adding the
tag `AMSNotificationOptOut` and setting the value to `True` on a specific vault. To resume getting notifications from the vault,
remove the tag.

To view a list of your AMS backups, open the
[AWS Backup console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup"). In the navigation pane, choose **Backup vaults** and select the one of
the AMS backup vaults from the following tables. In the **Backups** section, view the list of all the backups in the backup vault.
Select a backup to edit, delete, or restore.

**Vaults for AMS backup plans**

| AMS Vault Name                           | Description                                                                                                                                                                                                                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ams-automated-backups**                | This vault receives all recovery points taken by the AMS Advanced default AWS Backup plan **default-backup-plan**.                                                                                                                                  |
| **ams-automated-enhanced-backups**       | This vault receives all recovery points taken by AMS Advanced enhanced default AWS Backup plan **ams-enhanced-default-backup-plan**.                                                                                                                |
| **ams-automated-data-sensitive-backups** | This vault receives all recovery points taken by AMS Advanced AWS Backup plan **ams-data-sensitive-backup-plan**.                                                                                                                                   |
| **ams-manual-backups**                   | This is the default location for all backups from Start Backup Job RFC (ct-2hhud2lx01tq7) backup plans, if no vault name is defined.                                                                                                                |
| **ams-custom-backups**                   | This is the default location for the snapshots AMS takes prior to patching an instance using Patch Orchestrator or the monthly patch<br>activities. These are automatically removed according to the AMS patch lifecycle default policy of 60 days. |

## AMS backup change types

AMS provides several CTs for you to create and use backup plans.

###### Important

Do not edit your AMS default backup plans as your changes may be lost. Instead, create new plans for your custom configurations.

- [Backup plan: Create](../ctref/deployment-aws-backup-plan-create.md "../ctref/deployment-aws-backup-plan-create.md")
- [Backup Job: Start](../ctref/management-aws-backup-job-start.md "../ctref/management-aws-backup-job-start.md")
- [Backup Job: Stop](../ctref/management-aws-backup-job-stop.md "../ctref/management-aws-backup-job-stop.md")
- [Recovery Point: Delete](../ctref/management-aws-recovery-point-delete.md "../ctref/management-aws-recovery-point-delete.md")
- [DynamoDB | Create from Backup](../ctref/deployment-advanced-dynamodb-create-from-backup.md "../ctref/deployment-advanced-dynamodb-create-from-backup.md")
- [EBS Volume: Create From Backup](../ctref/deployment-advanced-ebs-volume-create-from-backup.md "../ctref/deployment-advanced-ebs-volume-create-from-backup.md")
- [Amazon Elastic File System (EFS): Create From Backup](../ctref/deployment-advanced-elastic-file-system-efs-create-from-backup.md "../ctref/deployment-advanced-elastic-file-system-efs-create-from-backup.md")

## AMS backup monitoring and reporting

###### Important

AMS backup monitoring and reporting are only available in AMS-supported regions. Those are US East (Virginia), US West (N. California), US West (Oregon), US East (Ohio), Canada (Central), South America (São Paulo), EU (Ireland), EU (Frankfurt), EU (London), EU (Paris), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo).

AMS generates daily self-service reports as well as monthly reports on resource coverage and backup job status. The monthly reports are shared in Monthly Business Reviews (MBRs). To learn more about daily backup reports, see [Daily backup report](daily-backup-report.md "daily-backup-report.md") .

AMS experts monitor all your backup tasks that are configured using AWS Backup. In case of backup failures, AMS investigates the failure and notifies you with the root cause and remediation options, if available. To avoid alert noise, during events that cause a high number of backup failures in your accounts, AMS makes a collective recommendation, through your CSDM, instead of notifying you for each individual failure.

Note that AMS does not monitor any backups configured using an AWS service’s standalone backup feature.
