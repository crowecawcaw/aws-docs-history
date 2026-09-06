

# Adding a tag to an access point for directory buckets
<a name="access-points-db-tag-add"></a>



You can add tags to Amazon S3 Access Points for directory buckets and modify these tags. For additional information, see [Using tags with S3 Access Points for directory buckets](access-points-db-tagging.md).

## Permissions
<a name="access-points-db-tag-add-permissions"></a>

To add a tag to an access point for directory buckets, you must have the following permission:
+ `s3express:TagResource`

## Troubleshooting errors
<a name="access-points-db-tag-add-troubleshooting"></a>

If you encounter an error when attempting to add a tag to an access point for directory buckets, you can do the following: 
+ Verify that you have the required [Permissions](#access-points-db-tag-add-permissions) to add a tag to an access point for directory buckets.
+ If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again. 

## Steps
<a name="access-points-db-tag-add-steps"></a>

You can add tags to access points for directory buckets by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

## Using the S3 console
<a name="access-points-db-tag-add-console"></a>

To add tags to an access point for directory buckets using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Access Points (Directory Buckets)**.

1. Choose the access point name. 

1. Choose the **Properties** tab. 

1. Scroll to the **Tags** section and choose **Add new Tag**. 

1. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs. 

1. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.

1. You can also edit the values of existing tags on this page.

1. After you have added the tag(s), choose **Save changes**. 

## Using the AWS SDKs
<a name="access-points-db-tag-add-sdks"></a>

------
#### [ SDK for Java 2.x ]

This example shows you how to add tags to an access point for directory buckets by using the AWS SDK for Java 2.x. To use the command replace the {{user input placeholders}} with your own information. 

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.Tag;
import software.amazon.awssdk.services.s3control.model.TagResourceRequest;
import software.amazon.awssdk.services.s3control.model.TagResourceResponse;

public class TagResourceExample {
    public static void tagResourceExample() {
        S3ControlClient s3Control = S3ControlClient.builder().region(Region.{{US_WEST_2}}).build();

        TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                .resourceArn("arn:aws::s3:{{region}}:{{111122223333}}:accesspoint/{{{{my-access-point}}}}/*")
                .accountId("{{111122223333}}")
                .tags(Tag.builder().key("{{key1}}").value("{{value1}}").build())
                .build();

        TagResourceResponse response = s3Control.tagResource(tagResourceRequest);
        System.out.println("Status code (should be 204):");
        System.out.println(response.sdkHttpResponse().statusCode());
    }
}
```

------

## Using the REST API
<a name="access-points-db-tag-add-api"></a>

For information about the Amazon S3 REST API support for adding tags to an access point for directory buckets, see the following section in the *Amazon Simple Storage Service API Reference*:
+ [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html)

## Using the AWS CLI
<a name="access-points-db-tag-add-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to add tags to a directory bucket by using the AWS CLI. To use the command replace the {{user input placeholders}} with your own information.

**Request:**

```
aws s3control tag-resource \
--account-id {{111122223333}} \
--resource-arn arn:aws::s3express:{{region}}:{{444455556666}}:bucket/prefix--{{use1-az4}}--x-s3 \
--tags "Key={{key1}},Value={{value1}}"
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