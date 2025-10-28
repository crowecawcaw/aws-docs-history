# Amazon Redshift Serverless backups

## Overview

AWS Backup offers full backup management of your Amazon Redshift Serverless namespaces.
Through AWS Backup, you can schedule and restore Redshift Serverless manual snapshots through
the console or through CLI.

Redshift Serverless data protection through AWS Backup provides several options
for backing up and restoring your data warehouses. You can create a scheduled or on-demand
snapshot of your namespace. Then, you can choose to restore all the databases in that
snapshot to a Amazon Redshift provisioned cluster or a Serverless namespace. Alternatively, you
can restore a single table.

Redshift Serverless offers both automated and manual snapshots. Currently,
AWS Backup can be used to manage manual snapshots but not automated ones.

## Backup options for Redshift Serverless

You can use the AWS Backup console or CLI to create backups on demand or as part of a
backup plan.

### Create on-demand backup

You can create on-demand backups of Redshift Serverless namespaces through the following
steps:

Console

1. Open the [AWS Backup console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. On the dashboard, choose **Create an on-demand
   backup**.
3. Choose **Redshift Serverless** in the resource type
   dropdown menu.
4. Select the namespace you plan to back up.
5. Ensure **Create backup now** is selected.
6. Specify the retention period for the backup.
7. Choose an existing backup vault or create a new one.
8. Select the IAM role to use for the backup.
9. Optionally, add tags to the backup. To assign a tag to your on-demand
   backup, expand **Tags added to recovery points**, choose
   **Add new tag**, and enter a tag key and tag value.
10. Select **Create on-demand backup** to begin the backup
    job.
11. Once the job is initiated, the console will show the Jobs screen where you
    can see a list of your backup jobs and their statuses.

AWS CLI
Use the **start-backup-job** command.

**Required parameters**

- `BackupVaultName`
- `IamRoleArn`
- `ResourceArn`

**Optional parameters**

- `CompleteWindowMinutes`
- `IdempotencyToken`
- `Lifecyle`
- `StartWindowMinutes`

###### Example

The following example creates an on-demand backup of a Redshift Serverless
namespace.

```
aws backup start-backup-job \
    --backup-vault-name sample-vault \
    --iam-role-arn arn:aws:iam::`account`:role/service-role/AWSBackupDefaultServiceRole \
    --resource-arn arn:aws:redshift-serverless:`region`:`account`:namespace/`namespace-name-UUID`
```

### Create scheduled Redshift Serverless backups

in a backup plan

You can create a new backup plan for their Redshift Serverless namespaces through the AWS Backup
console or through CLI, or you can add Redshift Serverless to an existing backup plan.

Your scheduled backups can include Redshift Serverless namespaces if they are a protected
resource. To opt into protecting Redshift Serverless in the AWS Backup console, complete the following
steps:

Console
To opt into protecting Redshift Serverless in the AWS Backup console, complete the following
steps:

1. Open the [AWS Backup console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Using the navigation pane, choose **Protected
   resources**.
3. Toggle **Amazon Redshift Serverless** to **On**.
4. See [Select AWS services to backup](assigning-resources.md "assigning-resources.md") to include Redshift Serverless namespaces in an
   existing or new plan. When you add the resource type
   _Redshift Serverless_, you can choose to add **All Amazon
   Redshift namespaces**, or check the boxes next to the namespaces
   you wish to back up.

Under **Manage Backup plans**, you can:

- [Create a backup plan](creating-a-backup-plan.md "creating-a-backup-plan.md") and include Redshift Serverless;
- [Update](updating-a-backup-plan.md "updating-a-backup-plan.md") an existing backup plan to include Redshift Serverless.

AWS CLI
See [Create backup plans using the AWS CLI](creating-a-backup-plan.md#create-backup-plan-cli "creating-a-backup-plan.md#create-backup-plan-cli") for guidance to use
**create-backup-plan**.

If you want to alter an existing plan to include your Serverless resources,
use the command **update-backup-plan**.

The ARN (Amazon Resource Name) for Serverless resources to include in
"BackupSelection": { "Resources" has the following format:

```
arn:aws:redshift-serverless:Region:account:snapshot/a12bc34d-567e-890f-123g-h4ijk56l78m9
```

See [Amazon Redshift Serverless restore](redshift-serverless-restore.md "redshift-serverless-restore.md") for
information to restore data from a snapshot to a Serverless namespace.
