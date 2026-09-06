

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DescribePredictorBacktestExportJob
<a name="API_DescribePredictorBacktestExportJob"></a>

Describes a predictor backtest export job created using the [CreatePredictorBacktestExportJob](API_CreatePredictorBacktestExportJob.md) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

In addition to listing the properties provided by the user in the `CreatePredictorBacktestExportJob` request, this operation lists the following properties:
+  `CreationTime` 
+  `LastModificationTime` 
+  `Status` 
+  `Message` (if an error occurred)

## Request Syntax
<a name="API_DescribePredictorBacktestExportJob_RequestSyntax"></a>

```
{
   "PredictorBacktestExportJobArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePredictorBacktestExportJob_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [PredictorBacktestExportJobArn](#API_DescribePredictorBacktestExportJob_RequestSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-request-PredictorBacktestExportJobArn"></a>
The Amazon Resource Name (ARN) of the predictor backtest export job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribePredictorBacktestExportJob_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "Destination": { 
      "S3Config": { 
         "KMSKeyArn": "string",
         "Path": "string",
         "RoleArn": "string"
      }
   },
   "Format": "string",
   "LastModificationTime": number,
   "Message": "string",
   "PredictorArn": "string",
   "PredictorBacktestExportJobArn": "string",
   "PredictorBacktestExportJobName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribePredictorBacktestExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-CreationTime"></a>
When the predictor backtest export job was created.  
Type: Timestamp

 ** [Destination](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-Destination"></a>
The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast to access the location, and an AWS Key Management Service (KMS) key (optional).   
Type: [DataDestination](API_DataDestination.md) object

 ** [Format](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-Format"></a>
The format of the exported data, CSV or PARQUET.  
Type: String  
Length Constraints: Maximum length of 7.  
Pattern: `^CSV|PARQUET$` 

 ** [LastModificationTime](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp

 ** [Message](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-Message"></a>
Information about any errors that may have occurred during the backtest export.  
Type: String

 ** [PredictorArn](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-PredictorArn"></a>
The Amazon Resource Name (ARN) of the predictor.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [PredictorBacktestExportJobArn](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-PredictorBacktestExportJobArn"></a>
The Amazon Resource Name (ARN) of the predictor backtest export job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [PredictorBacktestExportJobName](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-PredictorBacktestExportJobName"></a>
The name of the predictor backtest export job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

 ** [Status](#API_DescribePredictorBacktestExportJob_ResponseSyntax) **   <a name="forecast-DescribePredictorBacktestExportJob-response-Status"></a>
The status of the predictor backtest export job. States include:   
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
Type: String  
Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribePredictorBacktestExportJob_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribePredictorBacktestExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DescribePredictorBacktestExportJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DescribePredictorBacktestExportJob) 