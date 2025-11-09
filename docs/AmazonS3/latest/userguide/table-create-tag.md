# Creating tables with tags

You can tag Amazon S3 tables when you create them. There is no additional charge for using tags on tables beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). For more information about tagging tables, see [Using tags with S3 tables](table-tagging.md "table-tagging.md").

## Permissions

To create a table with tags, you must have the following permissions:

- `s3tables:CreateTable`
- `s3tables:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create a table with tags, you can do the following:

- Verify that you have the required [Permissions](#table-create-tag-permissions "#table-create-tag-permissions") to create the table and apply a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC) conditions. Your policy may require you to tag your tables with only specific tag keys and values. For more information about ABAC and example table ABAC policies, see [ABAC for S3 tables](table-tagging.md#abac-for-tables "table-tagging.md#abac-for-tables").

## Steps

You can create a table with tags applied by using the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and the AWS SDKs.

For information about the Amazon S3 Tables REST API support for creating a table with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateTable](../API/API_s3Buckets_CreateTable.md "../API/API_s3Buckets_CreateTable.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create a table with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

When you create a table you must provide configuration details. For more information, see [Creating an Amazon S3 table](s3-tables-create.md "s3-tables-create.md"). You must also name the table with a name that follows the table naming convention. For more information see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md "s3-tables-buckets-naming.md").

**Request:**

```
aws --region `us-west-2` \
s3tables create-table \
--endpoint `https://ufwae60e2k.execute-api.us-west-2.amazonaws.com/personal/` \
--table-bucket-arn arn:aws:s3tables:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`
--tags '{"`Department`":"`Engineering`"}' \
--name `my_table_abc` \
--namespace `my_namesapce_123a` \
--format ICEBERG
```
