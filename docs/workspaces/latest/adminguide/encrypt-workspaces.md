# Encrypted WorkSpaces in WorkSpaces Personal

WorkSpaces is integrated with the AWS Key Management Service (AWS KMS). This enables you to encrypt storage
volumes of WorkSpaces using AWS KMS Key. When you launch a WorkSpace, you can encrypt the root
volume (for Microsoft Windows, the C drive; for Linux, /) and the user volume (for Windows,
the D drive; for Linux, /home). Doing so ensures that the data stored at rest, disk I/O to
the volume, and snapshots created from the volumes are all encrypted.

###### Note

- In addition to encrypting your WorkSpaces, you can also use FIPS endpoint encryption in
  certain AWS US Regions. For more information, see [Configure FedRAMP authorization or DoD SRG
  compliance for WorkSpaces Personal](fips-encryption.md "fips-encryption.md").
- BitLocker encryption is not supported for Amazon WorkSpaces.

###### Contents

- [Prerequisites](#encryption_prerequisites "#encryption_prerequisites")
- [Limits](#encryption_limits "#encryption_limits")
- [Overview of WorkSpaces encryption using
  AWS KMS](#kms-workspaces-overview "#kms-workspaces-overview")
- [WorkSpaces encryption context](#kms-workspaces-encryption-context "#kms-workspaces-encryption-context")
- [Grant WorkSpaces permission to use a KMS Key on
  your behalf](#kms-workspaces-permissions "#kms-workspaces-permissions")
- [Encrypt a WorkSpace](#encrypt_workspace "#encrypt_workspace")
- [View encrypted WorkSpaces](#maintain_encryption "#maintain_encryption")

## Prerequisites

You need an AWS KMS Key before you can begin the encryption process. This KMS Key can
be either the [AWS managed KMS
Key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") for Amazon WorkSpaces (**aws/workspaces**) or a symmetric
[customer managed KMS
Key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

- **AWS managed KMS Keys** – The first time
  that you launch an unencrypted WorkSpace from the WorkSpaces console in a Region,
  Amazon WorkSpaces automatically creates an AWS managed KMS Key (**aws/workspaces**) in your account. You can select this AWS managed
  KMS Key to encrypt the user and root volumes of your WorkSpace. For details, see
  [Overview of WorkSpaces encryption using
  AWS KMS](#kms-workspaces-overview "#kms-workspaces-overview").

You can view this AWS managed KMS Key, including its policies and grants, and
can track its use in AWS CloudTrail logs, but you cannot use or manage this KMS Key.
Amazon WorkSpaces creates and manages this KMS Key. Only Amazon WorkSpaces can use this KMS Key,
and WorkSpaces can use it only to encrypt WorkSpaces resources in your account.

AWS managed KMS Key, including the one that Amazon WorkSpaces supports, are rotated
every year. For details, see [Rotating AWS KMS Key](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS Key Management Service Developer Guide_.

- **Customer managed KMS Key** –
  Alternatively, you can select a symmetric customer managed KMS Key that you
  created using AWS KMS. You can view, use, and manage this KMS Key, including setting
  its policies. For more information about creating KMS Keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
  _AWS Key Management Service Developer Guide_. For more information about creating KMS
  Keys using the AWS KMS API, see [Working with Keys](../../../kms/latest/developerguide/programming-keys.md "../../../kms/latest/developerguide/programming-keys.md") in the _AWS Key Management Service Developer Guide_.

Customer managed KMS Keys are not automatically rotated unless you decide to
enable automatic key rotation. For details, see [Rotating AWS KMS Keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the
_AWS Key Management Service Developer Guide_.

###### Important

When you manually rotate KMS Keys, you must keep both the original KMS Key and the new KMS
Key enabled so that AWS KMS can decrypt the WorkSpaces that the original KMS Key encrypted.
If you don't want to keep the original KMS Key enabled, you must recreate your WorkSpaces
and encrypt them using the new KMS Key.

You must meet the following requirements to use an AWS KMS Key to encrypt your
WorkSpaces:

- **The KMS Key must be symmetric.** Amazon WorkSpaces does
  not support asymmetric KMS Keys. For information about distinguishing between
  symmetric and asymmetric KMS Keys, see [Identifying Symmetric and
  Asymmetric KMS Keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the _AWS Key Management Service Developer Guide_.
- **The KMS Key must be enabled.** To determine
  whether a KMS Key is enabled, see [Displaying KMS Key Details](../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details "../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details") in the
  _AWS Key Management Service Developer Guide_.
- **You must have the correct permissions and policies
  associated with the KMS Key.** For more information, see [Part 2: Grant WorkSpaces administrators
  additional permissions using an IAM policy](#kms-permissions-iam-policy "#kms-permissions-iam-policy").

## Limits

- You can't encrypt an existing WorkSpace. You must encrypt a WorkSpace when you
  launch it.
- Creating a custom image from an encrypted WorkSpace is not supported.
- Disabling encryption for an encrypted WorkSpace is not currently
  supported.
- WorkSpaces launched with root volume encryption enabled might take up to an hour to
  provision.
- To reboot or rebuild an encrypted WorkSpace, first make sure that the AWS KMS
  Key is enabled; otherwise, the WorkSpace becomes unusable. To determine whether a
  KMS Key is enabled, see [Displaying KMS Key Details](../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details "../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details") in the
  _AWS Key Management Service Developer Guide_.

## Overview of WorkSpaces encryption using

AWS KMS

When you create WorkSpaces with encrypted volumes, WorkSpaces uses Amazon Elastic Block Store (Amazon EBS) to create
and manage those volumes. Amazon EBS encrypts your volumes with a data key using the
industry-standard AES-256 algorithm. Both Amazon EBS and Amazon WorkSpaces use your KMS Key
to work with the encrypted volumes. For more information about EBS volume encryption,
see [Amazon EBS Encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md") in the
_Amazon EC2 User Guide_.

When you launch WorkSpaces with encrypted volumes, the end-to-end process works like
this:

1. You specify the KMS Key to use for encryption as well as the user and directory
   for the WorkSpace. This action creates a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") that allows WorkSpaces to
   use your KMS Key only for this WorkSpace—that is, only for the WorkSpace
   associated with the specified user and directory.
2. WorkSpaces creates an encrypted EBS volume for the WorkSpace and specifies the KMS
   Key to use as well as the volume's user and directory. This action creates a grant
   that allows Amazon EBS to use your KMS Key only for this WorkSpace and
   volume—that is, only for the WorkSpace associated with the specified user
   and directory, and only for the specified volume.
3. Amazon EBS requests a volume data key that is encrypted under your KMS Key and
   specifies the WorkSpace user's Active Directory security identifier (SID) and
   AWS Directory Service directory ID as well as the Amazon EBS volume ID as the [encryption context](#kms-workspaces-encryption-context "#kms-workspaces-encryption-context").
4. AWS KMS creates a new data key, encrypts it under your KMS Key, and then sends
   the encrypted data key to Amazon EBS.
5. WorkSpaces uses Amazon EBS to attach the encrypted volume to your WorkSpace. Amazon EBS sends
   the encrypted data key to AWS KMS with a [`Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") request and specifies the WorkSpace user's SID,
   the directory ID, and the volume ID, which is used as the encryption
   context.
6. AWS KMS uses your KMS Key to decrypt the data key, and then sends the plain text
   data key to Amazon EBS.
7. Amazon EBS uses the plain text data key to encrypt all data going to and from the
   encrypted volume. Amazon EBS keeps the plain text data key in memory for as long as the
   volume is attached to the WorkSpace.
8. Amazon EBS stores the encrypted data key (received at [Step 4](#WSP-KMS-creates-data-key "#WSP-KMS-creates-data-key")) with the volume metadata for future use
   in case you reboot or rebuild the WorkSpace.
9. When you use the AWS Management Console to remove a WorkSpace (or use the [`TerminateWorkspaces`](../devguide/API_TerminateWorkspaces.md "../devguide/API_TerminateWorkspaces.md") action in the WorkSpaces API), WorkSpaces and
   Amazon EBS retire the grants that allowed them to use your KMS Key for that
   WorkSpace.

## WorkSpaces encryption context

WorkSpaces doesn't use your KMS Key directly for cryptographic operations (such as [`Encrypt`](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md"), [`Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md"), [`GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md"),
etc.), which means WorkSpaces doesn't send requests to AWS KMS that include an [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context"). However, when Amazon EBS requests an encrypted data key for
the encrypted volumes of your WorkSpaces ([Step 3](#WSP-EBS-requests-encrypted-volume-data-key "#WSP-EBS-requests-encrypted-volume-data-key") in the [Overview of WorkSpaces encryption using
AWS KMS](#kms-workspaces-overview "#kms-workspaces-overview")) and when
it requests a plain text copy of that data key ([Step 5](#WSP-uses-EBS-to-attach-encrypted-volume "#WSP-uses-EBS-to-attach-encrypted-volume")), it includes encryption context
in the request.

The encryption context provides [additional authenticated
data](../../../crypto/latest/userguide/cryptography-concepts.md#term-aad "../../../crypto/latest/userguide/cryptography-concepts.md#term-aad") (AAD) that AWS KMS uses to ensure data integrity. The encryption context
is also written to your AWS CloudTrail log files, which can help you understand why a given
KMS Key was used. Amazon EBS uses the following for the encryption context:

- The security identifier (SID) of the Active Directory user that is associated
  with the WorkSpace
- The directory ID of the AWS Directory Service directory that is associated with the
  WorkSpace
- The Amazon EBS volume ID of the encrypted volume

The following example shows a JSON representation of the encryption context that
Amazon EBS uses:

```
{
  "aws:workspaces:sid-directoryid": "[`S-1-5-21-277731876-1789304096-451871588-1107`]@[`d-1234abcd01`]",
  "aws:ebs:id": "`vol-1234abcd`"
}
```

## Grant WorkSpaces permission to use a KMS Key on

your behalf

You can protect your WorkSpace data under the AWS managed KMS Key for WorkSpaces
(**aws/workspaces**) or a customer managed KMS Key. If you use a
customer managed KMS Key, you need to grant WorkSpaces permission to use the KMS Key on
behalf of the WorkSpaces administrators in your account. The AWS managed KMS Key for WorkSpaces
has the required permissions by default.

To prepare your customer managed KMS Key for use with WorkSpaces, use the following
procedure.

1. [Add your WorkSpaces administrators to the
   list of key users in the KMS Key's key policy](#kms-permissions-key-users "#kms-permissions-key-users")
2. [Give your WorkSpaces administrators
   additional permissions with an IAM policy](#kms-permissions-iam-policy "#kms-permissions-iam-policy")

Your WorkSpaces administrators also need permission to use WorkSpaces. For more information
about these permissions, go to [Identity and access management for WorkSpaces](workspaces-access-control.md "workspaces-access-control.md").

### Part 1: Add WorkSpaces administrators to as

key users

To give WorkSpaces administrators the permissions that they require, you can use the
AWS Management Console or the AWS KMS API.

#### To add WorkSpaces administrators as

key users for a KMS Key (console)

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**.
4. Choose the key ID or alias of your preferred customer managed KMS
   Key.
5. Choose the **Key policy** tab. Under **Key
   users**, choose **Add**.
6. In the list of IAM users and roles, select the users and roles that
   correspond to your WorkSpaces administrators, and then choose
   **Add**.

#### To add WorkSpaces administrators as key

users for a KMS Key (API)

1. Use the [GetKeyPolicy](../../../kms/latest/APIReference/API_GetKeyPolicy.md "../../../kms/latest/APIReference/API_GetKeyPolicy.md") operation to get the existing key policy, and then
   save the policy document to a file.
2. Open the policy document in your preferred text editor. Add the IAM users
   and roles that correspond to your WorkSpaces administrators to the policy
   statements that [give permission to key users](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users"). Then save the file.
3. Use the [PutKeyPolicy](../../../kms/latest/APIReference/API_PutKeyPolicy.md "../../../kms/latest/APIReference/API_PutKeyPolicy.md") operation to apply the key policy to the KMS
   Key.

### Part 2: Grant WorkSpaces administrators

additional permissions using an IAM policy

If you select a customer managed KMS Key to use for encryption, you must establish
IAM policies that allow Amazon WorkSpaces to use the KMS Key on behalf of an IAM user in your
account who launches encrypted WorkSpaces. That user also needs permission to use
Amazon WorkSpaces. For more information about creating and editing IAM user policies, see
[Managing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_ and
[Identity and access management for WorkSpaces](workspaces-access-control.md "workspaces-access-control.md").

WorkSpaces encryption requires limited access to the KMS Key. The following is a sample
key policy that you can use. This policy separates the principals who can manage the
AWS KMS Key from those who can use it. Before you use this sample key policy, replace
the example account ID and IAM user name with actual values from your
account.

The first statement matches the default AWS KMS key policy. It gives your account
permission to use IAM policies to control access to the KMS Key. The second and
third statements define which AWS principals can manage and use the key,
respectively. The fourth statement enables AWS services that are integrated with
AWS KMS to use the key on behalf of the specified principal. This statement enables
AWS services to create and manage grants. The statement uses a condition element
that limits grants on the KMS Key to those made by AWS services on behalf of users
in your account.

###### Note

If your WorkSpaces administrators use the AWS Management Console to create WorkSpaces with encrypted
volumes, the administrators need permission to list aliases and list keys (the
`"kms:ListAliases"` and `"kms:ListKeys"` permissions). If
your WorkSpaces administrators use only the Amazon WorkSpaces API (not the console), you can
omit the `"kms:ListAliases"` and `"kms:ListKeys"`
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`123456789012`:root"},
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`123456789012`:user/`Alice`"},
 "Action": [
 "kms:Create*",
 "kms:Describe*",
 "kms:Enable*",
 "kms:List*",
 "kms:Put*",
 "kms:Update*",
 "kms:Revoke*",
 "kms:Disable*",
 "kms:Get*",
 "kms:Delete*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`123456789012`:user/`Alice`"},
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncryptFrom",
 "kms:ReEncryptTo",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`123456789012`:user/`Alice`"},
 "Action": [
 "kms:CreateGrant",
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": "*",
 "Condition": {"Bool": {"kms:GrantIsForAWSResource": "true"}}
 }
 ]
}`

```

The IAM policy for a user or role that is encrypting a WorkSpace must include
usage permissions on the customer managed KMS Key, as well as access to WorkSpaces. To
give an IAM user or role WorkSpaces permissions, you can attach the following sample
policy to the IAM user or role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ds:*",
 "ds:DescribeDirectories",
 "workspaces:*",
 "workspaces:DescribeWorkspaceBundles",
 "workspaces:CreateWorkspaces",
 "workspaces:DescribeWorkspaceBundles",
 "workspaces:DescribeWorkspaceDirectories",
 "workspaces:DescribeWorkspaces",
 "workspaces:RebootWorkspaces",
 "workspaces:RebuildWorkspaces"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following IAM policy is required by the user for using AWS KMS. It gives the
user read-only access to the KMS Key along with the ability to create grants.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:Describe*",
 "kms:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you want to specify the KMS Key in your policy, use an IAM policy similar to
the following. Replace the example KMS Key ARN with a valid one.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:CreateGrant",
 "Resource": "`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases",
 "kms:ListKeys"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Encrypt a WorkSpace

###### To encrypt a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Launch WorkSpaces** and complete the first three
   steps.
3. For the **WorkSpaces Configuration** step, do the following:
   1. Select the volumes to encrypt: **Root Volume**,
      **User Volume**, or both volumes.
   2. For **Encryption Key**, select an AWS KMS Key, either the
      AWS managed KMS Key created by Amazon WorkSpaces or a KMS Key that you created.
      The KMS Key that you select must be symmetric. Amazon WorkSpaces does not support
      asymmetric KMS Keys.
   3. Choose **Next Step**.

4. Choose **Launch WorkSpaces**.

## View encrypted WorkSpaces

To see which WorkSpaces and volumes have been encrypted from the WorkSpaces console, choose
**WorkSpaces** from the navigation bar on the left. The **Volume
Encryption** column shows whether each WorkSpace has encryption enabled or
disabled. To see which specific volumes have been encrypted, expand the WorkSpace entry
to see the **Encrypted Volumes** field.
