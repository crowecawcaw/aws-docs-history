# KMS key access and permissions

To use AWS KMS, you must have credentials that AWS can use to authenticate your requests.
The credentials must include permissions to access AWS resources: AWS KMS keys and [aliases](kms-alias.md "kms-alias.md"). No AWS principal has
any permissions to a KMS key unless that permission is provided explicitly and never denied.
There are no implicit or automatic permission to use or manage a KMS key.

To control access to your KMS keys, you can use the following policy mechanisms.

- [Key policy](key-policies.md "key-policies.md") – Every KMS key has a key
  policy. It is the primary mechanism for controlling access to a KMS key. You can use the
  key policy alone to control access, which means the full scope of access to the KMS key is
  defined in a single document (the key policy). For more information about using key
  policies, see [Key policies](key-policies.md "key-policies.md").
- [IAM policies](iam-policies.md "iam-policies.md") – You can use IAM policies
  in combination with the key policy and grants to control access to a KMS key. Controlling
  access this way enables you to manage all of the permissions for your IAM identities in
  IAM. To use an IAM policy to allow access to a KMS key, the key policy must explicitly
  allow it. For more information about using IAM policies, see [IAM policies](iam-policies.md "iam-policies.md").
- [Grants](grants.md "grants.md") – You can use grants in combination with the
  key policy and IAM policies to allow access to a KMS key. Controlling access this way
  enables you to allow access to the KMS key in the key policy, and to allow identities to
  delegate their access to others. For more information about using grants, see [Grants in AWS KMS](grants.md "grants.md").

## KMS key policies

The primary way to manage access to your AWS KMS resources is with
_policies_. Policies are documents that describe which principals can
access which resources. Policies attached to an IAM identity are called
_identity-based policies_ (or _IAM policies_), and
policies attached to other kinds of resources are called _resource
policies_. AWS KMS resource policies for KMS keys are called _key
policies_.

All KMS keys have a key policy. If you don't provide one, AWS KMS creates one for you. The
[default key policy](key-policy-default.md "key-policy-default.md") that AWS KMS uses differs
depending on whether you create the key in the AWS KMS console or you use the AWS KMS API. We
recommend that you edit the default key policy to align with your organization’s requirements
for [least-privilege permissions](least-privilege.md "least-privilege.md").

You can use the key policy alone to control access if the key and the IAM principal are
in the same AWS account, which means the full scope of access to the KMS key is defined in
a single document (the key policy). However, when a caller in one account must access a key in
a different account, you cannot use key policy alone to grant access. In the cross-account
scenario, an IAM policy must be attached to the caller's user or role that explicitly allows
the caller to make the API call.

You can also use IAM policies in combination with key policies and grants to control
access to a KMS key. To use an IAM policy to control access to a KMS key, the key policy
must give the account permission to use IAM policies. You can either specify a [key policy statement that enables IAM
policies](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam"), or you can explicitly [specify allowed principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying") in the key policy.

When writing policies, ensure that you have strong controls restricting who can perform
the following actions:

- Update, create, and delete IAM and KMS key policies
- Attach and detach IAM policies from users, roles, and groups
- Attach and detach KMS key polices from your KMS keys

## KMS key grants

In addition to IAM and key policies, AWS KMS supports [grants](grants.md "grants.md"). Grants provide a flexible and powerful way to delegate permissions. You can
use grants to issue time-bound KMS key access to IAM principals in your AWS account, or
in other AWS accounts. We recommend issuing time-bound access if you don't know the names of
the principals at the time that the policies are created, or if the principals that require
access frequently change. The [grantee principal](grants.md#terms-grantee-principal "grants.md#terms-grantee-principal")
can be in the same account as the KMS key or a different account. If the principal and
KMS key are in different accounts, then you must specify an IAM policy in addition to the
grant. Grants require additional management because you must call an API to create the grant
and to retire or revoke the grant when it is no longer needed.
