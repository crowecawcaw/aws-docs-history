# Adding a tag to a table

You can add tags to Amazon S3 tables and modify these tags. For more information about tagging tables, see [Using tags with S3 tables](table-tagging.md "table-tagging.md").

## Permissions

To add a tag to a table, you must have the following permission:

- `s3tables:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to add a tag to a table, you can do the following:

- Verify that you have the required [Permissions](#table-tag-add-permissions "#table-tag-add-permissions") to add a tag to a table.
- If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again.
- The tag key is required. Also, make sure that the tag key and the tag value do not exceed the maximum character length and do not contain restricted characters. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

## Steps

You can add tags to tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and AWS SDKs.

To add tags to a table using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose the table bucket name.
4. Choose the table name.
5. Choose the **Properties** tab.
6. Scroll to the **Tags** section and choose **Add new Tag**.
7. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs.
8. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.
9. You can also edit the values of existing tags on this page.
10. After you have added the tag(s), choose **Save changes**.
    For information about the Amazon S3 REST API support for adding tags to a table, see the following section in the _Amazon Simple Storage Service API Reference_:

- [TagResource](../API/API_s3Buckets_TagResource.md "../API/API_s3Buckets_TagResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to add tags to a table by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws --region `us-west-2` \
s3tables tag-resource \
--resource-arn arn:aws::s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`my_example_table` \
--tags '{"Department":"engineering"}'
```
