

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# QueryWhatIfForecast
<a name="API_forecastquery_QueryWhatIfForecast"></a>

Retrieves a what-if forecast.

## Request Syntax
<a name="API_forecastquery_QueryWhatIfForecast_RequestSyntax"></a>

```
{
   "EndDate": "{{string}}",
   "Filters": { 
      "{{string}}" : "{{string}}" 
   },
   "NextToken": "{{string}}",
   "StartDate": "{{string}}",
   "WhatIfForecastArn": "{{string}}"
}
```

## Request Parameters
<a name="API_forecastquery_QueryWhatIfForecast_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [EndDate](#API_forecastquery_QueryWhatIfForecast_RequestSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-request-EndDate"></a>
The end date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00.   
Type: String  
Required: No

 ** [Filters](#API_forecastquery_QueryWhatIfForecast_RequestSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-request-Filters"></a>
The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for `client_21` in the electricity usage dataset, specify the following:  
 `{"item_id" : "client_21"}`   
To get the full what-if forecast, use the [CreateForecastExportJob](https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateWhatIfForecastExport.html) operation.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Maximum length of 256.  
Key Pattern: `^[a-zA-Z0-9\_\-]+$`   
Value Length Constraints: Maximum length of 256.  
Required: Yes

 ** [NextToken](#API_forecastquery_QueryWhatIfForecast_RequestSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-request-NextToken"></a>
If the result of the previous request was truncated, the response includes a `NextToken`. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 3000.  
Required: No

 ** [StartDate](#API_forecastquery_QueryWhatIfForecast_RequestSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-request-StartDate"></a>
The start date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.  
Type: String  
Required: No

 ** [WhatIfForecastArn](#API_forecastquery_QueryWhatIfForecast_RequestSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-request-WhatIfForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast to query.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_forecastquery_QueryWhatIfForecast_ResponseSyntax"></a>

```
{
   "Forecast": { 
      "Predictions": { 
         "string" : [ 
            { 
               "Timestamp": "string",
               "Value": number
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_forecastquery_QueryWhatIfForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Forecast](#API_forecastquery_QueryWhatIfForecast_ResponseSyntax) **   <a name="forecast-forecastquery_QueryWhatIfForecast-response-Forecast"></a>
Provides information about a forecast. Returned as part of the [QueryForecast](API_forecastquery_QueryForecast.md) response.  
Type: [Forecast](API_forecastquery_Forecast.md) object

## Errors
<a name="API_forecastquery_QueryWhatIfForecast_Errors"></a>

 ** InvalidInputException **   
The value is invalid or is too long.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The token is not valid. Tokens expire after 24 hours.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of requests per second has been exceeded.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find that resource. Check the information that you've provided and try again.  
HTTP Status Code: 400

## See Also
<a name="API_forecastquery_QueryWhatIfForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecastquery-2018-06-26/QueryWhatIfForecast) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecastquery-2018-06-26/QueryWhatIfForecast) 