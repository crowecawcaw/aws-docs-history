

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DescribeAutoPredictor
<a name="API_DescribeAutoPredictor"></a>

Describes a predictor created using the CreateAutoPredictor operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

## Request Syntax
<a name="API_DescribeAutoPredictor_RequestSyntax"></a>

```
{
   "PredictorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAutoPredictor_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PredictorArn](#API_DescribeAutoPredictor_RequestSyntax) **   <a name="forecast-DescribeAutoPredictor-request-PredictorArn"></a>
The Amazon Resource Name (ARN) of the predictor.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribeAutoPredictor_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DataConfig": { 
      "AdditionalDatasets": [ 
         { 
            "Configuration": { 
               "string" : [ "string" ]
            },
            "Name": "string"
         }
      ],
      "AttributeConfigs": [ 
         { 
            "AttributeName": "string",
            "Transformations": { 
               "string" : "string" 
            }
         }
      ],
      "DatasetGroupArn": "string"
   },
   "DatasetImportJobArns": [ "string" ],
   "EncryptionConfig": { 
      "KMSKeyArn": "string",
      "RoleArn": "string"
   },
   "EstimatedTimeRemainingInMinutes": number,
   "ExplainabilityInfo": { 
      "ExplainabilityArn": "string",
      "Status": "string"
   },
   "ForecastDimensions": [ "string" ],
   "ForecastFrequency": "string",
   "ForecastHorizon": number,
   "ForecastTypes": [ "string" ],
   "LastModificationTime": number,
   "Message": "string",
   "MonitorInfo": { 
      "MonitorArn": "string",
      "Status": "string"
   },
   "OptimizationMetric": "string",
   "PredictorArn": "string",
   "PredictorName": "string",
   "ReferencePredictorSummary": { 
      "Arn": "string",
      "State": "string"
   },
   "Status": "string",
   "TimeAlignmentBoundary": { 
      "DayOfMonth": number,
      "DayOfWeek": "string",
      "Hour": number,
      "Month": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAutoPredictor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-CreationTime"></a>
The timestamp of the CreateAutoPredictor request.  
Type: Timestamp

 ** [DataConfig](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-DataConfig"></a>
The data configuration for your dataset group and any additional datasets.  
Type: [DataConfig](API_DataConfig.md) object

 ** [DatasetImportJobArns](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-DatasetImportJobArns"></a>
An array of the ARNs of the dataset import jobs used to import training data for the predictor.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [EncryptionConfig](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-EncryptionConfig"></a>
An AWS Key Management Service (KMS) key and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key. You can specify this optional object in the [CreateDataset](API_CreateDataset.md) and [CreatePredictor](API_CreatePredictor.md) requests.  
Type: [EncryptionConfig](API_EncryptionConfig.md) object

 ** [EstimatedTimeRemainingInMinutes](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-EstimatedTimeRemainingInMinutes"></a>
The estimated time remaining in minutes for the predictor training job to complete.  
Type: Long

 ** [ExplainabilityInfo](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ExplainabilityInfo"></a>
Provides the status and ARN of the Predictor Explainability.  
Type: [ExplainabilityInfo](API_ExplainabilityInfo.md) object

 ** [ForecastDimensions](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ForecastDimensions"></a>
An array of dimension (field) names that specify the attributes used to group your time series.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

 ** [ForecastFrequency](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ForecastFrequency"></a>
The frequency of predictions in a forecast.  
Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "Y" indicates every year and "5min" indicates every five minutes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `^Y|M|W|D|H|30min|15min|10min|5min|1min$` 

 ** [ForecastHorizon](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ForecastHorizon"></a>
The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.  
Type: Integer

 ** [ForecastTypes](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ForecastTypes"></a>
The forecast types used during predictor training. Default value is ["0.1","0.5","0.9"].  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 2. Maximum length of 4.  
Pattern: `(^0?\.\d\d?$|^mean$)` 

 ** [LastModificationTime](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp

 ** [Message](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-Message"></a>
In the event of an error, a message detailing the cause of the error.  
Type: String

 ** [MonitorInfo](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-MonitorInfo"></a>
A [MonitorInfo](API_MonitorInfo.md) object with the Amazon Resource Name (ARN) and status of the monitor resource.  
Type: [MonitorInfo](API_MonitorInfo.md) object

 ** [OptimizationMetric](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-OptimizationMetric"></a>
The accuracy metric used to optimize the predictor.  
Type: String  
Valid Values: `WAPE | RMSE | AverageWeightedQuantileLoss | MASE | MAPE` 

 ** [PredictorArn](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-PredictorArn"></a>
The Amazon Resource Name (ARN) of the predictor  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [PredictorName](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-PredictorName"></a>
The name of the predictor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

 ** [ReferencePredictorSummary](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-ReferencePredictorSummary"></a>
The ARN and state of the reference predictor. This parameter is only valid for retrained or upgraded predictors.  
Type: [ReferencePredictorSummary](API_ReferencePredictorSummary.md) object

 ** [Status](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-Status"></a>
The status of the predictor. States include:   
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
Type: String  
Length Constraints: Maximum length of 256.

 ** [TimeAlignmentBoundary](#API_DescribeAutoPredictor_ResponseSyntax) **   <a name="forecast-DescribeAutoPredictor-response-TimeAlignmentBoundary"></a>
The time boundary Forecast uses when aggregating data.  
Type: [TimeAlignmentBoundary](API_TimeAlignmentBoundary.md) object

## Errors
<a name="API_DescribeAutoPredictor_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeAutoPredictor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DescribeAutoPredictor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DescribeAutoPredictor) 