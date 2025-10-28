Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# SchemaAttribute

An attribute of a schema, which defines a dataset field. A schema attribute is required
for every field in a dataset. The [Schema](API_Schema.md "API_Schema.md") object contains an array of
`SchemaAttribute` objects.

## Contents

**AttributeName**

The name of the dataset field.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**AttributeType**

The data type of the field.

For a related time series dataset, other than date, item_id, and forecast dimensions attributes, all attributes should be of numerical type (integer/float).

Type: String

Valid Values: `string | integer | float | timestamp | geolocation`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/SchemaAttribute.md "../../../goto/SdkForCpp/forecast-2018-06-26/SchemaAttribute.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/SchemaAttribute.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/SchemaAttribute.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/SchemaAttribute.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/SchemaAttribute.md")
