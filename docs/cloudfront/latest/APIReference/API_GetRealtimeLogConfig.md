# GetRealtimeLogConfig

Gets a real-time log configuration.

To get a real-time log configuration, you can provide the configuration's name or its
 Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront
 uses the name to identify the real-time log configuration to get.


## Request Syntax



```
POST /2020-05-31/get-realtime-log-config HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<GetRealtimeLogConfigRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ARN>`string`</ARN>
   <Name>`string`</Name>
</GetRealtimeLogConfigRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[GetRealtimeLogConfigRequest](#API_GetRealtimeLogConfig_RequestSyntax "#API_GetRealtimeLogConfig_RequestSyntax")**


Root level tag for the GetRealtimeLogConfigRequest parameters.


Required: Yes




**[ARN](#API_GetRealtimeLogConfig_RequestSyntax "#API_GetRealtimeLogConfig_RequestSyntax")**


The Amazon Resource Name (ARN) of the real-time log configuration to get.


Type: String


Required: No




**[Name](#API_GetRealtimeLogConfig_RequestSyntax "#API_GetRealtimeLogConfig_RequestSyntax")**


The name of the real-time log configuration to get.


Type: String


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetRealtimeLogConfigResult>
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
</GetRealtimeLogConfigResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetRealtimeLogConfigResult](#API_GetRealtimeLogConfig_ResponseSyntax "#API_GetRealtimeLogConfig_ResponseSyntax")**


Root level tag for the GetRealtimeLogConfigResult parameters.


Required: Yes




**[RealtimeLogConfig](#API_GetRealtimeLogConfig_ResponseSyntax "#API_GetRealtimeLogConfig_ResponseSyntax")**


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetRealtimeLogConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetRealtimeLogConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetRealtimeLogConfig")
