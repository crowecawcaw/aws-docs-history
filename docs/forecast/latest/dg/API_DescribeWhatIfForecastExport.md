Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeWhatIfForecastExport

Describes the what-if forecast export created using the [CreateWhatIfForecastExport](API_CreateWhatIfForecastExport.md "API_CreateWhatIfForecastExport.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the properties provided in the `CreateWhatIfForecastExport` request, this operation lists the following properties:

- `CreationTime`
- `LastModificationTime`
- `Message` - If an error occurred, information about the error.
- `Status`

## Request Syntax

```
{
   "WhatIfForecastExportArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[WhatIfForecastExportArn](#API_DescribeWhatIfForecastExport_RequestSyntax "#API_DescribeWhatIfForecastExport_RequestSyntax")**

The Amazon Resource Name (ARN) of the what-if forecast export that you are interested in.

Type: String

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "Destination": {
      "S3Config": {
         "KMSKeyArn": "***string***",
         "Path": "***string***",
         "RoleArn": "***string***"
      }
   },
   "EstimatedTimeRemainingInMinutes": ***number***,
   "Format": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "Status": "***string***",
   "WhatIfForecastArns": [ "***string***" ],
   "WhatIfForecastExportArn": "***string***",
   "WhatIfForecastExportName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

When the what-if forecast export was created.

Type: Timestamp

**[Destination](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast
to access the location, and an AWS Key Management Service (KMS) key (optional).

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

**[EstimatedTimeRemainingInMinutes](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The approximate time remaining to complete the what-if forecast export, in minutes.

Type: Long

**[Format](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The format of the exported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

**[LastModificationTime](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[Status](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The status of the what-if forecast. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the what-if forecast export must be `ACTIVE` before you can access the
forecast export.

Type: String

Length Constraints: Maximum length of 256.

**[WhatIfForecastArns](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

An array of Amazon Resource Names (ARNs) that represent all of the what-if forecasts exported in this
resource.

Type: Array of strings

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[WhatIfForecastExportArn](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The Amazon Resource Name (ARN) of the what-if forecast export.

Type: String

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[WhatIfForecastExportName](#API_DescribeWhatIfForecastExport_ResponseSyntax "#API_DescribeWhatIfForecastExport_ResponseSyntax")**

The name of the what-if forecast export.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/cli2/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/boto3/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfForecastExport.md")
