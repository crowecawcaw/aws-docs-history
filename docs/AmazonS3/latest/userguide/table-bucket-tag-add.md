# Adding a tag to a table bucket

You can add tags to Amazon S3 table buckets and modify these tags. For more information about tagging table buckets, see [Using tags with S3 table buckets](table-bucket-tagging.md "table-bucket-tagging.md").

## Permissions

To add a tag to a table bucket, you must have the following permission:

- `s3tables:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to add a tag to a table bucket, you can do the following:

- Verify that you have the required [Permissions](#table-bucket-tag-add-permissions "#table-bucket-tag-add-permissions") to add a tag to a table bucket.
- If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again.
- The tag key is required. Also, make sure that the tag key and the tag value do not exceed the maximum character length and do not contain restricted characters. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

## Steps

You can add tags to table buckets by using the Amazon S3 Console, the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and the AWS SDKs.

To add tags to a table bucket using the Amazon S3 console:

1. Sign in to the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose the table bucket name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and choose **Add new Tag**.
6. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs.
7. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.
8. You can also edit the values of existing tags on this page.
9. After you have added the tag(s), choose **Save changes**.
   For information about the Amazon S3 REST API support for adding tags to a table bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [TagResource](../API/API_s3Buckets_TagResource.md "../API/API_s3Buckets_TagResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to add tags to a table bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws --region `us-west-2` \
s3tables tag-resource \
--resource-arn arn:aws::s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket` \
--tags '{"`Department`":"`Engineering`"}'
```
