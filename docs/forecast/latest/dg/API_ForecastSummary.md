Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ForecastSummary

Provides a summary of the forecast properties used in the [ListForecasts](API_ListForecasts.md "API_ListForecasts.md")
operation. To get the complete set of properties, call the [DescribeForecast](API_DescribeForecast.md "API_DescribeForecast.md")
operation, and provide the `ForecastArn` that is listed in the summary.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Contents

**CreatedUsingAutoPredictor**

Whether the Forecast was created from an AutoPredictor.

Type: Boolean

Required: No

**CreationTime**

When the forecast creation task was created.

Type: Timestamp

Required: No

**DatasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group that provided the data used to train
the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

Required: No

**ForecastArn**

The ARN of the forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**ForecastName**

The name of the forecast.

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

**PredictorArn**

The ARN of the predictor used to generate the forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

Required: No

**Status**

The status of the forecast. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the forecast must be `ACTIVE` before you can query
or export the forecast.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ForecastSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/ForecastSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ForecastSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ForecastSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ForecastSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ForecastSummary.md")
