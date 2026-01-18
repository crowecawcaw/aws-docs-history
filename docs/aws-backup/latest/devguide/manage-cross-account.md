# Managing AWS Backup resources across multiple

AWS accounts

###### Note

Before you manage resources across multiple AWS accounts in AWS Backup,
your accounts must belong to the same organization in the
AWS Organizations service.

## Cross-account management overview

You can use the cross-account management feature in AWS Backup to manage and monitor your
backup, restore, and copy jobs across AWS accounts that you configure with AWS Organizations.
[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") is a service that
offers policy-based management for multiple AWS accounts from a single management account.
It enables you to standardize the way you implement backup policies, minimizing manual
errors and effort simultaneously. From a central view, you can easily identify resources in
all accounts that meet the criteria that you are interested in.

If you set up AWS Organizations, you can configure AWS Backup to monitor activities in all of your
accounts in one place. You can also create a backup policy and apply it to selected accounts
that are part of your organization and view the aggregate backup job activities directly
from the AWS Backup console. This functionality enables backup administrators to effectively
monitor backup job status in hundreds of accounts across their entire enterprise from a
single management account. [AWS Organizations quotas](../../../organizations/latest/userguide/orgs_reference_limits.md "../../../organizations/latest/userguide/orgs_reference_limits.md")
apply.

For example, you define a backup policy A that takes daily backups of specific resources
and keeps them for 7 days. You choose to apply backup policy A to the whole organization.
(This means that each account in the organization gets that backup policy, which creates a
corresponding backup plan that is visible in that account.) Then, you create an OU named
Finance, and you decide to keep its backups for only 30 days. In this case, you define a
backup policy B, which overrides the lifecycle value, and attach it to that Finance OU. This
means that all the accounts under the Finance OU get a new effective backup plan that takes
daily backups of all specified resources and keeps them for 30 days.

In this example, backup policy A and backup policy B were merged into a single backup
policy, which defines the protection strategy for all accounts under the OU named Finance.
All the other accounts in the organization remain protected by backup policy A. Merging is
done only for backup policies that share the same backup plan name. You can also have policy
A and policy B coexist in that account without any merging. You can use advanced merging
operators in the JSON view of the console only. For details about merging policies, see
[Defining policies, policy syntax, and policy
inheritance](#merging-policies "#merging-policies") in the
_AWS Organizations User Guide_. For additional references and use cases, see
the blog [Managing backups at scale in your AWS Organizations using AWS Backup](https://aws.amazon.com/blogs/storage/managing-backups-at-scale-in-your-aws-organizations-using-aws-backup/ "https://aws.amazon.com/blogs/storage/managing-backups-at-scale-in-your-aws-organizations-using-aws-backup/") and the video tutorial
[Managing backups at scale in
your AWS Organizations using AWS Backup](https://www.youtube.com/watch?v=a6QI3iSCVz4 "https://www.youtube.com/watch?v=a6QI3iSCVz4").

Cross-account management consists of cross-account monitoring, cross-account
backups, backup policies, and delegated administrator accounts.
Not all of these elements are available in all Regions. For information about where
cross-account management is available, see [Feature availability by AWS Region](whatisbackup.md#features-by-region "whatisbackup.md#features-by-region") .

###### To use cross-account management

1. Create a management account in AWS Organizations and add accounts under the
   management account.
2. Enable the cross-account management feature in AWS Backup.
3. Create a backup policy to apply to all AWS accounts under your
   management account.

###### Note

For backup plans that are managed by Organizations, the resource opt-in
settings in the management account override the settings in a member account,
even if one or more delegated administrator accounts are configured. Delegated
administrator accounts are member accounts with enhanced features and cannot
override settings like a management account can. 4. Manage backup, restore, and copy jobs in all your AWS accounts.

## Cross-account management settings

Cross-account management allows you to enable or disable settings for managing and monitoring activities across multiple accounts within your organization.

Cross-account backup

Allow accounts in your organization to copy backups to other accounts.

Multi-party approval

Multi-party approval integration allows you to opt-in all accounts in your organization to Multi-party approval.

Delegated Administrator

Delegated Administrator allows Backup to automatically synchronize delegated administrator permissions with Organizations.

## Creating a management account in Organizations

First, you must [create your
organization](../../../organizations/latest/userguide/orgs_getting-started.md "../../../organizations/latest/userguide/orgs_getting-started.md") and configure it with AWS member accounts in AWS Organizations. For
instructions, see [Tutorial: Creating
and configuring an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") in the _AWS Organizations User
Guide_.

As you add member accounts to your organization, ensure that each account has:

- At least one backup and/or logically air-gapped vault
- An IAM role

The backup policies you create will have a backup plan, but they will also identify
the AWS Regions, the vault(s) used in the backup plan, the resources that will be
backed up, and the IAM role that will be used to create the backup. Backup policies
that reference accounts that lack the required information will not work as
expected.

For more information, see [Syntax for backup policies](../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md#backup-policy-syntax-reference "../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md#backup-policy-syntax-reference") in the _AWS Organizations User Guide_.

## Enabling cross-account management

Before you can use cross-account management in AWS Backup, the management account must
enable the feature (that is, _opt in_ to it). After the management
account enables cross-account management, you can create backup policies that manage
resources in multiple accounts.

###### To enable cross-account management

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
   You must sign in using the credentials of your management account.
2. In the left navigation pane, choose **Settings** to open the
   cross-account management page.
3. In the **Backup policies** section, choose
   **Enable**.

This gives you access to all the accounts and allows you to create policies
that automate management of multiple accounts in your organization
simultaneously. 4. In the **Cross-account monitoring** section, choose
**Enable**.

This enables you to monitor the backup, copy, and restore activities of all
accounts in your organization from your management account.

## Backup policies

You can combine backup plans with the scalability of [policies in
AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md") to create [backup
policies](../../../organizations/latest/userguide/orgs_manage_policies_backup.md "../../../organizations/latest/userguide/orgs_manage_policies_backup.md") to simplify management across your organization.

See the _AWS Organizations User Guide_ for information on how to
enable backup policies for your organization so you can:

- [Create a backup policy](../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md "../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md")
- [Update a backup policy](../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md#update-backup-policy-procedure "../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md#update-backup-policy-procedure"); or,
- [Delete a backup policy](../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md#delete-backup-policy-procedure "../../../organizations/latest/userguide/orgs_manage_policies_backup_create.md#delete-backup-policy-procedure")
- [Backup policy syntax and examples](../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md")

See [AWS Backup quotas](aws-backup-limits.md "aws-backup-limits.md") for
AWS Backup-specific quotas on elements contained in a policy.

##

Delegated administrator

Delegated administration provides a convenient way for assigned users in a
registered member account to perform most AWS Backup administrative tasks. You can
choose to delegate administration of AWS Backup to a member account in AWS Organizations, thereby
extending the ability to manage AWS Backup from outside the management account and across
the entire organization.

A management account, by default, is the account used to edit and manage policies.
Using the delegated administrator feature, you can delegate
these management functions to member accounts you designate. In turn,
those accounts can manage policies, in addition to the management account.

After a member account has been successfully registered for
delegated administration, it is a delegated administrator account. Note that
accounts, not users, are designated as delegated administrators.

Enabling delegated administrator accounts allows the option of managing
backup policies, it minimizes the number of users with access to the
management account, and it permits cross-account monitoring of jobs.

Below is a table showing the functions of the management account, accounts
delegated as Backup administrators, and accounts that are members within
the AWS Organization.

###### Note

Delegated administrator accounts are member accounts with enhanced features
but cannot override service opt-in settings of other member accounts
like a management account can.

| **PRIVILEGES**                                                  | **MANAGEMENT ACCOUNT** | **DELEGATED ADMINISTRATOR** | **MEMBER ACCOUNT** |
| --------------------------------------------------------------- | ---------------------- | --------------------------- | ------------------ |
| **Register/deregister delegated administrator accounts**        | Yes                    | No                          | No                 |
| **Enable cross-account management**                             | Yes                    | No                          | No                 |
| **Manage backup policies across accounts in AWS Organizations** | Yes                    | Yes                         | No                 |
| **Monitor cross-account jobs**                                  | Yes                    | Yes                         | No                 |

### Prerequisites

Before you can delegate backup administration, you must first register at least one
member account in your AWS organization as a
**delegated administrator**. Before you can register an account
as a delegated administrator, you must first configure the following:

- [AWS Organizations must be enabled and configured](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") with at least one member
  account in addition to your default management account.
- It is recommended that the Organization Management Account have the AWS Backup Backup Service-Linked Role
  (AWS BackupServiceRoleForBackup) present to automatically sync delegated administrator permissions with
  Organizations. This ensures delegated administrators have proper access when you enable opt-in
  regions or change administrator assignment. If the Backup Service-Linked Role is not present or got
  deleted, customers have a few options to create it:
  - Enabling the Delegated Administrator feature.
  - Access the Backup Vaults Console page.
  - Manually create it following the documentation in
    [Creating the Default Service Role.](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md")

- In the AWS Backup console, ensure **backup policies**,
  **cross-account monitoring**,
  **cross-account backup**, and
  **delegated administrator** features are turned on. These
  are below the **Delegated administrators** pane in
  the AWS Backup console.
  - [Cross-account monitoring](manage-cross-account.md#enable-cross-account "manage-cross-account.md#enable-cross-account") allows you to monitor
    backup activity across all the accounts in your organization
    from the management account, as well as from delegated administrator
    accounts.
  - _Optional:_ Cross-account backup,
    which allows accounts in your organization
    to copy backups to other accounts (for Backup-supported
    cross-account resources).
  - _Optional:_ Delegated administrator, which allows AWS Backup Backup
    to automatically create the Backup Service-Linked Role to sync delegated
    administrator permissions with Organizations.
  - Enable [service access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html") with AWS Backup.

There are two steps involved in setting up delegated administration. The first step is to delegate
cross-account jobs monitoring. The second step is to delegate backup policy management.

### Register a member account as a delegated administrator account

This is the first section: Using the AWS Backup console to register a delegated administrator account to monitor cross-
account jobs. To delegate AWS Backup policies, you will use the Organizations console in the next section.

**To register a member account using the AWS Backup Console:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
   You must sign in using the credentials of your management account.
2. Under **My Account** in the left-hand navigation of the console, choose
   **Settings**.
3. In the **Delegated administrator** pane, click
   **Register delegated administrator** or **Add delegated administrator**.
4. On the **Register delegated administrator** page, select the
   account you want to register, and then choose **Register account**.

This designated account will now be registered as a delegated administrator, with administrative privileges
to monitor jobs across accounts within the organization and can view and edit policies (policy delegation).
This member account cannot register or deregister other delegated administrator accounts. You can use the
console to register up to 5 accounts as delegated administrators.

Ensure that the delegated administrator has the permissions granted by [AWSBackupOrganizationAdminAccess](security-iam-awsmanpol.md#AWSBackupOrganizationAdminAccess "security-iam-awsmanpol.md#AWSBackupOrganizationAdminAccess").

**To register a member account using programmatically:**

Use the CLI command `register-delegated-administrator`. You can specify the following
parameters in your CLI request:

- `service-principal`
- `account-id`

Below is an example of a CLI request to register a member account programmatically:

```
aws organizations register-delegated-administrator \
--account-id 012345678912 \
--service-principal "backup.amazonaws.com"
```

### Deregister a member account

Use the following procedure to remove administrative access from AWS Backup by deregistering a member account
in your AWS organization that had previously been designated as a delegated administrator.

**To deregister a member account using the Console**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
   You must sign in using the credentials of your management account.
2. Under **My Account** in the left-hand navigation of the console, choose
   **Settings**.
3. In the **Delegated administrator** section, click **Deregister account**.
4. Choose the account(s) you want to deregister.
5. In the **Deregister account** dialog box, review the security
   implications, and then type `confirm` to complete the deregistration.
6. Choose `Deregister account`.

**To deregister a member account using programmatically:**

Use the CLI command `deregister-delegated-administrator` to deregister a delegated administrator
account. You can specify the following parameters in your API request:

- `service-principal`
- `account-id`

Below is an example of a CLI request to deregister a member account programmatically:

```
aws organizations deregister-delegated-administrator \
--account-id 012345678912 \
--service-principal "backup.amazonaws.com"
```

### Delegate AWS Backup policies through AWS Organizations

Within the AWS Organizations console, you can delegate administration of multiple policies, including
Backup policies.

From the management account logged into the
[AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"),
you can create, view, or delete a resource-based delegation policy for your organization.
For steps to delegate policies, see
[Create a resource-based delegation policy](../../../organizations/latest/userguide/orgs_delegate_policies.md "../../../organizations/latest/userguide/orgs_delegate_policies.md") in the _AWS Organizations User Guide_.

## Monitoring activities in multiple

AWS accounts

To monitor backup, copy, and restore jobs across accounts, you must enable
cross-account monitoring. This lets you monitor backup activities in all accounts from
your organizations management account. After you opt in, all the jobs across your
organization that were created after the opt-in are visible. When you opt out, AWS Backup
keeps the jobs in the aggregated view for 30 days (from reaching a terminus state).
Created jobs after the opt-out are not visible and do not show any newly created backup
jobs. For opt-in instructions, see [Enabling cross-account management](#enable-cross-account "#enable-cross-account").

###### To monitor multiple accounts

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
   You must sign in using the credentials of your management account.
2. In the left navigation pane, choose **Settings** to open the
   cross-account management page.
3. In the **Cross-account monitoring** section, choose
   **Enable**.

This enables you to monitor the backup and restore activities of all accounts
in your organization from your management account. 4. In the left navigation pane, choose **Cross-account
monitoring**. 5. On the **Cross-account monitoring** page, choose the
**Backup jobs**, **Restore jobs**, or
**Copy jobs** tab to see all the jobs created in all your
accounts. You can see each of these jobs by AWS account ID, and you can see
all the jobs in a particular account. 6. In the search box, you can filter the jobs by **Account ID**,
**Status**, or **Job ID**.

For example, you can choose the **Backup jobs** tab and see
all backup jobs created in all your accounts. You can filter the list by
**Account ID** and see all the backup jobs created in that
account.

## Resource opt-in rules

If a member account's backup plan was created by an Organizations-level backup policy, the
AWS Backup opt-in settings for the Organizations management account will override the opt-in settings
in that member account, but only for that backup plan.

If the member account also has local-level backup plans created by users, those backup
plans will follow the opt-in settings in the member account, without reference to the
Organizations management account's opt-in settings.

## Defining policies, policy syntax, and policy

inheritance

The following topics are documented in the _AWS Organizations User
Guide_.

- **Backup policies** – See [Backup
  policies](../../../organizations/latest/userguide/orgs_manage_policies_backup.md "../../../organizations/latest/userguide/orgs_manage_policies_backup.md").
- **Policy syntax** – See [Backup policy
  syntax and examples](../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_backup_syntax.md").
- **Inheritance for management policy types**
  – See [Inheritance for management policy types](../../../organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.md "../../../organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.md").
