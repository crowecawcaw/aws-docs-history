# GetInsightRuleReport

This operation returns the time series data collected by a Contributor Insights rule.
 The data includes the identity and number of contributors to the log group.

You can also optionally return one or more statistics about each data point in the
 time series. These statistics can include the following:


* `UniqueContributors` -- the number of unique contributors for each
 data point.
* `MaxContributorValue` -- the value of the top contributor for each
 data point. The identity of the contributor might change for each data point in
 the graph.


If this rule aggregates by COUNT, the top contributor for each data point is
 the contributor with the most occurrences in that period. If the rule aggregates
 by SUM, the top contributor is the contributor with the highest sum in the log
 field specified by the rule's `Value`, during that period.
* `SampleCount` -- the number of data points matched by the
 rule.
* `Sum` -- the sum of the values from all contributors during the
 time period represented by that data point.
* `Minimum` -- the minimum value from a single observation during the
 time period represented by that data point.
* `Maximum` -- the maximum value from a single observation during the
 time period represented by that data point.
* `Average` -- the average value from all contributors during the
 time period represented by that data point.

## Request Parameters





**EndTime** 


The end time of the data to use in the report. When used in a raw HTTP Query API, it
 is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example,
 `2019-07-01T23:59:59`.


Type: Timestamp


Required: Yes




**MaxContributorCount** 


The maximum number of contributors to include in the report. The range is 1 to 100. If
 you omit this, the default of 10 is used.


Type: Integer


Required: No




**Metrics** 


Specifies which metrics to use for aggregation of contributor values for the report.
 You can specify one or more of the following metrics:



* `UniqueContributors` -- the number of unique contributors for each
 data point.
* `MaxContributorValue` -- the value of the top contributor for each
 data point. The identity of the contributor might change for each data point in
 the graph.


If this rule aggregates by COUNT, the top contributor for each data point is
 the contributor with the most occurrences in that period. If the rule aggregates
 by SUM, the top contributor is the contributor with the highest sum in the log
 field specified by the rule's `Value`, during that period.
* `SampleCount` -- the number of data points matched by the
 rule.
* `Sum` -- the sum of the values from all contributors during the
 time period represented by that data point.
* `Minimum` -- the minimum value from a single observation during the
 time period represented by that data point.
* `Maximum` -- the maximum value from a single observation during the
 time period represented by that data point.
* `Average` -- the average value from all contributors during the
 time period represented by that data point.

Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `[\x20-\x7E]+`



Required: No




**OrderBy** 


Determines what statistic to use to rank the contributors. Valid values are
 `Sum` and `Maximum`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `[\x20-\x7E]+`



Required: No




**Period** 


The period, in seconds, to use for the statistics in the
 `InsightRuleMetricDatapoint` results.


Type: Integer


Valid Range: Minimum value of 1.


Required: Yes




**RuleName** 


The name of the rule that you want to see data from.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[\x20-\x7E]+`



Required: Yes




**StartTime** 


The start time of the data to use in the report. When used in a raw HTTP Query API, it
 is formatted as `yyyy-MM-dd'T'HH:mm:ss`. For example,
 `2019-07-01T23:59:59`.


Type: Timestamp


Required: Yes




## Response Elements


The following elements are returned by the service.





**AggregateValue** 


The sum of the values from all individual contributors that match the rule.


Type: Double




**AggregationStatistic** 


Specifies whether this rule aggregates contributor data by COUNT or SUM.


Type: String




**ApproximateUniqueCount** 


An approximate count of the unique contributors found by this rule in this time
 period.


Type: Long




**Contributors** 


An array of the unique contributors found by this rule in this time period. If the
 rule contains multiple keys, each combination of values for the keys counts as a unique
 contributor.


Type: Array of [InsightRuleContributor](API_InsightRuleContributor.md "API_InsightRuleContributor.md") objects




**KeyLabels** 


An array of the strings used as the keys for this rule. The keys are the dimensions
 used to classify contributors. If the rule contains more than one key, then each unique
 combination of values for the keys is counted as a unique contributor.


Type: Array of strings




**MetricDatapoints** 


A time series of metric data points that matches the time period in the rule
 request.


Type: Array of [InsightRuleMetricDatapoint](API_InsightRuleMetricDatapoint.md "API_InsightRuleMetricDatapoint.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetInsightRuleReport")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetInsightRuleReport "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetInsightRuleReport")
