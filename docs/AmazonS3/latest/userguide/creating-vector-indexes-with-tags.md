# Creating vector indexes with tags

You can tag Amazon S3 vector indexes when you create them. There is no additional charge for
using tags on vector indexes beyond the standard S3 API request rates. For more information,
see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information
about tagging vector indexes, see [Using tags with S3 vector indexes](vector-index-tagging.md "vector-index-tagging.md").

## Permissions

To create a vector index with tags, you must have the following permissions:

- `s3vectors:CreateIndex`
- `s3vectors:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create a vector index with tags, you can
do the following:

- Verify that you have the required [Permissions](#index-tags-permissions "#index-tags-permissions") to create the vector index and add a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC)
  conditions. You may be required to label your vector indexes only with specific tag
  keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

## Steps

You can create a vector index with tags applied by using the Amazon S3 console, the
AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

###### To create a vector index with tags using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **vector indexes**.
3. Choose **create vector index** to create a new vector
   index.
4. Create a vector index as you normally would; see [Creating a vector index in a vector bucket](s3-vectors-create-index.md "s3-vectors-create-index.md").
5. On the **Create vector index** page, **Tags**
   is an option when creating a new vector index.
6. Enter a name for the vector index.
7. Choose **Add new Tag** to open the Tags editor and enter a tag
   key-value pair. The tag key is required, but the value is optional.
8. To add another tag, select **Add new Tag** again. You can enter
   up to 50 tag key-value pairs.
9. After you complete specifying the options for your new vector index, choose
   **Create vector index**.

For information about the Amazon S3 REST API support for creating a vector index
with tags, see the following section in the _Amazon S3 Vectors
API Reference_:

[CreateIndex](../API/API_S3VectorBuckets_CreateIndex.md "../API/API_S3VectorBuckets_CreateIndex.md")

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create a vector index with tags by using
the AWS CLI. To use the command replace the `user input
 placeholders` with your own information.

When you create a vector index you must provide configuration details and use the
following naming convention: `example-vector-index`

```
aws s3vectors create-index --vector-bucket-name `acc-bucket` --data-type "float32" \
 --index-name `accounts-index` --dimension 1024 --distance-metric euclidean \
 --tags `Department`=`Accounting`,`Stage`=`Prod`
```
