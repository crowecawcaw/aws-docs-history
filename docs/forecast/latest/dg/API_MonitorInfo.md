

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# MonitorInfo
<a name="API_MonitorInfo"></a>

Provides information about the monitor resource.

## Contents
<a name="API_MonitorInfo_Contents"></a>

 ** MonitorArn **   <a name="forecast-Type-MonitorInfo-MonitorArn"></a>
The Amazon Resource Name (ARN) of the monitor resource.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`   
Required: No

 ** Status **   <a name="forecast-Type-MonitorInfo-Status"></a>
The status of the monitor. States include:  
+  `ACTIVE` 
+  `ACTIVE_STOPPING`, `ACTIVE_STOPPED` 
+  `UPDATE_IN_PROGRESS` 
+  `CREATE_PENDING`, `CREATE_IN_PROGRESS`, `CREATE_FAILED` 
+  `DELETE_PENDING`, `DELETE_IN_PROGRESS`, `DELETE_FAILED` 
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_MonitorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/MonitorInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/MonitorInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/MonitorInfo) 