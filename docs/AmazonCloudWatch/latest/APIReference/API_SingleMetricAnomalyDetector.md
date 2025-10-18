# SingleMetricAnomalyDetector

Designates the CloudWatch metric and statistic that provides the time series the
 anomaly detector uses as input. If you have enabled unified cross-account observability,
 and this account is a monitoring account, the metric can be in the same account or a
 source account.


## Contents





**AccountId** 


If the CloudWatch metric that provides the time series that the anomaly
 detector uses as input is in another account, specify that account ID here. If you omit
 this parameter, the current account is used.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Dimensions** 


The metric dimensions to create the anomaly detection model for.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**MetricName** 


The name of the metric to create the anomaly detection model for.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Namespace** 


The namespace of the metric to create the anomaly detection model for.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**Stat** 


The statistic to use for the metric and anomaly detection model.


Type: String


Length Constraints: Maximum length of 50.


Pattern: `(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/SingleMetricAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/SingleMetricAnomalyDetector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/SingleMetricAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/SingleMetricAnomalyDetector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/SingleMetricAnomalyDetector "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/SingleMetricAnomalyDetector")
