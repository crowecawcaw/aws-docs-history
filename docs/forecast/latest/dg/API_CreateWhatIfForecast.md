

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# CreateWhatIfForecast
<a name="API_CreateWhatIfForecast"></a>

A what-if forecast is a forecast that is created from a modified version of the baseline forecast. Each what-if forecast incorporates either a replacement dataset or a set of transformations to the original dataset. 

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_CreateWhatIfForecast_RequestSyntax"></a>

```
{
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimeSeriesReplacementsDataSource": { 
      "Format": "{{string}}",
      "S3Config": { 
         "KMSKeyArn": "{{string}}",
         "Path": "{{string}}",
         "RoleArn": "{{string}}"
      },
      "Schema": { 
         "Attributes": [ 
            { 
               "AttributeName": "{{string}}",
               "AttributeType": "{{string}}"
            }
         ]
      },
      "TimestampFormat": "{{string}}"
   },
   "TimeSeriesTransformations": [ 
      { 
         "Action": { 
            "AttributeName": "{{string}}",
            "Operation": "{{string}}",
            "Value": {{number}}
         },
         "TimeSeriesConditions": [ 
            { 
               "AttributeName": "{{string}}",
               "AttributeValue": "{{string}}",
               "Condition": "{{string}}"
            }
         ]
      }
   ],
   "WhatIfAnalysisArn": "{{string}}",
   "WhatIfForecastName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateWhatIfForecast_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_CreateWhatIfForecast_RequestSyntax) **   <a name="forecast-CreateWhatIfForecast-request-Tags"></a>
A list of [tags](https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html) to apply to the what if forecast.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [TimeSeriesReplacementsDataSource](#API_CreateWhatIfForecast_RequestSyntax) **   <a name="forecast-CreateWhatIfForecast-request-TimeSeriesReplacementsDataSource"></a>
The replacement time series dataset, which contains the rows that you want to change in the related time series dataset. A replacement time series does not need to contain all rows that are in the baseline related time series. Include only the rows (measure-dimension combinations) that you want to include in the what-if forecast.  
This dataset is merged with the original time series to create a transformed dataset that is used for the what-if analysis.  
This dataset should contain the items to modify (such as item\_id or workforce\_type), any relevant dimensions, the timestamp column, and at least one of the related time series columns. This file should not contain duplicate timestamps for the same time series. This file must be in CSV format.  
Timestamps and item\_ids not included in this dataset are not included in the what-if analysis.   
Type: [TimeSeriesReplacementsDataSource](API_TimeSeriesReplacementsDataSource.md) object  
Required: No

 ** [TimeSeriesTransformations](#API_CreateWhatIfForecast_RequestSyntax) **   <a name="forecast-CreateWhatIfForecast-request-TimeSeriesTransformations"></a>
The transformations that are applied to the baseline time series. Each transformation contains an action and a set of conditions. An action is applied only when all conditions are met. If no conditions are provided, the action is applied to all items.  
Type: Array of [TimeSeriesTransformation](API_TimeSeriesTransformation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 30 items.  
Required: No

 ** [WhatIfAnalysisArn](#API_CreateWhatIfForecast_RequestSyntax) **   <a name="forecast-CreateWhatIfForecast-request-WhatIfAnalysisArn"></a>
The Amazon Resource Name (ARN) of the what-if analysis.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

 ** [WhatIfForecastName](#API_CreateWhatIfForecast_RequestSyntax) **   <a name="forecast-CreateWhatIfForecast-request-WhatIfForecastName"></a>
The name of the what-if forecast. Names must be unique within each what-if analysis.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: Yes

## Response Syntax
<a name="API_CreateWhatIfForecast_ResponseSyntax"></a>

```
{
   "WhatIfForecastArn": "string"
}
```

## Response Elements
<a name="API_CreateWhatIfForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WhatIfForecastArn](#API_CreateWhatIfForecast_ResponseSyntax) **   <a name="forecast-CreateWhatIfForecast-response-WhatIfForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

## Errors
<a name="API_CreateWhatIfForecast_Errors"></a>

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
<a name="API_CreateWhatIfForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/CreateWhatIfForecast) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/CreateWhatIfForecast) 