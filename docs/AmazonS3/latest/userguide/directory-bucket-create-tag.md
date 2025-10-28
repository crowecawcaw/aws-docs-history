# Creating directory buckets with tags

You can tag Amazon S3 directory buckets when you create them. There is no additional charge for using tags on directory buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information about tagging directory buckets, see [Using tags with S3 directory buckets](directory-buckets-tagging.md "directory-buckets-tagging.md").

## Permissions

To create a directory bucket with tags, you must have the following permissions:

- `s3express:CreateBucket`
- `s3express:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create a directory bucket with tags, you can do the following:

- Verify that you have the required [Permissions](#create-tag-permissions "#create-tag-permissions") to create the directory bucket and add a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC) conditions. You may be required to label your directory buckets only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

## Steps

You can create a directory bucket with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To create a directory bucket with tags using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **directory buckets**.
3. Choose **create bucket** to create a new directory bucket.
4. You can create two types of directory buckets:

Create a directory bucket in an Availability Zone for a high performance workload. For more information, see [High performance workloads](directory-bucket-high-performance.md "directory-bucket-high-performance.md").

Create a directory bucket in a Local Zone for a data residency workload. For more information, see [Data residency workloads](directory-bucket-data-residency.md "directory-bucket-data-residency.md"). 5. For both types of directory buckets, on the **Create bucket** page, **Tags** is an option when creating a new directory bucket. 6. Enter a name for the bucket. For more information, see [Directory bucket naming rules](directory-bucket-naming-rules.md "directory-bucket-naming-rules.md"). 7. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional. 8. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs. 9. After you complete specifying the options for your new directory bucket, choose **Create bucket**.

SDK for Java 2.x
This example shows you how to create a directory bucket with tags by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.BucketInfo;
import software.amazon.awssdk.services.s3.model.BucketType;
import software.amazon.awssdk.services.s3.model.CreateBucketConfiguration;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateBucketResponse;
import software.amazon.awssdk.services.s3.model.DataRedundancy;
import software.amazon.awssdk.services.s3.model.LocationInfo;
import software.amazon.awssdk.services.s3.model.LocationType;
import software.amazon.awssdk.services.s3.model.Tag;

public class CreateBucketWithTagsExample {
    public static void createBucketWithTagsExample() {
        S3Client s3 = S3Client.builder().region(Region.`US_WEST_2`).build();

        CreateBucketConfiguration bucketConfiguration = CreateBucketConfiguration.builder()
                .location(LocationInfo.builder()
                        .type(LocationType.AVAILABILITY_ZONE)
                        .name("`usw2-az1`").build())
                .bucket(BucketInfo.builder()
                        .type(BucketType.DIRECTORY)
                        .dataRedundancy(DataRedundancy.SINGLE_AVAILABILITY_ZONE)
                        .build())
                .tags(Tag.builder().key("`MyTagKey`").value("`MyTagValue`").build())
                .build();

        CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
                .bucket("`amzn-s3-demo-bucket--usw2-az1--x-s3`--`usw2-az1`--x-s3")
                .createBucketConfiguration(bucketConfiguration)
                .build();

        CreateBucketResponse response = s3.createBucket(createBucketRequest);
        System.out.println("Status code (should be 200):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}

```

For information about the Amazon S3 REST API support for creating a directory bucket with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create a directory bucket with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

When you create a directory bucket you must provide configuration details and use the following naming convention:
``bucket-base-name`--`zone-id`--x-s3`

**Request:**

```
aws s3api create-bucket \
--bucket ``bucket-base-name`--`zone-id`--x-s3` \
--create-bucket-configuration "Location={Type=AvailabilityZone,Name=`zone-id`},Bucket={DataRedundancy=SingleAvailabilityZone,Type=Directory},Tags=[{Key=`mykey1`,Value=`myvalue1`}, {Key=`mykey2`,Value=`myvalue2`}]"

```

**Response:**

```
{
  "Location": "http://bucket--`use1-az4`--x-s3.s3express-`use1-az4`.`us-east-1`.amazonaws.com/"
}

```
