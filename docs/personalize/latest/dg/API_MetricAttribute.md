# MetricAttribute

Contains information on a metric that a metric attribution reports on. For more information, see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

## Contents

**eventType**

The metric's event type.

Type: String

Length Constraints: Maximum length of 256.

Required: Yes

**expression**

The attribute's expression. Available functions are `SUM()` or `SAMPLECOUNT()`. For SUM() functions, provide the
dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).

Type: String

Length Constraints: Maximum length of 256.

Required: Yes

**metricName**

The metric's name. The name helps you identify the metric in Amazon CloudWatch or Amazon S3.

Type: String

Length Constraints: Maximum length of 256.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttribute.md "../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttribute.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttribute.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttribute.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttribute.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttribute.md")
