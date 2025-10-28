# IAM policy examples

In this section, you can find example IAM policies that allow permissions for various
AWS KMS actions.

###### Important

Some of the permissions in the following policies are allowed only when the KMS key's
key policy also allows them. For more information, see [Permissions reference](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

###### Examples

- [Allow a user to view KMS keys in
  the AWS KMS console](#iam-policy-example-read-only-console "#iam-policy-example-read-only-console")
- [Allow a user to create KMS keys](#iam-policy-example-create-key "#iam-policy-example-create-key")
- [Allow a user to encrypt and
  decrypt with any KMS key in a specific AWS account](#iam-policy-example-encrypt-decrypt-one-account "#iam-policy-example-encrypt-decrypt-one-account")
- [Allow a user to
  encrypt and decrypt with any KMS key in a specific AWS account and Region](#iam-policy-example-encrypt-decrypt-one-account-one-region "#iam-policy-example-encrypt-decrypt-one-account-one-region")
- [Allow a user to encrypt
  and decrypt with specific KMS keys](#iam-policy-example-encrypt-decrypt-specific-cmks "#iam-policy-example-encrypt-decrypt-specific-cmks")
- [Prevent a user from disabling or
  deleting any KMS keys](#iam-policy-example-deny-disable-delete "#iam-policy-example-deny-disable-delete")

## Allow a user to view KMS keys in

the AWS KMS console

The following IAM policy allows users read-only access to the AWS KMS console. Users
with these permissions can view all KMS keys in their AWS account, but they cannot
create or change any KMS keys.

To view KMS keys on the **AWS managed keys** and
**Customer managed keys** pages, principals require [kms:ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md"), [kms:ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md"), and [tag:GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md") permissions, even if the keys do not have tags or aliases. The
remaining permissions, particularly [kms:DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md"), are required to view optional KMS key table columns and data
on the KMS key detail pages. The [iam:ListUsers](../../../IAM/latest/APIReference/API_ListUsers.md "../../../IAM/latest/APIReference/API_ListUsers.md") and [iam:ListRoles](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md") permissions are required to display the key policy in default view
without error. To view data on the **Custom key stores** page and details
about KMS keys in custom key stores, principals also need [kms:DescribeCustomKeyStores](../APIReference/API_DescribeCustomKeyStores.md "../APIReference/API_DescribeCustomKeyStores.md")
permission.

If you limit a user's console access to particular KMS keys, the console displays an
error for each KMS key that is not visible.

This policy includes of two policy statements. The `Resource` element in the
first policy statement allows the specified permissions on all KMS keys in all Regions of
the example AWS account. Console viewers don't need additional access because the AWS KMS
console displays only KMS keys in the principal's account. This is true even if they have
permission to view KMS keys in other AWS accounts. The remaining AWS KMS and IAM
permissions require a `"Resource": "*"` element because they don't apply to any
particular KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyAccessForAllKMSKeysInAccount",
 "Effect": "Allow",
 "Action": [
 "kms:GetPublicKey",
 "kms:GetKeyRotationStatus",
 "kms:GetKeyPolicy",
 "kms:DescribeKey",
 "kms:ListKeyPolicies",
 "kms:ListResourceTags",
 "tag:GetResources"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 },
 {
 "Sid": "ReadOnlyAccessForOperationsWithNoKMSKey",
 "Effect": "Allow",
 "Action": [
 "kms:ListKeys",
 "kms:ListAliases",
 "iam:ListRoles",
 "iam:ListUsers"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow a user to create KMS keys

The following IAM policy allows a user to create all types of KMS keys. The value of
the `Resource` element is `*` because the `CreateKey`
operation does not use any particular AWS KMS resources (KMS keys or aliases).

To restrict the user to particular types of KMS keys, use the [kms:KeySpec](conditions-kms.md#conditions-kms-key-spec "conditions-kms.md#conditions-kms-key-spec"), [kms:KeyUsage](conditions-kms.md#conditions-kms-key-usage "conditions-kms.md#conditions-kms-key-usage"), and [kms:KeyOrigin](conditions-kms.md#conditions-kms-key-origin "conditions-kms.md#conditions-kms-key-origin") condition keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "kms:CreateKey",
 "Resource": "*"
 }
}`

```

Principals who create keys might need some related permissions.

- **kms:PutKeyPolicy** — Principals who have
  `kms:CreateKey` permission can set the initial key policy for the
  KMS key. However, the `CreateKey` caller must have [kms:PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") permission, which
  lets them change the KMS key policy, or they must specify the
  `BypassPolicyLockoutSafetyCheck` parameter of `CreateKey`, which
  is not recommended. The `CreateKey` caller can get
  `kms:PutKeyPolicy` permission for the KMS key from an IAM policy or
  they can include this permission in the key policy of the KMS key that they're
  creating.
- **kms:TagResource** — To add tags to the
  KMS key during the `CreateKey` operation, the `CreateKey` caller
  must have [kms:TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
  permission in an IAM policy. Including this permission in the key policy of the new
  KMS key isn't sufficient. However, if the `CreateKey` caller includes
  `kms:TagResource` in the initial key policy, they can add tags in a
  separate call after the KMS key is created.
- **kms:CreateAlias** — Principals who create a
  KMS key in the AWS KMS console must have [kms:CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") permission on the KMS key and on the alias. (The console
  makes two calls; one to `CreateKey` and one to `CreateAlias`). You
  must provide the alias permission in an IAM policy. You can provide the KMS key
  permission in a key policy or IAM policy. For details, see [Controlling access to aliases](alias-access.md "alias-access.md").

In addition to `kms:CreateKey`, the following IAM policy provides
`kms:TagResource` permission on all KMS keys in the AWS account and
`kms:CreateAlias` permission on all aliases that the account. It also includes
some useful read-only permissions that can be provided only in an IAM policy.

This IAM policy does not include `kms:PutKeyPolicy` permission or any other
permissions that can be set in a key policy. It's a [best practice](iam-policies-best-practices.md "iam-policies-best-practices.md") to set these permissions in the
key policy where they apply exclusively to one KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMPermissionsForParticularKMSKeys",
 "Effect": "Allow",
 "Action": "kms:TagResource",
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 },
 {
 "Sid": "IAMPermissionsForParticularAliases",
 "Effect": "Allow",
 "Action": "kms:CreateAlias",
 "Resource": "arn:aws:kms:*:`111122223333`:alias/*"
 },
 {
 "Sid": "IAMPermissionsForAllKMSKeys",
 "Effect": "Allow",
 "Action": [
 "kms:CreateKey",
 "kms:ListKeys",
 "kms:ListAliases"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow a user to encrypt and

decrypt with any KMS key in a specific AWS account

The following IAM policy allows a user to encrypt and decrypt data with any KMS key
in AWS account 111122223333.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 }
}`

```

## Allow a user to

encrypt and decrypt with any KMS key in a specific AWS account and Region

The following IAM policy allows a user to encrypt and decrypt data with any KMS key
in AWS account `111122223333` in the US West (Oregon)
Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-west-2:`111122223333`:key/*"
 ]
 }
}`

```

## Allow a user to encrypt

and decrypt with specific KMS keys

The following IAM policy allows a user to encrypt and decrypt data with the two
KMS keys specified in the `Resource` element. When specifying a KMS key in an
IAM policy statement, you must use the [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") of
the KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-west-2:`111122223333`:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "arn:aws:kms:us-west-2:`111122223333`:key/01234abc-d12a-b34c-d56e-f1234567890a'"
 ]
 }
}`

```

## Prevent a user from disabling or

deleting any KMS keys

The following IAM policy prevents a user from disabling or deleting any KMS keys,
even when another IAM policy or a key policy allows these permissions. A policy that
explicitly denies permissions overrides all other policies, even those that explicitly allow
the same permissions. For more information, see [Troubleshooting AWS KMS permissions](policy-evaluation.md "policy-evaluation.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": [
 "kms:DisableKey",
 "kms:ScheduleKeyDeletion"
 ],
 "Resource": "*"
 }
}`

```
