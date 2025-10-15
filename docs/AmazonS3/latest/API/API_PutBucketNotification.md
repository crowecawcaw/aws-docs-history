# PutBucketNotification

###### Note

This operation is not supported for directory buckets.

 No longer used, see the [PutBucketNotificationConfiguration](API_PutBucketNotificationConfiguration.md "API_PutBucketNotificationConfiguration.md") operation.


## Request Syntax



```
PUT /?notification HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[NotificationConfiguration](#AmazonS3-PutBucketNotification-request-NotificationConfiguration "#AmazonS3-PutBucketNotification-request-NotificationConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[TopicConfiguration](#AmazonS3-PutBucketNotification-request-TopicConfiguration "#AmazonS3-PutBucketNotification-request-TopicConfiguration")>
      <[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event")>`string`</[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event")>
      <[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events")>`string`</[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events")>
      ...
      <[Id](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id")>`string`</[Id](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id")>
      <[Topic](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic")>`string`</[Topic](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic")>
   </[TopicConfiguration](#AmazonS3-PutBucketNotification-request-TopicConfiguration "#AmazonS3-PutBucketNotification-request-TopicConfiguration")>
   <[QueueConfiguration](#AmazonS3-PutBucketNotification-request-QueueConfiguration "#AmazonS3-PutBucketNotification-request-QueueConfiguration")>
      <[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event")>`string`</[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event")>
      <[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events")>`string`</[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events")>
      ...
      <[Id](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id")>`string`</[Id](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id")>
      <[Queue](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue")>`string`</[Queue](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue")>
   </[QueueConfiguration](#AmazonS3-PutBucketNotification-request-QueueConfiguration "#AmazonS3-PutBucketNotification-request-QueueConfiguration")>
   <[CloudFunctionConfiguration](#AmazonS3-PutBucketNotification-request-CloudFunctionConfiguration "#AmazonS3-PutBucketNotification-request-CloudFunctionConfiguration")>
      <[CloudFunction](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction")>`string`</[CloudFunction](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction")>
      <[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event")>`string`</[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event")>
      <[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events")>`string`</[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events")>
      ...
      <[Id](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id")>`string`</[Id](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id")>
      <[InvocationRole](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole")>`string`</[InvocationRole](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole")>
   </[CloudFunctionConfiguration](#AmazonS3-PutBucketNotification-request-CloudFunctionConfiguration "#AmazonS3-PutBucketNotification-request-CloudFunctionConfiguration")>
</[NotificationConfiguration](#AmazonS3-PutBucketNotification-request-NotificationConfiguration "#AmazonS3-PutBucketNotification-request-NotificationConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


The name of the bucket.


Required: Yes




**[Content-MD5](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


The MD5 hash of the `PutPublicAccessBlock` request body.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[NotificationConfiguration](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


Root level tag for the NotificationConfiguration parameters.


Required: Yes




**[CloudFunctionConfiguration](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


Container for specifying the AWS Lambda notification configuration.


Type: [CloudFunctionConfiguration](API_CloudFunctionConfiguration.md "API_CloudFunctionConfiguration.md") data type


Required: No




**[QueueConfiguration](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


This data type is deprecated. This data type specifies the configuration for publishing messages to
 an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events. 


Type: [QueueConfigurationDeprecated](API_QueueConfigurationDeprecated.md "API_QueueConfigurationDeprecated.md") data type


Required: No




**[TopicConfiguration](#API_PutBucketNotification_RequestSyntax "#API_PutBucketNotification_RequestSyntax")**


This data type is deprecated. A container for specifying the configuration for publication of
 messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
 


Type: [TopicConfigurationDeprecated](API_TopicConfigurationDeprecated.md "API_TopicConfigurationDeprecated.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketNotification")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketNotification "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketNotification")
