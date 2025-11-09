# Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus

resources

Amazon Managed Service for Prometheus vends usage metrics to CloudWatch. These metrics provide visibility about your
workspace utilization. The vended metrics can be found in the `AWS/Usage`
and `AWS/Prometheus` namespaces in CloudWatch. These metrics are available in CloudWatch
for no charge. For more information about usage metrics, see [CloudWatch usage metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md").

| CloudWatch metric name                | Resource name                           | CloudWatch namespace | Description                                                                                                                                                                                                                                                    |
| ------------------------------------- | --------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ResourceCount\*                       | CreateAlertManagerAlertsTPS             | `AWS/Usage`          | The maximum number of `CreateAlertManagerAlerts` API<br>operations per second, per workspace                                                                                                                                                                   |
| ResourceCount\*                       | DeleteAlertManagerSilencesTPS           | `AWS/Usage`          | The maximum number of `DeleteAlertManagerSilences` API<br>operations per second, per workspace                                                                                                                                                                 |
| ResourceCount\*                       | GetAlertManagerSilenceTPS               | `AWS/Usage`          | The maximum number of `GetAlertManagerSilence` API<br>operations per second, per workspace                                                                                                                                                                     |
| ResourceCount\*                       | GetAlertManagerStatusTPS                | `AWS/Usage`          | The maximum number of `GetAlertManagerStatus` API<br>operations per second, per workspace                                                                                                                                                                      |
| ResourceCount\*                       | GetLabelsTPS                            | `AWS/Usage`          | The maximum number of `GetLabels` API operations per<br>second, per workspace                                                                                                                                                                                  |
| ResourceCount\*                       | GetMetricMetadataTPS                    | `AWS/Usage`          | The maximum number of `GetMetricMetadata` API<br>operations per second, per workspace                                                                                                                                                                          |
| ResourceCount\*                       | GetSeriesTPS                            | `AWS/Usage`          | The maximum number of `GetSeries` API operations per<br>second, per workspace                                                                                                                                                                                  |
| ResourceCount                         | InhibitionRulesInAlertManagerDefinition | `AWS/Usage`          | The maximum number of inhibition rules in alert manager definition<br>file.                                                                                                                                                                                    |
| ResourceCount\*                       | ListAlertManagerAlertGroupInfosTPS      | `AWS/Usage`          | The maximum number of `ListAlertManagerAlertGroupInfos`<br>API operations per second, per workspace                                                                                                                                                            |
| ResourceCount\*                       | ListAlertManagerAlertGroupsTPS          | `AWS/Usage`          | The maximum number of `ListAlertManagerAlertGroups` API<br>operations per second, per workspace                                                                                                                                                                |
| ResourceCount\*                       | ListAlertManagerAlertsTPS               | `AWS/Usage`          | The maximum number of `ListAlertManagerAlerts` API<br>operations per second, per workspace                                                                                                                                                                     |
| ResourceCount\*                       | ListAlertManagerReceiversTPS            | `AWS/Usage`          | The maximum number of `ListAlertManagerReceivers` API<br>operations per second, per workspace                                                                                                                                                                  |
| ResourceCount\*                       | ListAlertManagerSilencesTPS             | `AWS/Usage`          | The maximum number of `ListAlertManagerSilences` API<br>operations per second, per workspace                                                                                                                                                                   |
| ResourceCount\*                       | ListAlertsTPS                           | `AWS/Usage`          | The maximum number of `ListAlerts` API operations per<br>second, per workspace                                                                                                                                                                                 |
| ResourceCount\*                       | ListRulesTPS                            | `AWS/Usage`          | The maximum number of `ListRules` API operations per<br>second, per workspace                                                                                                                                                                                  |
| ResourceCount\*                       | PutAlertManagerSilencesTPS              | `AWS/Usage`          | The maximum number of `PutAlertManagerSilences` API<br>operations per second, per workspace                                                                                                                                                                    |
| ResourceCount                         | HAReplicaGroupCount                     | `AWS/Usage`          | Number of high availability replica groups                                                                                                                                                                                                                     |
| ResourceCount\*                       | QueryMetricsTPS                         | `AWS/Usage`          | Query operations per second                                                                                                                                                                                                                                    |
| ResourceCount\*                       | RemoteWriteTPS                          | `AWS/Usage`          | Remote write operations per second                                                                                                                                                                                                                             |
| ResourceCount                         | ActiveAlerts                            | `AWS/Usage`          | Number of active alerts per workspace<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                      |
| ResourceCount                         | ActiveSeries                            | `AWS/Usage`          | Number of active series per workspace<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                      |
| ResourceCount                         | AlertAggregationGroupSize               | `AWS/Usage`          | The maximum size of an alert aggregation group in alert manager<br>definition file. Each label value combination of<br>`group_by` would create an aggregation group.                                                                                           |
| ResourceCount                         | AlertManagerDefinitionSizeBytes         | `AWS/Usage`          | The maximum size of an alert manager definition file, in<br>bytes.                                                                                                                                                                                             |
| ResourceCount                         | AllSilences                             | `AWS/Usage`          | Maximum number of silences, including expired, active, and pending<br>silences, per workspace.                                                                                                                                                                 |
| ResourceCount                         | AllAlerts                               | `AWS/Usage`          | Number of alerts in any state per workspace.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                               |
| ResourceCount                         | IngestionRate                           | `AWS/Usage`          | Sample ingestion rate<br>Units: Count per second<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                           |
| ResourceCount                         | RuleEvaluationInterval                  | `AWS/Usage`          | The minimum rule evaluation interval                                                                                                                                                                                                                           |
| ResourceCount                         | RuleGroupNamespaceDefinitionSizeBytes   | `AWS/Usage`          | The maximum size of a rule group namespace definition file, in<br>bytes.                                                                                                                                                                                       |
| ResourceCount                         | TemplatesInAlertManagerDefinition       | `AWS/Usage`          | The maximum number of templates in the alert manager definition<br>file.                                                                                                                                                                                       |
| ResourceCount                         | WorkspaceCount                          | `AWS/Usage`          | The maximum number of workspaces per Region, per accountc.                                                                                                                                                                                                     |
| ResourceCount                         | SizeOfAlerts                            | `AWS/Usage`          | Total size of all alerts in the workspace, in bytes<br>Units: bytes<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                        |
| ResourceCount                         | SuppressedAlerts                        | `AWS/Usage`          | Number of alerts in suppressed state per workspace. An alert can<br>be suppressed by a silence or inhibition.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                              |
| ResourceCount                         | UnprocessedAlerts                       | `AWS/Usage`          | Number of alerts in unprocessed state per workspace. An alert is<br>in unprocessed state once it is received by AlertManager, but is<br>waiting for the next aggregation group evaluation.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum |
| ResourceCount                         | AllAlerts                               | `AWS/Usage`          | Number of alerts in any state per workspace.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                               |
| ResourceCount                         | AllRules                                | `AWS/Usage`          | Number of rules in any state per workspace.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                |
| ActiveSeriesPerLabelSet               | -                                       | `AWS/Prometheus`     | The current active series usage for each user-defined label<br>set<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                         |
| ActiveSeriesLimitPerLabelSet          | -                                       | `AWS/Prometheus`     | The current active series limit value for each user-defined label<br>set<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                   |
| AlertManagerAlertsReceived            | -                                       | `AWS/Prometheus`     | Total successful alerts received by alert manager<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                          |
| AlertManagerNotificationsFailed       | -                                       | `AWS/Prometheus`     | Number of failed alert deliveries<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                          |
| AlertManagerNotificationsThrottled    | -                                       | `AWS/Prometheus`     | Number of throttled alerts<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                                 |
| AnomalyDetectors                      | WorkspaceId                             | `AWS/Prometheus`     | Total number of anomaly detectors for a given workspace<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                    |
| AnomalyDetectorEvaluations            | WorkspaceId, AnomalyDetectorId          | `AWS/Prometheus`     | Total number of anomaly detector evaluations<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                               |
| AnomalyDetectorEvaluationFailures     | WorkspaceId, AnomalyDetectorId          | `AWS/Prometheus`     | Number of anomaly detector failures in the interval<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                        |
| AnomalyDetectorLastEvaluationDuration | WorkspaceId, AnomalyDetectorId          | `AWS/Prometheus`     | Duration of an anomaly detector’s last evaluation<br>Units: Seconds<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                        |
| AnomalyDetectorMissedEvaluations      | WorkspaceId, AnomalyDetectorId          | `AWS/Prometheus`     | Number of missed anomaly detector evaluations in the<br>interval<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                           |
| DiscardedSamples\*\*                  | -                                       | `AWS/Prometheus`     | Number of discarded samples by reason<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                      |
| DiscardedSamplesPerLabelSet           | -                                       | `AWS/Prometheus`     | The count of discarded samples for each user-defined label<br>set<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                          |
| IngestionRatePerLabelSet              | -                                       | `AWS/Prometheus`     | The ingestion rate for each user-defined label set<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                         |
| QuerySamplesProcessed                 | -                                       | `AWS/Prometheus`     | Number of query samples processed<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                          |
| RuleEvaluations                       | -                                       | `AWS/Prometheus`     | Total number of rule evaluations<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                                           |
| RuleEvaluationFailures                | -                                       | `AWS/Prometheus`     | Number of rule evaluation failures in the interval<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                         |
| RuleGroupIterationsMissed             | -                                       | `AWS/Prometheus`     | Number of Rule Group iterations missed in the interval.<br>Units: Count<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                    |
| RuleGroupLastEvaluationDuration       | -                                       | `AWS/Prometheus`     | Duration of a rule group's last evaluation.<br>Units: seconds<br>Valid Statistics: Average, Minimum, Maximum, Sum                                                                                                                                              |

\*TPS metrics are generated every minute and are a
per-second average over that minute. Short burst periods will not be captured in the TPS
metrics.

\*\*Some of the reasons that cause samples to be discarded
are as follows.

| Reason                      | Meaning                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| greater_than_max_sample_age | Discarding samples which are older than one hour.                                                       |
| new-value-for-timestamp     | Duplicate samples are sent with the same timestamp as the previous<br>sample but with different values. |
| per_labelset_series_limit   | User has hit the total number of active series per label set<br>limit.                                  |
| per_metric_series_limit     | User has hit the active series per metric limit.                                                        |
| per_user_series_limit       | User has hit the total number of active series limit.                                                   |
| rate_limited                | Ingestion rate limited.                                                                                 |
| sample-out-of-order         | Samples are sent out of order and cannot be processed.                                                  |
| label_value_too_long        | Label value is longer than allowed character limit.                                                     |
| max_label_names_per_series  | User has hit the label names per metric.                                                                |
| missing_metric_name         | Metric name is not provided.                                                                            |
| metric_name_invalid         | Invalid metric name provided.                                                                           |
| label_invalid               | Invalid label provided.                                                                                 |
| duplicate_label_names       | Duplicate label names provided.                                                                         |

###### Note

A metric not existing or missing is the same as the value of that metric being 0.

###### Note

`RuleGroupIterationsMissed`, `RuleEvaluations`,
`RuleEvaluationFailures`, and
`RuleGroupLastEvaluationDuration` have the `RuleGroup`
dimension of the following structure:

`RuleGroupNamespace`;`RuleGroup`

## Setting a CloudWatch alarm on Prometheus vended

metrics

You can monitor usage of Prometheus resources using CloudWatch alarms.

###### To set an alarm on the number of **ActiveSeries** in

Prometheus

1. Choose the **Graphed metrics** tab and scroll down to the
   **ActiveSeries** label.

In the **Graphed metrics** view, only the metrics
currently being ingested will appear. 2. Choose the **notification** icon in the
**Actions** column. 3. In **Specify metric and conditions**, enter the threshold
condition in the **Conditions value** field and choose
**Next**. 4. In **Configure actions**, select an existing SNS topic or
create a new SNS topic to send the notification to. 5. In **Add name and description**, add the name of the
alarm and an optional description. 6. Choose **Create alarm**.
