# Logically air-gapped vault

## Overview of logically air-gapped vaults

AWS Backup offers a secondary type of vault which can store copies of backups in a container
with additional security features. A **logically air-gapped vault** is a
specialized vault which provides increased security beyond a standard backup vault, as well
as the ability to share vault access to other accounts so that recovery
time objectives (RTOs) can be faster and more flexible in case of an incident that requires
rapid restoration of resources.

Logically air-gapped vaults come equipped with additional protection features; each
vault is encrypted with either an [AWS owned key](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") (default) or optionally with a customer-managed KMS key, and each vault is equipped with [AWS Backup Vault
Lock](vault-lock.md "vault-lock.md")'s compliance mode. The encryption key type information is visible through AWS Backup APIs and console for transparency and compliance reporting.

You can integrate your logically air-gapped vaults with [Multi-party approval](multipartyapproval.md "multipartyapproval.md") (MPA) to enable recovery of backups in
the vaults even if the vault-owning account is inaccessible, which helps to maintain
business continuity. Further more, you can choose to integrate with [AWS Resource Access Manager](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") (RAM) to share a logically air-gapped vault with other AWS accounts
(including accounts in other organizations) so that the backups stored within the vault can
be restored from an account with which the vault is shared, if needed for data loss recovery
or [restore testing](restore-testing.md "restore-testing.md"). As part of this added security, a
logically air-gapped vault stores its backups in an AWS Backup service owned account (which
results in backups shown as shared outside your organization in modify attribute items in
AWS CloudTrail logs).

You can view the storage pricing for backups of supported services in a logically
air-gapped vault on the [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/")
page.

See [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") for
resource types you can copy to a logically air-gapped vault.

###### Topics

- [Use case for logically air-gapped vaults](#lag-usecase "#lag-usecase")
- [Compare and contrast with a standard backup
  vault](#lag-compare-and-contrast "#lag-compare-and-contrast")
- [Create a logically air-gapped vault](#lag-create "#lag-create")
- [View logically air-gapped vault details](#lag-view "#lag-view")
- [Copy to a logically air-gapped vault](#lag-copy "#lag-copy")
- [Share a logically air-gapped vault](#lag-share "#lag-share")
- [Restore a backup from a logically air-gapped vault](#lag-restore "#lag-restore")
- [Delete a logically air-gapped vault](#lag-delete "#lag-delete")
- [Additional programmatic options for logically air-gapped
  vaults](#lag-programmatic "#lag-programmatic")
- [Understanding encryption key types for logically air-gapped vaults](#lag-encryption-key-types "#lag-encryption-key-types")
- [Troubleshoot a logically air-gapped vault issue](#lag-troubleshoot "#lag-troubleshoot")
- [Multi-party approval for logically air-gapped
  vaults](multipartyapproval.md "multipartyapproval.md")

## Use case for logically air-gapped vaults

A logically air-gapped vault is a secondary vault that serves as part of a data
protection strategy. This vault can help enhance your organization's retention strategy and
recovery when you desire a vault for your backups that

- Is automatically set with a vault lock in [compliance
  mode](vault-lock.md "vault-lock.md")
- By default offers encryption with an AWS owned key. Optionally you can provide a customer managed key
- Contains backups which, through AWS RAM or MPA, can be shared with and restored from a
  different account than the one that created the backup

**Considerations and limitations**

- Cross-Region copy to or from a logically air-gapped vault is not currently available
  for backups that contain Amazon Aurora, Amazon DocumentDB, and Amazon Neptune.
- A backup containing one or more Amazon EBS volumes that is copied into a logically air-gapped vault must
  be smaller than 16 TB; backups for this resource type that are greater in size
  are not supported.
- Amazon EC2 offers [EC2 Allowed AMIs](../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md "../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md"). If
  this setting is enabled in your account, add the alias `aws-backup-vault` to your
  allowlist.

If this alias is not included, copy operations from a logically air-gapped vault to
a backup vault and restore operations of EC2 instances from a logically air-gapped vault
will fail with an error message such as "Source AMI ami-xxxxxx not found in Region."

- The ARN (Amazon Resource Name) of a recovery point stored in a logically air-gapped
  vault will have `backup` in place of the underlying resource type. For
  example, if the original ARN begins with
  `arn:aws:ec2:`region`::image/ami-*` , then the
  ARN of the recovery point in the logically air-gapped vault will be
  `arn:aws:backup:`region`:`account-id`:recovery-point:*`.

You can use the CLI command [`list-recovery-points-by-backup-vault`](API_ListRecoveryPointsByBackupVault.md "API_ListRecoveryPointsByBackupVault.md") to determine the
ARN.

## Compare and contrast with a standard backup

vault

A **backup vault** is the primary and standard type of vault used in
AWS Backup. Each backup is stored in a backup vault when the backup is created. You can assign
resource-based policies to manage backups stored in the vault, such as the lifecycle of
backups stored within the vault.

A **logically air-gapped vault** is a specialized vault with additional
security and flexible sharing for faster recovery time (RTO). This vault stores copies of
backups that were initially created and stored within a standard backup vault.

Backup vaults are encrypted with a key, a security mechanism
that limits access to intended users. These keys can be customer managed or AWS managed.
See [Copy encryption](encryption.md#copy-encryption "encryption.md#copy-encryption") for encryption behavior
during copy jobs, including copying into a logically air-gapped vault.

Additionally, a backup vault can have additional security through a vault lock; logically air-gapped
vaults come equipped by a vault lock in compliance mode.

Similar to backup vaults, logically air-gapped vaults also support
[restricted tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-restrictions "../../../AWSEC2/latest/UserGuide/Using_Tags.md#tag-restrictions")
for Amazon EC2 backups.

| Feature                                                                                | Backup vault                                                                                                                                                                                                                                                                                                                      | Logically air-gapped vault                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AWS Backup Audit Manager](aws-backup-audit-manager.md "aws-backup-audit-manager.md")  | You can use AWS Backup Audit Manager [Controls and<br>remediation](controls-and-remediation.md "controls-and-remediation.md") to monitor your backup vaults.                                                                                                                                                                      | Ensure a copy of a backup of a specific resource has been copied to<br>[at least one logically air-gapped<br>vault](controls-and-remediation.md#resources-in-lag-vault-control "controls-and-remediation.md#resources-in-lag-vault-control") on a schedule you determine, in addition to controls available to<br>standard vaults.                                                           |
| [Backup<br>creation](creating-a-backup.md "creating-a-backup.md")                      | When a backup is created, it is stored as a recovery<br>point.                                                                                                                                                                                                                                                                    | Backups are not stored in this vault upon creation.                                                                                                                                                                                                                                                                                                                                          |
| [Backup storage](vaults.md "vaults.md")                                                | Can store initial backups of resources and copies of<br>backups                                                                                                                                                                                                                                                                   | Can store copies of backups from other vaults                                                                                                                                                                                                                                                                                                                                                |
| Billing                                                                                | Storage and data transfer charges for resources fully managed by AWS Backup<br>occur under "AWS Backup". Other resource type storage and data transfer charges will<br>occur under their respective services.<br>For example, Amazon EBS backups will show under "Amazon EBS"; Amazon S3 backups will show<br>under "AWS Backup". | All billing charges from these vaults (storage or data transfer) occur<br>under "AWS Backup".                                                                                                                                                                                                                                                                                                |
| [Regions](whatisbackup.md#features-by-region "whatisbackup.md#features-by-region")     | Available in all Regions in which AWS Backup operates                                                                                                                                                                                                                                                                             | Available in most Regions supported by AWS Backup. Not currently available in<br>Asia Pacific (Malaysia), Canada West (Calgary), China (Beijing), China (Ningxia),<br>AWS GovCloud (US-East), or AWS GovCloud (US-West).                                                                                                                                                                     |
| [Resources](whatisbackup.md#supported-resources "whatisbackup.md#supported-resources") | Can store copies of backups for most resource types that support<br>cross-account copy.                                                                                                                                                                                                                                           | See the logically air-gapped vault column in<br>[Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource")<br>for resources that can be copied to<br>this vault.                                                                                                                                          |
| [Restore](restoring-a-backup.md "restoring-a-backup.md")                               | Backups can be restored by the same account to which the<br>vault belongs.                                                                                                                                                                                                                                                        | Backups can be restored by a different account than the one to<br>which the vault belongs if the vault is shared with that separate account.                                                                                                                                                                                                                                                 |
| [Security](security-considerations.md "security-considerations.md")                    | Can optionally be encrypted with a key (customer managed or AWS<br>managed)<br>Can optionally use a vault lock in compliance or governance<br>mode                                                                                                                                                                                | Can be encrypted with an [AWS owned key](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") or a customer managed key<br>Is always locked with a [vault lock](vault-lock.md "vault-lock.md") in<br>compliance mode<br>Encryption key type information is preserved and visible when vaults are shared through AWS RAM or MPA |
| [Sharing](#lag-share "#lag-share")                                                     | Access can be managed through policies and [AWS Organizations](manage-cross-account.md "manage-cross-account.md")<br>Not compatible with AWS RAM                                                                                                                                                                                  | Can optionally be shared across accounts using [AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md")                                                                                                                                                                                                        |

## Create a logically air-gapped vault

You can create a logically air-gapped vault either through the AWS Backup console or through
a combination of AWS Backup and AWS RAM CLI commands.

Each logically air-gapped comes equipped with a vault lock in compliance mode. See [AWS Backup Vault Lock](vault-lock.md "vault-lock.md") to help determine the retention
period values most appropriate for your operation

Console

###### Create a logically air-gapped vault from the console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, select **Vaults**.
3. Both types of vaults will be displayed. Select **Create new
   vault**.
4. Enter a name for your backup vault. You can name your vault to reflect what
   you will store in it, or to make it easier to search for the backups you need. For
   example, you could name it `FinancialBackups`.
5. Select the radio button for **Logically air-gapped vault**.
6. _(Optional)_ Choose an encryption key. You can select a customer-managed KMS key for additional control over encryption, or use the default AWS-owned key (recommended).
7. Set the **Minimum retention period**.

This value (in days, months, or years) is the shortest amount of time a backup
can be retained in this vault. Backups with retention periods shorter than this
value cannot be copied to this vault.

The minimum value allowed is `7` days. Values for months
and years meet this minimum. 8. Set the **Maximum retention period**.

This value (in days, months, or years) is the longest amount of time a backup
can be retained in this vault. Backups with retention periods greater than this
value cannot be copied to this vault. 9. _(Optional)_ Add tags that will help you search for and
identify your logically air-gapped vault. For example, you could add a
`BackupType:Financial` tag. 10. Select **Create vault**. 11. Review the settings. If all settings show as you intended, select
**Create logically air-gapped vault**. 12. The console will take you to the details page of your new vault. Verify the
vault details are as expected. 13. Select **Vaults** to view vaults in your account. Your logically air-gapped vault
will be displayed. The KMS key will be available approximately 1 to 3 minutes
after the vault creation. Refresh the page to see the associated key. Once the key
is visible, the vault is in an available state and can be used.

AWS CLI
Create a logically air-gapped vault from CLI

You can use AWS CLI to programmatically carry out operations for logically
air-gapped vaults. Each CLI is specific to the AWS service in which it originates.
Commands related to sharing are prepended with `aws ram`; all other
commands should be prepended with `aws backup`.

Use the CLI command [`create-logically-air-gapped-backup-vault`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-logically-air-gapped-backup-vault.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-logically-air-gapped-backup-vault.html"), modified with the
following parameters:

```
aws backup create-logically-air-gapped-backup-vault
--region us-east-1 // *optional*
--backup-vault-name `sampleName` // *required*
--min-retention-days `7` // *required* *Value must be an integer 7 or greater*
--max-retention-days `35` // *required*
--encryption-key-arn `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012` // *optional*
--creator-request-id `123456789012-34567-8901` // *optional*
```

The optional `--encryption-key-arn` parameter allows you to specify a customer-managed KMS key for vault encryption. If not provided, the vault will use an AWS-owned key.

Example CLI command to create a logically air-gapped vault:

```
aws backup create-logically-air-gapped-backup-vault
--region us-east-1
--backup-vault-name sampleName
--min-retention-days 7
--max-retention-days 35
--creator-request-id 123456789012-34567-8901 // optional
```

Example CLI command to create a logically air-gapped vault with customer-managed encryption:

```
aws backup create-logically-air-gapped-backup-vault
--region us-east-1
--backup-vault-name sampleName
--min-retention-days 7
--max-retention-days 35
--encryption-key-arn arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
--creator-request-id 123456789012-34567-8901 // optional
```

See [CreateLogicallyAirGappedBackupVault API response elements](API_CreateLogicallyAirGappedBackupVault.md "API_CreateLogicallyAirGappedBackupVault.md") for information
after the create operation. If the operation was successful, the new logically
air-gapped vault will have the VaultState of `CREATING`.

Once the creation is complete and the KMS encrypted key has been assigned, the
VaultState will transition to `AVAILABLE`. Once available, the vault can be
used. `VaultState` can be retrieved by calling [`DescribeBackupVault`](API_DescribeBackupVault.md "API_DescribeBackupVault.md") or [`ListBackupVaults`](API_ListBackupVaults.md "API_ListBackupVaults.md").

## View logically air-gapped vault details

You can see the vault details such as summary, the recovery points, the protected
resources, account sharing, access policy, and tags through the AWS Backup console or the AWS Backup
CLI.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Vaults** from the left-hand navigation.
3. Below the descriptions of vaults will be two lists, **Vaults owned by
   this account** and **Vaults shared with this
   account**. Select the desired tab to view the vaults.
4. Under **Vault name**, click on the name of the vault to open
   the details page. You can see the summary, the recovery points, the protected
   resources, account sharing, access policy, and tag details.

Details display depending on account type: Accounts which own a vault can
view account sharing; accounts which do not own a vault will not be able
to view account sharing. For shared vaults, the encryption key type (AWS-owned
or customer-managed KMS key) is displayed in the vault summary.

AWS CLI
View details of a logically air-gapped vault through CLI

The CLI command [`describe-backup-vault`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-vault.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-backup-vault.html") can be used to obtain details about a
vault. Parameter `backup-vault-name` is required; `region` is
optional.

```
aws backup describe-backup-vault
--region `us-east-1`
--backup-vault-name `testvaultname`
```

Example of response:

```
{
"BackupVaultName": "LOG-AIR-GAP-VAULT-TEST",
"BackupVaultArn": "arn:aws:backup:us-east-1:234567890123:backup-vault:IAD-LAGV-01",
"VaultType": "LOGICALLY_AIR_GAPPED_BACKUP_VAULT",
"EncryptionKeyType": "AWS_OWNED_KMS_KEY",
"CreationDate": "2024-07-25T16:05:23.554000-07:00",
"NumberOfRecoveryPoints": 0,
"Locked": true,
"MinRetentionDays": 8,
"MaxRetentionDays": 30,
"LockDate": "2024-07-25T16:05:23.554000-07:00"
}
```

## Copy to a logically air-gapped vault

Logically air-gapped vaults can only be a copy job destination target in a backup plan
or a target for an on-demand copy job.

**Compatible encryption**

A successful copy job from a backup vault to a logically air-gapped vault requires
an encryption key that is determined by the resource type being copied.

When you copy a backup of a [fully managed
resource type](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource"), the source backup in the (standard backup vault) can be
encrypted by a customer managed key or by an AWS managed key.

When you copy a backup of other resource types (ones [not fully managed](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource")), the backup must be encrypted with a customer managed key. AWS managed keys
for the resource types are not supported for copies.

**Copy to a logically air-gapped vault through a backup plan**

You can copy a backup (recovery point) from a standard backup vault to a logically
air-gapped vault by [creating a new backup plan](creating-a-backup-plan.md "creating-a-backup-plan.md")
or [updating an existing one](updating-a-backup-plan.md "updating-a-backup-plan.md") in the AWS Backup
console or through the AWS CLI commands [`create-backup-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html") and [`update-backup-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-backup-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/update-backup-plan.html").

You can copy a backup from one logically air-gapped vault to another logically
air-gapped vault on-demand (this type of backup cannot be scheduled in a backup plan). You
can copy a backup from a logically air-gapped vault to a standard backup vault as long as
the copy is encrypted with a customer managed key.

**On-demand backup copy to a logically air-gapped vault**

To create a one-time [on-demand](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") copy of a backup to a logically air-gapped vault, you can copy from a
standard backup vault. Cross-Region or cross-account copies are available if the resource
type supports the copy type.

**Copy availability**

A copy of a backup can be created from the account to which the vault belongs. Accounts
with which the vault has been shared have the ability to view or a restore a backup, but not
to create a copy.

Only [resource types that support cross-Region or
cross-account copy](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") can be included.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Vaults** from the left-hand navigation.
3. In the vault detail page, all recovery points within that vault are displayed.
   Place a check mark next to the recovery point you wish to copy.
4. Select **Actions**, and then select **Copy**
   from the drop-down menu.
5. On the next screen, input the details of the destination.
   1. Specify the destination Region.
   2. Destination backup vault drop-down menu displays eligible destination
      vaults. Select one with the type `logically air-gapped
vault`

6. Select **Copy** once all details are set to your preferences.

On the **Jobs** page in the console, you can select
**Copy** jobs to see current copy jobs.

AWS CLI
Use [start-copy-job](https://amazonaws.com/aws-backup/latest/devguide/API_StartCopyJob.html "https://amazonaws.com/aws-backup/latest/devguide/API_StartCopyJob.html") to copy an existing backup in a backup vault to a logically
air-gapped vault.

Sample CLI input:

```
aws backup start-copy-job
--region `us-east-1`
--recovery-point-arn `arn:aws:resourcetype:region::snapshot/snap-12345678901234567`
--source-backup-vault-name `sourcevaultname`
--destination-backup-vault-arn `arn:aws:backup:us-east-1:123456789012:backup-vault:destinationvaultname`
--iam-role-arn `arn:aws:iam::123456789012:role/service-role/servicerole`
```

For more information, see [Copying a backup](recov-point-create-a-copy.md "recov-point-create-a-copy.md"),
[cross-Region backup](cross-region-backup.md "cross-region-backup.md"), and [Cross-account
backup](create-cross-account-backup.md "create-cross-account-backup.md").

## Share a logically air-gapped vault

You can use AWS Resource Access Manager (RAM) to share a logically air-gapped vault with other accounts
you designate. When sharing vaults, the encryption key type information (AWS-owned or
customer-managed KMS key) is preserved and visible to accounts with which the vault is shared.

A vault can be shared with an account in its organization or with an account in another
organization. The vault cannot be shared with an entire organization, only with accounts within the
organization.

Only accounts with specific IAM privileges can share and manage the sharing of vaults.

To share using AWS RAM, ensure you have the following:

- Two or more accounts that can access AWS Backup
- Vault-owning account that intends to share has necessary RAM permissions. The permission
  `ram:CreateResourceShare` is necessary for this procedure. The policy
  `AWSResourceAccessManagerFullAccess` contains all needed RAM-related
  permissions:
  - `backup:DescribeBackupVault`
  - `backup:DescribeRecoveryPoint`
  - `backup:GetRecoveryPointRestoreMetadata`
  - `backup:ListProtectedResourcesByBackupVault`
  - `backup:ListRecoveryPointsByBackupVault`
  - `backup:ListTags`
  - `backup:StartRestoreJob`

- At least one logically air-gapped vault

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Vaults** from the left-hand navigation.
3. Below the descriptions of vaults will be two lists, **Vaults owned by
   this account** and **Vaults shared with this
   account**. Vaults owned by the account are eligible to be
   shared.
4. Under **Vault name**, select the name of the logically
   air-gapped vault to open the details page.
5. The **Account sharing** pane shows with which accounts the
   vault is being shared.
6. To begin sharing with another account or to edit accounts already being
   shared, select **Manage sharing**.
7. The AWS RAM console opens when **Manage sharing** is selected.
   For steps to share a resource using AWS RAM, see [Creating a resource
   share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User
   Guide_.
8. The account invited to accept an invitation to receive a share has 12 hours to
   accept the invitation. See [Accepting and
   rejecting resource share invitations](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the _AWS RAM User
   Guide_.
9. If the sharing steps are completed and accepted, the vault summary page will
   show under **Account sharing = “Shared - see account sharing table
   below**”.

AWS CLI
AWS RAM uses the CLI command `create-resource-share`. The access to this
command is only available to accounts with sufficient permissions. See [Creating a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") for CLI steps.

Steps 1 through 4 are conducted with the account that owns the logically
air-gapped vault. Steps 5 through 8 are conducted with the account with which the
logically air-gapped vault will be shared.

1. Log into the owning account OR request a user at your organization with
   sufficient credentials for accessing the source account completes these steps.
   1. If a resource share was previously created and you wish to add an
      additional resource to it, use CLI `associate-resource-share`
      instead with the ARN of the new vault.

2. Fetch credentials of a role with sufficient permissions to share via RAM.
   [Input these into the CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new").
   1. The permission `ram:CreateResourceShare` is necessary for this
      procedure. The policy [AWSResourceAccessManagerFullAccess](https://console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAWSResourceAccessManagerFullAccess "https://console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAWSResourceAccessManagerFullAccess") contains all RAM-related
      permissions.

3. Use [create-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html").
   1. Include the ARN of the logically air-gapped vault.
   2. Example input:

   ```
   aws ram create-resource-share
   --name `MyLogicallyAirGappedVault`
   --resource-arns arn:aws:backup:us-east-1:`123456789012`:backup-vault:`test-vault-1`
   --principals `123456789012`
   --region us-east-1
   ```

   3. Example output:

   ```
   {
      "resourceShare":{
         "resourceShareArn":"arn:aws:ram:us-east-1:123456789012:resource-share/12345678-abcd-09876543",
         "name":"MyLogicallyAirGappedVault",
         "owningAccountId":"123456789012",
         "allowExternalPrincipals":true,
         "status":"ACTIVE",
         "creationTime":"2021-09-14T20:42:40.266000-07:00",
         "lastUpdatedTime":"2021-09-14T20:42:40.266000-07:00"
      }
   }
   ```

4. Copy the resource share ARN in the output (which is needed for subsequent
   steps). Give the ARN to the operator of account you are inviting to receive the
   share.
5. Obtain the resource share ARN
   1. If you did not perform steps 1 through 4, obtain the resourceShareArn from
      whomever did.
   2. Example:
      `arn:aws:ram:us-east-1:`123456789012`:resource-share/`12345678-abcd-09876543``

6. In the CLI, assume credentials of the recipient account.
7. Get resource share invitation with [`get-resource-share-invitations`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-share-invitations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-share-invitations.html"). For more information,
   see [Accepting and
   rejecting invitations](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the _AWS RAM User
   Guide_.
8. Accept the invitation in destination (recovery) account.
   1. Use [`accept-resource-share-invitation`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/accept-resource-share-invitation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/accept-resource-share-invitation.html") (can also [`reject-resource-share-invitation`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/reject-resource-share-invitation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/reject-resource-share-invitation.html")).

You can use AWS RAM CLI commands to view shared items:

- Resources you have shared:

`aws ram list-resources --resource-owner SELF --resource-type
 backup:backup-vault --region us-east-1`

- Show the principal:

`aws ram get-resource-share-associations --association-type PRINCIPAL
 --region us-east-1`

- Resources shared by other accounts:

`aws ram list-resources --resource-owner OTHER-ACCOUNTS --resource-type
 backup:backup-vault --region us-east-1`

## Restore a backup from a logically air-gapped vault

You can restore a backup stored in a logically air-gapped vault from either the account
that owns the vault or from any account with which the vault is shared.

See [Restoring a backup](restoring-a-backup.md "restoring-a-backup.md") for information on how to restore a recovery point through the
AWS Backup console.

Once a backup has been shared from a logically air-gapped vault to your account, you
can use [`start-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html") to restore the backup.

A sample CLI input can include
the following command and parameters:

```
aws backup start-restore-job
--recovery-point-arn `arn:aws:backup:us-east-1:accountnumber:recovery-point:RecoveryPointID`
--metadata {\"availabilityzone\":\"us-east-1d\"}
--idempotency-token TokenNumber
--resource-type ResourceType
--iam-role arn:aws:iam::number:role/service-role/servicerole
--region us-east-1
```

## Delete a logically air-gapped vault

See [delete a vault](create-a-vault.md#delete-a-vault "create-a-vault.md#delete-a-vault"). Vaults cannot be deleted if they still
contain backups (recovery points). Ensure the vault is empty of backups before you initiate
a delete operation.

Deletion of a vault also deletes the key associated with the vault seven days after
the vault is deleted in accordance with key deletion policy.

The following sample CLI command [`delete-backup-vault`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-vault.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/delete-backup-vault.html") can be used to delete a vault.

```
aws backup delete-backup-vault
--region us-east-1
--backup-vault-name `testvaultname`
```

## Additional programmatic options for logically air-gapped

vaults

The CLI command [`list-backup-vaults`](API_ListBackupVaults.md "API_ListBackupVaults.md") can be modified to list all the vaults owned by and
present in the account:

```
aws backup list-backup-vaults
--region us-east-1
```

To list just the logically air-gapped vaults, add the parameter

```
--by-vault-type LOGICALLY_AIR_GAPPED_BACKUP_VAULT
```

Include the parameter `by-shared` to
filter the returned list of vaults to show only shared logically air-gapped vaults.
The response will include encryption key type information for each shared vault.

```
aws backup list-backup-vaults
--region us-east-1
--by-shared
```

Example response showing encryption key type information:

```
{
    "BackupVaultList": [
        {
            "BackupVaultName": "shared-logically air-gapped-vault",
            "BackupVaultArn": "arn:aws:backup:us-east-1:123456789012:backup-vault:shared-logically air-gapped-vault",
            "VaultType": "LOGICALLY_AIR_GAPPED_BACKUP_VAULT",
            "EncryptionKeyType": "AWS_OWNED_KMS_KEY",
            "CreationDate": "2024-07-25T16:05:23.554000-07:00",
            "Locked": true,
            "MinRetentionDays": 7,
            "MaxRetentionDays": 30
        }
    ]
}
```

## Understanding encryption key types for logically air-gapped vaults

Logically air-gapped vaults support different encryption key types, and this information
is visible through AWS Backup APIs and console. When vaults are shared through AWS RAM or MPA,
the encryption key type information is preserved and made visible to accounts with which
the vault is shared. This transparency helps you understand the encryption configuration
of vaults and make informed decisions about backup and restore operations.

### Encryption key type values

The `EncryptionKeyType` field can have the following values:

- `AWS_OWNED_KMS_KEY` - The vault is encrypted with an AWS-owned key.
  This is the default encryption method for logically air-gapped vaults when no customer-managed key is specified.
- `CUSTOMER_MANAGED_KMS_KEY` - The vault is encrypted with a
  customer-managed KMS key that you control. This option provides additional control over encryption keys and access policies.

###### Note

- AWS Backup recommends using AWS owned keys with logically air-gapped vaults. However, if your organization policy requires using a customer managed key,
  use keys from another account in a secondary organization dedicated to recovery as a best practice. You can reference the blog
  [Encrypt AWS Backup logically air-gapped vaults with customer-managed keys](https://aws.amazon.com/blogs/storage/encrypt-aws-backup-logically-air-gapped-vaults-with-customer-managed-keys/ "https://aws.amazon.com/blogs/storage/encrypt-aws-backup-logically-air-gapped-vaults-with-customer-managed-keys/") to gather more insights into setting up CMK based logically air-gapped vaults.
- You can only select an AWS KMS encryption key during vault creation.
  Once created, all backups contained in the vault will be encrypted with that key. You cannot change or migrate your vaults to use a different encryption key.

### Key policy for CMK encrypted logically air-gapped vault

creation

When creating a logically air-gapped vault with a customer managed key, you must apply the AWS-managed policy
`AWSBackupFullAccess` to your account role. This policy includes
`Allow` actions that enable AWS Backup to interact with AWS KMS for grant creation
on KMS keys during backup, copy, and storage operations. Additionally, you must ensure
your customer managed key (if used) policy includes specific required permissions.

- The CMK must be shared with the account where the logically air-gapped vault
  resides

```
{
    "Sid": "Allow use of the key to create a logically air-gapped vault",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::[account-id]:role/TheRoleToAccessAccount"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
    "Resource": "*",
   "Condition": {
        "StringLike": {
            "kms:ViaService": "backup.*.amazonaws.com"
        }
   }
}
```

**Key policy for copy/restore**

To prevent job failures, review your AWS KMS key policy to ensure it
includes all required permissions and doesn't contain any deny statements that could block
operations. The following conditions apply:

- For all copy scenarios, the CMKs must be shared with the source copy role

```
{
    "Sid": "Allow use of the key for copy",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::[source-account-id]:role/service-role/AWSBackupDefaultServiceRole"      //[Source copy role]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
   "Condition": {
         "StringLike": {
            "kms:ViaService": "backup.*.amazonaws.com"
         }
   }
},
{
    "Sid": "Allow AWS Backup to create grant on the key for copy",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::[source-account-id]:role/service-role/AWSBackupDefaultServiceRole" //[Source copy role]
    },
    "Action": [
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        },
        "StringLike": {
            "kms:ViaService": "backup.*.amazonaws.com"
        }
    }
}
```

- When copying from a CMK encrypted logically air-gapped vault to a backup vault, the CMK must
  also be shared with the destination account SLR

```
{
    "Sid": "Allow use of the key for copy from a CMK encrypted logically air-gapped vault to normal backup vault",
    "Effect": "Allow",
    "Principal": {
        "AWS": ["arn:aws:iam::[source-account-id]:role/service-role/AWSBackupDefaultServiceRole",      //[Source copy role]
                "arn:aws:iam::[destination-account-id]:role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup"], //[Destination SLR]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Sid": "Allow AWS Backup to create grant on the key for copy",
    "Effect": "Allow",
    "Principal": {
          "AWS": ["arn:aws:iam::[source-account-id]:role/service-role/AWSBackupDefaultServiceRole",      //[Source copy role]
                  "arn:aws:iam::[destination-account-id]:role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup"], //[Destination SLR]
    },
    "Action": [
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

- When copying or restoring from a recovery account using RAM/MPA shared logically air-gapped vault

```
{
    "Sid": "Allow use of the key for copy/restore from a recovery account",
    "Effect": "Allow",
    "Principal": {
        "AWS": ["arn:aws:iam::[recovery-account-id]:role/service-role/AWSBackupDefaultServiceRole", //[Recovery account copy/restore role]
                "arn:aws:iam::[destination-account-id]:role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup"] //[Destination SLR]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Sid": "Allow AWS Backup to create grant on the key for copy",
    "Effect": "Allow",
    "Principal": {
        "AWS": ["arn:aws:iam::[recovery-account-id]:role/service-role/AWSBackupDefaultServiceRole" //[Recovery account copy/restore role]
                "arn:aws:iam::[destination-account-id]:role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup"], //[Destination SLR]

    },
    "Action": [
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

**IAM Role**

When performing logically air-gapped vault copy operations, customers can utilize the
`AWSBackupDefaultServiceRole` which includes the AWS-managed policy
`AWSBackupServiceRolePolicyForBackup`. However, if customers prefer to
implement a least-privilege policy approach, their IAM policy must include a specific
requirement:

- The source account's copy role must have access permissions to both the source and
  destination CMKs.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
         {
            "Sid": "KMSPermissions",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": [
                "arn:aws:kms:*:[source-account-id]:key/*",  - Source logically air-gapped vault CMK -
                "arn:aws:kms:*:[destination-account-id]:key/*".  - Destination logically air-gapped vault CMK -
            ]
        },
        {
            "Sid": "KMSCreateGrantPermissions",
            "Effect": "Allow",
            "Action": "kms:CreateGrant",
            "Resource": [
                "arn:aws:kms:*:[source-account-id]:key/*",  - Source logically air-gapped vault CMK -
                "arn:aws:kms:*:[destination-account-id]:key/*".  - Destination logically air-gapped vault CMK -
            ]
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        },
    ]
}
```

Consequently, one of the most common customer errors occurs during copy when customers
fail to provide sufficient permissions on their CMKs and copy roles.

### Viewing encryption key types

You can view encryption key type information through both the AWS Backup console
and programmatically using the AWS CLI or SDKs.

**Console:** When viewing logically air-gapped vaults in the AWS Backup console,
the encryption key type is displayed in the vault details page under the security
information section.

**AWS CLI/API:** The encryption key type is returned in the response
of the following operations when querying logically air-gapped vaults:

- `list-backup-vaults` (including `--by-shared` for shared vaults)
- `describe-backup-vault`
- `describe-recovery-point`
- `list-recovery-points-by-backup-vault`
- `list-recovery-points-by-resource`

### Considerations for vault encryption

When working with logically air-gapped vaults and encryption key types, consider the following:

- **Key selection during creation:** You can optionally specify a customer-managed KMS key when creating a logically air-gapped vault. If not specified, an AWS-owned key will be used.
- **Shared vault visibility:** Accounts with which a vault is shared can view
  the encryption key type but cannot modify the encryption configuration.
- **Recovery point information:** The encryption key type is also available when viewing recovery points within logically air-gapped vaults.
- **Restore operations:** Understanding the encryption key type
  helps you plan restore operations and understand any potential access requirements.
- **Compliance:** The encryption key type information supports
  compliance reporting and audit requirements by providing transparency into the
  encryption methods used for backup data.

## Troubleshoot a logically air-gapped vault issue

If you encounter errors during your workflow, consult the following example errors and
suggested resolutions:

### `AccessDeniedException`

**Error:** `An error occured (AccessDeniedException) when calling 
 the *[command]* operation: Insufficient privileges to perform this action."`

**Possible cause:** The parameter `--backup-vault-account-id`
was not included when one of the following requests was run on a vault shared by RAM:

- `describe-backup-vault`
- `describe-recovery-point`
- `get-recovery-point-restore-metadata`
- `list-protected-resources-by-backup-vault`
- `list-recovery-points-by-backup-vault`

**Resolution:** Retry the command that returned the error, but include
the parameter `--backup-vault-account-id` that specifies the account that owns
the vault.

### `OperationNotPermittedException`

**Error:** `OperationNotPermittedException` is returned
after a `CreateResourceShare` call.

**Possible cause:** If you attempted to share a resource,
such as a logically air-gapped vault, with another organization, you may get
this exception. A vault can be shared with an account in another organization,
but it cannot be shared with the other organization itself.

**Resolution:** Retry the operation, but specify an
account as the value for `principals` instead of an organization
or OU.

### Encryption key type not displayed

**Issue:** The encryption key type is not visible when viewing
a logically air-gapped vault or its recovery points.

**Possible causes:**

- You are viewing an older vault that was created before encryption
  key type support was added
- You are using an older version of the AWS CLI or SDK
- The API response does not include the encryption key type field

**Resolution:**

- Update your AWS CLI to the latest version
- For older vaults, the encryption key type will be populated automatically
  and should appear in subsequent API calls
- Verify you are using the correct API operations that return encryption key type information
- For shared vaults, verify that the vault is properly shared through AWS Resource Access Manager

### "FAILED" VaultState with AccessDeniedException in CloudTrail logs

**Error in CloudTrail:** `"User: <assumed role> is not authorized to perform: kms:CreateGrant on this resource because the resource does not exist in this Region, no resource-based policies allow access, or a resource-based policy explicitly denies access"`

**Possible causes:**

- The vault was created using a customer managed key, but the assumed role does not have CreateGrant permission on the key policy required to use the key for vault creation

**Resolution:**

- Grant the permissions specified in the [Key policy for CMK encrypted logically air-gapped vault
  creation](#key-policy-lag-vault-creation "#key-policy-lag-vault-creation") section, then retry the vault creation workflow.
