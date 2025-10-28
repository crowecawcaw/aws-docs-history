Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Featurization

###### Note

This object belongs to the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation. If you created
your predictor with [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md"), see [AttributeConfig](API_AttributeConfig.md "API_AttributeConfig.md").

Provides featurization (transformation) information for a dataset field. This object is
part of the [FeaturizationConfig](API_FeaturizationConfig.md "API_FeaturizationConfig.md") object.

For example:

`{`

`"AttributeName": "demand",`

`FeaturizationPipeline [ {`

`"FeaturizationMethodName": "filling",`

`"FeaturizationMethodParameters": {"aggregation": "avg", "backfill":
 "nan"}`

`} ]`

`}`

## Contents

**AttributeName**

The name of the schema attribute that specifies the data field to be featurized. Amazon
Forecast supports the target field of the `TARGET_TIME_SERIES` and the
`RELATED_TIME_SERIES` datasets. For example, for the `RETAIL` domain,
the target is `demand`, and for the `CUSTOM` domain, the target is
`target_value`. For more information, see [Handling Missing Values](howitworks-missing-values.md "howitworks-missing-values.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**FeaturizationPipeline**

An array of one `FeaturizationMethod` object that specifies the feature
transformation method.

Type: Array of [FeaturizationMethod](API_FeaturizationMethod.md "API_FeaturizationMethod.md") objects

Array Members: Fixed number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/Featurization.md "../../../goto/SdkForCpp/forecast-2018-06-26/Featurization.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/Featurization.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/Featurization.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/Featurization.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/Featurization.md")
