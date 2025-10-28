# MetricAttributionSummary

Provides a summary of the properties of a metric attribution. For a complete listing, call the [DescribeMetricAttribution](API_DescribeMetricAttribution.md "API_DescribeMetricAttribution.md").

## Contents

**creationDateTime**

The metric attribution's creation date time.

Type: Timestamp

Required: No

**failureReason**

The metric attribution's failure reason.

Type: String

Required: No

**lastUpdatedDateTime**

The metric attribution's last updated date time.

Type: Timestamp

Required: No

**metricAttributionArn**

The metric attribution's Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**name**

The name of the metric attribution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**status**

The metric attribution's status.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttributionSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttributionSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttributionSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttributionSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttributionSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttributionSummary.md")
