# Creating general purpose buckets with tags

You can tag Amazon S3 general purpose buckets when you create them. There is no additional charge for using tags on buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information about tagging buckets, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").

## Permissions

To create a bucket with tags, you must have the following permissions:

- `s3:CreateBucket`
- `s3:TagResource`

Amazon S3 Console and CloudFormation now use this capability to create buckets with tags.

## Troubleshooting errors

If you encounter an error when attempting to create a bucket with tags, you can do the following:

- Verify that you have the required [Permissions](#bucket-create-tag-permissions "#bucket-create-tag-permissions") to create the bucket and add a tag to it.
- Check your IAM policy for `aws:TagKeys` or `aws:RequestTag/key-name` condition keys. You might be required to label your buckets only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

###### Note

Amazon S3 and CloudFormation now use this capability to create buckets with tags. When creating buckets with tags, note that tag-based conditions to access your bucket using `aws:ResourceTag` and `s3:BucketTag` condition keys are applicable only after you enable ABAC on the bucket. To learn more, see [Enabling ABAC in general purpose buckets](buckets-tagging-enable-abac.md "buckets-tagging-enable-abac.md").

## Steps

You can create a bucket with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To create a bucket with tags using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **buckets**.
3. Choose **create bucket** to create a new bucket.
4. Create a bucket a general purpose bucket as you normally would; see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").
5. On the **Create bucket** page, **Tags** is an option when creating a new bucket.
6. Enter a name for the bucket. For more information, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").
7. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional.
8. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.
9. After you complete specifying the options for your new bucket, choose **Create bucket**.

SDK for Java 2.x
This example shows you how to create a general purpose bucket with tags by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.BucketLocationConstraint;
import software.amazon.awssdk.services.s3.model.CreateBucketConfiguration;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateBucketResponse;
import software.amazon.awssdk.services.s3.model.Tag;

public class CreateBucketWithTagsExample {
    public static void createBucketWithTagsExample() {
        S3Client s3 = S3Client.builder().region(Region.US_WEST_2).build();

        CreateBucketConfiguration bucketConfiguration = CreateBucketConfiguration.builder()
                .locationConstraint(BucketLocationConstraint.US_WEST_2)
                .tags(Tag.builder().key("MyTagKey").value("MyTagValue").build())
                .build();

        CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
                .bucket("mybucket")
                .createBucketConfiguration(bucketConfiguration)
                .build();

        CreateBucketResponse response = s3.createBucket(createBucketRequest);
        System.out.println("Status code (should be 200):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}
```

For information about the Amazon S3 REST API support for creating a general purpose bucket with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create a bucket with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

When you create a bucket, you must provide configuration details and use the following
naming convention: `amzn-s3-demo-bucket`

**Request:**

```
aws s3api create-bucket \
--bucket `mybucket` \
--create-bucket-configuration 'LocationConstraint=us-west-2,Tags=[{Key=`MyTagKey`,Value=`MyTagValue`}]' --region us-west-2"

```

**Response:**

```
{
  "Location": "http://`mybucket`s3.amazonaws.com/"
}

```
