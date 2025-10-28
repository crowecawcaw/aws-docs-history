# Best practices for IAM policies

Securing access to AWS KMS keys is critical to the security of all of your AWS
resources. KMS keys are used to protect many of the most sensitive resources in your
AWS account. Take the time to design the [key policies](key-policies.md "key-policies.md"),
IAM policies, [grants](grants.md "grants.md"), and VPC
endpoint policies that control access to your KMS keys.

In IAM policy statements that control access to KMS keys, use the [least privileged
principle](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"). Give IAM principals only the permissions they need on only the
KMS keys they must use or manage.

The following best practices apply to IAM policies that control access to AWS KMS keys and
aliases. For general IAM policy best practice guidance, see
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

**Use key policies**

Whenever possible, provide permissions in key policies that affect one KMS key,
rather than in an IAM policy that can apply to many KMS keys, including those in
other AWS accounts. This is particularly important for sensitive permissions like
[kms:PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") and [kms:ScheduleKeyDeletion](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md") but
also for cryptographic operations that determine how your data is protected.

**Limit CreateKey permission**

Give permission to create keys ([kms:CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")) only to principals who need it. Principals who create a
KMS key also set its key policy, so they can give themselves and others permission to
use and manage the KMS keys they create. When you allow this permission, consider
limiting it by using [policy conditions](policy-conditions.md "policy-conditions.md"). For
example, you can use the [kms:KeySpec](conditions-kms.md#conditions-kms-key-spec "conditions-kms.md#conditions-kms-key-spec")
condition to limit the permission to symmetric encryption KMS keys.

**Specify KMS keys in an IAM policy**

As a best practice, specify the [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") of
each KMS key to which the permission applies in the `Resource` element of
the policy statement. This practice restricts the permission to the KMS keys that
principal requires. For example, this `Resource` element lists only the
KMS keys the principal needs to use.

```
"Resource": [
    "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321"
]
```

When specifying KMS keys is impractical, use a `Resource` value that
limits access to KMS keys in a trusted AWS account and Region, such as
`arn:aws:kms:`region`:`account`:key/**\***`. Or limit access to KMS keys in all Regions (\*) of
a trusted AWS account, such as `arn:aws:kms:**\***:`account`:key/**\***`.

You cannot use a [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id"), [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name"), or [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") to represent a KMS key in the `Resource` field of an
IAM policy. If you specify an alias ARN, the policy applies to the alias, not to the
KMS key. For information about IAM policies for aliases, see [Controlling access to aliases](alias-access.md "alias-access.md")

**Avoid "Resource": "\*" in an IAM policy**

Use wildcard characters (\*) judiciously. In a key policy, the wildcard character in
the `Resource` element represents the KMS key to which the key policy is
attached. But in an IAM policy, a wildcard character alone in the
`Resource` element (`"Resource": "*"`) applies the permissions
to all KMS keys in all AWS accounts that the principal's account has permission to
use. This might include [KMS keys in other AWS accounts](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md"), as well as KMS keys in the principal's
account.

For example, to use a KMS key in another AWS account, a principal needs
permission from the key policy of the KMS key in the external account, and from an
IAM policy in their own account. Suppose that an arbitrary account gave your
AWS account [kms:Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") permission
on their KMS keys. If so, an IAM policy in your account that gives a role
`kms:Decrypt` permission on all KMS keys (`"Resource": "*"`)
would satisfy the IAM part of the requirement. As a result, principals who can assume
that role can now decrypt ciphertexts using the KMS key in the untrusted account.
Entries for their operations appear in the CloudTrail logs of both accounts.

In particular, avoid using `"Resource": "*"` in a policy statement that
allows the following API operations. These operations can be called on KMS keys in
other AWS accounts.

- [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md")
- [GetKeyRotationStatus](../APIReference/API_GetKeyRotationStatus.md "../APIReference/API_GetKeyRotationStatus.md")
- [Cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") ([Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md"), [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"),
  [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md"), [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md"), [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md"), [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md"), [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md"), [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md"))
- [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md"), [ListGrants](../APIReference/API_ListGrants.md "../APIReference/API_ListGrants.md"), [ListRetirableGrants](../APIReference/API_ListRetirableGrants.md "../APIReference/API_ListRetirableGrants.md"),
  [RetireGrant](../APIReference/API_RetireGrant.md "../APIReference/API_RetireGrant.md"), [RevokeGrant](../APIReference/API_RevokeGrant.md "../APIReference/API_RevokeGrant.md")

**When to use "Resource": "\*"**

In an IAM policy, use a wildcard character in the `Resource` element
only for permissions that require it. Only the following permissions require the
`"Resource": "*"` element.

- [kms:CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
- [kms:GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md")
- [kms:ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md")
- [kms:ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md")
- Permissions for custom key stores, such as [kms:CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md")
  and [kms:ConnectCustomKeyStore](../APIReference/API_ConnectCustomKeyStore.md "../APIReference/API_ConnectCustomKeyStore.md").

###### Note

Permissions for alias operations ([kms:CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md"), [kms:UpdateAlias](../APIReference/API_UpdateAlias.md "../APIReference/API_UpdateAlias.md"), [kms:DeleteAlias](../APIReference/API_DeleteAlias.md "../APIReference/API_DeleteAlias.md")) must be attached to the alias and the KMS key. You can
use `"Resource": "*"` in an IAM policy to represent the aliases and the
KMS keys, or specify the aliases and KMS keys in the `Resource`
element. For examples, see [Controlling access to aliases](alias-access.md "alias-access.md").

 

The examples in this topic provide more information and guidance for designing IAM
policies for KMS keys. For IAM best practices for all AWS resources, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.
