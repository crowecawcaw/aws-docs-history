Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreateForecastExportJob

Exports a forecast created by the [CreateForecast](API_CreateForecast.md "API_CreateForecast.md") operation to your
Amazon Simple Storage Service (Amazon S3) bucket. The forecast file name will match the following conventions:

<ForecastExportJobName>\_<ExportTimestamp>\_<PartNumber>

where the <ExportTimestamp> component is in Java SimpleDateFormat
(yyyy-MM-ddTHH-mm-ssZ).

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

You must specify a [DataDestination](API_DataDestination.md "API_DataDestination.md") object that includes an AWS Identity and Access Management
(IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket. For more information, see
[Set Up Permissions for Amazon Forecast](aws-forecast-iam-roles.md "aws-forecast-iam-roles.md").

For more information, see [Generating Forecasts](howitworks-forecast.md "howitworks-forecast.md").

To get a list of all your forecast export jobs, use the [ListForecastExportJobs](API_ListForecastExportJobs.md "API_ListForecastExportJobs.md") operation.

###### Note

The `Status` of the forecast export job must be `ACTIVE` before
you can access the forecast in your Amazon S3 bucket. To get the status, use the [DescribeForecastExportJob](API_DescribeForecastExportJob.md "API_DescribeForecastExportJob.md") operation.

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
   "ForecastArn": "`string`",
   "ForecastExportJobName": "`string`",
   "Format": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Destination](#API_CreateForecastExportJob_RequestSyntax "#API_CreateForecastExportJob_RequestSyntax")**

The location where you want to save the forecast and an AWS Identity and Access Management (IAM) role that
Amazon Forecast can assume to access the location. The forecast must be exported to an Amazon S3
bucket.

If encryption is used, `Destination` must include an AWS Key Management Service (KMS) key. The
IAM role must allow Amazon Forecast permission to access the key.

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: Yes

**[ForecastArn](#API_CreateForecastExportJob_RequestSyntax "#API_CreateForecastExportJob_RequestSyntax")**

The Amazon Resource Name (ARN) of the forecast that you want to export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**[ForecastExportJobName](#API_CreateForecastExportJob_RequestSyntax "#API_CreateForecastExportJob_RequestSyntax")**

The name for the forecast export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**[Format](#API_CreateForecastExportJob_RequestSyntax "#API_CreateForecastExportJob_RequestSyntax")**

The format of the exported data, CSV or PARQUET. The default value is CSV.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

Required: No

**[Tags](#API_CreateForecastExportJob_RequestSyntax "#API_CreateForecastExportJob_RequestSyntax")**

The optional metadata that you apply to the forecast export job to help you categorize and
organize them. Each tag consists of a key and an optional value, both of which you
define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one
  value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that
  other services may have restrictions on allowed characters. Generally allowed characters
  are: letters, numbers, and spaces representable in UTF-8, and the following characters: +

* = . \_ : / @.

- Tag keys and values are case sensitive.
- Do not use `aws:`, `AWS:`, or any upper or lowercase combination
  of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag
  keys with this prefix. Values can have this prefix. If a tag value has `aws` as
  its prefix but the key does not, then Forecast considers it to be a user tag and will
  count against the limit of 50 tags. Tags with only the key prefix of `aws` do
  not count against your tags per resource limit.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "ForecastExportJobArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ForecastExportJobArn](#API_CreateForecastExportJob_ResponseSyntax "#API_CreateForecastExportJob_ResponseSyntax")**

The Amazon Resource Name (ARN) of the export job.

Type: String

Length Constraints: Maximum length of 256.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/cli2/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/boto3/forecast-2018-06-26/CreateForecastExportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateForecastExportJob.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateForecastExportJob.md")
