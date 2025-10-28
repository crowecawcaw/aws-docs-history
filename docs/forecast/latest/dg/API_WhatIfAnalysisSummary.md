Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# WhatIfAnalysisSummary

Provides a summary of the what-if analysis properties used in the [ListWhatIfAnalyses](API_ListWhatIfAnalyses.md "API_ListWhatIfAnalyses.md") operation. To get the complete set of properties, call the [DescribeWhatIfAnalysis](API_DescribeWhatIfAnalysis.md "API_DescribeWhatIfAnalysis.md") operation, and provide the `WhatIfAnalysisArn` that is listed in the summary.

## Contents

**CreationTime**

When the what-if analysis was created.

Type: Timestamp

Required: No

**ForecastArn**

The Amazon Resource Name (ARN) of the baseline forecast that is being used in this what-if analysis.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

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

The status of the what-if analysis. States include:

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

**WhatIfAnalysisArn**

The Amazon Resource Name (ARN) of the what-if analysis.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**WhatIfAnalysisName**

The name of the what-if analysis.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/WhatIfAnalysisSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/WhatIfAnalysisSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/WhatIfAnalysisSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/WhatIfAnalysisSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/WhatIfAnalysisSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/WhatIfAnalysisSummary.md")
