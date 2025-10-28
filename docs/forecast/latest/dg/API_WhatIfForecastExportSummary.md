Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# WhatIfForecastExportSummary

Provides a summary of the what-if forecast export properties used in the [ListWhatIfForecastExports](API_ListWhatIfForecastExports.md "API_ListWhatIfForecastExports.md") operation. To get the complete set of properties, call the [DescribeWhatIfForecastExport](API_DescribeWhatIfForecastExport.md "API_DescribeWhatIfForecastExport.md") operation, and provide the `WhatIfForecastExportArn` that is listed in the summary.

## Contents

**CreationTime**

When the what-if forecast export was created.

Type: Timestamp

Required: No

**Destination**

The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.

Type: [DataDestination](API_DataDestination.md "API_DataDestination.md") object

Required: No

**LastModificationTime**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

Required: No

**Message**

If an error occurred, an informational message about the error.

Type: String

Required: No

**Status**

The status of the what-if forecast export. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the what-if analysis must be `ACTIVE` before you can access the
analysis.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**WhatIfForecastArns**

An array of Amazon Resource Names (ARNs) that define the what-if forecasts included in the export.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**WhatIfForecastExportArn**

The Amazon Resource Name (ARN) of the what-if forecast export.

Type: String

Length Constraints: Maximum length of 300.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**WhatIfForecastExportName**

The what-if forecast export name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/WhatIfForecastExportSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/WhatIfForecastExportSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/WhatIfForecastExportSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/WhatIfForecastExportSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/WhatIfForecastExportSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/WhatIfForecastExportSummary.md")
