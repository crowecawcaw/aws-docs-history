# ListRealtimeLogConfigs

Gets a list of real-time log configurations.

You can optionally specify the maximum number of items to receive in the response. If
 the total number of items in the list exceeds the maximum that you specify, or the
 default maximum, the response is paginated. To get the next page of items, send a
 subsequent request that specifies the `NextMarker` value from the current
 response as the `Marker` value in the subsequent request.


## Request Syntax



```
GET /2020-05-31/realtime-log-config?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListRealtimeLogConfigs_RequestSyntax "#API_ListRealtimeLogConfigs_RequestSyntax")**


Use this field when paginating results to indicate where to begin in your list of
 real-time log configurations. The response includes real-time log configurations in the
 list that occur after the marker. To get the next page of the list, set this field's
 value to the value of `NextMarker` from the current page's response.




**[MaxItems](#API_ListRealtimeLogConfigs_RequestSyntax "#API_ListRealtimeLogConfigs_RequestSyntax")**


The maximum number of real-time log configurations that you want in the
 response.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<RealtimeLogConfigs>
   <IsTruncated>***boolean***</IsTruncated>
   <Items>
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
   </Items>
   <Marker>***string***</Marker>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
</RealtimeLogConfigs>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[RealtimeLogConfigs](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


Root level tag for the RealtimeLogConfigs parameters.


Required: Yes




**[IsTruncated](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


A flag that indicates whether there are more real-time log configurations than are
 contained in this list.


Type: Boolean




**[Items](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


Contains the list of real-time log configurations.


Type: Array of [RealtimeLogConfig](API_RealtimeLogConfig.md "API_RealtimeLogConfig.md") objects




**[Marker](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


This parameter indicates where this list of real-time log configurations begins. This
 list includes real-time log configurations that occur after the marker.


Type: String




**[MaxItems](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


The maximum number of real-time log configurations requested.


Type: Integer




**[NextMarker](#API_ListRealtimeLogConfigs_ResponseSyntax "#API_ListRealtimeLogConfigs_ResponseSyntax")**


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing real-time log configurations where you left off.
 


Type: String




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListRealtimeLogConfigs")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListRealtimeLogConfigs "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListRealtimeLogConfigs")
