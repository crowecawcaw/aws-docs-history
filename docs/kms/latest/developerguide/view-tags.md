# View tags associated with a KMS key

Tags help identify and organize your AWS resources. You can view the tags associated
with your customer managed KMS keys in the AWS KMS console or by using the [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md") operation.

The following procedures demonstrate how to find the tags associated with a specific
KMS key. The AWS KMS API examples use the [AWS Command Line Interface
(AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), but you can use any supported programming language.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. (You cannot manage the tags of an
   AWS managed key)
4. You can use the table filter to display only KMS keys with particular
   tags.

To display only KMS keys with a particular tag, choose the filter box, choose
the tag key, and then choose from among the actual tag values. You can also type all
or part of the tag value.

The resulting table displays all KMS keys with the chosen tag. However, it
doesn't display the tag. To see the tag, choose the key ID or alias of the KMS key
and on its detail page, choose the **Tags** tab. The tabs appear
below the **General configuration** section.

This filter requires both the tag key and tag value. It won't find KMS keys by
typing only the tag key or only its value. To filter tags by all or part of the tag
key or value, use the [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md") operation to get tagged KMS keys, then use the filtering
features of your programming language. 5. Select the check box next to the alias of a KMS key. 6. Choose **Key actions**, **Add or edit
tags**. 7. On the details page for KMS key, choose the **Tags**
tab.
The [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md")
operation gets the tags for a KMS key. The `KeyId` parameter is required. You
cannot use this operation to view the tags on KMS keys in a different
AWS account.

For example, the following command gets the tags for an example KMS key.

```
`$` `aws kms list-resource-tags --key-id 1234abcd-12ab-34cd-56ef-1234567890ab`

  `"Truncated": false,
 "Tags": [
 {
 "TagKey": "Project",
 "TagValue": "Alpha"
 },
 {
 "TagKey": "Purpose",
 "TagValue": "Test"
 },
 {
 "TagKey": "Department",
 "TagValue": "Finance"
 }
 ]`
}
```
