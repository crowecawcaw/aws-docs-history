Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeForecastExportJob

Describes a forecast export job created using the [CreateForecastExportJob](API_CreateForecastExportJob.md "API_CreateForecastExportJob.md") operation.

In addition to listing the properties provided by the user in the
`CreateForecastExportJob` request, this operation lists the following
properties:

- `CreationTime`
- `LastModificationTime`
- `Status`
- `Message` - If an error occurred, information about the error.

## Request Syntax

```
{
   "ForecastExportJobArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ForecastExportJobArn](#API_DescribeForecastExportJob_RequestSyntax "#API_DescribeForecastExportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the forecast export job.

Type: String

Length Constraints: Maximum length of 256.

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
   "ForecastArn": "***string***",
   "ForecastExportJobArn": "***string***",
   "ForecastExportJobName": "***string***",
   "Format": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

When the forecast export job was created.

Type: Timestamp

**[Destination](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

**[ForecastArn](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the exported forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ForecastExportJobArn](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The ARN of the forecast export job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ForecastExportJobName](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The name of the forecast export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[Format](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The format of the exported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

**[LastModificationTime](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[Status](#API_DescribeForecastExportJob_ResponseSyntax "#API_DescribeForecastExportJob_ResponseSyntax")**

The status of the forecast export job. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the forecast export job must be `ACTIVE` before
you can access the forecast in your S3 bucket.

Type: String

Length Constraints: Maximum length of 256.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/cli2/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/boto3/forecast-2018-06-26/DescribeForecastExportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeForecastExportJob.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeForecastExportJob.md")
