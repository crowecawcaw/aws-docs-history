# UpdateRealtimeLogConfig

Updates a real-time log configuration.

When you update a real-time log configuration, all the parameters are updated with the
 values provided in the request. You cannot update some parameters independent of others.
 To update a real-time log configuration:


1. Call `GetRealtimeLogConfig` to get the current real-time log
 configuration.
2. Locally modify the parameters in the real-time log configuration that you want
 to update.
3. Call this API (`UpdateRealtimeLogConfig`) by providing the entire
 real-time log configuration, including the parameters that you modified and
 those that you didn't.
You cannot update a real-time log configuration's `Name` or
 `ARN`.


## Request Syntax



```
PUT /2020-05-31/realtime-log-config HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateRealtimeLogConfigRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ARN>`string`</ARN>
   <EndPoints>
      <EndPoint>
         <KinesisStreamConfig>
            <RoleARN>`string`</RoleARN>
            <StreamARN>`string`</StreamARN>
         </KinesisStreamConfig>
         <StreamType>`string`</StreamType>
      </EndPoint>
   </EndPoints>
   <Fields>
      <Field>`string`</Field>
   </Fields>
   <Name>`string`</Name>
   <SamplingRate>`long`</SamplingRate>
</UpdateRealtimeLogConfigRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[UpdateRealtimeLogConfigRequest](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


Root level tag for the UpdateRealtimeLogConfigRequest parameters.


Required: Yes




**[ARN](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


The Amazon Resource Name (ARN) for this real-time log configuration.


Type: String


Required: No




**[EndPoints](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


Contains information about the Amazon Kinesis data stream where you are sending real-time
 log data.


Type: Array of [EndPoint](API_EndPoint.md "API_EndPoint.md") objects


Required: No




**[Fields](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


A list of fields to include in each real-time log record.


For more information about fields, see [Real-time log configuration fields](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-fields "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md#understand-real-time-log-config-fields") in the
 *Amazon CloudFront Developer Guide*.


Type: Array of strings


Required: No




**[Name](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


The name for this real-time log configuration.


Type: String


Required: No




**[SamplingRate](#API_UpdateRealtimeLogConfig_RequestSyntax "#API_UpdateRealtimeLogConfig_RequestSyntax")**


The sampling rate for this real-time log configuration. The sampling rate determines
 the percentage of viewer requests that are represented in the real-time log data. You
 must provide an integer between 1 and 100, inclusive.


Type: Long


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateRealtimeLogConfigResult>
   <RealtimeLogConfig>
      <ARN>***string***</ARN>
      <EndPoints>
         <EndPoint>
            <KinesisStreamConfig>
               <RoleARN>***string***</RoleARN>
               <StreamARN>***string***</StreamARN>
            </KinesisStreamConfig>
            <StreamType>***string***</StreamType>
         </EndPoint>
      </EndPoints>
      <Fields>
         <Field>***string***</Field>
      </Fields>
      <Name>***string***</Name>
      <SamplingRate>***long***</SamplingRate>
   </RealtimeLogConfig>
</UpdateRealtimeLogConfigResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[UpdateRealtimeLogConfigResult](#API_UpdateRealtimeLogConfig_ResponseSyntax "#API_UpdateRealtimeLogConfig_ResponseSyntax")**


Root level tag for the UpdateRealtimeLogConfigResult parameters.


Required: Yes




**[RealtimeLogConfig](#API_UpdateRealtimeLogConfig_ResponseSyntax "#API_UpdateRealtimeLogConfig_ResponseSyntax")**


A real-time log configuration.


Type: [RealtimeLogConfig](API_RealtimeLogConfig.md "API_RealtimeLogConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchRealtimeLogConfig** 


The real-time log configuration does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateRealtimeLogConfig")
