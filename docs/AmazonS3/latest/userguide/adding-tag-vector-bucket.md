

# Adding a tag to a vector bucket
<a name="adding-tag-vector-bucket"></a>

You can add tags to Amazon S3 vector buckets and modify these tags. There is no additional charge for using tags on vector buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). For more information about tagging vector buckets, see [Using tags with S3 vector buckets](s3-vectors-tags.md).

## Permissions
<a name="add-bucket-tag-permissions"></a>

To add a tag to a vector bucket, you must have the following permission:
+ `s3vectors:TagResource`

## Troubleshooting errors
<a name="add-bucket-tag-troubleshooting"></a>

If you encounter an error when attempting to add a tag to a vector bucket, you can do the following:
+ Verify that you have the required [Permissions](#add-bucket-tag-permissions) to add a tag to a vector bucket.
+ If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again.

## Steps
<a name="add-bucket-tag-steps"></a>

You can add tags to vector buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWSSDKs.

### Using the S3 console
<a name="add-bucket-tag-console"></a>

**To add tags to a vector bucket using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **vector buckets**.

1. Choose the vector bucket name.

1. Choose the **Properties** tab.

1. Scroll to the **Tags** section and choose **Add new Tag**.

1. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs.

1. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.

1. You can also edit the values of existing tags on this page.

1. After you have added the tag(s), choose **Save changes**.

### Using the REST API
<a name="add-bucket-tag-api"></a>

For information about the Amazon S3 REST API support for adding tags to a vector bucket, see the following section in the *Amazon S3 Vectors API Reference*:

[TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_TagResource.html)

### Using the AWS CLI
<a name="add-bucket-tag-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to add tags to a vector bucket by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

```
aws s3vectors tag-resource \
--resource-arn arn:aws:s3vectors:us-east-1:{{012345678900}}:bucket/{{acc-bucket}} \
--tags {{Stage}}={{Prod}},{{CostCenter}}={{Marketing}}
```