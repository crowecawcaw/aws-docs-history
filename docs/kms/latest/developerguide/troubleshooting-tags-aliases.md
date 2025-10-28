# Troubleshooting ABAC for AWS KMS

Controlling access to KMS keys based on their tags and aliases is convenient and
powerful. However, it's prone to a few predictable errors that you'll want to
prevent.

## Access changed due to tag change

If a tag is deleted or its value is changed, principals who have access to a
KMS key based only on that tag will be denied access to the KMS key. This can
also happen when a tag that is included in a deny policy statement is added to a
KMS key. Adding a policy-related tag to a KMS key can allow access to principals
who should be denied access to a KMS key.

For example, suppose that a principal has access to a KMS key based on the
`Project=Alpha` tag, such as the permission provided by the following
example IAM policy statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMPolicyWithResourceTag",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKeyWithoutPlaintext",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:ap-southeast-1:`111122223333`:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "Alpha"
 }
 }
 }
 ]
}`

```

If the tag is deleted from that KMS key or the tag value is changed, the
principal no longer has permission to use the KMS key for the specified
operations. This might become evident when the principal tries to read or write data
in an AWS service that uses a customer managed key To trace the tag change, review your CloudTrail
logs for [TagResource](ct-tagresource.md "ct-tagresource.md") or [UntagResource entries](ct-untagresource.md "ct-untagresource.md").

To restore access without updating the policy, change the tags on the KMS key.
This action has minimal impact other than a brief period while it is taking effect
throughout AWS KMS. To prevent an error like this one, give tagging and untagging
permissions only to principals who need it and [limit their tagging permissions](tag-permissions.md#tag-permissions-conditions "tag-permissions.md#tag-permissions-conditions") to
tags they need to manage. Before changing a tag, search policies to detect access
that depends on the tag, and get KMS keys in all Regions that have the tag. You
might consider creating an Amazon CloudWatch alarm when particular tags are changed.

## Access change due to alias change

If an alias is deleted or associated with a different KMS key, principals who
have access to the KMS key based only on that alias will be denied access to the
KMS key. This can also happen when an alias that is associated with a KMS key is
included in a deny policy statement. Adding a policy-related alias to a KMS key
can also allow access to principals who should be denied access to a
KMS key.

For example, the following IAM policy statement uses the [kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases "conditions-kms.md#conditions-kms-resource-aliases") condition
key to allow access to KMS keys in different Regions of the account with any of
the specified aliases.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AliasBasedIAMPolicy",
 "Effect": "Allow",
 "Action": [
 "kms:List*",
 "kms:Describe*",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "kms:ResourceAliases": [
 "alias/ProjectAlpha",
 "alias/ProjectAlpha_Test",
 "alias/ProjectAlpha_Dev"
 ]
 }
 }
 }
 ]
}`

```

To trace the alias change, review your CloudTrail logs for [CreateAlias](ct-createalias.md "ct-createalias.md"), [UpdateAlias](ct-updatealias.md "ct-updatealias.md"), and [DeleteAlias](ct-deletealias.md "ct-deletealias.md")
entries.

To restore access without updating the policy, change the alias associated with
the KMS key. Because each alias can be associated with only one KMS key in an
account and Region, managing aliases is a bit more difficult than managing tags.
Restoring access to some principals on one KMS key can deny the same or other
principals access to a different KMS key.

To prevent this error, give alias management permissions only to principals who
need it and [limit their alias-management
permissions](alias-access.md#alias-access-limiting "alias-access.md#alias-access-limiting") to aliases they need to manage. Before updating or deleting
an alias, search policies to detect access that depends on the alias, and find
KMS keys in all Regions that are associated with the alias.

## Access denied due to alias quota

Users who are authorized to use a KMS key by an [kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases "conditions-kms.md#conditions-kms-resource-aliases") condition
will get an `AccessDenied` exception if the KMS key exceeds the default
[aliases per KMS key](resource-limits.md#aliases-per-key "resource-limits.md#aliases-per-key") quota for that
account and Region.

To restore access, delete aliases that are associated with the KMS key so it
complies with the quota. Or use an alternate mechanism to give users access to the
KMS key.

## Delayed authorization change

Changes that you make to tags and aliases might take up to five minutes to affect
the authorization of KMS keys. As a result, a tag or alias change might be
reflected in the responses from API operations before they affect authorization.
This delay is likely to be longer than the brief eventual consistency delay that
affects most AWS KMS operations.

For example, you might have an IAM policy that allows certain principals to use
any KMS key with a `"Purpose"="Test"` tag. Then you add the
`"Purpose"="Test"` tag to a KMS key. Although the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation completes
and [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md")
response confirms that the tag is assigned to the KMS key, the principals might
not have access to the KMS key for up to five minutes.

To prevent errors, build this expected delay into your code.

## Failed requests due to alias updates

When you update an alias, you associate an existing alias with a different
KMS key.

[Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") and [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") requests that specify
the [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name") or [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") might fail because the alias is now
associated with a KMS key that didn't encrypt the ciphertext. This situation
typically returns an `IncorrectKeyException` or
`NotFoundException`. Or if the request has no `KeyId` or
`DestinationKeyId` parameter, the operation might fail with
`AccessDenied` exception because the caller no longer has access to
the KMS key that encrypted the ciphertext.

You can trace the change by looking at CloudTrail logs for [CreateAlias](ct-createalias.md "ct-createalias.md"), [UpdateAlias](ct-updatealias.md "ct-updatealias.md"), and [DeleteAlias](ct-deletealias.md "ct-deletealias.md") log
entries. You can also use the value of the `LastUpdatedDate` field in the
[ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") response to
detect a change.

For example, the following [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") example response shows that the
`ProjectAlpha_Test` alias in the `kms:ResourceAliases`
condition was updated. As a result, the principals who have access based on the
alias lose access to the previously associated KMS key. Instead, they have access
to the newly associated KMS key.

```
`$` aws kms list-aliases --query 'Aliases[?starts_with(AliasName, `alias/ProjectAlpha`)]'

`{
 "Aliases": [
 {
 "AliasName": "alias/ProjectAlpha_Test",
 "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/ProjectAlpha_Test",
 "TargetKeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
 "CreationDate": 1566518783.394,
 **"LastUpdatedDate": 1605308931.903**
 },
 {
 "AliasName": "alias/ProjectAlpha_Restricted",
 "AliasArn": "arn:aws:kms:us-west-2:111122223333:alias/ProjectAlpha_Restricted",
 "TargetKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
 "CreationDate": 1553410800.010,
 "LastUpdatedDate": 1553410800.010
 }
 ]
}`
```

The remedy for this change isn't simple. You can update the alias again to
associate it with the original KMS key. However, before you act, you need to
consider the effect of that change on the currently associated KMS key. If
principals used the latter KMS key in cryptographic operations, they might need
continued access to it. In this case, you might want to update the policy to ensure
that principals have permission to use both of the KMS keys.

You can prevent an error like this one: Before updating an alias, search policies
to detect access that depends on the alias. Then get KMS keys in all Regions that
are associated with the alias. Give alias management permissions only to principals
who need it and [limit their alias-management
permissions](alias-access.md#alias-access-limiting "alias-access.md#alias-access-limiting") to aliases they need to manage.
