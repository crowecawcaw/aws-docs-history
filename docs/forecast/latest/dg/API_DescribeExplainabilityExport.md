Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeExplainabilityExport

Describes an Explainability export created using the [CreateExplainabilityExport](API_CreateExplainabilityExport.md "API_CreateExplainabilityExport.md") operation.

## Request Syntax

```
{
   "ExplainabilityExportArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ExplainabilityExportArn](#API_DescribeExplainabilityExport_RequestSyntax "#API_DescribeExplainabilityExport_RequestSyntax")**

The Amazon Resource Name (ARN) of the Explainability export.

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
   "ExplainabilityArn": "***string***",
   "ExplainabilityExportArn": "***string***",
   "ExplainabilityExportName": "***string***",
   "Format": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

When the Explainability export was created.

Type: Timestamp

**[Destination](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast
to access the location, and an AWS Key Management Service (KMS) key (optional).

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

**[ExplainabilityArn](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The Amazon Resource Name (ARN) of the Explainability export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ExplainabilityExportArn](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The Amazon Resource Name (ARN) of the Explainability export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ExplainabilityExportName](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The name of the Explainability export.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[Format](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The format of the exported data, CSV or PARQUET.

Type: String

Length Constraints: Maximum length of 7.

Pattern: `^CSV|PARQUET$`

**[LastModificationTime](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

Information about any errors that occurred during the export.

Type: String

**[Status](#API_DescribeExplainabilityExport_ResponseSyntax "#API_DescribeExplainabilityExport_ResponseSyntax")**

The status of the Explainability export. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/cli2/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/boto3/forecast-2018-06-26/DescribeExplainabilityExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeExplainabilityExport.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeExplainabilityExport.md")
