Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ExplainabilityExportSummary

Provides a summary of the Explainability export properties used in the [ListExplainabilityExports](API_ListExplainabilityExports.md "API_ListExplainabilityExports.md") operation. To get a complete set of
properties, call the [DescribeExplainabilityExport](API_DescribeExplainabilityExport.md "API_DescribeExplainabilityExport.md") operation, and
provide the `ExplainabilityExportArn`.

## Contents

**CreationTime**

When the Explainability was created.

Type: Timestamp

Required: No

**Destination**

The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast
to access the location, and an AWS Key Management Service (KMS) key (optional).

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: No

**ExplainabilityExportArn**

The Amazon Resource Name (ARN) of the Explainability export.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**ExplainabilityExportName**

The name of the Explainability export

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**LastModificationTime**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

Required: No

**Message**

Information about any errors that may have occurred during the Explainability
export.

Type: String

Required: No

**Status**

The status of the Explainability export. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ExplainabilityExportSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/ExplainabilityExportSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ExplainabilityExportSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ExplainabilityExportSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ExplainabilityExportSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ExplainabilityExportSummary.md")
