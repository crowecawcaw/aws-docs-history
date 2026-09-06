

# Add tags to a KMS key
<a name="add-tags"></a>

Tags help identify and organize your AWS resources. You can add tags to a customer managed key when you [create the KMS key](create-keys.md), or add tags to existing KMS keys. You cannot tag AWS managed keys.

The following procedures demonstrate how to add tags to customer managed keys using the AWS KMS console and AWS KMS API. The AWS KMS API examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), but you can use any supported programming language.

**Topics**
+ [Add tags while creating a KMS key](#tag-on-create)
+ [Add tags to existing KMS keys](#tag-exisiting)

## Add tags while creating a KMS key
<a name="tag-on-create"></a>

You can add tags to a KMS key as you create the key using the AWS KMS console or the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) operation. To add tags when creating a KMS key, you must have `kms:TagResource` permission in an IAM policy in addition to the permissions required to create KMS keys. At a minimum, the permission must cover all KMS keys in the account and Region. For details, see [Controlling access to tags](tag-permissions.md).

### Using the AWS KMS console
<a name="tag-on-create-console"></a>

To add tags when creating a KMS key in the console, you must have the permissions required to view KMS keys in the console in addition to the permissions required to tag and create KMS keys. At a minimum, the permission must cover all KMS keys in the account and Region.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**. (You cannot manage the tags of an AWS managed key)

1. Choose the key type, then choose **Next**.

1. Enter an alias and optional description.

1. Enter a tag key and, optionally, a tag value. To add additional tags, choose **Add tag**. To delete a tag, choose **Remove**. When you're done tagging your new KMS key, choose **Next**.

1. Finish creating your KMS key.

### Using the AWS KMS API
<a name="tagging-keys-create-key"></a>

To specify tags when creating keys using the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) operation, use the `Tags` parameter of the operation. 

The value of the `Tags` parameter of `CreateKey` is a collection of case-sensitive tag key and tag value pairs. Each tag on a KMS key must have a different tag name. The tag value can be a null or empty string.

For example, the following AWS CLI command creates a symmetric encryption KMS key with a `Project:Alpha` tag. When specifying more than one key-value pair, use a space to separate each pair.

```
$ aws kms create-key --tags TagKey=Project,TagValue=Alpha
```

When this command is successful, it returns a `KeyMetadata` object with information about the new KMS key. However, the `KeyMetadata` does not include tags. To get the tags, use the [ListResourceTags](view-tags.md#tagging-keys-list-resource-tags) operation.

## Add tags to existing KMS keys
<a name="tag-exisiting"></a>

You can add tags to your existing customer managed KMS keys in the AWS KMS console or by using the [TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html) operation. To add tags, you need tagging permission on the KMS key. You can get this permission from the key policy for the KMS key or, if the key policy allows it, from an IAM policy that includes the KMS key.

### Using the AWS KMS console
<a name="tag-existing-console"></a>

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Customer managed keys**. (You cannot manage the tags of an AWS managed key)

1. You can use the table filter to display only KMS keys with particular tags. For details, see [View tags using the AWS KMS console](view-tags.md#view-tag-console).

1. Select the check box next to the alias of a KMS key.

1. Choose **Key actions**, **Add or edit tags**.

1. On the details page for KMS key, choose the **Tags** tab.
   + To create your first tag, choose **Create tag**, type a tag key (required) and tag value (optional), and then choose **Save**.

     If you leave the tag value blank, the actual tag value is a null or empty string.
   + To add a tag, choose **Edit**, choose **Add tag**, type a tag key and tag value, and then choose **Save**.

1. To save your changes, choose **Save changes**.

### Using the AWS KMS API
<a name="tagging-keys-tag-resource"></a>

The [TagResource](https://docs.aws.amazon.com/kms/latest/APIReference/API_TagResource.html) operation adds one or more tags to a KMS key. You cannot use this operation to add tags in a different AWS account. You can also use the TagResource operation to edit existing tags. For more information, see [Edit tags associated with a KMS key](edit-tags.md).

To add a tag, specify a new tag key and a tag value. Each tag on a KMS key must have a different tag key. The tag value can be a null or empty string.

For example, the following command adds **Purpose** and **Department** tags to an example KMS key.

```
$ aws kms tag-resource \
         --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
         --tags TagKey=Purpose,TagValue=Pretest TagKey=Department,TagValue=Finance
```

When this command is successful, it does not return any output. To view the tags on a KMS key, use the [ListResourceTags](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListResourceTags.html) operation.