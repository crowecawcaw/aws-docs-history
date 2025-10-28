Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DataConfig

The data configuration for your dataset group and any additional datasets.

## Contents

**DatasetGroupArn**

The ARN of the dataset group used to train the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**AdditionalDatasets**

Additional built-in datasets like Holidays and the Weather Index.

Type: Array of [AdditionalDataset](API_AdditionalDataset.md "API_AdditionalDataset.md") objects

Array Members: Minimum number of 1 item. Maximum number of 2 items.

Required: No

**AttributeConfigs**

Aggregation and filling options for attributes in your dataset group.

Type: Array of [AttributeConfig](API_AttributeConfig.md "API_AttributeConfig.md") objects

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DataConfig.md "../../../goto/SdkForCpp/forecast-2018-06-26/DataConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DataConfig.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DataConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DataConfig.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DataConfig.md")
