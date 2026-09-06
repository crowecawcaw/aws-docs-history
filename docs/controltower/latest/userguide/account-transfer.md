

# Transfer an account to a different organization
<a name="account-transfer"></a>

You can transfer a member account that is enrolled in AWS Control Tower to a different AWS Organizations organization.

## Prerequisites
<a name="account-transfer-prerequisites"></a>
+ The account must be enrolled in AWS Control Tower in the source organization. That is, the account has baselines, proactive controls, or detective controls applied to it.
+ The account must have been created at least 4 days before the transfer.
+ You must have access to the management account of both the source and destination organizations.

## Step 1: Unenroll the account from AWS Control Tower
<a name="account-transfer-unenroll"></a>

Before you transfer the account, you must disable all AWS Control Tower resources directly applied to it. The account can continue to inherit preventive controls.

**If you use Auto Enroll**

Move the account to one of the following locations:
+ The root of the organization
+ An unmanaged OU
+ With Landing Zone 4.0 or later, an OU that has only preventive controls enabled

**If you don't use Auto Enroll**

The methods below are also available if you use Auto Enroll.
+ For accounts with the AWS Control Tower and Backup baseline, choose **Unmanage** from the AWS Control Tower console. You can also terminate the provisioned product with the AWS Service Catalog APIs or console.
+ For accounts with the AWS Config baseline, disable the AWS Config baseline on the OU, or move the account to root and use the `DisableBaseline` API.

## Step 2: Transfer the account to the destination organization
<a name="account-transfer-migrate"></a>

After all AWS Control Tower baselines and controls applied to the account other than preventive controls are disabled, complete the transfer.

1. From the management account of the destination organization, send an invitation to the member account.

1. Accept the invitation from the member account.

1. From the management account of the destination organization, move the account to the desired OU.

For instructions on the migration process, see [Migrating AWS accounts to a different organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_migration.html) in the *AWS Organizations User Guide*.

## Step 3: Enroll the account in the destination organization
<a name="account-transfer-enroll"></a>

After the account is in the destination organization, enroll it in AWS Control Tower.
+ If Auto Enroll is enabled in the AWS Control Tower landing zone that governs the destination organization, AWS Control Tower automatically applies baselines and controls to the account.
+ If you don't use Auto Enroll in the destination organization, manually enroll the account in AWS Control Tower. For more information, see [About enrolling existing accounts](enroll-account.md).

## Additional considerations
<a name="account-transfer-considerations"></a>

Wait period  
Accounts created through AWS Organizations or Account Factory must be at least 4 days old before you can transfer them or remove them from an organization. For more information, see [Removing a member account from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) in the *AWS Organizations User Guide*.

AWS Config aggregator limits  
When you transfer multiple accounts, you might reach the AWS Config limit for the maximum number of accounts added or deleted per week for all aggregators (1,000). To request a limit increase, see [AWS Config service limits](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html). You can also upgrade to landing zone version 4.0, which uses a service-linked Config aggregator. For more details, see [AWS Config updates in landing zone version 4.0](https://docs.aws.amazon.com/controltower/latest/userguide/config-updates-v4.html).

Member account access  
Unenrolled accounts don't have an `AWSControlTowerExecution` role. When you disable the Config or AWS Control Tower baseline, AWS Control Tower deletes its execution role and adds the `OrganizationsAccountAccessRole`. You can use this role to accept an invitation for the destination organization.  
When the account is enrolled in the destination organization, the `AWSControlTowerExecution` role is created. This role replaces the `OrganizationsAccountAccessRole` and trusts the new management account.

AWS Service Catalog and Auto Enroll  
Auto Enroll doesn't act on resources in AWS Service Catalog. Any Account Factory provisioned products remain in the management account even if the underlying accounts are unenrolled. To terminate these provisioned products in the management account, see [Deleting provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) in the *AWS Service Catalog User Guide*. Any Account Factory Customization (AFC) blueprints remain in the account.