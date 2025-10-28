# Edit tags associated with a KMS key

Tags help identify and organize your AWS resources. You can edit the tags associated
with your customer managed KMS keys in the AWS KMS console or by using the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation. You cannot edit the
tags of an AWS managed key.

The following procedures demonstrate how to edit the tags associated with a KMS key. The
AWS KMS API examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"),
but you can use any supported programming language.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. (You cannot edit the tags of an AWS managed key)
4. You can use the table filter to display only KMS keys with particular tags. For
   details, see [View tags using the AWS KMS
   console](view-tags.md#view-tag-console "view-tags.md#view-tag-console").
5. Select the check box next to the alias of a KMS key.
6. Choose **Key actions**, **Add or edit
   tags**.
7. On the details page for KMS key, choose the **Tags**
   tab.
   - To change the name or value of a tag, choose **Edit**, make
     your changes, and then choose **Save**.

8. To save your changes, choose **Save changes**.
   The [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation add
   one or more tags to a customer managed key;. However, you can also use **TagResource** to change the tag value of an existing tag. You
   cannot use this operation to add or edit tags in a different AWS account.

To edit a tag, specify an existing tag key and a new tag value. Each tag on a
KMS key must have a different tag key. The tag value can be a null or empty
string.

For example, this command changes the value of the `Purpose` tag from
`Pretest` to `Test`.

```
`$` `aws kms tag-resource \
 --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
 --tags TagKey=Purpose,TagValue=Test`
```
