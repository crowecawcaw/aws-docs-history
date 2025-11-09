# Creating table buckets with tags

You can tag Amazon S3 table buckets when you create them. There is no additional charge for using tags on table buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information about tagging table buckets, see [Using tags with S3 table buckets](table-bucket-tagging.md "table-bucket-tagging.md").

## Permissions

To create a table bucket with tags, you must have the following permissions:

- `s3tables:CreateTableBucket`
- `s3tables:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create a table bucket with tags, you can do the following:

- Verify that you have the required [Permissions](#table-bucket-create-tag-permissions "#table-bucket-create-tag-permissions") to create the table bucket and apply a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC) conditions. Your policy may require you to tag your table buckets with only specific tag keys and values. For more information about ABAC and example table bucket ABAC policies, see [ABAC for S3 table buckets](table-bucket-tagging.md#abac-for-table-buckets "table-bucket-tagging.md#abac-for-table-buckets").

## Steps

You can create a table bucket with tags applied by using the Amazon S3 Console, the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and the AWS SDKs.

To create a table bucket with tags using the Amazon S3 console:

1. Sign in to the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. To create a new table bucket, choose **Create table bucket**.
4. Enter a name for the table bucket. For more information, see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md").
5. On the **Create table bucket** page, there is a **Tags** section.
6. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional.
7. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.
8. Specify the remaining options for your new table bucket. For more information, see [Creating a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md").
9. Choose **Create table bucket**.
   For information about the Amazon S3 Tables REST API support for creating a table bucket with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateTableBucket](../API/API_s3Buckets_CreateTableBucket.md "../API/API_s3Buckets_CreateTableBucket.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create a table bucket with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

When you create a table bucket you must provide configuration details. For more information, see [Creating a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md"). You must also name the table bucket with a name that follows the table bucket naming convention. For more information see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md").

**Request:**

```
aws --region `us-west-2` \
s3tables create-table-bucket \
--tags '{"`Department`":"`Engineering`"}' \
--name `amzn-s3-demo-table-bucket`
```
