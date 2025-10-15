# PutBucketNotificationConfiguration

###### Note

This operation is not supported for directory buckets.

Enables notifications of specified events for a bucket. For more information about event
 notifications, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html").

Using this API, you can replace an existing notification configuration. The configuration is an XML
 file that defines the event types that you want Amazon S3 to publish and the destination where you want Amazon S3
 to publish an event notification when it detects an event of the specified type.

By default, your bucket has no event notifications configured. That is, the notification
 configuration will be an empty `NotificationConfiguration`.


`<NotificationConfiguration>`



`</NotificationConfiguration>`


This action replaces the existing notification configuration with the configuration you include in
 the request body.

After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification Service
 (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the bucket owner
 has permission to publish to it by sending a test notification. In the case of AWS Lambda destinations,
 Amazon S3 verifies that the Lambda function permissions grant Amazon S3 permission to invoke the function from the
 Amazon S3 bucket. For more information, see [Configuring Notifications for Amazon S3
 Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html").

You can disable notifications by adding the empty NotificationConfiguration element.

For more information about the number of event notification configurations that you can create per
 bucket, see [Amazon S3 service
 quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3 "https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3") in *AWS General Reference*.

By default, only the bucket owner can configure notifications on a bucket. However, bucket owners
 can use a bucket policy to grant permission to other users to set this configuration with the required
 `s3:PutBucketNotification` permission.

###### Note

The PUT notification is an atomic operation. For example, suppose your notification configuration
 includes SNS topic, SQS queue, and Lambda function configurations. When you send a PUT request with
 this configuration, Amazon S3 sends test messages to your SNS topic. If the message fails, the entire PUT
 action will fail, and Amazon S3 will not add the configuration to your bucket.

If the configuration in the request body includes only one `TopicConfiguration`
 specifying only the `s3:ReducedRedundancyLostObject` event type, the response will also
 include the `x-amz-sns-test-message-id` header containing the message ID of the test
 notification sent to the topic.

The following action is related to `PutBucketNotificationConfiguration`:


* [GetBucketNotificationConfiguration](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?notification HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-skip-destination-validation: `SkipDestinationValidation`
<?xml version="1.0" encoding="UTF-8"?>
<[NotificationConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-NotificationConfiguration "#AmazonS3-PutBucketNotificationConfiguration-request-NotificationConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[TopicConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-TopicConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-TopicConfigurations")>
      <[Event](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events")>`string`</[Event](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Events")>
      ...
      <[Filter](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>`string`</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>`string`</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Filter")>
      <[Id](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id")>`string`</[Id](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-Id")>
      <[Topic](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn")>`string`</[Topic](API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn "API_TopicConfiguration.md#AmazonS3-Type-TopicConfiguration-TopicArn")>
   </[TopicConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-TopicConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-TopicConfigurations")>
   ...
   <[QueueConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-QueueConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-QueueConfigurations")>
      <[Event](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events")>`string`</[Event](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Events")>
      ...
      <[Filter](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>`string`</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>`string`</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Filter")>
      <[Id](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id")>`string`</[Id](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-Id")>
      <[Queue](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn")>`string`</[Queue](API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn "API_QueueConfiguration.md#AmazonS3-Type-QueueConfiguration-QueueArn")>
   </[QueueConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-QueueConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-QueueConfigurations")>
   ...
   <[CloudFunctionConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-LambdaFunctionConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-LambdaFunctionConfigurations")>
      <[Event](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events")>`string`</[Event](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Events")>
      ...
      <[Filter](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter")>
         <[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
            <[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
               <[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>`string`</[Name](API_FilterRule.md#AmazonS3-Type-FilterRule-Name "API_FilterRule.md#AmazonS3-Type-FilterRule-Name")>
               <[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>`string`</[Value](API_FilterRule.md#AmazonS3-Type-FilterRule-Value "API_FilterRule.md#AmazonS3-Type-FilterRule-Value")>
            </[FilterRule](API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules "API_S3KeyFilter.md#AmazonS3-Type-S3KeyFilter-FilterRules")>
            ...
         </[S3Key](API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key "API_NotificationConfigurationFilter.md#AmazonS3-Type-NotificationConfigurationFilter-Key")>
      </[Filter](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Filter")>
      <[Id](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id")>`string`</[Id](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-Id")>
      <[CloudFunction](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn")>`string`</[CloudFunction](API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn "API_LambdaFunctionConfiguration.md#AmazonS3-Type-LambdaFunctionConfiguration-LambdaFunctionArn")>
   </[CloudFunctionConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-LambdaFunctionConfigurations "#AmazonS3-PutBucketNotificationConfiguration-request-LambdaFunctionConfigurations")>
   ...
   <[EventBridgeConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-EventBridgeConfiguration "#AmazonS3-PutBucketNotificationConfiguration-request-EventBridgeConfiguration")>
   </[EventBridgeConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-EventBridgeConfiguration "#AmazonS3-PutBucketNotificationConfiguration-request-EventBridgeConfiguration")>
</[NotificationConfiguration](#AmazonS3-PutBucketNotificationConfiguration-request-NotificationConfiguration "#AmazonS3-PutBucketNotificationConfiguration-request-NotificationConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


The name of the bucket.


Required: Yes




**[x-amz-expected-bucket-owner](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-skip-destination-validation](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


Skips validation of Amazon SQS, Amazon SNS, and AWS Lambda destinations.
 True or false value.




## Request Body


The request accepts the following data in XML format.





**[NotificationConfiguration](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


Root level tag for the NotificationConfiguration parameters.


Required: Yes




**[CloudFunctionConfiguration](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


Describes the AWS Lambda functions to invoke and the events for which to invoke them.


Type: Array of [LambdaFunctionConfiguration](API_LambdaFunctionConfiguration.md "API_LambdaFunctionConfiguration.md") data types


Required: No




**[EventBridgeConfiguration](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


Enables delivery of events to Amazon EventBridge.


Type: [EventBridgeConfiguration](API_EventBridgeConfiguration.md "API_EventBridgeConfiguration.md") data type


Required: No




**[QueueConfiguration](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


The Amazon Simple Queue Service queues to publish messages to and the events for which to publish
 messages.


Type: Array of [QueueConfiguration](API_QueueConfiguration.md "API_QueueConfiguration.md") data types


Required: No




**[TopicConfiguration](#API_PutBucketNotificationConfiguration_RequestSyntax "#API_PutBucketNotificationConfiguration_RequestSyntax")**


The topic to which notifications are sent and the events for which notifications are
 generated.


Type: Array of [TopicConfiguration](API_TopicConfiguration.md "API_TopicConfiguration.md") data types


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Example 1: Configure notification to invoke a cloud function in Lambda


The following notification configuration includes CloudFunctionConfiguration, which identifies
 the event type for which Amazon S3 can invoke a cloud function and the name of the cloud function to
 invoke. 



```

<NotificationConfiguration>
  <CloudFunctionConfiguration>
    <Id>ObjectCreatedEvents</Id>
    <CloudFunction>arn:aws:lambda:us-west-2:35667example:function:CreateThumbnail</CloudFunction>
    <Event>s3:ObjectCreated:*</Event>
  </CloudFunctionConfiguration>
</NotificationConfiguration>
         
```

### Example


The following PUT uploads the notification configuration. The action replaces the existing
 notification configuration.



```

PUT http://s3.<Region>.amazonaws.com/examplebucket?notification= HTTP/1.1
User-Agent: s3curl 2.0
Host: s3.amazonaws.com
Pragma: no-cache
Accept: */*
Proxy-Connection: Keep-Alive
Authorization: authorization string
Date: Mon, 13 Oct 2014 23:14:52 +0000
Content-Length: length

[request body]
         
```

### Sample Response


This example illustrates one usage of PutBucketNotificationConfiguration.



```

HTTP/1.1 200 OK
x-amz-id-2: 8+FlwagBSoT2qpMaGlfCUkRkFR5W3OeS7UhhoBb17j+kqvpS2cSFlgJ5coLd53d2
x-amz-request-id: E5BA4600A3937335
Date: Fri, 31 Oct 2014 01:49:50 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Example 2: Configure a notification with multiple destinations


The following notification configuration includes the topic and queue configurations:



* A topic configuration identifying an SNS topic for Amazon S3 to publish events of the
 `s3:ReducedRedundancyLostObject` type.
* A queue configuration identifying an SQS queue for Amazon S3 to publish events of the
 `s3:ObjectCreated:*` type.


```

<NotificationConfiguration>
  <TopicConfiguration>
    <Topic>arn:aws:sns:us-east-1:356671443308:s3notificationtopic2</Topic>
    <Event>s3:ReducedRedundancyLostObject</Event>
  </TopicConfiguration>
  <QueueConfiguration>
    <Queue>arn:aws:sqs:us-east-1:356671443308:s3notificationqueue</Queue>
    <Event>s3:ObjectCreated:*</Event>
  </QueueConfiguration>
</NotificationConfiguration>
         
```

### Example


The following PUT request against the notification subresource of the `examplebucket`
 bucket sends the preceding notification configuration in the request body. The action replaces the
 existing notification configuration on the bucket.



```

PUT http://s3.<Region>.amazonaws.com/examplebucket?notification= HTTP/1.1
User-Agent: s3curl 2.0
Host: s3.amazonaws.com
Pragma: no-cache
Accept: */*
Proxy-Connection: Keep-Alive
Authorization: authorization string
Date: Mon, 13 Oct 2014 22:58:43 +0000
Content-Length: 391
Expect: 100-continue

         
```

### Example 3: Configure a notification with object key name filtering


The following notification configuration contains a queue configuration identifying an Amazon
 SQS queue for Amazon S3 to publish events to of the `s3:ObjectCreated:Put` type. The events
 will be published whenever an object that has a prefix of `images/` and a
 `.jpg` suffix is PUT to a bucket. For more examples of notification configurations that
 use filtering, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html").



```

<NotificationConfiguration>
  <QueueConfiguration>
      <Id>1</Id>
      <Filter>
          <S3Key>
              <FilterRule>
                  <Name>prefix</Name>
                  <Value>images/</Value>
              </FilterRule>
              <FilterRule>
                  <Name>suffix</Name>
                  <Value>.jpg</Value>
              </FilterRule>
          </S3Key>
     </Filter>
     <Queue>arn:aws:sqs:us-west-2:444455556666:s3notificationqueue</Queue>
     <Event>s3:ObjectCreated:Put</Event>
  </QueueConfiguration>
</NotificationConfiguration>

         
```

### Example


The following PUT request against the notification subresource of the `examplebucket`
 bucket sends the preceding notification configuration in the request body. The action replaces the
 existing notification configuration on the bucket.



```

PUT http://s3.<Region>.amazonaws.com/examplebucket?notification= HTTP/1.1
User-Agent: s3curl 2.0
Host: s3.amazonaws.com
Pragma: no-cache
Accept: */*
Proxy-Connection: Keep-Alive
Authorization: authorization string
Date: Mon, 13 Oct 2014 22:58:43 +0000
Content-Length: length
Expect: 100-continue

         
```

### Sample Response


This example illustrates one usage of PutBucketNotificationConfiguration.



```

HTTP/1.1 200 OK
x-amz-id-2: SlvJLkfunoAGILZK3KqHSSUq4kwbudkrROmESoHOpDacULy+cxRoR1Svrfoyvg2A
x-amz-request-id: BB1BA8E12D6A80B7
Date: Mon, 13 Oct 2014 22:58:44 GMT
Content-Length: 0
Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketNotificationConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketNotificationConfiguration")
