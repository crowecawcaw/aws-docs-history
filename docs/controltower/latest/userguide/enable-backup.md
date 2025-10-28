# Enable backups

You can enable backups for resources in your accounts that are enrolled in AWS Control Tower,
either during landing zone setup, or when you update your landing zone.

###### As [Prerequisites](backup-prerequisites.md "backup-prerequisites.md"),

you must provide the following items

- An AWS account to serve as the AWS Backup Administrator account
- An AWS account to serve as the AWS Backup Central Backup account
- A multi-region AWS KMS key that you manage, for cross-account backups
  **How to enable backups**

The enablement process has two main parts: _first_, enable backups
for your landing zone; _then_, enable backups for each registered OU
that requires backups.

## First part: Set up backups for your landing

zone

**Console:** You can set up backups for your landing zone in the
AWS Control Tower console, on the **Landing zone settings** page. You'll see
this option during the initial landing zone setup operation, and you can revisit it
later with a landing zone update.

**API:** You can enable backups with the AWS Control Tower APIs, by
calling the [`UpdateLandingZone`](../APIReference/API_UpdateLandingZone.md "../APIReference/API_UpdateLandingZone.md") API, if you already have an AWS Control Tower
landing zone, or the [`CreateLandingZone`](../APIReference/API_CreateLandingZone.md "../APIReference/API_CreateLandingZone.md") API if you're setting up AWS Control Tower
for the first time. (Hint: After that, call the [`EnableBaseline`](../APIReference/API_EnableBaseline.md "../APIReference/API_EnableBaseline.md") API to establish backups for each OU
that you require.)

**Outside the AWS Control Tower console**

Part of enabling backups for your landing zone includes a step outside of the
AWS Control Tower console. You must navigate to the AWS Backup console to review your
resources.

###### To review your opted-in resource types or opt-in to additional resource

types

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Settings**.
3. On the **Service opt-in** page, choose
   **Configure resources**.
4. Use the toggle switches to enable or disable the services that you want
   to include with AWS Backup. _Be sure that the resources that you want to
   back up are selected, such as RDS, EC2, DDB, and so forth, whether they
   are part of your AWS Control Tower environment or not._

For more details, see [Opt in to managing services with AWS Backup](../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in "../../../aws-backup/latest/devguide/working-with-supported-services.md#opt-in").

###### Considerations for new resource types

Before you rely on AWS Backup to manage data protection for any AWS service's
resources, you must perform the previous procedure and opt in to AWS Backup for that
service. Also, as the AWS Backup service adds support for additional services and
their resource types in the future, you must repeat this procedure and opt in
for each additional resource type with AWS Backup before you can back up that
resource type in AWS Control Tower. Tagging an unsupported resource type may cause your
backup to fail.

When you activate backups for your landing zone, AWS Control Tower establishes the two
accounts you've provided as the **Central Backup** account and the
**Backup Administrator** account, respectively. AWS Control Tower
creates [resources](backup-resources.md "backup-resources.md") in
these accounts and other accounts.

###### Important

To enable backups for the AWS Control Tower **Audit** and
**Log Archive** accounts, you must set up backups for the
**Security OU,** by calling the `EnableBaseline`
API. We recommend that you do so.

**The recommended bank of
plans and retention is as follows:**

- Hourly backups = 2-weeks retention in local vault, no copy in central
  backup vault
- Daily backups = 2-weeks retention in local vault, 1-month retention in
  central backup vault
- Weekly backups = 1-month retention in local vault, 3-months retention in
  central vault
- Monthly backups = 3-months retention in local vault, 3-months retention in
  central backup vault

For information about how to create your backup plans, see [Creating
report plans using the AWS Backup console](../../../aws-backup/latest/devguide/create-report-plan-console.md "../../../aws-backup/latest/devguide/create-report-plan-console.md").

## Next part: Enable backups on OUs

After you enable AWS Backup in your landing zone settings, you must take the additional
step to enable backup on the specific OUs that you want to back up. If you've
enabled AWS Backup for your landing zone, you'll see a section on the **OU
details** page in the console, which allows you to choose
**Enable backup** for the OU. If backup is not enabled at the
landing zone level, you will not see this section on the OU details page.

To enable the `BackupBaseline` on an OU, that OU must have the
`AWSControlTowerBaseline` enabled already. Enrolled accounts in each
OU have the `AWSControlTowerBaseline` enabled.

###### In your selected accounts and OUs, AWS Control Tower sets up additional

resources

- **A local Backup vault**

AWS Control Tower creates a local backup vault in your accounts, with four possible
types of backup plans attached to the vault. Backup plans created through
AWS Control Tower are tagged with a prefix.

```
BackupPlanTags:
        aws-control-tower: 'managed-by-control-tower'
```

- **Four types of backup
  plans**—**hourly**,
  **daily**, **weekly**,
  **monthly**.

Each plan is associated with a tag-based resource assignment. For example,
any resource tagged with **aws-control-tower-backuphourly :
true** is protected with an hourly backup plan.

- **A local backup role in your
  accounts**

AWS Control Tower creates an IAM role, which is used for backups. The role requires
four specific permissions.

```
"backup:UpdateGlobalSettings","organizations:RegisterDelegatedAdministrator","organizations:EnableAWSServiceAccess","organizations:DeregisterDelegatedAdministrator"
```

The role has a trust relationship with the service principal for AWS Backup The
role is named `aws-controltower-backup-role`, and it has the
following managed permissions attached to it:

    + [`AWSBackupServiceRolePolicyForBackup`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.md")
    + [`AWSBackupServiceRolePolicyForRestores`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md")
    + [`AWSBackupServiceRolePolicyForS3Backup`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Backup.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Backup.md")
    + [`AWSBackupServiceRolePolicyForS3Restore`](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.md")

**Tag resources for backup**

Part of the process of setting up backups in AWS Control Tower is to tag the resources that
you wish to include in your backup plan. The tags specify the frequency of backups.
These are the possible tags.

- `aws-control-tower-backuphourly : true`
- `aws-control-tower-backupdaily: true`
- `aws-control-tower-backupweekly: true`
- `aws-control-tower-backupmonthly: true`

**Considerations**

- When AWS Backup is active on an OU, you’ll see a value of
  **Enabled** in the **Status** field on
  the **OU details** page in the AWS Control Tower console. Some other
  possible values of the **Status** field include
  **Not enabled**, **In progress**, and
  **Failed**. If you see a status of
  **Failed**, choose
  **Re-register OU** to reapply your AWS Backup configuration to
  the OU.
- If you have AWS Backup enabled on an OU, new accounts provisioned through
  Account Factory under that the OU will include AWS Backup.
