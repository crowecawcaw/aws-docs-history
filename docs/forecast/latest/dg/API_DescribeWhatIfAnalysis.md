

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DescribeWhatIfAnalysis
<a name="API_DescribeWhatIfAnalysis"></a>

Describes the what-if analysis created using the [CreateWhatIfAnalysis](API_CreateWhatIfAnalysis.md) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

In addition to listing the properties provided in the `CreateWhatIfAnalysis` request, this operation lists the following properties:
+  `CreationTime` 
+  `LastModificationTime` 
+  `Message` - If an error occurred, information about the error.
+  `Status` 

## Request Syntax
<a name="API_DescribeWhatIfAnalysis_RequestSyntax"></a>

```
{
   "WhatIfAnalysisArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWhatIfAnalysis_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [WhatIfAnalysisArn](#API_DescribeWhatIfAnalysis_RequestSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-request-WhatIfAnalysisArn"></a>
The Amazon Resource Name (ARN) of the what-if analysis that you are interested in.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribeWhatIfAnalysis_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EstimatedTimeRemainingInMinutes": number,
   "ForecastArn": "string",
   "LastModificationTime": number,
   "Message": "string",
   "Status": "string",
   "TimeSeriesSelector": { 
      "TimeSeriesIdentifiers": { 
         "DataSource": { 
            "S3Config": { 
               "KMSKeyArn": "string",
               "Path": "string",
               "RoleArn": "string"
            }
         },
         "Format": "string",
         "Schema": { 
            "Attributes": [ 
               { 
                  "AttributeName": "string",
                  "AttributeType": "string"
               }
            ]
         }
      }
   },
   "WhatIfAnalysisArn": "string",
   "WhatIfAnalysisName": "string"
}
```

## Response Elements
<a name="API_DescribeWhatIfAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-CreationTime"></a>
When the what-if analysis was created.  
Type: Timestamp

 ** [EstimatedTimeRemainingInMinutes](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-EstimatedTimeRemainingInMinutes"></a>
The approximate time remaining to complete the what-if analysis, in minutes.  
Type: Long

 ** [ForecastArn](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-ForecastArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [LastModificationTime](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp

 ** [Message](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-Message"></a>
If an error occurred, an informational message about the error.  
Type: String

 ** [Status](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-Status"></a>
The status of the what-if analysis. States include:  
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
The `Status` of the what-if analysis must be `ACTIVE` before you can access the analysis.
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[a-zA-Z0-9\_]+$` 

 ** [TimeSeriesSelector](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-TimeSeriesSelector"></a>
Defines the set of time series that are used to create the forecasts in a `TimeSeriesIdentifiers` object.  
The `TimeSeriesIdentifiers` object needs the following information:  
+  `DataSource` 
+  `Format` 
+  `Schema` 
Type: [TimeSeriesSelector](API_TimeSeriesSelector.md) object

 ** [WhatIfAnalysisArn](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-WhatIfAnalysisArn"></a>
The Amazon Resource Name (ARN) of the what-if analysis.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [WhatIfAnalysisName](#API_DescribeWhatIfAnalysis_ResponseSyntax) **   <a name="forecast-DescribeWhatIfAnalysis-response-WhatIfAnalysisName"></a>
The name of the what-if analysis.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

## Errors
<a name="API_DescribeWhatIfAnalysis_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeWhatIfAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DescribeWhatIfAnalysis) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfAnalysis) 