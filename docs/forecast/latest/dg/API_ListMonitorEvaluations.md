

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# ListMonitorEvaluations
<a name="API_ListMonitorEvaluations"></a>

Returns a list of the monitoring evaluation results and predictor events collected by the monitor resource during different windows of time.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

For information about monitoring see [Predictor Monitoring](predictor-monitoring.md). For more information about retrieving monitoring results see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html).

## Request Syntax
<a name="API_ListMonitorEvaluations_RequestSyntax"></a>

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
   "MonitorArn": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitorEvaluations_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListMonitorEvaluations_RequestSyntax) **   <a name="forecast-ListMonitorEvaluations-request-Filters"></a>
An array of filters. For each filter, provide a condition and a match statement. The condition is either `IS` or `IS_NOT`, which specifies whether to include or exclude the resources that match the statement from the list. The match statement consists of a key and a value.  
 **Filter properties**   
+  `Condition` - The condition to apply. Valid values are `IS` and `IS_NOT`.
+  `Key` - The name of the parameter to filter on. The only valid value is `EvaluationState`.
+  `Value` - The value to match. Valid values are only `SUCCESS` or `FAILURE`.
For example, to list only successful monitor evaluations, you would specify:  
 `"Filters": [ { "Condition": "IS", "Key": "EvaluationState", "Value": "SUCCESS" } ]`   
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** [MaxResults](#API_ListMonitorEvaluations_RequestSyntax) **   <a name="forecast-ListMonitorEvaluations-request-MaxResults"></a>
The maximum number of monitoring results to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [MonitorArn](#API_ListMonitorEvaluations_RequestSyntax) **   <a name="forecast-ListMonitorEvaluations-request-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor resource to get results from.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

 ** [NextToken](#API_ListMonitorEvaluations_RequestSyntax) **   <a name="forecast-ListMonitorEvaluations-request-NextToken"></a>
If the result of the previous request was truncated, the response includes a `NextToken`. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+`   
Required: No

## Response Syntax
<a name="API_ListMonitorEvaluations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PredictorMonitorEvaluations": [ 
      { 
         "EvaluationState": "string",
         "EvaluationTime": number,
         "Message": "string",
         "MetricResults": [ 
            { 
               "MetricName": "string",
               "MetricValue": number
            }
         ],
         "MonitorArn": "string",
         "MonitorDataSource": { 
            "DatasetImportJobArn": "string",
            "ForecastArn": "string",
            "PredictorArn": "string"
         },
         "NumItemsEvaluated": number,
         "PredictorEvent": { 
            "Datetime": number,
            "Detail": "string"
         },
         "ResourceArn": "string",
         "WindowEndDatetime": number,
         "WindowStartDatetime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListMonitorEvaluations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListMonitorEvaluations_ResponseSyntax) **   <a name="forecast-ListMonitorEvaluations-response-NextToken"></a>
If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Pattern: `.+` 

 ** [PredictorMonitorEvaluations](#API_ListMonitorEvaluations_ResponseSyntax) **   <a name="forecast-ListMonitorEvaluations-response-PredictorMonitorEvaluations"></a>
The monitoring results and predictor events collected by the monitor resource during different windows of time.  
For information about monitoring see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html). For more information about retrieving monitoring results see [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html).  
Type: Array of [PredictorMonitorEvaluation](API_PredictorMonitorEvaluation.md) objects

## Errors
<a name="API_ListMonitorEvaluations_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The token is not valid. Tokens expire after 24 hours.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_ListMonitorEvaluations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/ListMonitorEvaluations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/ListMonitorEvaluations) 