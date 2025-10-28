# MetricAttributionOutput

The output configuration details for a metric attribution.

## Contents

**roleArn**

The Amazon Resource Name (ARN) of the IAM service role that has permissions to add data to your output Amazon S3 bucket and add metrics to Amazon CloudWatch. For more information, see [Measuring impact of recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: Yes

**s3DataDestination**

The configuration details of an Amazon S3 input or output bucket.

Type: [S3DataConfig](API_S3DataConfig.md "API_S3DataConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttributionOutput.md "../../../goto/SdkForCpp/personalize-2018-05-22/MetricAttributionOutput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttributionOutput.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/MetricAttributionOutput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttributionOutput.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/MetricAttributionOutput.md")
