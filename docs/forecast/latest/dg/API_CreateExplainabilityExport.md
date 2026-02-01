Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreateExplainabilityExport

Exports an Explainability resource created by the [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md") operation. Exported files are exported to an Amazon Simple Storage Service (Amazon
S3) bucket.

You must specify a [DataDestination](API_DataDestination.md "API_DataDestination.md") object that includes an Amazon S3
bucket and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3
bucket. For more information, see [Set Up Permissions for Amazon Forecast](aws-forecast-iam-roles.md "aws-forecast-iam-roles.md").

###### Note

The `Status` of the export job must be `ACTIVE` before you
can access the export in your Amazon S3 bucket. To get the status, use the [DescribeExplainabilityExport](API_DescribeExplainabilityExport.md "API_DescribeExplainabilityExport.md") operation.

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
   "ExplainabilityArn": "`string`",
   "ExplainabilityExportName": "`string`",
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

**[Destination](#API_CreateExplainabilityExport_RequestSyntax "#API_CreateExplainabilityExport_RequestSyntax")**

The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast
to access the location, and an AWS Key Management Service (KMS) key (optional).

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: Yes

**[ExplainabilityArn](#API_CreateExplainabilityExport_RequestSyntax "#API_CreateExplainabilityExport_RequestSyntax")**

The Amazon Resource Name (ARN) of the Explainability to export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**[ExplainabilityExportName](#API_CreateExplainabilityExport_RequestSyntax "#API_CreateExplainabilityExport_RequestSyntax")**

A unique name for the Explainability export.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**[Format](#API_CreateExplainabilityExport_RequestSyntax "#API_CreateExplainabilityExport_RequestSyntax")**

The format of the exported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

Required: No

**[Tags](#API_CreateExplainabilityExport_RequestSyntax "#API_CreateExplainabilityExport_RequestSyntax")**

Optional metadata to help you categorize and organize your resources. Each tag
consists of a key and an optional value, both of which you define. Tag keys and values
are case sensitive.

The following restrictions apply to tags:

- For each resource, each tag key must be unique and each tag key must have one
  value.
- Maximum number of tags per resource: 50.
- Maximum key length: 128 Unicode characters in UTF-8.
- Maximum value length: 256 Unicode characters in UTF-8.
- Accepted characters: all letters and numbers, spaces representable in UTF-8,
  and + - = . \_ : / @. If your tagging schema is used across other services and
  resources, the character restrictions of those services also apply.
- Key prefixes cannot include any upper or lowercase combination of
  `aws:` or `AWS:`. Values can have this prefix. If a
  tag value has `aws` as its prefix but the key does not, Forecast
  considers it to be a user tag and will count against the limit of 50 tags. Tags
  with only the key prefix of `aws` do not count against your tags per
  resource limit. You cannot edit or delete tag keys with this prefix.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "ExplainabilityExportArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ExplainabilityExportArn](#API_CreateExplainabilityExport_ResponseSyntax "#API_CreateExplainabilityExport_ResponseSyntax")**

The Amazon Resource Name (ARN) of the export.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/cli2/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/boto3/forecast-2018-06-26/CreateExplainabilityExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateExplainabilityExport.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateExplainabilityExport.md")
