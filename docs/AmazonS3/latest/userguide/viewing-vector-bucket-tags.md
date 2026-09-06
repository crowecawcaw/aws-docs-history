

# Viewing vector bucket tags
<a name="viewing-vector-bucket-tags"></a>

You can view or list tags applied to Amazon S3 vector buckets. For more information about tagging vector buckets, see [Using tags with S3 vector buckets](s3-vectors-tags.md).

## Permissions
<a name="view-bucket-tag-permissions"></a>

To view tags applied to a vector bucket, you must have the following permission:
+ `s3vectors:ListTagsForResource`

## Troubleshooting errors
<a name="view-bucket-tag-troubleshooting"></a>

If you encounter an error when attempting to list or view the tags of a vector bucket, you can do the following:
+ Verify that you have the required [Permissions](#view-bucket-tag-permissions) to view or list the tags of the vector bucket.

## Steps
<a name="view-bucket-tag-steps"></a>

You can view tags applied to vector buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

### Using the S3 console
<a name="view-bucket-tag-console"></a>

**To view tags applied to a vector bucket using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **vector buckets**.

1. Choose the vector bucket name.

1. Choose the **Properties** tab.

1. Scroll to the **Tags** section to view all of the tags applied to the vector bucket.

1. The **Tags** section shows the User-defined tags by default. You can select the AWS-generated tags tab to view tags applied to your vector bucket by AWS services.

### Using the REST API
<a name="view-bucket-tag-api"></a>

For information about the Amazon S3 REST API support for viewing the tags applied to a vector bucket, see the following section in the Amazon Simple Vectors API Reference:

[ListTagsforResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListTagsForResource.html)

### Using the AWS CLI
<a name="view-bucket-tag-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to view tags applied to a vector bucket. To use the command replace the {{user input placeholders}} with your own information.

```
aws s3vectors list-tags-for-resource \ 
--resource-arn arn:aws:s3vectors:us-east-1:012345678900:bucket/acc-bucket
```