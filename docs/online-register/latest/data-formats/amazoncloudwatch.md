

# Data retrieval APIs for Amazon CloudWatch
<a name="amazoncloudwatch"></a>

Amazon CloudWatch provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cloudwatch-BatchGetServiceLevelIndicatorReport"></a>[BatchGetServiceLevelIndicatorReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Batch get service level indicator report | Read | 
| <a name="cloudwatch-BatchGetServiceLevelObjectiveBudgetReport"></a>[BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Batch retrieve a service level objective budget report | Read | 
| <a name="cloudwatch-DescribeAlarmHistory"></a>[DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html) | Retrieve the history for the specified alarm | Read | 
| <a name="cloudwatch-DescribeAlarms"></a>[DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) | Describe all alarms, currently owned by the user's account | Read | 
| <a name="cloudwatch-DescribeAlarmsForMetric"></a>[DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html) | Describe all alarms configured on the specified metric, currently owned by the user's account | Read | 
| <a name="cloudwatch-DescribeAnomalyDetectors"></a>[DescribeAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAnomalyDetectors.html) | List the anomaly detection models that you have created in your account | Read | 
| <a name="cloudwatch-DescribeInsightRules"></a>[DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html) | Describe all insight rules, currently owned by the user's account | Read | 
| <a name="cloudwatch-GenerateQuery"></a>[GenerateQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-query-assist.html) | Generate a Metrics Insights or Logs Insights query string from a natural language prompt | Read | 
| <a name="cloudwatch-GenerateQueryResultsSummary"></a>[GenerateQueryResultsSummary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) | Generate a summary of CloudWatch LogInsights query results in natural language using generative AI | Read | 
| <a name="cloudwatch-GetAlarmMuteRule"></a>[GetAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetAlarmMuteRule.html) | Get an alarm mute rule | Read | 
| <a name="cloudwatch-GetDashboard"></a>[GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html) | Display the details of the CloudWatch dashboard you specify | Read | 
| <a name="cloudwatch-GetDataset"></a>[GetDataset](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDataset.html) | Get a dataset | Read | 
| <a name="cloudwatch-GetInsightRuleReport"></a>[GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) | Return the top-N report of unique contributors over a time range for a given insight rule | Read | 
| <a name="cloudwatch-GetMetricData"></a>[GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) | Retrieve batch amounts of CloudWatch classic metric data and perform metric math on retrieved data; and grants permission to retrieve OTLP metric data using PromQL | Read | 
| <a name="cloudwatch-GetMetricStatistics"></a>[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) | Retrieve statistics for the specified metric | Read | 
| <a name="cloudwatch-GetMetricStream"></a>[GetMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html) | Return the details of a CloudWatch metric stream | Read | 
| <a name="cloudwatch-GetMetricWidgetImage"></a>[GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html) | Retrieve snapshots of metric widgets | Read | 
| <a name="cloudwatch-GetOTelEnrichment"></a>[GetOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve the status of OTel Enrichment of vended metrics for PromQL querying | Read | 
| <a name="cloudwatch-GetService"></a>[GetService](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve information about a service | Read | 
| <a name="cloudwatch-GetServiceData"></a>[GetServiceData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve service data | Read | 
| <a name="cloudwatch-GetServiceLevelObjective"></a>[GetServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve information about service level objective | Read | 
| <a name="cloudwatch-GetTopologyDiscoveryStatus"></a>[GetTopologyDiscoveryStatus](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve a CloudWatch topology discovery status | Read | 
| <a name="cloudwatch-GetTopologyMap"></a>[GetTopologyMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve a CloudWatch topology map | Read | 
| <a name="cloudwatch-ListAlarmMuteRules"></a>[ListAlarmMuteRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html) | Retrieve a list of alarm mute rules owned by the user's account | List | 
| <a name="cloudwatch-ListDashboards"></a>[ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html) | Return a list of all CloudWatch dashboards in your account | List | 
| <a name="cloudwatch-ListEntitiesForMetric"></a>[ListEntitiesForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve all the entities that are emitting a given metric | List | 
| <a name="cloudwatch-ListManagedInsightRules"></a>[ListManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListManagedInsightRules.html) | List available managed Insight Rules for a given Resource ARN | Read | 
| <a name="cloudwatch-ListMetricStreams"></a>[ListMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html) | Return a list of all CloudWatch metric streams in your account | List | 
| <a name="cloudwatch-ListMetrics"></a>[ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) | Retrieve a list of valid metrics stored for the AWS account owner | List | 
| <a name="cloudwatch-ListServiceLevelObjectives"></a>[ListServiceLevelObjectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | List service level objectives | List | 
| <a name="cloudwatch-ListServices"></a>[ListServices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | List services | List | 
| <a name="cloudwatch-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html) | List tags for an Amazon CloudWatch resource | List | 