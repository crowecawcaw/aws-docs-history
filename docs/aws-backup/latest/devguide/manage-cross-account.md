

# Managing AWS Backup resources across multiple AWS accounts
<a name="manage-cross-account"></a>

**Note**  
Before you manage resources across multiple AWS accounts in AWS Backup, your accounts must belong to the same organization in the AWS Organizations service.

## Cross-account management overview
<a name="cross-account-management-overview"></a>

You can use the cross-account management feature in AWS Backup to manage and monitor your backup, restore, and copy jobs across AWS accounts that you configure with AWS Organizations. [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is a service that offers policy-based management for multiple AWS accounts from a single management account. It enables you to standardize the way you implement backup policies, minimizing manual errors and effort simultaneously. From a central view, you can easily identify resources in all accounts that meet the criteria that you are interested in.

If you set up AWS Organizations, you can configure AWS Backup to monitor activities in all of your accounts in one place. You can also create a backup policy and apply it to selected accounts that are part of your organization and view the aggregate backup job activities directly from the AWS Backup console. This functionality enables backup administrators to effectively monitor backup job status in hundreds of accounts across their entire enterprise from a single management account. [AWS Organizations quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) apply.

For example, you define a backup policy A that takes daily backups of specific resources and keeps them for 7 days. You choose to apply backup policy A to the whole organization. (This means that each account in the organization gets that backup policy, which creates a corresponding backup plan that is visible in that account.) Then, you create an OU named Finance, and you decide to keep its backups for only 30 days. In this case, you define a backup policy B, which overrides the lifecycle value, and attach it to that Finance OU. This means that all the accounts under the Finance OU get a new effective backup plan that takes daily backups of all specified resources and keeps them for 30 days. 

In this example, backup policy A and backup policy B were merged into a single backup policy, which defines the protection strategy for all accounts under the OU named Finance. All the other accounts in the organization remain protected by backup policy A. Merging is done only for backup policies that share the same backup plan name. You can also have policy A and policy B coexist in that account without any merging. You can use advanced merging operators in the JSON view of the console only. For details about merging policies, see [Defining policies, policy syntax, and policy inheritance](#merging-policies) in the *AWS Organizations User Guide*. For additional references and use cases, see the blog [Managing backups at scale in your AWS Organizations using AWS Backup](https://aws.amazon.com/blogs/storage/managing-backups-at-scale-in-your-aws-organizations-using-aws-backup/) and the video tutorial [Managing backups at scale in your AWS Organizations using AWS Backup](https://www.youtube.com/watch?v=a6QI3iSCVz4).

Cross-account management consists of cross-account monitoring, cross-account backups, backup policies, and delegated administrator accounts. Not all of these elements are available in all Regions. For information about where cross-account management is available, see [Feature availability by AWS Region](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-region) .

**To use cross-account management**

1. Create a management account in AWS Organizations and add accounts under the management account.

1. Enable the cross-account management feature in AWS Backup.

1. Create a backup policy to apply to all AWS accounts under your management account.
**Note**  
For backup plans that are managed by Organizations, the resource opt-in settings in the management account override the settings in a member account for that particular backup plan, even if one or more delegated administrator accounts are configured. Delegated administrator accounts are member accounts with enhanced features and cannot override settings like a management account can.

1. Manage backup, restore, and copy jobs in all your AWS accounts.

## Cross-account management settings
<a name="cross-account-management-settings"></a>

Cross-account management allows you to enable or disable settings for managing and monitoring activities across multiple accounts within your organization.

Cross-account backup  
Allow accounts in your organization to copy backups to other accounts.

Multi-party approval  
Multi-party approval integration allows you to opt-in all accounts in your organization to Multi-party approval.

Delegated Administrator  
Delegated Administrator allows Backup to automatically synchronize delegated administrator permissions with Organizations.

## Creating a management account in Organizations
<a name="create-organization"></a>

First, you must [create your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html) and configure it with AWS member accounts in AWS Organizations. For instructions, see [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) in the *AWS Organizations User Guide*.

As you add member accounts to your organization, ensure that each account has:
+ At least one backup and/or logically air-gapped vault
+ An IAM role

The backup policies you create will have a backup plan, but they will also identify the AWS Regions, the vault(s) used in the backup plan, the resources that will be backed up, and the IAM role that will be used to create the backup. Backup policies that reference accounts that lack the required information will not work as expected.

For more information, see [Syntax for backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_syntax.html#backup-policy-syntax-reference) in the *AWS Organizations User Guide*.

## Enabling cross-account management
<a name="enable-cross-account"></a>

Before you can use cross-account management in AWS Backup, the management account must enable the feature (that is, *opt in* to it). After the management account enables cross-account management, you can create backup policies that manage resources in multiple accounts.

**To enable cross-account management**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup). You must sign in using the credentials of your management account.

1. In the left navigation pane, choose **Settings** to open the cross-account management page.

1. In the **Backup policies** section, choose **Enable**. 

   This gives you access to all the accounts and allows you to create policies that automate management of multiple accounts in your organization simultaneously.

1. In the **Cross-account monitoring** section, choose **Enable**. 

   This enables you to monitor the backup, copy, and restore activities of all accounts in your organization from your management account.

## Backup policies
<a name="create-backup-policy"></a>

You can combine backup plans with the scalability of [policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) to create [backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html) to simplify management across your organization.

See the *AWS Organizations User Guide* for information on how to enable backup policies for your organization so you can:
+ [Create a backup policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_create.html)
+ [Update a backup policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_create.html#update-backup-policy-procedure); or,
+ [Delete a backup policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_create.html#delete-backup-policy-procedure)
+ [Backup policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_syntax.html)

See [AWS Backup quotas](aws-backup-limits.md) for AWS Backup-specific quotas on elements contained in a policy.

**Important**  
Backup policies support resource selection by resource types (for example, `arn:aws:ec2:*:*:volume/*`) or by tags, but not by individual resource ARNs. Use backup policies for broad application across multiple accounts in an organization or OU, not for targeting individual resources.  
To back up individual resources by ARN, use a local backup plan resource assignment instead.  
For full details on the `selections` syntax, see [Backup policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_syntax.html) in the AWS Organizations User Guide.

## Delegated administrator
<a name="backup-delegatedadmin"></a>

Delegated administration provides a convenient way for assigned users in a registered member account to perform most AWS Backup administrative tasks. You can choose to delegate administration of AWS Backup to a member account in AWS Organizations, thereby extending the ability to manage AWS Backup from outside the management account and across the entire organization.

A management account, by default, is the account used to edit and manage policies. Using the delegated administrator feature, you can delegate these management functions to member accounts you designate. In turn, those accounts can manage policies, in addition to the management account.

After a member account has been successfully registered for delegated administration, it is a delegated administrator account. Note that accounts, not users, are designated as delegated administrators.

Enabling delegated administrator accounts allows the option of managing backup policies, it minimizes the number of users with access to the management account, and it permits cross-account monitoring of jobs.

Below is a table showing the functions of the management account, accounts delegated as Backup administrators, and accounts that are members within the AWS Organization.

**Note**  
Delegated administrator accounts are member accounts with enhanced features but cannot override service opt-in settings of other member accounts like a management account can.


| **PRIVILEGES** | **MANAGEMENT ACCOUNT** | **DELEGATED ADMINISTRATOR** | **MEMBER ACCOUNT** | 
| --- | --- | --- | --- | 
| Register/deregister delegated administrator accounts | Yes | No | No | 
| Enable cross-account management | Yes | No | No | 
| Manage backup policies across accounts in AWS Organizations | Yes | Yes | No | 
| Monitor cross-account jobs | Yes | Yes | No | 

### Prerequisites
<a name="prereqs"></a>

Before you can delegate backup administration, you must first register at least one member account in your AWS organization as a **delegated administrator**. Before you can register an account as a delegated administrator, you must first configure the following:
+  [AWS Organizations must be enabled and configured](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) with at least one member account in addition to your default management account.
+  It is recommended that the Organization Management Account have the AWS Backup Service-Linked Role (AWSServiceRoleForBackup) present to automatically sync delegated administrator permissions with Organizations. This ensures delegated administrators have proper access when you enable opt-in regions or change administrator assignment. If the Backup Service-Linked Role is not present or got deleted, customers have a few options to create it: 
  + Enabling the Delegated Administrator feature.
  + Access the Backup Vaults Console page.
  + Manually create it following the documentation in [ Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html).
+ In the AWS Backup console, ensure **backup policies**, **cross-account monitoring**, **cross-account backup**, and **delegated administrator** features are turned on. These are below the **Delegated administrators** pane in the AWS Backup console.
  + [ Cross-account monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html#enable-cross-account) allows you to monitor backup activity across all the accounts in your organization from the management account, as well as from delegated administrator accounts.
  + *Optional:* Cross-account backup, which allows accounts in your organization to copy backups to other accounts (for Backup-supported cross-account resources).
  + *Optional:* Delegated administrator, which allows AWS Backup to automatically create the Backup Service-Linked Role to sync delegated administrator permissions with Organizations. 
  + Enable [ service access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html) with AWS Backup.

There are two steps involved in setting up delegated administration. The first step is to delegate cross-account jobs monitoring. The second step is to delegate backup policy management.

### Register a member account as a delegated administrator account
<a name="registermemberaccount"></a>

This is the first section: Using the AWS Backup console to register a delegated administrator account to monitor cross- account jobs. To delegate AWS Backup policies, you will use the Organizations console in the next section.

**To register a member account using the AWS Backup Console:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup). You must sign in using the credentials of your management account.

1. Under **My Account** in the left-hand navigation of the console, choose **Settings**.

1. In the **Delegated administrator** pane, click **Register delegated administrator** or **Add delegated administrator**.

1. On the **Register delegated administrator** page, select the account you want to register, and then choose **Register account**.

This designated account will now be registered as a delegated administrator, with administrative privileges to monitor jobs across accounts within the organization. This member account cannot register or deregister other delegated administrator accounts. You can use the console to register up to 5 accounts as delegated administrators.

**Important**  
Registering an account as a delegated administrator alone does not enable backup policy management. To allow the delegated administrator account to view and edit backup policies, you must also complete the following steps:  
Attach the [AWSBackupOrganizationAdminAccess](security-iam-awsmanpol.md#AWSBackupOrganizationAdminAccess) managed policy to the IAM roles or users in the delegated administrator account that need to perform organization-level tasks. This policy is not attached automatically.
Delegate backup policy management through AWS Organizations by creating a resource-based delegation policy in the management account. For steps, see [Delegate AWS Backup policies through AWS Organizations](#policydelegation).

**To register a member account using programmatically:**

Use the CLI command `register-delegated-administrator`. You can specify the following parameters in your CLI request:
+ `service-principal`
+ `account-id`

Below is an example of a CLI request to register a member account programmatically:

```
aws organizations register-delegated-administrator \
--account-id 012345678912 \
--service-principal "backup.amazonaws.com"
```

### Deregister a member account
<a name="deregistermemberaccount"></a>

 Use the following procedure to remove administrative access from AWS Backup by deregistering a member account in your AWS organization that had previously been designated as a delegated administrator.

**To deregister a member account using the Console**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup). You must sign in using the credentials of your management account.

1. Under **My Account** in the left-hand navigation of the console, choose **Settings**.

1. In the **Delegated administrator** section, click **Deregister account**.

1. Choose the account(s) you want to deregister.

1. In the **Deregister account** dialog box, review the security implications, and then type `confirm` to complete the deregistration.

1. Choose `Deregister account`.

**To deregister a member account using programmatically:**

Use the CLI command `deregister-delegated-administrator` to deregister a delegated administrator account. You can specify the following parameters in your API request:
+ `service-principal`
+ `account-id`

Below is an example of a CLI request to deregister a member account programmatically:

```
aws organizations deregister-delegated-administrator \
--account-id 012345678912 \
--service-principal "backup.amazonaws.com"
```

### Delegate AWS Backup policies through AWS Organizations
<a name="policydelegation"></a>

Within the AWS Organizations console, you can delegate administration of multiple policies, including Backup policies.

From the management account logged into the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2), you can create, view, or delete a resource-based delegation policy for your organization. For steps to delegate policies, see [ Create a resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html) in the *AWS Organizations User Guide*.

## Monitoring activities in multiple AWS accounts
<a name="enable-xcross-monitoring"></a>

To monitor backup, copy, and restore jobs across accounts, you must enable cross-account monitoring. This lets you monitor backup activities in all accounts from your organizations management account. After you opt in, all the jobs across your organization that were created after the opt-in are visible. When you opt out, AWS Backup keeps the jobs in the aggregated view for 30 days (from reaching a terminus state). Created jobs after the opt-out are not visible and do not show any newly created backup jobs. For opt-in instructions, see [Enabling cross-account management](#enable-cross-account).

**To monitor multiple accounts**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup). You must sign in using the credentials of your management account.

1. In the left navigation pane, choose **Settings** to open the cross-account management page.

1. In the **Cross-account monitoring** section, choose **Enable**. 

   This enables you to monitor the backup and restore activities of all accounts in your organization from your management account.

1. In the left navigation pane, choose **Cross-account monitoring**.

   

1. On the **Cross-account monitoring** page, choose the **Backup jobs**, **Restore jobs**, or **Copy jobs** tab to see all the jobs created in all your accounts. You can see each of these jobs by AWS account ID, and you can see all the jobs in a particular account.

1. In the search box, you can filter the jobs by **Account ID**, **Status**, or **Job ID**.

   For example, you can choose the **Backup jobs** tab and see all backup jobs created in all your accounts. You can filter the list by **Account ID** and see all the backup jobs created in that account.

## Resource opt-in rules
<a name="resource-opt-in-rules"></a>

If a member account's backup plan was created by an Organizations-level backup policy, the AWS Backup opt-in settings for the Organizations management account will override the opt-in settings in that member account, but only for that backup plan.

If the member account also has local-level backup plans created by users, those backup plans will follow the opt-in settings in the member account, without reference to the Organizations management account's opt-in settings.

## Defining policies, policy syntax, and policy inheritance
<a name="merging-policies"></a>

The following topics are documented in the * AWS Organizations User Guide*.
+ **Backup policies** – See [Backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html).
+ **Policy syntax** – See [Backup policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup_syntax.html).
+ **Inheritance for management policy types ** – See [Inheritance for management policy types](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html).