# Sharing a DB Cluster Snapshot

Using Neptune, you can share a manual DB cluster snapshot in the following ways:

- Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables
  authorized AWS accounts to copy the snapshot.
- Sharing a manual DB cluster snapshot, whether encrypted or unencrypted, enables
  authorized AWS accounts to directly restore a DB cluster from the snapshot instead of taking
  a copy of it and restoring from that.

###### Note

To share an automated DB cluster snapshot, create a manual DB cluster snapshot by copying
the automated snapshot, and then share that copy.

For more information about restoring a DB cluster from a DB cluster snapshot, see [How to restore from a snapshot](backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring "backup-restore-restore-snapshot.md#backup-restore-restore-snapshot-restoring").

You can share a manual snapshot with up to 20 other AWS accounts. You can also share an
unencrypted manual snapshot as public, which makes the snapshot available to all AWS accounts.
Take care when sharing a snapshot as public so that none of your private information is included
in any of your public snapshots.

###### Note

When you restore a DB cluster from a shared snapshot using the AWS Command Line Interface (AWS CLI) or
Neptune API, you must specify the Amazon Resource Name (ARN) of the shared snapshot as the
snapshot identifier.

###### Topics

- [Sharing an Encrypted DB Cluster Snapshot](#backup-restore-share-snapshot-encrypted "#backup-restore-share-snapshot-encrypted")
- [Sharing a DB Cluster Snapshot](#backup-restore-share-snapshot-sharing "#backup-restore-share-snapshot-sharing")

## Sharing an Encrypted DB Cluster Snapshot

You can share DB cluster snapshots that have been encrypted "at rest" using the AES-256
encryption algorithm. For more information, see [Encrypting data at rest in your Amazon Neptune database](encrypt.md "encrypt.md"). To do this, you must take the following steps:

1. Share the AWS Key Management Service (AWS KMS) encryption key that was used to encrypt the snapshot with
   any accounts that you want to be able to access the snapshot.

You can share AWS KMS encryption keys with another AWS account by adding the other
account to the KMS key policy. For details on updating a key policy, see [Key Policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS KMS Developer
Guide_. For an example of creating a key policy, see [Creating
an IAM Policy to Enable Copying of the Encrypted Snapshot](#backup-restore-share-snapshot-encrypted-key-iam "#backup-restore-share-snapshot-encrypted-key-iam") later in this
topic. 2. Use the AWS Management Console, AWS CLI, or Neptune API to share the encrypted snapshot with the
other accounts.

These restrictions apply to sharing encrypted snapshots:

- You cannot share encrypted snapshots as public.
- You cannot share a snapshot that has been encrypted using the default
  AWS KMS encryption key of the AWS account that shared the snapshot.

### Allowing Access

to an AWS KMS Encryption Key

For another AWS account to copy an encrypted DB cluster snapshot shared from your
account, the account that you share your snapshot with must have access to the KMS key that
encrypted the snapshot. To allow another AWS account access to an AWS KMS key, update the key
policy for the KMS key with the ARN of the AWS account that you are sharing to as a
`Principal` in the KMS key policy. Then allow the `kms:CreateGrant`
action. See [Allowing
users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the _AWS Key Management Service Developer Guide_
for general instructions.

After you have given an AWS account access to your KMS encryption key, to copy your
encrypted snapshot, that AWS account must create an IAM user if it doesn’t
already have one. KMS security restrictions don't permit use of a root AWS account
identity for this. The AWS account must also attach an IAM policy to that
IAM user that allows the IAM user to copy an encrypted DB cluster snapshot using
your KMS key.

In the following key policy example, user `111122223333` is the owner of the
KMS encryption key, and user `444455556666` is the account that the key is being
shared with. This updated key policy gives the AWS account access to the KMS key by
including the ARN for the root AWS account identity for user `444455556666` as a
`Principal` for the policy, and by allowing the `kms:CreateGrant`
action.

JSON

```
`{
 "Id": "key-policy-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUseOfTheKey",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111122223333:user/KeyUser",
 "arn:aws:iam::444455556666:root"
 ]
 },
 "Action": [
 "kms:CreateGrant",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAttachmentOfPersistentResources",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111122223333:user/KeyUser",
 "arn:aws:iam::444455556666:root"
 ]
 },
 "Action": [
 "kms:CreateGrant",
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "kms:GrantIsForAWSResource": true
 }
 }
 }
 ]
}`

```

#### Creating

an IAM Policy to Enable Copying of the Encrypted Snapshot

After the external AWS account has access to your KMS key, the owner of that account
can create a policy that allows an IAM user created for the account to copy an encrypted
snapshot encrypted with that KMS key.

The following example shows a policy that can be attached to an IAM user for AWS
account `444455556666`. It enables the IAM user to copy a shared snapshot from
AWS account `111122223333` that has been encrypted with the KMS key
`c989c1dd-a3f2-4a5d-8d96-e793d082ab26` in the `us-west-2`
Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUseOfTheKey",
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:RetireGrant"
 ],
 "Resource": ["arn:aws:kms:us-west-2:111122223333:key/c989c1dd-a3f2-4a5d-8d96-e793d082ab26"]
 },
 {
 "Sid": "AllowAttachmentOfPersistentResources",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": ["arn:aws:kms:us-west-2:111122223333:key/c989c1dd-a3f2-4a5d-8d96-e793d082ab26"],
 "Condition": {
 "Bool": {
 "kms:GrantIsForAWSResource": true
 }
 }
 }
 ]
}`

```

For details on updating a key policy, see [Key Policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

## Sharing a DB Cluster Snapshot

You can share a DB cluster snapshot using the AWS Management Console, the AWS CLI, or the Neptune
API.

### Using the Console to Share a

DB Cluster Snapshot

Using the Neptune console, you can share a manual DB cluster snapshot with up to 20
AWS accounts. You can also stop sharing a manual snapshot with one or more accounts.

###### To share a manual DB cluster snapshot

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Snapshots**.
3. Choose the manual snapshot that you want to share.
4. Choose **Actions**, **Share Snapshot**.
5. Choose one of the following options for **DB snapshot
   visibility**.
   - If the source is unencrypted, choose **Public** to permit all
     AWS accounts to restore a DB cluster from your manual DB cluster snapshot. Or choose
     **Private** to permit only AWS accounts that you specify to
     restore a DB cluster from your manual DB cluster snapshot.

   ###### Warning

   If you set **DB snapshot visibility** to
   **Public**, all AWS accounts can restore a DB cluster from your
   manual DB cluster snapshot and have access to your data. Do not share any manual
   DB cluster snapshots that contain private information as
   **Public**.
   - If the source is encrypted, **DB snapshot visibility** is set
     as **Private** because encrypted snapshots can't be shared as
     public.

6. For **AWS Account ID**, enter the AWS account identifier for an
   account that you want to permit to restore a DB cluster from your manual snapshot. Then
   choose **Add**. Repeat to include additional AWS account identifiers,
   up to 20 AWS accounts.

If you make an error when adding an AWS account identifier to the list of
permitted accounts, you can delete it from the list by choosing
**Delete** at the right of the incorrect AWS account
identifier. 7. After you add identifiers for all of the AWS accounts that you want to permit to restore the
manual snapshot, choose **Save**.

###### To stop sharing a manual DB cluster snapshot with an AWS account

1. Open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Snapshots**.
3. Choose the manual snapshot that you want to stop sharing.
4. Choose **Actions**, and then choose **Share
   Snapshot**.
5. To remove permission for an AWS account, choose **Delete** for
   the AWS account identifier for that account from the list of authorized
   accounts.
6. Choose **Save**.
