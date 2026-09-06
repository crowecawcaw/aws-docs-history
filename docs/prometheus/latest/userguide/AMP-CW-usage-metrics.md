

# Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus resources
<a name="AMP-CW-usage-metrics"></a>

Amazon Managed Service for Prometheus vends usage metrics to CloudWatch. These metrics provide visibility about your workspace utilization. The vended metrics can be found in the `AWS/Usage` and `AWS/Prometheus` namespaces in CloudWatch. These metrics are available in CloudWatch for no charge. For more information about usage metrics, see [CloudWatch usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html).


| CloudWatch metric name | Resource name | CloudWatch namespace | Description | 
| --- | --- | --- | --- | 
| ResourceCount\* | CreateAlertManagerAlertsTPS | `AWS/Usage` | The maximum number of `CreateAlertManagerAlerts` API operations per second, per workspace | 
| ResourceCount\* | DeleteAlertManagerSilencesTPS | `AWS/Usage` | The maximum number of `DeleteAlertManagerSilences` API operations per second, per workspace | 
| ResourceCount\* | GetAlertManagerSilenceTPS | `AWS/Usage` | The maximum number of `GetAlertManagerSilence` API operations per second, per workspace | 
| ResourceCount\* | GetAlertManagerStatusTPS | `AWS/Usage` | The maximum number of `GetAlertManagerStatus` API operations per second, per workspace | 
| ResourceCount\* | GetLabelsTPS | `AWS/Usage` | The maximum number of `GetLabels` API operations per second, per workspace | 
| ResourceCount\* | GetMetricMetadataTPS | `AWS/Usage` | The maximum number of `GetMetricMetadata` API operations per second, per workspace | 
| ResourceCount\* | GetSeriesTPS | `AWS/Usage` | The maximum number of `GetSeries` API operations per second, per workspace | 
| ResourceCount | InhibitionRulesInAlertManagerDefinition | `AWS/Usage` | The maximum number of inhibition rules in alert manager definition file. | 
| ResourceCount\* | ListAlertManagerAlertGroupInfosTPS | `AWS/Usage` | The maximum number of `ListAlertManagerAlertGroupInfos` API operations per second, per workspace | 
| ResourceCount\* | ListAlertManagerAlertGroupsTPS | `AWS/Usage` | The maximum number of `ListAlertManagerAlertGroups` API operations per second, per workspace | 
| ResourceCount\* | ListAlertManagerAlertsTPS | `AWS/Usage` | The maximum number of `ListAlertManagerAlerts` API operations per second, per workspace | 
| ResourceCount\* | ListAlertManagerReceiversTPS | `AWS/Usage` | The maximum number of `ListAlertManagerReceivers` API operations per second, per workspace | 
| ResourceCount\* | ListAlertManagerSilencesTPS | `AWS/Usage` | The maximum number of `ListAlertManagerSilences` API operations per second, per workspace | 
| ResourceCount\* | ListAlertsTPS | `AWS/Usage` | The maximum number of `ListAlerts` API operations per second, per workspace | 
| ResourceCount\* | ListRulesTPS | `AWS/Usage` | The maximum number of `ListRules` API operations per second, per workspace | 
| ResourceCount\* | PutAlertManagerSilencesTPS | `AWS/Usage` | The maximum number of `PutAlertManagerSilences` API operations per second, per workspace | 
| ResourceCount | HAReplicaGroupCount | `AWS/Usage` | Number of high availability replica groups | 
| ResourceCount\* | QueryMetricsTPS | `AWS/Usage` | Query operations per second | 
| ResourceCount\* | RemoteWriteTPS | `AWS/Usage` | Remote write operations per second | 
| ResourceCount | ActiveAlerts | `AWS/Usage` | Number of active alerts per workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | ActiveSeries | `AWS/Usage` | Number of active series per workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | AlertAggregationGroupSize | `AWS/Usage` | The maximum size of an alert aggregation group in alert manager definition file. Each label value combination of `group_by` would create an aggregation group. | 
| ResourceCount | AlertManagerDefinitionSizeBytes | `AWS/Usage` | The maximum size of an alert manager definition file, in bytes. | 
| ResourceCount | AllSilences | `AWS/Usage` | Maximum number of silences, including expired, active, and pending silences, per workspace. | 
| ResourceCount | IngestionRate | `AWS/Usage` | Sample ingestion rate<br />Units: Count per second<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | RuleEvaluationInterval | `AWS/Usage` | The minimum rule evaluation interval | 
| ResourceCount | RuleGroupNamespaceDefinitionSizeBytes | `AWS/Usage` | The maximum size of a rule group namespace definition file, in bytes. | 
| ResourceCount | TemplatesInAlertManagerDefinition | `AWS/Usage` | The maximum number of templates in the alert manager definition file. | 
| ResourceCount | WorkspaceCount | `AWS/Usage` | The maximum number of workspaces per Region, per accountc. | 
| ResourceCount | SizeOfAlerts | `AWS/Usage` | Total size of all alerts in the workspace, in bytes<br />Units: Bytes<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | SuppressedAlerts | `AWS/Usage` | Number of alerts in suppressed state per workspace. An alert can be suppressed by a silence or inhibition.<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | UnprocessedAlerts | `AWS/Usage` | Number of alerts in unprocessed state per workspace. An alert is in unprocessed state once it is received by AlertManager, but is waiting for the next aggregation group evaluation.<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | AllAlerts | `AWS/Usage` | Number of alerts in any state per workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | AllRules | `AWS/Usage` | Number of rules in any state per workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | NativeHistogramActiveSeries | `AWS/Usage` | The number of unique native histogram active series per workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| ResourceCount | NativeHistogramIngestionRate | `AWS/Usage` | Native histogram sample ingestion rate per workspace per second<br />Units: Count per second<br />Valid Statistics: Average, Minimum, Maximum | 
| ActiveSeriesPerLabelSet |  - | `AWS/Prometheus` | The current active series usage for each user-defined label set<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| ActiveSeriesLimitPerLabelSet |  - | `AWS/Prometheus` | The current active series limit value for each user-defined label set<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AlertManagerAlertsReceived |  - | `AWS/Prometheus` | Total successful alerts received by alert manager<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AlertManagerNotificationsFailed |  - | `AWS/Prometheus` | Number of failed alert deliveries<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AlertManagerNotificationsThrottled |  - | `AWS/Prometheus` | Number of throttled alerts<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AnomalyDetectors | WorkspaceId | `AWS/Prometheus` | Total number of anomaly detectors for a given workspace<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum | 
| AnomalyDetectorEvaluations | WorkspaceId, AnomalyDetectorId | `AWS/Prometheus` | Total number of anomaly detector evaluations<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AnomalyDetectorEvaluationFailures | WorkspaceId, AnomalyDetectorId | `AWS/Prometheus` | Number of anomaly detector failures in the interval<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AnomalyDetectorLastEvaluationDuration | WorkspaceId, AnomalyDetectorId | `AWS/Prometheus` | Duration of an anomaly detector’s last evaluation<br />Units: Seconds<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| AnomalyDetectorMissedEvaluations | WorkspaceId, AnomalyDetectorId | `AWS/Prometheus` | Number of missed anomaly detector evaluations in the interval<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| DiscardedSamples\*\* |  - | `AWS/Prometheus` | Number of discarded samples by reason<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| DiscardedSeries\*\* |  - | `AWS/Prometheus` | Number of series that contain a discarded sample by reason<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| DiscardedSamplesPerLabelSet |  - | `AWS/Prometheus` | The count of discarded samples for each user-defined label set<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| DiscardedSeriesPerLabelSet |  - | `AWS/Prometheus` | The count of series that contain a discarded sample for each user-defined label set<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| IngestionRatePerLabelSet |  - | `AWS/Prometheus` | The ingestion rate for each user-defined label set<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| NativeHistogramIngestedBucketsRate |  - | `AWS/Prometheus` | Rate of populated buckets received per second across all native histogram samples. Excludes rejected buckets.<br />Units: Count per second<br />Valid Statistics: Average, Minimum, Maximum | 
| NativeHistogramReducedResolutionCount |  - | `AWS/Prometheus` | Count of native histogram samples with automatically reduced bucket resolution. Resolution is reduced when a sample exceeds the maximum bucket count limit.<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| OutOfOrderIngestionRate |  - | `AWS/Prometheus` | Out-of-order sample ingestion rate<br />Units: Count per second<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| OutOfOrderSampleAge\*\*\* |  - | `AWS/Prometheus` | The difference between an out-of-order sample's timestamp and its ingestion time, which indicates how old the sample is when ingested.<br />Units: Seconds<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| QuerySamplesProcessed |  - | `AWS/Prometheus` | Number of query samples processed<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| RuleEvaluations |  - | `AWS/Prometheus` | Total number of rule evaluations<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| RuleEvaluationFailures |  - | `AWS/Prometheus` | Number of rule evaluation failures in the interval<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| RuleGroupIterationsMissed |  - | `AWS/Prometheus` | Number of Rule Group iterations missed in the interval.<br />Units: Count<br />Valid Statistics: Average, Minimum, Maximum, Sum | 
| RuleGroupLastEvaluationDuration |  - | `AWS/Prometheus` | Duration of a rule group's last evaluation.<br />Units: Seconds<br />Valid Statistics: Average, Minimum, Maximum, Sum | 

