Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ExplainabilityConfig

The ExplainabilityConfig data type defines the number of time series and time points
included in [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md").

If you provide a predictor ARN for `ResourceArn`, you must set both
`TimePointGranularity` and `TimeSeriesGranularity` to “ALL”.
When creating Predictor Explainability, Amazon Forecast considers all time series and
time points.

If you provide a forecast ARN for `ResourceArn`, you can set
`TimePointGranularity` and `TimeSeriesGranularity` to either
“ALL” or “Specific”.

## Contents

**TimePointGranularity**

To create an Explainability for all time points in your forecast horizon, use
`ALL`. To create an Explainability for specific time points in your
forecast horizon, use `SPECIFIC`.

Specify time points with the `StartDateTime` and `EndDateTime`
parameters within the [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md") operation.

Type: String

Valid Values: `ALL | SPECIFIC`

Required: Yes

**TimeSeriesGranularity**

To create an Explainability for all time series in your datasets, use
`ALL`. To create an Explainability for specific time series in your datasets,
use `SPECIFIC`.

Specify time series by uploading a CSV or Parquet file to an Amazon S3 bucket and set the location
within the [DataDestination](API_DataDestination.md "API_DataDestination.md") data type.

Type: String

Valid Values: `ALL | SPECIFIC`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ExplainabilityConfig.md "../../../goto/SdkForCpp/forecast-2018-06-26/ExplainabilityConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ExplainabilityConfig.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ExplainabilityConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ExplainabilityConfig.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ExplainabilityConfig.md")
