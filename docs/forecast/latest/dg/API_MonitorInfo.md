Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# MonitorInfo

Provides information about the monitor resource.

## Contents

**MonitorArn**

The Amazon Resource Name (ARN) of the monitor resource.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**Status**

The status of the monitor. States include:

- `ACTIVE`
- `ACTIVE_STOPPING`, `ACTIVE_STOPPED`
- `UPDATE_IN_PROGRESS`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED`

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/MonitorInfo.md "../../../goto/SdkForCpp/forecast-2018-06-26/MonitorInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/MonitorInfo.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/MonitorInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/MonitorInfo.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/MonitorInfo.md")
