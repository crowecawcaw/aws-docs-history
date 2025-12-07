# Viewing bucket tags

You can view or list tags applied to S3 buckets. For more information about tags, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").

## Permissions

To view tags applied to a bucket, you must have the following permission:

- `s3:ListTagsForResource`

## Troubleshooting errors

If you encounter an error when attempting to list or view the tags of a bucket, you can do the following:

- Verify that you have the required [Permissions](#bucket-tag-view-permissions "#bucket-tag-view-permissions") to view or list the tags of the bucket.

## Steps

You can view tags applied to buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To view tags applied to a bucket using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **buckets**.
3. Choose the bucket name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section to view all of the tags applied to the general purpose bucket.
6. The **Tags** section shows the **User-defined tags** by default. You can select the **AWS-generated tags** tab to view tags applied to your bucket by AWS services.
   This section provides an example of how to view tags applied to a general purpose bucket by using the AWS SDKs.

SDK for Java 2.x
This example shows you how to view tags applied to a general purpose bucket by using the AWS SDK for Java 2.x.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceResponse;

public class ListTagsForResourceExample {
    public static void listTagsForResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.US_WEST_2).build();

        ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                .resourceArn("arn:aws::s3:::bucket/my-bucket")
                .accountId("111122223333")
                .build();

        ListTagsForResourceResponse response = s3Control.listTagsForResource(listTagsForResourceRequest);
        System.out.println("Tags on my resource:");
        System.out.println(response.toString());
    }
}
```

For information about the Amazon S3 REST API support for viewing the tags applied to a general purpose bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [ListTagsforResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to view tags applied to a bucket. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws s3control list-tags-for-resource \
--account-id `111122223333` \
--resource-arn arn:aws::s3:`us-east-1`:`444455556666`:bucket/prefix--`use1-az4`--x-s3 \

```

**Response - tags present:**

```
{
  "Tags": [
      {
          "Key": "`MyKey1`",
          "Value": "`MyValue1`"
      },
      {
          "Key": "`MyKey2`",
          "Value": "`MyValue2`"
      },
      {
          "Key": "`MyKey3`",
          "Value": "`MyValue3`"
      }
  ]
}

```

**Response - no tags present:**

```
{
  "Tags": []
}

```
