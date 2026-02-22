# Creating backup copies across

AWS accounts

Using AWS Backup, you can back up to multiple AWS accounts on demand or automatically as
part of a scheduled backup plan. Use a cross-account backup if you want to securely copy
your backups to one or more AWS accounts in your organization for operational or security
reasons. If your original backup is inadvertently deleted, you can copy the backup from its
destination account to its source account, and then start the restore. Before you can do
this, you must have two accounts that belong to the same organization in the AWS Organizations
service. For more information, see [Tutorial: Creating and
configuring an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") in the _Organizations User Guide_.

In your destination account, you must create a backup vault. Then, you assign a customer
managed key to encrypt backups in the destination account, and a resource-based access
policy to allow AWS Backup to access the resources you would like to copy. In the source account,
if your resources are encrypted with a customer managed key, you must share this customer
managed key with the destination account. You can then create a backup plan and choose a
destination account that is part of your organizational unit in AWS Organizations.

When you copy a backup to cross-account for the first time, AWS Backup copies the backup in
full. In general, if a service supports incremental backups, subsequent copies of that
backup in the same account are incremental. AWS Backup re-encrypts your copy using the customer
managed key of your destination vault.

###### Requirements

- Before you manage resources across multiple AWS accounts in AWS Backup, your accounts
  must belong to the same organization in the AWS Organizations service.
- Most resources supported by AWS Backup support cross-account backup. For specifics, see
  [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").
- Most AWS Regions support cross-account backup. For specifics, see [Feature availability by AWS Region](backup-feature-availability.md#features-by-region "backup-feature-availability.md#features-by-region").
- AWS Backup does not support cross-account copies for storage in cold tiers.

## Setting up cross-account backup

###### What do you need to create cross-account backups?

- **A source account**

The source account is the account where your production AWS resources and
primary backups reside.

The source account user initiates the cross-account backup operation. The source
account user or role must have appropriate API permissions to initiate the operation.
Appropriate permissions might be the AWS managed policy
`AWSBackupFullAccess`, which enables full access to AWS Backup operations, or
a customer managed policy that allows actions such as
`ec2:ModifySnapshotAttribute`. For more information about policy types,
see [AWS Backup Managed
Policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

- **A destination account**

The destination account is the account where you would like to keep a copy of your
backup. You can choose more than one destination account. The destination account must
be in the same organization as the source account in AWS Organizations.

You must “Allow” the access policy `backup:CopyIntoBackupVault` for
your destination backup vault. The absence of this policy will deny attempts to copy
into the destination account.

- **A management account in AWS Organizations**

The management account is the primary account in your organization, as defined by
AWS Organizations, that you use to manage cross-account backup across your AWS accounts. To
use cross-account backup, you also must enable service trust. After enabling service
trust, you can use any account in the organization as a destination account. From your
destination account, you can choose which vaults to use for cross-account
backup.

- **Enable cross-account backup in the AWS Backup
  console**

For information about security, see [Security considerations for cross-account
backup](#security-considerations-cab "#security-considerations-cab").

To use cross-account backup, you must enable the cross-account backup feature. Then,
you must "Allow" the access policy `backup:CopyIntoBackupVault` into your
destination backup vault.

Amazon EC2 offers [EC2 Allowed AMIs](../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md "../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md"). If this
setting is enabled in your account, add your source account ID to your allowlist.
Otherwise, the copy operation will fail with an error message, such as "Source AMI not
found in Region".

###### Enable cross-account backup

1. Log in using your AWS Organizations management account credentials. Cross-account backup
   can only be enabled or disabled using these credentials.
2. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
3. In **My account**, choose **Settings**.
4. For **Cross-account backup**, choose
   **Enable**.
5. In **Backup vaults**, choose your destination vault.

For cross-account copy, the source vault and the destination vault are in
different accounts. Switch to the account which owns the destination account, as
necessary. 6. In the **Access policy** section, "Allow"
`backup:CopyIntoBackupVault`. For an example, choose **Add
permissions** and then **Allow access to a Backup vault from
organization**. Any cross-account action other than
`backup:CopyIntoBackupVault` will be rejected. 7. Now, any account in your organization can share the contents of their backup
vault with any other account in your organization. For more information, see [Configuring backup vault access for cross-account copies](#share-vault-cab "#share-vault-cab"). To limit which accounts
can receive the contents of other accounts' backup vaults, see [Configuring your account as a
destination account](#designate-destination-accounts-cab "#designate-destination-accounts-cab").

## Scheduling cross-account backup

You can use a scheduled backup plan to copy backups across AWS accounts.

###### To copy a backup using a scheduled backup

plan

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In **My account**, choose **Backup plans**, and
   then choose **Create Backup plan**.
3. On the **Create Backup plan** page, choose **Build a new
   plan**.
4. For **Backup plan name**, enter a name for your backup
   plan.
5. In the **Backup rule configuration** section, add a backup rule
   that defines a backup schedule, backup window, and lifecycle rules. You can add more
   backup rules later.

For **Rule name**, enter a name for your rule. 6. In the **Schedule** section under **Frequency**,
choose how often you want the backup to be taken. 7. For **Backup window**, choose **Use backup window
defaults** (recommended). You can customize the backup window. 8. For **Backup vault**, choose a vault from the list. Recovery
points for this backup will be saved in this vault. You can create a new backup
vault. 9. In the **Generate copy - optional** section, enter the following
values:

**Destination Region**

Choose the destination AWS Region for your backup copy. Your backup will
be copied to this Region. You can add a new copy rule per copy to a new
destination.

**Copy to another account's vault**

Toggle to choose this option. The option turns blue when selected. The
**External vault ARN** option will appear.

**External vault ARN**

Enter the Amazon Resource Name (ARN) of the destination account. The ARN is
a string that contains the account ID and its AWS Region. AWS Backup will copy the
backup to the destination account's vault. The **Destination
region** list automatically updates to the Region in the external
vault ARN.

For **Allow Backup vault access**, choose
**Allow**. Then choose **Allow** in the
wizard that opens.

AWS Backup needs permissions to access the external account to copy backup to the
specified value. The wizard shows the following example policy that provides
this access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccountCopyIntoBackupVault",
 "Effect": "Allow",
 "Action": "backup:CopyIntoBackupVault",
 "Resource": "*",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 }
 }
 ]
}`

```

**Transition to cold storage**

Choose when to transition the backup copy to cold storage and when to expire
(delete) the copy. Backups transitioned to cold storage must be stored in cold
storage for a minimum of 90 days. This value cannot be changed after a copy has
transitioned to cold storage.

To see the list of resources that you can transition to cold storage, see
the "Lifecycle to cold storage" section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table.
The cold storage expression is ignored for other resources.

**Expire** specifies the number of days after creation that
the copy is deleted. This value must be greater than 90 days beyond the
**Transition to cold storage** value.

###### Note

When backups expire and are marked for deletion as part of your lifecycle
policy, AWS Backup deletes the backups at a randomly chosen point over the
following 8 hours. This window helps ensure consistent performance. 10. Choose **Tags added to recovery points** to add tags to your
recovery points. 11. For **Advanced backup settings**, choose **Windows
VSS** to enable application-aware snapshots for the selected third-party
software running on EC2. 12. Choose **Create plan**.

## Performing on-demand cross-account backup

You can copy a backup to a different AWS account on demand.

###### To copy a backup on-demand

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. For **My account**, choose **Backup vault** to
   see all your backup vaults listed. You can filter by the backup vault name or
   tag.
3. Choose the **Recovery point ID** of the backup you want to
   copy.
4. Choose **Copy**.
5. Expand **Backup details** to see information about the recovery
   point you are copying.
6. In the **Copy configuration** section, choose an option from the
   **Destination region** list.
7. Choose **Copy to another account's vault**. The option turns blue
   when selected.
8. Enter the Amazon Resource Name (ARN) of the destination account. The ARN is a
   string that contains the account ID and its AWS Region. AWS Backup will copy the backup
   to the destination account's vault. The **Destination region** list
   automatically updates to the Region in the external vault ARN.
9. For **Allow Backup vault access**, choose
   **Allow**. Then choose **Allow** in the wizard
   that opens.

To create the copy, AWS Backup needs permissions to access the source account. The
wizard shows an example policy that provides this access. This policy is shown
following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccountCopyIntoBackupVault",
 "Effect": "Allow",
 "Action": "backup:CopyIntoBackupVault",
 "Resource": "*",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 }
 }
 ]
}`

```

