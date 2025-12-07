# Deleting a tag from a bucket

You can remove tags from S3 buckets. An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 buckets. For more information about tags, see [Using tags with S3 general purpose buckets](buckets-tagging.md "buckets-tagging.md").

###### Note

If you delete a tag and later learn that it was being used to track costs or for access control, you can add the tag back to the bucket.

## Permissions

To delete a tag from a bucket, you must have the following permission:

- `s3:UntagResource`

## Troubleshooting errors

If you encounter an error when attempting to delete a tag from a bucket, you can do the following:

- Verify that you have the required [Permissions](#bucket-tag-delete-permissions "#bucket-tag-delete-permissions") to delete a tag from a bucket.

## Steps

You can delete tags from buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To delete tags from a bucket using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **buckets**.
3. Choose the bucket name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and select the checkbox next to the tag or tags that you would like to delete.
6. Choose **Delete**.
7. The **Delete user-defined tags** pop-up appears and asks you to confirm the deletion of the tag or tags you selected.
8. Choose **Delete** to confirm.

SDK for Java 2.x
This example shows you how to delete tags from a general purpose bucket by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.UntagResourceRequest;
import software.amazon.awssdk.services.s3control.model.UntagResourceResponse;

public class UntagResourceExample {
    public static void untagResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.US_WEST_2).build();

        UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                .resourceArn("arn:aws::s3:::bucket/my-bucket")
                .accountId("111122223333")
                .tagKeys("myTagKey")
                .build();

        UntagResourceResponse response = s3Control.untagResource(untagResourceRequest);
        System.out.println("Status code (should be 204):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}
```

For information about the Amazon S3 REST API support for deleting tags from a general purpose bucket, see the following section in the _Amazon Simple Storage Service API Reference_:

- [UnTagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to delete tags from a general purpose bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws s3control untag-resource \
--resource-arn arn:aws::s3:::`amzn-s3-demo-bucket` --region `us-east-2` --account-id `111122223333` \
--tag-keys "`tagkey1`" "`tagkey2`"
```
