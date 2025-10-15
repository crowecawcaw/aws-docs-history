# Adding a tag to an access point

You can add tags to Amazon S3 Access Points and modify these tags. There is no additional charge for using tags on access points beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://docs.aws.amazon.com/s3/pricing/ "https://docs.aws.amazon.com/s3/pricing/"). For more information about tagging access points, see [Using tags with S3 Access Points for general purpose buckets](access-points-tagging.md "access-points-tagging.md").


## Permissions


To add a tag to an access point, you must have the following permission:



* `s3:TagResource`

## Troubleshooting errors


If you encounter an error when attempting to add a tag to an access point, you can do the following: 



* Verify that you have the required [Permissions](#access-points-tag-add-permissions "#access-points-tag-add-permissions") to add a tag to an access point.
* If you attempted to add a tag key that starts with the AWS reserved prefix `aws:`, change the tag key and try again.

## Steps


You can add tags to access points by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.


To add tags to an access point using the Amazon S3 console:


1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access Points (General Purpose Buckets)**.
3. Choose the access point name.
4. Choose the **Properties** tab.
5. Scroll to the **Tags** section and choose **Add new Tag**.
6. This opens the **Add Tags** page. You can enter up to 50 tag key value pairs.
7. If you add a new tag with the same key name as an existing tag, the value of the new tag overrides the value of the existing tag.
8. You can also edit the values of existing tags on this page.
9. After you have added the tag(s), choose **Save changes**.

SDK for Java 2.x
This example shows you how to add tags to an access point by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information. 



```
TagResourceRequest tagResourceRequest = TagResourceRequest.builder().resourceArn(arn:aws::s3:`region`:`111122223333`:accesspoint/``my-access-point``/*)
.accountId(`111122223333`)
.tags(List.of(Tag.builder().key("`key1`").value("`value1`").build(),
Tag.builder().key("`key2`").value("`value2`").build()))
.build();
awss3Control.tagResource(tagResourceRequest);

```


For information about the Amazon S3 REST API support for adding tags to an access point, see the following section in the *Amazon Simple Storage Service API Reference*:


* [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md")
To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*.

The following CLI example shows you how to add tags to an access point by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**


```
aws s3control tag-resource \
--account-id `111122223333` \
--resource-arn arn:aws::s3:`region`:`111122223333`:accesspoint/``my-access-point``/* \
--tags "Key=`key1`,Value=`value1`"

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
