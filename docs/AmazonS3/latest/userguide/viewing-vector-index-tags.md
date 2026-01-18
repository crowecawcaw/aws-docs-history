# Viewing vector index tags

You can view or list tags applied to Amazon S3 vector indexes. For more information about
tagging vector indexes, see [Using tags with S3 vector indexes](vector-index-tagging.md "vector-index-tagging.md").

## Permissions

To view tags applied to a vector index, you must have the following permission:

- `s3vectors:ListTagsForResource`

## Troubleshooting errors

If you encounter an error when attempting to list or view the tags of a vector index,
you can do the following:

- Verify that you have the required [Permissions](#view-index-tag-permissions "#view-index-tag-permissions") to view or list the tags of the vector index.

## Steps

You can view tags applied to vector indexes by using the Amazon S3 console, the
AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

###### To view tags applied to a vector index using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **vector indexes**.
3. Choose the vector index name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section to view all of the tags applied
   to the vector index.
6. The **Tags** section shows the User-defined tags by default.
   You can select the AWS-generated tags tab to view tags applied to your vector
   index by AWS services.

For information about the Amazon S3 REST API support for viewing the tags applied to
a vector index, see the following section in the Amazon Simple Vectors API
Reference:

[ListTagsforResource](../API/API_S3VectorBuckets_ListTagsForResource.md "../API/API_S3VectorBuckets_ListTagsForResource.md")

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to view tags applied to a vector index. To
use the command replace the `user input placeholders` with
your own information.

```
aws s3vectors list-tags-for-resource \
  --resource-arn arn:aws:s3vectors:us-east-1:012345678900:bucket/`acc-bucket`/index/`accounts-index`
```
