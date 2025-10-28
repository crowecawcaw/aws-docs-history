# Managing key tags with API operations

You can use the [AWS Payment Cryptography API](../APIReference/Welcome.md "../APIReference/Welcome.md") to add, delete,
and list tags for the keys that you manage. These examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported
programming language. You cannot tag AWS managed keys.

To add, edit, view, and delete tags for a key, you must have the required
permissions. For details, see [Controlling access to tags](tag-permissions.md "tag-permissions.md").

###### Topics

- [CreateKey: Add tags to a new key](#tagging-keys-create-key "#tagging-keys-create-key")
- [TagResource: Add or change tags for a
  key](#tagging-keys-tag-resource "#tagging-keys-tag-resource")
- [ListResourceTags: Get the tags for a
  key](#tagging-keys-list-resource-tags "#tagging-keys-list-resource-tags")
- [UntagResource: Delete tags from a
  key](#tagging-keys-untag-resource "#tagging-keys-untag-resource")

## CreateKey: Add tags to a new key

You can add tags when you create a key. To specify the tags, use the `Tags`
parameter of the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation.

To add tags when creating a key, the caller must have `payment-cryptography:TagResource`
permission in an IAM policy. At a minimum, the permission must cover all keys in the
account and Region. For details, see [Controlling access to tags](tag-permissions.md "tag-permissions.md").

The value of the `Tags` parameter of `CreateKey` is a collection
of case-sensitive tag key and tag value pairs. Each tag on a key must have a different
tag name. The tag value can be a null or empty string.

For example, the following AWS CLI command creates a symmetric encryption key with a
`Project:Alpha` tag. When specifying more than one key-value pair, use a space
to separate each pair.

```
`$` `aws payment-cryptography create-key --exportable --key-attributes KeyAlgorithm=TDES_2KEY, \
 KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY, \
 KeyModesOfUse='{Generate=true,Verify=true}' \
 --tags '[{"Key":"Project","Value":"Alpha"},{"Key":"BIN","Value":"123456"}]'`
```

When this command is successful, it returns a `Key` object with
information about the new key. However, the `Key` does not include
tags. To get the tags, use the [ListResourceTags](#tagging-keys-list-resource-tags "#tagging-keys-list-resource-tags") operation.

## TagResource: Add or change tags for a

key

The [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation adds
one or more tags to a key. You cannot use this operation to add or edit tags in a
different AWS account.

To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing
tag key and a new tag value. Each tag on a key must have a different tag key. The tag
value can be a null or empty string.

For example, the following command adds `UseCase` and
`BIN` tags to an example key.

```
`$` `aws payment-cryptography tag-resource --resource-arn arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h --tags '[{"Key":"UseCase","Value":"Acquiring"},{"Key":"BIN","Value":"123456"}]'`
```

When this command is successful, it does not return any output. To view the tags on a
key, use the [ListResourceTags](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation.

You can also use **TagResource** to change
the tag value of an existing tag. To replace a tag value, specify the same tag key with a
different value. Tags not listed in a modify command are not changed or removed.

For example, this command changes the value of the `Project` tag from
`Alpha` to `Noe`.

The command will return http/200 with no content. To see your changes, use `ListTagsForResource`

```
`$` `aws payment-cryptography tag-resource --resource-arn arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h \
 --tags '[{"Key":"Project","Value":"Noe"}]'`
```

## ListResourceTags: Get the tags for a

key

The [ListResourceTags](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
operation gets the tags for a key. The `ResourceArn` (keyArn or keyAlias) parameter is required. You
cannot use this operation to view the tags on keys in a different
AWS account.

For example, the following command gets the tags for an example key.

```
`$` `aws payment-cryptography list-tags-for-resource --resource-arn arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`

  `{
 "Tags": [
 {
 "Key": "BIN",
 "Value": "20151120"
 },
 {
 "Key": "Project",
 "Value": "Production"
 }
 ]
}`

```

## UntagResource: Delete tags from a

key

The [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation
deletes tags from a key. To identify the tags to delete, specify the tag keys. You
cannot use this operation to delete tags from keys a different AWS account.

When it succeeds, the `UntagResource` operation doesn't return any output.
Also, if the specified tag key isn't found on the key, it doesn't throw an exception
or return a response. To confirm that the operation worked, use the [ListResourceTags](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation.

For example, this command deletes the `Purpose` tag and its value
from the specified key.

```
`$` `aws payment-cryptography untag-resource \
 --resource-arn arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h --tag-keys Project`
```
