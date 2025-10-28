# Adding a tag to a directory bucket

You can add tags to Amazon S3 directory buckets and modify these tags. There is no additional charge for using tags on directory buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information about tagging directory buckets, see [Using tags with S3 directory buckets](directory-buckets-tagging.md "directory-buckets-tagging.md").

## Permissions

To add a tag to a directory bucket, you must have the following permission:

- `s3express:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to add a tag to a directory bucket, you can do the following:

- Verify that you have the required [Permissions](#tag-add-permissions "#tag-add-permissions") to add a tag to a directory bucket.
- If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again.

## Steps

You can add tags to directory buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To add tags to a directory bucket using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **directory buckets**.
3. Choose the bucket name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and choose **Add new Tag**.
6. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs.
7. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.
8. You can also edit the values of existing tags on this page.
9. After you have added the tag(s), choose **Save changes**.

SDK for Java 2.x
This example shows you how to add tags to a directory bucket by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.Tag;
import software.amazon.awssdk.services.s3control.model.TagResourceRequest;
import software.amazon.awssdk.services.s3control.model.TagResourceResponse;

public class TagResourceExample {
    public static void tagResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.`US_WEST_2`).build();

        TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                .resourceArn("arn:aws::s3express:`us-west-2`:111122223333:bucket/my-directory-bucket--`usw2-az1`--x-s3")
                .accountId("111122223333")
                .tags(Tag.builder().key("`MyTagKey`").value("`MyTagValue`").build())
                .build();

        TagResourceResponse response = s3Control.tagResource(tagResourceRequest);
        System.out.println("Status code (should be 204):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}

```

For information about the Amazon S3 REST API support for adding tags to a directory bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to add tags to a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws s3control tag-resource \
--account-id `111122223333` \
--resource-arn arn:aws::s3express:`us-east-1`:`444455556666`:bucket/prefix--`use1-az4`--x-s3 \
--tags "Key=`mykey`,Value=`myvalue`"

```

**Response:**

```
{
  "ResponseMetadata": {
      "RequestId": "EXAMPLE123456789",
      "HTTPStatusCode": 200,
      "HTTPHeaders": {
          "date": "Wed, 19 Jun 2025 10:30:00 GMT",
          "content-length": "0"
      },
      "RetryAttempts": 0
  }
}

```
