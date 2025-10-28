Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# InputDataConfig

###### Note

This object belongs to the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation. If you created
your predictor with [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md"), see [DataConfig](API_DataConfig.md "API_DataConfig.md").

The data used to train a predictor. The data includes a dataset group and any
supplementary features. You specify this object in the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md")
request.

## Contents

**DatasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**SupplementaryFeatures**

An array of supplementary features. The only supported feature is a holiday
calendar.

Type: Array of [SupplementaryFeature](API_SupplementaryFeature.md "API_SupplementaryFeature.md") objects

Array Members: Minimum number of 1 item. Maximum number of 2 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/InputDataConfig.md "../../../goto/SdkForCpp/forecast-2018-06-26/InputDataConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/InputDataConfig.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/InputDataConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/InputDataConfig.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/InputDataConfig.md")
