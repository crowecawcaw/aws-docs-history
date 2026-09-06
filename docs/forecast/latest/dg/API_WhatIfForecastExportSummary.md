

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# WhatIfForecastExportSummary
<a name="API_WhatIfForecastExportSummary"></a>

Provides a summary of the what-if forecast export properties used in the [ListWhatIfForecastExports](API_ListWhatIfForecastExports.md) operation. To get the complete set of properties, call the [DescribeWhatIfForecastExport](API_DescribeWhatIfForecastExport.md) operation, and provide the `WhatIfForecastExportArn` that is listed in the summary.

## Contents
<a name="API_WhatIfForecastExportSummary_Contents"></a>

 ** CreationTime **   <a name="forecast-Type-WhatIfForecastExportSummary-CreationTime"></a>
When the what-if forecast export was created.  
Type: Timestamp  
Required: No

 ** Destination **   <a name="forecast-Type-WhatIfForecastExportSummary-Destination"></a>
The path to the Amazon Simple Storage Service (Amazon S3) bucket where the forecast is exported.  
Type: [DataDestination](API_DataDestination.md) object  
Required: No

 ** LastModificationTime **   <a name="forecast-Type-WhatIfForecastExportSummary-LastModificationTime"></a>
The last time the resource was modified. The timestamp depends on the status of the job:  
+  `CREATE_PENDING` - The `CreationTime`.
+  `CREATE_IN_PROGRESS` - The current timestamp.
+  `CREATE_STOPPING` - The current timestamp.
+  `CREATE_STOPPED` - When the job stopped.
+  `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.
Type: Timestamp  
Required: No

 ** Message **   <a name="forecast-Type-WhatIfForecastExportSummary-Message"></a>
If an error occurred, an informational message about the error.  
Type: String  
Required: No

 ** Status **   <a name="forecast-Type-WhatIfForecastExportSummary-Status"></a>
The status of the what-if forecast export. States include:  
+  `ACTIVE` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `CREATE_STOPPING`, `CREATE_STOPPED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
The `Status` of the what-if analysis must be `ACTIVE` before you can access the analysis.
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** WhatIfForecastArns **   <a name="forecast-Type-WhatIfForecastExportSummary-WhatIfForecastArns"></a>
An array of Amazon Resource Names (ARNs) that define the what-if forecasts included in the export.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** WhatIfForecastExportArn **   <a name="forecast-Type-WhatIfForecastExportSummary-WhatIfForecastExportArn"></a>
The Amazon Resource Name (ARN) of the what-if forecast export.  
Type: String  
Length Constraints: Maximum length of 300.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** WhatIfForecastExportName **   <a name="forecast-Type-WhatIfForecastExportSummary-WhatIfForecastExportName"></a>
The what-if forecast export name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`   
Required: No

## See Also
<a name="API_WhatIfForecastExportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/WhatIfForecastExportSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/WhatIfForecastExportSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/WhatIfForecastExportSummary) 