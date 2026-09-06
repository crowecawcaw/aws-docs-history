

# Creating vector indexes with tags
<a name="creating-vector-indexes-with-tags"></a>

You can tag Amazon S3 vector indexes when you create them. There is no additional charge for using tags on vector indexes beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). For more information about tagging vector indexes, see [Using tags with S3 vector indexes](vector-index-tagging.md).

## Permissions
<a name="index-tags-permissions"></a>

To create a vector index with tags, you must have the following permissions:
+ `s3vectors:CreateIndex`
+ `s3vectors:TagResource`

## Troubleshooting errors
<a name="index-tags-troubleshooting"></a>

If you encounter an error when attempting to create a vector index with tags, you can do the following:
+ Verify that you have the required [Permissions](#index-tags-permissions) to create the vector index and add a tag to it.
+ Check your IAM user policy for any attribute-based access control (ABAC) conditions. You may be required to label your vector indexes only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac).

## Steps
<a name="index-tags-steps"></a>

You can create a vector index with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

### Using the S3 console
<a name="index-tags-console"></a>

**To create a vector index with tags using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **vector indexes**.

1. Choose **create vector index** to create a new vector index.

1. Create a vector index as you normally would; see [Creating a vector index in a vector bucket](s3-vectors-create-index.md).

1. On the **Create vector index** page, **Tags** is an option when creating a new vector index.

1. Enter a name for the vector index.

1. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional.

1. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.

1. After you complete specifying the options for your new vector index, choose **Create vector index**.

### Using the REST API
<a name="index-tags-api"></a>

For information about the Amazon S3 REST API support for creating a vector index with tags, see the following section in the *Amazon S3 Vectors API Reference*:

[CreateIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateIndex.html)

### Using the AWS CLI
<a name="index-tags-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to create a vector index with tags by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

When you create a vector index you must provide configuration details and use the following naming convention: `example-vector-index`

```
aws s3vectors create-index --vector-bucket-name {{acc-bucket}} --data-type "float32" \
 --index-name {{accounts-index}} --dimension 1024 --distance-metric euclidean \
 --tags {{Department}}={{Accounting}},{{Stage}}={{Prod}}
```