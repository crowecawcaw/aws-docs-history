

# Deleting a tag from an access point for directory buckets
<a name="access-points-db-tag-delete"></a>

You can remove tags from Access Points for directory buckets. For additional information, see [Using tags with S3 Access Points for directory buckets](access-points-db-tagging.md).

**Note**  
If you delete a tag and later learn that it was being used to track costs or for access control, you can add the tag back to the access point for directory buckets. 

## Permissions
<a name="access-points-db-tag-delete-permissions"></a>

To delete a tag from an access point for directory buckets, you must have the following permission: 
+ `s3express:UntagResource`

## Troubleshooting errors
<a name="access-points-db-tag-delete-troubleshooting"></a>

If you encounter an error when attempting to delete a tag from an access point for directory buckets, you can do the following: 
+ Verify that you have the required [Permissions](#access-points-db-tag-delete-permissions) to delete a tag from an access point for directory buckets.

## Steps
<a name="access-points-db-tag-delete-steps"></a>

You can delete tags from access points for directory buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

## Using the S3 console
<a name="access-points-db-tag-delete-console"></a>

To delete tags from an access point for directory buckets using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Access Points (Directory Buckets)**.

1. Choose the access point name. 

1. Choose the **Properties** tab. 

1. Scroll to the **Tags** section and select the checkbox next to the tag or tags that you would like to delete. 

1. Choose **Delete**. 

1. The **Delete user-defined tags** pop-up appears and asks you to confirm the deletion of the tag or tags you selected. 

1. Choose **Delete** to confirm.

## Using the AWS SDKs
<a name="access-points-db-tag-delete-sdks"></a>

------
#### [ SDK for Java 2.x ]

This example shows you how to delete tags from a directory bucket by using the AWS SDK for Java 2.x. To use the command replace the {{user input placeholders}} with your own information. 

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceResponse;

public class ListTagsForResourceExample {
    public static void listTagsForResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.{{US_WEST_2}}).build();

        UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                .resourceArn("arn:aws::s3:{{region}}:{{111122223333}}:accesspoint/{{{{my-access-point}}}}/*")
                .accountId("{{111122223333}}")
                .tagKeys("{{key1}}")
                .build();

        UntagResourceResponse response = s3Control.untagResource(untagResourceRequest);
        System.out.println("Status code (should be 204):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}
```

------

## Using the REST API
<a name="access-points-db-tag-delete-api"></a>

For information about the Amazon S3 REST API support for deleting tags from an access point, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [UnTagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)

## Using the AWS CLI
<a name="access-points-db-tag-delete-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to delete tags from an access point by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

**Request:**

```
aws s3control untag-resource \
--account-id {{111122223333}} \
--resource-arn arn:aws::s3:{{region}}:{{111122223333}}:accesspoint/{{{{my-access-point}}}}/* \
--tag-keys "{{key1}}" "{{key2}}"
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