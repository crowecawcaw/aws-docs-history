

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# DescribeWhatIfForecastExport
<a name="API_DescribeWhatIfForecastExport"></a>

Describes the what-if forecast export created using the [CreateWhatIfForecastExport](API_CreateWhatIfForecastExport.md) operation.

**Important**  
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/) 

In addition to listing the properties provided in the `CreateWhatIfForecastExport` request, this operation lists the following properties:
+  `CreationTime` 
+  `LastModificationTime` 
+  `Message` - If an error occurred, information about the error.
+  `Status` 

## Request Syntax
<a name="API_DescribeWhatIfForecastExport_RequestSyntax"></a>

```
{
   "WhatIfForecastExportArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWhatIfForecastExport_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [WhatIfForecastExportArn](#API_DescribeWhatIfForecastExport_RequestSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-request-WhatIfForecastExportArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast export that you are interested in.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: Yes

## Response Syntax
<a name="API_DescribeWhatIfForecastExport_ResponseSyntax"></a>

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
   "EstimatedTimeRemainingInMinutes": number,
   "Format": "string",
   "LastModificationTime": number,
   "Message": "string",
   "Status": "string",
   "WhatIfForecastArns": [ "string" ],
   "WhatIfForecastExportArn": "string",
   "WhatIfForecastExportName": "string"
}
```

## Response Elements
<a name="API_DescribeWhatIfForecastExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-CreationTime"></a>
When the what-if forecast export was created.  
Type: Timestamp

 ** [Destination](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-Destination"></a>
The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast to access the location, and an AWS Key Management Service (KMS) key (optional).   
Type: [DataDestination](API_DataDestination.md) object

 ** [EstimatedTimeRemainingInMinutes](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-EstimatedTimeRemainingInMinutes"></a>
The approximate time remaining to complete the what-if forecast export, in minutes.  
Type: Long

 ** [Format](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-Format"></a>
The format of the exported data, CSV or PARQUET.  
Type: String  
Length Constraints: Maximum length of 7.  
Pattern: `^CSV|PARQUET$` 

 ** [LastModificationTime](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp

 ** [Message](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-Message"></a>
If an error occurred, an informational message about the error.  
Type: String

 ** [Status](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-Status"></a>
The status of the what-if forecast. States include:  
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
The `Status` of the what-if forecast export must be `ACTIVE` before you can access the forecast export.
Type: String  
Length Constraints: Maximum length of 256.

 ** [WhatIfForecastArns](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-WhatIfForecastArns"></a>
An array of Amazon Resource Names (ARNs) that represent all of the what-if forecasts exported in this resource.  
Type: Array of strings  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [WhatIfForecastExportArn](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-WhatIfForecastExportArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast export.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+` 

 ** [WhatIfForecastExportName](#API_DescribeWhatIfForecastExport_ResponseSyntax) **   <a name="forecast-DescribeWhatIfForecastExport-response-WhatIfForecastExportName"></a>
The name of the what-if forecast export.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*` 

## Errors
<a name="API_DescribeWhatIfForecastExport_Errors"></a>

 ** InvalidInputException **   
We can't process the request because it includes an invalid value or a value that exceeds the valid range.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeWhatIfForecastExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/forecast-2018-06-26/DescribeWhatIfForecastExport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfForecastExport) 