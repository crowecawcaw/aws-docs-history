# Adding a tag to a vector index

You can add tags to Amazon S3 vector indexes and modify these tags. There is no additional
charge for using tags on vector indexes beyond the standard S3 API request rates. For more
information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For
more information about tagging vector indexes, see [Using tags with S3 vector indexes](vector-index-tagging.md "vector-index-tagging.md").

## Permissions

To add a tag to a vector index, you must have the following permission:

- `s3vectors:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to add a tag to a vector index, you can do
the following:

- Verify that you have the required [Permissions](#add-index-tag-permissions "#add-index-tag-permissions") to add a tag to a vector index.
- If you attempted to add a tag key that starts with the AWS reserved prefix
  `aws:`, change the tag key and try again.

## Steps

You can add tags to vector indexes by using the Amazon S3 console, the AWS Command Line Interface
(AWS CLI), the Amazon S3 REST API, and AWSSDKs.

###### To add tags to a vector index using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **vector indexes**.
3. Choose the vector index name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and choose **Add new
   Tag**.
6. This opens the **Add Tags** page. You can enter up to 50 tag
   key value pairs.
7. If you add a new tag with the same key name as an existing tag, the value of the
   new tag overrides the value of the existing tag.
8. You can also edit the values of existing tags on this page.
9. After you have added the tag(s), choose **Save
   changes**.

For information about the Amazon S3 REST API support for adding tags to a vector
index, see the following section in the _Amazon S3 Vectors API
Reference_:

[TagResource](../API/API_S3VectorBuckets_TagResource.md "../API/API_S3VectorBuckets_TagResource.md")

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to add tags to a vector index by using the
AWS CLI. To use the command replace the `user input
 placeholders` with your own information.

```
aws s3vectors tag-resource \
--resource-arn arn:aws:s3vectors:us-east-1:`012345678900`:bucket/`acc-bucket`/index/`accounts-index` \
--tags `Stage`=`Prod`,`CostCenter`=`Marketing`
```
