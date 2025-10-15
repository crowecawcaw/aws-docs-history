# GetBucketNotification

###### Note

This operation is not supported for directory buckets.

 No longer used, see [GetBucketNotificationConfiguration](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md").


## Request Syntax



```
GET /?notification HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketNotification_RequestSyntax "#API_GetBucketNotification_RequestSyntax")**


The name of the bucket for which to get the notification configuration.


When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.


When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketNotification_RequestSyntax "#API_GetBucketNotification_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[NotificationConfiguration](#AmazonS3-GetBucketNotification-response-NotificationConfigurationDeprecated "#AmazonS3-GetBucketNotification-response-NotificationConfigurationDeprecated")>
   <[TopicConfiguration](#AmazonS3-GetBucketNotification-response-TopicConfiguration "#AmazonS3-GetBucketNotification-response-TopicConfiguration")>
      <[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event")>***string***</[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Event")>
      <[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events")>***string***</[Event](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Events")>
      ...
      <[Id](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id")>***string***</[Id](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Id")>
      <[Topic](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic")>***string***</[Topic](API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic "API_TopicConfigurationDeprecated.md#AmazonS3-Type-TopicConfigurationDeprecated-Topic")>
   </[TopicConfiguration](#AmazonS3-GetBucketNotification-response-TopicConfiguration "#AmazonS3-GetBucketNotification-response-TopicConfiguration")>
   <[QueueConfiguration](#AmazonS3-GetBucketNotification-response-QueueConfiguration "#AmazonS3-GetBucketNotification-response-QueueConfiguration")>
      <[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event")>***string***</[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Event")>
      <[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events")>***string***</[Event](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Events")>
      ...
      <[Id](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id")>***string***</[Id](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Id")>
      <[Queue](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue")>***string***</[Queue](API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue "API_QueueConfigurationDeprecated.md#AmazonS3-Type-QueueConfigurationDeprecated-Queue")>
   </[QueueConfiguration](#AmazonS3-GetBucketNotification-response-QueueConfiguration "#AmazonS3-GetBucketNotification-response-QueueConfiguration")>
   <[CloudFunctionConfiguration](#AmazonS3-GetBucketNotification-response-CloudFunctionConfiguration "#AmazonS3-GetBucketNotification-response-CloudFunctionConfiguration")>
      <[CloudFunction](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction")>***string***</[CloudFunction](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-CloudFunction")>
      <[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event")>***string***</[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Event")>
      <[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events")>***string***</[Event](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Events")>
      ...
      <[Id](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id")>***string***</[Id](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-Id")>
      <[InvocationRole](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole")>***string***</[InvocationRole](API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole "API_CloudFunctionConfiguration.md#AmazonS3-Type-CloudFunctionConfiguration-InvocationRole")>
   </[CloudFunctionConfiguration](#AmazonS3-GetBucketNotification-response-CloudFunctionConfiguration "#AmazonS3-GetBucketNotification-response-CloudFunctionConfiguration")>
</[NotificationConfiguration](#AmazonS3-GetBucketNotification-response-NotificationConfigurationDeprecated "#AmazonS3-GetBucketNotification-response-NotificationConfigurationDeprecated")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[NotificationConfiguration](#API_GetBucketNotification_ResponseSyntax "#API_GetBucketNotification_ResponseSyntax")**


Root level tag for the NotificationConfiguration parameters.


Required: Yes




**[CloudFunctionConfiguration](#API_GetBucketNotification_ResponseSyntax "#API_GetBucketNotification_ResponseSyntax")**


Container for specifying the AWS Lambda notification configuration.


Type: [CloudFunctionConfiguration](API_CloudFunctionConfiguration.md "API_CloudFunctionConfiguration.md") data type




**[QueueConfiguration](#API_GetBucketNotification_ResponseSyntax "#API_GetBucketNotification_ResponseSyntax")**


This data type is deprecated. This data type specifies the configuration for publishing messages to
 an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events. 


Type: [QueueConfigurationDeprecated](API_QueueConfigurationDeprecated.md "API_QueueConfigurationDeprecated.md") data type




**[TopicConfiguration](#API_GetBucketNotification_ResponseSyntax "#API_GetBucketNotification_ResponseSyntax")**


This data type is deprecated. A container for specifying the configuration for publication of
 messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
 


Type: [TopicConfigurationDeprecated](API_TopicConfigurationDeprecated.md "API_TopicConfigurationDeprecated.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotification")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotification "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotification")
