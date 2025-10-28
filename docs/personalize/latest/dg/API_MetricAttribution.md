# MetricAttribution

Contains information on a metric attribution. A metric attribution creates reports on the data that you import into Amazon Personalize.
Depending on how you import the data, you can view reports in Amazon CloudWatch or Amazon S3.
For more information, see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

## Contents

**creationDateTime**

The metric attribution's creation date time.

Type: Timestamp

Required: No

**datasetGroupArn**

The metric attribution's dataset group Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

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

**metricsOutputConfig**

The metric attribution's output configuration.

Type: [MetricAttributionOutput](API_MetricAttributionOutput.md "API_MetricAttributionOutput.md") object

Required: No

**name**

The metric attribution's name.

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

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttribution.md "../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttribution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttribution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttribution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttribution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttribution.md")
