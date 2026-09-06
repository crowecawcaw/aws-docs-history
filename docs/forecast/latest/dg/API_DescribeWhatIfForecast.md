

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DescribeWhatIfForecast
<a name="API_DescribeWhatIfForecast"></a>

Describes the what-if forecast created using the [CreateWhatIfForecast](API_CreateWhatIfForecast.md) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

In addition to listing the properties provided in the `CreateWhatIfForecast` request, this operation lists the following properties:
+  `CreationTime` 
+  `LastModificationTime` 
+  `Message` - If an error occurred, information about the error.
+  `Status` 

## Request Syntax
<a name="API_DescribeWhatIfForecast_RequestSyntax"></a>

```
{
   "WhatIfForecastArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWhatIfForecast_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [WhatIfForecastArn](#API_DescribeWhatIfForecast_RequestSyntax) **   <a name="forecast-DescribeWhatIfForecast-request-WhatIfForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast that you are interested in.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribeWhatIfForecast_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EstimatedTimeRemainingInMinutes": number,
   "ForecastTypes": [ "string" ],
   "LastModificationTime": number,
   "Message": "string",
   "Status": "string",
   "TimeSeriesReplacementsDataSource": { 
      "Format": "string",
      "S3Config": { 
         "KMSKeyArn": "string",
         "Path": "string",
         "RoleArn": "string"
      },
      "Schema": { 
         "Attributes": [ 
            { 
               "AttributeName": "string",
               "AttributeType": "string"
            }
         ]
      },
      "TimestampFormat": "string"
   },
   "TimeSeriesTransformations": [ 
      { 
         "Action": { 
            "AttributeName": "string",
            "Operation": "string",
            "Value": number
         },
         "TimeSeriesConditions": [ 
            { 
               "AttributeName": "string",
               "AttributeValue": "string",
               "Condition": "string"
            }
         ]
      }
   ],
   "WhatIfAnalysisArn": "string",
   "WhatIfForecastArn": "string",
   "WhatIfForecastName": "string"
}
```

## Response Elements
<a name="API_DescribeWhatIfForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-CreationTime"></a>
When the what-if forecast was created.  
Type: Timestamp

 ** [EstimatedTimeRemainingInMinutes](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-EstimatedTimeRemainingInMinutes"></a>
The approximate time remaining to complete the what-if forecast, in minutes.  
Type: Long

 ** [ForecastTypes](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-ForecastTypes"></a>
The quantiles at which probabilistic forecasts are generated. You can specify up to five quantiles per what-if forecast in the [CreateWhatIfForecast](API_CreateWhatIfForecast.md) operation. If you didn't specify quantiles, the default values are `["0.1", "0.5", "0.9"]`.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 2. Maximum length of 4.  
Pattern: `(^0?\.\d\d?$|^mean$)` 

 ** [LastModificationTime](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp

 ** [Message](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-Message"></a>
If an error occurred, an informational message about the error.  
Type: String

 ** [Status](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-Status"></a>
The status of the what-if forecast. States include:  
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
The `Status` of the what-if forecast must be `ACTIVE` before you can access the forecast.
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[a-zA-Z0-9\_]+$` 

 ** [TimeSeriesReplacementsDataSource](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-TimeSeriesReplacementsDataSource"></a>
An array of `S3Config`, `Schema`, and `Format` elements that describe the replacement time series.  
Type: [TimeSeriesReplacementsDataSource](API_TimeSeriesReplacementsDataSource.md) object

 ** [TimeSeriesTransformations](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-TimeSeriesTransformations"></a>
An array of `Action` and `TimeSeriesConditions` elements that describe what transformations were applied to which time series.  
Type: Array of [TimeSeriesTransformation](API_TimeSeriesTransformation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [WhatIfAnalysisArn](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-WhatIfAnalysisArn"></a>
The Amazon Resource Name (ARN) of the what-if analysis that contains this forecast.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [WhatIfForecastArn](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-WhatIfForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [WhatIfForecastName](#API_DescribeWhatIfForecast_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecast-response-WhatIfForecastName"></a>
The name of the what-if forecast.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

## Errors
<a name="API_DescribeWhatIfForecast_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeWhatIfForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DescribeWhatIfForecast) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfForecast) 