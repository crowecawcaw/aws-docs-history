# Datapoint

Encapsulates the statistical data that CloudWatch computes from metric
 data.


## Contents





**Average** 


The average of the metric values that correspond to the data point.


Type: Double


Required: No




**ExtendedStatistics** 


The percentile statistic for the data point.


Type: String to double map


Required: No




**Maximum** 


The maximum metric value for the data point.


Type: Double


Required: No




**Minimum** 


The minimum metric value for the data point.


Type: Double


Required: No




**SampleCount** 


The number of metric values that contributed to the aggregate value of this data
 point.


Type: Double


Required: No




**Sum** 


The sum of the metric values for the data point.


Type: Double


Required: No




**Timestamp** 


The time stamp used for the data point.


Type: Timestamp


Required: No




**Unit** 


The standard unit for the data point.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Datapoint "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Datapoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Datapoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Datapoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Datapoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Datapoint")
