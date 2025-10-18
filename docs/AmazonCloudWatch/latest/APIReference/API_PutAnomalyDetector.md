# PutAnomalyDetector

Creates an anomaly detection model for a CloudWatch metric. You can use the model to
 display a band of expected normal values when the metric is graphed.

If you have enabled unified cross-account observability, and this account is a
 monitoring account, the metric can be in the same account or a source account. You can
 specify the account ID in the object you specify in the
 `SingleMetricAnomalyDetector` parameter.

For more information, see [CloudWatch Anomaly Detection](../monitoring/CloudWatch_Anomaly_Detection.md "../monitoring/CloudWatch_Anomaly_Detection.md").


## Request Parameters





**Configuration** 


The configuration specifies details about how the anomaly detection model is to be
 trained, including time ranges to exclude when training and updating the model. You can
 specify as many as 10 time ranges.


The configuration can also include the time zone to use for the metric.


Type: [AnomalyDetectorConfiguration](API_AnomalyDetectorConfiguration.md "API_AnomalyDetectorConfiguration.md") object


Required: No




**Dimensions** 



*This parameter has been deprecated.*



The metric dimensions to create the anomaly detection model for.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**MetricCharacteristics** 


Use this object to include parameters to provide information about your metric to
 CloudWatch to help it build more accurate anomaly detection models.
 Currently, it includes the `PeriodicSpikes` parameter.


Type: [MetricCharacteristics](API_MetricCharacteristics.md "API_MetricCharacteristics.md") object


Required: No




**MetricMathAnomalyDetector** 


The metric math anomaly detector to be created.


When using `MetricMathAnomalyDetector`, you cannot include the following
 parameters in the same operation:



* `Dimensions`
* `MetricName`
* `Namespace`
* `Stat`
* the `SingleMetricAnomalyDetector` parameters of
 `PutAnomalyDetectorInput`

Instead, specify the metric math anomaly detector attributes as part of the property
 `MetricMathAnomalyDetector`.


Type: [MetricMathAnomalyDetector](API_MetricMathAnomalyDetector.md "API_MetricMathAnomalyDetector.md") object


Required: No




**MetricName** 



*This parameter has been deprecated.*



The name of the metric to create the anomaly detection model for.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Namespace** 



*This parameter has been deprecated.*



The namespace of the metric to create the anomaly detection model for.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**SingleMetricAnomalyDetector** 


A single metric anomaly detector to be created.


When using `SingleMetricAnomalyDetector`, you cannot include the following
 parameters in the same operation:



* `Dimensions`
* `MetricName`
* `Namespace`
* `Stat`
* the `MetricMathAnomalyDetector` parameters of
 `PutAnomalyDetectorInput`

Instead, specify the single metric anomaly detector attributes as part of the property
 `SingleMetricAnomalyDetector`.


Type: [SingleMetricAnomalyDetector](API_SingleMetricAnomalyDetector.md "API_SingleMetricAnomalyDetector.md") object


Required: No




**Stat** 



*This parameter has been deprecated.*



The statistic to use for the metric and the anomaly detection model.


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




**LimitExceededException** 


The operation exceeded one or more limits.


HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAnomalyDetector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAnomalyDetector")
