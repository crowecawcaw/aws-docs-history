# ABAC for AWS KMS

Attribute-based access control (ABAC) is an authorization strategy that defines
permissions based on attributes. AWS KMS supports ABAC by allowing you to control access to
your customer managed keys based on the tags and aliases associated with the KMS keys. The tag and
alias condition keys that enable ABAC in AWS KMS provide a powerful and flexible way to
authorize principals to use KMS keys without editing policies or managing grants. But you
should use these feature with care so principals aren't inadvertently allowed or denied
access.

If you use ABAC, be aware that permission to manage tags and aliases is now an access
control permission. Be sure that you know the existing tags and aliases on all KMS keys
before you deploy a policy that depends on tags or aliases. Take reasonable precautions when
adding, deleting, and updating aliases, and when tagging and untagging keys. Give
permissions to manage tags and aliases only to principals who need them, and limit the tags
and aliases they can manage.

###### Notes

When using ABAC for AWS KMS, be cautious about giving principals permission to manage
tags and aliases. Changing a tag or alias might allow or deny permission to a KMS key.
Key administrators who don't have permission to change key policies or create grants can
control access to KMS keys if they have permission to manage tags or aliases.

It might take up to five minutes for tag and alias changes to affect KMS key authorization. Recent changes might be visible in API operations before they affect authorization.

To control access to a KMS key based on its alias, you must use a condition key. You
cannot use an alias to represent a KMS key in the `Resource` element of a
policy statement. When an alias appears in the `Resource` element, the policy
statement applies to the alias, not to the associated KMS key.

**Learn more**

