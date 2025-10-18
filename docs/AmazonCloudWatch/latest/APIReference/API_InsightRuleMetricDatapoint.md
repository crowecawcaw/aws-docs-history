# InsightRuleMetricDatapoint

One data point from the metric time series returned in a Contributor Insights rule
 report.

For more information, see [GetInsightRuleReport](API_GetInsightRuleReport.md "API_GetInsightRuleReport.md").


## Contents





**Timestamp** 


The timestamp of the data point.


Type: Timestamp


Required: Yes




**Average** 


The average value from all contributors during the time period represented by that
 data point.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**MaxContributorValue** 


The maximum value provided by one contributor during this timestamp. Each timestamp is
 evaluated separately, so the identity of the max contributor could be different for each
 timestamp.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**Maximum** 


The maximum value from a single occurence from a single contributor during the time
 period represented by that data point.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**Minimum** 


The minimum value from a single contributor during the time period represented by that
 data point.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**SampleCount** 


The number of occurrences that matched the rule during this data point.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**Sum** 


The sum of the values from all contributors during the time period represented by that
 data point.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




**UniqueContributors** 


The number of unique contributors who published data during this timestamp.


This statistic is returned only if you included it in the `Metrics` array
 in your request.


Type: Double


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleMetricDatapoint "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleMetricDatapoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleMetricDatapoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleMetricDatapoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleMetricDatapoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleMetricDatapoint")