\*TPS metrics are generated every minute and are a per-second average over that minute. Short burst periods will not be captured in the TPS metrics.

\*\*Some of the reasons that cause samples to be discarded are as follows. Not all reasons below appear in the DiscardedSeries metric.


|  Reason  |  Meaning  | 
| --- | --- | 
| greater\_than\_max\_sample\_age | Discarding samples which are older than one hour. | 
| new-value-for-timestamp | Duplicate samples are sent with the same timestamp as the previous sample but with different values. | 
| per\_labelset\_series\_limit | User has hit the total number of active series per label set limit. | 
| per\_metric\_series\_limit | User has hit the active series per metric limit. | 
| per\_user\_series\_limit | User has hit the total number of active series limit. | 
| rate\_limited | Ingestion rate limited. | 
| sample-out-of-order | Samples are sent out of order and cannot be processed. | 
| sample-too-old | Sample is older than the configured out-of-order time window and cannot be processed. | 
| out-of-order-rate-limit | Out-of-order ingestion rate limit was reached and the sample cannot be processed. For more information, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md). | 
| label\_value\_too\_long | Label value is longer than allowed character limit. | 
| max\_label\_names\_per\_series | User has hit the label names per metric. | 
| missing\_metric\_name | Metric name is not provided. | 
| metric\_name\_invalid | Invalid metric name provided. | 
| label\_invalid | Invalid label provided. | 
| duplicate\_label\_names | Duplicate label names provided. | 
| native\_histogram\_sample\_size\_bytes\_exceeded | Native histogram sample exceeds the maximum allowed sample size in bytes. | 
| native\_histogram\_invalid\_schema | Native histogram has an invalid schema value. Valid schemas range from -4 to 8. | 
| native\_histogram\_invalid | Native histogram fails validation (for example, negative bucket counts, mismatched bucket counts, or malformed bucket spans). | 
| native\_histogram\_buckets\_exceeded | Native histogram exceeds the maximum bucket count limit and resolution cannot be automatically reduced. | 
| native\_histogram\_rate\_limited | Native histogram sample was rejected because the native histogram ingestion rate limit was reached. | 
| per\_user\_native\_histogram\_series\_limit | User has hit the native histogram active series limit per workspace. | 

