

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# ListMonitors
<a name="API_ListMonitors"></a>

Returns a list of monitors created with the [CreateMonitor](API_CreateMonitor.md) operation and [CreateAutoPredictor](API_CreateAutoPredictor.md) operation. For each monitor resource, this operation returns of a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve a complete set of properties of a monitor resource by specify the monitor's ARN in the [DescribeMonitor](API_DescribeMonitor.md) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_ListMonitors_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Condition": "{{string}}",
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitors_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListMonitors_RequestSyntax) **   <a name="forecast-ListMonitors-request-Filters"></a>
An array of filters. For each filter, provide a condition and a match statement. The condition is either `IS` or `IS_NOT`, which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.  
 **Filter properties**   
+  `Condition` - The condition to apply. Valid values are `IS` and `IS_NOT`.
+  `Key` - The name of the parameter to filter on. The only valid value is `Status`.
+  `Value` - The value to match.
For example, to list all monitors who's status is ACTIVE, you would specify:  
 `"Filters": [ { "Condition": "IS", "Key": "Status", "Value": "ACTIVE" } ]`   
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** [MaxResults](#API_ListMonitors_RequestSyntax) **   <a name="forecast-ListMonitors-request-MaxResults"></a>
The maximum number of monitors to include in the response.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListMonitors_RequestSyntax) **   <a name="forecast-ListMonitors-request-NextToken"></a>
If the result of the previous request was truncated, the response includes a `NextToken`. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+`   
Required: No

## Response Syntax
<a name="API_ListMonitors_ResponseSyntax"></a>

```
{
   "Monitors": [ 
      { 
         "CreationTime": number,
         "LastModificationTime": number,
         "MonitorArn": "string",
         "MonitorName": "string",
         "ResourceArn": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Monitors](#API_ListMonitors_ResponseSyntax) **   <a name="forecast-ListMonitors-response-Monitors"></a>
An array of objects that summarize each monitor's properties.  
Type: Array of [MonitorSummary](API_MonitorSummary.md) objects

 ** [NextToken](#API_ListMonitors_ResponseSyntax) **   <a name="forecast-ListMonitors-response-NextToken"></a>
If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+` 

## Errors
<a name="API_ListMonitors_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The token is not valid. Tokens expire after 24 hours.  
HTTP Status Code: 400

## See Also
<a name="API_ListMonitors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/ListMonitors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/ListMonitors) 