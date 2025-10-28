# Remove tags associated with a KMS key

Tags help identify and organize your AWS resources. You can remove the tags associated
with your customer managed KMS keys in the AWS KMS console or by using the [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation. You cannot edit
or remove the tags of an AWS managed key.

The following procedures demonstrate how to remove tags from a KMS key. The
AWS KMS API examples use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"),
but you can use any supported programming language.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. (You cannot manage the tags of an
   AWS managed key)
4. You can use the table filter to display only KMS keys with particular tags. For
   details, see [View tags using the AWS KMS
   console](view-tags.md#view-tag-console "view-tags.md#view-tag-console").
5. Select the check box next to the alias of a KMS key.
6. Choose **Key actions**, **Add or edit
   tags**.
7. On the details page for KMS key, choose the **Tags**
   tab.
   - To delete a tag, choose **Edit**. On the tag row, choose
     **Remove**, and then choose **Save**.

8. To save your changes, choose **Save changes**.
   The [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation
   deletes tags from a KMS key. To identify the tags to delete, specify the tag keys. You
   cannot use this operation to delete tags from KMS keys a different AWS account.

When it succeeds, the `UntagResource` operation doesn't return any output.
Also, if the specified tag key isn't found on the KMS key, it doesn't throw an exception
or return a response. To confirm that the operation worked, use the [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md") operation.

For example, this command deletes the `Purpose` tag and its value
from the specified KMS key.

```
`$` `aws kms untag-resource --key-id 1234abcd-12ab-34cd-56ef-1234567890ab --tag-keys Purpose`
```
