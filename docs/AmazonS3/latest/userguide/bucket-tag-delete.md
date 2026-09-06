

# Deleting a tag from a bucket
<a name="bucket-tag-delete"></a>

You can remove tags from S3 buckets. An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 buckets. For more information about tags, see [Using tags with S3 general purpose buckets](buckets-tagging.md).

**Note**  
If you delete a tag and later learn that it was being used to track costs or for access control, you can add the tag back to the bucket. 

## Permissions
<a name="bucket-tag-delete-permissions"></a>

To delete a tag from a bucket, you must have the following permission: 
+ `s3:UntagResource`

## Troubleshooting errors
<a name="bucket-tag-delete-troubleshooting"></a>

If you encounter an error when attempting to delete a tag from a bucket, you can do the following: 
+ Verify that you have the required [Permissions](#bucket-tag-delete-permissions) to delete a tag from a bucket.

## Steps
<a name="bucket-tag-delete-steps"></a>

You can delete tags from buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

## Using the S3 console
<a name="bucket-tag-delete-console"></a>

To delete tags from a bucket using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **buckets**.

1. Choose the bucket name. 

1. Choose the **Properties** tab. 

1. Scroll to the **Tags** section and select the checkbox next to the tag or tags that you would like to delete. 

1. Choose **Delete**. 

1. The **Delete user-defined tags** pop-up appears and asks you to confirm the deletion of the tag or tags you selected. 

1. Choose **Delete** to confirm.

## Using the AWS SDKs
<a name="bucket-tag-delete-sdks"></a>

------
#### [ SDK for Java 2.x ]

This example shows you how to delete tags from a general purpose bucket by using the AWS SDK for Java 2.x. To use the command replace the {{user input placeholders}} with your own information. 

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

------

## Using the REST API
<a name="bucket-tag-delete-api"></a>

For information about the Amazon S3 REST API support for deleting tags from a general purpose bucket, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [UnTagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)

## Using the AWS CLI
<a name="bucket-tag-delete-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to delete tags from a general purpose bucket by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

**Request:**

```
aws s3control untag-resource \
--resource-arn arn:aws::s3:::{{amzn-s3-demo-bucket}} --region {{us-east-2}} --account-id {{111122223333}} \
--tag-keys "{{tagkey1}}" "{{tagkey2}}"
```