10. For **Transition to cold storage**, choose when to transition the
    backup copy to cold storage and when to expire (delete) the copy. Backups transitioned
    to cold storage must be stored in cold storage for a minimum of 90 days. This value
    cannot be changed after a copy has transitioned to cold storage.

To see the list of resources that you can transition to cold storage, see the
"Lifecycle to cold storage" section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table. The cold storage expression is ignored
for other resources.

**Expire** specifies the number of days after creation that the
copy is deleted. This value must be greater than 90 days beyond the
**Transition to cold storage** value. 11. For **IAM role**, specify the IAM role (such as the default role)
that has the permissions to make your backup available for copying. The act of copying
is performed by your destination account's service linked role. 12. Choose **Copy**. Depending on the size of the resource you are
copying, this process could take several hours to complete. When the copy job
completes, you will see the copy in the **Copy jobs** tab in the
**Jobs** menu.

## Encryption keys and cross-account copies

See [Encryption for a backup copy to a
different account or AWS Region](encryption.md#copy-encryption "encryption.md#copy-encryption") for details on how encryption works for copy
job.

For additional help troubleshooting cross-account copy failures, please see the [AWS
Knowledge Center](https://repost.aws/knowledge-center/backup-troubleshoot-cross-account-copy "https://repost.aws/knowledge-center/backup-troubleshoot-cross-account-copy").

## Restoring a backup from one AWS account to another

AWS Backup does not support recovering resources from one AWS account to another.
However, you can copy a backup from one account to a different account and then restore it
in that account. For example, you can't restore a backup from account A to account B, but
you can copy a backup from account A to account B, and then restore it in account
B.

Restoring a backup from one account to another is a two-step process.

###### To restore a backup from one account to another

1. Copy the backup from the source AWS account to the account you want to restore
   to. For instructions, see [Setting
   up cross-account backup](create-cross-account-backup.md#prereq-cab "create-cross-account-backup.md#prereq-cab").
2. Use the appropriate instructions for your resource to restore the backup.

## Configuring backup vault access for cross-account copies

AWS Backup allows you to configure your backup vault to grant access to other AWS accounts, allowing them to copy recovery points to your vault for cross-account backup. This access configuration uses resource-based policies to permit specific accounts to perform backup operations.

###### Note

This is different from AWS Backup vault sharing for Logically Air Gapped (LAG) vaults, which uses AWS Resource Access Manager (RAM) to share vault resources directly.

You can grant vault access to one or multiple accounts, or your entire organization in AWS Organizations. You can configure a destination backup vault with access for a source AWS Account, user, or IAM role.

###### To configure vault access for a destination Backup vault

1. Choose **AWS Backup**, and then choose **Backup
   vaults**.
2. Choose the name of the backup vault that you want to configure access for.
3. In the **Access policy** pane, choose the **Add
   permissions** dropdown.
4. Choose **Allow account level access to a Backup vault**. Or, you
   can choose to allow organization-level or role-level access.
5. Enter the **AccountID** of the account you'd like to grant access to
   this destination backup vault.
6. Choose **Save policy**.

You can use IAM policies to configure vault access.

###### Configure destination backup vault access for an

AWS account or IAM role

The following policy configures vault access for account number
`4444555566666` and the IAM role `SomeRole` in account number
`111122223333`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":[
 "arn:aws:iam::444455556666:root",
 "arn:aws:iam::111122223333:role/SomeRole"
 ]
 },
 "Action":"backup:CopyIntoBackupVault",
 "Resource":"*"
 }
 ]
}`

```

