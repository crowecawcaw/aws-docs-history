# Examining the key policy

[Key policies](key-policies.md "key-policies.md") are the primary way to control access to
KMS keys. Every KMS key has exactly one key policy.

When a key policy consists of or includes the [default key policy](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam"), the key policy
allows IAM administrators in the account to use IAM policies to control
access to the KMS key. Also, if the key policy gives [another AWS account](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md") permission to
use the KMS key, the IAM administrators in the external account can use IAM policies to
delegate those permissions. To determine the complete list of principals that can access the
KMS key, [examine the IAM policies](determining-access-iam-policies.md "determining-access-iam-policies.md").

To view the key policy of an AWS KMS [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") or [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key") in your account, use
the AWS Management Console or the [GetKeyPolicy](../APIReference/API_GetKeyPolicy.md "../APIReference/API_GetKeyPolicy.md")
operation in the AWS KMS API. To view the key policy, you must have
`kms:GetKeyPolicy` permissions for the KMS key. For instructions for viewing the key
policy for a KMS key, see [View a key policies](key-policy-viewing.md "key-policy-viewing.md").

Examine the key policy document and take note of all principals specified in each policy
statement's `Principal` element. In a policy statement with an `Allow`
effect, the IAM users, IAM roles, and AWS accounts in the `Principal` element
have access to this KMS key.

###### Note

Do not set the Principal to an asterisk (\*) in any key policy statement that allows permissions unless you use [conditions](policy-conditions.md "policy-conditions.md") to limit the key policy. An asterisk gives every identity in every AWS account permission to use the KMS key, unless another policy statement explicitly denies it. Users in other AWS accounts can use your KMS key whenever they have corresponding permissions in their own account.

The following examples use the policy statements found in the [default key policy](key-policy-default.md "key-policy-default.md") to demonstrate how to do
this.

###### Example Policy statement 1

```
{
  "Sid": "Enable IAM User Permissions",
  "Effect": "Allow",
  **"Principal": {"AWS": "arn:aws:iam::111122223333:root"},**
  "Action": "kms:*",
  "Resource": "*"
}
```

In policy statement 1, `arn:aws:iam::111122223333:root` is an
[AWS account principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-accounts") that refers to the AWS account 111122223333.
(It is not the account root user.) By default, a policy statement like this one is included
in the key policy document when you create a new KMS key with the AWS Management Console, or create a
new KMS key programmatically but do not provide a key policy.

A key policy document with a statement that allows access to the AWS account enables
[IAM policies in the account to
allow access to the KMS key](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam"). This means that users and roles in the account might
have access to the KMS key even if they are not explicitly listed as principals in the key
policy document. Take care to [examine all
IAM policies](determining-access-iam-policies.md "determining-access-iam-policies.md") in all AWS accounts listed as principals to determine whether they
allow access to this KMS key.

###### Example Policy statement 2

```
{
  "Sid": "Allow access for Key Administrators",
  "Effect": "Allow",
  **"Principal": {"AWS": "arn:aws:iam::111122223333:role/KMSKeyAdmins"},**
  "Action": [
    "kms:Describe*",
    "kms:Put*",
    "kms:Create*",
    "kms:Update*",
    "kms:Enable*",
    "kms:Revoke*",
    "kms:List*",
    "kms:Disable*",
    "kms:Get*",
    "kms:Delete*",
    "kms:ScheduleKeyDeletion",
    "kms:CancelKeyDeletion"
  ],
  "Resource": "*"
}
```

In policy statement 2,
`arn:aws:iam::111122223333:role/KMSKeyAdmins` refers to the IAM
role named KMSKeyAdmins in AWS account 111122223333. Users who are authorized to
assume this role are allowed to perform the actions listed in the policy statement, which
are the administrative actions for managing a KMS key.

###### Example Policy statement 3

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  **"Principal": {"AWS": "arn:aws:iam::111122223333:role/EncryptionApp"},**
  "Action": [
    "kms:DescribeKey",
    "kms:GenerateDataKey*",
    "kms:Encrypt",
    "kms:ReEncrypt*",
    "kms:Decrypt"
  ],
  "Resource": "*"
}
```

In policy statement 3,
`arn:aws:iam::111122223333:role/EncryptionApp` refers to the IAM
role named EncryptionApp in AWS account 111122223333. Principals who are
authorized to assume this role are allowed to perform the actions listed in the policy
statement, which include the [cryptographic
operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") for a symmetric encryption KMS key.

###### Example Policy statement 4

```
{
  "Sid": "Allow attachment of persistent resources",
  "Effect": "Allow",
  **"Principal": {"AWS": "arn:aws:iam::111122223333:role/EncryptionApp"},**
  "Action": [
    "kms:ListGrants",
    "kms:CreateGrant",
    "kms:RevokeGrant"
  ],
  "Resource": "*",
  "Condition": {"Bool": {"kms:GrantIsForAWSResource": true}}
}
```

In policy statement 4,
`arn:aws:iam::111122223333:role/EncryptionApp` refers to the IAM
role named EncryptionApp in AWS account 111122223333. Principals who are
authorized assume this role are allowed to perform the actions listed in the policy
statement. These actions, when combined with the actions allowed in **Example policy statement 3**, are those necessary to delegate use of the
KMS key to most [AWS services that integrate with
AWS KMS](service-integration.md "service-integration.md"), specifically the services that use [grants](grants.md "grants.md"). The
[kms:GrantIsForAWSResource](conditions-kms.md#conditions-kms-grant-is-for-aws-resource "conditions-kms.md#conditions-kms-grant-is-for-aws-resource")
value in the `Condition` element ensures that the delegation is allowed only when
the delegate is an AWS service that integrates with AWS KMS and uses grants for
authorization.

To learn all the different ways you can specify a principal in a key policy document,
see [Specifying a Principal](../../../IAM/latest/UserGuide/reference_policies_elements.md#Principal_specifying "../../../IAM/latest/UserGuide/reference_policies_elements.md#Principal_specifying") in the _IAM User Guide_.

To learn more about AWS KMS key policies, see [Key policies in AWS KMS](key-policies.md "key-policies.md").
