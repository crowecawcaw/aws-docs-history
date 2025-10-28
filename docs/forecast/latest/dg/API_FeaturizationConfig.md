Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# FeaturizationConfig

###### Note

This object belongs to the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation. If you created
your predictor with [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md"), see [AttributeConfig](API_AttributeConfig.md "API_AttributeConfig.md").

In a [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation, the specified algorithm trains a model
using the specified dataset group. You can optionally tell the operation to modify data fields
prior to training a model. These modifications are referred to as
_featurization_.

You define featurization using the `FeaturizationConfig` object. You specify an
array of transformations, one for each field that you want to featurize. You then include the
`FeaturizationConfig` object in your `CreatePredictor` request.
Amazon Forecast applies the featurization to the `TARGET_TIME_SERIES` and
`RELATED_TIME_SERIES` datasets before model training.

You can create multiple featurization configurations. For example, you might call the
`CreatePredictor` operation twice by specifying different featurization
configurations.

## Contents

**ForecastFrequency**

The frequency of predictions in a forecast.

Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example,
"1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:

- Minute - 1-59
- Hour - 1-23
- Day - 1-6
- Week - 1-4
- Month - 1-11
- Year - 1

Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".

The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset
frequency.

When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the
TARGET_TIME_SERIES dataset frequency.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5.

Pattern: `^Y|M|W|D|H|30min|15min|10min|5min|1min$`

Required: Yes

**Featurizations**

An array of featurization (transformation) information for the fields of a dataset.

Type: Array of [Featurization](API_Featurization.md "API_Featurization.md") objects

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Required: No

**ForecastDimensions**

An array of dimension (field) names that specify how to group the generated
forecast.

For example, suppose that you are generating a forecast for item sales across all of your
stores, and your dataset contains a `store_id` field. If you want the sales
forecast for each item by store, you would specify `store_id` as the
dimension.

All forecast dimensions specified in the `TARGET_TIME_SERIES` dataset don't
need to be specified in the `CreatePredictor` request. All forecast dimensions
specified in the `RELATED_TIME_SERIES` dataset must be specified in the
`CreatePredictor` request.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/FeaturizationConfig.md "../../../goto/SdkForCpp/forecast-2018-06-26/FeaturizationConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/FeaturizationConfig.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/FeaturizationConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/FeaturizationConfig.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/FeaturizationConfig.md")
