# Using tags to control access to keys

You can control access to AWS Payment Cryptography based on the tags on the key. For example,
you can write an IAM policy that allows principals to enable and disable only the keys
that have a particular tag. Or you can use an IAM policy to prevent principals from using
keys in cryptographic operations unless the key has a particular tag.

This feature is part of AWS Payment Cryptography support for attribute-based access
control(ABAC). For information about using tags to control access to AWS
resources, see [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") and [Controlling
Access to AWS Resources Using Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_.

AWS Payment Cryptography supports the [aws:ResourceTag/_tag-key_](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") global condition context
key, which lets you control access to keys based on the tags on the key.
Because multiple keys can have the same tag, this feature lets you apply the permission
to a select set of keys. You can also easily change the keys in the set by
changing their tags.

In AWS Payment Cryptography, the `aws:ResourceTag/*tag-key*`
condition key is supported only in IAM policies. It isn't supported in key policies, which
apply only to one key, or on operations that don't use a particular key, such as
the [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md") or [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") operations.

Controlling access with tags provides a simple, scalable, and flexible way to manage
permissions. However, if not properly designed and managed, it can allow or deny access to
your keys inadvertently. If you are using tags to control access, consider the following
practices.

- Use tags to reinforce the best practice of [least privileged
  access](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"). Give IAM principals only the permissions they need on only the
  keys they must use or manage. For example, use tags to label the keys used for
  a project. Then give the project team permission to use only keys with the project
  tag.
- Be cautious about giving principals the `payment-cryptography:TagResource` and
  `payment-cryptography:UntagResource` permissions that let them add, edit, and delete tags.
  When you use tags to control access to keys, changing a tag can give principals
  permission to use keys that they didn't otherwise have permission to use. It can
  also deny access to keys that other principals require to do their jobs. Key
  administrators who don't have permission to change key policies or create grants can
  control access to keys if they have permission to manage tags.

Whenever possible, use a policy condition, such as `aws:RequestTag/*tag-key*` or `aws:TagKeys` to [limit a principal's tagging permissions](tag-permissions.md#tag-permissions-conditions "tag-permissions.md#tag-permissions-conditions") to
particular tags or tag patterns on particular keys.

- Review the principals in your AWS account that currently have tagging and untagging
  permissions and adjust them, if necessary. IAM policies might allow
  tag and untag permissions on all keys. For example, the _Admin_ managed policy
  allows principals to tag, untag, and list tags on all keys.
- Before setting a policy that depends on a tag, review the tags on the keys in
  your AWS account. Make sure that your policy applies only to the tags you intend to
  include. Use [CloudTrail logs](monitoring-cloudtrail.md "monitoring-cloudtrail.md") and CloudWatch alarms to alert you to tag changes that might
  affect access to your keys.
- The tag-based policy conditions use pattern matching; they aren't tied to a particular
  instance of a tag. A policy that uses tag-based condition keys affects all new and
  existing tags that match the pattern. If you delete and recreate a tag that matches a
  policy condition, the condition applies to the new tag, just as it did to the old
  one.
  For example, consider the following IAM policy. It allows the principals to call the
  [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operations only on keys in your account that are the
  US East (N. Virginia) Region and have a `"Project"="Alpha"` tag. You might attach
  this policy to roles in the example Alpha project.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMPolicyWithResourceTag",
 "Effect": "Allow",
 "Action": [
 "payment-cryptography:DecryptData"
 ],
 "Resource": "arn:aws:payment-cryptography:us-east-1:`111122223333`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "Alpha"
 }
 }
 }
 ]
}`

```

The following example IAM policy allows the principals to use any key in the
account for certain cryptographic operations. But it prohibits the principals from using these
cryptographic operations on keys with a `"Type"="Reserved"` tag or no
`"Type"` tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMAllowCryptographicOperations",
 "Effect": "Allow",
 "Action": [
 "payment-cryptography:EncryptData",
 "payment-cryptography:DecryptData",
 "payment-cryptography:ReEncrypt*"
 ],
 "Resource": "arn:aws:payment-cryptography:*:`111122223333`:key/*"
 },
 {
 "Sid": "IAMDenyOnTag",
 "Effect": "Deny",
 "Action": [
 "payment-cryptography:EncryptData",
 "payment-cryptography:DecryptData",
 "payment-cryptography:ReEncrypt*"
 ],
 "Resource": "arn:aws:payment-cryptography:*:`111122223333`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Type": "Reserved"
 }
 }
 },
 {
 "Sid": "IAMDenyNoTag",
 "Effect": "Deny",
 "Action": [
 "payment-cryptography:EncryptData",
 "payment-cryptography:DecryptData",
 "payment-cryptography:ReEncrypt*"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/Type": "true"
 }
 }
 }
 ]
}`

```
