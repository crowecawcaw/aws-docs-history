# DeleteAnomalyDetector

 Deletes the specified anomaly detection model from your account. For more information
 about how to delete an anomaly detection model, see [Deleting an anomaly detection model](../monitoring/Create_Anomaly_Detection_Alarm.md#Delete_Anomaly_Detection_Model "../monitoring/Create_Anomaly_Detection_Alarm.md#Delete_Anomaly_Detection_Model") in the *CloudWatch User
 Guide*. 


## Request Parameters





**Dimensions** 



*This parameter has been deprecated.*



The metric dimensions associated with the anomaly detection model to delete.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**MetricMathAnomalyDetector** 


The metric math anomaly detector to be deleted.


When using `MetricMathAnomalyDetector`, you cannot include following
 parameters in the same operation:



* `Dimensions`,
* `MetricName`
* `Namespace`
* `Stat`
* the `SingleMetricAnomalyDetector` parameters of
 `DeleteAnomalyDetectorInput`

Instead, specify the metric math anomaly detector attributes as part of the
 `MetricMathAnomalyDetector` property.


Type: [MetricMathAnomalyDetector](API_MetricMathAnomalyDetector.md "API_MetricMathAnomalyDetector.md") object


Required: No




**MetricName** 



*This parameter has been deprecated.*



The metric name associated with the anomaly detection model to delete.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Namespace** 



*This parameter has been deprecated.*



The namespace associated with the anomaly detection model to delete.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**SingleMetricAnomalyDetector** 


A single metric anomaly detector to be deleted.


When using `SingleMetricAnomalyDetector`, you cannot include the following
 parameters in the same operation:



* `Dimensions`,
* `MetricName`
* `Namespace`
* `Stat`
* the `MetricMathAnomalyDetector` parameters of
 `DeleteAnomalyDetectorInput`

Instead, specify the single metric anomaly detector attributes as part of the
 `SingleMetricAnomalyDetector` property.


Type: [SingleMetricAnomalyDetector](API_SingleMetricAnomalyDetector.md "API_SingleMetricAnomalyDetector.md") object


Required: No




**Stat** 



*This parameter has been deprecated.*



The statistic associated with the anomaly detection model to delete.


Type: String


Length Constraints: Maximum length of 50.


Pattern: `(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)`



Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterCombination** 


Parameters were used together that cannot be used together.





**message** 





HTTP Status Code: 400




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




**ResourceNotFoundException** 


The named resource does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAnomalyDetector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAnomalyDetector")
