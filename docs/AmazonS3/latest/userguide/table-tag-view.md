# Viewing table tags

You can view or list tags applied to Amazon S3 tables. For more information about tags, see [Using tags with S3 tables](table-tagging.md "table-tagging.md").

## Permissions

To view tags applied to a table, you must have the following permission:

- `s3tables:ListTagsForResource`

## Troubleshooting errors

If you encounter an error when attempting to list or view the tags of a table, you can do the following:

- Verify that you have the required [Permissions](#table-tag-view-permissions "#table-tag-view-permissions") to view or list the tags of the table.

## Steps

You can view tags applied to tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To view tags applied to a table using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose the Table bucket name.
4. Choose the table name within the Table bucket.
5. Choose the **Properties** tab.
6. Scroll to the **Tags** section to view all of the tags applied to the table.
7. The **Tags** section shows the **User-defined tags** by default. You can select the **AWS-generated tags** tab to view tags applied to your table by AWS services.
   For information about the Amazon S3 REST API support for viewing the tags applied to a table, see the following section in the _Amazon Simple Storage Service API Reference_:

- [ListTagsforResource](../API/API_s3Buckets_ListTagsForResource.md "../API/API_s3Buckets_ListTagsForResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to view tags applied to a table. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws --region `us-west-2` \
s3tables list-tags-for-resource \
--resource-arn arn:aws::s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`my_example_table`

```
