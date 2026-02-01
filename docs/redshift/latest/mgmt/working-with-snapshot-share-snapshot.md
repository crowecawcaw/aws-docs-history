Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing a snapshot

You can share an existing manual snapshot with other AWS customer accounts by
authorizing access to the snapshot. You can authorize up to 20 for each snapshot and 100
for each AWS Key Management Service (AWS KMS) key. That is, if you have 10 snapshots that are encrypted with a
single KMS key, then you can authorize 10 AWS accounts to restore each snapshot, or other
combinations that add up to 100 accounts and do not exceed 20 accounts for each snapshot. A
person logged in as a user in one of the authorized accounts can then describe the snapshot
or restore it to create a new Amazon Redshift cluster under their account. For example, if you use
separate AWS customer accounts for production and test, a user can log on using the
production account and share a snapshot with users in the test account. Someone logged on
as a test account user can then restore the snapshot to create a new cluster that is owned
by the test account for testing or diagnostic work.

A manual snapshot is permanently owned by the AWS customer account under which it was
created. Only users in the account owning the snapshot can authorize other accounts to
access the snapshot, or to revoke authorizations. Users in the authorized accounts can only
describe or restore any snapshot that has been shared with them; they cannot copy or delete
snapshots that have been shared with them. An authorization remains in effect until the
snapshot owner revokes it. If an authorization is revoked, the previously authorized user
loses visibility of the snapshot and cannot launch any new actions referencing the
snapshot. If the account is in the process of restoring the snapshot when access is
revoked, the restore runs to completion. You cannot delete a snapshot while it has active
authorizations; you must first revoke all of the authorizations.

AWS customer accounts are always authorized to access snapshots owned by the account.
Attempts to authorize or revoke access to the owner account will receive an error. You
cannot restore or describe a snapshot that is owned by an inactive AWS customer account.

After you have authorized access to an AWS customer account, no users in
that account can perform any actions on the snapshot unless they assume a role with
policies that allow them to do so.

- Users in the snapshot owner account can authorize and revoke access to a snapshot
  only if they assume a role with an IAM policy that allows them to perform those
  actions with a resource specification that includes the snapshot. For example, the
  following policy allows a user or role in AWS account `012345678912` to
  authorize other accounts to access a snapshot named
  `my-snapshot20130829`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "redshift:AuthorizeSnapshotAccess",
 "redshift:RevokeSnapshotAccess"
 ],
 "Resource":[
 "arn:aws:redshift:us-east-1:012345678912:snapshot:*/my-snapshot20130829"
 ]
 }
 ]
}`

```

- Users in an AWS account with which a snapshot has been shared cannot perform
  actions on that snapshot unless they have permissions allowing those actions. You can
  do this by assigning the policy to a role and assuming the role.
  - To list or describe a snapshot, they must have an IAM policy that allows the
    `DescribeClusterSnapshots` action. The following code shows an
    example:

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement":[
   {
   "Effect":"Allow",
   "Action":[
   "redshift:DescribeClusterSnapshots"
   ],
   "Resource":[
   "*"
   ]
   }
   ]
  }`

  ```

  - To restore a snapshot, a user must assume a role with an IAM policy that
    allows the `RestoreFromClusterSnapshot` action and has a resource
    element that covers both the cluster they are attempting to create and the
    snapshot. For example, if a user in account `012345678912` has
    shared snapshot `my-snapshot20130829` with account
    `219876543210`, in order to create a cluster by restoring the
    snapshot, a user in account `219876543210` must assume a role with a
    policy such as the following:

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement":[
   {
   "Effect":"Allow",
   "Action":[
   "redshift:RestoreFromClusterSnapshot"
   ],
   "Resource":[
   "arn:aws:redshift:us-east-1:012345678912:snapshot:*/my-snapshot20130829",
   "arn:aws:redshift:us-east-1:219876543210:cluster:from-another-account"
   ]
   }
   ]
  }`

  ```

  - After access to a snapshot has been revoked from an AWS account, no users
    in that account can access the snapshot. This is the case even if those
    accounts have IAM policies that allow actions on the previously shared
    snapshot resource.

## Sharing a cluster snapshot using the console

On the console, you can authorize other users to access a manual snapshot you own,
and you can later revoke that access when it is no longer required.

###### To share a snapshot with another account

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose the manual snapshot to share.
3. For **Actions**, choose **Manual snapshot
   settings** to display the properties of the manual snapshot.
4. Enter the account or accounts to share with in the **Manage
   access** section, then choose **Save**.

## Security considerations for sharing

encrypted snapshots

When you provide access to an encrypted snapshot, Redshift requires that the AWS
KMS customer managed key used to create the snapshot is shared with the account or
accounts performing the restore. If the key isn't shared, attempting to restore the
snapshot results in an access-denied error. The receiving account doesn't need any extra
permissions to restore a shared snapshot. When you authorize snapshot access and share
the key, the identity authorizing access must have `kms:DescribeKey`
permissions on the key used to encrypt the snapshot. This permission is described in
more detail in [AWS KMS
permissions](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md"). For more information, see [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") in the Amazon Redshift API reference
documentation.

The customer managed key policy can be updated programmatically or in the AWS Key Management Service
console.

###### Note

If you're using a default KMS key, you don't need to take action or change anything in AWS KMS
in order to share a snapshot.

### Allowing access to

the AWS KMS key for an encrypted snapshot

To share the AWS KMS customer managed key for an encrypted snapshot, update
the key policy by performing the following steps:

1. Update the KMS key policy with the Amazon Resource Name (ARN) of the AWS
   account that you are sharing to as `Principal` in the KMS key
   policy.
2. Allow the `kms:Decrypt` action.

In the following key-policy example, user `111122223333` is the owner
of the KMS key, and user `444455556666` is the account that the key is
shared with. This key policy gives the AWS account access to the sample KMS key by
including the ARN for the root AWS account identity for user
`444455556666` as a `Principal` for the policy, and by
allowing the `kms:Decrypt` action.

JSON

```
`{
 "Id": "key-policy-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111122223333:user/KeyUser",
 "arn:aws:iam::444455556666:root"
 ]
 },
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

After access is granted to the customer managed KMS key, the account that restores
the encrypted snapshot must create an AWS Identity and Access Management (IAM) role, or user, if it doesn't
already have one. In addition, that AWS account must also attach an IAM policy to
that IAM role or user that allows them to restore an encrypted database snapshot,
using your KMS key.

For more information about giving access to an AWS KMS key, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console"), in the AWS Key Management Service
developer guide.

For an overview of key policies, see [How Amazon Redshift uses AWS KMS](../../../kms/latest/developerguide/services-redshift.md "../../../kms/latest/developerguide/services-redshift.md").
