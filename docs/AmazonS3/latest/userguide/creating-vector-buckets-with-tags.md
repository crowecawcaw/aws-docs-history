

# Creating vector buckets with tags
<a name="creating-vector-buckets-with-tags"></a>

You can tag Amazon S3 vector buckets when you create them. There is no additional charge for using tags on vector buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). For more information about tagging vector buckets, see [Using tags with S3 vector buckets](s3-vectors-tags.md).

## Permissions
<a name="bucket-tags-permissions"></a>

To create a vector bucket with tags, you must have the following permissions:
+ `s3vectors:CreateVectorBucket`
+ `s3vectors:TagResource`

## Troubleshooting errors
<a name="bucket-tags-troubleshooting"></a>

If you encounter an error when attempting to create a vector bucket with tags, you can do the following:
+ Verify that you have the required [Permissions](#bucket-tags-permissions) to create the vector bucket and add a tag to it.
+ Check your IAM user policy for any attribute-based access control (ABAC) conditions. You may be required to label your vector buckets only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac).

## Steps
<a name="bucket-tags-steps"></a>

You can create a vector bucket with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

### Using the S3 console
<a name="bucket-tags-console"></a>

**To create a vector bucket with tags using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **vector buckets**.

1. Choose **create vector bucket** to create a new vector bucket.

1. Create a vector bucket as you normally would; see [Creating a vector bucket](s3-vectors-buckets-create.md).

1. On the **Create vector bucket** page, **Tags** is an option when creating a new vector bucket.

1. Enter a name for the vector bucket.

1. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional.

1. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.

1. After you complete specifying the options for your new vector bucket, choose **Create vector bucket**.

### Using the REST API
<a name="bucket-tags-api"></a>

For information about the Amazon S3 REST API support for creating a vector bucket with tags, see the following section in the *Amazon S3 Vectors API Reference*:

[CreateVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_CreateVectorBucket.html)

### Using the AWS CLI
<a name="bucket-tags-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to create a vector bucket with tags by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

When you create a vector bucket you must provide configuration details and use the following naming convention: `example-vector-bucket`

```
aws s3vector create-vector-bucket --vector-bucket-name {{acc-bucket}} \
  --tags {{Department}}={{Accounting}},{{Stage}}={{Prod}}
```