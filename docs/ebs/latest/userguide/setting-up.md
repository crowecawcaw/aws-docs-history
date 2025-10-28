# Set up for Amazon EBS

Complete the tasks in this section to get set up for working with Amazon EBS resources.

###### Tasks

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [(Optional) Create and use a customer managed key for
  Amazon EBS encryption](#create-kms-key "#create-kms-key")
- [(Optional) Enable block public access for Amazon EBS
  snapshots](#setup-bpa "#setup-bpa")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## (_Optional_) Create and use a customer managed key for

Amazon EBS encryption

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

## (_Optional_) Enable block public access for Amazon EBS

snapshots

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
