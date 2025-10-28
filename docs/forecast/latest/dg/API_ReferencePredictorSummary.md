Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ReferencePredictorSummary

Provides a summary of the reference predictor used when retraining or upgrading a
predictor.

## Contents

**Arn**

The ARN of the reference predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**State**

Whether the reference predictor is `Active` or `Deleted`.

Type: String

Valid Values: `Active | Deleted`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ReferencePredictorSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/ReferencePredictorSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ReferencePredictorSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ReferencePredictorSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ReferencePredictorSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ReferencePredictorSummary.md")
