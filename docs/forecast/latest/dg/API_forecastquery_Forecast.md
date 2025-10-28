Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Forecast

Provides information about a forecast. Returned as part of the [QueryForecast](API_forecastquery_QueryForecast.md "API_forecastquery_QueryForecast.md") response.

## Contents

**Predictions**

The forecast.

The _string_ of the string-to-array map is one of the following
values:

- p10
- p50
- p90

The default setting is `["0.1", "0.5", "0.9"]`. Use the optional `ForecastTypes` parameter of the [CreateForecast](API_CreateForecast.md "API_CreateForecast.md") operation to change the values. The values will vary depending on how this is set, with a minimum of `1` and a maximum of `5.`

Type: String to array of [DataPoint](API_forecastquery_DataPoint.md "API_forecastquery_DataPoint.md") objects map

Key Length Constraints: Maximum length of 4.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecastquery-2018-06-26/Forecast.md "../../../goto/SdkForCpp/forecastquery-2018-06-26/Forecast.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecastquery-2018-06-26/Forecast.md "../../../goto/SdkForJavaV2/forecastquery-2018-06-26/Forecast.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecastquery-2018-06-26/Forecast.md "../../../goto/SdkForRubyV3/forecastquery-2018-06-26/Forecast.md")
