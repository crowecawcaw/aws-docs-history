Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# MonitorSummary

Provides a summary of the monitor properties used in the [ListMonitors](API_ListMonitors.md "API_ListMonitors.md") operation. To get a complete set of properties,
call the [DescribeMonitor](API_DescribeMonitor.md "API_DescribeMonitor.md") operation, and provide the listed
`MonitorArn`.

## Contents

**CreationTime**

When the monitor resource was created.

Type: Timestamp

Required: No

**LastModificationTime**

The last time the monitor resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `STOPPED` - When the resource stopped.
- `ACTIVE` or `CREATE_FAILED` - When the monitor creation finished or
  failed.

Type: Timestamp

Required: No

**MonitorArn**

The Amazon Resource Name (ARN) of the monitor resource.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**MonitorName**

The name of the monitor resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) of the predictor being monitored.

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

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/MonitorSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/MonitorSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/MonitorSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/MonitorSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/MonitorSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/MonitorSummary.md")