###### Share a destination backup vault an

organizational unit in AWS Organizations

The following policy shares a backup vault with organizational units using their
`PrincipalOrgPaths`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":"*",
 "Action":"backup:CopyIntoBackupVault",
 "Resource":"*",
 "Condition":{
 "ForAnyValue:StringLike":{
 "aws:PrincipalOrgPaths":[
 "o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-def0-awsbbbbb/",
 "o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-def0-awsbbbbb/ou-jkl0-awsddddd/*"
 ]
 }
 }
 }
 ]
}`

```

###### Share a destination backup vault

with an organization in AWS Organizations

The following policy shares a backup vault with the organization with
`PrincipalOrgID` "o-a1b2c3d4e5".

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":"*",
 "Action":"backup:CopyIntoBackupVault",
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "aws:PrincipalOrgID":[
 "o-a1b2c3d4e5"
 ]
 }
 }
 }
 ]
}`

```

## Configuring your account as a

destination account

When you first enable cross-account backups using your AWS Organizations management account, any
user of a member account can configure their account to be a destination account. We
recommend setting one or more of the following service control policies (SCPs) in AWS Organizations
to limit your destination accounts. To learn more about attaching service control policies
to AWS Organizations nodes, see [Attaching and
detaching service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_attach.md").

###### Limit destination accounts using

tags

When attached to an AWS Organizations root, OU, or individual account, this policy limits
copies destinations from that root, OU, or account to only those accounts with backup
vaults you’ve tagged `DestinationBackupVault`. The permission
`"backup:CopyIntoBackupVault"` controls how a backup vault behaves and, in
this case, which destination backup vaults are valid. Use this policy, along with the
corresponding tag applied to approved destination vaults, to control the destinations of
cross-account copies to only approved accounts and backup vaults.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Deny",
 "Action":"backup:CopyIntoBackupVault",
 "Resource":"*",
 "Condition":{
 "Null":{
 "aws:ResourceTag/DestinationBackupVault":"true"
 }
 }
 }
 ]
}`

```

