# Set up for Amazon EBS

Complete the tasks in this section to get set up for working with Amazon EBS resources.

###### Tasks

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [(Optional) Create and use a customer managed key for Amazon EBS encryption](#create-kms-key "#create-kms-key")
- [(Optional) Enable block public access for Amazon EBS snapshots](#setup-bpa "#setup-bpa")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## (_Optional_) Create and use a customer managed key for Amazon EBS encryption

Amazon EBS encryption is an encryption solution that uses AWS KMS cryptographic keys to encrypt your
Amazon EBS volumes and Amazon EBS snapshots. Amazon EBS automatically creates a unique AWS managed KMS key
for Amazon EBS encryption in each Region. This KMS key has the alias `aws/ebs`. You can't
rotate the default KMS key or manage its permissions. For more flexibility and control over
the KMS key used for Amazon EBS encryption, you might consider creating and using a customer managed key.

###### To create and use a customer managed key for Amazon EBS encryption

1. [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk").
2. [Select the KMS key as the default KMS key for
   Amazon EBS encryption.](encryption-by-default.md "encryption-by-default.md")
3. [Give users permission to use the KMS key for
   Amazon EBS encryption](ebs-encryption-requirements.md#ebs-encryption-permissions "ebs-encryption-requirements.md#ebs-encryption-permissions").

## (_Optional_) Enable block public access for Amazon EBS snapshots

To prevent public sharing of your snapshots, you can enable block public access for snapshots.
After you enable block public access for snapshots in a Region, any attempt to publicly share
snapshots in that Region is automatically blocked. This can help you to improve the security of
your snapshots and to protect your snapshot data from unauthorized or unintended access.

For more information, see [Block public access for Amazon EBS snapshots](block-public-access-snapshots.md "block-public-access-snapshots.md").

Console

###### To enable block public access for snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**, and then in
   **Account attributes** (on the right-hand side), choose
   **Data protection and security**.
3. In the **Block public access for EBS snapshots** section, choose
   **Manage**.
4. Select **Block public access** and then choose one of the
   following options:

   - **Block all public access** — To block all public sharing of your
     snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
     were already publicly shared are treated as private and are no longer publicly available.
   - **Block new public sharing** — To block only new public sharing of
     your snapshots. Users in the account can't request new public sharing. However, snapshots that
     were already publicly shared, remain publicly available.

5. Choose **Update**.

AWS CLI

###### To enable block public access for snapshots

Use the [enable-snapshot-block-public-access](../../../cli/latest/reference/ec2/enable-snapshot-block-public-access.md "../../../cli/latest/reference/ec2/enable-snapshot-block-public-access.md")
command. For `--state` specify one of the following values:

- `block-all-sharing` — To block all public sharing of your
  snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
  were already publicly shared are treated as private and are no longer publicly available.
- `block-new-sharing` — To block only new public sharing of
  your snapshots. Users in the account can't request new public sharing. However, snapshots that
  were already publicly shared, remain publicly available.

```
aws ec2 enable-snapshot-block-public-access --state `block-new-sharing`
```

PowerShell

###### To enable block public access for snapshots

Use the [Enable-EC2SnapshotBlockPublicAccess](../../../powershell/latest/reference/items/Enable-EC2SnapshotBlockPublicAccess.md "../../../powershell/latest/reference/items/Enable-EC2SnapshotBlockPublicAccess.md") cmdlet. For `-State` specify one of the following values:

- `block-all-sharing` — To block all public sharing of your
  snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
  were already publicly shared are treated as private and are no longer publicly available.
- `block-new-sharing` — To block only new public sharing of
  your snapshots. Users in the account can't request new public sharing. However, snapshots that
  were already publicly shared, remain publicly available.

```
Enable-EC2SnapshotBlockPublicAccess -State `block-new-sharing`
```
