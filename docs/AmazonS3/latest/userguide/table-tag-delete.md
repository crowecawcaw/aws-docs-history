

# Deleting a tag from a table
<a name="table-tag-delete"></a>

You can remove tags from Amazon S3 tables. For more information about tagging tables, see [Using tags with S3 tables](table-tagging.md).

**Note**  
If you delete a tag and later learn that it was being used to track costs or for access control, you can add the tag back to the table. 

## Permissions
<a name="table-tag-delete-permissions"></a>

To delete a tag from a table, you must have the following permission: 
+ `s3tables:UntagResource`

## Troubleshooting errors
<a name="table-tag-delete-troubleshooting"></a>

If you encounter an error when attempting to delete a tag from a table, you can do the following: 
+ Verify that you have the required [Permissions](#table-tag-delete-permissions) to delete a tag from a table.

## Steps
<a name="table-tag-delete-steps"></a>

You can delete tags from tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 Tables REST API, and AWS SDKs.

## Using the S3 console
<a name="table-tag-delete-console"></a>

To delete tags from a table using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. Choose the table bucket name. 

1. Choose the table name. 

1. Choose the **Properties** tab. 

1. Scroll to the **Tags** section and select the checkbox next to the tag or tags that you would like to delete. 

1. Choose **Delete**. 

1. The **Delete user-defined tags** pop-up appears and asks you to confirm the deletion of the tag or tags you selected. 

1. Choose **Delete** to confirm.

## Using the REST API
<a name="table-tag-delete-api"></a>

For information about the Amazon S3 REST API support for deleting tags from a table, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [UnTagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_UntagResource.html)

## Using the AWS CLI
<a name="table-tag-delete-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to delete tags from a table by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

**Request:**

```
aws --region {{us-west-2}} \ 
s3tables untag-resource \
--resource-arn arn:aws::s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/{{my_example_table}} \
--tag-keys '["department"]'
```