###### Limit destination accounts using

account numbers and vault names

When attached to an AWS Organizations root, OU, or individual account, this policy limits
copies originating from that root, OU, or account to only two destination accounts. The
permission `"backup:CopyFromBackupVault"` controls how a recovery point in
the backup vault behaves, and, in this case, the destinations where you can copy that
recovery point to. The source vault will only permit copies to the first destination
account (112233445566) if one or more destination backup vault names begin with
`cab-`. The source vault will only permit copies to the second destination
account (123456789012) if the destination is the single backup vault named
`fort-knox`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCopyFromBackupVault",
 "Effect": "Deny",
 "Action": "backup:CopyFromBackupVault",
 "Resource": "arn:aws:ec2:*:*:snapshot/*",
 "Condition": {
 "ForAllValues:ArnNotLike": {
 "backup:CopyTargets": [
 "arn:aws:backup:*:112233445566:backup-vault:cab-*",
 "arn:aws:backup:us-east-1:123456789012:backup-vault:fort-knox"
 ]
 }
 }
 }
 ]
}`

```

###### Limit destination

accounts using organizational units in AWS Organizations

When attached to an AWS Organizations root or OU that contains your source account, or when
attached to your source account, the following policy limits the destination accounts to
those accounts within the two specified OUs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Deny",
 "Action":"backup:CopyFromBackupVault",
 "Resource":"*",
 "Condition":{
 "ForAllValues:StringNotLike":{
 "backup:CopyTargetOrgPaths":[
 "o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-def0-awsbbbbb/",
 "o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-def0-awsbbbbb/ou-jkl0-awsddddd/*"
 ]
 }
 }
 }
 ]
}`

```

## Security considerations for cross-account

backup

Be aware of the following when using performing cross-account backups in AWS Backup:

- The destination vault cannot be the default vault. This is because the default
  vault is encrypted with a key that cannot be shared with other accounts.
- Cross-account backups might still run for up to 15 minutes after you disable
  cross-account backup. This is due to eventual consistency, and might result in some
  cross-account jobs starting or completing even after you disable cross-account
  backup.
- If the destination account leaves the organization at a later date, that account
  will retain the backups. To avoid potential data leakage, place a deny permission on
  the `organizations:LeaveOrganization` permission in a service control
  policy (SCP) attached to the destination account. For detailed information about SCPs,
  see [Removing a
  member account from your organization](../../../organizations/latest/userguide/orgs_manage_accounts_remove.md "../../../organizations/latest/userguide/orgs_manage_accounts_remove.md") in the _Organizations
  User Guide_.
- If you delete a copy job role during a cross-account copy, AWS Backup can't unshare
  snapshots from the source account when the copy job completes. In this case, the
  backup job finishes, but the copy job status shows as **`Failed to unshare
snapshot`**.
