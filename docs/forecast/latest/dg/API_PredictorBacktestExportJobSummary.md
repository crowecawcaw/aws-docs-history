Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# PredictorBacktestExportJobSummary

Provides a summary of the predictor backtest export job properties used in the [ListPredictorBacktestExportJobs](API_ListPredictorBacktestExportJobs.md "API_ListPredictorBacktestExportJobs.md") operation. To get a complete set of
properties, call the [DescribePredictorBacktestExportJob](API_DescribePredictorBacktestExportJob.md "API_DescribePredictorBacktestExportJob.md") operation, and
provide the listed `PredictorBacktestExportJobArn`.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreationTime**

When the predictor backtest export job was created.

Type: Timestamp

Required: No

**Destination**

The destination for an export job. Provide an S3 path, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast
to access the location, and an AWS Key Management Service (KMS) key (optional).

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

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

Information about any errors that may have occurred during the backtest export.

Type: String

Required: No

**PredictorBacktestExportJobArn**

The Amazon Resource Name (ARN) of the predictor backtest export job.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**PredictorBacktestExportJobName**

The name of the predictor backtest export job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**Status**

The status of the predictor backtest export job. States include:

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

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/PredictorBacktestExportJobSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/PredictorBacktestExportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorBacktestExportJobSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorBacktestExportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorBacktestExportJobSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorBacktestExportJobSummary.md")
