Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeExplainability

Describes an Explainability resource created using the [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "ExplainabilityArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ExplainabilityArn](#API_DescribeExplainability_RequestSyntax "#API_DescribeExplainability_RequestSyntax")**

The Amazon Resource Name (ARN) of the Explaianability to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "DataSource": {
      "S3Config": {
         "KMSKeyArn": "***string***",
         "Path": "***string***",
         "RoleArn": "***string***"
      }
   },
   "EnableVisualization": ***boolean***,
   "EndDateTime": "***string***",
   "EstimatedTimeRemainingInMinutes": ***number***,
   "ExplainabilityArn": "***string***",
   "ExplainabilityConfig": {
      "TimePointGranularity": "***string***",
      "TimeSeriesGranularity": "***string***"
   },
   "ExplainabilityName": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "ResourceArn": "***string***",
   "Schema": {
      "Attributes": [
         {
            "AttributeName": "***string***",
            "AttributeType": "***string***"
         }
      ]
   },
   "StartDateTime": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

When the Explainability resource was created.

Type: Timestamp

**[DataSource](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The source of your data, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast to
access the data and, optionally, an AWS Key Management Service (KMS) key.

Type: [DataSource](API_DataSource.md "API_DataSource.md") object

**[EnableVisualization](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

Whether the visualization was enabled for the Explainability resource.

Type: Boolean

**[EndDateTime](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

If `TimePointGranularity` is set to `SPECIFIC`, the last time
point in the Explainability.

Type: String

Length Constraints: Maximum length of 19.

Pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$`

**[EstimatedTimeRemainingInMinutes](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The estimated time remaining in minutes for the [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md")
job to complete.

Type: Long

**[ExplainabilityArn](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The Amazon Resource Name (ARN) of the Explainability.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ExplainabilityConfig](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The configuration settings that define the granularity of time series and time points
for the Explainability.

Type: [ExplainabilityConfig](API_ExplainabilityConfig.md "API_ExplainabilityConfig.md") object

**[ExplainabilityName](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The name of the Explainability.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[LastModificationTime](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

If an error occurred, a message about the error.

Type: String

**[ResourceArn](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the
Explainability resource.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[Schema](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

Defines the fields of a dataset.

Type: [Schema](API_Schema.md "API_Schema.md") object

**[StartDateTime](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

If `TimePointGranularity` is set to `SPECIFIC`, the first time
point in the Explainability.

Type: String

Length Constraints: Maximum length of 19.

Pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$`

**[Status](#API_DescribeExplainability_ResponseSyntax "#API_DescribeExplainability_ResponseSyntax")**

The status of the Explainability resource. States include:

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeExplainability.md "../../../goto/cli2/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeExplainability.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeExplainability.md "../../../goto/boto3/forecast-2018-06-26/DescribeExplainability.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeExplainability.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeExplainability.md")
