Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Filter

Describes a filter for choosing a subset of objects. Each filter consists of a
condition and a match statement. The condition is either `IS` or
`IS_NOT`, which specifies whether to include or exclude
the objects that match the statement, respectively. The match statement consists of a key and a
value.

## Contents

**Condition**

The condition to apply. To include the objects that match the statement, specify
`IS`. To exclude matching objects, specify `IS_NOT`.

Type: String

Valid Values: `IS | IS_NOT`

Required: Yes

**Key**

The name of the parameter to filter on.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

Required: Yes

**Value**

The value to match.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/Filter.md "../../../goto/SdkForCpp/forecast-2018-06-26/Filter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/Filter.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/Filter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/Filter.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/Filter.md")
