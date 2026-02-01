Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreateWhatIfForecastExport

Exports a forecast created by the [CreateWhatIfForecast](API_CreateWhatIfForecast.md "API_CreateWhatIfForecast.md") operation to your
Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:

`≈<ForecastExportJobName>_<ExportTimestamp>_<PartNumber>`

The <ExportTimestamp> component is in Java SimpleDateFormat
(yyyy-MM-ddTHH-mm-ssZ).

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

You must specify a [DataDestination](API_DataDestination.md "API_DataDestination.md") object that includes an AWS Identity and Access Management
(IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see
[Set Up Permissions for Amazon Forecast](aws-forecast-iam-roles.md "aws-forecast-iam-roles.md").

For more information, see [Generating Forecasts](howitworks-forecast.md "howitworks-forecast.md").

To get a list of all your what-if forecast export jobs, use the [ListWhatIfForecastExports](API_ListWhatIfForecastExports.md "API_ListWhatIfForecastExports.md")
operation.

###### Note

The `Status` of the forecast export job must be `ACTIVE` before
you can access the forecast in your Amazon S3 bucket. To get the status, use the [DescribeWhatIfForecastExport](API_DescribeWhatIfForecastExport.md "API_DescribeWhatIfForecastExport.md") operation.

## Request Syntax

```
{
   "Destination": {
      "S3Config": {
         "KMSKeyArn": "`string`",
         "Path": "`string`",
         "RoleArn": "`string`"
      }
   },
   "Format": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "WhatIfForecastArns": [ "`string`" ],
   "WhatIfForecastExportName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Destination](#API_CreateWhatIfForecastExport_RequestSyntax "#API_CreateWhatIfForecastExport_RequestSyntax")**

The location where you want to save the forecast and an AWS Identity and Access Management (IAM) role that
Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3
bucket.

If encryption is used, `Destination` must include an AWS Key Management Service (KMS) key. The
IAM role must allow Amazon Forecast permission to access the key.

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: Yes

**[Format](#API_CreateWhatIfForecastExport_RequestSyntax "#API_CreateWhatIfForecastExport_RequestSyntax")**

The format of the exported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

Required: No

**[Tags](#API_CreateWhatIfForecastExport_RequestSyntax "#API_CreateWhatIfForecastExport_RequestSyntax")**

A list of [tags](tagging-forecast-resources.md "tagging-forecast-resources.md") to apply to the what if forecast.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[WhatIfForecastArns](#API_CreateWhatIfForecastExport_RequestSyntax "#API_CreateWhatIfForecastExport_RequestSyntax")**

The list of what-if forecast Amazon Resource Names (ARNs) to export.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**[WhatIfForecastExportName](#API_CreateWhatIfForecastExport_RequestSyntax "#API_CreateWhatIfForecastExport_RequestSyntax")**

The name of the what-if forecast to export.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

## Response Syntax

```
{
   "WhatIfForecastExportArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[WhatIfForecastExportArn](#API_CreateWhatIfForecastExport_ResponseSyntax "#API_CreateWhatIfForecastExport_ResponseSyntax")**

The Amazon Resource Name (ARN) of the what-if forecast.

Type: String

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of resources per account has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

There is already a resource with this name. Try again with a different name.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/cli2/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/boto3/forecast-2018-06-26/CreateWhatIfForecastExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateWhatIfForecastExport.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateWhatIfForecastExport.md")
