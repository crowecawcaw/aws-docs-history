Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# TestWindowSummary

The status, start time, and end time of a backtest, as well as a failure reason if
applicable.

## Contents

**Message**

If the test failed, the reason why it failed.

Type: String

Required: No

**Status**

The status of the test. Possible status values are:

- `ACTIVE`
- `CREATE_IN_PROGRESS`
- `CREATE_FAILED`

Type: String

Length Constraints: Maximum length of 256.

Required: No

**TestWindowEnd**

The time at which the test ended.

Type: Timestamp

Required: No

**TestWindowStart**

The time at which the test began.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/TestWindowSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/TestWindowSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/TestWindowSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/TestWindowSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/TestWindowSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/TestWindowSummary.md")
