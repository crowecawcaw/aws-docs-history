# GetBucketNotificationConfiguration

###### Note

This operation is not supported for directory buckets.

Returns the notification configuration of a bucket.

If notifications are not enabled on the bucket, the action returns an empty
 `NotificationConfiguration` element.

By default, you must be the bucket owner to read the notification configuration of a bucket.
 However, the bucket owner can use a bucket policy to grant permission to other users to read this
 configuration with the `s3:GetBucketNotification` permission.

When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.

When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").

For more information about setting and reading the notification configuration on a bucket, see
 [Setting Up Notification
 of Bucket Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html"). For more information about bucket policies, see [Using Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html").

The following action is related to `GetBucketNotification`:


* [PutBucketNotification](API_PutBucketNotification.md "API_PutBucketNotification.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?notification HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketNotificationConfiguration_RequestSyntax "#API_GetBucketNotificationConfiguration_RequestSyntax")**


The name of the bucket for which to get the notification configuration.


When you use this API operation with an access point, provide the alias of the access point in place of the bucket name.


When you use this API operation with an Object Lambda access point, provide the alias of the Object Lambda access point in place of the bucket name. 
If the Object Lambda access point alias in a request is not valid, the error code `InvalidAccessPointAliasError` is returned. 
For more information about `InvalidAccessPointAliasError`, see [List of
 Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketNotificationConfiguration_RequestSyntax "#API_GetBucketNotificationConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[NotificationConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-NotificationConfiguration "#AmazonS3-GetBucketNotificationConfiguration-response-NotificationConfiguration")>
   <[TopicConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-TopicConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-TopicConfigurations")>
      <[Event](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events")>***string***</[Event](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events")>
      ...
      <[Filter](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>***string***</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>***string***</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter")>
      <[Id](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id")>***string***</[Id](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id")>
      <[Topic](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn")>***string***</[Topic](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn")>
   </[TopicConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-TopicConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-TopicConfigurations")>
   ...
   <[QueueConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-QueueConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-QueueConfigurations")>
      <[Event](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events")>***string***</[Event](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events")>
      ...
      <[Filter](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>***string***</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>***string***</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter")>
      <[Id](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id")>***string***</[Id](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id")>
      <[Queue](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn")>***string***</[Queue](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn")>
   </[QueueConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-QueueConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-QueueConfigurations")>
   ...
   <[CloudFunctionConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-LambdaFunctionConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-LambdaFunctionConfigurations")>
      <[Event](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events")>***string***</[Event](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events")>
      ...
      <[Filter](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>***string***</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>***string***</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter")>
      <[Id](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id")>***string***</[Id](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id")>
      <[CloudFunction](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn")>***string***</[CloudFunction](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn")>
   </[CloudFunctionConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-LambdaFunctionConfigurations "#AmazonS3-GetBucketNotificationConfiguration-response-LambdaFunctionConfigurations")>
   ...
   <[EventBridgeConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-EventBridgeConfiguration "#AmazonS3-GetBucketNotificationConfiguration-response-EventBridgeConfiguration")>
   </[EventBridgeConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-EventBridgeConfiguration "#AmazonS3-GetBucketNotificationConfiguration-response-EventBridgeConfiguration")>
</[NotificationConfiguration](#AmazonS3-GetBucketNotificationConfiguration-response-NotificationConfiguration "#AmazonS3-GetBucketNotificationConfiguration-response-NotificationConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[NotificationConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax "#API_GetBucketNotificationConfiguration_ResponseSyntax")**


Root level tag for the NotificationConfiguration parameters.


Required: Yes




**[CloudFunctionConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax "#API_GetBucketNotificationConfiguration_ResponseSyntax")**


Describes the AWS Lambda functions to invoke and the events for which to invoke them.


Type: Array of [LambdaFunctionConfiguration](API_LambdaFunctionConfiguration.md "API_LambdaFunctionConfiguration.md") data types




**[EventBridgeConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax "#API_GetBucketNotificationConfiguration_ResponseSyntax")**


Enables delivery of events to Amazon EventBridge.


Type: [EventBridgeConfiguration](API_EventBridgeConfiguration.md "API_EventBridgeConfiguration.md") data type




**[QueueConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax "#API_GetBucketNotificationConfiguration_ResponseSyntax")**


The Amazon Simple Queue Service queues to publish messages to and the events for which to publish
 messages.


Type: Array of [QueueConfiguration](API_QueueConfiguration.md "API_QueueConfiguration.md") data types




**[TopicConfiguration](#API_GetBucketNotificationConfiguration_ResponseSyntax "#API_GetBucketNotificationConfiguration_ResponseSyntax")**


The topic to which notifications are sent and the events for which notifications are
 generated.


Type: Array of [TopicConfiguration](API_TopicConfiguration.md "API_TopicConfiguration.md") data types




## Examples


### Sample Request


This request returns the notification configuration on the bucket
 `amzn-s3-demo-bucket.s3.<Region>.amazonaws.com`.



```

            GET ?notification HTTP/1.1 
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 15 Oct 2014 16:59:03 GMT
            Authorization: authorization string
         
```

### Sample Response


This response returns that the notification configuration for the specified bucket. 



```

            HTTP/1.1 200 OK
            x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
            x-amz-request-id: 236A8905248E5A02
            Date: Wed, 15 Oct 2014 16:59:04 GMT
            Server: AmazonS3
            <?xml version="1.0" encoding="UTF-8"?>

            <NotificationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
             <TopicConfiguration>
               <Id>YjVkM2Y0YmUtNGI3NC00ZjQyLWEwNGItNDIyYWUxY2I0N2M4</Id>
              <Topic>arn:aws:sns:us-east-1:account-id:s3notificationtopic2</Topic>
              <Event>s3:ReducedRedundancyLostObject</Event>
              <Event>s3:ObjectCreated:*</Event>
             </TopicConfiguration>
            </NotificationConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketNotificationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketNotificationConfiguration")
