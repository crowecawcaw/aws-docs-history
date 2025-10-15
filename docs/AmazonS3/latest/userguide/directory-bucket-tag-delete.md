# Deleting a tag from a directory bucket

You can remove tags from S3 directory buckets. An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 directory buckets. For more information about tags, see [Using tags with S3 directory buckets](directory-buckets-tagging.md "directory-buckets-tagging.md").

###### Note

If you delete a tag and later learn that it was being used to track costs or for access control, you can add the tag back to the directory bucket. 


## Permissions


To delete a tag from a directory bucket, you must have the following permission: 



* `s3express:UntagResource`

## Troubleshooting errors


If you encounter an error when attempting to delete a tag from a directory bucket, you can do the following: 



* Verify that you have the required [Permissions](#tag-delete-permissions "#tag-delete-permissions") to delete a tag from a directory bucket.

## Steps


You can delete tags from directory buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.


To delete tags from a directory bucket using the Amazon S3 console:


1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **directory buckets**.
3. Choose the bucket name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and select the checkbox next to the tag or tags that you would like to delete.
6. Choose **Delete**.
7. The **Delete user-defined tags** pop-up appears and asks you to confirm the deletion of the tag or tags you selected.
8. Choose **Delete** to confirm.

SDK for Java 2.x
This example shows you how to delete tags from a directory bucket by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information. 



```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.UntagResourceRequest;
import software.amazon.awssdk.services.s3control.model.UntagResourceResponse;

public class UntagResourceExample {
    public static void untagResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.`US_WEST_2`).build();

        UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                .resourceArn("arn:aws::s3express:`us-west-2`:`111122223333`:bucket/my-directory-bucket--`usw2-az1`--x-s3")
                .accountId("`111122223333`")
                .tagKeys("`myTagKey`")
                .build();

        UntagResourceResponse response = s3Control.untagResource(untagResourceRequest);
        System.out.println("Status code (should be 204):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}

```


For information about the Amazon S3 REST API support for deleting tags from a directory bucket, see the following section in the *Amazon Simple Storage Service API Reference*:


* [UnTagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md")
To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to delete tags from a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**


```
aws s3control untag-resource \
--account-id `111122223333` \
--resource-arn arn:aws::s3express:`us-east-1`:`444455556666`:bucket/prefix--`use1-az4`--x-s3 \
--tag-keys "`tagkey1`" "`tagkey2`"

```
**Response:**


```
{
  "ResponseMetadata": {
    "RequestId": "EXAMPLE123456789",
    "HTTPStatusCode": 204,
    "HTTPHeaders": {
        "date": "Wed, 19 Jun 2025 10:30:00 GMT",
        "content-length": "0"
    },
    "RetryAttempts": 0
  }
}

```
