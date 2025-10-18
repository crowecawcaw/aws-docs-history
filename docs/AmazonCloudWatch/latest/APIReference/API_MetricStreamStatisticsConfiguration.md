# MetricStreamStatisticsConfiguration

By default, a metric stream always sends the `MAX`, `MIN`,
 `SUM`, and `SAMPLECOUNT` statistics for each metric that is
 streamed. This structure contains information for one metric that includes additional
 statistics in the stream. For more information about statistics, see CloudWatch,
 listed in [CloudWatch statistics definitions](../monitoring/Statistics-definitions.md "../monitoring/Statistics-definitions.md").


## Contents





**AdditionalStatistics** 


The list of additional statistics that are to be streamed for the metrics listed in
 the `IncludeMetrics` array in this structure. This list can include as many
 as 20 statistics.


If the `OutputFormat` for the stream is `opentelemetry1.0` or
 `opentelemetry0.7`, the only valid values are
 `p*??*` percentile statistics such as
 `p90`, `p99` and so on.


If the `OutputFormat` for the stream is `json`, the valid values
 include the abbreviations for all of the statistics listed in [CloudWatch statistics definitions](../monitoring/Statistics-definitions.md "../monitoring/Statistics-definitions.md"). For example, this includes
 `tm98,` 
`wm90`, `PR(:300)`, and so on.


Type: Array of strings


Required: Yes




**IncludeMetrics** 


An array of metric name and namespace pairs that stream the additional statistics
 listed in the value of the `AdditionalStatistics` parameter. There can be as
 many as 100 pairs in the array.


All metrics that match the combination of metric name and namespace will be streamed
 with the additional statistics, no matter their dimensions.


Type: Array of [MetricStreamStatisticsMetric](API_MetricStreamStatisticsMetric.md "API_MetricStreamStatisticsMetric.md") objects


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamStatisticsConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamStatisticsConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamStatisticsConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamStatisticsConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamStatisticsConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamStatisticsConfiguration")
