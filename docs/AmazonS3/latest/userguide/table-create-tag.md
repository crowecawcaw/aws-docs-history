

# Creating tables with tags
<a name="table-create-tag"></a>

You can tag Amazon S3 tables when you create them. There is no additional charge for using tags on tables beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). For more information about tagging tables, see [Using tags with S3 tables](table-tagging.md).

## Permissions
<a name="table-create-tag-permissions"></a>

To create a table with tags, you must have the following permissions:
+ `s3tables:CreateTable`
+ `s3tables:TagResource`

## Troubleshooting errors
<a name="table-create-tag-troubleshooting"></a>

If you encounter an error when attempting to create a table with tags, you can do the following: 
+ Verify that you have the required [Permissions](#table-create-tag-permissions) to create the table and apply a tag to it.
+ Check your IAM user policy for any attribute-based access control (ABAC) conditions. Your policy may require you to tag your tables with only specific tag keys and values. For more information about ABAC and example table ABAC policies, see [ABAC for S3 tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/table-tagging.html#abac-for-tables).

## Steps
<a name="table-create-tag-steps"></a>

You can create a table with tags applied by using the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and the AWS SDKs.

## Using the REST API
<a name="table-create-tag-api"></a>

For information about the Amazon S3 Tables REST API support for creating a table with tags, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html)

## Using the AWS CLI
<a name="table-create-tag-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to create a table with tags by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

When you create a table you must provide configuration details. For more information, see [Creating an Amazon S3 table](s3-tables-create.md). You must also name the table with a name that follows the table naming convention. For more information see [Amazon S3 table bucket, table, and namespace naming rules](s3-tables-buckets-naming.md). 

**Request:**

```
aws --region {{us-west-2}} \
s3tables create-table \
--endpoint {{https://ufwae60e2k.execute-api.us-west-2.amazonaws.com/personal/}} \
--table-bucket-arn arn:aws:s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}
--tags '{"{{Department}}":"{{Engineering}}"}' \
--name {{my_table_abc}} \
--namespace {{my_namesapce_123a}} \
--format ICEBERG
```