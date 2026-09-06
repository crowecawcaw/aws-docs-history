

# Viewing table tags
<a name="table-tag-view"></a>

You can view or list tags applied to Amazon S3 tables. For more information about tags, see [Using tags with S3 tables](table-tagging.md).

## Permissions
<a name="table-tag-view-permissions"></a>

To view tags applied to a table, you must have the following permission: 
+ `s3tables:ListTagsForResource`

## Troubleshooting errors
<a name="table-tag-view-troubleshooting"></a>

If you encounter an error when attempting to list or view the tags of a table, you can do the following: 
+ Verify that you have the required [Permissions](#table-tag-view-permissions) to view or list the tags of the table.

## Steps
<a name="table-tag-view-steps"></a>

You can view tags applied to tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

## Using the S3 console
<a name="table-tag-view-console"></a>

To view tags applied to a table using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. Choose the Table bucket name. 

1. Choose the table name within the Table bucket. 

1. Choose the **Properties** tab. 

1. Scroll to the **Tags** section to view all of the tags applied to the table. 

1. The **Tags** section shows the **User-defined tags** by default. You can select the **AWS-generated tags** tab to view tags applied to your table by AWS services.

## Using the REST API
<a name="table-tag-view-api"></a>

For information about the Amazon S3 REST API support for viewing the tags applied to a table, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [ListTagsforResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTagsForResource.html)

## Using the AWS CLI
<a name="table-tag-view-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to view tags applied to a table. To use the command replace the {{user input placeholders}} with your own information.

**Request:**

```
aws --region {{us-west-2}} \ 
s3tables list-tags-for-resource \
--resource-arn arn:aws::s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/{{my_example_table}}
```