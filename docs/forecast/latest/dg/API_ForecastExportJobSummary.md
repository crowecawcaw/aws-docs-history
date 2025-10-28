Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ForecastExportJobSummary

Provides a summary of the forecast export job properties used in the [ListForecastExportJobs](API_ListForecastExportJobs.md "API_ListForecastExportJobs.md") operation. To get the complete set of properties, call
the [DescribeForecastExportJob](API_DescribeForecastExportJob.md "API_DescribeForecastExportJob.md") operation, and provide the listed
`ForecastExportJobArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the forecast export job was created.

Type: Timestamp

Required: No

**Destination**

The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: No

**ForecastExportJobArn**

The Amazon Resource Name (ARN) of the forecast export job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**ForecastExportJobName**

The name of the forecast export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**LastModificationTime**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

Required: No

**Message**

If an error occurred, an informational message about the error.

Type: String

Required: No

**Status**

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

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ForecastExportJobSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/ForecastExportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ForecastExportJobSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ForecastExportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ForecastExportJobSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ForecastExportJobSummary.md")