\*\*\*The `OutOfOrderSampleAge` metric includes a `Percentile` dimension. You can use this metric to determine the appropriate out of order time window for your workspace. The valid values for the `Percentile` dimension are as follows.


|  Percentile  |  Description  | 
| --- | --- | 
| p50 | The 50th percentile age of out-of-order samples. | 
| p99 | The 99th percentile age of out-of-order samples. | 
| max | The maximum age of out-of-order samples. | 

**Note**  
A metric not existing or missing is the same as the value of that metric being 0.

**Note**  
`RuleGroupIterationsMissed`, `RuleEvaluations`, `RuleEvaluationFailures`, and `RuleGroupLastEvaluationDuration` have the `RuleGroup` dimension of the following structure:   
{{RuleGroupNamespace}};{{RuleGroup}}

## Setting a CloudWatch alarm on Prometheus vended metrics
<a name="AMP-CW-examples"></a>

You can monitor usage of Prometheus resources using CloudWatch alarms.

**To set an alarm on the number of **ActiveSeries** in Prometheus**

1. Choose the **Graphed metrics** tab and scroll down to the **ActiveSeries** label.

   In the **Graphed metrics** view, only the metrics currently being ingested will appear.

1. Choose the **notification ** icon in the **Actions** column.

1. In **Specify metric and conditions**, enter the threshold condition in the **Conditions value** field and choose **Next**.

1. In **Configure actions**, select an existing SNS topic or create a new SNS topic to send the notification to.

1. In **Add name and description**, add the name of the alarm and an optional description.

1. Choose **Create alarm**.