- For details about AWS KMS support for ABAC, including examples, see [Use aliases to control access to KMS keys](alias-authorization.md "alias-authorization.md") and [Use tags to control access to KMS keys](tag-authorization.md "tag-authorization.md").
- For more general information about using tags to control access to AWS
  resources, see [What is
  ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") and [Controlling Access to AWS Resources Using Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
  _IAM User Guide_.

## ABAC condition keys for AWS KMS

To authorize access to KMS keys based on their tags and aliases, use the following
condition keys in a key policy or IAM policy.

| ABAC condition key                                                                                                                                                                                                      | Description                                                                                            | Policy type                  | AWS KMS operations                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [aws:ResourceTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag")        | Tag (key and value) on the KMS key matches the tag (key and value)<br>or tag pattern in the policy     | IAM policy only              | KMS key resource operations 2                                                                                                                                                                                                                                                                                 |
| [aws:RequestTag/_tag-key_](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag") | Tag (key and value) in the request matches the tag (key and value) or<br>tag pattern in the policy     | Key policy and IAM policies1 | [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md"),<br>[UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                                                                                                                       |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                    | Tag keys in the request match the tag keys in the policy                                               | Key policy and IAM policies1 | [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md"),<br>[UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                                                                                                                       |
| [kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases "conditions-kms.md#conditions-kms-resource-aliases")                                                                                            | Aliases associated with the KMS key match the aliases or alias<br>patterns in the policy               | IAM policy only              | KMS key resource operations 2                                                                                                                                                                                                                                                                                 |
| [kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias "conditions-kms.md#conditions-kms-request-alias")                                                                                                     | Alias that represents the KMS key in the request matches the alias<br>or alias patterns in the policy. | Key policy and IAM policies1 | [Cryptographic<br>operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"), [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md"), [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") |

1Any condition key that can be used in a key policy can
also be used in an IAM policy, but only if [the key policy allows
it](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam").

2A _KMS key resource
operation_ is an operation authorized for a particular KMS key. To
identify the KMS key resource operations, in the [AWS KMS permissions table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look
for a value of KMS key in the `Resources` column for the operation.

For example, you can use these condition keys to create the following policies.

- An IAM policy with `kms:ResourceAliases` that allows permission
  to use KMS keys with a particular alias or alias pattern. This is a bit
  different from policies that rely on tags: Although you can use alias patterns
  in a policy, each alias must be unique in an AWS account and Region. This
  allows you to apply a policy to a select set of KMS keys without listing the
  key ARNs of the KMS keys in the policy statement. To add or remove KMS keys
  from the set, change the alias of the KMS key.
- A key policy with `kms:RequestAlias` that allows principals to use
  a KMS key in a `Encrypt` operation, but only when the
  `Encrypt` request uses that alias to identify the
  KMS key.
- An IAM policy with `aws:ResourceTag/*tag-key*` that denies permission to use KMS keys with
  a particular tag key and tag value. This lets you apply a policy to a select set
  of KMS keys without listing the key ARNs of the KMS keys in the policy
  statement. To add or remove KMS keys from the set, tag or untag the
  KMS key.
- An IAM policy with `aws:RequestTag/*tag-key*` that allows principals to delete only
  `"Purpose"="Test"` KMS key tags.
- An IAM policy with `aws:TagKeys` that denies permission to tag or
  untag a KMS key with a `Restricted` tag key.

ABAC makes access management flexible and scalable. For example, you can use the
`aws:ResourceTag/*tag-key*`
condition key to create an IAM policy that allows principals to use a KMS key for
specified operations only when the KMS key has a `Purpose=Test` tag. The
policy applies to all KMS keys in all Regions of the AWS account.

When attached to a user or role, the following IAM policy allows principals to use
all existing KMS keys with a `Purpose=Test` tag for the specified
operations. To provide this access to new or existing KMS keys, you don't need to
change the policy. Just attach the `Purpose=Test` tag to the KMS keys.
Similarly, to remove this access from KMS keys with a `Purpose=Test` tag,
edit or delete the tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AliasBasedIAMPolicy",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Purpose": "Test"
 }
 }
 }
 ]
}`

```

However, if you use this feature, be careful when managing tags and aliases. Adding,
changing, or deleting a tag or alias can inadvertently allow or deny access to a
KMS key. Key administrators who don't have permission to change key policies or create
grants can control access to KMS keys if they have permission to manage tags and
aliases. To mitigate this risk, consider [limiting permissions to manage tags](tag-permissions.md#tag-permissions-conditions "tag-permissions.md#tag-permissions-conditions") and [aliases](alias-access.md#alias-access-limiting "alias-access.md#alias-access-limiting"). For example, you might want to allow
only select principals to manage `Purpose=Test` tags. For details, see [Use aliases to control access to KMS keys](alias-authorization.md "alias-authorization.md") and [Use tags to control access to KMS keys](tag-authorization.md "tag-authorization.md").

## Tags or aliases?

AWS KMS supports ABAC with tags and aliases. Both options provide a flexible, scalable
access control strategy, but they're slightly different from each other.

You might decide to use tags or use aliases based on your particular AWS use
patterns. For example, if you have already given tagging permissions to most
administrators, it might be easier to control an authorization strategy based on
aliases. Or, if you are close to the quota for [aliases
per KMS key](resource-limits.md#aliases-per-key "resource-limits.md#aliases-per-key"), you might prefer an authorization strategy based on tags.

The following benefits are of general interest.

**Benefits of tag-based access control**

- Same authorization mechanism for different types of AWS resources.

You can use the same tag or tag key to control access to multiple resource
types, such as an Amazon Relational Database Service (Amazon RDS) cluster, an Amazon Elastic Block Store (Amazon EBS) volume, and a KMS key. This feature enables several different authorization models that are
more flexible than traditional role-based access control.

- Authorize access to a group of KMS keys.

You can use tags to manage access to a group of KMS keys in the same
AWS account and Region. Assign the same tag or tag key to the KMS keys that
you choose. Then create a simple, easy-to-maintain policy statement that is
based on the tag or tag key. To add or remove a KMS key from your
authorization group, add or remove the tag; you don't need to edit the
policy.

**Benefits of alias-based access control**

- Authorize access to cryptographic operations based on aliases.

Most request-based policy conditions for attributes, including [aws:RequestTag/_tag-key_](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag"),
affect only operations that add, edit, or delete the attribute. But the [kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias "conditions-kms.md#conditions-kms-request-alias") condition key
controls access to cryptographic operations based on the alias used to identify
the KMS key in the request. For example, you can give a principal permission
to use a KMS key in a `Encrypt` operation but only when the value
of the `KeyId` parameter is `alias/restricted-key-1`. To
satisfy this condition requires all of the following:

    + The KMS key must be associated with that alias.
    + The request must use the alias to identify the KMS key.
    + The principal must have permission to use the KMS key subject to the
     `kms:RequestAlias` condition.

This is particularly useful if your applications commonly use alias names or
alias ARNs to refer to KMS keys.

- Provide very limited permissions.

An alias must be unique in an AWS account and Region. As a result, giving
principals access to a KMS key based on an alias can be much more restrictive
than giving them access based on a tag. Unlike aliases, tags can be assigned to
multiple KMS keys in the same account and Region. If you choose, you can use
an alias pattern, such as `alias/test*`, to give principals access to
a group of KMS keys in the same account and Region. However, allowing or
denying access to a particular alias allows very strict control on
KMS keys.
