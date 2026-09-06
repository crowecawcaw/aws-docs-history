

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# CreateMonitor
<a name="API_CreateMonitor"></a>

Creates a predictor monitor resource for an existing auto predictor. Predictor monitoring allows you to see how your predictor's performance changes over time. For more information, see [Predictor Monitoring](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html). 

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_CreateMonitor_RequestSyntax"></a>

```
{
   "MonitorName": "{{string}}",
   "ResourceArn": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateMonitor_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MonitorName](#API_CreateMonitor_RequestSyntax) **   <a name="forecast-CreateMonitor-request-MonitorName"></a>
The name of the monitor resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

 ** [ResourceArn](#API_CreateMonitor_RequestSyntax) **   <a name="forecast-CreateMonitor-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the predictor to monitor.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

 ** [Tags](#API_CreateMonitor_RequestSyntax) **   <a name="forecast-CreateMonitor-request-Tags"></a>
A list of [tags](https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html) to apply to the monitor resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateMonitor_ResponseSyntax"></a>

```
{
   "MonitorArn": "string"
}
```

## Response Elements
<a name="API_CreateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitorArn](#API_CreateMonitor_ResponseSyntax) **   <a name="forecast-CreateMonitor-response-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor resource.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

## Errors
<a name="API_CreateMonitor_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of resources per account has been exceeded.  
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **   
There is already a resource with this name. Try again with a different name.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_CreateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/CreateMonitor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/CreateMonitor) 