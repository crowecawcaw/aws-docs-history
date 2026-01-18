# Deleting a tag from a vector index

You can remove tags from S3 vector indexes. An AWS tag is a key-value pair that holds
metadata about resources, in this case Amazon S3 vector indexes. For more information about
tagging vector indexes, see [Using tags with S3 vector indexes](vector-index-tagging.md "vector-index-tagging.md").

###### Note

If you delete a tag and later learn that it was being used to track costs or for
access control, you can add the tag back to the vector index.

## Permissions

To delete a tag from a vector index, you must have the following permission:

- `s3vectors:UntagResource`

## Troubleshooting errors

If you encounter an error when attempting to delete a tag from a vector index, you can
do the following:

- Verify that you have the required [Permissions](#delete-index-tag-permissions "#delete-index-tag-permissions") to delete a tag from a vector index.

## Steps

You can delete tags from vector indexes by using the Amazon S3 console, the AWS Command Line Interface
(AWS CLI), the Amazon S3 REST API, and AWS SDKs.

###### To delete tags from a vector index using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **vector indexes**.
3. Choose the vector index name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and select the checkbox next to
   the tag or tags that you would like to delete.
6. Choose **Delete**.
7. The **Delete user-defined tags** pop-up appears and asks you to
   confirm the deletion of the tag or tags you selected.
8. Choose **Delete** to confirm.

For information about the Amazon S3 REST API support for deleting tags from a vector
index, see the following section in the _Amazon S3 Vectors API
Reference_:

[UntagResource](../API/API_S3VectorBuckets_UntagResource.md "../API/API_S3VectorBuckets_UntagResource.md")

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to delete tags from a vector index by using
the AWS CLI. To use the command replace the `user input
 placeholders` with your own information.

```
aws s3vectors untag-resource \
--resource-arn arn:aws:s3vectors:us-east-1:`012345678900`:bucket/`acc-bucket`/index/`accounts-index` \
--tag-keys `CostCenter` `Department`
```
